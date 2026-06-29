# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_modelstudio20260210 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions
from darabonba.url import Url as DaraURL

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'eu-central-1': 'modelstudio.eu-central-1.aliyuncs.com',
            'cn-hongkong': 'modelstudio.cn-hongkong.aliyuncs.com',
            'cn-beijing': 'modelstudio.cn-beijing.aliyuncs.com',
            'ap-southeast-1': 'modelstudio.ap-southeast-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('modelstudio', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_organization_member_with_options(
        self,
        request: main_models.AddOrganizationMemberRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddOrganizationMemberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.org_role_code):
            query['OrgRoleCode'] = request.org_role_code
        if not DaraCore.is_null(request.spec_type):
            query['SpecType'] = request.spec_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddOrganizationMember',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/tokenplan/organization/member-additions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddOrganizationMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_organization_member_with_options_async(
        self,
        request: main_models.AddOrganizationMemberRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddOrganizationMemberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.org_role_code):
            query['OrgRoleCode'] = request.org_role_code
        if not DaraCore.is_null(request.spec_type):
            query['SpecType'] = request.spec_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddOrganizationMember',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/tokenplan/organization/member-additions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddOrganizationMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_organization_member(
        self,
        request: main_models.AddOrganizationMemberRequest,
    ) -> main_models.AddOrganizationMemberResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.add_organization_member_with_options(request, headers, runtime)

    async def add_organization_member_async(
        self,
        request: main_models.AddOrganizationMemberRequest,
    ) -> main_models.AddOrganizationMemberResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.add_organization_member_with_options_async(request, headers, runtime)

    def batch_assign_seats_with_options(
        self,
        request: main_models.BatchAssignSeatsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchAssignSeatsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_ids):
            query['AccountIds'] = request.account_ids
        if not DaraCore.is_null(request.locale):
            query['Locale'] = request.locale
        if not DaraCore.is_null(request.seat_type):
            query['SeatType'] = request.seat_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchAssignSeats',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/tokenplan/subscription/seat-assignments',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchAssignSeatsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_assign_seats_with_options_async(
        self,
        request: main_models.BatchAssignSeatsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchAssignSeatsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_ids):
            query['AccountIds'] = request.account_ids
        if not DaraCore.is_null(request.locale):
            query['Locale'] = request.locale
        if not DaraCore.is_null(request.seat_type):
            query['SeatType'] = request.seat_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchAssignSeats',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/tokenplan/subscription/seat-assignments',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchAssignSeatsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_assign_seats(
        self,
        request: main_models.BatchAssignSeatsRequest,
    ) -> main_models.BatchAssignSeatsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.batch_assign_seats_with_options(request, headers, runtime)

    async def batch_assign_seats_async(
        self,
        request: main_models.BatchAssignSeatsRequest,
    ) -> main_models.BatchAssignSeatsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.batch_assign_seats_with_options_async(request, headers, runtime)

    def batch_revoke_seats_with_options(
        self,
        tmp_req: main_models.BatchRevokeSeatsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchRevokeSeatsResponse:
        tmp_req.validate()
        request = main_models.BatchRevokeSeatsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.items):
            request.items_shrink = Utils.array_to_string_with_specified_style(tmp_req.items, 'Items', 'json')
        query = {}
        if not DaraCore.is_null(request.items_shrink):
            query['Items'] = request.items_shrink
        if not DaraCore.is_null(request.locale):
            query['Locale'] = request.locale
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchRevokeSeats',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/tokenplan/subscription/seat-revocations',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchRevokeSeatsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_revoke_seats_with_options_async(
        self,
        tmp_req: main_models.BatchRevokeSeatsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchRevokeSeatsResponse:
        tmp_req.validate()
        request = main_models.BatchRevokeSeatsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.items):
            request.items_shrink = Utils.array_to_string_with_specified_style(tmp_req.items, 'Items', 'json')
        query = {}
        if not DaraCore.is_null(request.items_shrink):
            query['Items'] = request.items_shrink
        if not DaraCore.is_null(request.locale):
            query['Locale'] = request.locale
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchRevokeSeats',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/tokenplan/subscription/seat-revocations',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchRevokeSeatsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_revoke_seats(
        self,
        request: main_models.BatchRevokeSeatsRequest,
    ) -> main_models.BatchRevokeSeatsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.batch_revoke_seats_with_options(request, headers, runtime)

    async def batch_revoke_seats_async(
        self,
        request: main_models.BatchRevokeSeatsRequest,
    ) -> main_models.BatchRevokeSeatsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.batch_revoke_seats_with_options_async(request, headers, runtime)

    def create_api_key_with_options(
        self,
        request: main_models.CreateApiKeyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateApiKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        if not DaraCore.is_null(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not DaraCore.is_null(request.auth):
            body['auth'] = request.auth
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateApiKey',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/modelstudio/apikeys',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApiKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_api_key_with_options_async(
        self,
        request: main_models.CreateApiKeyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateApiKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        if not DaraCore.is_null(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not DaraCore.is_null(request.auth):
            body['auth'] = request.auth
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateApiKey',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/modelstudio/apikeys',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApiKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_api_key(
        self,
        request: main_models.CreateApiKeyRequest,
    ) -> main_models.CreateApiKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_api_key_with_options(request, headers, runtime)

    async def create_api_key_async(
        self,
        request: main_models.CreateApiKeyRequest,
    ) -> main_models.CreateApiKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_api_key_with_options_async(request, headers, runtime)

    def create_token_plan_invite_link_with_options(
        self,
        request: main_models.CreateTokenPlanInviteLinkRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTokenPlanInviteLinkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.expire_type):
            query['ExpireType'] = request.expire_type
        if not DaraCore.is_null(request.sso_source):
            query['SsoSource'] = request.sso_source
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTokenPlanInviteLink',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/tokenplan/invite/link/create',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTokenPlanInviteLinkResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_token_plan_invite_link_with_options_async(
        self,
        request: main_models.CreateTokenPlanInviteLinkRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTokenPlanInviteLinkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.expire_type):
            query['ExpireType'] = request.expire_type
        if not DaraCore.is_null(request.sso_source):
            query['SsoSource'] = request.sso_source
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTokenPlanInviteLink',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/tokenplan/invite/link/create',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTokenPlanInviteLinkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_token_plan_invite_link(
        self,
        request: main_models.CreateTokenPlanInviteLinkRequest,
    ) -> main_models.CreateTokenPlanInviteLinkResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_token_plan_invite_link_with_options(request, headers, runtime)

    async def create_token_plan_invite_link_async(
        self,
        request: main_models.CreateTokenPlanInviteLinkRequest,
    ) -> main_models.CreateTokenPlanInviteLinkResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_token_plan_invite_link_with_options_async(request, headers, runtime)

    def create_token_plan_key_with_options(
        self,
        request: main_models.CreateTokenPlanKeyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTokenPlanKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTokenPlanKey',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/tokenplan/api-keys',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTokenPlanKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_token_plan_key_with_options_async(
        self,
        request: main_models.CreateTokenPlanKeyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTokenPlanKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTokenPlanKey',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/tokenplan/api-keys',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTokenPlanKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_token_plan_key(
        self,
        request: main_models.CreateTokenPlanKeyRequest,
    ) -> main_models.CreateTokenPlanKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_token_plan_key_with_options(request, headers, runtime)

    async def create_token_plan_key_async(
        self,
        request: main_models.CreateTokenPlanKeyRequest,
    ) -> main_models.CreateTokenPlanKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_token_plan_key_with_options_async(request, headers, runtime)

    def create_workspace_with_options(
        self,
        request: main_models.CreateWorkspaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateWorkspaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.service_site):
            query['serviceSite'] = request.service_site
        if not DaraCore.is_null(request.workspace_name):
            query['workspaceName'] = request.workspace_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateWorkspace',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/modelstudio/workspaces',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_workspace_with_options_async(
        self,
        request: main_models.CreateWorkspaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateWorkspaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.service_site):
            query['serviceSite'] = request.service_site
        if not DaraCore.is_null(request.workspace_name):
            query['workspaceName'] = request.workspace_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateWorkspace',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/modelstudio/workspaces',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
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
        headers = {}
        return self.create_workspace_with_options(request, headers, runtime)

    async def create_workspace_async(
        self,
        request: main_models.CreateWorkspaceRequest,
    ) -> main_models.CreateWorkspaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_workspace_with_options_async(request, headers, runtime)

    def delete_api_key_with_options(
        self,
        api_key_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApiKeyResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteApiKey',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/modelstudio/apikeys/{DaraURL.percent_encode(api_key_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApiKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_api_key_with_options_async(
        self,
        api_key_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApiKeyResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteApiKey',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/modelstudio/apikeys/{DaraURL.percent_encode(api_key_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApiKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_api_key(
        self,
        api_key_id: str,
    ) -> main_models.DeleteApiKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_api_key_with_options(api_key_id, headers, runtime)

    async def delete_api_key_async(
        self,
        api_key_id: str,
    ) -> main_models.DeleteApiKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_api_key_with_options_async(api_key_id, headers, runtime)

    def delete_workspace_with_options(
        self,
        workspace_id: str,
        request: main_models.DeleteWorkspaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWorkspaceResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteWorkspace',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/modelstudio/workspaces/{DaraURL.percent_encode(workspace_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_workspace_with_options_async(
        self,
        workspace_id: str,
        request: main_models.DeleteWorkspaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWorkspaceResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteWorkspace',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/modelstudio/workspaces/{DaraURL.percent_encode(workspace_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_workspace(
        self,
        workspace_id: str,
        request: main_models.DeleteWorkspaceRequest,
    ) -> main_models.DeleteWorkspaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_workspace_with_options(workspace_id, request, headers, runtime)

    async def delete_workspace_async(
        self,
        workspace_id: str,
        request: main_models.DeleteWorkspaceRequest,
    ) -> main_models.DeleteWorkspaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_workspace_with_options_async(workspace_id, request, headers, runtime)

    def disable_api_key_with_options(
        self,
        api_key_id: str,
        request: main_models.DisableApiKeyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DisableApiKeyResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DisableApiKey',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/modelstudio/apikeys/{DaraURL.percent_encode(api_key_id)}/disable',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableApiKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_api_key_with_options_async(
        self,
        api_key_id: str,
        request: main_models.DisableApiKeyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DisableApiKeyResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DisableApiKey',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/modelstudio/apikeys/{DaraURL.percent_encode(api_key_id)}/disable',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableApiKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_api_key(
        self,
        api_key_id: str,
        request: main_models.DisableApiKeyRequest,
    ) -> main_models.DisableApiKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.disable_api_key_with_options(api_key_id, request, headers, runtime)

    async def disable_api_key_async(
        self,
        api_key_id: str,
        request: main_models.DisableApiKeyRequest,
    ) -> main_models.DisableApiKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.disable_api_key_with_options_async(api_key_id, request, headers, runtime)

    def enable_api_key_with_options(
        self,
        api_key_id: str,
        request: main_models.EnableApiKeyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.EnableApiKeyResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'EnableApiKey',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/modelstudio/apikeys/{DaraURL.percent_encode(api_key_id)}/enable',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableApiKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_api_key_with_options_async(
        self,
        api_key_id: str,
        request: main_models.EnableApiKeyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.EnableApiKeyResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'EnableApiKey',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/modelstudio/apikeys/{DaraURL.percent_encode(api_key_id)}/enable',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableApiKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_api_key(
        self,
        api_key_id: str,
        request: main_models.EnableApiKeyRequest,
    ) -> main_models.EnableApiKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.enable_api_key_with_options(api_key_id, request, headers, runtime)

    async def enable_api_key_async(
        self,
        api_key_id: str,
        request: main_models.EnableApiKeyRequest,
    ) -> main_models.EnableApiKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.enable_api_key_with_options_async(api_key_id, request, headers, runtime)

    def get_api_key_with_options(
        self,
        api_key_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetApiKeyResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetApiKey',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/modelstudio/apikeys/{DaraURL.percent_encode(api_key_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApiKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_api_key_with_options_async(
        self,
        api_key_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetApiKeyResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetApiKey',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/modelstudio/apikeys/{DaraURL.percent_encode(api_key_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApiKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_api_key(
        self,
        api_key_id: str,
    ) -> main_models.GetApiKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_api_key_with_options(api_key_id, headers, runtime)

    async def get_api_key_async(
        self,
        api_key_id: str,
    ) -> main_models.GetApiKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_api_key_with_options_async(api_key_id, headers, runtime)

    def get_organization_with_options(
        self,
        request: main_models.GetOrganizationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetOrganizationResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetOrganization',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/tokenplan/organization',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOrganizationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_organization_with_options_async(
        self,
        request: main_models.GetOrganizationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetOrganizationResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetOrganization',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/tokenplan/organization',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOrganizationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_organization(
        self,
        request: main_models.GetOrganizationRequest,
    ) -> main_models.GetOrganizationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_organization_with_options(request, headers, runtime)

    async def get_organization_async(
        self,
        request: main_models.GetOrganizationRequest,
    ) -> main_models.GetOrganizationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_organization_with_options_async(request, headers, runtime)

    def get_organization_member_seat_stats_with_options(
        self,
        request: main_models.GetOrganizationMemberSeatStatsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetOrganizationMemberSeatStatsResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetOrganizationMemberSeatStats',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/tokenplan/organization/member-seat-stats',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOrganizationMemberSeatStatsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_organization_member_seat_stats_with_options_async(
        self,
        request: main_models.GetOrganizationMemberSeatStatsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetOrganizationMemberSeatStatsResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetOrganizationMemberSeatStats',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/tokenplan/organization/member-seat-stats',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOrganizationMemberSeatStatsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_organization_member_seat_stats(
        self,
        request: main_models.GetOrganizationMemberSeatStatsRequest,
    ) -> main_models.GetOrganizationMemberSeatStatsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_organization_member_seat_stats_with_options(request, headers, runtime)

    async def get_organization_member_seat_stats_async(
        self,
        request: main_models.GetOrganizationMemberSeatStatsRequest,
    ) -> main_models.GetOrganizationMemberSeatStatsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_organization_member_seat_stats_with_options_async(request, headers, runtime)

    def get_subscription_seat_details_with_options(
        self,
        request: main_models.GetSubscriptionSeatDetailsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSubscriptionSeatDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_assigned):
            query['QueryAssigned'] = request.query_assigned
        if not DaraCore.is_null(request.seat_id):
            query['SeatId'] = request.seat_id
        if not DaraCore.is_null(request.seat_type):
            query['SeatType'] = request.seat_type
        if not DaraCore.is_null(request.status_list):
            query['StatusList'] = request.status_list
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSubscriptionSeatDetails',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/tokenplan/subscription/seat-detail',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSubscriptionSeatDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_subscription_seat_details_with_options_async(
        self,
        request: main_models.GetSubscriptionSeatDetailsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSubscriptionSeatDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_assigned):
            query['QueryAssigned'] = request.query_assigned
        if not DaraCore.is_null(request.seat_id):
            query['SeatId'] = request.seat_id
        if not DaraCore.is_null(request.seat_type):
            query['SeatType'] = request.seat_type
        if not DaraCore.is_null(request.status_list):
            query['StatusList'] = request.status_list
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSubscriptionSeatDetails',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/tokenplan/subscription/seat-detail',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSubscriptionSeatDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_subscription_seat_details(
        self,
        request: main_models.GetSubscriptionSeatDetailsRequest,
    ) -> main_models.GetSubscriptionSeatDetailsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_subscription_seat_details_with_options(request, headers, runtime)

    async def get_subscription_seat_details_async(
        self,
        request: main_models.GetSubscriptionSeatDetailsRequest,
    ) -> main_models.GetSubscriptionSeatDetailsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_subscription_seat_details_with_options_async(request, headers, runtime)

    def get_subscription_stats_with_options(
        self,
        request: main_models.GetSubscriptionStatsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSubscriptionStatsResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetSubscriptionStats',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/tokenplan/subscription/stats',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSubscriptionStatsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_subscription_stats_with_options_async(
        self,
        request: main_models.GetSubscriptionStatsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSubscriptionStatsResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetSubscriptionStats',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/tokenplan/subscription/stats',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSubscriptionStatsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_subscription_stats(
        self,
        request: main_models.GetSubscriptionStatsRequest,
    ) -> main_models.GetSubscriptionStatsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_subscription_stats_with_options(request, headers, runtime)

    async def get_subscription_stats_async(
        self,
        request: main_models.GetSubscriptionStatsRequest,
    ) -> main_models.GetSubscriptionStatsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_subscription_stats_with_options_async(request, headers, runtime)

    def get_token_plan_account_detail_with_options(
        self,
        request: main_models.GetTokenPlanAccountDetailRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTokenPlanAccountDetailResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTokenPlanAccountDetail',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/tokenplan/account',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTokenPlanAccountDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_token_plan_account_detail_with_options_async(
        self,
        request: main_models.GetTokenPlanAccountDetailRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTokenPlanAccountDetailResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTokenPlanAccountDetail',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/tokenplan/account',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTokenPlanAccountDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_token_plan_account_detail(
        self,
        request: main_models.GetTokenPlanAccountDetailRequest,
    ) -> main_models.GetTokenPlanAccountDetailResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_token_plan_account_detail_with_options(request, headers, runtime)

    async def get_token_plan_account_detail_async(
        self,
        request: main_models.GetTokenPlanAccountDetailRequest,
    ) -> main_models.GetTokenPlanAccountDetailResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_token_plan_account_detail_with_options_async(request, headers, runtime)

    def get_token_plan_invite_link_with_options(
        self,
        request: main_models.GetTokenPlanInviteLinkRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTokenPlanInviteLinkResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTokenPlanInviteLink',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/tokenplan/invite/link/get',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTokenPlanInviteLinkResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_token_plan_invite_link_with_options_async(
        self,
        request: main_models.GetTokenPlanInviteLinkRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTokenPlanInviteLinkResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTokenPlanInviteLink',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/tokenplan/invite/link/get',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTokenPlanInviteLinkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_token_plan_invite_link(
        self,
        request: main_models.GetTokenPlanInviteLinkRequest,
    ) -> main_models.GetTokenPlanInviteLinkResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_token_plan_invite_link_with_options(request, headers, runtime)

    async def get_token_plan_invite_link_async(
        self,
        request: main_models.GetTokenPlanInviteLinkRequest,
    ) -> main_models.GetTokenPlanInviteLinkResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_token_plan_invite_link_with_options_async(request, headers, runtime)

    def get_token_plan_org_invite_config_with_options(
        self,
        request: main_models.GetTokenPlanOrgInviteConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTokenPlanOrgInviteConfigResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTokenPlanOrgInviteConfig',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/tokenplan/invite/config/get',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTokenPlanOrgInviteConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_token_plan_org_invite_config_with_options_async(
        self,
        request: main_models.GetTokenPlanOrgInviteConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTokenPlanOrgInviteConfigResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTokenPlanOrgInviteConfig',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/tokenplan/invite/config/get',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTokenPlanOrgInviteConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_token_plan_org_invite_config(
        self,
        request: main_models.GetTokenPlanOrgInviteConfigRequest,
    ) -> main_models.GetTokenPlanOrgInviteConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_token_plan_org_invite_config_with_options(request, headers, runtime)

    async def get_token_plan_org_invite_config_async(
        self,
        request: main_models.GetTokenPlanOrgInviteConfigRequest,
    ) -> main_models.GetTokenPlanOrgInviteConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_token_plan_org_invite_config_with_options_async(request, headers, runtime)

    def list_api_keys_with_options(
        self,
        request: main_models.ListApiKeysRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListApiKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_key_id):
            query['apiKeyId'] = request.api_key_id
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.order):
            query['order'] = request.order
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApiKeys',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/modelstudio/apikeys',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApiKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_api_keys_with_options_async(
        self,
        request: main_models.ListApiKeysRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListApiKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_key_id):
            query['apiKeyId'] = request.api_key_id
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.order):
            query['order'] = request.order
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApiKeys',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/modelstudio/apikeys',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApiKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_api_keys(
        self,
        request: main_models.ListApiKeysRequest,
    ) -> main_models.ListApiKeysResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_api_keys_with_options(request, headers, runtime)

    async def list_api_keys_async(
        self,
        request: main_models.ListApiKeysRequest,
    ) -> main_models.ListApiKeysResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_api_keys_with_options_async(request, headers, runtime)

    def list_organization_members_with_options(
        self,
        request: main_models.ListOrganizationMembersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListOrganizationMembersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.has_seat):
            query['HasSeat'] = request.has_seat
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOrganizationMembers',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/tokenplan/organization/members',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOrganizationMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_organization_members_with_options_async(
        self,
        request: main_models.ListOrganizationMembersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListOrganizationMembersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.has_seat):
            query['HasSeat'] = request.has_seat
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOrganizationMembers',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/tokenplan/organization/members',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOrganizationMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_organization_members(
        self,
        request: main_models.ListOrganizationMembersRequest,
    ) -> main_models.ListOrganizationMembersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_organization_members_with_options(request, headers, runtime)

    async def list_organization_members_async(
        self,
        request: main_models.ListOrganizationMembersRequest,
    ) -> main_models.ListOrganizationMembersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_organization_members_with_options_async(request, headers, runtime)

    def list_subscription_shared_packages_with_options(
        self,
        request: main_models.ListSubscriptionSharedPackagesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSubscriptionSharedPackagesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.status_list):
            query['StatusList'] = request.status_list
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSubscriptionSharedPackages',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/tokenplan/subscription/shared-packages',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSubscriptionSharedPackagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_subscription_shared_packages_with_options_async(
        self,
        request: main_models.ListSubscriptionSharedPackagesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSubscriptionSharedPackagesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.status_list):
            query['StatusList'] = request.status_list
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSubscriptionSharedPackages',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/tokenplan/subscription/shared-packages',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSubscriptionSharedPackagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_subscription_shared_packages(
        self,
        request: main_models.ListSubscriptionSharedPackagesRequest,
    ) -> main_models.ListSubscriptionSharedPackagesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_subscription_shared_packages_with_options(request, headers, runtime)

    async def list_subscription_shared_packages_async(
        self,
        request: main_models.ListSubscriptionSharedPackagesRequest,
    ) -> main_models.ListSubscriptionSharedPackagesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_subscription_shared_packages_with_options_async(request, headers, runtime)

    def list_workspaces_with_options(
        self,
        request: main_models.ListWorkspacesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListWorkspacesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        if not DaraCore.is_null(request.workspace_name):
            query['workspaceName'] = request.workspace_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWorkspaces',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/modelstudio/workspaces',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWorkspacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_workspaces_with_options_async(
        self,
        request: main_models.ListWorkspacesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListWorkspacesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        if not DaraCore.is_null(request.workspace_name):
            query['workspaceName'] = request.workspace_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWorkspaces',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/modelstudio/workspaces',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWorkspacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_workspaces(
        self,
        request: main_models.ListWorkspacesRequest,
    ) -> main_models.ListWorkspacesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_workspaces_with_options(request, headers, runtime)

    async def list_workspaces_async(
        self,
        request: main_models.ListWorkspacesRequest,
    ) -> main_models.ListWorkspacesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_workspaces_with_options_async(request, headers, runtime)

    def remove_organization_member_with_options(
        self,
        request: main_models.RemoveOrganizationMemberRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RemoveOrganizationMemberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_ids):
            query['AccountIds'] = request.account_ids
        if not DaraCore.is_null(request.locale):
            query['Locale'] = request.locale
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveOrganizationMember',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/tokenplan/organization/member-removals',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveOrganizationMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_organization_member_with_options_async(
        self,
        request: main_models.RemoveOrganizationMemberRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RemoveOrganizationMemberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_ids):
            query['AccountIds'] = request.account_ids
        if not DaraCore.is_null(request.locale):
            query['Locale'] = request.locale
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveOrganizationMember',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/tokenplan/organization/member-removals',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveOrganizationMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_organization_member(
        self,
        request: main_models.RemoveOrganizationMemberRequest,
    ) -> main_models.RemoveOrganizationMemberResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.remove_organization_member_with_options(request, headers, runtime)

    async def remove_organization_member_async(
        self,
        request: main_models.RemoveOrganizationMemberRequest,
    ) -> main_models.RemoveOrganizationMemberResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.remove_organization_member_with_options_async(request, headers, runtime)

    def reset_api_key_with_options(
        self,
        api_key_id: str,
        request: main_models.ResetApiKeyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ResetApiKeyResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ResetApiKey',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/modelstudio/apikeys/{DaraURL.percent_encode(api_key_id)}/reset',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetApiKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_api_key_with_options_async(
        self,
        api_key_id: str,
        request: main_models.ResetApiKeyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ResetApiKeyResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ResetApiKey',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/modelstudio/apikeys/{DaraURL.percent_encode(api_key_id)}/reset',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetApiKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_api_key(
        self,
        api_key_id: str,
        request: main_models.ResetApiKeyRequest,
    ) -> main_models.ResetApiKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.reset_api_key_with_options(api_key_id, request, headers, runtime)

    async def reset_api_key_async(
        self,
        api_key_id: str,
        request: main_models.ResetApiKeyRequest,
    ) -> main_models.ResetApiKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.reset_api_key_with_options_async(api_key_id, request, headers, runtime)

    def revoke_token_plan_invite_link_with_options(
        self,
        request: main_models.RevokeTokenPlanInviteLinkRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RevokeTokenPlanInviteLinkResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'RevokeTokenPlanInviteLink',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/tokenplan/invite/link/revoke',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokeTokenPlanInviteLinkResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_token_plan_invite_link_with_options_async(
        self,
        request: main_models.RevokeTokenPlanInviteLinkRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RevokeTokenPlanInviteLinkResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'RevokeTokenPlanInviteLink',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/tokenplan/invite/link/revoke',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokeTokenPlanInviteLinkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_token_plan_invite_link(
        self,
        request: main_models.RevokeTokenPlanInviteLinkRequest,
    ) -> main_models.RevokeTokenPlanInviteLinkResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.revoke_token_plan_invite_link_with_options(request, headers, runtime)

    async def revoke_token_plan_invite_link_async(
        self,
        request: main_models.RevokeTokenPlanInviteLinkRequest,
    ) -> main_models.RevokeTokenPlanInviteLinkResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.revoke_token_plan_invite_link_with_options_async(request, headers, runtime)

    def rotate_token_plan_key_with_options(
        self,
        request: main_models.RotateTokenPlanKeyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RotateTokenPlanKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_key_id):
            query['ApiKeyId'] = request.api_key_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RotateTokenPlanKey',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/tokenplan/api-key-rotations',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RotateTokenPlanKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def rotate_token_plan_key_with_options_async(
        self,
        request: main_models.RotateTokenPlanKeyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RotateTokenPlanKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_key_id):
            query['ApiKeyId'] = request.api_key_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RotateTokenPlanKey',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/tokenplan/api-key-rotations',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RotateTokenPlanKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rotate_token_plan_key(
        self,
        request: main_models.RotateTokenPlanKeyRequest,
    ) -> main_models.RotateTokenPlanKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.rotate_token_plan_key_with_options(request, headers, runtime)

    async def rotate_token_plan_key_async(
        self,
        request: main_models.RotateTokenPlanKeyRequest,
    ) -> main_models.RotateTokenPlanKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.rotate_token_plan_key_with_options_async(request, headers, runtime)

    def set_token_plan_org_invite_config_with_options(
        self,
        request: main_models.SetTokenPlanOrgInviteConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SetTokenPlanOrgInviteConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.default_role_id):
            query['DefaultRoleId'] = request.default_role_id
        if not DaraCore.is_null(request.seat_assign_strategy):
            query['SeatAssignStrategy'] = request.seat_assign_strategy
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetTokenPlanOrgInviteConfig',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/tokenplan/invite/config/set',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetTokenPlanOrgInviteConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_token_plan_org_invite_config_with_options_async(
        self,
        request: main_models.SetTokenPlanOrgInviteConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SetTokenPlanOrgInviteConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.default_role_id):
            query['DefaultRoleId'] = request.default_role_id
        if not DaraCore.is_null(request.seat_assign_strategy):
            query['SeatAssignStrategy'] = request.seat_assign_strategy
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetTokenPlanOrgInviteConfig',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/tokenplan/invite/config/set',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetTokenPlanOrgInviteConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_token_plan_org_invite_config(
        self,
        request: main_models.SetTokenPlanOrgInviteConfigRequest,
    ) -> main_models.SetTokenPlanOrgInviteConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.set_token_plan_org_invite_config_with_options(request, headers, runtime)

    async def set_token_plan_org_invite_config_async(
        self,
        request: main_models.SetTokenPlanOrgInviteConfigRequest,
    ) -> main_models.SetTokenPlanOrgInviteConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.set_token_plan_org_invite_config_with_options_async(request, headers, runtime)

    def update_api_key_with_options(
        self,
        api_key_id: str,
        request: main_models.UpdateApiKeyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApiKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        body = {}
        if not DaraCore.is_null(request.auth):
            body['auth'] = request.auth
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApiKey',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/modelstudio/apikeys/{DaraURL.percent_encode(api_key_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApiKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_api_key_with_options_async(
        self,
        api_key_id: str,
        request: main_models.UpdateApiKeyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApiKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['description'] = request.description
        body = {}
        if not DaraCore.is_null(request.auth):
            body['auth'] = request.auth
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApiKey',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/modelstudio/apikeys/{DaraURL.percent_encode(api_key_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApiKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_api_key(
        self,
        api_key_id: str,
        request: main_models.UpdateApiKeyRequest,
    ) -> main_models.UpdateApiKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_api_key_with_options(api_key_id, request, headers, runtime)

    async def update_api_key_async(
        self,
        api_key_id: str,
        request: main_models.UpdateApiKeyRequest,
    ) -> main_models.UpdateApiKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_api_key_with_options_async(api_key_id, request, headers, runtime)

    def update_organization_with_options(
        self,
        request: main_models.UpdateOrganizationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateOrganizationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateOrganization',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/tokenplan/organization',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateOrganizationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_organization_with_options_async(
        self,
        request: main_models.UpdateOrganizationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateOrganizationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateOrganization',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/tokenplan/organization',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateOrganizationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_organization(
        self,
        request: main_models.UpdateOrganizationRequest,
    ) -> main_models.UpdateOrganizationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_organization_with_options(request, headers, runtime)

    async def update_organization_async(
        self,
        request: main_models.UpdateOrganizationRequest,
    ) -> main_models.UpdateOrganizationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_organization_with_options_async(request, headers, runtime)

    def update_organization_member_with_options(
        self,
        request: main_models.UpdateOrganizationMemberRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateOrganizationMemberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_ids):
            query['AccountIds'] = request.account_ids
        if not DaraCore.is_null(request.new_role_code):
            query['NewRoleCode'] = request.new_role_code
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateOrganizationMember',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/tokenplan/organization/members/update',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateOrganizationMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_organization_member_with_options_async(
        self,
        request: main_models.UpdateOrganizationMemberRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateOrganizationMemberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_ids):
            query['AccountIds'] = request.account_ids
        if not DaraCore.is_null(request.new_role_code):
            query['NewRoleCode'] = request.new_role_code
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateOrganizationMember',
            version = '2026-02-10',
            protocol = 'HTTPS',
            pathname = f'/tokenplan/organization/members/update',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateOrganizationMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_organization_member(
        self,
        request: main_models.UpdateOrganizationMemberRequest,
    ) -> main_models.UpdateOrganizationMemberResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_organization_member_with_options(request, headers, runtime)

    async def update_organization_member_async(
        self,
        request: main_models.UpdateOrganizationMemberRequest,
    ) -> main_models.UpdateOrganizationMemberResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_organization_member_with_options_async(request, headers, runtime)
