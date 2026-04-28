# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_gateway_pds.client import Client as GatewayClientClient
from alibabacloud_pds20220301 import models as main_models
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
        self._product_id = 'pds'
        gateway_client = GatewayClientClient()
        self._spi = gateway_client
        self._disable_http_2 = True
        self._endpoint_rule = ''

    def add_group_member_with_options(
        self,
        request: main_models.AddGroupMemberRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddGroupMemberResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.group_id):
            body['group_id'] = request.group_id
        if not DaraCore.is_null(request.member_id):
            body['member_id'] = request.member_id
        if not DaraCore.is_null(request.member_type):
            body['member_type'] = request.member_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddGroupMember',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/group/add_member',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddGroupMemberResponse(),
            self.execute(params, req, runtime)
        )

    async def add_group_member_with_options_async(
        self,
        request: main_models.AddGroupMemberRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddGroupMemberResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.group_id):
            body['group_id'] = request.group_id
        if not DaraCore.is_null(request.member_id):
            body['member_id'] = request.member_id
        if not DaraCore.is_null(request.member_type):
            body['member_type'] = request.member_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddGroupMember',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/group/add_member',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddGroupMemberResponse(),
            await self.execute_async(params, req, runtime)
        )

    def add_group_member(
        self,
        request: main_models.AddGroupMemberRequest,
    ) -> main_models.AddGroupMemberResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.add_group_member_with_options(request, headers, runtime)

    async def add_group_member_async(
        self,
        request: main_models.AddGroupMemberRequest,
    ) -> main_models.AddGroupMemberResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.add_group_member_with_options_async(request, headers, runtime)

    def add_story_files_with_options(
        self,
        request: main_models.AddStoryFilesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddStoryFilesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.files):
            body['files'] = request.files
        if not DaraCore.is_null(request.story_id):
            body['story_id'] = request.story_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddStoryFiles',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/image/add_story_files',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddStoryFilesResponse(),
            self.execute(params, req, runtime)
        )

    async def add_story_files_with_options_async(
        self,
        request: main_models.AddStoryFilesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddStoryFilesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.files):
            body['files'] = request.files
        if not DaraCore.is_null(request.story_id):
            body['story_id'] = request.story_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddStoryFiles',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/image/add_story_files',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddStoryFilesResponse(),
            await self.execute_async(params, req, runtime)
        )

    def add_story_files(
        self,
        request: main_models.AddStoryFilesRequest,
    ) -> main_models.AddStoryFilesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.add_story_files_with_options(request, headers, runtime)

    async def add_story_files_async(
        self,
        request: main_models.AddStoryFilesRequest,
    ) -> main_models.AddStoryFilesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.add_story_files_with_options_async(request, headers, runtime)

    def assign_role_with_options(
        self,
        request: main_models.AssignRoleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AssignRoleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.identity):
            body['identity'] = request.identity
        if not DaraCore.is_null(request.manage_resource_id):
            body['manage_resource_id'] = request.manage_resource_id
        if not DaraCore.is_null(request.manage_resource_type):
            body['manage_resource_type'] = request.manage_resource_type
        if not DaraCore.is_null(request.role_id):
            body['role_id'] = request.role_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AssignRole',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/role/assign',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssignRoleResponse(),
            self.execute(params, req, runtime)
        )

    async def assign_role_with_options_async(
        self,
        request: main_models.AssignRoleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AssignRoleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.identity):
            body['identity'] = request.identity
        if not DaraCore.is_null(request.manage_resource_id):
            body['manage_resource_id'] = request.manage_resource_id
        if not DaraCore.is_null(request.manage_resource_type):
            body['manage_resource_type'] = request.manage_resource_type
        if not DaraCore.is_null(request.role_id):
            body['role_id'] = request.role_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AssignRole',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/role/assign',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssignRoleResponse(),
            await self.execute_async(params, req, runtime)
        )

    def assign_role(
        self,
        request: main_models.AssignRoleRequest,
    ) -> main_models.AssignRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.assign_role_with_options(request, headers, runtime)

    async def assign_role_async(
        self,
        request: main_models.AssignRoleRequest,
    ) -> main_models.AssignRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.assign_role_with_options_async(request, headers, runtime)

    def audit_log_export_with_options(
        self,
        request: main_models.AuditLogExportRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AuditLogExportResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.file_name):
            body['file_name'] = request.file_name
        if not DaraCore.is_null(request.language):
            body['language'] = request.language
        if not DaraCore.is_null(request.order_by):
            body['order_by'] = request.order_by
        if not DaraCore.is_null(request.query):
            body['query'] = request.query
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AuditLogExport',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/audit_log/export',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuditLogExportResponse(),
            self.execute(params, req, runtime)
        )

    async def audit_log_export_with_options_async(
        self,
        request: main_models.AuditLogExportRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AuditLogExportResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.file_name):
            body['file_name'] = request.file_name
        if not DaraCore.is_null(request.language):
            body['language'] = request.language
        if not DaraCore.is_null(request.order_by):
            body['order_by'] = request.order_by
        if not DaraCore.is_null(request.query):
            body['query'] = request.query
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AuditLogExport',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/audit_log/export',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuditLogExportResponse(),
            await self.execute_async(params, req, runtime)
        )

    def audit_log_export(
        self,
        request: main_models.AuditLogExportRequest,
    ) -> main_models.AuditLogExportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.audit_log_export_with_options(request, headers, runtime)

    async def audit_log_export_async(
        self,
        request: main_models.AuditLogExportRequest,
    ) -> main_models.AuditLogExportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.audit_log_export_with_options_async(request, headers, runtime)

    def authorize_with_options(
        self,
        tmp_req: main_models.AuthorizeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AuthorizeResponse:
        tmp_req.validate()
        request = main_models.AuthorizeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.scope):
            request.scope_shrink = Utils.array_to_string_with_specified_style(tmp_req.scope, 'scope', 'simple')
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['client_id'] = request.client_id
        if not DaraCore.is_null(request.hide_consent):
            query['hide_consent'] = request.hide_consent
        if not DaraCore.is_null(request.login_type):
            query['login_type'] = request.login_type
        if not DaraCore.is_null(request.redirect_uri):
            query['redirect_uri'] = request.redirect_uri
        if not DaraCore.is_null(request.response_type):
            query['response_type'] = request.response_type
        if not DaraCore.is_null(request.scope_shrink):
            query['scope'] = request.scope_shrink
        if not DaraCore.is_null(request.state):
            query['state'] = request.state
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Authorize',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/oauth/authorize',
            method = 'GET',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'binary'
        )
        return DaraCore.from_map(
            main_models.AuthorizeResponse(),
            self.execute(params, req, runtime)
        )

    async def authorize_with_options_async(
        self,
        tmp_req: main_models.AuthorizeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AuthorizeResponse:
        tmp_req.validate()
        request = main_models.AuthorizeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.scope):
            request.scope_shrink = Utils.array_to_string_with_specified_style(tmp_req.scope, 'scope', 'simple')
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['client_id'] = request.client_id
        if not DaraCore.is_null(request.hide_consent):
            query['hide_consent'] = request.hide_consent
        if not DaraCore.is_null(request.login_type):
            query['login_type'] = request.login_type
        if not DaraCore.is_null(request.redirect_uri):
            query['redirect_uri'] = request.redirect_uri
        if not DaraCore.is_null(request.response_type):
            query['response_type'] = request.response_type
        if not DaraCore.is_null(request.scope_shrink):
            query['scope'] = request.scope_shrink
        if not DaraCore.is_null(request.state):
            query['state'] = request.state
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Authorize',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/oauth/authorize',
            method = 'GET',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'binary'
        )
        return DaraCore.from_map(
            main_models.AuthorizeResponse(),
            await self.execute_async(params, req, runtime)
        )

    def authorize(
        self,
        request: main_models.AuthorizeRequest,
    ) -> main_models.AuthorizeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.authorize_with_options(request, headers, runtime)

    async def authorize_async(
        self,
        request: main_models.AuthorizeRequest,
    ) -> main_models.AuthorizeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.authorize_with_options_async(request, headers, runtime)

    def batch_with_options(
        self,
        request: main_models.BatchRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.requests):
            body['requests'] = request.requests
        if not DaraCore.is_null(request.resource):
            body['resource'] = request.resource
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Batch',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/batch',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchResponse(),
            self.execute(params, req, runtime)
        )

    async def batch_with_options_async(
        self,
        request: main_models.BatchRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.requests):
            body['requests'] = request.requests
        if not DaraCore.is_null(request.resource):
            body['resource'] = request.resource
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Batch',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/batch',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchResponse(),
            await self.execute_async(params, req, runtime)
        )

    def batch(
        self,
        request: main_models.BatchRequest,
    ) -> main_models.BatchResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.batch_with_options(request, headers, runtime)

    async def batch_async(
        self,
        request: main_models.BatchRequest,
    ) -> main_models.BatchResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.batch_with_options_async(request, headers, runtime)

    def cancel_assign_role_with_options(
        self,
        request: main_models.CancelAssignRoleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CancelAssignRoleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.identity):
            body['identity'] = request.identity
        if not DaraCore.is_null(request.manage_resource_id):
            body['manage_resource_id'] = request.manage_resource_id
        if not DaraCore.is_null(request.manage_resource_type):
            body['manage_resource_type'] = request.manage_resource_type
        if not DaraCore.is_null(request.role_id):
            body['role_id'] = request.role_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CancelAssignRole',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/role/cancel_assign',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelAssignRoleResponse(),
            self.execute(params, req, runtime)
        )

    async def cancel_assign_role_with_options_async(
        self,
        request: main_models.CancelAssignRoleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CancelAssignRoleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.identity):
            body['identity'] = request.identity
        if not DaraCore.is_null(request.manage_resource_id):
            body['manage_resource_id'] = request.manage_resource_id
        if not DaraCore.is_null(request.manage_resource_type):
            body['manage_resource_type'] = request.manage_resource_type
        if not DaraCore.is_null(request.role_id):
            body['role_id'] = request.role_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CancelAssignRole',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/role/cancel_assign',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelAssignRoleResponse(),
            await self.execute_async(params, req, runtime)
        )

    def cancel_assign_role(
        self,
        request: main_models.CancelAssignRoleRequest,
    ) -> main_models.CancelAssignRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.cancel_assign_role_with_options(request, headers, runtime)

    async def cancel_assign_role_async(
        self,
        request: main_models.CancelAssignRoleRequest,
    ) -> main_models.CancelAssignRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.cancel_assign_role_with_options_async(request, headers, runtime)

    def cancel_share_link_with_options(
        self,
        request: main_models.CancelShareLinkRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CancelShareLinkResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.share_id):
            body['share_id'] = request.share_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CancelShareLink',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/share_link/cancel',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelShareLinkResponse(),
            self.execute(params, req, runtime)
        )

    async def cancel_share_link_with_options_async(
        self,
        request: main_models.CancelShareLinkRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CancelShareLinkResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.share_id):
            body['share_id'] = request.share_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CancelShareLink',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/share_link/cancel',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelShareLinkResponse(),
            await self.execute_async(params, req, runtime)
        )

    def cancel_share_link(
        self,
        request: main_models.CancelShareLinkRequest,
    ) -> main_models.CancelShareLinkResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.cancel_share_link_with_options(request, headers, runtime)

    async def cancel_share_link_async(
        self,
        request: main_models.CancelShareLinkRequest,
    ) -> main_models.CancelShareLinkResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.cancel_share_link_with_options_async(request, headers, runtime)

    def clear_recyclebin_with_options(
        self,
        request: main_models.ClearRecyclebinRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ClearRecyclebinResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ClearRecyclebin',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/recyclebin/clear',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ClearRecyclebinResponse(),
            self.execute(params, req, runtime)
        )

    async def clear_recyclebin_with_options_async(
        self,
        request: main_models.ClearRecyclebinRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ClearRecyclebinResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ClearRecyclebin',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/recyclebin/clear',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ClearRecyclebinResponse(),
            await self.execute_async(params, req, runtime)
        )

    def clear_recyclebin(
        self,
        request: main_models.ClearRecyclebinRequest,
    ) -> main_models.ClearRecyclebinResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.clear_recyclebin_with_options(request, headers, runtime)

    async def clear_recyclebin_async(
        self,
        request: main_models.ClearRecyclebinRequest,
    ) -> main_models.ClearRecyclebinResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.clear_recyclebin_with_options_async(request, headers, runtime)

    def complete_file_with_options(
        self,
        request: main_models.CompleteFileRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CompleteFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.crc_64hash):
            body['crc64_hash'] = request.crc_64hash
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.file_id):
            body['file_id'] = request.file_id
        if not DaraCore.is_null(request.upload_id):
            body['upload_id'] = request.upload_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CompleteFile',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/complete',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CompleteFileResponse(),
            self.execute(params, req, runtime)
        )

    async def complete_file_with_options_async(
        self,
        request: main_models.CompleteFileRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CompleteFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.crc_64hash):
            body['crc64_hash'] = request.crc_64hash
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.file_id):
            body['file_id'] = request.file_id
        if not DaraCore.is_null(request.upload_id):
            body['upload_id'] = request.upload_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CompleteFile',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/complete',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CompleteFileResponse(),
            await self.execute_async(params, req, runtime)
        )

    def complete_file(
        self,
        request: main_models.CompleteFileRequest,
    ) -> main_models.CompleteFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.complete_file_with_options(request, headers, runtime)

    async def complete_file_async(
        self,
        request: main_models.CompleteFileRequest,
    ) -> main_models.CompleteFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.complete_file_with_options_async(request, headers, runtime)

    def copy_file_with_options(
        self,
        request: main_models.CopyFileRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CopyFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_rename):
            body['auto_rename'] = request.auto_rename
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.file_id):
            body['file_id'] = request.file_id
        if not DaraCore.is_null(request.share_id):
            body['share_id'] = request.share_id
        if not DaraCore.is_null(request.to_drive_id):
            body['to_drive_id'] = request.to_drive_id
        if not DaraCore.is_null(request.to_parent_file_id):
            body['to_parent_file_id'] = request.to_parent_file_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CopyFile',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/copy',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CopyFileResponse(),
            self.execute(params, req, runtime)
        )

    async def copy_file_with_options_async(
        self,
        request: main_models.CopyFileRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CopyFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_rename):
            body['auto_rename'] = request.auto_rename
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.file_id):
            body['file_id'] = request.file_id
        if not DaraCore.is_null(request.share_id):
            body['share_id'] = request.share_id
        if not DaraCore.is_null(request.to_drive_id):
            body['to_drive_id'] = request.to_drive_id
        if not DaraCore.is_null(request.to_parent_file_id):
            body['to_parent_file_id'] = request.to_parent_file_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CopyFile',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/copy',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CopyFileResponse(),
            await self.execute_async(params, req, runtime)
        )

    def copy_file(
        self,
        request: main_models.CopyFileRequest,
    ) -> main_models.CopyFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.copy_file_with_options(request, headers, runtime)

    async def copy_file_async(
        self,
        request: main_models.CopyFileRequest,
    ) -> main_models.CopyFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.copy_file_with_options_async(request, headers, runtime)

    def create_customized_story_with_options(
        self,
        request: main_models.CreateCustomizedStoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateCustomizedStoryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.custom_labels):
            body['custom_labels'] = request.custom_labels
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.story_cover):
            body['story_cover'] = request.story_cover
        if not DaraCore.is_null(request.story_files):
            body['story_files'] = request.story_files
        if not DaraCore.is_null(request.story_name):
            body['story_name'] = request.story_name
        if not DaraCore.is_null(request.story_sub_type):
            body['story_sub_type'] = request.story_sub_type
        if not DaraCore.is_null(request.story_type):
            body['story_type'] = request.story_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateCustomizedStory',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/image/create_customized_story',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCustomizedStoryResponse(),
            self.execute(params, req, runtime)
        )

    async def create_customized_story_with_options_async(
        self,
        request: main_models.CreateCustomizedStoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateCustomizedStoryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.custom_labels):
            body['custom_labels'] = request.custom_labels
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.story_cover):
            body['story_cover'] = request.story_cover
        if not DaraCore.is_null(request.story_files):
            body['story_files'] = request.story_files
        if not DaraCore.is_null(request.story_name):
            body['story_name'] = request.story_name
        if not DaraCore.is_null(request.story_sub_type):
            body['story_sub_type'] = request.story_sub_type
        if not DaraCore.is_null(request.story_type):
            body['story_type'] = request.story_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateCustomizedStory',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/image/create_customized_story',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCustomizedStoryResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_customized_story(
        self,
        request: main_models.CreateCustomizedStoryRequest,
    ) -> main_models.CreateCustomizedStoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_customized_story_with_options(request, headers, runtime)

    async def create_customized_story_async(
        self,
        request: main_models.CreateCustomizedStoryRequest,
    ) -> main_models.CreateCustomizedStoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_customized_story_with_options_async(request, headers, runtime)

    def create_domain_with_options(
        self,
        request: main_models.CreateDomainRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDomainResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.domain_name):
            body['domain_name'] = request.domain_name
        if not DaraCore.is_null(request.init_drive_enable):
            body['init_drive_enable'] = request.init_drive_enable
        if not DaraCore.is_null(request.init_drive_size):
            body['init_drive_size'] = request.init_drive_size
        if not DaraCore.is_null(request.parent_domain_id):
            body['parent_domain_id'] = request.parent_domain_id
        if not DaraCore.is_null(request.size_quota):
            body['size_quota'] = request.size_quota
        if not DaraCore.is_null(request.store_redundancy_type):
            body['store_redundancy_type'] = request.store_redundancy_type
        if not DaraCore.is_null(request.user_count_quota):
            body['user_count_quota'] = request.user_count_quota
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDomain',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/domain/create',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDomainResponse(),
            self.execute(params, req, runtime)
        )

    async def create_domain_with_options_async(
        self,
        request: main_models.CreateDomainRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDomainResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.domain_name):
            body['domain_name'] = request.domain_name
        if not DaraCore.is_null(request.init_drive_enable):
            body['init_drive_enable'] = request.init_drive_enable
        if not DaraCore.is_null(request.init_drive_size):
            body['init_drive_size'] = request.init_drive_size
        if not DaraCore.is_null(request.parent_domain_id):
            body['parent_domain_id'] = request.parent_domain_id
        if not DaraCore.is_null(request.size_quota):
            body['size_quota'] = request.size_quota
        if not DaraCore.is_null(request.store_redundancy_type):
            body['store_redundancy_type'] = request.store_redundancy_type
        if not DaraCore.is_null(request.user_count_quota):
            body['user_count_quota'] = request.user_count_quota
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDomain',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/domain/create',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDomainResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_domain(
        self,
        request: main_models.CreateDomainRequest,
    ) -> main_models.CreateDomainResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_domain_with_options(request, headers, runtime)

    async def create_domain_async(
        self,
        request: main_models.CreateDomainRequest,
    ) -> main_models.CreateDomainResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_domain_with_options_async(request, headers, runtime)

    def create_drive_with_options(
        self,
        request: main_models.CreateDriveRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDriveResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.default):
            body['default'] = request.default
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.drive_name):
            body['drive_name'] = request.drive_name
        if not DaraCore.is_null(request.drive_type):
            body['drive_type'] = request.drive_type
        if not DaraCore.is_null(request.owner):
            body['owner'] = request.owner
        if not DaraCore.is_null(request.owner_type):
            body['owner_type'] = request.owner_type
        if not DaraCore.is_null(request.status):
            body['status'] = request.status
        if not DaraCore.is_null(request.total_size):
            body['total_size'] = request.total_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDrive',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/drive/create',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDriveResponse(),
            self.execute(params, req, runtime)
        )

    async def create_drive_with_options_async(
        self,
        request: main_models.CreateDriveRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDriveResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.default):
            body['default'] = request.default
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.drive_name):
            body['drive_name'] = request.drive_name
        if not DaraCore.is_null(request.drive_type):
            body['drive_type'] = request.drive_type
        if not DaraCore.is_null(request.owner):
            body['owner'] = request.owner
        if not DaraCore.is_null(request.owner_type):
            body['owner_type'] = request.owner_type
        if not DaraCore.is_null(request.status):
            body['status'] = request.status
        if not DaraCore.is_null(request.total_size):
            body['total_size'] = request.total_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDrive',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/drive/create',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDriveResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_drive(
        self,
        request: main_models.CreateDriveRequest,
    ) -> main_models.CreateDriveResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_drive_with_options(request, headers, runtime)

    async def create_drive_async(
        self,
        request: main_models.CreateDriveRequest,
    ) -> main_models.CreateDriveResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_drive_with_options_async(request, headers, runtime)

    def create_file_with_options(
        self,
        request: main_models.CreateFileRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.check_name_mode):
            body['check_name_mode'] = request.check_name_mode
        if not DaraCore.is_null(request.content_hash):
            body['content_hash'] = request.content_hash
        if not DaraCore.is_null(request.content_hash_name):
            body['content_hash_name'] = request.content_hash_name
        if not DaraCore.is_null(request.content_type):
            body['content_type'] = request.content_type
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.file_id):
            body['file_id'] = request.file_id
        if not DaraCore.is_null(request.hidden):
            body['hidden'] = request.hidden
        if not DaraCore.is_null(request.local_created_at):
            body['local_created_at'] = request.local_created_at
        if not DaraCore.is_null(request.local_modified_at):
            body['local_modified_at'] = request.local_modified_at
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.parallel_upload):
            body['parallel_upload'] = request.parallel_upload
        if not DaraCore.is_null(request.parent_file_id):
            body['parent_file_id'] = request.parent_file_id
        if not DaraCore.is_null(request.part_info_list):
            body['part_info_list'] = request.part_info_list
        if not DaraCore.is_null(request.pre_hash):
            body['pre_hash'] = request.pre_hash
        if not DaraCore.is_null(request.share_id):
            body['share_id'] = request.share_id
        if not DaraCore.is_null(request.size):
            body['size'] = request.size
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        if not DaraCore.is_null(request.user_tags):
            body['user_tags'] = request.user_tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateFile',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/create',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFileResponse(),
            self.execute(params, req, runtime)
        )

    async def create_file_with_options_async(
        self,
        request: main_models.CreateFileRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.check_name_mode):
            body['check_name_mode'] = request.check_name_mode
        if not DaraCore.is_null(request.content_hash):
            body['content_hash'] = request.content_hash
        if not DaraCore.is_null(request.content_hash_name):
            body['content_hash_name'] = request.content_hash_name
        if not DaraCore.is_null(request.content_type):
            body['content_type'] = request.content_type
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.file_id):
            body['file_id'] = request.file_id
        if not DaraCore.is_null(request.hidden):
            body['hidden'] = request.hidden
        if not DaraCore.is_null(request.local_created_at):
            body['local_created_at'] = request.local_created_at
        if not DaraCore.is_null(request.local_modified_at):
            body['local_modified_at'] = request.local_modified_at
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.parallel_upload):
            body['parallel_upload'] = request.parallel_upload
        if not DaraCore.is_null(request.parent_file_id):
            body['parent_file_id'] = request.parent_file_id
        if not DaraCore.is_null(request.part_info_list):
            body['part_info_list'] = request.part_info_list
        if not DaraCore.is_null(request.pre_hash):
            body['pre_hash'] = request.pre_hash
        if not DaraCore.is_null(request.share_id):
            body['share_id'] = request.share_id
        if not DaraCore.is_null(request.size):
            body['size'] = request.size
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        if not DaraCore.is_null(request.user_tags):
            body['user_tags'] = request.user_tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateFile',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/create',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFileResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_file(
        self,
        request: main_models.CreateFileRequest,
    ) -> main_models.CreateFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_file_with_options(request, headers, runtime)

    async def create_file_async(
        self,
        request: main_models.CreateFileRequest,
    ) -> main_models.CreateFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_file_with_options_async(request, headers, runtime)

    def create_group_with_options(
        self,
        request: main_models.CreateGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.group_name):
            body['group_name'] = request.group_name
        if not DaraCore.is_null(request.is_root):
            body['is_root'] = request.is_root
        if not DaraCore.is_null(request.parent_group_id):
            body['parent_group_id'] = request.parent_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateGroup',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/group/create',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGroupResponse(),
            self.execute(params, req, runtime)
        )

    async def create_group_with_options_async(
        self,
        request: main_models.CreateGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.group_name):
            body['group_name'] = request.group_name
        if not DaraCore.is_null(request.is_root):
            body['is_root'] = request.is_root
        if not DaraCore.is_null(request.parent_group_id):
            body['parent_group_id'] = request.parent_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateGroup',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/group/create',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGroupResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_group(
        self,
        request: main_models.CreateGroupRequest,
    ) -> main_models.CreateGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_group_with_options(request, headers, runtime)

    async def create_group_async(
        self,
        request: main_models.CreateGroupRequest,
    ) -> main_models.CreateGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_group_with_options_async(request, headers, runtime)

    def create_identity_to_benefit_pkg_mapping_with_options(
        self,
        request: main_models.CreateIdentityToBenefitPkgMappingRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateIdentityToBenefitPkgMappingResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.amount):
            body['amount'] = request.amount
        if not DaraCore.is_null(request.benefit_pkg_id):
            body['benefit_pkg_id'] = request.benefit_pkg_id
        if not DaraCore.is_null(request.expire_time):
            body['expire_time'] = request.expire_time
        if not DaraCore.is_null(request.identity_id):
            body['identity_id'] = request.identity_id
        if not DaraCore.is_null(request.identity_type):
            body['identity_type'] = request.identity_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateIdentityToBenefitPkgMapping',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/benefit/identity_to_benefit_pkg_mapping/create',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIdentityToBenefitPkgMappingResponse(),
            self.execute(params, req, runtime)
        )

    async def create_identity_to_benefit_pkg_mapping_with_options_async(
        self,
        request: main_models.CreateIdentityToBenefitPkgMappingRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateIdentityToBenefitPkgMappingResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.amount):
            body['amount'] = request.amount
        if not DaraCore.is_null(request.benefit_pkg_id):
            body['benefit_pkg_id'] = request.benefit_pkg_id
        if not DaraCore.is_null(request.expire_time):
            body['expire_time'] = request.expire_time
        if not DaraCore.is_null(request.identity_id):
            body['identity_id'] = request.identity_id
        if not DaraCore.is_null(request.identity_type):
            body['identity_type'] = request.identity_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateIdentityToBenefitPkgMapping',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/benefit/identity_to_benefit_pkg_mapping/create',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIdentityToBenefitPkgMappingResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_identity_to_benefit_pkg_mapping(
        self,
        request: main_models.CreateIdentityToBenefitPkgMappingRequest,
    ) -> main_models.CreateIdentityToBenefitPkgMappingResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_identity_to_benefit_pkg_mapping_with_options(request, headers, runtime)

    async def create_identity_to_benefit_pkg_mapping_async(
        self,
        request: main_models.CreateIdentityToBenefitPkgMappingRequest,
    ) -> main_models.CreateIdentityToBenefitPkgMappingResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_identity_to_benefit_pkg_mapping_with_options_async(request, headers, runtime)

    def create_order_with_options(
        self,
        request: main_models.CreateOrderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateOrderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_pay):
            body['auto_pay'] = request.auto_pay
        if not DaraCore.is_null(request.auto_renew):
            body['auto_renew'] = request.auto_renew
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.instance_id):
            body['instance_id'] = request.instance_id
        if not DaraCore.is_null(request.order_type):
            body['order_type'] = request.order_type
        if not DaraCore.is_null(request.package):
            body['package'] = request.package
        if not DaraCore.is_null(request.period):
            body['period'] = request.period
        if not DaraCore.is_null(request.period_unit):
            body['period_unit'] = request.period_unit
        if not DaraCore.is_null(request.total_size):
            body['total_size'] = request.total_size
        if not DaraCore.is_null(request.user_count):
            body['user_count'] = request.user_count
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateOrder',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/domain/create_order',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOrderResponse(),
            self.execute(params, req, runtime)
        )

    async def create_order_with_options_async(
        self,
        request: main_models.CreateOrderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateOrderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_pay):
            body['auto_pay'] = request.auto_pay
        if not DaraCore.is_null(request.auto_renew):
            body['auto_renew'] = request.auto_renew
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.instance_id):
            body['instance_id'] = request.instance_id
        if not DaraCore.is_null(request.order_type):
            body['order_type'] = request.order_type
        if not DaraCore.is_null(request.package):
            body['package'] = request.package
        if not DaraCore.is_null(request.period):
            body['period'] = request.period
        if not DaraCore.is_null(request.period_unit):
            body['period_unit'] = request.period_unit
        if not DaraCore.is_null(request.total_size):
            body['total_size'] = request.total_size
        if not DaraCore.is_null(request.user_count):
            body['user_count'] = request.user_count
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateOrder',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/domain/create_order',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOrderResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_order(
        self,
        request: main_models.CreateOrderRequest,
    ) -> main_models.CreateOrderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_order_with_options(request, headers, runtime)

    async def create_order_async(
        self,
        request: main_models.CreateOrderRequest,
    ) -> main_models.CreateOrderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_order_with_options_async(request, headers, runtime)

    def create_share_link_with_options(
        self,
        request: main_models.CreateShareLinkRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateShareLinkResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.creatable):
            body['creatable'] = request.creatable
        if not DaraCore.is_null(request.creatable_file_id_list):
            body['creatable_file_id_list'] = request.creatable_file_id_list
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.disable_download):
            body['disable_download'] = request.disable_download
        if not DaraCore.is_null(request.disable_preview):
            body['disable_preview'] = request.disable_preview
        if not DaraCore.is_null(request.disable_save):
            body['disable_save'] = request.disable_save
        if not DaraCore.is_null(request.download_limit):
            body['download_limit'] = request.download_limit
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.expiration):
            body['expiration'] = request.expiration
        if not DaraCore.is_null(request.file_id_list):
            body['file_id_list'] = request.file_id_list
        if not DaraCore.is_null(request.office_editable):
            body['office_editable'] = request.office_editable
        if not DaraCore.is_null(request.preview_limit):
            body['preview_limit'] = request.preview_limit
        if not DaraCore.is_null(request.require_login):
            body['require_login'] = request.require_login
        if not DaraCore.is_null(request.save_limit):
            body['save_limit'] = request.save_limit
        if not DaraCore.is_null(request.share_all_files):
            body['share_all_files'] = request.share_all_files
        if not DaraCore.is_null(request.share_name):
            body['share_name'] = request.share_name
        if not DaraCore.is_null(request.share_pwd):
            body['share_pwd'] = request.share_pwd
        if not DaraCore.is_null(request.user_id):
            body['user_id'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateShareLink',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/share_link/create',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateShareLinkResponse(),
            self.execute(params, req, runtime)
        )

    async def create_share_link_with_options_async(
        self,
        request: main_models.CreateShareLinkRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateShareLinkResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.creatable):
            body['creatable'] = request.creatable
        if not DaraCore.is_null(request.creatable_file_id_list):
            body['creatable_file_id_list'] = request.creatable_file_id_list
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.disable_download):
            body['disable_download'] = request.disable_download
        if not DaraCore.is_null(request.disable_preview):
            body['disable_preview'] = request.disable_preview
        if not DaraCore.is_null(request.disable_save):
            body['disable_save'] = request.disable_save
        if not DaraCore.is_null(request.download_limit):
            body['download_limit'] = request.download_limit
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.expiration):
            body['expiration'] = request.expiration
        if not DaraCore.is_null(request.file_id_list):
            body['file_id_list'] = request.file_id_list
        if not DaraCore.is_null(request.office_editable):
            body['office_editable'] = request.office_editable
        if not DaraCore.is_null(request.preview_limit):
            body['preview_limit'] = request.preview_limit
        if not DaraCore.is_null(request.require_login):
            body['require_login'] = request.require_login
        if not DaraCore.is_null(request.save_limit):
            body['save_limit'] = request.save_limit
        if not DaraCore.is_null(request.share_all_files):
            body['share_all_files'] = request.share_all_files
        if not DaraCore.is_null(request.share_name):
            body['share_name'] = request.share_name
        if not DaraCore.is_null(request.share_pwd):
            body['share_pwd'] = request.share_pwd
        if not DaraCore.is_null(request.user_id):
            body['user_id'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateShareLink',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/share_link/create',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateShareLinkResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_share_link(
        self,
        request: main_models.CreateShareLinkRequest,
    ) -> main_models.CreateShareLinkResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_share_link_with_options(request, headers, runtime)

    async def create_share_link_async(
        self,
        request: main_models.CreateShareLinkRequest,
    ) -> main_models.CreateShareLinkResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_share_link_with_options_async(request, headers, runtime)

    def create_similar_image_cluster_task_with_options(
        self,
        request: main_models.CreateSimilarImageClusterTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateSimilarImageClusterTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSimilarImageClusterTask',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/image/create_similar_image_cluster_task',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSimilarImageClusterTaskResponse(),
            self.execute(params, req, runtime)
        )

    async def create_similar_image_cluster_task_with_options_async(
        self,
        request: main_models.CreateSimilarImageClusterTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateSimilarImageClusterTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSimilarImageClusterTask',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/image/create_similar_image_cluster_task',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSimilarImageClusterTaskResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_similar_image_cluster_task(
        self,
        request: main_models.CreateSimilarImageClusterTaskRequest,
    ) -> main_models.CreateSimilarImageClusterTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_similar_image_cluster_task_with_options(request, headers, runtime)

    async def create_similar_image_cluster_task_async(
        self,
        request: main_models.CreateSimilarImageClusterTaskRequest,
    ) -> main_models.CreateSimilarImageClusterTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_similar_image_cluster_task_with_options_async(request, headers, runtime)

    def create_story_with_options(
        self,
        request: main_models.CreateStoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateStoryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.address):
            body['address'] = request.address
        if not DaraCore.is_null(request.custom_labels):
            body['custom_labels'] = request.custom_labels
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.max_image_count):
            body['max_image_count'] = request.max_image_count
        if not DaraCore.is_null(request.min_image_count):
            body['min_image_count'] = request.min_image_count
        if not DaraCore.is_null(request.story_end_time):
            body['story_end_time'] = request.story_end_time
        if not DaraCore.is_null(request.story_id):
            body['story_id'] = request.story_id
        if not DaraCore.is_null(request.story_name):
            body['story_name'] = request.story_name
        if not DaraCore.is_null(request.story_start_time):
            body['story_start_time'] = request.story_start_time
        if not DaraCore.is_null(request.story_sub_type):
            body['story_sub_type'] = request.story_sub_type
        if not DaraCore.is_null(request.story_type):
            body['story_type'] = request.story_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateStory',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/image/create_story',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateStoryResponse(),
            self.execute(params, req, runtime)
        )

    async def create_story_with_options_async(
        self,
        request: main_models.CreateStoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateStoryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.address):
            body['address'] = request.address
        if not DaraCore.is_null(request.custom_labels):
            body['custom_labels'] = request.custom_labels
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.max_image_count):
            body['max_image_count'] = request.max_image_count
        if not DaraCore.is_null(request.min_image_count):
            body['min_image_count'] = request.min_image_count
        if not DaraCore.is_null(request.story_end_time):
            body['story_end_time'] = request.story_end_time
        if not DaraCore.is_null(request.story_id):
            body['story_id'] = request.story_id
        if not DaraCore.is_null(request.story_name):
            body['story_name'] = request.story_name
        if not DaraCore.is_null(request.story_start_time):
            body['story_start_time'] = request.story_start_time
        if not DaraCore.is_null(request.story_sub_type):
            body['story_sub_type'] = request.story_sub_type
        if not DaraCore.is_null(request.story_type):
            body['story_type'] = request.story_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateStory',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/image/create_story',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateStoryResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_story(
        self,
        request: main_models.CreateStoryRequest,
    ) -> main_models.CreateStoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_story_with_options(request, headers, runtime)

    async def create_story_async(
        self,
        request: main_models.CreateStoryRequest,
    ) -> main_models.CreateStoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_story_with_options_async(request, headers, runtime)

    def create_user_with_options(
        self,
        request: main_models.CreateUserRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateUserResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.avatar):
            body['avatar'] = request.avatar
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.email):
            body['email'] = request.email
        if not DaraCore.is_null(request.group_info_list):
            body['group_info_list'] = request.group_info_list
        if not DaraCore.is_null(request.nick_name):
            body['nick_name'] = request.nick_name
        if not DaraCore.is_null(request.phone):
            body['phone'] = request.phone
        if not DaraCore.is_null(request.role):
            body['role'] = request.role
        if not DaraCore.is_null(request.status):
            body['status'] = request.status
        if not DaraCore.is_null(request.user_data):
            body['user_data'] = request.user_data
        if not DaraCore.is_null(request.user_id):
            body['user_id'] = request.user_id
        if not DaraCore.is_null(request.user_name):
            body['user_name'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateUser',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/user/create',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUserResponse(),
            self.execute(params, req, runtime)
        )

    async def create_user_with_options_async(
        self,
        request: main_models.CreateUserRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateUserResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.avatar):
            body['avatar'] = request.avatar
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.email):
            body['email'] = request.email
        if not DaraCore.is_null(request.group_info_list):
            body['group_info_list'] = request.group_info_list
        if not DaraCore.is_null(request.nick_name):
            body['nick_name'] = request.nick_name
        if not DaraCore.is_null(request.phone):
            body['phone'] = request.phone
        if not DaraCore.is_null(request.role):
            body['role'] = request.role
        if not DaraCore.is_null(request.status):
            body['status'] = request.status
        if not DaraCore.is_null(request.user_data):
            body['user_data'] = request.user_data
        if not DaraCore.is_null(request.user_id):
            body['user_id'] = request.user_id
        if not DaraCore.is_null(request.user_name):
            body['user_name'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateUser',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/user/create',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUserResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_user(
        self,
        request: main_models.CreateUserRequest,
    ) -> main_models.CreateUserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_user_with_options(request, headers, runtime)

    async def create_user_async(
        self,
        request: main_models.CreateUserRequest,
    ) -> main_models.CreateUserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_user_with_options_async(request, headers, runtime)

    def csi_get_file_info_with_options(
        self,
        request: main_models.CsiGetFileInfoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CsiGetFileInfoResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.file_id):
            body['file_id'] = request.file_id
        if not DaraCore.is_null(request.url_expire_sec):
            body['url_expire_sec'] = request.url_expire_sec
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CsiGetFileInfo',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/csi/get_file_info',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CsiGetFileInfoResponse(),
            self.execute(params, req, runtime)
        )

    async def csi_get_file_info_with_options_async(
        self,
        request: main_models.CsiGetFileInfoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CsiGetFileInfoResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.file_id):
            body['file_id'] = request.file_id
        if not DaraCore.is_null(request.url_expire_sec):
            body['url_expire_sec'] = request.url_expire_sec
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CsiGetFileInfo',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/csi/get_file_info',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CsiGetFileInfoResponse(),
            await self.execute_async(params, req, runtime)
        )

    def csi_get_file_info(
        self,
        request: main_models.CsiGetFileInfoRequest,
    ) -> main_models.CsiGetFileInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.csi_get_file_info_with_options(request, headers, runtime)

    async def csi_get_file_info_async(
        self,
        request: main_models.CsiGetFileInfoRequest,
    ) -> main_models.CsiGetFileInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.csi_get_file_info_with_options_async(request, headers, runtime)

    def delete_domain_with_options(
        self,
        request: main_models.DeleteDomainRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDomainResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.domain_id):
            body['domain_id'] = request.domain_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDomain',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/domain/delete',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDomainResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_domain_with_options_async(
        self,
        request: main_models.DeleteDomainRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDomainResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.domain_id):
            body['domain_id'] = request.domain_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDomain',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/domain/delete',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDomainResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_domain(
        self,
        request: main_models.DeleteDomainRequest,
    ) -> main_models.DeleteDomainResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_domain_with_options(request, headers, runtime)

    async def delete_domain_async(
        self,
        request: main_models.DeleteDomainRequest,
    ) -> main_models.DeleteDomainResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_domain_with_options_async(request, headers, runtime)

    def delete_drive_with_options(
        self,
        request: main_models.DeleteDriveRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDriveResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDrive',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/drive/delete',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDriveResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_drive_with_options_async(
        self,
        request: main_models.DeleteDriveRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDriveResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDrive',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/drive/delete',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDriveResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_drive(
        self,
        request: main_models.DeleteDriveRequest,
    ) -> main_models.DeleteDriveResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_drive_with_options(request, headers, runtime)

    async def delete_drive_async(
        self,
        request: main_models.DeleteDriveRequest,
    ) -> main_models.DeleteDriveResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_drive_with_options_async(request, headers, runtime)

    def delete_file_with_options(
        self,
        request: main_models.DeleteFileRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.file_id):
            body['file_id'] = request.file_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFile',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/delete',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFileResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_file_with_options_async(
        self,
        request: main_models.DeleteFileRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.file_id):
            body['file_id'] = request.file_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFile',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/delete',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFileResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_file(
        self,
        request: main_models.DeleteFileRequest,
    ) -> main_models.DeleteFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_file_with_options(request, headers, runtime)

    async def delete_file_async(
        self,
        request: main_models.DeleteFileRequest,
    ) -> main_models.DeleteFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_file_with_options_async(request, headers, runtime)

    def delete_group_with_options(
        self,
        request: main_models.DeleteGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.group_id):
            body['group_id'] = request.group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGroup',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/group/delete',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGroupResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_group_with_options_async(
        self,
        request: main_models.DeleteGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.group_id):
            body['group_id'] = request.group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGroup',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/group/delete',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGroupResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_group(
        self,
        request: main_models.DeleteGroupRequest,
    ) -> main_models.DeleteGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_group_with_options(request, headers, runtime)

    async def delete_group_async(
        self,
        request: main_models.DeleteGroupRequest,
    ) -> main_models.DeleteGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_group_with_options_async(request, headers, runtime)

    def delete_revision_with_options(
        self,
        request: main_models.DeleteRevisionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRevisionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.file_id):
            body['file_id'] = request.file_id
        if not DaraCore.is_null(request.revision_id):
            body['revision_id'] = request.revision_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRevision',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/revision/delete',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRevisionResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_revision_with_options_async(
        self,
        request: main_models.DeleteRevisionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRevisionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.file_id):
            body['file_id'] = request.file_id
        if not DaraCore.is_null(request.revision_id):
            body['revision_id'] = request.revision_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRevision',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/revision/delete',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRevisionResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_revision(
        self,
        request: main_models.DeleteRevisionRequest,
    ) -> main_models.DeleteRevisionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_revision_with_options(request, headers, runtime)

    async def delete_revision_async(
        self,
        request: main_models.DeleteRevisionRequest,
    ) -> main_models.DeleteRevisionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_revision_with_options_async(request, headers, runtime)

    def delete_story_with_options(
        self,
        request: main_models.DeleteStoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteStoryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.story_id):
            body['story_id'] = request.story_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteStory',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/image/delete_story',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteStoryResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_story_with_options_async(
        self,
        request: main_models.DeleteStoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteStoryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.story_id):
            body['story_id'] = request.story_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteStory',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/image/delete_story',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteStoryResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_story(
        self,
        request: main_models.DeleteStoryRequest,
    ) -> main_models.DeleteStoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_story_with_options(request, headers, runtime)

    async def delete_story_async(
        self,
        request: main_models.DeleteStoryRequest,
    ) -> main_models.DeleteStoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_story_with_options_async(request, headers, runtime)

    def delete_user_with_options(
        self,
        request: main_models.DeleteUserRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.user_id):
            body['user_id'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUser',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/user/delete',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUserResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_user_with_options_async(
        self,
        request: main_models.DeleteUserRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.user_id):
            body['user_id'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUser',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/user/delete',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUserResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_user(
        self,
        request: main_models.DeleteUserRequest,
    ) -> main_models.DeleteUserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_user_with_options(request, headers, runtime)

    async def delete_user_async(
        self,
        request: main_models.DeleteUserRequest,
    ) -> main_models.DeleteUserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_user_with_options_async(request, headers, runtime)

    def delta_get_last_cursor_with_options(
        self,
        request: main_models.DeltaGetLastCursorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeltaGetLastCursorResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.sync_root_id):
            body['sync_root_id'] = request.sync_root_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeltaGetLastCursor',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/get_last_cursor',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeltaGetLastCursorResponse(),
            self.execute(params, req, runtime)
        )

    async def delta_get_last_cursor_with_options_async(
        self,
        request: main_models.DeltaGetLastCursorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeltaGetLastCursorResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.sync_root_id):
            body['sync_root_id'] = request.sync_root_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeltaGetLastCursor',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/get_last_cursor',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeltaGetLastCursorResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delta_get_last_cursor(
        self,
        request: main_models.DeltaGetLastCursorRequest,
    ) -> main_models.DeltaGetLastCursorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delta_get_last_cursor_with_options(request, headers, runtime)

    async def delta_get_last_cursor_async(
        self,
        request: main_models.DeltaGetLastCursorRequest,
    ) -> main_models.DeltaGetLastCursorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delta_get_last_cursor_with_options_async(request, headers, runtime)

    def download_file_with_options(
        self,
        request: main_models.DownloadFileRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DownloadFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.drive_id):
            query['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.file_id):
            query['file_id'] = request.file_id
        if not DaraCore.is_null(request.image_thumbnail_process):
            query['image_thumbnail_process'] = request.image_thumbnail_process
        if not DaraCore.is_null(request.office_thumbnail_process):
            query['office_thumbnail_process'] = request.office_thumbnail_process
        if not DaraCore.is_null(request.share_id):
            query['share_id'] = request.share_id
        if not DaraCore.is_null(request.video_thumbnail_process):
            query['video_thumbnail_process'] = request.video_thumbnail_process
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DownloadFile',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/download',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'binary'
        )
        return DaraCore.from_map(
            main_models.DownloadFileResponse(),
            self.execute(params, req, runtime)
        )

    async def download_file_with_options_async(
        self,
        request: main_models.DownloadFileRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DownloadFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.drive_id):
            query['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.file_id):
            query['file_id'] = request.file_id
        if not DaraCore.is_null(request.image_thumbnail_process):
            query['image_thumbnail_process'] = request.image_thumbnail_process
        if not DaraCore.is_null(request.office_thumbnail_process):
            query['office_thumbnail_process'] = request.office_thumbnail_process
        if not DaraCore.is_null(request.share_id):
            query['share_id'] = request.share_id
        if not DaraCore.is_null(request.video_thumbnail_process):
            query['video_thumbnail_process'] = request.video_thumbnail_process
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DownloadFile',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/download',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'binary'
        )
        return DaraCore.from_map(
            main_models.DownloadFileResponse(),
            await self.execute_async(params, req, runtime)
        )

    def download_file(
        self,
        request: main_models.DownloadFileRequest,
    ) -> main_models.DownloadFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.download_file_with_options(request, headers, runtime)

    async def download_file_async(
        self,
        request: main_models.DownloadFileRequest,
    ) -> main_models.DownloadFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.download_file_with_options_async(request, headers, runtime)

    def file_add_permission_with_options(
        self,
        request: main_models.FileAddPermissionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.FileAddPermissionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.file_id):
            body['file_id'] = request.file_id
        if not DaraCore.is_null(request.member_list):
            body['member_list'] = request.member_list
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'FileAddPermission',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/add_permission',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FileAddPermissionResponse(),
            self.execute(params, req, runtime)
        )

    async def file_add_permission_with_options_async(
        self,
        request: main_models.FileAddPermissionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.FileAddPermissionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.file_id):
            body['file_id'] = request.file_id
        if not DaraCore.is_null(request.member_list):
            body['member_list'] = request.member_list
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'FileAddPermission',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/add_permission',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FileAddPermissionResponse(),
            await self.execute_async(params, req, runtime)
        )

    def file_add_permission(
        self,
        request: main_models.FileAddPermissionRequest,
    ) -> main_models.FileAddPermissionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.file_add_permission_with_options(request, headers, runtime)

    async def file_add_permission_async(
        self,
        request: main_models.FileAddPermissionRequest,
    ) -> main_models.FileAddPermissionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.file_add_permission_with_options_async(request, headers, runtime)

    def file_delete_user_tags_with_options(
        self,
        request: main_models.FileDeleteUserTagsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.FileDeleteUserTagsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.file_id):
            body['file_id'] = request.file_id
        if not DaraCore.is_null(request.key_list):
            body['key_list'] = request.key_list
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'FileDeleteUserTags',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/delete_usertags',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FileDeleteUserTagsResponse(),
            self.execute(params, req, runtime)
        )

    async def file_delete_user_tags_with_options_async(
        self,
        request: main_models.FileDeleteUserTagsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.FileDeleteUserTagsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.file_id):
            body['file_id'] = request.file_id
        if not DaraCore.is_null(request.key_list):
            body['key_list'] = request.key_list
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'FileDeleteUserTags',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/delete_usertags',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FileDeleteUserTagsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def file_delete_user_tags(
        self,
        request: main_models.FileDeleteUserTagsRequest,
    ) -> main_models.FileDeleteUserTagsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.file_delete_user_tags_with_options(request, headers, runtime)

    async def file_delete_user_tags_async(
        self,
        request: main_models.FileDeleteUserTagsRequest,
    ) -> main_models.FileDeleteUserTagsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.file_delete_user_tags_with_options_async(request, headers, runtime)

    def file_list_permission_with_options(
        self,
        request: main_models.FileListPermissionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.FileListPermissionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.file_id):
            body['file_id'] = request.file_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'FileListPermission',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/list_permission',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'array'
        )
        return DaraCore.from_map(
            main_models.FileListPermissionResponse(),
            self.execute(params, req, runtime)
        )

    async def file_list_permission_with_options_async(
        self,
        request: main_models.FileListPermissionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.FileListPermissionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.file_id):
            body['file_id'] = request.file_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'FileListPermission',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/list_permission',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'array'
        )
        return DaraCore.from_map(
            main_models.FileListPermissionResponse(),
            await self.execute_async(params, req, runtime)
        )

    def file_list_permission(
        self,
        request: main_models.FileListPermissionRequest,
    ) -> main_models.FileListPermissionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.file_list_permission_with_options(request, headers, runtime)

    async def file_list_permission_async(
        self,
        request: main_models.FileListPermissionRequest,
    ) -> main_models.FileListPermissionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.file_list_permission_with_options_async(request, headers, runtime)

    def file_put_user_tags_with_options(
        self,
        request: main_models.FilePutUserTagsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.FilePutUserTagsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.file_id):
            body['file_id'] = request.file_id
        if not DaraCore.is_null(request.user_tags):
            body['user_tags'] = request.user_tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'FilePutUserTags',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/put_usertags',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FilePutUserTagsResponse(),
            self.execute(params, req, runtime)
        )

    async def file_put_user_tags_with_options_async(
        self,
        request: main_models.FilePutUserTagsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.FilePutUserTagsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.file_id):
            body['file_id'] = request.file_id
        if not DaraCore.is_null(request.user_tags):
            body['user_tags'] = request.user_tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'FilePutUserTags',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/put_usertags',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FilePutUserTagsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def file_put_user_tags(
        self,
        request: main_models.FilePutUserTagsRequest,
    ) -> main_models.FilePutUserTagsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.file_put_user_tags_with_options(request, headers, runtime)

    async def file_put_user_tags_async(
        self,
        request: main_models.FilePutUserTagsRequest,
    ) -> main_models.FilePutUserTagsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.file_put_user_tags_with_options_async(request, headers, runtime)

    def file_remove_permission_with_options(
        self,
        request: main_models.FileRemovePermissionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.FileRemovePermissionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.file_id):
            body['file_id'] = request.file_id
        if not DaraCore.is_null(request.member_list):
            body['member_list'] = request.member_list
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'FileRemovePermission',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/remove_permission',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FileRemovePermissionResponse(),
            self.execute(params, req, runtime)
        )

    async def file_remove_permission_with_options_async(
        self,
        request: main_models.FileRemovePermissionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.FileRemovePermissionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.file_id):
            body['file_id'] = request.file_id
        if not DaraCore.is_null(request.member_list):
            body['member_list'] = request.member_list
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'FileRemovePermission',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/remove_permission',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FileRemovePermissionResponse(),
            await self.execute_async(params, req, runtime)
        )

    def file_remove_permission(
        self,
        request: main_models.FileRemovePermissionRequest,
    ) -> main_models.FileRemovePermissionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.file_remove_permission_with_options(request, headers, runtime)

    async def file_remove_permission_async(
        self,
        request: main_models.FileRemovePermissionRequest,
    ) -> main_models.FileRemovePermissionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.file_remove_permission_with_options_async(request, headers, runtime)

    def get_async_task_with_options(
        self,
        request: main_models.GetAsyncTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAsyncTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.async_task_id):
            body['async_task_id'] = request.async_task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetAsyncTask',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/async_task/get',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAsyncTaskResponse(),
            self.execute(params, req, runtime)
        )

    async def get_async_task_with_options_async(
        self,
        request: main_models.GetAsyncTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAsyncTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.async_task_id):
            body['async_task_id'] = request.async_task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetAsyncTask',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/async_task/get',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAsyncTaskResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_async_task(
        self,
        request: main_models.GetAsyncTaskRequest,
    ) -> main_models.GetAsyncTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_async_task_with_options(request, headers, runtime)

    async def get_async_task_async(
        self,
        request: main_models.GetAsyncTaskRequest,
    ) -> main_models.GetAsyncTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_async_task_with_options_async(request, headers, runtime)

    def get_default_drive_with_options(
        self,
        request: main_models.GetDefaultDriveRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDefaultDriveResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.user_id):
            body['user_id'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDefaultDrive',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/drive/get_default_drive',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDefaultDriveResponse(),
            self.execute(params, req, runtime)
        )

    async def get_default_drive_with_options_async(
        self,
        request: main_models.GetDefaultDriveRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDefaultDriveResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.user_id):
            body['user_id'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDefaultDrive',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/drive/get_default_drive',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDefaultDriveResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_default_drive(
        self,
        request: main_models.GetDefaultDriveRequest,
    ) -> main_models.GetDefaultDriveResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_default_drive_with_options(request, headers, runtime)

    async def get_default_drive_async(
        self,
        request: main_models.GetDefaultDriveRequest,
    ) -> main_models.GetDefaultDriveResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_default_drive_with_options_async(request, headers, runtime)

    def get_domain_with_options(
        self,
        request: main_models.GetDomainRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDomainResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.domain_id):
            body['domain_id'] = request.domain_id
        if not DaraCore.is_null(request.fields):
            body['fields'] = request.fields
        if not DaraCore.is_null(request.get_quota_used):
            body['get_quota_used'] = request.get_quota_used
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDomain',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/domain/get',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDomainResponse(),
            self.execute(params, req, runtime)
        )

    async def get_domain_with_options_async(
        self,
        request: main_models.GetDomainRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDomainResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.domain_id):
            body['domain_id'] = request.domain_id
        if not DaraCore.is_null(request.fields):
            body['fields'] = request.fields
        if not DaraCore.is_null(request.get_quota_used):
            body['get_quota_used'] = request.get_quota_used
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDomain',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/domain/get',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDomainResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_domain(
        self,
        request: main_models.GetDomainRequest,
    ) -> main_models.GetDomainResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_domain_with_options(request, headers, runtime)

    async def get_domain_async(
        self,
        request: main_models.GetDomainRequest,
    ) -> main_models.GetDomainResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_domain_with_options_async(request, headers, runtime)

    def get_domain_quota_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDomainQuotaResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetDomainQuota',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/domain/get_quota',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDomainQuotaResponse(),
            self.execute(params, req, runtime)
        )

    async def get_domain_quota_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDomainQuotaResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetDomainQuota',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/domain/get_quota',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDomainQuotaResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_domain_quota(self) -> main_models.GetDomainQuotaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_domain_quota_with_options(headers, runtime)

    async def get_domain_quota_async(self) -> main_models.GetDomainQuotaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_domain_quota_with_options_async(headers, runtime)

    def get_download_url_with_options(
        self,
        request: main_models.GetDownloadUrlRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDownloadUrlResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.expire_sec):
            body['expire_sec'] = request.expire_sec
        if not DaraCore.is_null(request.file_id):
            body['file_id'] = request.file_id
        if not DaraCore.is_null(request.file_name):
            body['file_name'] = request.file_name
        if not DaraCore.is_null(request.response_content_type):
            body['response_content_type'] = request.response_content_type
        if not DaraCore.is_null(request.share_id):
            body['share_id'] = request.share_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDownloadUrl',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/get_download_url',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDownloadUrlResponse(),
            self.execute(params, req, runtime)
        )

    async def get_download_url_with_options_async(
        self,
        request: main_models.GetDownloadUrlRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDownloadUrlResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.expire_sec):
            body['expire_sec'] = request.expire_sec
        if not DaraCore.is_null(request.file_id):
            body['file_id'] = request.file_id
        if not DaraCore.is_null(request.file_name):
            body['file_name'] = request.file_name
        if not DaraCore.is_null(request.response_content_type):
            body['response_content_type'] = request.response_content_type
        if not DaraCore.is_null(request.share_id):
            body['share_id'] = request.share_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDownloadUrl',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/get_download_url',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDownloadUrlResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_download_url(
        self,
        request: main_models.GetDownloadUrlRequest,
    ) -> main_models.GetDownloadUrlResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_download_url_with_options(request, headers, runtime)

    async def get_download_url_async(
        self,
        request: main_models.GetDownloadUrlRequest,
    ) -> main_models.GetDownloadUrlResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_download_url_with_options_async(request, headers, runtime)

    def get_drive_with_options(
        self,
        request: main_models.GetDriveRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDriveResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDrive',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/drive/get',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDriveResponse(),
            self.execute(params, req, runtime)
        )

    async def get_drive_with_options_async(
        self,
        request: main_models.GetDriveRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDriveResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDrive',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/drive/get',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDriveResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_drive(
        self,
        request: main_models.GetDriveRequest,
    ) -> main_models.GetDriveResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_drive_with_options(request, headers, runtime)

    async def get_drive_async(
        self,
        request: main_models.GetDriveRequest,
    ) -> main_models.GetDriveResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_drive_with_options_async(request, headers, runtime)

    def get_file_with_options(
        self,
        request: main_models.GetFileRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.fields):
            body['fields'] = request.fields
        if not DaraCore.is_null(request.file_id):
            body['file_id'] = request.file_id
        if not DaraCore.is_null(request.share_id):
            body['share_id'] = request.share_id
        if not DaraCore.is_null(request.thumbnail_processes):
            body['thumbnail_processes'] = request.thumbnail_processes
        if not DaraCore.is_null(request.url_expire_sec):
            body['url_expire_sec'] = request.url_expire_sec
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetFile',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/get',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFileResponse(),
            self.execute(params, req, runtime)
        )

    async def get_file_with_options_async(
        self,
        request: main_models.GetFileRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.fields):
            body['fields'] = request.fields
        if not DaraCore.is_null(request.file_id):
            body['file_id'] = request.file_id
        if not DaraCore.is_null(request.share_id):
            body['share_id'] = request.share_id
        if not DaraCore.is_null(request.thumbnail_processes):
            body['thumbnail_processes'] = request.thumbnail_processes
        if not DaraCore.is_null(request.url_expire_sec):
            body['url_expire_sec'] = request.url_expire_sec
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetFile',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/get',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFileResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_file(
        self,
        request: main_models.GetFileRequest,
    ) -> main_models.GetFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_file_with_options(request, headers, runtime)

    async def get_file_async(
        self,
        request: main_models.GetFileRequest,
    ) -> main_models.GetFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_file_with_options_async(request, headers, runtime)

    def get_group_with_options(
        self,
        request: main_models.GetGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.group_id):
            body['group_id'] = request.group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetGroup',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/group/get',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGroupResponse(),
            self.execute(params, req, runtime)
        )

    async def get_group_with_options_async(
        self,
        request: main_models.GetGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.group_id):
            body['group_id'] = request.group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetGroup',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/group/get',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGroupResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_group(
        self,
        request: main_models.GetGroupRequest,
    ) -> main_models.GetGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_group_with_options(request, headers, runtime)

    async def get_group_async(
        self,
        request: main_models.GetGroupRequest,
    ) -> main_models.GetGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_group_with_options_async(request, headers, runtime)

    def get_identity_to_benefit_pkg_mapping_with_options(
        self,
        request: main_models.GetIdentityToBenefitPkgMappingRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetIdentityToBenefitPkgMappingResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.benefit_pkg_id):
            body['benefit_pkg_id'] = request.benefit_pkg_id
        if not DaraCore.is_null(request.identity_id):
            body['identity_id'] = request.identity_id
        if not DaraCore.is_null(request.identity_type):
            body['identity_type'] = request.identity_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetIdentityToBenefitPkgMapping',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/benefit/identity_to_benefit_pkg_mapping/get',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIdentityToBenefitPkgMappingResponse(),
            self.execute(params, req, runtime)
        )

    async def get_identity_to_benefit_pkg_mapping_with_options_async(
        self,
        request: main_models.GetIdentityToBenefitPkgMappingRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetIdentityToBenefitPkgMappingResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.benefit_pkg_id):
            body['benefit_pkg_id'] = request.benefit_pkg_id
        if not DaraCore.is_null(request.identity_id):
            body['identity_id'] = request.identity_id
        if not DaraCore.is_null(request.identity_type):
            body['identity_type'] = request.identity_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetIdentityToBenefitPkgMapping',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/benefit/identity_to_benefit_pkg_mapping/get',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIdentityToBenefitPkgMappingResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_identity_to_benefit_pkg_mapping(
        self,
        request: main_models.GetIdentityToBenefitPkgMappingRequest,
    ) -> main_models.GetIdentityToBenefitPkgMappingResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_identity_to_benefit_pkg_mapping_with_options(request, headers, runtime)

    async def get_identity_to_benefit_pkg_mapping_async(
        self,
        request: main_models.GetIdentityToBenefitPkgMappingRequest,
    ) -> main_models.GetIdentityToBenefitPkgMappingResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_identity_to_benefit_pkg_mapping_with_options_async(request, headers, runtime)

    def get_link_info_with_options(
        self,
        request: main_models.GetLinkInfoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLinkInfoResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.extra):
            body['extra'] = request.extra
        if not DaraCore.is_null(request.identity):
            body['identity'] = request.identity
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetLinkInfo',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/account/get_link_info',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLinkInfoResponse(),
            self.execute(params, req, runtime)
        )

    async def get_link_info_with_options_async(
        self,
        request: main_models.GetLinkInfoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLinkInfoResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.extra):
            body['extra'] = request.extra
        if not DaraCore.is_null(request.identity):
            body['identity'] = request.identity
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetLinkInfo',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/account/get_link_info',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLinkInfoResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_link_info(
        self,
        request: main_models.GetLinkInfoRequest,
    ) -> main_models.GetLinkInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_link_info_with_options(request, headers, runtime)

    async def get_link_info_async(
        self,
        request: main_models.GetLinkInfoRequest,
    ) -> main_models.GetLinkInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_link_info_with_options_async(request, headers, runtime)

    def get_link_info_by_user_id_with_options(
        self,
        request: main_models.GetLinkInfoByUserIdRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLinkInfoByUserIdResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.user_id):
            body['user_id'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetLinkInfoByUserId',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/account/get_link_info_by_user_id',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLinkInfoByUserIdResponse(),
            self.execute(params, req, runtime)
        )

    async def get_link_info_by_user_id_with_options_async(
        self,
        request: main_models.GetLinkInfoByUserIdRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLinkInfoByUserIdResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.user_id):
            body['user_id'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetLinkInfoByUserId',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/account/get_link_info_by_user_id',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLinkInfoByUserIdResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_link_info_by_user_id(
        self,
        request: main_models.GetLinkInfoByUserIdRequest,
    ) -> main_models.GetLinkInfoByUserIdResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_link_info_by_user_id_with_options(request, headers, runtime)

    async def get_link_info_by_user_id_async(
        self,
        request: main_models.GetLinkInfoByUserIdRequest,
    ) -> main_models.GetLinkInfoByUserIdResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_link_info_by_user_id_with_options_async(request, headers, runtime)

    def get_revision_with_options(
        self,
        request: main_models.GetRevisionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetRevisionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.fields):
            body['fields'] = request.fields
        if not DaraCore.is_null(request.file_id):
            body['file_id'] = request.file_id
        if not DaraCore.is_null(request.revision_id):
            body['revision_id'] = request.revision_id
        if not DaraCore.is_null(request.url_expire_sec):
            body['url_expire_sec'] = request.url_expire_sec
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetRevision',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/revision/get',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRevisionResponse(),
            self.execute(params, req, runtime)
        )

    async def get_revision_with_options_async(
        self,
        request: main_models.GetRevisionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetRevisionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.fields):
            body['fields'] = request.fields
        if not DaraCore.is_null(request.file_id):
            body['file_id'] = request.file_id
        if not DaraCore.is_null(request.revision_id):
            body['revision_id'] = request.revision_id
        if not DaraCore.is_null(request.url_expire_sec):
            body['url_expire_sec'] = request.url_expire_sec
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetRevision',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/revision/get',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRevisionResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_revision(
        self,
        request: main_models.GetRevisionRequest,
    ) -> main_models.GetRevisionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_revision_with_options(request, headers, runtime)

    async def get_revision_async(
        self,
        request: main_models.GetRevisionRequest,
    ) -> main_models.GetRevisionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_revision_with_options_async(request, headers, runtime)

    def get_share_link_with_options(
        self,
        request: main_models.GetShareLinkRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetShareLinkResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.share_id):
            body['share_id'] = request.share_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetShareLink',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/share_link/get',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetShareLinkResponse(),
            self.execute(params, req, runtime)
        )

    async def get_share_link_with_options_async(
        self,
        request: main_models.GetShareLinkRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetShareLinkResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.share_id):
            body['share_id'] = request.share_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetShareLink',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/share_link/get',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetShareLinkResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_share_link(
        self,
        request: main_models.GetShareLinkRequest,
    ) -> main_models.GetShareLinkResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_share_link_with_options(request, headers, runtime)

    async def get_share_link_async(
        self,
        request: main_models.GetShareLinkRequest,
    ) -> main_models.GetShareLinkResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_share_link_with_options_async(request, headers, runtime)

    def get_share_link_by_anonymous_with_options(
        self,
        request: main_models.GetShareLinkByAnonymousRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetShareLinkByAnonymousResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.share_id):
            body['share_id'] = request.share_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetShareLinkByAnonymous',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/share_link/get_by_anonymous',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetShareLinkByAnonymousResponse(),
            self.execute(params, req, runtime)
        )

    async def get_share_link_by_anonymous_with_options_async(
        self,
        request: main_models.GetShareLinkByAnonymousRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetShareLinkByAnonymousResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.share_id):
            body['share_id'] = request.share_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetShareLinkByAnonymous',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/share_link/get_by_anonymous',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetShareLinkByAnonymousResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_share_link_by_anonymous(
        self,
        request: main_models.GetShareLinkByAnonymousRequest,
    ) -> main_models.GetShareLinkByAnonymousResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_share_link_by_anonymous_with_options(request, headers, runtime)

    async def get_share_link_by_anonymous_async(
        self,
        request: main_models.GetShareLinkByAnonymousRequest,
    ) -> main_models.GetShareLinkByAnonymousResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_share_link_by_anonymous_with_options_async(request, headers, runtime)

    def get_share_link_token_with_options(
        self,
        request: main_models.GetShareLinkTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetShareLinkTokenResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.expire_sec):
            body['expire_sec'] = request.expire_sec
        if not DaraCore.is_null(request.share_id):
            body['share_id'] = request.share_id
        if not DaraCore.is_null(request.share_pwd):
            body['share_pwd'] = request.share_pwd
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetShareLinkToken',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/share_link/get_share_token',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetShareLinkTokenResponse(),
            self.execute(params, req, runtime)
        )

    async def get_share_link_token_with_options_async(
        self,
        request: main_models.GetShareLinkTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetShareLinkTokenResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.expire_sec):
            body['expire_sec'] = request.expire_sec
        if not DaraCore.is_null(request.share_id):
            body['share_id'] = request.share_id
        if not DaraCore.is_null(request.share_pwd):
            body['share_pwd'] = request.share_pwd
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetShareLinkToken',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/share_link/get_share_token',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetShareLinkTokenResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_share_link_token(
        self,
        request: main_models.GetShareLinkTokenRequest,
    ) -> main_models.GetShareLinkTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_share_link_token_with_options(request, headers, runtime)

    async def get_share_link_token_async(
        self,
        request: main_models.GetShareLinkTokenRequest,
    ) -> main_models.GetShareLinkTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_share_link_token_with_options_async(request, headers, runtime)

    def get_story_with_options(
        self,
        request: main_models.GetStoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetStoryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cover_image_thumbnail_process):
            body['cover_image_thumbnail_process'] = request.cover_image_thumbnail_process
        if not DaraCore.is_null(request.cover_video_thumbnail_process):
            body['cover_video_thumbnail_process'] = request.cover_video_thumbnail_process
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.image_thumbnail_process):
            body['image_thumbnail_process'] = request.image_thumbnail_process
        if not DaraCore.is_null(request.image_url_process):
            body['image_url_process'] = request.image_url_process
        if not DaraCore.is_null(request.story_id):
            body['story_id'] = request.story_id
        if not DaraCore.is_null(request.url_expire_sec):
            body['url_expire_sec'] = request.url_expire_sec
        if not DaraCore.is_null(request.video_thumbnail_process):
            body['video_thumbnail_process'] = request.video_thumbnail_process
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetStory',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/image/get_story',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStoryResponse(),
            self.execute(params, req, runtime)
        )

    async def get_story_with_options_async(
        self,
        request: main_models.GetStoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetStoryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cover_image_thumbnail_process):
            body['cover_image_thumbnail_process'] = request.cover_image_thumbnail_process
        if not DaraCore.is_null(request.cover_video_thumbnail_process):
            body['cover_video_thumbnail_process'] = request.cover_video_thumbnail_process
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.image_thumbnail_process):
            body['image_thumbnail_process'] = request.image_thumbnail_process
        if not DaraCore.is_null(request.image_url_process):
            body['image_url_process'] = request.image_url_process
        if not DaraCore.is_null(request.story_id):
            body['story_id'] = request.story_id
        if not DaraCore.is_null(request.url_expire_sec):
            body['url_expire_sec'] = request.url_expire_sec
        if not DaraCore.is_null(request.video_thumbnail_process):
            body['video_thumbnail_process'] = request.video_thumbnail_process
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetStory',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/image/get_story',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStoryResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_story(
        self,
        request: main_models.GetStoryRequest,
    ) -> main_models.GetStoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_story_with_options(request, headers, runtime)

    async def get_story_async(
        self,
        request: main_models.GetStoryRequest,
    ) -> main_models.GetStoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_story_with_options_async(request, headers, runtime)

    def get_task_status_with_options(
        self,
        request: main_models.GetTaskStatusRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTaskStatusResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.task_id):
            body['task_id'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetTaskStatus',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/image/get_task_status',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTaskStatusResponse(),
            self.execute(params, req, runtime)
        )

    async def get_task_status_with_options_async(
        self,
        request: main_models.GetTaskStatusRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTaskStatusResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.task_id):
            body['task_id'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetTaskStatus',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/image/get_task_status',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTaskStatusResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_task_status(
        self,
        request: main_models.GetTaskStatusRequest,
    ) -> main_models.GetTaskStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_task_status_with_options(request, headers, runtime)

    async def get_task_status_async(
        self,
        request: main_models.GetTaskStatusRequest,
    ) -> main_models.GetTaskStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_task_status_with_options_async(request, headers, runtime)

    def get_upload_url_with_options(
        self,
        request: main_models.GetUploadUrlRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetUploadUrlResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.file_id):
            body['file_id'] = request.file_id
        if not DaraCore.is_null(request.part_info_list):
            body['part_info_list'] = request.part_info_list
        if not DaraCore.is_null(request.share_id):
            body['share_id'] = request.share_id
        if not DaraCore.is_null(request.upload_id):
            body['upload_id'] = request.upload_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetUploadUrl',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/get_upload_url',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUploadUrlResponse(),
            self.execute(params, req, runtime)
        )

    async def get_upload_url_with_options_async(
        self,
        request: main_models.GetUploadUrlRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetUploadUrlResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.file_id):
            body['file_id'] = request.file_id
        if not DaraCore.is_null(request.part_info_list):
            body['part_info_list'] = request.part_info_list
        if not DaraCore.is_null(request.share_id):
            body['share_id'] = request.share_id
        if not DaraCore.is_null(request.upload_id):
            body['upload_id'] = request.upload_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetUploadUrl',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/get_upload_url',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUploadUrlResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_upload_url(
        self,
        request: main_models.GetUploadUrlRequest,
    ) -> main_models.GetUploadUrlResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_upload_url_with_options(request, headers, runtime)

    async def get_upload_url_async(
        self,
        request: main_models.GetUploadUrlRequest,
    ) -> main_models.GetUploadUrlResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_upload_url_with_options_async(request, headers, runtime)

    def get_user_with_options(
        self,
        request: main_models.GetUserRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetUserResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.user_id):
            body['user_id'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetUser',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/user/get',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserResponse(),
            self.execute(params, req, runtime)
        )

    async def get_user_with_options_async(
        self,
        request: main_models.GetUserRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetUserResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.user_id):
            body['user_id'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetUser',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/user/get',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_user(
        self,
        request: main_models.GetUserRequest,
    ) -> main_models.GetUserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_user_with_options(request, headers, runtime)

    async def get_user_async(
        self,
        request: main_models.GetUserRequest,
    ) -> main_models.GetUserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_user_with_options_async(request, headers, runtime)

    def get_video_preview_play_info_with_options(
        self,
        request: main_models.GetVideoPreviewPlayInfoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetVideoPreviewPlayInfoResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.category):
            body['category'] = request.category
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.file_id):
            body['file_id'] = request.file_id
        if not DaraCore.is_null(request.get_master_url):
            body['get_master_url'] = request.get_master_url
        if not DaraCore.is_null(request.get_without_url):
            body['get_without_url'] = request.get_without_url
        if not DaraCore.is_null(request.re_transcode):
            body['re_transcode'] = request.re_transcode
        if not DaraCore.is_null(request.share_id):
            body['share_id'] = request.share_id
        if not DaraCore.is_null(request.template_id):
            body['template_id'] = request.template_id
        if not DaraCore.is_null(request.url_expire_sec):
            body['url_expire_sec'] = request.url_expire_sec
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetVideoPreviewPlayInfo',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/get_video_preview_play_info',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVideoPreviewPlayInfoResponse(),
            self.execute(params, req, runtime)
        )

    async def get_video_preview_play_info_with_options_async(
        self,
        request: main_models.GetVideoPreviewPlayInfoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetVideoPreviewPlayInfoResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.category):
            body['category'] = request.category
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.file_id):
            body['file_id'] = request.file_id
        if not DaraCore.is_null(request.get_master_url):
            body['get_master_url'] = request.get_master_url
        if not DaraCore.is_null(request.get_without_url):
            body['get_without_url'] = request.get_without_url
        if not DaraCore.is_null(request.re_transcode):
            body['re_transcode'] = request.re_transcode
        if not DaraCore.is_null(request.share_id):
            body['share_id'] = request.share_id
        if not DaraCore.is_null(request.template_id):
            body['template_id'] = request.template_id
        if not DaraCore.is_null(request.url_expire_sec):
            body['url_expire_sec'] = request.url_expire_sec
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetVideoPreviewPlayInfo',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/get_video_preview_play_info',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVideoPreviewPlayInfoResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_video_preview_play_info(
        self,
        request: main_models.GetVideoPreviewPlayInfoRequest,
    ) -> main_models.GetVideoPreviewPlayInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_video_preview_play_info_with_options(request, headers, runtime)

    async def get_video_preview_play_info_async(
        self,
        request: main_models.GetVideoPreviewPlayInfoRequest,
    ) -> main_models.GetVideoPreviewPlayInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_video_preview_play_info_with_options_async(request, headers, runtime)

    def get_video_preview_play_meta_with_options(
        self,
        request: main_models.GetVideoPreviewPlayMetaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetVideoPreviewPlayMetaResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.category):
            body['category'] = request.category
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.file_id):
            body['file_id'] = request.file_id
        if not DaraCore.is_null(request.share_id):
            body['share_id'] = request.share_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetVideoPreviewPlayMeta',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/get_video_preview_play_meta',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVideoPreviewPlayMetaResponse(),
            self.execute(params, req, runtime)
        )

    async def get_video_preview_play_meta_with_options_async(
        self,
        request: main_models.GetVideoPreviewPlayMetaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetVideoPreviewPlayMetaResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.category):
            body['category'] = request.category
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.file_id):
            body['file_id'] = request.file_id
        if not DaraCore.is_null(request.share_id):
            body['share_id'] = request.share_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetVideoPreviewPlayMeta',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/get_video_preview_play_meta',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVideoPreviewPlayMetaResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_video_preview_play_meta(
        self,
        request: main_models.GetVideoPreviewPlayMetaRequest,
    ) -> main_models.GetVideoPreviewPlayMetaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_video_preview_play_meta_with_options(request, headers, runtime)

    async def get_video_preview_play_meta_async(
        self,
        request: main_models.GetVideoPreviewPlayMetaRequest,
    ) -> main_models.GetVideoPreviewPlayMetaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_video_preview_play_meta_with_options_async(request, headers, runtime)

    def group_update_name_with_options(
        self,
        request: main_models.GroupUpdateNameRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GroupUpdateNameResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.group_id):
            body['group_id'] = request.group_id
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GroupUpdateName',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/group/update_name',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GroupUpdateNameResponse(),
            self.execute(params, req, runtime)
        )

    async def group_update_name_with_options_async(
        self,
        request: main_models.GroupUpdateNameRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GroupUpdateNameResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.group_id):
            body['group_id'] = request.group_id
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GroupUpdateName',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/group/update_name',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GroupUpdateNameResponse(),
            await self.execute_async(params, req, runtime)
        )

    def group_update_name(
        self,
        request: main_models.GroupUpdateNameRequest,
    ) -> main_models.GroupUpdateNameResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.group_update_name_with_options(request, headers, runtime)

    async def group_update_name_async(
        self,
        request: main_models.GroupUpdateNameRequest,
    ) -> main_models.GroupUpdateNameResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.group_update_name_with_options_async(request, headers, runtime)

    def import_user_with_options(
        self,
        request: main_models.ImportUserRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ImportUserResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.authentication_display_name):
            body['authentication_display_name'] = request.authentication_display_name
        if not DaraCore.is_null(request.authentication_type):
            body['authentication_type'] = request.authentication_type
        if not DaraCore.is_null(request.auto_create_drive):
            body['auto_create_drive'] = request.auto_create_drive
        if not DaraCore.is_null(request.drive_total_size):
            body['drive_total_size'] = request.drive_total_size
        if not DaraCore.is_null(request.extra):
            body['extra'] = request.extra
        if not DaraCore.is_null(request.identity):
            body['identity'] = request.identity
        if not DaraCore.is_null(request.nick_name):
            body['nick_name'] = request.nick_name
        if not DaraCore.is_null(request.parent_group_id):
            body['parent_group_id'] = request.parent_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ImportUser',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/user/import',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportUserResponse(),
            self.execute(params, req, runtime)
        )

    async def import_user_with_options_async(
        self,
        request: main_models.ImportUserRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ImportUserResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.authentication_display_name):
            body['authentication_display_name'] = request.authentication_display_name
        if not DaraCore.is_null(request.authentication_type):
            body['authentication_type'] = request.authentication_type
        if not DaraCore.is_null(request.auto_create_drive):
            body['auto_create_drive'] = request.auto_create_drive
        if not DaraCore.is_null(request.drive_total_size):
            body['drive_total_size'] = request.drive_total_size
        if not DaraCore.is_null(request.extra):
            body['extra'] = request.extra
        if not DaraCore.is_null(request.identity):
            body['identity'] = request.identity
        if not DaraCore.is_null(request.nick_name):
            body['nick_name'] = request.nick_name
        if not DaraCore.is_null(request.parent_group_id):
            body['parent_group_id'] = request.parent_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ImportUser',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/user/import',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportUserResponse(),
            await self.execute_async(params, req, runtime)
        )

    def import_user(
        self,
        request: main_models.ImportUserRequest,
    ) -> main_models.ImportUserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.import_user_with_options(request, headers, runtime)

    async def import_user_async(
        self,
        request: main_models.ImportUserRequest,
    ) -> main_models.ImportUserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.import_user_with_options_async(request, headers, runtime)

    def investigate_file_with_options(
        self,
        request: main_models.InvestigateFileRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InvestigateFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_file_ids):
            body['drive_file_ids'] = request.drive_file_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'InvestigateFile',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/csi/investigate_file',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InvestigateFileResponse(),
            self.execute(params, req, runtime)
        )

    async def investigate_file_with_options_async(
        self,
        request: main_models.InvestigateFileRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InvestigateFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_file_ids):
            body['drive_file_ids'] = request.drive_file_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'InvestigateFile',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/csi/investigate_file',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InvestigateFileResponse(),
            await self.execute_async(params, req, runtime)
        )

    def investigate_file(
        self,
        request: main_models.InvestigateFileRequest,
    ) -> main_models.InvestigateFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.investigate_file_with_options(request, headers, runtime)

    async def investigate_file_async(
        self,
        request: main_models.InvestigateFileRequest,
    ) -> main_models.InvestigateFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.investigate_file_with_options_async(request, headers, runtime)

    def link_account_with_options(
        self,
        request: main_models.LinkAccountRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.LinkAccountResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.extra):
            body['extra'] = request.extra
        if not DaraCore.is_null(request.identity):
            body['identity'] = request.identity
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        if not DaraCore.is_null(request.user_id):
            body['user_id'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'LinkAccount',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/account/link',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LinkAccountResponse(),
            self.execute(params, req, runtime)
        )

    async def link_account_with_options_async(
        self,
        request: main_models.LinkAccountRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.LinkAccountResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.extra):
            body['extra'] = request.extra
        if not DaraCore.is_null(request.identity):
            body['identity'] = request.identity
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        if not DaraCore.is_null(request.user_id):
            body['user_id'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'LinkAccount',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/account/link',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LinkAccountResponse(),
            await self.execute_async(params, req, runtime)
        )

    def link_account(
        self,
        request: main_models.LinkAccountRequest,
    ) -> main_models.LinkAccountResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.link_account_with_options(request, headers, runtime)

    async def link_account_async(
        self,
        request: main_models.LinkAccountRequest,
    ) -> main_models.LinkAccountResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.link_account_with_options_async(request, headers, runtime)

    def list_address_groups_with_options(
        self,
        request: main_models.ListAddressGroupsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAddressGroupsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.image_thumbnail_process):
            body['image_thumbnail_process'] = request.image_thumbnail_process
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.marker):
            body['marker'] = request.marker
        if not DaraCore.is_null(request.video_thumbnail_process):
            body['video_thumbnail_process'] = request.video_thumbnail_process
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAddressGroups',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/image/list_address_groups',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAddressGroupsResponse(),
            self.execute(params, req, runtime)
        )

    async def list_address_groups_with_options_async(
        self,
        request: main_models.ListAddressGroupsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAddressGroupsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.image_thumbnail_process):
            body['image_thumbnail_process'] = request.image_thumbnail_process
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.marker):
            body['marker'] = request.marker
        if not DaraCore.is_null(request.video_thumbnail_process):
            body['video_thumbnail_process'] = request.video_thumbnail_process
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAddressGroups',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/image/list_address_groups',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAddressGroupsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_address_groups(
        self,
        request: main_models.ListAddressGroupsRequest,
    ) -> main_models.ListAddressGroupsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_address_groups_with_options(request, headers, runtime)

    async def list_address_groups_async(
        self,
        request: main_models.ListAddressGroupsRequest,
    ) -> main_models.ListAddressGroupsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_address_groups_with_options_async(request, headers, runtime)

    def list_assignment_with_options(
        self,
        request: main_models.ListAssignmentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAssignmentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.manage_resource_id):
            body['manage_resource_id'] = request.manage_resource_id
        if not DaraCore.is_null(request.manage_resource_type):
            body['manage_resource_type'] = request.manage_resource_type
        if not DaraCore.is_null(request.marker):
            body['marker'] = request.marker
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAssignment',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/role/list_assignment',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAssignmentResponse(),
            self.execute(params, req, runtime)
        )

    async def list_assignment_with_options_async(
        self,
        request: main_models.ListAssignmentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAssignmentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.manage_resource_id):
            body['manage_resource_id'] = request.manage_resource_id
        if not DaraCore.is_null(request.manage_resource_type):
            body['manage_resource_type'] = request.manage_resource_type
        if not DaraCore.is_null(request.marker):
            body['marker'] = request.marker
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAssignment',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/role/list_assignment',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAssignmentResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_assignment(
        self,
        request: main_models.ListAssignmentRequest,
    ) -> main_models.ListAssignmentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_assignment_with_options(request, headers, runtime)

    async def list_assignment_async(
        self,
        request: main_models.ListAssignmentRequest,
    ) -> main_models.ListAssignmentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_assignment_with_options_async(request, headers, runtime)

    def list_delta_with_options(
        self,
        request: main_models.ListDeltaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDeltaResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cursor):
            body['cursor'] = request.cursor
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.sync_root_id):
            body['sync_root_id'] = request.sync_root_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDelta',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/list_delta',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDeltaResponse(),
            self.execute(params, req, runtime)
        )

    async def list_delta_with_options_async(
        self,
        request: main_models.ListDeltaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDeltaResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cursor):
            body['cursor'] = request.cursor
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.sync_root_id):
            body['sync_root_id'] = request.sync_root_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDelta',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/list_delta',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDeltaResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_delta(
        self,
        request: main_models.ListDeltaRequest,
    ) -> main_models.ListDeltaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_delta_with_options(request, headers, runtime)

    async def list_delta_async(
        self,
        request: main_models.ListDeltaRequest,
    ) -> main_models.ListDeltaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_delta_with_options_async(request, headers, runtime)

    def list_domains_with_options(
        self,
        request: main_models.ListDomainsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDomainsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.marker):
            body['marker'] = request.marker
        if not DaraCore.is_null(request.parent_domain_id):
            body['parent_domain_id'] = request.parent_domain_id
        if not DaraCore.is_null(request.service_code):
            body['service_code'] = request.service_code
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDomains',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/domain/list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDomainsResponse(),
            self.execute(params, req, runtime)
        )

    async def list_domains_with_options_async(
        self,
        request: main_models.ListDomainsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDomainsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.marker):
            body['marker'] = request.marker
        if not DaraCore.is_null(request.parent_domain_id):
            body['parent_domain_id'] = request.parent_domain_id
        if not DaraCore.is_null(request.service_code):
            body['service_code'] = request.service_code
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDomains',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/domain/list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDomainsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_domains(
        self,
        request: main_models.ListDomainsRequest,
    ) -> main_models.ListDomainsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_domains_with_options(request, headers, runtime)

    async def list_domains_async(
        self,
        request: main_models.ListDomainsRequest,
    ) -> main_models.ListDomainsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_domains_with_options_async(request, headers, runtime)

    def list_drive_with_options(
        self,
        request: main_models.ListDriveRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDriveResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.marker):
            body['marker'] = request.marker
        if not DaraCore.is_null(request.owner):
            body['owner'] = request.owner
        if not DaraCore.is_null(request.owner_type):
            body['owner_type'] = request.owner_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDrive',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/drive/list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDriveResponse(),
            self.execute(params, req, runtime)
        )

    async def list_drive_with_options_async(
        self,
        request: main_models.ListDriveRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDriveResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.marker):
            body['marker'] = request.marker
        if not DaraCore.is_null(request.owner):
            body['owner'] = request.owner
        if not DaraCore.is_null(request.owner_type):
            body['owner_type'] = request.owner_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDrive',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/drive/list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDriveResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_drive(
        self,
        request: main_models.ListDriveRequest,
    ) -> main_models.ListDriveResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_drive_with_options(request, headers, runtime)

    async def list_drive_async(
        self,
        request: main_models.ListDriveRequest,
    ) -> main_models.ListDriveResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_drive_with_options_async(request, headers, runtime)

    def list_facegroups_with_options(
        self,
        request: main_models.ListFacegroupsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListFacegroupsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.marker):
            body['marker'] = request.marker
        if not DaraCore.is_null(request.remarks):
            body['remarks'] = request.remarks
        if not DaraCore.is_null(request.return_total_count):
            body['return_total_count'] = request.return_total_count
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListFacegroups',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/image/list_facegroups',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFacegroupsResponse(),
            self.execute(params, req, runtime)
        )

    async def list_facegroups_with_options_async(
        self,
        request: main_models.ListFacegroupsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListFacegroupsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.marker):
            body['marker'] = request.marker
        if not DaraCore.is_null(request.remarks):
            body['remarks'] = request.remarks
        if not DaraCore.is_null(request.return_total_count):
            body['return_total_count'] = request.return_total_count
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListFacegroups',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/image/list_facegroups',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFacegroupsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_facegroups(
        self,
        request: main_models.ListFacegroupsRequest,
    ) -> main_models.ListFacegroupsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_facegroups_with_options(request, headers, runtime)

    async def list_facegroups_async(
        self,
        request: main_models.ListFacegroupsRequest,
    ) -> main_models.ListFacegroupsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_facegroups_with_options_async(request, headers, runtime)

    def list_file_with_options(
        self,
        request: main_models.ListFileRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.category):
            body['category'] = request.category
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.fields):
            body['fields'] = request.fields
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.marker):
            body['marker'] = request.marker
        if not DaraCore.is_null(request.order_by):
            body['order_by'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            body['order_direction'] = request.order_direction
        if not DaraCore.is_null(request.parent_file_id):
            body['parent_file_id'] = request.parent_file_id
        if not DaraCore.is_null(request.share_id):
            body['share_id'] = request.share_id
        if not DaraCore.is_null(request.status):
            body['status'] = request.status
        if not DaraCore.is_null(request.thumbnail_processes):
            body['thumbnail_processes'] = request.thumbnail_processes
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListFile',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFileResponse(),
            self.execute(params, req, runtime)
        )

    async def list_file_with_options_async(
        self,
        request: main_models.ListFileRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.category):
            body['category'] = request.category
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.fields):
            body['fields'] = request.fields
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.marker):
            body['marker'] = request.marker
        if not DaraCore.is_null(request.order_by):
            body['order_by'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            body['order_direction'] = request.order_direction
        if not DaraCore.is_null(request.parent_file_id):
            body['parent_file_id'] = request.parent_file_id
        if not DaraCore.is_null(request.share_id):
            body['share_id'] = request.share_id
        if not DaraCore.is_null(request.status):
            body['status'] = request.status
        if not DaraCore.is_null(request.thumbnail_processes):
            body['thumbnail_processes'] = request.thumbnail_processes
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListFile',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFileResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_file(
        self,
        request: main_models.ListFileRequest,
    ) -> main_models.ListFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_file_with_options(request, headers, runtime)

    async def list_file_async(
        self,
        request: main_models.ListFileRequest,
    ) -> main_models.ListFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_file_with_options_async(request, headers, runtime)

    def list_group_with_options(
        self,
        request: main_models.ListGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.marker):
            body['marker'] = request.marker
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListGroup',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/group/list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGroupResponse(),
            self.execute(params, req, runtime)
        )

    async def list_group_with_options_async(
        self,
        request: main_models.ListGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.marker):
            body['marker'] = request.marker
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListGroup',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/group/list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGroupResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_group(
        self,
        request: main_models.ListGroupRequest,
    ) -> main_models.ListGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_group_with_options(request, headers, runtime)

    async def list_group_async(
        self,
        request: main_models.ListGroupRequest,
    ) -> main_models.ListGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_group_with_options_async(request, headers, runtime)

    def list_group_member_with_options(
        self,
        request: main_models.ListGroupMemberRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListGroupMemberResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.group_id):
            body['group_id'] = request.group_id
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.marker):
            body['marker'] = request.marker
        if not DaraCore.is_null(request.member_type):
            body['member_type'] = request.member_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListGroupMember',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/group/list_member',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGroupMemberResponse(),
            self.execute(params, req, runtime)
        )

    async def list_group_member_with_options_async(
        self,
        request: main_models.ListGroupMemberRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListGroupMemberResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.group_id):
            body['group_id'] = request.group_id
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.marker):
            body['marker'] = request.marker
        if not DaraCore.is_null(request.member_type):
            body['member_type'] = request.member_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListGroupMember',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/group/list_member',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGroupMemberResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_group_member(
        self,
        request: main_models.ListGroupMemberRequest,
    ) -> main_models.ListGroupMemberResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_group_member_with_options(request, headers, runtime)

    async def list_group_member_async(
        self,
        request: main_models.ListGroupMemberRequest,
    ) -> main_models.ListGroupMemberResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_group_member_with_options_async(request, headers, runtime)

    def list_identity_role_with_options(
        self,
        request: main_models.ListIdentityRoleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListIdentityRoleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.identity):
            body['identity'] = request.identity
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListIdentityRole',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/role/list_identity_role',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIdentityRoleResponse(),
            self.execute(params, req, runtime)
        )

    async def list_identity_role_with_options_async(
        self,
        request: main_models.ListIdentityRoleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListIdentityRoleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.identity):
            body['identity'] = request.identity
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListIdentityRole',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/role/list_identity_role',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIdentityRoleResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_identity_role(
        self,
        request: main_models.ListIdentityRoleRequest,
    ) -> main_models.ListIdentityRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_identity_role_with_options(request, headers, runtime)

    async def list_identity_role_async(
        self,
        request: main_models.ListIdentityRoleRequest,
    ) -> main_models.ListIdentityRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_identity_role_with_options_async(request, headers, runtime)

    def list_identity_to_benefit_pkg_mapping_with_options(
        self,
        request: main_models.ListIdentityToBenefitPkgMappingRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListIdentityToBenefitPkgMappingResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.identity_id):
            body['identity_id'] = request.identity_id
        if not DaraCore.is_null(request.identity_type):
            body['identity_type'] = request.identity_type
        if not DaraCore.is_null(request.include_expired):
            body['include_expired'] = request.include_expired
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListIdentityToBenefitPkgMapping',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/benefit/identity_to_benefit_pkg_mapping/list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIdentityToBenefitPkgMappingResponse(),
            self.execute(params, req, runtime)
        )

    async def list_identity_to_benefit_pkg_mapping_with_options_async(
        self,
        request: main_models.ListIdentityToBenefitPkgMappingRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListIdentityToBenefitPkgMappingResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.identity_id):
            body['identity_id'] = request.identity_id
        if not DaraCore.is_null(request.identity_type):
            body['identity_type'] = request.identity_type
        if not DaraCore.is_null(request.include_expired):
            body['include_expired'] = request.include_expired
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListIdentityToBenefitPkgMapping',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/benefit/identity_to_benefit_pkg_mapping/list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIdentityToBenefitPkgMappingResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_identity_to_benefit_pkg_mapping(
        self,
        request: main_models.ListIdentityToBenefitPkgMappingRequest,
    ) -> main_models.ListIdentityToBenefitPkgMappingResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_identity_to_benefit_pkg_mapping_with_options(request, headers, runtime)

    async def list_identity_to_benefit_pkg_mapping_async(
        self,
        request: main_models.ListIdentityToBenefitPkgMappingRequest,
    ) -> main_models.ListIdentityToBenefitPkgMappingResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_identity_to_benefit_pkg_mapping_with_options_async(request, headers, runtime)

    def list_my_drives_with_options(
        self,
        request: main_models.ListMyDrivesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMyDrivesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.marker):
            body['marker'] = request.marker
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListMyDrives',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/drive/list_my_drives',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMyDrivesResponse(),
            self.execute(params, req, runtime)
        )

    async def list_my_drives_with_options_async(
        self,
        request: main_models.ListMyDrivesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMyDrivesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.marker):
            body['marker'] = request.marker
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListMyDrives',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/drive/list_my_drives',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMyDrivesResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_my_drives(
        self,
        request: main_models.ListMyDrivesRequest,
    ) -> main_models.ListMyDrivesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_my_drives_with_options(request, headers, runtime)

    async def list_my_drives_async(
        self,
        request: main_models.ListMyDrivesRequest,
    ) -> main_models.ListMyDrivesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_my_drives_with_options_async(request, headers, runtime)

    def list_my_group_drive_with_options(
        self,
        request: main_models.ListMyGroupDriveRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMyGroupDriveResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_name):
            body['drive_name'] = request.drive_name
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.marker):
            body['marker'] = request.marker
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListMyGroupDrive',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/drive/list_my_group_drive',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMyGroupDriveResponse(),
            self.execute(params, req, runtime)
        )

    async def list_my_group_drive_with_options_async(
        self,
        request: main_models.ListMyGroupDriveRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMyGroupDriveResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_name):
            body['drive_name'] = request.drive_name
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.marker):
            body['marker'] = request.marker
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListMyGroupDrive',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/drive/list_my_group_drive',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMyGroupDriveResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_my_group_drive(
        self,
        request: main_models.ListMyGroupDriveRequest,
    ) -> main_models.ListMyGroupDriveResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_my_group_drive_with_options(request, headers, runtime)

    async def list_my_group_drive_async(
        self,
        request: main_models.ListMyGroupDriveRequest,
    ) -> main_models.ListMyGroupDriveResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_my_group_drive_with_options_async(request, headers, runtime)

    def list_received_file_with_options(
        self,
        request: main_models.ListReceivedFileRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListReceivedFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.marker):
            body['marker'] = request.marker
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListReceivedFile',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/list_received_file',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListReceivedFileResponse(),
            self.execute(params, req, runtime)
        )

    async def list_received_file_with_options_async(
        self,
        request: main_models.ListReceivedFileRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListReceivedFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.marker):
            body['marker'] = request.marker
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListReceivedFile',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/list_received_file',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListReceivedFileResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_received_file(
        self,
        request: main_models.ListReceivedFileRequest,
    ) -> main_models.ListReceivedFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_received_file_with_options(request, headers, runtime)

    async def list_received_file_async(
        self,
        request: main_models.ListReceivedFileRequest,
    ) -> main_models.ListReceivedFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_received_file_with_options_async(request, headers, runtime)

    def list_recyclebin_with_options(
        self,
        request: main_models.ListRecyclebinRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListRecyclebinResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.fields):
            body['fields'] = request.fields
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.marker):
            body['marker'] = request.marker
        if not DaraCore.is_null(request.thumbnail_processes):
            body['thumbnail_processes'] = request.thumbnail_processes
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListRecyclebin',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/recyclebin/list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRecyclebinResponse(),
            self.execute(params, req, runtime)
        )

    async def list_recyclebin_with_options_async(
        self,
        request: main_models.ListRecyclebinRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListRecyclebinResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.fields):
            body['fields'] = request.fields
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.marker):
            body['marker'] = request.marker
        if not DaraCore.is_null(request.thumbnail_processes):
            body['thumbnail_processes'] = request.thumbnail_processes
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListRecyclebin',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/recyclebin/list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRecyclebinResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_recyclebin(
        self,
        request: main_models.ListRecyclebinRequest,
    ) -> main_models.ListRecyclebinResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_recyclebin_with_options(request, headers, runtime)

    async def list_recyclebin_async(
        self,
        request: main_models.ListRecyclebinRequest,
    ) -> main_models.ListRecyclebinResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_recyclebin_with_options_async(request, headers, runtime)

    def list_revision_with_options(
        self,
        request: main_models.ListRevisionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListRevisionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.fields):
            body['fields'] = request.fields
        if not DaraCore.is_null(request.file_id):
            body['file_id'] = request.file_id
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.marker):
            body['marker'] = request.marker
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListRevision',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/revision/list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRevisionResponse(),
            self.execute(params, req, runtime)
        )

    async def list_revision_with_options_async(
        self,
        request: main_models.ListRevisionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListRevisionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.fields):
            body['fields'] = request.fields
        if not DaraCore.is_null(request.file_id):
            body['file_id'] = request.file_id
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.marker):
            body['marker'] = request.marker
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListRevision',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/revision/list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRevisionResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_revision(
        self,
        request: main_models.ListRevisionRequest,
    ) -> main_models.ListRevisionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_revision_with_options(request, headers, runtime)

    async def list_revision_async(
        self,
        request: main_models.ListRevisionRequest,
    ) -> main_models.ListRevisionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_revision_with_options_async(request, headers, runtime)

    def list_share_link_with_options(
        self,
        request: main_models.ListShareLinkRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListShareLinkResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.creator):
            body['creator'] = request.creator
        if not DaraCore.is_null(request.include_cancelled):
            body['include_cancelled'] = request.include_cancelled
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.marker):
            body['marker'] = request.marker
        if not DaraCore.is_null(request.order_by):
            body['order_by'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            body['order_direction'] = request.order_direction
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListShareLink',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/share_link/list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListShareLinkResponse(),
            self.execute(params, req, runtime)
        )

    async def list_share_link_with_options_async(
        self,
        request: main_models.ListShareLinkRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListShareLinkResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.creator):
            body['creator'] = request.creator
        if not DaraCore.is_null(request.include_cancelled):
            body['include_cancelled'] = request.include_cancelled
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.marker):
            body['marker'] = request.marker
        if not DaraCore.is_null(request.order_by):
            body['order_by'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            body['order_direction'] = request.order_direction
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListShareLink',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/share_link/list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListShareLinkResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_share_link(
        self,
        request: main_models.ListShareLinkRequest,
    ) -> main_models.ListShareLinkResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_share_link_with_options(request, headers, runtime)

    async def list_share_link_async(
        self,
        request: main_models.ListShareLinkRequest,
    ) -> main_models.ListShareLinkResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_share_link_with_options_async(request, headers, runtime)

    def list_tags_with_options(
        self,
        request: main_models.ListTagsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTagsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.image_thumbnail_process):
            body['image_thumbnail_process'] = request.image_thumbnail_process
        if not DaraCore.is_null(request.video_thumbnail_process):
            body['video_thumbnail_process'] = request.video_thumbnail_process
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListTags',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/image/list_tags',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagsResponse(),
            self.execute(params, req, runtime)
        )

    async def list_tags_with_options_async(
        self,
        request: main_models.ListTagsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTagsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.image_thumbnail_process):
            body['image_thumbnail_process'] = request.image_thumbnail_process
        if not DaraCore.is_null(request.video_thumbnail_process):
            body['video_thumbnail_process'] = request.video_thumbnail_process
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListTags',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/image/list_tags',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_tags(
        self,
        request: main_models.ListTagsRequest,
    ) -> main_models.ListTagsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_tags_with_options(request, headers, runtime)

    async def list_tags_async(
        self,
        request: main_models.ListTagsRequest,
    ) -> main_models.ListTagsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_tags_with_options_async(request, headers, runtime)

    def list_uploaded_parts_with_options(
        self,
        request: main_models.ListUploadedPartsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListUploadedPartsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.file_id):
            body['file_id'] = request.file_id
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.part_number_marker):
            body['part_number_marker'] = request.part_number_marker
        if not DaraCore.is_null(request.share_id):
            body['share_id'] = request.share_id
        if not DaraCore.is_null(request.upload_id):
            body['upload_id'] = request.upload_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListUploadedParts',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/list_uploaded_parts',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUploadedPartsResponse(),
            self.execute(params, req, runtime)
        )

    async def list_uploaded_parts_with_options_async(
        self,
        request: main_models.ListUploadedPartsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListUploadedPartsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.file_id):
            body['file_id'] = request.file_id
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.part_number_marker):
            body['part_number_marker'] = request.part_number_marker
        if not DaraCore.is_null(request.share_id):
            body['share_id'] = request.share_id
        if not DaraCore.is_null(request.upload_id):
            body['upload_id'] = request.upload_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListUploadedParts',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/list_uploaded_parts',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUploadedPartsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_uploaded_parts(
        self,
        request: main_models.ListUploadedPartsRequest,
    ) -> main_models.ListUploadedPartsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_uploaded_parts_with_options(request, headers, runtime)

    async def list_uploaded_parts_async(
        self,
        request: main_models.ListUploadedPartsRequest,
    ) -> main_models.ListUploadedPartsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_uploaded_parts_with_options_async(request, headers, runtime)

    def list_user_with_options(
        self,
        request: main_models.ListUserRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListUserResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.marker):
            body['marker'] = request.marker
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListUser',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/user/list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserResponse(),
            self.execute(params, req, runtime)
        )

    async def list_user_with_options_async(
        self,
        request: main_models.ListUserRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListUserResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.marker):
            body['marker'] = request.marker
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListUser',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/user/list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_user(
        self,
        request: main_models.ListUserRequest,
    ) -> main_models.ListUserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_user_with_options(request, headers, runtime)

    async def list_user_async(
        self,
        request: main_models.ListUserRequest,
    ) -> main_models.ListUserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_user_with_options_async(request, headers, runtime)

    def move_file_with_options(
        self,
        request: main_models.MoveFileRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.MoveFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.check_name_mode):
            body['check_name_mode'] = request.check_name_mode
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.file_id):
            body['file_id'] = request.file_id
        if not DaraCore.is_null(request.to_parent_file_id):
            body['to_parent_file_id'] = request.to_parent_file_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'MoveFile',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/move',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveFileResponse(),
            self.execute(params, req, runtime)
        )

    async def move_file_with_options_async(
        self,
        request: main_models.MoveFileRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.MoveFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.check_name_mode):
            body['check_name_mode'] = request.check_name_mode
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.file_id):
            body['file_id'] = request.file_id
        if not DaraCore.is_null(request.to_parent_file_id):
            body['to_parent_file_id'] = request.to_parent_file_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'MoveFile',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/move',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveFileResponse(),
            await self.execute_async(params, req, runtime)
        )

    def move_file(
        self,
        request: main_models.MoveFileRequest,
    ) -> main_models.MoveFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.move_file_with_options(request, headers, runtime)

    async def move_file_async(
        self,
        request: main_models.MoveFileRequest,
    ) -> main_models.MoveFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.move_file_with_options_async(request, headers, runtime)

    def punish_file_with_options(
        self,
        request: main_models.PunishFileRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PunishFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.action_code):
            body['action_code'] = request.action_code
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.file_id):
            body['file_id'] = request.file_id
        if not DaraCore.is_null(request.punish_reason):
            body['punish_reason'] = request.punish_reason
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PunishFile',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/csi/business/punish_file',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PunishFileResponse(),
            self.execute(params, req, runtime)
        )

    async def punish_file_with_options_async(
        self,
        request: main_models.PunishFileRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PunishFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.action_code):
            body['action_code'] = request.action_code
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.file_id):
            body['file_id'] = request.file_id
        if not DaraCore.is_null(request.punish_reason):
            body['punish_reason'] = request.punish_reason
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PunishFile',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/csi/business/punish_file',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PunishFileResponse(),
            await self.execute_async(params, req, runtime)
        )

    def punish_file(
        self,
        request: main_models.PunishFileRequest,
    ) -> main_models.PunishFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.punish_file_with_options(request, headers, runtime)

    async def punish_file_async(
        self,
        request: main_models.PunishFileRequest,
    ) -> main_models.PunishFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.punish_file_with_options_async(request, headers, runtime)

    def query_order_price_with_options(
        self,
        request: main_models.QueryOrderPriceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryOrderPriceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.instance_id):
            body['instance_id'] = request.instance_id
        if not DaraCore.is_null(request.order_type):
            body['order_type'] = request.order_type
        if not DaraCore.is_null(request.package):
            body['package'] = request.package
        if not DaraCore.is_null(request.period):
            body['period'] = request.period
        if not DaraCore.is_null(request.period_unit):
            body['period_unit'] = request.period_unit
        if not DaraCore.is_null(request.total_size):
            body['total_size'] = request.total_size
        if not DaraCore.is_null(request.user_count):
            body['user_count'] = request.user_count
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryOrderPrice',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/domain/query_order_price',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryOrderPriceResponse(),
            self.execute(params, req, runtime)
        )

    async def query_order_price_with_options_async(
        self,
        request: main_models.QueryOrderPriceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryOrderPriceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.instance_id):
            body['instance_id'] = request.instance_id
        if not DaraCore.is_null(request.order_type):
            body['order_type'] = request.order_type
        if not DaraCore.is_null(request.package):
            body['package'] = request.package
        if not DaraCore.is_null(request.period):
            body['period'] = request.period
        if not DaraCore.is_null(request.period_unit):
            body['period_unit'] = request.period_unit
        if not DaraCore.is_null(request.total_size):
            body['total_size'] = request.total_size
        if not DaraCore.is_null(request.user_count):
            body['user_count'] = request.user_count
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryOrderPrice',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/domain/query_order_price',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryOrderPriceResponse(),
            await self.execute_async(params, req, runtime)
        )

    def query_order_price(
        self,
        request: main_models.QueryOrderPriceRequest,
    ) -> main_models.QueryOrderPriceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.query_order_price_with_options(request, headers, runtime)

    async def query_order_price_async(
        self,
        request: main_models.QueryOrderPriceRequest,
    ) -> main_models.QueryOrderPriceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.query_order_price_with_options_async(request, headers, runtime)

    def remove_face_group_file_with_options(
        self,
        request: main_models.RemoveFaceGroupFileRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RemoveFaceGroupFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.face_group_id):
            body['face_group_id'] = request.face_group_id
        if not DaraCore.is_null(request.file_id):
            body['file_id'] = request.file_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RemoveFaceGroupFile',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/albums/unassign_facegroup_item',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveFaceGroupFileResponse(),
            self.execute(params, req, runtime)
        )

    async def remove_face_group_file_with_options_async(
        self,
        request: main_models.RemoveFaceGroupFileRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RemoveFaceGroupFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.face_group_id):
            body['face_group_id'] = request.face_group_id
        if not DaraCore.is_null(request.file_id):
            body['file_id'] = request.file_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RemoveFaceGroupFile',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/albums/unassign_facegroup_item',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveFaceGroupFileResponse(),
            await self.execute_async(params, req, runtime)
        )

    def remove_face_group_file(
        self,
        request: main_models.RemoveFaceGroupFileRequest,
    ) -> main_models.RemoveFaceGroupFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.remove_face_group_file_with_options(request, headers, runtime)

    async def remove_face_group_file_async(
        self,
        request: main_models.RemoveFaceGroupFileRequest,
    ) -> main_models.RemoveFaceGroupFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.remove_face_group_file_with_options_async(request, headers, runtime)

    def remove_group_member_with_options(
        self,
        request: main_models.RemoveGroupMemberRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RemoveGroupMemberResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.group_id):
            body['group_id'] = request.group_id
        if not DaraCore.is_null(request.member_id):
            body['member_id'] = request.member_id
        if not DaraCore.is_null(request.member_type):
            body['member_type'] = request.member_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RemoveGroupMember',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/group/remove_member',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveGroupMemberResponse(),
            self.execute(params, req, runtime)
        )

    async def remove_group_member_with_options_async(
        self,
        request: main_models.RemoveGroupMemberRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RemoveGroupMemberResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.group_id):
            body['group_id'] = request.group_id
        if not DaraCore.is_null(request.member_id):
            body['member_id'] = request.member_id
        if not DaraCore.is_null(request.member_type):
            body['member_type'] = request.member_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RemoveGroupMember',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/group/remove_member',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveGroupMemberResponse(),
            await self.execute_async(params, req, runtime)
        )

    def remove_group_member(
        self,
        request: main_models.RemoveGroupMemberRequest,
    ) -> main_models.RemoveGroupMemberResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.remove_group_member_with_options(request, headers, runtime)

    async def remove_group_member_async(
        self,
        request: main_models.RemoveGroupMemberRequest,
    ) -> main_models.RemoveGroupMemberResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.remove_group_member_with_options_async(request, headers, runtime)

    def remove_story_files_with_options(
        self,
        request: main_models.RemoveStoryFilesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RemoveStoryFilesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.files):
            body['files'] = request.files
        if not DaraCore.is_null(request.story_id):
            body['story_id'] = request.story_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RemoveStoryFiles',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/image/remove_story_files',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveStoryFilesResponse(),
            self.execute(params, req, runtime)
        )

    async def remove_story_files_with_options_async(
        self,
        request: main_models.RemoveStoryFilesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RemoveStoryFilesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.files):
            body['files'] = request.files
        if not DaraCore.is_null(request.story_id):
            body['story_id'] = request.story_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RemoveStoryFiles',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/image/remove_story_files',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveStoryFilesResponse(),
            await self.execute_async(params, req, runtime)
        )

    def remove_story_files(
        self,
        request: main_models.RemoveStoryFilesRequest,
    ) -> main_models.RemoveStoryFilesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.remove_story_files_with_options(request, headers, runtime)

    async def remove_story_files_async(
        self,
        request: main_models.RemoveStoryFilesRequest,
    ) -> main_models.RemoveStoryFilesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.remove_story_files_with_options_async(request, headers, runtime)

    def restore_file_with_options(
        self,
        request: main_models.RestoreFileRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RestoreFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.file_id):
            body['file_id'] = request.file_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RestoreFile',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/recyclebin/restore',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestoreFileResponse(),
            self.execute(params, req, runtime)
        )

    async def restore_file_with_options_async(
        self,
        request: main_models.RestoreFileRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RestoreFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.file_id):
            body['file_id'] = request.file_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RestoreFile',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/recyclebin/restore',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestoreFileResponse(),
            await self.execute_async(params, req, runtime)
        )

    def restore_file(
        self,
        request: main_models.RestoreFileRequest,
    ) -> main_models.RestoreFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.restore_file_with_options(request, headers, runtime)

    async def restore_file_async(
        self,
        request: main_models.RestoreFileRequest,
    ) -> main_models.RestoreFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.restore_file_with_options_async(request, headers, runtime)

    def restore_revision_with_options(
        self,
        request: main_models.RestoreRevisionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RestoreRevisionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.file_id):
            body['file_id'] = request.file_id
        if not DaraCore.is_null(request.revision_id):
            body['revision_id'] = request.revision_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RestoreRevision',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/revision/restore',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestoreRevisionResponse(),
            self.execute(params, req, runtime)
        )

    async def restore_revision_with_options_async(
        self,
        request: main_models.RestoreRevisionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RestoreRevisionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.file_id):
            body['file_id'] = request.file_id
        if not DaraCore.is_null(request.revision_id):
            body['revision_id'] = request.revision_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RestoreRevision',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/revision/restore',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestoreRevisionResponse(),
            await self.execute_async(params, req, runtime)
        )

    def restore_revision(
        self,
        request: main_models.RestoreRevisionRequest,
    ) -> main_models.RestoreRevisionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.restore_revision_with_options(request, headers, runtime)

    async def restore_revision_async(
        self,
        request: main_models.RestoreRevisionRequest,
    ) -> main_models.RestoreRevisionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.restore_revision_with_options_async(request, headers, runtime)

    def scan_file_with_options(
        self,
        request: main_models.ScanFileRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ScanFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.fields):
            body['fields'] = request.fields
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.marker):
            body['marker'] = request.marker
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ScanFile',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/scan',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ScanFileResponse(),
            self.execute(params, req, runtime)
        )

    async def scan_file_with_options_async(
        self,
        request: main_models.ScanFileRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ScanFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.fields):
            body['fields'] = request.fields
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.marker):
            body['marker'] = request.marker
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ScanFile',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/scan',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ScanFileResponse(),
            await self.execute_async(params, req, runtime)
        )

    def scan_file(
        self,
        request: main_models.ScanFileRequest,
    ) -> main_models.ScanFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.scan_file_with_options(request, headers, runtime)

    async def scan_file_async(
        self,
        request: main_models.ScanFileRequest,
    ) -> main_models.ScanFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.scan_file_with_options_async(request, headers, runtime)

    def search_address_groups_with_options(
        self,
        request: main_models.SearchAddressGroupsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SearchAddressGroupsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.address_level):
            body['address_level'] = request.address_level
        if not DaraCore.is_null(request.address_names):
            body['address_names'] = request.address_names
        if not DaraCore.is_null(request.br_geo_point):
            body['br_geo_point'] = request.br_geo_point
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.image_thumbnail_process):
            body['image_thumbnail_process'] = request.image_thumbnail_process
        if not DaraCore.is_null(request.tl_geo_point):
            body['tl_geo_point'] = request.tl_geo_point
        if not DaraCore.is_null(request.video_thumbnail_process):
            body['video_thumbnail_process'] = request.video_thumbnail_process
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SearchAddressGroups',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/image/search_address_groups',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchAddressGroupsResponse(),
            self.execute(params, req, runtime)
        )

    async def search_address_groups_with_options_async(
        self,
        request: main_models.SearchAddressGroupsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SearchAddressGroupsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.address_level):
            body['address_level'] = request.address_level
        if not DaraCore.is_null(request.address_names):
            body['address_names'] = request.address_names
        if not DaraCore.is_null(request.br_geo_point):
            body['br_geo_point'] = request.br_geo_point
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.image_thumbnail_process):
            body['image_thumbnail_process'] = request.image_thumbnail_process
        if not DaraCore.is_null(request.tl_geo_point):
            body['tl_geo_point'] = request.tl_geo_point
        if not DaraCore.is_null(request.video_thumbnail_process):
            body['video_thumbnail_process'] = request.video_thumbnail_process
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SearchAddressGroups',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/image/search_address_groups',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchAddressGroupsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def search_address_groups(
        self,
        request: main_models.SearchAddressGroupsRequest,
    ) -> main_models.SearchAddressGroupsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.search_address_groups_with_options(request, headers, runtime)

    async def search_address_groups_async(
        self,
        request: main_models.SearchAddressGroupsRequest,
    ) -> main_models.SearchAddressGroupsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.search_address_groups_with_options_async(request, headers, runtime)

    def search_domains_with_options(
        self,
        request: main_models.SearchDomainsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SearchDomainsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.marker):
            body['marker'] = request.marker
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.order_by):
            body['order_by'] = request.order_by
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SearchDomains',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/domain/search',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchDomainsResponse(),
            self.execute(params, req, runtime)
        )

    async def search_domains_with_options_async(
        self,
        request: main_models.SearchDomainsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SearchDomainsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.marker):
            body['marker'] = request.marker
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.order_by):
            body['order_by'] = request.order_by
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SearchDomains',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/domain/search',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchDomainsResponse(),
            await self.execute_async(params, req, runtime)
        )

    def search_domains(
        self,
        request: main_models.SearchDomainsRequest,
    ) -> main_models.SearchDomainsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.search_domains_with_options(request, headers, runtime)

    async def search_domains_async(
        self,
        request: main_models.SearchDomainsRequest,
    ) -> main_models.SearchDomainsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.search_domains_with_options_async(request, headers, runtime)

    def search_drive_with_options(
        self,
        request: main_models.SearchDriveRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SearchDriveResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_name):
            body['drive_name'] = request.drive_name
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.marker):
            body['marker'] = request.marker
        if not DaraCore.is_null(request.owner):
            body['owner'] = request.owner
        if not DaraCore.is_null(request.owner_type):
            body['owner_type'] = request.owner_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SearchDrive',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/drive/search',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchDriveResponse(),
            self.execute(params, req, runtime)
        )

    async def search_drive_with_options_async(
        self,
        request: main_models.SearchDriveRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SearchDriveResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_name):
            body['drive_name'] = request.drive_name
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.marker):
            body['marker'] = request.marker
        if not DaraCore.is_null(request.owner):
            body['owner'] = request.owner
        if not DaraCore.is_null(request.owner_type):
            body['owner_type'] = request.owner_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SearchDrive',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/drive/search',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchDriveResponse(),
            await self.execute_async(params, req, runtime)
        )

    def search_drive(
        self,
        request: main_models.SearchDriveRequest,
    ) -> main_models.SearchDriveResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.search_drive_with_options(request, headers, runtime)

    async def search_drive_async(
        self,
        request: main_models.SearchDriveRequest,
    ) -> main_models.SearchDriveResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.search_drive_with_options_async(request, headers, runtime)

    def search_file_with_options(
        self,
        request: main_models.SearchFileRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SearchFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.fields):
            body['fields'] = request.fields
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.marker):
            body['marker'] = request.marker
        if not DaraCore.is_null(request.order_by):
            body['order_by'] = request.order_by
        if not DaraCore.is_null(request.query):
            body['query'] = request.query
        if not DaraCore.is_null(request.recursive):
            body['recursive'] = request.recursive
        if not DaraCore.is_null(request.return_total_count):
            body['return_total_count'] = request.return_total_count
        if not DaraCore.is_null(request.thumbnail_processes):
            body['thumbnail_processes'] = request.thumbnail_processes
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SearchFile',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/search',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchFileResponse(),
            self.execute(params, req, runtime)
        )

    async def search_file_with_options_async(
        self,
        request: main_models.SearchFileRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SearchFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.fields):
            body['fields'] = request.fields
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.marker):
            body['marker'] = request.marker
        if not DaraCore.is_null(request.order_by):
            body['order_by'] = request.order_by
        if not DaraCore.is_null(request.query):
            body['query'] = request.query
        if not DaraCore.is_null(request.recursive):
            body['recursive'] = request.recursive
        if not DaraCore.is_null(request.return_total_count):
            body['return_total_count'] = request.return_total_count
        if not DaraCore.is_null(request.thumbnail_processes):
            body['thumbnail_processes'] = request.thumbnail_processes
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SearchFile',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/search',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchFileResponse(),
            await self.execute_async(params, req, runtime)
        )

    def search_file(
        self,
        request: main_models.SearchFileRequest,
    ) -> main_models.SearchFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.search_file_with_options(request, headers, runtime)

    async def search_file_async(
        self,
        request: main_models.SearchFileRequest,
    ) -> main_models.SearchFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.search_file_with_options_async(request, headers, runtime)

    def search_share_link_with_options(
        self,
        request: main_models.SearchShareLinkRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SearchShareLinkResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.creators):
            body['creators'] = request.creators
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.marker):
            body['marker'] = request.marker
        if not DaraCore.is_null(request.order_by):
            body['order_by'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            body['order_direction'] = request.order_direction
        if not DaraCore.is_null(request.query):
            body['query'] = request.query
        if not DaraCore.is_null(request.return_total_count):
            body['return_total_count'] = request.return_total_count
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SearchShareLink',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/share_link/search',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchShareLinkResponse(),
            self.execute(params, req, runtime)
        )

    async def search_share_link_with_options_async(
        self,
        request: main_models.SearchShareLinkRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SearchShareLinkResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.creators):
            body['creators'] = request.creators
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.marker):
            body['marker'] = request.marker
        if not DaraCore.is_null(request.order_by):
            body['order_by'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            body['order_direction'] = request.order_direction
        if not DaraCore.is_null(request.query):
            body['query'] = request.query
        if not DaraCore.is_null(request.return_total_count):
            body['return_total_count'] = request.return_total_count
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SearchShareLink',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/share_link/search',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchShareLinkResponse(),
            await self.execute_async(params, req, runtime)
        )

    def search_share_link(
        self,
        request: main_models.SearchShareLinkRequest,
    ) -> main_models.SearchShareLinkResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.search_share_link_with_options(request, headers, runtime)

    async def search_share_link_async(
        self,
        request: main_models.SearchShareLinkRequest,
    ) -> main_models.SearchShareLinkResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.search_share_link_with_options_async(request, headers, runtime)

    def search_similar_image_clusters_with_options(
        self,
        request: main_models.SearchSimilarImageClustersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SearchSimilarImageClustersResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.image_thumbnail_process):
            body['image_thumbnail_process'] = request.image_thumbnail_process
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.marker):
            body['marker'] = request.marker
        if not DaraCore.is_null(request.order):
            body['order'] = request.order
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SearchSimilarImageClusters',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/image/query_similar_image_clusters',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchSimilarImageClustersResponse(),
            self.execute(params, req, runtime)
        )

    async def search_similar_image_clusters_with_options_async(
        self,
        request: main_models.SearchSimilarImageClustersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SearchSimilarImageClustersResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.image_thumbnail_process):
            body['image_thumbnail_process'] = request.image_thumbnail_process
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.marker):
            body['marker'] = request.marker
        if not DaraCore.is_null(request.order):
            body['order'] = request.order
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SearchSimilarImageClusters',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/image/query_similar_image_clusters',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchSimilarImageClustersResponse(),
            await self.execute_async(params, req, runtime)
        )

    def search_similar_image_clusters(
        self,
        request: main_models.SearchSimilarImageClustersRequest,
    ) -> main_models.SearchSimilarImageClustersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.search_similar_image_clusters_with_options(request, headers, runtime)

    async def search_similar_image_clusters_async(
        self,
        request: main_models.SearchSimilarImageClustersRequest,
    ) -> main_models.SearchSimilarImageClustersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.search_similar_image_clusters_with_options_async(request, headers, runtime)

    def search_stories_with_options(
        self,
        request: main_models.SearchStoriesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SearchStoriesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cover_image_thumbnail_process):
            body['cover_image_thumbnail_process'] = request.cover_image_thumbnail_process
        if not DaraCore.is_null(request.cover_video_thumbnail_process):
            body['cover_video_thumbnail_process'] = request.cover_video_thumbnail_process
        if not DaraCore.is_null(request.create_time_range):
            body['create_time_range'] = request.create_time_range
        if not DaraCore.is_null(request.custom_labels):
            body['custom_labels'] = request.custom_labels
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.face_group_ids):
            body['face_group_ids'] = request.face_group_ids
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.marker):
            body['marker'] = request.marker
        if not DaraCore.is_null(request.order):
            body['order'] = request.order
        if not DaraCore.is_null(request.sort):
            body['sort'] = request.sort
        if not DaraCore.is_null(request.story_end_time_range):
            body['story_end_time_range'] = request.story_end_time_range
        if not DaraCore.is_null(request.story_id):
            body['story_id'] = request.story_id
        if not DaraCore.is_null(request.story_name):
            body['story_name'] = request.story_name
        if not DaraCore.is_null(request.story_start_time_range):
            body['story_start_time_range'] = request.story_start_time_range
        if not DaraCore.is_null(request.story_type):
            body['story_type'] = request.story_type
        if not DaraCore.is_null(request.url_expire_sec):
            body['url_expire_sec'] = request.url_expire_sec
        if not DaraCore.is_null(request.with_empty_stories):
            body['with_empty_stories'] = request.with_empty_stories
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SearchStories',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/image/find_stories',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchStoriesResponse(),
            self.execute(params, req, runtime)
        )

    async def search_stories_with_options_async(
        self,
        request: main_models.SearchStoriesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SearchStoriesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cover_image_thumbnail_process):
            body['cover_image_thumbnail_process'] = request.cover_image_thumbnail_process
        if not DaraCore.is_null(request.cover_video_thumbnail_process):
            body['cover_video_thumbnail_process'] = request.cover_video_thumbnail_process
        if not DaraCore.is_null(request.create_time_range):
            body['create_time_range'] = request.create_time_range
        if not DaraCore.is_null(request.custom_labels):
            body['custom_labels'] = request.custom_labels
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.face_group_ids):
            body['face_group_ids'] = request.face_group_ids
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.marker):
            body['marker'] = request.marker
        if not DaraCore.is_null(request.order):
            body['order'] = request.order
        if not DaraCore.is_null(request.sort):
            body['sort'] = request.sort
        if not DaraCore.is_null(request.story_end_time_range):
            body['story_end_time_range'] = request.story_end_time_range
        if not DaraCore.is_null(request.story_id):
            body['story_id'] = request.story_id
        if not DaraCore.is_null(request.story_name):
            body['story_name'] = request.story_name
        if not DaraCore.is_null(request.story_start_time_range):
            body['story_start_time_range'] = request.story_start_time_range
        if not DaraCore.is_null(request.story_type):
            body['story_type'] = request.story_type
        if not DaraCore.is_null(request.url_expire_sec):
            body['url_expire_sec'] = request.url_expire_sec
        if not DaraCore.is_null(request.with_empty_stories):
            body['with_empty_stories'] = request.with_empty_stories
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SearchStories',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/image/find_stories',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchStoriesResponse(),
            await self.execute_async(params, req, runtime)
        )

    def search_stories(
        self,
        request: main_models.SearchStoriesRequest,
    ) -> main_models.SearchStoriesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.search_stories_with_options(request, headers, runtime)

    async def search_stories_async(
        self,
        request: main_models.SearchStoriesRequest,
    ) -> main_models.SearchStoriesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.search_stories_with_options_async(request, headers, runtime)

    def search_user_with_options(
        self,
        request: main_models.SearchUserRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SearchUserResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.email):
            body['email'] = request.email
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.marker):
            body['marker'] = request.marker
        if not DaraCore.is_null(request.nick_name):
            body['nick_name'] = request.nick_name
        if not DaraCore.is_null(request.nick_name_for_fuzzy):
            body['nick_name_for_fuzzy'] = request.nick_name_for_fuzzy
        if not DaraCore.is_null(request.phone):
            body['phone'] = request.phone
        if not DaraCore.is_null(request.role):
            body['role'] = request.role
        if not DaraCore.is_null(request.status):
            body['status'] = request.status
        if not DaraCore.is_null(request.user_name):
            body['user_name'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SearchUser',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/user/search',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchUserResponse(),
            self.execute(params, req, runtime)
        )

    async def search_user_with_options_async(
        self,
        request: main_models.SearchUserRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SearchUserResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.email):
            body['email'] = request.email
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.marker):
            body['marker'] = request.marker
        if not DaraCore.is_null(request.nick_name):
            body['nick_name'] = request.nick_name
        if not DaraCore.is_null(request.nick_name_for_fuzzy):
            body['nick_name_for_fuzzy'] = request.nick_name_for_fuzzy
        if not DaraCore.is_null(request.phone):
            body['phone'] = request.phone
        if not DaraCore.is_null(request.role):
            body['role'] = request.role
        if not DaraCore.is_null(request.status):
            body['status'] = request.status
        if not DaraCore.is_null(request.user_name):
            body['user_name'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SearchUser',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/user/search',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchUserResponse(),
            await self.execute_async(params, req, runtime)
        )

    def search_user(
        self,
        request: main_models.SearchUserRequest,
    ) -> main_models.SearchUserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.search_user_with_options(request, headers, runtime)

    async def search_user_async(
        self,
        request: main_models.SearchUserRequest,
    ) -> main_models.SearchUserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.search_user_with_options_async(request, headers, runtime)

    def token_with_options(
        self,
        request: main_models.TokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TokenResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.assertion):
            body['assertion'] = request.assertion
        if not DaraCore.is_null(request.client_id):
            body['client_id'] = request.client_id
        if not DaraCore.is_null(request.client_secret):
            body['client_secret'] = request.client_secret
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.grant_type):
            body['grant_type'] = request.grant_type
        if not DaraCore.is_null(request.redirect_uri):
            body['redirect_uri'] = request.redirect_uri
        if not DaraCore.is_null(request.refresh_token):
            body['refresh_token'] = request.refresh_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Token',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/oauth/token',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TokenResponse(),
            self.execute(params, req, runtime)
        )

    async def token_with_options_async(
        self,
        request: main_models.TokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TokenResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.assertion):
            body['assertion'] = request.assertion
        if not DaraCore.is_null(request.client_id):
            body['client_id'] = request.client_id
        if not DaraCore.is_null(request.client_secret):
            body['client_secret'] = request.client_secret
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.grant_type):
            body['grant_type'] = request.grant_type
        if not DaraCore.is_null(request.redirect_uri):
            body['redirect_uri'] = request.redirect_uri
        if not DaraCore.is_null(request.refresh_token):
            body['refresh_token'] = request.refresh_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Token',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/oauth/token',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TokenResponse(),
            await self.execute_async(params, req, runtime)
        )

    def token(
        self,
        request: main_models.TokenRequest,
    ) -> main_models.TokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.token_with_options(request, headers, runtime)

    async def token_async(
        self,
        request: main_models.TokenRequest,
    ) -> main_models.TokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.token_with_options_async(request, headers, runtime)

    def trash_file_with_options(
        self,
        request: main_models.TrashFileRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TrashFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.file_id):
            body['file_id'] = request.file_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TrashFile',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/recyclebin/trash',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TrashFileResponse(),
            self.execute(params, req, runtime)
        )

    async def trash_file_with_options_async(
        self,
        request: main_models.TrashFileRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TrashFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.file_id):
            body['file_id'] = request.file_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TrashFile',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/recyclebin/trash',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TrashFileResponse(),
            await self.execute_async(params, req, runtime)
        )

    def trash_file(
        self,
        request: main_models.TrashFileRequest,
    ) -> main_models.TrashFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.trash_file_with_options(request, headers, runtime)

    async def trash_file_async(
        self,
        request: main_models.TrashFileRequest,
    ) -> main_models.TrashFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.trash_file_with_options_async(request, headers, runtime)

    def un_link_account_with_options(
        self,
        request: main_models.UnLinkAccountRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UnLinkAccountResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.extra):
            body['extra'] = request.extra
        if not DaraCore.is_null(request.identity):
            body['identity'] = request.identity
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        if not DaraCore.is_null(request.user_id):
            body['user_id'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UnLinkAccount',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/account/unlink',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnLinkAccountResponse(),
            self.execute(params, req, runtime)
        )

    async def un_link_account_with_options_async(
        self,
        request: main_models.UnLinkAccountRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UnLinkAccountResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.extra):
            body['extra'] = request.extra
        if not DaraCore.is_null(request.identity):
            body['identity'] = request.identity
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        if not DaraCore.is_null(request.user_id):
            body['user_id'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UnLinkAccount',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/account/unlink',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnLinkAccountResponse(),
            await self.execute_async(params, req, runtime)
        )

    def un_link_account(
        self,
        request: main_models.UnLinkAccountRequest,
    ) -> main_models.UnLinkAccountResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.un_link_account_with_options(request, headers, runtime)

    async def un_link_account_async(
        self,
        request: main_models.UnLinkAccountRequest,
    ) -> main_models.UnLinkAccountResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.un_link_account_with_options_async(request, headers, runtime)

    def update_domain_with_options(
        self,
        request: main_models.UpdateDomainRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDomainResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.domain_id):
            body['domain_id'] = request.domain_id
        if not DaraCore.is_null(request.domain_name):
            body['domain_name'] = request.domain_name
        if not DaraCore.is_null(request.init_drive_enable):
            body['init_drive_enable'] = request.init_drive_enable
        if not DaraCore.is_null(request.init_drive_size):
            body['init_drive_size'] = request.init_drive_size
        if not DaraCore.is_null(request.published_app_access_strategy):
            body['published_app_access_strategy'] = request.published_app_access_strategy
        if not DaraCore.is_null(request.size_quota):
            body['size_quota'] = request.size_quota
        if not DaraCore.is_null(request.user_count_quota):
            body['user_count_quota'] = request.user_count_quota
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDomain',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/domain/update',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDomainResponse(),
            self.execute(params, req, runtime)
        )

    async def update_domain_with_options_async(
        self,
        request: main_models.UpdateDomainRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDomainResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.domain_id):
            body['domain_id'] = request.domain_id
        if not DaraCore.is_null(request.domain_name):
            body['domain_name'] = request.domain_name
        if not DaraCore.is_null(request.init_drive_enable):
            body['init_drive_enable'] = request.init_drive_enable
        if not DaraCore.is_null(request.init_drive_size):
            body['init_drive_size'] = request.init_drive_size
        if not DaraCore.is_null(request.published_app_access_strategy):
            body['published_app_access_strategy'] = request.published_app_access_strategy
        if not DaraCore.is_null(request.size_quota):
            body['size_quota'] = request.size_quota
        if not DaraCore.is_null(request.user_count_quota):
            body['user_count_quota'] = request.user_count_quota
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDomain',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/domain/update',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDomainResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_domain(
        self,
        request: main_models.UpdateDomainRequest,
    ) -> main_models.UpdateDomainResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_domain_with_options(request, headers, runtime)

    async def update_domain_async(
        self,
        request: main_models.UpdateDomainRequest,
    ) -> main_models.UpdateDomainResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_domain_with_options_async(request, headers, runtime)

    def update_drive_with_options(
        self,
        request: main_models.UpdateDriveRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDriveResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.drive_name):
            body['drive_name'] = request.drive_name
        if not DaraCore.is_null(request.owner):
            body['owner'] = request.owner
        if not DaraCore.is_null(request.status):
            body['status'] = request.status
        if not DaraCore.is_null(request.total_size):
            body['total_size'] = request.total_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDrive',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/drive/update',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDriveResponse(),
            self.execute(params, req, runtime)
        )

    async def update_drive_with_options_async(
        self,
        request: main_models.UpdateDriveRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDriveResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.drive_name):
            body['drive_name'] = request.drive_name
        if not DaraCore.is_null(request.owner):
            body['owner'] = request.owner
        if not DaraCore.is_null(request.status):
            body['status'] = request.status
        if not DaraCore.is_null(request.total_size):
            body['total_size'] = request.total_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDrive',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/drive/update',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDriveResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_drive(
        self,
        request: main_models.UpdateDriveRequest,
    ) -> main_models.UpdateDriveResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_drive_with_options(request, headers, runtime)

    async def update_drive_async(
        self,
        request: main_models.UpdateDriveRequest,
    ) -> main_models.UpdateDriveResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_drive_with_options_async(request, headers, runtime)

    def update_facegroup_with_options(
        self,
        request: main_models.UpdateFacegroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFacegroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.group_cover_face_id):
            body['group_cover_face_id'] = request.group_cover_face_id
        if not DaraCore.is_null(request.group_id):
            body['group_id'] = request.group_id
        if not DaraCore.is_null(request.group_name):
            body['group_name'] = request.group_name
        if not DaraCore.is_null(request.remarks):
            body['remarks'] = request.remarks
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFacegroup',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/image/update_facegroup_info',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFacegroupResponse(),
            self.execute(params, req, runtime)
        )

    async def update_facegroup_with_options_async(
        self,
        request: main_models.UpdateFacegroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFacegroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.group_cover_face_id):
            body['group_cover_face_id'] = request.group_cover_face_id
        if not DaraCore.is_null(request.group_id):
            body['group_id'] = request.group_id
        if not DaraCore.is_null(request.group_name):
            body['group_name'] = request.group_name
        if not DaraCore.is_null(request.remarks):
            body['remarks'] = request.remarks
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFacegroup',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/image/update_facegroup_info',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFacegroupResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_facegroup(
        self,
        request: main_models.UpdateFacegroupRequest,
    ) -> main_models.UpdateFacegroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_facegroup_with_options(request, headers, runtime)

    async def update_facegroup_async(
        self,
        request: main_models.UpdateFacegroupRequest,
    ) -> main_models.UpdateFacegroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_facegroup_with_options_async(request, headers, runtime)

    def update_file_with_options(
        self,
        request: main_models.UpdateFileRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.check_name_mode):
            body['check_name_mode'] = request.check_name_mode
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.file_id):
            body['file_id'] = request.file_id
        if not DaraCore.is_null(request.hidden):
            body['hidden'] = request.hidden
        if not DaraCore.is_null(request.labels):
            body['labels'] = request.labels
        if not DaraCore.is_null(request.local_modified_at):
            body['local_modified_at'] = request.local_modified_at
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.starred):
            body['starred'] = request.starred
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFile',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/update',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFileResponse(),
            self.execute(params, req, runtime)
        )

    async def update_file_with_options_async(
        self,
        request: main_models.UpdateFileRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFileResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.check_name_mode):
            body['check_name_mode'] = request.check_name_mode
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.file_id):
            body['file_id'] = request.file_id
        if not DaraCore.is_null(request.hidden):
            body['hidden'] = request.hidden
        if not DaraCore.is_null(request.labels):
            body['labels'] = request.labels
        if not DaraCore.is_null(request.local_modified_at):
            body['local_modified_at'] = request.local_modified_at
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.starred):
            body['starred'] = request.starred
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFile',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/update',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFileResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_file(
        self,
        request: main_models.UpdateFileRequest,
    ) -> main_models.UpdateFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_file_with_options(request, headers, runtime)

    async def update_file_async(
        self,
        request: main_models.UpdateFileRequest,
    ) -> main_models.UpdateFileResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_file_with_options_async(request, headers, runtime)

    def update_group_with_options(
        self,
        request: main_models.UpdateGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.group_id):
            body['group_id'] = request.group_id
        if not DaraCore.is_null(request.group_name):
            body['group_name'] = request.group_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGroup',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/group/update',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGroupResponse(),
            self.execute(params, req, runtime)
        )

    async def update_group_with_options_async(
        self,
        request: main_models.UpdateGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.group_id):
            body['group_id'] = request.group_id
        if not DaraCore.is_null(request.group_name):
            body['group_name'] = request.group_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGroup',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/group/update',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGroupResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_group(
        self,
        request: main_models.UpdateGroupRequest,
    ) -> main_models.UpdateGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_group_with_options(request, headers, runtime)

    async def update_group_async(
        self,
        request: main_models.UpdateGroupRequest,
    ) -> main_models.UpdateGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_group_with_options_async(request, headers, runtime)

    def update_identity_to_benefit_pkg_mapping_with_options(
        self,
        request: main_models.UpdateIdentityToBenefitPkgMappingRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateIdentityToBenefitPkgMappingResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.amount):
            body['amount'] = request.amount
        if not DaraCore.is_null(request.benefit_pkg_id):
            body['benefit_pkg_id'] = request.benefit_pkg_id
        if not DaraCore.is_null(request.expire_time):
            body['expire_time'] = request.expire_time
        if not DaraCore.is_null(request.identity_id):
            body['identity_id'] = request.identity_id
        if not DaraCore.is_null(request.identity_type):
            body['identity_type'] = request.identity_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateIdentityToBenefitPkgMapping',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/benefit/identity_to_benefit_pkg_mapping/update',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateIdentityToBenefitPkgMappingResponse(),
            self.execute(params, req, runtime)
        )

    async def update_identity_to_benefit_pkg_mapping_with_options_async(
        self,
        request: main_models.UpdateIdentityToBenefitPkgMappingRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateIdentityToBenefitPkgMappingResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.amount):
            body['amount'] = request.amount
        if not DaraCore.is_null(request.benefit_pkg_id):
            body['benefit_pkg_id'] = request.benefit_pkg_id
        if not DaraCore.is_null(request.expire_time):
            body['expire_time'] = request.expire_time
        if not DaraCore.is_null(request.identity_id):
            body['identity_id'] = request.identity_id
        if not DaraCore.is_null(request.identity_type):
            body['identity_type'] = request.identity_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateIdentityToBenefitPkgMapping',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/benefit/identity_to_benefit_pkg_mapping/update',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateIdentityToBenefitPkgMappingResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_identity_to_benefit_pkg_mapping(
        self,
        request: main_models.UpdateIdentityToBenefitPkgMappingRequest,
    ) -> main_models.UpdateIdentityToBenefitPkgMappingResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_identity_to_benefit_pkg_mapping_with_options(request, headers, runtime)

    async def update_identity_to_benefit_pkg_mapping_async(
        self,
        request: main_models.UpdateIdentityToBenefitPkgMappingRequest,
    ) -> main_models.UpdateIdentityToBenefitPkgMappingResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_identity_to_benefit_pkg_mapping_with_options_async(request, headers, runtime)

    def update_revision_with_options(
        self,
        request: main_models.UpdateRevisionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRevisionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.file_id):
            body['file_id'] = request.file_id
        if not DaraCore.is_null(request.keep_forever):
            body['keep_forever'] = request.keep_forever
        if not DaraCore.is_null(request.revision_description):
            body['revision_description'] = request.revision_description
        if not DaraCore.is_null(request.revision_id):
            body['revision_id'] = request.revision_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRevision',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/revision/update',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRevisionResponse(),
            self.execute(params, req, runtime)
        )

    async def update_revision_with_options_async(
        self,
        request: main_models.UpdateRevisionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRevisionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.file_id):
            body['file_id'] = request.file_id
        if not DaraCore.is_null(request.keep_forever):
            body['keep_forever'] = request.keep_forever
        if not DaraCore.is_null(request.revision_description):
            body['revision_description'] = request.revision_description
        if not DaraCore.is_null(request.revision_id):
            body['revision_id'] = request.revision_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRevision',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/revision/update',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRevisionResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_revision(
        self,
        request: main_models.UpdateRevisionRequest,
    ) -> main_models.UpdateRevisionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_revision_with_options(request, headers, runtime)

    async def update_revision_async(
        self,
        request: main_models.UpdateRevisionRequest,
    ) -> main_models.UpdateRevisionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_revision_with_options_async(request, headers, runtime)

    def update_share_link_with_options(
        self,
        request: main_models.UpdateShareLinkRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateShareLinkResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.disable_download):
            body['disable_download'] = request.disable_download
        if not DaraCore.is_null(request.disable_preview):
            body['disable_preview'] = request.disable_preview
        if not DaraCore.is_null(request.disable_save):
            body['disable_save'] = request.disable_save
        if not DaraCore.is_null(request.download_count):
            body['download_count'] = request.download_count
        if not DaraCore.is_null(request.download_limit):
            body['download_limit'] = request.download_limit
        if not DaraCore.is_null(request.expiration):
            body['expiration'] = request.expiration
        if not DaraCore.is_null(request.office_editable):
            body['office_editable'] = request.office_editable
        if not DaraCore.is_null(request.preview_count):
            body['preview_count'] = request.preview_count
        if not DaraCore.is_null(request.preview_limit):
            body['preview_limit'] = request.preview_limit
        if not DaraCore.is_null(request.report_count):
            body['report_count'] = request.report_count
        if not DaraCore.is_null(request.save_count):
            body['save_count'] = request.save_count
        if not DaraCore.is_null(request.save_limit):
            body['save_limit'] = request.save_limit
        if not DaraCore.is_null(request.share_id):
            body['share_id'] = request.share_id
        if not DaraCore.is_null(request.share_name):
            body['share_name'] = request.share_name
        if not DaraCore.is_null(request.share_pwd):
            body['share_pwd'] = request.share_pwd
        if not DaraCore.is_null(request.status):
            body['status'] = request.status
        if not DaraCore.is_null(request.video_preview_count):
            body['video_preview_count'] = request.video_preview_count
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateShareLink',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/share_link/update',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateShareLinkResponse(),
            self.execute(params, req, runtime)
        )

    async def update_share_link_with_options_async(
        self,
        request: main_models.UpdateShareLinkRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateShareLinkResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.disable_download):
            body['disable_download'] = request.disable_download
        if not DaraCore.is_null(request.disable_preview):
            body['disable_preview'] = request.disable_preview
        if not DaraCore.is_null(request.disable_save):
            body['disable_save'] = request.disable_save
        if not DaraCore.is_null(request.download_count):
            body['download_count'] = request.download_count
        if not DaraCore.is_null(request.download_limit):
            body['download_limit'] = request.download_limit
        if not DaraCore.is_null(request.expiration):
            body['expiration'] = request.expiration
        if not DaraCore.is_null(request.office_editable):
            body['office_editable'] = request.office_editable
        if not DaraCore.is_null(request.preview_count):
            body['preview_count'] = request.preview_count
        if not DaraCore.is_null(request.preview_limit):
            body['preview_limit'] = request.preview_limit
        if not DaraCore.is_null(request.report_count):
            body['report_count'] = request.report_count
        if not DaraCore.is_null(request.save_count):
            body['save_count'] = request.save_count
        if not DaraCore.is_null(request.save_limit):
            body['save_limit'] = request.save_limit
        if not DaraCore.is_null(request.share_id):
            body['share_id'] = request.share_id
        if not DaraCore.is_null(request.share_name):
            body['share_name'] = request.share_name
        if not DaraCore.is_null(request.share_pwd):
            body['share_pwd'] = request.share_pwd
        if not DaraCore.is_null(request.status):
            body['status'] = request.status
        if not DaraCore.is_null(request.video_preview_count):
            body['video_preview_count'] = request.video_preview_count
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateShareLink',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/share_link/update',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateShareLinkResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_share_link(
        self,
        request: main_models.UpdateShareLinkRequest,
    ) -> main_models.UpdateShareLinkResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_share_link_with_options(request, headers, runtime)

    async def update_share_link_async(
        self,
        request: main_models.UpdateShareLinkRequest,
    ) -> main_models.UpdateShareLinkResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_share_link_with_options_async(request, headers, runtime)

    def update_story_with_options(
        self,
        request: main_models.UpdateStoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateStoryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cover):
            body['cover'] = request.cover
        if not DaraCore.is_null(request.custom_labels):
            body['custom_labels'] = request.custom_labels
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.story_id):
            body['story_id'] = request.story_id
        if not DaraCore.is_null(request.story_name):
            body['story_name'] = request.story_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateStory',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/image/update_story',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateStoryResponse(),
            self.execute(params, req, runtime)
        )

    async def update_story_with_options_async(
        self,
        request: main_models.UpdateStoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateStoryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cover):
            body['cover'] = request.cover
        if not DaraCore.is_null(request.custom_labels):
            body['custom_labels'] = request.custom_labels
        if not DaraCore.is_null(request.drive_id):
            body['drive_id'] = request.drive_id
        if not DaraCore.is_null(request.story_id):
            body['story_id'] = request.story_id
        if not DaraCore.is_null(request.story_name):
            body['story_name'] = request.story_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateStory',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/image/update_story',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateStoryResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_story(
        self,
        request: main_models.UpdateStoryRequest,
    ) -> main_models.UpdateStoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_story_with_options(request, headers, runtime)

    async def update_story_async(
        self,
        request: main_models.UpdateStoryRequest,
    ) -> main_models.UpdateStoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_story_with_options_async(request, headers, runtime)

    def update_user_with_options(
        self,
        request: main_models.UpdateUserRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.avatar):
            body['avatar'] = request.avatar
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.email):
            body['email'] = request.email
        if not DaraCore.is_null(request.group_info_list):
            body['group_info_list'] = request.group_info_list
        if not DaraCore.is_null(request.nick_name):
            body['nick_name'] = request.nick_name
        if not DaraCore.is_null(request.phone):
            body['phone'] = request.phone
        if not DaraCore.is_null(request.role):
            body['role'] = request.role
        if not DaraCore.is_null(request.status):
            body['status'] = request.status
        if not DaraCore.is_null(request.user_data):
            body['user_data'] = request.user_data
        if not DaraCore.is_null(request.user_id):
            body['user_id'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUser',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/user/update',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUserResponse(),
            self.execute(params, req, runtime)
        )

    async def update_user_with_options_async(
        self,
        request: main_models.UpdateUserRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.avatar):
            body['avatar'] = request.avatar
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.email):
            body['email'] = request.email
        if not DaraCore.is_null(request.group_info_list):
            body['group_info_list'] = request.group_info_list
        if not DaraCore.is_null(request.nick_name):
            body['nick_name'] = request.nick_name
        if not DaraCore.is_null(request.phone):
            body['phone'] = request.phone
        if not DaraCore.is_null(request.role):
            body['role'] = request.role
        if not DaraCore.is_null(request.status):
            body['status'] = request.status
        if not DaraCore.is_null(request.user_data):
            body['user_data'] = request.user_data
        if not DaraCore.is_null(request.user_id):
            body['user_id'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUser',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/user/update',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUserResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_user(
        self,
        request: main_models.UpdateUserRequest,
    ) -> main_models.UpdateUserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_user_with_options(request, headers, runtime)

    async def update_user_async(
        self,
        request: main_models.UpdateUserRequest,
    ) -> main_models.UpdateUserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_user_with_options_async(request, headers, runtime)

    def video_drmlicense_with_options(
        self,
        request: main_models.VideoDRMLicenseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.VideoDRMLicenseResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drm_type):
            body['drmType'] = request.drm_type
        if not DaraCore.is_null(request.license_request):
            body['licenseRequest'] = request.license_request
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'VideoDRMLicense',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/video_drm_license',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VideoDRMLicenseResponse(),
            self.execute(params, req, runtime)
        )

    async def video_drmlicense_with_options_async(
        self,
        request: main_models.VideoDRMLicenseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.VideoDRMLicenseResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.drm_type):
            body['drmType'] = request.drm_type
        if not DaraCore.is_null(request.license_request):
            body['licenseRequest'] = request.license_request
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'VideoDRMLicense',
            version = '2022-03-01',
            protocol = 'HTTPS',
            pathname = f'/v2/file/video_drm_license',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VideoDRMLicenseResponse(),
            await self.execute_async(params, req, runtime)
        )

    def video_drmlicense(
        self,
        request: main_models.VideoDRMLicenseRequest,
    ) -> main_models.VideoDRMLicenseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.video_drmlicense_with_options(request, headers, runtime)

    async def video_drmlicense_async(
        self,
        request: main_models.VideoDRMLicenseRequest,
    ) -> main_models.VideoDRMLicenseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.video_drmlicense_with_options_async(request, headers, runtime)
