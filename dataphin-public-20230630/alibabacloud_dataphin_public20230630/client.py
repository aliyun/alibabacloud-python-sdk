# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_dataphin_public20230630 import models as main_models
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
        self._endpoint = self.get_endpoint('dataphin-public', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_data_service_project_member_with_options(
        self,
        tmp_req: main_models.AddDataServiceProjectMemberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddDataServiceProjectMemberResponse:
        tmp_req.validate()
        request = main_models.AddDataServiceProjectMemberShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.add_command):
            request.add_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.add_command, 'AddCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        body = {}
        if not DaraCore.is_null(request.add_command_shrink):
            body['AddCommand'] = request.add_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddDataServiceProjectMember',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDataServiceProjectMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_data_service_project_member_with_options_async(
        self,
        tmp_req: main_models.AddDataServiceProjectMemberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddDataServiceProjectMemberResponse:
        tmp_req.validate()
        request = main_models.AddDataServiceProjectMemberShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.add_command):
            request.add_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.add_command, 'AddCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        body = {}
        if not DaraCore.is_null(request.add_command_shrink):
            body['AddCommand'] = request.add_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddDataServiceProjectMember',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDataServiceProjectMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_data_service_project_member(
        self,
        request: main_models.AddDataServiceProjectMemberRequest,
    ) -> main_models.AddDataServiceProjectMemberResponse:
        runtime = RuntimeOptions()
        return self.add_data_service_project_member_with_options(request, runtime)

    async def add_data_service_project_member_async(
        self,
        request: main_models.AddDataServiceProjectMemberRequest,
    ) -> main_models.AddDataServiceProjectMemberResponse:
        runtime = RuntimeOptions()
        return await self.add_data_service_project_member_with_options_async(request, runtime)

    def add_project_member_with_options(
        self,
        tmp_req: main_models.AddProjectMemberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddProjectMemberResponse:
        tmp_req.validate()
        request = main_models.AddProjectMemberShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.add_command):
            request.add_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.add_command, 'AddCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.add_command_shrink):
            body['AddCommand'] = request.add_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddProjectMember',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddProjectMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_project_member_with_options_async(
        self,
        tmp_req: main_models.AddProjectMemberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddProjectMemberResponse:
        tmp_req.validate()
        request = main_models.AddProjectMemberShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.add_command):
            request.add_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.add_command, 'AddCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.add_command_shrink):
            body['AddCommand'] = request.add_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddProjectMember',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddProjectMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_project_member(
        self,
        request: main_models.AddProjectMemberRequest,
    ) -> main_models.AddProjectMemberResponse:
        runtime = RuntimeOptions()
        return self.add_project_member_with_options(request, runtime)

    async def add_project_member_async(
        self,
        request: main_models.AddProjectMemberRequest,
    ) -> main_models.AddProjectMemberResponse:
        runtime = RuntimeOptions()
        return await self.add_project_member_with_options_async(request, runtime)

    def add_register_lineage_with_options(
        self,
        tmp_req: main_models.AddRegisterLineageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddRegisterLineageResponse:
        tmp_req.validate()
        request = main_models.AddRegisterLineageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.add_register_lineage_command):
            request.add_register_lineage_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.add_register_lineage_command, 'AddRegisterLineageCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.add_register_lineage_command_shrink):
            body['AddRegisterLineageCommand'] = request.add_register_lineage_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddRegisterLineage',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddRegisterLineageResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_register_lineage_with_options_async(
        self,
        tmp_req: main_models.AddRegisterLineageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddRegisterLineageResponse:
        tmp_req.validate()
        request = main_models.AddRegisterLineageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.add_register_lineage_command):
            request.add_register_lineage_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.add_register_lineage_command, 'AddRegisterLineageCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.add_register_lineage_command_shrink):
            body['AddRegisterLineageCommand'] = request.add_register_lineage_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddRegisterLineage',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddRegisterLineageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_register_lineage(
        self,
        request: main_models.AddRegisterLineageRequest,
    ) -> main_models.AddRegisterLineageResponse:
        runtime = RuntimeOptions()
        return self.add_register_lineage_with_options(request, runtime)

    async def add_register_lineage_async(
        self,
        request: main_models.AddRegisterLineageRequest,
    ) -> main_models.AddRegisterLineageResponse:
        runtime = RuntimeOptions()
        return await self.add_register_lineage_with_options_async(request, runtime)

    def add_tenant_members_with_options(
        self,
        tmp_req: main_models.AddTenantMembersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddTenantMembersResponse:
        tmp_req.validate()
        request = main_models.AddTenantMembersShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.add_command):
            request.add_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.add_command, 'AddCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.add_command_shrink):
            body['AddCommand'] = request.add_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddTenantMembers',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddTenantMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_tenant_members_with_options_async(
        self,
        tmp_req: main_models.AddTenantMembersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddTenantMembersResponse:
        tmp_req.validate()
        request = main_models.AddTenantMembersShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.add_command):
            request.add_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.add_command, 'AddCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.add_command_shrink):
            body['AddCommand'] = request.add_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddTenantMembers',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddTenantMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_tenant_members(
        self,
        request: main_models.AddTenantMembersRequest,
    ) -> main_models.AddTenantMembersResponse:
        runtime = RuntimeOptions()
        return self.add_tenant_members_with_options(request, runtime)

    async def add_tenant_members_async(
        self,
        request: main_models.AddTenantMembersRequest,
    ) -> main_models.AddTenantMembersResponse:
        runtime = RuntimeOptions()
        return await self.add_tenant_members_with_options_async(request, runtime)

    def add_tenant_members_by_source_user_with_options(
        self,
        tmp_req: main_models.AddTenantMembersBySourceUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddTenantMembersBySourceUserResponse:
        tmp_req.validate()
        request = main_models.AddTenantMembersBySourceUserShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.add_command):
            request.add_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.add_command, 'AddCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.add_command_shrink):
            body['AddCommand'] = request.add_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddTenantMembersBySourceUser',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddTenantMembersBySourceUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_tenant_members_by_source_user_with_options_async(
        self,
        tmp_req: main_models.AddTenantMembersBySourceUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddTenantMembersBySourceUserResponse:
        tmp_req.validate()
        request = main_models.AddTenantMembersBySourceUserShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.add_command):
            request.add_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.add_command, 'AddCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.add_command_shrink):
            body['AddCommand'] = request.add_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddTenantMembersBySourceUser',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddTenantMembersBySourceUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_tenant_members_by_source_user(
        self,
        request: main_models.AddTenantMembersBySourceUserRequest,
    ) -> main_models.AddTenantMembersBySourceUserResponse:
        runtime = RuntimeOptions()
        return self.add_tenant_members_by_source_user_with_options(request, runtime)

    async def add_tenant_members_by_source_user_async(
        self,
        request: main_models.AddTenantMembersBySourceUserRequest,
    ) -> main_models.AddTenantMembersBySourceUserResponse:
        runtime = RuntimeOptions()
        return await self.add_tenant_members_by_source_user_with_options_async(request, runtime)

    def add_user_group_member_with_options(
        self,
        tmp_req: main_models.AddUserGroupMemberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddUserGroupMemberResponse:
        tmp_req.validate()
        request = main_models.AddUserGroupMemberShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.add_command):
            request.add_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.add_command, 'AddCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.add_command_shrink):
            body['AddCommand'] = request.add_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddUserGroupMember',
            version = '2023-06-30',
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
        tmp_req: main_models.AddUserGroupMemberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddUserGroupMemberResponse:
        tmp_req.validate()
        request = main_models.AddUserGroupMemberShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.add_command):
            request.add_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.add_command, 'AddCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.add_command_shrink):
            body['AddCommand'] = request.add_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddUserGroupMember',
            version = '2023-06-30',
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

    def apply_data_service_api_with_options(
        self,
        tmp_req: main_models.ApplyDataServiceApiRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ApplyDataServiceApiResponse:
        tmp_req.validate()
        request = main_models.ApplyDataServiceApiShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.apply_command):
            request.apply_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.apply_command, 'ApplyCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        body = {}
        if not DaraCore.is_null(request.apply_command_shrink):
            body['ApplyCommand'] = request.apply_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ApplyDataServiceApi',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApplyDataServiceApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_data_service_api_with_options_async(
        self,
        tmp_req: main_models.ApplyDataServiceApiRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ApplyDataServiceApiResponse:
        tmp_req.validate()
        request = main_models.ApplyDataServiceApiShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.apply_command):
            request.apply_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.apply_command, 'ApplyCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        body = {}
        if not DaraCore.is_null(request.apply_command_shrink):
            body['ApplyCommand'] = request.apply_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ApplyDataServiceApi',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApplyDataServiceApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_data_service_api(
        self,
        request: main_models.ApplyDataServiceApiRequest,
    ) -> main_models.ApplyDataServiceApiResponse:
        runtime = RuntimeOptions()
        return self.apply_data_service_api_with_options(request, runtime)

    async def apply_data_service_api_async(
        self,
        request: main_models.ApplyDataServiceApiRequest,
    ) -> main_models.ApplyDataServiceApiResponse:
        runtime = RuntimeOptions()
        return await self.apply_data_service_api_with_options_async(request, runtime)

    def apply_data_service_app_with_options(
        self,
        tmp_req: main_models.ApplyDataServiceAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ApplyDataServiceAppResponse:
        tmp_req.validate()
        request = main_models.ApplyDataServiceAppShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.apply_command):
            request.apply_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.apply_command, 'ApplyCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        body = {}
        if not DaraCore.is_null(request.apply_command_shrink):
            body['ApplyCommand'] = request.apply_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ApplyDataServiceApp',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApplyDataServiceAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_data_service_app_with_options_async(
        self,
        tmp_req: main_models.ApplyDataServiceAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ApplyDataServiceAppResponse:
        tmp_req.validate()
        request = main_models.ApplyDataServiceAppShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.apply_command):
            request.apply_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.apply_command, 'ApplyCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        body = {}
        if not DaraCore.is_null(request.apply_command_shrink):
            body['ApplyCommand'] = request.apply_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ApplyDataServiceApp',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApplyDataServiceAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_data_service_app(
        self,
        request: main_models.ApplyDataServiceAppRequest,
    ) -> main_models.ApplyDataServiceAppResponse:
        runtime = RuntimeOptions()
        return self.apply_data_service_app_with_options(request, runtime)

    async def apply_data_service_app_async(
        self,
        request: main_models.ApplyDataServiceAppRequest,
    ) -> main_models.ApplyDataServiceAppResponse:
        runtime = RuntimeOptions()
        return await self.apply_data_service_app_with_options_async(request, runtime)

    def assign_quality_rule_of_all_rule_scope_schedules_with_options(
        self,
        tmp_req: main_models.AssignQualityRuleOfAllRuleScopeSchedulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssignQualityRuleOfAllRuleScopeSchedulesResponse:
        tmp_req.validate()
        request = main_models.AssignQualityRuleOfAllRuleScopeSchedulesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.assign_command):
            request.assign_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.assign_command, 'AssignCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.assign_command_shrink):
            body['AssignCommand'] = request.assign_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AssignQualityRuleOfAllRuleScopeSchedules',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssignQualityRuleOfAllRuleScopeSchedulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def assign_quality_rule_of_all_rule_scope_schedules_with_options_async(
        self,
        tmp_req: main_models.AssignQualityRuleOfAllRuleScopeSchedulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssignQualityRuleOfAllRuleScopeSchedulesResponse:
        tmp_req.validate()
        request = main_models.AssignQualityRuleOfAllRuleScopeSchedulesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.assign_command):
            request.assign_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.assign_command, 'AssignCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.assign_command_shrink):
            body['AssignCommand'] = request.assign_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AssignQualityRuleOfAllRuleScopeSchedules',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssignQualityRuleOfAllRuleScopeSchedulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def assign_quality_rule_of_all_rule_scope_schedules(
        self,
        request: main_models.AssignQualityRuleOfAllRuleScopeSchedulesRequest,
    ) -> main_models.AssignQualityRuleOfAllRuleScopeSchedulesResponse:
        runtime = RuntimeOptions()
        return self.assign_quality_rule_of_all_rule_scope_schedules_with_options(request, runtime)

    async def assign_quality_rule_of_all_rule_scope_schedules_async(
        self,
        request: main_models.AssignQualityRuleOfAllRuleScopeSchedulesRequest,
    ) -> main_models.AssignQualityRuleOfAllRuleScopeSchedulesResponse:
        runtime = RuntimeOptions()
        return await self.assign_quality_rule_of_all_rule_scope_schedules_with_options_async(request, runtime)

    def check_compute_source_connectivity_with_options(
        self,
        tmp_req: main_models.CheckComputeSourceConnectivityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckComputeSourceConnectivityResponse:
        tmp_req.validate()
        request = main_models.CheckComputeSourceConnectivityShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.check_command):
            request.check_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.check_command, 'CheckCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.check_command_shrink):
            body['CheckCommand'] = request.check_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CheckComputeSourceConnectivity',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckComputeSourceConnectivityResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_compute_source_connectivity_with_options_async(
        self,
        tmp_req: main_models.CheckComputeSourceConnectivityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckComputeSourceConnectivityResponse:
        tmp_req.validate()
        request = main_models.CheckComputeSourceConnectivityShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.check_command):
            request.check_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.check_command, 'CheckCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.check_command_shrink):
            body['CheckCommand'] = request.check_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CheckComputeSourceConnectivity',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckComputeSourceConnectivityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_compute_source_connectivity(
        self,
        request: main_models.CheckComputeSourceConnectivityRequest,
    ) -> main_models.CheckComputeSourceConnectivityResponse:
        runtime = RuntimeOptions()
        return self.check_compute_source_connectivity_with_options(request, runtime)

    async def check_compute_source_connectivity_async(
        self,
        request: main_models.CheckComputeSourceConnectivityRequest,
    ) -> main_models.CheckComputeSourceConnectivityResponse:
        runtime = RuntimeOptions()
        return await self.check_compute_source_connectivity_with_options_async(request, runtime)

    def check_compute_source_connectivity_by_id_with_options(
        self,
        request: main_models.CheckComputeSourceConnectivityByIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckComputeSourceConnectivityByIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckComputeSourceConnectivityById',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckComputeSourceConnectivityByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_compute_source_connectivity_by_id_with_options_async(
        self,
        request: main_models.CheckComputeSourceConnectivityByIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckComputeSourceConnectivityByIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckComputeSourceConnectivityById',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckComputeSourceConnectivityByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_compute_source_connectivity_by_id(
        self,
        request: main_models.CheckComputeSourceConnectivityByIdRequest,
    ) -> main_models.CheckComputeSourceConnectivityByIdResponse:
        runtime = RuntimeOptions()
        return self.check_compute_source_connectivity_by_id_with_options(request, runtime)

    async def check_compute_source_connectivity_by_id_async(
        self,
        request: main_models.CheckComputeSourceConnectivityByIdRequest,
    ) -> main_models.CheckComputeSourceConnectivityByIdResponse:
        runtime = RuntimeOptions()
        return await self.check_compute_source_connectivity_by_id_with_options_async(request, runtime)

    def check_data_source_connectivity_with_options(
        self,
        tmp_req: main_models.CheckDataSourceConnectivityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckDataSourceConnectivityResponse:
        tmp_req.validate()
        request = main_models.CheckDataSourceConnectivityShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.check_command):
            request.check_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.check_command, 'CheckCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.check_command_shrink):
            body['CheckCommand'] = request.check_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CheckDataSourceConnectivity',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckDataSourceConnectivityResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_data_source_connectivity_with_options_async(
        self,
        tmp_req: main_models.CheckDataSourceConnectivityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckDataSourceConnectivityResponse:
        tmp_req.validate()
        request = main_models.CheckDataSourceConnectivityShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.check_command):
            request.check_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.check_command, 'CheckCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.check_command_shrink):
            body['CheckCommand'] = request.check_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CheckDataSourceConnectivity',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckDataSourceConnectivityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_data_source_connectivity(
        self,
        request: main_models.CheckDataSourceConnectivityRequest,
    ) -> main_models.CheckDataSourceConnectivityResponse:
        runtime = RuntimeOptions()
        return self.check_data_source_connectivity_with_options(request, runtime)

    async def check_data_source_connectivity_async(
        self,
        request: main_models.CheckDataSourceConnectivityRequest,
    ) -> main_models.CheckDataSourceConnectivityResponse:
        runtime = RuntimeOptions()
        return await self.check_data_source_connectivity_with_options_async(request, runtime)

    def check_data_source_connectivity_by_id_with_options(
        self,
        request: main_models.CheckDataSourceConnectivityByIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckDataSourceConnectivityByIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckDataSourceConnectivityById',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckDataSourceConnectivityByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_data_source_connectivity_by_id_with_options_async(
        self,
        request: main_models.CheckDataSourceConnectivityByIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckDataSourceConnectivityByIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckDataSourceConnectivityById',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckDataSourceConnectivityByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_data_source_connectivity_by_id(
        self,
        request: main_models.CheckDataSourceConnectivityByIdRequest,
    ) -> main_models.CheckDataSourceConnectivityByIdResponse:
        runtime = RuntimeOptions()
        return self.check_data_source_connectivity_by_id_with_options(request, runtime)

    async def check_data_source_connectivity_by_id_async(
        self,
        request: main_models.CheckDataSourceConnectivityByIdRequest,
    ) -> main_models.CheckDataSourceConnectivityByIdResponse:
        runtime = RuntimeOptions()
        return await self.check_data_source_connectivity_by_id_with_options_async(request, runtime)

    def check_project_has_dependency_with_options(
        self,
        request: main_models.CheckProjectHasDependencyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckProjectHasDependencyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckProjectHasDependency',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckProjectHasDependencyResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_project_has_dependency_with_options_async(
        self,
        request: main_models.CheckProjectHasDependencyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckProjectHasDependencyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckProjectHasDependency',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckProjectHasDependencyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_project_has_dependency(
        self,
        request: main_models.CheckProjectHasDependencyRequest,
    ) -> main_models.CheckProjectHasDependencyResponse:
        runtime = RuntimeOptions()
        return self.check_project_has_dependency_with_options(request, runtime)

    async def check_project_has_dependency_async(
        self,
        request: main_models.CheckProjectHasDependencyRequest,
    ) -> main_models.CheckProjectHasDependencyResponse:
        runtime = RuntimeOptions()
        return await self.check_project_has_dependency_with_options_async(request, runtime)

    def check_resource_permission_with_options(
        self,
        tmp_req: main_models.CheckResourcePermissionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckResourcePermissionResponse:
        tmp_req.validate()
        request = main_models.CheckResourcePermissionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.check_command):
            request.check_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.check_command, 'CheckCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.check_command_shrink):
            body['CheckCommand'] = request.check_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CheckResourcePermission',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckResourcePermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_resource_permission_with_options_async(
        self,
        tmp_req: main_models.CheckResourcePermissionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckResourcePermissionResponse:
        tmp_req.validate()
        request = main_models.CheckResourcePermissionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.check_command):
            request.check_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.check_command, 'CheckCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.check_command_shrink):
            body['CheckCommand'] = request.check_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CheckResourcePermission',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckResourcePermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_resource_permission(
        self,
        request: main_models.CheckResourcePermissionRequest,
    ) -> main_models.CheckResourcePermissionResponse:
        runtime = RuntimeOptions()
        return self.check_resource_permission_with_options(request, runtime)

    async def check_resource_permission_async(
        self,
        request: main_models.CheckResourcePermissionRequest,
    ) -> main_models.CheckResourcePermissionResponse:
        runtime = RuntimeOptions()
        return await self.check_resource_permission_with_options_async(request, runtime)

    def create_ad_hoc_file_with_options(
        self,
        tmp_req: main_models.CreateAdHocFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAdHocFileResponse:
        tmp_req.validate()
        request = main_models.CreateAdHocFileShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_command):
            request.create_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAdHocFile',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAdHocFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ad_hoc_file_with_options_async(
        self,
        tmp_req: main_models.CreateAdHocFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAdHocFileResponse:
        tmp_req.validate()
        request = main_models.CreateAdHocFileShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_command):
            request.create_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAdHocFile',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAdHocFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ad_hoc_file(
        self,
        request: main_models.CreateAdHocFileRequest,
    ) -> main_models.CreateAdHocFileResponse:
        runtime = RuntimeOptions()
        return self.create_ad_hoc_file_with_options(request, runtime)

    async def create_ad_hoc_file_async(
        self,
        request: main_models.CreateAdHocFileRequest,
    ) -> main_models.CreateAdHocFileResponse:
        runtime = RuntimeOptions()
        return await self.create_ad_hoc_file_with_options_async(request, runtime)

    def create_batch_task_with_options(
        self,
        tmp_req: main_models.CreateBatchTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBatchTaskResponse:
        tmp_req.validate()
        request = main_models.CreateBatchTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_command):
            request.create_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateBatchTask',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBatchTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_batch_task_with_options_async(
        self,
        tmp_req: main_models.CreateBatchTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBatchTaskResponse:
        tmp_req.validate()
        request = main_models.CreateBatchTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_command):
            request.create_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateBatchTask',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBatchTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_batch_task(
        self,
        request: main_models.CreateBatchTaskRequest,
    ) -> main_models.CreateBatchTaskResponse:
        runtime = RuntimeOptions()
        return self.create_batch_task_with_options(request, runtime)

    async def create_batch_task_async(
        self,
        request: main_models.CreateBatchTaskRequest,
    ) -> main_models.CreateBatchTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_batch_task_with_options_async(request, runtime)

    def create_biz_entity_with_options(
        self,
        tmp_req: main_models.CreateBizEntityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBizEntityResponse:
        tmp_req.validate()
        request = main_models.CreateBizEntityShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_command):
            request.create_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateBizEntity',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBizEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_biz_entity_with_options_async(
        self,
        tmp_req: main_models.CreateBizEntityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBizEntityResponse:
        tmp_req.validate()
        request = main_models.CreateBizEntityShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_command):
            request.create_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateBizEntity',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBizEntityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_biz_entity(
        self,
        request: main_models.CreateBizEntityRequest,
    ) -> main_models.CreateBizEntityResponse:
        runtime = RuntimeOptions()
        return self.create_biz_entity_with_options(request, runtime)

    async def create_biz_entity_async(
        self,
        request: main_models.CreateBizEntityRequest,
    ) -> main_models.CreateBizEntityResponse:
        runtime = RuntimeOptions()
        return await self.create_biz_entity_with_options_async(request, runtime)

    def create_biz_metric_with_options(
        self,
        tmp_req: main_models.CreateBizMetricRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBizMetricResponse:
        tmp_req.validate()
        request = main_models.CreateBizMetricShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_biz_metric_command):
            request.create_biz_metric_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_biz_metric_command, 'CreateBizMetricCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.create_biz_metric_command_shrink):
            body['CreateBizMetricCommand'] = request.create_biz_metric_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateBizMetric',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBizMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_biz_metric_with_options_async(
        self,
        tmp_req: main_models.CreateBizMetricRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBizMetricResponse:
        tmp_req.validate()
        request = main_models.CreateBizMetricShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_biz_metric_command):
            request.create_biz_metric_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_biz_metric_command, 'CreateBizMetricCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.create_biz_metric_command_shrink):
            body['CreateBizMetricCommand'] = request.create_biz_metric_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateBizMetric',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBizMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_biz_metric(
        self,
        request: main_models.CreateBizMetricRequest,
    ) -> main_models.CreateBizMetricResponse:
        runtime = RuntimeOptions()
        return self.create_biz_metric_with_options(request, runtime)

    async def create_biz_metric_async(
        self,
        request: main_models.CreateBizMetricRequest,
    ) -> main_models.CreateBizMetricResponse:
        runtime = RuntimeOptions()
        return await self.create_biz_metric_with_options_async(request, runtime)

    def create_biz_unit_with_options(
        self,
        tmp_req: main_models.CreateBizUnitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBizUnitResponse:
        tmp_req.validate()
        request = main_models.CreateBizUnitShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_command):
            request.create_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateBizUnit',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBizUnitResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_biz_unit_with_options_async(
        self,
        tmp_req: main_models.CreateBizUnitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBizUnitResponse:
        tmp_req.validate()
        request = main_models.CreateBizUnitShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_command):
            request.create_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateBizUnit',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBizUnitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_biz_unit(
        self,
        request: main_models.CreateBizUnitRequest,
    ) -> main_models.CreateBizUnitResponse:
        runtime = RuntimeOptions()
        return self.create_biz_unit_with_options(request, runtime)

    async def create_biz_unit_async(
        self,
        request: main_models.CreateBizUnitRequest,
    ) -> main_models.CreateBizUnitResponse:
        runtime = RuntimeOptions()
        return await self.create_biz_unit_with_options_async(request, runtime)

    def create_compute_source_with_options(
        self,
        tmp_req: main_models.CreateComputeSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateComputeSourceResponse:
        tmp_req.validate()
        request = main_models.CreateComputeSourceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_command):
            request.create_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateComputeSource',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateComputeSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_compute_source_with_options_async(
        self,
        tmp_req: main_models.CreateComputeSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateComputeSourceResponse:
        tmp_req.validate()
        request = main_models.CreateComputeSourceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_command):
            request.create_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateComputeSource',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateComputeSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_compute_source(
        self,
        request: main_models.CreateComputeSourceRequest,
    ) -> main_models.CreateComputeSourceResponse:
        runtime = RuntimeOptions()
        return self.create_compute_source_with_options(request, runtime)

    async def create_compute_source_async(
        self,
        request: main_models.CreateComputeSourceRequest,
    ) -> main_models.CreateComputeSourceResponse:
        runtime = RuntimeOptions()
        return await self.create_compute_source_with_options_async(request, runtime)

    def create_data_domain_with_options(
        self,
        tmp_req: main_models.CreateDataDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataDomainResponse:
        tmp_req.validate()
        request = main_models.CreateDataDomainShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_command):
            request.create_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataDomain',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_domain_with_options_async(
        self,
        tmp_req: main_models.CreateDataDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataDomainResponse:
        tmp_req.validate()
        request = main_models.CreateDataDomainShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_command):
            request.create_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataDomain',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_domain(
        self,
        request: main_models.CreateDataDomainRequest,
    ) -> main_models.CreateDataDomainResponse:
        runtime = RuntimeOptions()
        return self.create_data_domain_with_options(request, runtime)

    async def create_data_domain_async(
        self,
        request: main_models.CreateDataDomainRequest,
    ) -> main_models.CreateDataDomainResponse:
        runtime = RuntimeOptions()
        return await self.create_data_domain_with_options_async(request, runtime)

    def create_data_service_api_with_options(
        self,
        tmp_req: main_models.CreateDataServiceApiRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataServiceApiResponse:
        tmp_req.validate()
        request = main_models.CreateDataServiceApiShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_command):
            request.create_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataServiceApi',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataServiceApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_service_api_with_options_async(
        self,
        tmp_req: main_models.CreateDataServiceApiRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataServiceApiResponse:
        tmp_req.validate()
        request = main_models.CreateDataServiceApiShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_command):
            request.create_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataServiceApi',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataServiceApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_service_api(
        self,
        request: main_models.CreateDataServiceApiRequest,
    ) -> main_models.CreateDataServiceApiResponse:
        runtime = RuntimeOptions()
        return self.create_data_service_api_with_options(request, runtime)

    async def create_data_service_api_async(
        self,
        request: main_models.CreateDataServiceApiRequest,
    ) -> main_models.CreateDataServiceApiResponse:
        runtime = RuntimeOptions()
        return await self.create_data_service_api_with_options_async(request, runtime)

    def create_data_source_with_options(
        self,
        tmp_req: main_models.CreateDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataSourceResponse:
        tmp_req.validate()
        request = main_models.CreateDataSourceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_command):
            request.create_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataSource',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_source_with_options_async(
        self,
        tmp_req: main_models.CreateDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataSourceResponse:
        tmp_req.validate()
        request = main_models.CreateDataSourceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_command):
            request.create_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataSource',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_source(
        self,
        request: main_models.CreateDataSourceRequest,
    ) -> main_models.CreateDataSourceResponse:
        runtime = RuntimeOptions()
        return self.create_data_source_with_options(request, runtime)

    async def create_data_source_async(
        self,
        request: main_models.CreateDataSourceRequest,
    ) -> main_models.CreateDataSourceResponse:
        runtime = RuntimeOptions()
        return await self.create_data_source_with_options_async(request, runtime)

    def create_directory_with_options(
        self,
        tmp_req: main_models.CreateDirectoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDirectoryResponse:
        tmp_req.validate()
        request = main_models.CreateDirectoryShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_command):
            request.create_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDirectory',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_directory_with_options_async(
        self,
        tmp_req: main_models.CreateDirectoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDirectoryResponse:
        tmp_req.validate()
        request = main_models.CreateDirectoryShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_command):
            request.create_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDirectory',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_directory(
        self,
        request: main_models.CreateDirectoryRequest,
    ) -> main_models.CreateDirectoryResponse:
        runtime = RuntimeOptions()
        return self.create_directory_with_options(request, runtime)

    async def create_directory_async(
        self,
        request: main_models.CreateDirectoryRequest,
    ) -> main_models.CreateDirectoryResponse:
        runtime = RuntimeOptions()
        return await self.create_directory_with_options_async(request, runtime)

    def create_node_supplement_with_options(
        self,
        tmp_req: main_models.CreateNodeSupplementRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNodeSupplementResponse:
        tmp_req.validate()
        request = main_models.CreateNodeSupplementShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_command):
            request.create_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateNodeSupplement',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNodeSupplementResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_node_supplement_with_options_async(
        self,
        tmp_req: main_models.CreateNodeSupplementRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNodeSupplementResponse:
        tmp_req.validate()
        request = main_models.CreateNodeSupplementShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_command):
            request.create_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateNodeSupplement',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNodeSupplementResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_node_supplement(
        self,
        request: main_models.CreateNodeSupplementRequest,
    ) -> main_models.CreateNodeSupplementResponse:
        runtime = RuntimeOptions()
        return self.create_node_supplement_with_options(request, runtime)

    async def create_node_supplement_async(
        self,
        request: main_models.CreateNodeSupplementRequest,
    ) -> main_models.CreateNodeSupplementResponse:
        runtime = RuntimeOptions()
        return await self.create_node_supplement_with_options_async(request, runtime)

    def create_pipeline_with_options(
        self,
        tmp_req: main_models.CreatePipelineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePipelineResponse:
        tmp_req.validate()
        request = main_models.CreatePipelineShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.context):
            request.context_shrink = Utils.array_to_string_with_specified_style(tmp_req.context, 'Context', 'json')
        if not DaraCore.is_null(tmp_req.create_command):
            request.create_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.context_shrink):
            body['Context'] = request.context_shrink
        if not DaraCore.is_null(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePipeline',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_pipeline_with_options_async(
        self,
        tmp_req: main_models.CreatePipelineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePipelineResponse:
        tmp_req.validate()
        request = main_models.CreatePipelineShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.context):
            request.context_shrink = Utils.array_to_string_with_specified_style(tmp_req.context, 'Context', 'json')
        if not DaraCore.is_null(tmp_req.create_command):
            request.create_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.context_shrink):
            body['Context'] = request.context_shrink
        if not DaraCore.is_null(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePipeline',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePipelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_pipeline(
        self,
        request: main_models.CreatePipelineRequest,
    ) -> main_models.CreatePipelineResponse:
        runtime = RuntimeOptions()
        return self.create_pipeline_with_options(request, runtime)

    async def create_pipeline_async(
        self,
        request: main_models.CreatePipelineRequest,
    ) -> main_models.CreatePipelineResponse:
        runtime = RuntimeOptions()
        return await self.create_pipeline_with_options_async(request, runtime)

    def create_pipeline_by_async_with_options(
        self,
        tmp_req: main_models.CreatePipelineByAsyncRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePipelineByAsyncResponse:
        tmp_req.validate()
        request = main_models.CreatePipelineByAsyncShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.context):
            request.context_shrink = Utils.array_to_string_with_specified_style(tmp_req.context, 'Context', 'json')
        if not DaraCore.is_null(tmp_req.create_command):
            request.create_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.context_shrink):
            body['Context'] = request.context_shrink
        if not DaraCore.is_null(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePipelineByAsync',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePipelineByAsyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_pipeline_by_async_with_options_async(
        self,
        tmp_req: main_models.CreatePipelineByAsyncRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePipelineByAsyncResponse:
        tmp_req.validate()
        request = main_models.CreatePipelineByAsyncShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.context):
            request.context_shrink = Utils.array_to_string_with_specified_style(tmp_req.context, 'Context', 'json')
        if not DaraCore.is_null(tmp_req.create_command):
            request.create_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.context_shrink):
            body['Context'] = request.context_shrink
        if not DaraCore.is_null(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePipelineByAsync',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePipelineByAsyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_pipeline_by_async(
        self,
        request: main_models.CreatePipelineByAsyncRequest,
    ) -> main_models.CreatePipelineByAsyncResponse:
        runtime = RuntimeOptions()
        return self.create_pipeline_by_async_with_options(request, runtime)

    async def create_pipeline_by_async_async(
        self,
        request: main_models.CreatePipelineByAsyncRequest,
    ) -> main_models.CreatePipelineByAsyncResponse:
        runtime = RuntimeOptions()
        return await self.create_pipeline_by_async_with_options_async(request, runtime)

    def create_pipeline_node_with_options(
        self,
        tmp_req: main_models.CreatePipelineNodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePipelineNodeResponse:
        tmp_req.validate()
        request = main_models.CreatePipelineNodeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_pipeline_node_command):
            request.create_pipeline_node_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_pipeline_node_command, 'CreatePipelineNodeCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.create_pipeline_node_command_shrink):
            body['CreatePipelineNodeCommand'] = request.create_pipeline_node_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePipelineNode',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePipelineNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_pipeline_node_with_options_async(
        self,
        tmp_req: main_models.CreatePipelineNodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePipelineNodeResponse:
        tmp_req.validate()
        request = main_models.CreatePipelineNodeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_pipeline_node_command):
            request.create_pipeline_node_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_pipeline_node_command, 'CreatePipelineNodeCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.create_pipeline_node_command_shrink):
            body['CreatePipelineNodeCommand'] = request.create_pipeline_node_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePipelineNode',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePipelineNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_pipeline_node(
        self,
        request: main_models.CreatePipelineNodeRequest,
    ) -> main_models.CreatePipelineNodeResponse:
        runtime = RuntimeOptions()
        return self.create_pipeline_node_with_options(request, runtime)

    async def create_pipeline_node_async(
        self,
        request: main_models.CreatePipelineNodeRequest,
    ) -> main_models.CreatePipelineNodeResponse:
        runtime = RuntimeOptions()
        return await self.create_pipeline_node_with_options_async(request, runtime)

    def create_resource_with_options(
        self,
        tmp_req: main_models.CreateResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateResourceResponse:
        tmp_req.validate()
        request = main_models.CreateResourceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_command):
            request.create_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateResource',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_resource_with_options_async(
        self,
        tmp_req: main_models.CreateResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateResourceResponse:
        tmp_req.validate()
        request = main_models.CreateResourceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_command):
            request.create_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateResource',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_resource(
        self,
        request: main_models.CreateResourceRequest,
    ) -> main_models.CreateResourceResponse:
        runtime = RuntimeOptions()
        return self.create_resource_with_options(request, runtime)

    async def create_resource_async(
        self,
        request: main_models.CreateResourceRequest,
    ) -> main_models.CreateResourceResponse:
        runtime = RuntimeOptions()
        return await self.create_resource_with_options_async(request, runtime)

    def create_row_permission_with_options(
        self,
        tmp_req: main_models.CreateRowPermissionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRowPermissionResponse:
        tmp_req.validate()
        request = main_models.CreateRowPermissionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_row_permission_command):
            request.create_row_permission_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_row_permission_command, 'CreateRowPermissionCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.create_row_permission_command_shrink):
            body['CreateRowPermissionCommand'] = request.create_row_permission_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateRowPermission',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRowPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_row_permission_with_options_async(
        self,
        tmp_req: main_models.CreateRowPermissionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRowPermissionResponse:
        tmp_req.validate()
        request = main_models.CreateRowPermissionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_row_permission_command):
            request.create_row_permission_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_row_permission_command, 'CreateRowPermissionCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.create_row_permission_command_shrink):
            body['CreateRowPermissionCommand'] = request.create_row_permission_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateRowPermission',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRowPermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_row_permission(
        self,
        request: main_models.CreateRowPermissionRequest,
    ) -> main_models.CreateRowPermissionResponse:
        runtime = RuntimeOptions()
        return self.create_row_permission_with_options(request, runtime)

    async def create_row_permission_async(
        self,
        request: main_models.CreateRowPermissionRequest,
    ) -> main_models.CreateRowPermissionResponse:
        runtime = RuntimeOptions()
        return await self.create_row_permission_with_options_async(request, runtime)

    def create_security_classify_with_options(
        self,
        tmp_req: main_models.CreateSecurityClassifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSecurityClassifyResponse:
        tmp_req.validate()
        request = main_models.CreateSecurityClassifyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_command):
            request.create_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSecurityClassify',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSecurityClassifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_security_classify_with_options_async(
        self,
        tmp_req: main_models.CreateSecurityClassifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSecurityClassifyResponse:
        tmp_req.validate()
        request = main_models.CreateSecurityClassifyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_command):
            request.create_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSecurityClassify',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSecurityClassifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_security_classify(
        self,
        request: main_models.CreateSecurityClassifyRequest,
    ) -> main_models.CreateSecurityClassifyResponse:
        runtime = RuntimeOptions()
        return self.create_security_classify_with_options(request, runtime)

    async def create_security_classify_async(
        self,
        request: main_models.CreateSecurityClassifyRequest,
    ) -> main_models.CreateSecurityClassifyResponse:
        runtime = RuntimeOptions()
        return await self.create_security_classify_with_options_async(request, runtime)

    def create_security_classify_catalog_with_options(
        self,
        tmp_req: main_models.CreateSecurityClassifyCatalogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSecurityClassifyCatalogResponse:
        tmp_req.validate()
        request = main_models.CreateSecurityClassifyCatalogShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_command):
            request.create_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSecurityClassifyCatalog',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSecurityClassifyCatalogResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_security_classify_catalog_with_options_async(
        self,
        tmp_req: main_models.CreateSecurityClassifyCatalogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSecurityClassifyCatalogResponse:
        tmp_req.validate()
        request = main_models.CreateSecurityClassifyCatalogShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_command):
            request.create_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSecurityClassifyCatalog',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSecurityClassifyCatalogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_security_classify_catalog(
        self,
        request: main_models.CreateSecurityClassifyCatalogRequest,
    ) -> main_models.CreateSecurityClassifyCatalogResponse:
        runtime = RuntimeOptions()
        return self.create_security_classify_catalog_with_options(request, runtime)

    async def create_security_classify_catalog_async(
        self,
        request: main_models.CreateSecurityClassifyCatalogRequest,
    ) -> main_models.CreateSecurityClassifyCatalogResponse:
        runtime = RuntimeOptions()
        return await self.create_security_classify_catalog_with_options_async(request, runtime)

    def create_security_identify_result_with_options(
        self,
        tmp_req: main_models.CreateSecurityIdentifyResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSecurityIdentifyResultResponse:
        tmp_req.validate()
        request = main_models.CreateSecurityIdentifyResultShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_command):
            request.create_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSecurityIdentifyResult',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSecurityIdentifyResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_security_identify_result_with_options_async(
        self,
        tmp_req: main_models.CreateSecurityIdentifyResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSecurityIdentifyResultResponse:
        tmp_req.validate()
        request = main_models.CreateSecurityIdentifyResultShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_command):
            request.create_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSecurityIdentifyResult',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSecurityIdentifyResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_security_identify_result(
        self,
        request: main_models.CreateSecurityIdentifyResultRequest,
    ) -> main_models.CreateSecurityIdentifyResultResponse:
        runtime = RuntimeOptions()
        return self.create_security_identify_result_with_options(request, runtime)

    async def create_security_identify_result_async(
        self,
        request: main_models.CreateSecurityIdentifyResultRequest,
    ) -> main_models.CreateSecurityIdentifyResultResponse:
        runtime = RuntimeOptions()
        return await self.create_security_identify_result_with_options_async(request, runtime)

    def create_security_level_with_options(
        self,
        tmp_req: main_models.CreateSecurityLevelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSecurityLevelResponse:
        tmp_req.validate()
        request = main_models.CreateSecurityLevelShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_command):
            request.create_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSecurityLevel',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSecurityLevelResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_security_level_with_options_async(
        self,
        tmp_req: main_models.CreateSecurityLevelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSecurityLevelResponse:
        tmp_req.validate()
        request = main_models.CreateSecurityLevelShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_command):
            request.create_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSecurityLevel',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSecurityLevelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_security_level(
        self,
        request: main_models.CreateSecurityLevelRequest,
    ) -> main_models.CreateSecurityLevelResponse:
        runtime = RuntimeOptions()
        return self.create_security_level_with_options(request, runtime)

    async def create_security_level_async(
        self,
        request: main_models.CreateSecurityLevelRequest,
    ) -> main_models.CreateSecurityLevelResponse:
        runtime = RuntimeOptions()
        return await self.create_security_level_with_options_async(request, runtime)

    def create_standard_with_options(
        self,
        tmp_req: main_models.CreateStandardRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateStandardResponse:
        tmp_req.validate()
        request = main_models.CreateStandardShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_command):
            request.create_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateStandard',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateStandardResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_standard_with_options_async(
        self,
        tmp_req: main_models.CreateStandardRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateStandardResponse:
        tmp_req.validate()
        request = main_models.CreateStandardShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_command):
            request.create_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateStandard',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateStandardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_standard(
        self,
        request: main_models.CreateStandardRequest,
    ) -> main_models.CreateStandardResponse:
        runtime = RuntimeOptions()
        return self.create_standard_with_options(request, runtime)

    async def create_standard_async(
        self,
        request: main_models.CreateStandardRequest,
    ) -> main_models.CreateStandardResponse:
        runtime = RuntimeOptions()
        return await self.create_standard_with_options_async(request, runtime)

    def create_standard_lookup_table_with_options(
        self,
        tmp_req: main_models.CreateStandardLookupTableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateStandardLookupTableResponse:
        tmp_req.validate()
        request = main_models.CreateStandardLookupTableShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_command):
            request.create_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateStandardLookupTable',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateStandardLookupTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_standard_lookup_table_with_options_async(
        self,
        tmp_req: main_models.CreateStandardLookupTableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateStandardLookupTableResponse:
        tmp_req.validate()
        request = main_models.CreateStandardLookupTableShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_command):
            request.create_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateStandardLookupTable',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateStandardLookupTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_standard_lookup_table(
        self,
        request: main_models.CreateStandardLookupTableRequest,
    ) -> main_models.CreateStandardLookupTableResponse:
        runtime = RuntimeOptions()
        return self.create_standard_lookup_table_with_options(request, runtime)

    async def create_standard_lookup_table_async(
        self,
        request: main_models.CreateStandardLookupTableRequest,
    ) -> main_models.CreateStandardLookupTableResponse:
        runtime = RuntimeOptions()
        return await self.create_standard_lookup_table_with_options_async(request, runtime)

    def create_standard_mapping_with_options(
        self,
        tmp_req: main_models.CreateStandardMappingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateStandardMappingResponse:
        tmp_req.validate()
        request = main_models.CreateStandardMappingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_command):
            request.create_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateStandardMapping',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateStandardMappingResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_standard_mapping_with_options_async(
        self,
        tmp_req: main_models.CreateStandardMappingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateStandardMappingResponse:
        tmp_req.validate()
        request = main_models.CreateStandardMappingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_command):
            request.create_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateStandardMapping',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateStandardMappingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_standard_mapping(
        self,
        request: main_models.CreateStandardMappingRequest,
    ) -> main_models.CreateStandardMappingResponse:
        runtime = RuntimeOptions()
        return self.create_standard_mapping_with_options(request, runtime)

    async def create_standard_mapping_async(
        self,
        request: main_models.CreateStandardMappingRequest,
    ) -> main_models.CreateStandardMappingResponse:
        runtime = RuntimeOptions()
        return await self.create_standard_mapping_with_options_async(request, runtime)

    def create_standard_relations_with_options(
        self,
        tmp_req: main_models.CreateStandardRelationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateStandardRelationsResponse:
        tmp_req.validate()
        request = main_models.CreateStandardRelationsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_command):
            request.create_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateStandardRelations',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateStandardRelationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_standard_relations_with_options_async(
        self,
        tmp_req: main_models.CreateStandardRelationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateStandardRelationsResponse:
        tmp_req.validate()
        request = main_models.CreateStandardRelationsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_command):
            request.create_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateStandardRelations',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateStandardRelationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_standard_relations(
        self,
        request: main_models.CreateStandardRelationsRequest,
    ) -> main_models.CreateStandardRelationsResponse:
        runtime = RuntimeOptions()
        return self.create_standard_relations_with_options(request, runtime)

    async def create_standard_relations_async(
        self,
        request: main_models.CreateStandardRelationsRequest,
    ) -> main_models.CreateStandardRelationsResponse:
        runtime = RuntimeOptions()
        return await self.create_standard_relations_with_options_async(request, runtime)

    def create_standard_set_with_options(
        self,
        tmp_req: main_models.CreateStandardSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateStandardSetResponse:
        tmp_req.validate()
        request = main_models.CreateStandardSetShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_command):
            request.create_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateStandardSet',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateStandardSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_standard_set_with_options_async(
        self,
        tmp_req: main_models.CreateStandardSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateStandardSetResponse:
        tmp_req.validate()
        request = main_models.CreateStandardSetShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_command):
            request.create_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateStandardSet',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateStandardSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_standard_set(
        self,
        request: main_models.CreateStandardSetRequest,
    ) -> main_models.CreateStandardSetResponse:
        runtime = RuntimeOptions()
        return self.create_standard_set_with_options(request, runtime)

    async def create_standard_set_async(
        self,
        request: main_models.CreateStandardSetRequest,
    ) -> main_models.CreateStandardSetResponse:
        runtime = RuntimeOptions()
        return await self.create_standard_set_with_options_async(request, runtime)

    def create_standard_template_with_options(
        self,
        tmp_req: main_models.CreateStandardTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateStandardTemplateResponse:
        tmp_req.validate()
        request = main_models.CreateStandardTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_command):
            request.create_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateStandardTemplate',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateStandardTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_standard_template_with_options_async(
        self,
        tmp_req: main_models.CreateStandardTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateStandardTemplateResponse:
        tmp_req.validate()
        request = main_models.CreateStandardTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_command):
            request.create_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateStandardTemplate',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateStandardTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_standard_template(
        self,
        request: main_models.CreateStandardTemplateRequest,
    ) -> main_models.CreateStandardTemplateResponse:
        runtime = RuntimeOptions()
        return self.create_standard_template_with_options(request, runtime)

    async def create_standard_template_async(
        self,
        request: main_models.CreateStandardTemplateRequest,
    ) -> main_models.CreateStandardTemplateResponse:
        runtime = RuntimeOptions()
        return await self.create_standard_template_with_options_async(request, runtime)

    def create_standard_word_root_with_options(
        self,
        tmp_req: main_models.CreateStandardWordRootRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateStandardWordRootResponse:
        tmp_req.validate()
        request = main_models.CreateStandardWordRootShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_command):
            request.create_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateStandardWordRoot',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateStandardWordRootResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_standard_word_root_with_options_async(
        self,
        tmp_req: main_models.CreateStandardWordRootRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateStandardWordRootResponse:
        tmp_req.validate()
        request = main_models.CreateStandardWordRootShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_command):
            request.create_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateStandardWordRoot',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateStandardWordRootResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_standard_word_root(
        self,
        request: main_models.CreateStandardWordRootRequest,
    ) -> main_models.CreateStandardWordRootResponse:
        runtime = RuntimeOptions()
        return self.create_standard_word_root_with_options(request, runtime)

    async def create_standard_word_root_async(
        self,
        request: main_models.CreateStandardWordRootRequest,
    ) -> main_models.CreateStandardWordRootResponse:
        runtime = RuntimeOptions()
        return await self.create_standard_word_root_with_options_async(request, runtime)

    def create_stream_batch_job_mapping_with_options(
        self,
        tmp_req: main_models.CreateStreamBatchJobMappingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateStreamBatchJobMappingResponse:
        tmp_req.validate()
        request = main_models.CreateStreamBatchJobMappingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.stream_batch_job_mapping_create_command):
            request.stream_batch_job_mapping_create_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.stream_batch_job_mapping_create_command, 'StreamBatchJobMappingCreateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.stream_batch_job_mapping_create_command_shrink):
            body['StreamBatchJobMappingCreateCommand'] = request.stream_batch_job_mapping_create_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateStreamBatchJobMapping',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateStreamBatchJobMappingResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_stream_batch_job_mapping_with_options_async(
        self,
        tmp_req: main_models.CreateStreamBatchJobMappingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateStreamBatchJobMappingResponse:
        tmp_req.validate()
        request = main_models.CreateStreamBatchJobMappingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.stream_batch_job_mapping_create_command):
            request.stream_batch_job_mapping_create_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.stream_batch_job_mapping_create_command, 'StreamBatchJobMappingCreateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.stream_batch_job_mapping_create_command_shrink):
            body['StreamBatchJobMappingCreateCommand'] = request.stream_batch_job_mapping_create_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateStreamBatchJobMapping',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateStreamBatchJobMappingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_stream_batch_job_mapping(
        self,
        request: main_models.CreateStreamBatchJobMappingRequest,
    ) -> main_models.CreateStreamBatchJobMappingResponse:
        runtime = RuntimeOptions()
        return self.create_stream_batch_job_mapping_with_options(request, runtime)

    async def create_stream_batch_job_mapping_async(
        self,
        request: main_models.CreateStreamBatchJobMappingRequest,
    ) -> main_models.CreateStreamBatchJobMappingResponse:
        runtime = RuntimeOptions()
        return await self.create_stream_batch_job_mapping_with_options_async(request, runtime)

    def create_udf_with_options(
        self,
        tmp_req: main_models.CreateUdfRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUdfResponse:
        tmp_req.validate()
        request = main_models.CreateUdfShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_command):
            request.create_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateUdf',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUdfResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_udf_with_options_async(
        self,
        tmp_req: main_models.CreateUdfRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUdfResponse:
        tmp_req.validate()
        request = main_models.CreateUdfShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_command):
            request.create_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateUdf',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUdfResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_udf(
        self,
        request: main_models.CreateUdfRequest,
    ) -> main_models.CreateUdfResponse:
        runtime = RuntimeOptions()
        return self.create_udf_with_options(request, runtime)

    async def create_udf_async(
        self,
        request: main_models.CreateUdfRequest,
    ) -> main_models.CreateUdfResponse:
        runtime = RuntimeOptions()
        return await self.create_udf_with_options_async(request, runtime)

    def create_user_group_with_options(
        self,
        tmp_req: main_models.CreateUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUserGroupResponse:
        tmp_req.validate()
        request = main_models.CreateUserGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_command):
            request.create_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateUserGroup',
            version = '2023-06-30',
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
        tmp_req: main_models.CreateUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUserGroupResponse:
        tmp_req.validate()
        request = main_models.CreateUserGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_command):
            request.create_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateUserGroup',
            version = '2023-06-30',
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

    def delete_ad_hoc_file_with_options(
        self,
        request: main_models.DeleteAdHocFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAdHocFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_id):
            query['FileId'] = request.file_id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAdHocFile',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAdHocFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ad_hoc_file_with_options_async(
        self,
        request: main_models.DeleteAdHocFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAdHocFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_id):
            query['FileId'] = request.file_id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAdHocFile',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAdHocFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ad_hoc_file(
        self,
        request: main_models.DeleteAdHocFileRequest,
    ) -> main_models.DeleteAdHocFileResponse:
        runtime = RuntimeOptions()
        return self.delete_ad_hoc_file_with_options(request, runtime)

    async def delete_ad_hoc_file_async(
        self,
        request: main_models.DeleteAdHocFileRequest,
    ) -> main_models.DeleteAdHocFileResponse:
        runtime = RuntimeOptions()
        return await self.delete_ad_hoc_file_with_options_async(request, runtime)

    def delete_batch_task_with_options(
        self,
        tmp_req: main_models.DeleteBatchTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBatchTaskResponse:
        tmp_req.validate()
        request = main_models.DeleteBatchTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.delete_command):
            request.delete_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.delete_command, 'DeleteCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.delete_command_shrink):
            body['DeleteCommand'] = request.delete_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBatchTask',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBatchTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_batch_task_with_options_async(
        self,
        tmp_req: main_models.DeleteBatchTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBatchTaskResponse:
        tmp_req.validate()
        request = main_models.DeleteBatchTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.delete_command):
            request.delete_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.delete_command, 'DeleteCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.delete_command_shrink):
            body['DeleteCommand'] = request.delete_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBatchTask',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBatchTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_batch_task(
        self,
        request: main_models.DeleteBatchTaskRequest,
    ) -> main_models.DeleteBatchTaskResponse:
        runtime = RuntimeOptions()
        return self.delete_batch_task_with_options(request, runtime)

    async def delete_batch_task_async(
        self,
        request: main_models.DeleteBatchTaskRequest,
    ) -> main_models.DeleteBatchTaskResponse:
        runtime = RuntimeOptions()
        return await self.delete_batch_task_with_options_async(request, runtime)

    def delete_biz_entity_with_options(
        self,
        request: main_models.DeleteBizEntityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBizEntityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_unit_id):
            query['BizUnitId'] = request.biz_unit_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBizEntity',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBizEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_biz_entity_with_options_async(
        self,
        request: main_models.DeleteBizEntityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBizEntityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_unit_id):
            query['BizUnitId'] = request.biz_unit_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBizEntity',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBizEntityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_biz_entity(
        self,
        request: main_models.DeleteBizEntityRequest,
    ) -> main_models.DeleteBizEntityResponse:
        runtime = RuntimeOptions()
        return self.delete_biz_entity_with_options(request, runtime)

    async def delete_biz_entity_async(
        self,
        request: main_models.DeleteBizEntityRequest,
    ) -> main_models.DeleteBizEntityResponse:
        runtime = RuntimeOptions()
        return await self.delete_biz_entity_with_options_async(request, runtime)

    def delete_biz_metric_with_options(
        self,
        tmp_req: main_models.DeleteBizMetricRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBizMetricResponse:
        tmp_req.validate()
        request = main_models.DeleteBizMetricShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.delete_biz_metric_command):
            request.delete_biz_metric_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.delete_biz_metric_command, 'DeleteBizMetricCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.delete_biz_metric_command_shrink):
            body['DeleteBizMetricCommand'] = request.delete_biz_metric_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBizMetric',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBizMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_biz_metric_with_options_async(
        self,
        tmp_req: main_models.DeleteBizMetricRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBizMetricResponse:
        tmp_req.validate()
        request = main_models.DeleteBizMetricShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.delete_biz_metric_command):
            request.delete_biz_metric_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.delete_biz_metric_command, 'DeleteBizMetricCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.delete_biz_metric_command_shrink):
            body['DeleteBizMetricCommand'] = request.delete_biz_metric_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBizMetric',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBizMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_biz_metric(
        self,
        request: main_models.DeleteBizMetricRequest,
    ) -> main_models.DeleteBizMetricResponse:
        runtime = RuntimeOptions()
        return self.delete_biz_metric_with_options(request, runtime)

    async def delete_biz_metric_async(
        self,
        request: main_models.DeleteBizMetricRequest,
    ) -> main_models.DeleteBizMetricResponse:
        runtime = RuntimeOptions()
        return await self.delete_biz_metric_with_options_async(request, runtime)

    def delete_biz_unit_with_options(
        self,
        request: main_models.DeleteBizUnitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBizUnitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBizUnit',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBizUnitResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_biz_unit_with_options_async(
        self,
        request: main_models.DeleteBizUnitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBizUnitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBizUnit',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBizUnitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_biz_unit(
        self,
        request: main_models.DeleteBizUnitRequest,
    ) -> main_models.DeleteBizUnitResponse:
        runtime = RuntimeOptions()
        return self.delete_biz_unit_with_options(request, runtime)

    async def delete_biz_unit_async(
        self,
        request: main_models.DeleteBizUnitRequest,
    ) -> main_models.DeleteBizUnitResponse:
        runtime = RuntimeOptions()
        return await self.delete_biz_unit_with_options_async(request, runtime)

    def delete_compute_source_with_options(
        self,
        request: main_models.DeleteComputeSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteComputeSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteComputeSource',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteComputeSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_compute_source_with_options_async(
        self,
        request: main_models.DeleteComputeSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteComputeSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteComputeSource',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteComputeSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_compute_source(
        self,
        request: main_models.DeleteComputeSourceRequest,
    ) -> main_models.DeleteComputeSourceResponse:
        runtime = RuntimeOptions()
        return self.delete_compute_source_with_options(request, runtime)

    async def delete_compute_source_async(
        self,
        request: main_models.DeleteComputeSourceRequest,
    ) -> main_models.DeleteComputeSourceResponse:
        runtime = RuntimeOptions()
        return await self.delete_compute_source_with_options_async(request, runtime)

    def delete_data_domain_with_options(
        self,
        request: main_models.DeleteDataDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_unit_id):
            query['BizUnitId'] = request.biz_unit_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataDomain',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_domain_with_options_async(
        self,
        request: main_models.DeleteDataDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_unit_id):
            query['BizUnitId'] = request.biz_unit_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataDomain',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_domain(
        self,
        request: main_models.DeleteDataDomainRequest,
    ) -> main_models.DeleteDataDomainResponse:
        runtime = RuntimeOptions()
        return self.delete_data_domain_with_options(request, runtime)

    async def delete_data_domain_async(
        self,
        request: main_models.DeleteDataDomainRequest,
    ) -> main_models.DeleteDataDomainResponse:
        runtime = RuntimeOptions()
        return await self.delete_data_domain_with_options_async(request, runtime)

    def delete_data_source_with_options(
        self,
        tmp_req: main_models.DeleteDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataSourceResponse:
        tmp_req.validate()
        request = main_models.DeleteDataSourceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.delete_command):
            request.delete_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.delete_command, 'DeleteCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.delete_command_shrink):
            body['DeleteCommand'] = request.delete_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataSource',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_source_with_options_async(
        self,
        tmp_req: main_models.DeleteDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataSourceResponse:
        tmp_req.validate()
        request = main_models.DeleteDataSourceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.delete_command):
            request.delete_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.delete_command, 'DeleteCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.delete_command_shrink):
            body['DeleteCommand'] = request.delete_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataSource',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_source(
        self,
        request: main_models.DeleteDataSourceRequest,
    ) -> main_models.DeleteDataSourceResponse:
        runtime = RuntimeOptions()
        return self.delete_data_source_with_options(request, runtime)

    async def delete_data_source_async(
        self,
        request: main_models.DeleteDataSourceRequest,
    ) -> main_models.DeleteDataSourceResponse:
        runtime = RuntimeOptions()
        return await self.delete_data_source_with_options_async(request, runtime)

    def delete_directory_with_options(
        self,
        request: main_models.DeleteDirectoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDirectoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_id):
            query['FileId'] = request.file_id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDirectory',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_directory_with_options_async(
        self,
        request: main_models.DeleteDirectoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDirectoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_id):
            query['FileId'] = request.file_id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDirectory',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_directory(
        self,
        request: main_models.DeleteDirectoryRequest,
    ) -> main_models.DeleteDirectoryResponse:
        runtime = RuntimeOptions()
        return self.delete_directory_with_options(request, runtime)

    async def delete_directory_async(
        self,
        request: main_models.DeleteDirectoryRequest,
    ) -> main_models.DeleteDirectoryResponse:
        runtime = RuntimeOptions()
        return await self.delete_directory_with_options_async(request, runtime)

    def delete_quality_rules_with_options(
        self,
        tmp_req: main_models.DeleteQualityRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteQualityRulesResponse:
        tmp_req.validate()
        request = main_models.DeleteQualityRulesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.delete_command):
            request.delete_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.delete_command, 'DeleteCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.delete_command_shrink):
            body['DeleteCommand'] = request.delete_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteQualityRules',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteQualityRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_quality_rules_with_options_async(
        self,
        tmp_req: main_models.DeleteQualityRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteQualityRulesResponse:
        tmp_req.validate()
        request = main_models.DeleteQualityRulesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.delete_command):
            request.delete_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.delete_command, 'DeleteCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.delete_command_shrink):
            body['DeleteCommand'] = request.delete_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteQualityRules',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteQualityRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_quality_rules(
        self,
        request: main_models.DeleteQualityRulesRequest,
    ) -> main_models.DeleteQualityRulesResponse:
        runtime = RuntimeOptions()
        return self.delete_quality_rules_with_options(request, runtime)

    async def delete_quality_rules_async(
        self,
        request: main_models.DeleteQualityRulesRequest,
    ) -> main_models.DeleteQualityRulesResponse:
        runtime = RuntimeOptions()
        return await self.delete_quality_rules_with_options_async(request, runtime)

    def delete_quality_schedules_with_options(
        self,
        tmp_req: main_models.DeleteQualitySchedulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteQualitySchedulesResponse:
        tmp_req.validate()
        request = main_models.DeleteQualitySchedulesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.delete_command):
            request.delete_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.delete_command, 'DeleteCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.delete_command_shrink):
            body['DeleteCommand'] = request.delete_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteQualitySchedules',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteQualitySchedulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_quality_schedules_with_options_async(
        self,
        tmp_req: main_models.DeleteQualitySchedulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteQualitySchedulesResponse:
        tmp_req.validate()
        request = main_models.DeleteQualitySchedulesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.delete_command):
            request.delete_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.delete_command, 'DeleteCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.delete_command_shrink):
            body['DeleteCommand'] = request.delete_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteQualitySchedules',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteQualitySchedulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_quality_schedules(
        self,
        request: main_models.DeleteQualitySchedulesRequest,
    ) -> main_models.DeleteQualitySchedulesResponse:
        runtime = RuntimeOptions()
        return self.delete_quality_schedules_with_options(request, runtime)

    async def delete_quality_schedules_async(
        self,
        request: main_models.DeleteQualitySchedulesRequest,
    ) -> main_models.DeleteQualitySchedulesResponse:
        runtime = RuntimeOptions()
        return await self.delete_quality_schedules_with_options_async(request, runtime)

    def delete_quality_templates_with_options(
        self,
        tmp_req: main_models.DeleteQualityTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteQualityTemplatesResponse:
        tmp_req.validate()
        request = main_models.DeleteQualityTemplatesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.delete_command):
            request.delete_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.delete_command, 'DeleteCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.delete_command_shrink):
            body['DeleteCommand'] = request.delete_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteQualityTemplates',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteQualityTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_quality_templates_with_options_async(
        self,
        tmp_req: main_models.DeleteQualityTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteQualityTemplatesResponse:
        tmp_req.validate()
        request = main_models.DeleteQualityTemplatesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.delete_command):
            request.delete_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.delete_command, 'DeleteCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.delete_command_shrink):
            body['DeleteCommand'] = request.delete_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteQualityTemplates',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteQualityTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_quality_templates(
        self,
        request: main_models.DeleteQualityTemplatesRequest,
    ) -> main_models.DeleteQualityTemplatesResponse:
        runtime = RuntimeOptions()
        return self.delete_quality_templates_with_options(request, runtime)

    async def delete_quality_templates_async(
        self,
        request: main_models.DeleteQualityTemplatesRequest,
    ) -> main_models.DeleteQualityTemplatesResponse:
        runtime = RuntimeOptions()
        return await self.delete_quality_templates_with_options_async(request, runtime)

    def delete_quality_watches_with_options(
        self,
        tmp_req: main_models.DeleteQualityWatchesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteQualityWatchesResponse:
        tmp_req.validate()
        request = main_models.DeleteQualityWatchesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.delete_command):
            request.delete_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.delete_command, 'DeleteCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.delete_command_shrink):
            body['DeleteCommand'] = request.delete_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteQualityWatches',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteQualityWatchesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_quality_watches_with_options_async(
        self,
        tmp_req: main_models.DeleteQualityWatchesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteQualityWatchesResponse:
        tmp_req.validate()
        request = main_models.DeleteQualityWatchesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.delete_command):
            request.delete_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.delete_command, 'DeleteCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.delete_command_shrink):
            body['DeleteCommand'] = request.delete_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteQualityWatches',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteQualityWatchesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_quality_watches(
        self,
        request: main_models.DeleteQualityWatchesRequest,
    ) -> main_models.DeleteQualityWatchesResponse:
        runtime = RuntimeOptions()
        return self.delete_quality_watches_with_options(request, runtime)

    async def delete_quality_watches_async(
        self,
        request: main_models.DeleteQualityWatchesRequest,
    ) -> main_models.DeleteQualityWatchesResponse:
        runtime = RuntimeOptions()
        return await self.delete_quality_watches_with_options_async(request, runtime)

    def delete_register_lineage_with_options(
        self,
        tmp_req: main_models.DeleteRegisterLineageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRegisterLineageResponse:
        tmp_req.validate()
        request = main_models.DeleteRegisterLineageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.delete_register_lineage_command):
            request.delete_register_lineage_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.delete_register_lineage_command, 'DeleteRegisterLineageCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.delete_register_lineage_command_shrink):
            body['DeleteRegisterLineageCommand'] = request.delete_register_lineage_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRegisterLineage',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRegisterLineageResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_register_lineage_with_options_async(
        self,
        tmp_req: main_models.DeleteRegisterLineageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRegisterLineageResponse:
        tmp_req.validate()
        request = main_models.DeleteRegisterLineageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.delete_register_lineage_command):
            request.delete_register_lineage_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.delete_register_lineage_command, 'DeleteRegisterLineageCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.delete_register_lineage_command_shrink):
            body['DeleteRegisterLineageCommand'] = request.delete_register_lineage_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRegisterLineage',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRegisterLineageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_register_lineage(
        self,
        request: main_models.DeleteRegisterLineageRequest,
    ) -> main_models.DeleteRegisterLineageResponse:
        runtime = RuntimeOptions()
        return self.delete_register_lineage_with_options(request, runtime)

    async def delete_register_lineage_async(
        self,
        request: main_models.DeleteRegisterLineageRequest,
    ) -> main_models.DeleteRegisterLineageResponse:
        runtime = RuntimeOptions()
        return await self.delete_register_lineage_with_options_async(request, runtime)

    def delete_resource_with_options(
        self,
        request: main_models.DeleteResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteResource',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_resource_with_options_async(
        self,
        request: main_models.DeleteResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteResource',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_resource(
        self,
        request: main_models.DeleteResourceRequest,
    ) -> main_models.DeleteResourceResponse:
        runtime = RuntimeOptions()
        return self.delete_resource_with_options(request, runtime)

    async def delete_resource_async(
        self,
        request: main_models.DeleteResourceRequest,
    ) -> main_models.DeleteResourceResponse:
        runtime = RuntimeOptions()
        return await self.delete_resource_with_options_async(request, runtime)

    def delete_row_permission_with_options(
        self,
        tmp_req: main_models.DeleteRowPermissionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRowPermissionResponse:
        tmp_req.validate()
        request = main_models.DeleteRowPermissionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.delete_row_permission_command):
            request.delete_row_permission_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.delete_row_permission_command, 'DeleteRowPermissionCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.delete_row_permission_command_shrink):
            body['DeleteRowPermissionCommand'] = request.delete_row_permission_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRowPermission',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRowPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_row_permission_with_options_async(
        self,
        tmp_req: main_models.DeleteRowPermissionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRowPermissionResponse:
        tmp_req.validate()
        request = main_models.DeleteRowPermissionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.delete_row_permission_command):
            request.delete_row_permission_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.delete_row_permission_command, 'DeleteRowPermissionCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.delete_row_permission_command_shrink):
            body['DeleteRowPermissionCommand'] = request.delete_row_permission_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRowPermission',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRowPermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_row_permission(
        self,
        request: main_models.DeleteRowPermissionRequest,
    ) -> main_models.DeleteRowPermissionResponse:
        runtime = RuntimeOptions()
        return self.delete_row_permission_with_options(request, runtime)

    async def delete_row_permission_async(
        self,
        request: main_models.DeleteRowPermissionRequest,
    ) -> main_models.DeleteRowPermissionResponse:
        runtime = RuntimeOptions()
        return await self.delete_row_permission_with_options_async(request, runtime)

    def delete_security_classify_with_options(
        self,
        tmp_req: main_models.DeleteSecurityClassifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSecurityClassifyResponse:
        tmp_req.validate()
        request = main_models.DeleteSecurityClassifyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.delete_command):
            request.delete_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.delete_command, 'DeleteCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.delete_command_shrink):
            body['DeleteCommand'] = request.delete_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSecurityClassify',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSecurityClassifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_security_classify_with_options_async(
        self,
        tmp_req: main_models.DeleteSecurityClassifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSecurityClassifyResponse:
        tmp_req.validate()
        request = main_models.DeleteSecurityClassifyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.delete_command):
            request.delete_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.delete_command, 'DeleteCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.delete_command_shrink):
            body['DeleteCommand'] = request.delete_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSecurityClassify',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSecurityClassifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_security_classify(
        self,
        request: main_models.DeleteSecurityClassifyRequest,
    ) -> main_models.DeleteSecurityClassifyResponse:
        runtime = RuntimeOptions()
        return self.delete_security_classify_with_options(request, runtime)

    async def delete_security_classify_async(
        self,
        request: main_models.DeleteSecurityClassifyRequest,
    ) -> main_models.DeleteSecurityClassifyResponse:
        runtime = RuntimeOptions()
        return await self.delete_security_classify_with_options_async(request, runtime)

    def delete_security_classify_catalog_with_options(
        self,
        tmp_req: main_models.DeleteSecurityClassifyCatalogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSecurityClassifyCatalogResponse:
        tmp_req.validate()
        request = main_models.DeleteSecurityClassifyCatalogShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.delete_command):
            request.delete_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.delete_command, 'DeleteCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.delete_command_shrink):
            body['DeleteCommand'] = request.delete_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSecurityClassifyCatalog',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSecurityClassifyCatalogResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_security_classify_catalog_with_options_async(
        self,
        tmp_req: main_models.DeleteSecurityClassifyCatalogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSecurityClassifyCatalogResponse:
        tmp_req.validate()
        request = main_models.DeleteSecurityClassifyCatalogShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.delete_command):
            request.delete_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.delete_command, 'DeleteCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.delete_command_shrink):
            body['DeleteCommand'] = request.delete_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSecurityClassifyCatalog',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSecurityClassifyCatalogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_security_classify_catalog(
        self,
        request: main_models.DeleteSecurityClassifyCatalogRequest,
    ) -> main_models.DeleteSecurityClassifyCatalogResponse:
        runtime = RuntimeOptions()
        return self.delete_security_classify_catalog_with_options(request, runtime)

    async def delete_security_classify_catalog_async(
        self,
        request: main_models.DeleteSecurityClassifyCatalogRequest,
    ) -> main_models.DeleteSecurityClassifyCatalogResponse:
        runtime = RuntimeOptions()
        return await self.delete_security_classify_catalog_with_options_async(request, runtime)

    def delete_security_identify_results_with_options(
        self,
        tmp_req: main_models.DeleteSecurityIdentifyResultsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSecurityIdentifyResultsResponse:
        tmp_req.validate()
        request = main_models.DeleteSecurityIdentifyResultsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.delete_command):
            request.delete_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.delete_command, 'DeleteCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.delete_command_shrink):
            body['DeleteCommand'] = request.delete_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSecurityIdentifyResults',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSecurityIdentifyResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_security_identify_results_with_options_async(
        self,
        tmp_req: main_models.DeleteSecurityIdentifyResultsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSecurityIdentifyResultsResponse:
        tmp_req.validate()
        request = main_models.DeleteSecurityIdentifyResultsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.delete_command):
            request.delete_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.delete_command, 'DeleteCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.delete_command_shrink):
            body['DeleteCommand'] = request.delete_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSecurityIdentifyResults',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSecurityIdentifyResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_security_identify_results(
        self,
        request: main_models.DeleteSecurityIdentifyResultsRequest,
    ) -> main_models.DeleteSecurityIdentifyResultsResponse:
        runtime = RuntimeOptions()
        return self.delete_security_identify_results_with_options(request, runtime)

    async def delete_security_identify_results_async(
        self,
        request: main_models.DeleteSecurityIdentifyResultsRequest,
    ) -> main_models.DeleteSecurityIdentifyResultsResponse:
        runtime = RuntimeOptions()
        return await self.delete_security_identify_results_with_options_async(request, runtime)

    def delete_security_level_with_options(
        self,
        tmp_req: main_models.DeleteSecurityLevelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSecurityLevelResponse:
        tmp_req.validate()
        request = main_models.DeleteSecurityLevelShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.delete_command):
            request.delete_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.delete_command, 'DeleteCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.delete_command_shrink):
            body['DeleteCommand'] = request.delete_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSecurityLevel',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSecurityLevelResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_security_level_with_options_async(
        self,
        tmp_req: main_models.DeleteSecurityLevelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSecurityLevelResponse:
        tmp_req.validate()
        request = main_models.DeleteSecurityLevelShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.delete_command):
            request.delete_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.delete_command, 'DeleteCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.delete_command_shrink):
            body['DeleteCommand'] = request.delete_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSecurityLevel',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSecurityLevelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_security_level(
        self,
        request: main_models.DeleteSecurityLevelRequest,
    ) -> main_models.DeleteSecurityLevelResponse:
        runtime = RuntimeOptions()
        return self.delete_security_level_with_options(request, runtime)

    async def delete_security_level_async(
        self,
        request: main_models.DeleteSecurityLevelRequest,
    ) -> main_models.DeleteSecurityLevelResponse:
        runtime = RuntimeOptions()
        return await self.delete_security_level_with_options_async(request, runtime)

    def delete_standard_with_options(
        self,
        tmp_req: main_models.DeleteStandardRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteStandardResponse:
        tmp_req.validate()
        request = main_models.DeleteStandardShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.delete_command):
            request.delete_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.delete_command, 'DeleteCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.delete_command_shrink):
            body['DeleteCommand'] = request.delete_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteStandard',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteStandardResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_standard_with_options_async(
        self,
        tmp_req: main_models.DeleteStandardRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteStandardResponse:
        tmp_req.validate()
        request = main_models.DeleteStandardShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.delete_command):
            request.delete_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.delete_command, 'DeleteCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.delete_command_shrink):
            body['DeleteCommand'] = request.delete_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteStandard',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteStandardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_standard(
        self,
        request: main_models.DeleteStandardRequest,
    ) -> main_models.DeleteStandardResponse:
        runtime = RuntimeOptions()
        return self.delete_standard_with_options(request, runtime)

    async def delete_standard_async(
        self,
        request: main_models.DeleteStandardRequest,
    ) -> main_models.DeleteStandardResponse:
        runtime = RuntimeOptions()
        return await self.delete_standard_with_options_async(request, runtime)

    def delete_standard_in_valid_mapping_with_options(
        self,
        tmp_req: main_models.DeleteStandardInValidMappingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteStandardInValidMappingResponse:
        tmp_req.validate()
        request = main_models.DeleteStandardInValidMappingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.delete_command):
            request.delete_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.delete_command, 'DeleteCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.delete_command_shrink):
            body['DeleteCommand'] = request.delete_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteStandardInValidMapping',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteStandardInValidMappingResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_standard_in_valid_mapping_with_options_async(
        self,
        tmp_req: main_models.DeleteStandardInValidMappingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteStandardInValidMappingResponse:
        tmp_req.validate()
        request = main_models.DeleteStandardInValidMappingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.delete_command):
            request.delete_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.delete_command, 'DeleteCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.delete_command_shrink):
            body['DeleteCommand'] = request.delete_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteStandardInValidMapping',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteStandardInValidMappingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_standard_in_valid_mapping(
        self,
        request: main_models.DeleteStandardInValidMappingRequest,
    ) -> main_models.DeleteStandardInValidMappingResponse:
        runtime = RuntimeOptions()
        return self.delete_standard_in_valid_mapping_with_options(request, runtime)

    async def delete_standard_in_valid_mapping_async(
        self,
        request: main_models.DeleteStandardInValidMappingRequest,
    ) -> main_models.DeleteStandardInValidMappingResponse:
        runtime = RuntimeOptions()
        return await self.delete_standard_in_valid_mapping_with_options_async(request, runtime)

    def delete_standard_lookup_table_with_options(
        self,
        request: main_models.DeleteStandardLookupTableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteStandardLookupTableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteStandardLookupTable',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteStandardLookupTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_standard_lookup_table_with_options_async(
        self,
        request: main_models.DeleteStandardLookupTableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteStandardLookupTableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteStandardLookupTable',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteStandardLookupTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_standard_lookup_table(
        self,
        request: main_models.DeleteStandardLookupTableRequest,
    ) -> main_models.DeleteStandardLookupTableResponse:
        runtime = RuntimeOptions()
        return self.delete_standard_lookup_table_with_options(request, runtime)

    async def delete_standard_lookup_table_async(
        self,
        request: main_models.DeleteStandardLookupTableRequest,
    ) -> main_models.DeleteStandardLookupTableResponse:
        runtime = RuntimeOptions()
        return await self.delete_standard_lookup_table_with_options_async(request, runtime)

    def delete_standard_relations_with_options(
        self,
        tmp_req: main_models.DeleteStandardRelationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteStandardRelationsResponse:
        tmp_req.validate()
        request = main_models.DeleteStandardRelationsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.delete_command):
            request.delete_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.delete_command, 'DeleteCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.delete_command_shrink):
            body['DeleteCommand'] = request.delete_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteStandardRelations',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteStandardRelationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_standard_relations_with_options_async(
        self,
        tmp_req: main_models.DeleteStandardRelationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteStandardRelationsResponse:
        tmp_req.validate()
        request = main_models.DeleteStandardRelationsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.delete_command):
            request.delete_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.delete_command, 'DeleteCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.delete_command_shrink):
            body['DeleteCommand'] = request.delete_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteStandardRelations',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteStandardRelationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_standard_relations(
        self,
        request: main_models.DeleteStandardRelationsRequest,
    ) -> main_models.DeleteStandardRelationsResponse:
        runtime = RuntimeOptions()
        return self.delete_standard_relations_with_options(request, runtime)

    async def delete_standard_relations_async(
        self,
        request: main_models.DeleteStandardRelationsRequest,
    ) -> main_models.DeleteStandardRelationsResponse:
        runtime = RuntimeOptions()
        return await self.delete_standard_relations_with_options_async(request, runtime)

    def delete_standard_set_with_options(
        self,
        request: main_models.DeleteStandardSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteStandardSetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteStandardSet',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteStandardSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_standard_set_with_options_async(
        self,
        request: main_models.DeleteStandardSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteStandardSetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteStandardSet',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteStandardSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_standard_set(
        self,
        request: main_models.DeleteStandardSetRequest,
    ) -> main_models.DeleteStandardSetResponse:
        runtime = RuntimeOptions()
        return self.delete_standard_set_with_options(request, runtime)

    async def delete_standard_set_async(
        self,
        request: main_models.DeleteStandardSetRequest,
    ) -> main_models.DeleteStandardSetResponse:
        runtime = RuntimeOptions()
        return await self.delete_standard_set_with_options_async(request, runtime)

    def delete_standard_valid_mapping_with_options(
        self,
        tmp_req: main_models.DeleteStandardValidMappingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteStandardValidMappingResponse:
        tmp_req.validate()
        request = main_models.DeleteStandardValidMappingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.delete_command):
            request.delete_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.delete_command, 'DeleteCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.delete_command_shrink):
            body['DeleteCommand'] = request.delete_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteStandardValidMapping',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteStandardValidMappingResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_standard_valid_mapping_with_options_async(
        self,
        tmp_req: main_models.DeleteStandardValidMappingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteStandardValidMappingResponse:
        tmp_req.validate()
        request = main_models.DeleteStandardValidMappingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.delete_command):
            request.delete_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.delete_command, 'DeleteCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.delete_command_shrink):
            body['DeleteCommand'] = request.delete_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteStandardValidMapping',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteStandardValidMappingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_standard_valid_mapping(
        self,
        request: main_models.DeleteStandardValidMappingRequest,
    ) -> main_models.DeleteStandardValidMappingResponse:
        runtime = RuntimeOptions()
        return self.delete_standard_valid_mapping_with_options(request, runtime)

    async def delete_standard_valid_mapping_async(
        self,
        request: main_models.DeleteStandardValidMappingRequest,
    ) -> main_models.DeleteStandardValidMappingResponse:
        runtime = RuntimeOptions()
        return await self.delete_standard_valid_mapping_with_options_async(request, runtime)

    def delete_standard_word_root_with_options(
        self,
        request: main_models.DeleteStandardWordRootRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteStandardWordRootResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteStandardWordRoot',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteStandardWordRootResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_standard_word_root_with_options_async(
        self,
        request: main_models.DeleteStandardWordRootRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteStandardWordRootResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteStandardWordRoot',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteStandardWordRootResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_standard_word_root(
        self,
        request: main_models.DeleteStandardWordRootRequest,
    ) -> main_models.DeleteStandardWordRootResponse:
        runtime = RuntimeOptions()
        return self.delete_standard_word_root_with_options(request, runtime)

    async def delete_standard_word_root_async(
        self,
        request: main_models.DeleteStandardWordRootRequest,
    ) -> main_models.DeleteStandardWordRootResponse:
        runtime = RuntimeOptions()
        return await self.delete_standard_word_root_with_options_async(request, runtime)

    def delete_udf_with_options(
        self,
        request: main_models.DeleteUdfRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUdfResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUdf',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUdfResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_udf_with_options_async(
        self,
        request: main_models.DeleteUdfRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUdfResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUdf',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUdfResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_udf(
        self,
        request: main_models.DeleteUdfRequest,
    ) -> main_models.DeleteUdfResponse:
        runtime = RuntimeOptions()
        return self.delete_udf_with_options(request, runtime)

    async def delete_udf_async(
        self,
        request: main_models.DeleteUdfRequest,
    ) -> main_models.DeleteUdfResponse:
        runtime = RuntimeOptions()
        return await self.delete_udf_with_options_async(request, runtime)

    def delete_user_group_with_options(
        self,
        request: main_models.DeleteUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUserGroup',
            version = '2023-06-30',
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
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUserGroup',
            version = '2023-06-30',
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

    def execute_ad_hoc_task_with_options(
        self,
        tmp_req: main_models.ExecuteAdHocTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteAdHocTaskResponse:
        tmp_req.validate()
        request = main_models.ExecuteAdHocTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.execute_command):
            request.execute_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.execute_command, 'ExecuteCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.execute_command_shrink):
            body['ExecuteCommand'] = request.execute_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteAdHocTask',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteAdHocTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_ad_hoc_task_with_options_async(
        self,
        tmp_req: main_models.ExecuteAdHocTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteAdHocTaskResponse:
        tmp_req.validate()
        request = main_models.ExecuteAdHocTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.execute_command):
            request.execute_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.execute_command, 'ExecuteCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.execute_command_shrink):
            body['ExecuteCommand'] = request.execute_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteAdHocTask',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteAdHocTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_ad_hoc_task(
        self,
        request: main_models.ExecuteAdHocTaskRequest,
    ) -> main_models.ExecuteAdHocTaskResponse:
        runtime = RuntimeOptions()
        return self.execute_ad_hoc_task_with_options(request, runtime)

    async def execute_ad_hoc_task_async(
        self,
        request: main_models.ExecuteAdHocTaskRequest,
    ) -> main_models.ExecuteAdHocTaskResponse:
        runtime = RuntimeOptions()
        return await self.execute_ad_hoc_task_with_options_async(request, runtime)

    def execute_manual_node_with_options(
        self,
        tmp_req: main_models.ExecuteManualNodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteManualNodeResponse:
        tmp_req.validate()
        request = main_models.ExecuteManualNodeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.execute_command):
            request.execute_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.execute_command, 'ExecuteCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.execute_command_shrink):
            body['ExecuteCommand'] = request.execute_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteManualNode',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteManualNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_manual_node_with_options_async(
        self,
        tmp_req: main_models.ExecuteManualNodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteManualNodeResponse:
        tmp_req.validate()
        request = main_models.ExecuteManualNodeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.execute_command):
            request.execute_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.execute_command, 'ExecuteCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.execute_command_shrink):
            body['ExecuteCommand'] = request.execute_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteManualNode',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteManualNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_manual_node(
        self,
        request: main_models.ExecuteManualNodeRequest,
    ) -> main_models.ExecuteManualNodeResponse:
        runtime = RuntimeOptions()
        return self.execute_manual_node_with_options(request, runtime)

    async def execute_manual_node_async(
        self,
        request: main_models.ExecuteManualNodeRequest,
    ) -> main_models.ExecuteManualNodeResponse:
        runtime = RuntimeOptions()
        return await self.execute_manual_node_with_options_async(request, runtime)

    def execute_trigger_node_with_options(
        self,
        request: main_models.ExecuteTriggerNodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteTriggerNodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_date):
            query['BizDate'] = request.biz_date
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.index):
            query['Index'] = request.index
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteTriggerNode',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteTriggerNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_trigger_node_with_options_async(
        self,
        request: main_models.ExecuteTriggerNodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteTriggerNodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_date):
            query['BizDate'] = request.biz_date
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.index):
            query['Index'] = request.index
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteTriggerNode',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteTriggerNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_trigger_node(
        self,
        request: main_models.ExecuteTriggerNodeRequest,
    ) -> main_models.ExecuteTriggerNodeResponse:
        runtime = RuntimeOptions()
        return self.execute_trigger_node_with_options(request, runtime)

    async def execute_trigger_node_async(
        self,
        request: main_models.ExecuteTriggerNodeRequest,
    ) -> main_models.ExecuteTriggerNodeResponse:
        runtime = RuntimeOptions()
        return await self.execute_trigger_node_with_options_async(request, runtime)

    def fix_data_with_options(
        self,
        tmp_req: main_models.FixDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FixDataResponse:
        tmp_req.validate()
        request = main_models.FixDataShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.fix_data_command):
            request.fix_data_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.fix_data_command, 'FixDataCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.fix_data_command_shrink):
            body['FixDataCommand'] = request.fix_data_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'FixData',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FixDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def fix_data_with_options_async(
        self,
        tmp_req: main_models.FixDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FixDataResponse:
        tmp_req.validate()
        request = main_models.FixDataShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.fix_data_command):
            request.fix_data_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.fix_data_command, 'FixDataCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.fix_data_command_shrink):
            body['FixDataCommand'] = request.fix_data_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'FixData',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FixDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def fix_data(
        self,
        request: main_models.FixDataRequest,
    ) -> main_models.FixDataResponse:
        runtime = RuntimeOptions()
        return self.fix_data_with_options(request, runtime)

    async def fix_data_async(
        self,
        request: main_models.FixDataRequest,
    ) -> main_models.FixDataResponse:
        runtime = RuntimeOptions()
        return await self.fix_data_with_options_async(request, runtime)

    def get_account_by_row_permission_id_with_options(
        self,
        tmp_req: main_models.GetAccountByRowPermissionIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAccountByRowPermissionIdResponse:
        tmp_req.validate()
        request = main_models.GetAccountByRowPermissionIdShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.get_account_by_row_permission_id_query):
            request.get_account_by_row_permission_id_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.get_account_by_row_permission_id_query, 'GetAccountByRowPermissionIdQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.get_account_by_row_permission_id_query_shrink):
            body['GetAccountByRowPermissionIdQuery'] = request.get_account_by_row_permission_id_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetAccountByRowPermissionId',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAccountByRowPermissionIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_account_by_row_permission_id_with_options_async(
        self,
        tmp_req: main_models.GetAccountByRowPermissionIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAccountByRowPermissionIdResponse:
        tmp_req.validate()
        request = main_models.GetAccountByRowPermissionIdShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.get_account_by_row_permission_id_query):
            request.get_account_by_row_permission_id_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.get_account_by_row_permission_id_query, 'GetAccountByRowPermissionIdQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.get_account_by_row_permission_id_query_shrink):
            body['GetAccountByRowPermissionIdQuery'] = request.get_account_by_row_permission_id_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetAccountByRowPermissionId',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAccountByRowPermissionIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_account_by_row_permission_id(
        self,
        request: main_models.GetAccountByRowPermissionIdRequest,
    ) -> main_models.GetAccountByRowPermissionIdResponse:
        runtime = RuntimeOptions()
        return self.get_account_by_row_permission_id_with_options(request, runtime)

    async def get_account_by_row_permission_id_async(
        self,
        request: main_models.GetAccountByRowPermissionIdRequest,
    ) -> main_models.GetAccountByRowPermissionIdResponse:
        runtime = RuntimeOptions()
        return await self.get_account_by_row_permission_id_with_options_async(request, runtime)

    def get_ad_hoc_file_with_options(
        self,
        request: main_models.GetAdHocFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAdHocFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_id):
            query['FileId'] = request.file_id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAdHocFile',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAdHocFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ad_hoc_file_with_options_async(
        self,
        request: main_models.GetAdHocFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAdHocFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_id):
            query['FileId'] = request.file_id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAdHocFile',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAdHocFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ad_hoc_file(
        self,
        request: main_models.GetAdHocFileRequest,
    ) -> main_models.GetAdHocFileResponse:
        runtime = RuntimeOptions()
        return self.get_ad_hoc_file_with_options(request, runtime)

    async def get_ad_hoc_file_async(
        self,
        request: main_models.GetAdHocFileRequest,
    ) -> main_models.GetAdHocFileResponse:
        runtime = RuntimeOptions()
        return await self.get_ad_hoc_file_with_options_async(request, runtime)

    def get_ad_hoc_task_log_with_options(
        self,
        request: main_models.GetAdHocTaskLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAdHocTaskLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.offset):
            query['Offset'] = request.offset
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.sub_task_id):
            query['SubTaskId'] = request.sub_task_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAdHocTaskLog',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAdHocTaskLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ad_hoc_task_log_with_options_async(
        self,
        request: main_models.GetAdHocTaskLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAdHocTaskLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.offset):
            query['Offset'] = request.offset
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.sub_task_id):
            query['SubTaskId'] = request.sub_task_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAdHocTaskLog',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAdHocTaskLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ad_hoc_task_log(
        self,
        request: main_models.GetAdHocTaskLogRequest,
    ) -> main_models.GetAdHocTaskLogResponse:
        runtime = RuntimeOptions()
        return self.get_ad_hoc_task_log_with_options(request, runtime)

    async def get_ad_hoc_task_log_async(
        self,
        request: main_models.GetAdHocTaskLogRequest,
    ) -> main_models.GetAdHocTaskLogResponse:
        runtime = RuntimeOptions()
        return await self.get_ad_hoc_task_log_with_options_async(request, runtime)

    def get_ad_hoc_task_result_with_options(
        self,
        request: main_models.GetAdHocTaskResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAdHocTaskResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.sub_task_id):
            query['SubTaskId'] = request.sub_task_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAdHocTaskResult',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAdHocTaskResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ad_hoc_task_result_with_options_async(
        self,
        request: main_models.GetAdHocTaskResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAdHocTaskResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.sub_task_id):
            query['SubTaskId'] = request.sub_task_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAdHocTaskResult',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAdHocTaskResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ad_hoc_task_result(
        self,
        request: main_models.GetAdHocTaskResultRequest,
    ) -> main_models.GetAdHocTaskResultResponse:
        runtime = RuntimeOptions()
        return self.get_ad_hoc_task_result_with_options(request, runtime)

    async def get_ad_hoc_task_result_async(
        self,
        request: main_models.GetAdHocTaskResultRequest,
    ) -> main_models.GetAdHocTaskResultResponse:
        runtime = RuntimeOptions()
        return await self.get_ad_hoc_task_result_with_options_async(request, runtime)

    def get_alert_event_with_options(
        self,
        request: main_models.GetAlertEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAlertEventResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAlertEvent',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAlertEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_alert_event_with_options_async(
        self,
        request: main_models.GetAlertEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAlertEventResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAlertEvent',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAlertEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_alert_event(
        self,
        request: main_models.GetAlertEventRequest,
    ) -> main_models.GetAlertEventResponse:
        runtime = RuntimeOptions()
        return self.get_alert_event_with_options(request, runtime)

    async def get_alert_event_async(
        self,
        request: main_models.GetAlertEventRequest,
    ) -> main_models.GetAlertEventResponse:
        runtime = RuntimeOptions()
        return await self.get_alert_event_with_options_async(request, runtime)

    def get_asset_mapping_relations_with_options(
        self,
        tmp_req: main_models.GetAssetMappingRelationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAssetMappingRelationsResponse:
        tmp_req.validate()
        request = main_models.GetAssetMappingRelationsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.asset_mapping_query):
            request.asset_mapping_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.asset_mapping_query, 'AssetMappingQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.asset_mapping_query_shrink):
            body['AssetMappingQuery'] = request.asset_mapping_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetAssetMappingRelations',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAssetMappingRelationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_asset_mapping_relations_with_options_async(
        self,
        tmp_req: main_models.GetAssetMappingRelationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAssetMappingRelationsResponse:
        tmp_req.validate()
        request = main_models.GetAssetMappingRelationsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.asset_mapping_query):
            request.asset_mapping_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.asset_mapping_query, 'AssetMappingQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.asset_mapping_query_shrink):
            body['AssetMappingQuery'] = request.asset_mapping_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetAssetMappingRelations',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAssetMappingRelationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_asset_mapping_relations(
        self,
        request: main_models.GetAssetMappingRelationsRequest,
    ) -> main_models.GetAssetMappingRelationsResponse:
        runtime = RuntimeOptions()
        return self.get_asset_mapping_relations_with_options(request, runtime)

    async def get_asset_mapping_relations_async(
        self,
        request: main_models.GetAssetMappingRelationsRequest,
    ) -> main_models.GetAssetMappingRelationsResponse:
        runtime = RuntimeOptions()
        return await self.get_asset_mapping_relations_with_options_async(request, runtime)

    def get_batch_task_info_with_options(
        self,
        request: main_models.GetBatchTaskInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBatchTaskInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.file_id):
            query['FileId'] = request.file_id
        if not DaraCore.is_null(request.include_all_up_streams):
            query['IncludeAllUpStreams'] = request.include_all_up_streams
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBatchTaskInfo',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBatchTaskInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_batch_task_info_with_options_async(
        self,
        request: main_models.GetBatchTaskInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBatchTaskInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.file_id):
            query['FileId'] = request.file_id
        if not DaraCore.is_null(request.include_all_up_streams):
            query['IncludeAllUpStreams'] = request.include_all_up_streams
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBatchTaskInfo',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBatchTaskInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_batch_task_info(
        self,
        request: main_models.GetBatchTaskInfoRequest,
    ) -> main_models.GetBatchTaskInfoResponse:
        runtime = RuntimeOptions()
        return self.get_batch_task_info_with_options(request, runtime)

    async def get_batch_task_info_async(
        self,
        request: main_models.GetBatchTaskInfoRequest,
    ) -> main_models.GetBatchTaskInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_batch_task_info_with_options_async(request, runtime)

    def get_batch_task_info_by_version_with_options(
        self,
        request: main_models.GetBatchTaskInfoByVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBatchTaskInfoByVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_id):
            query['FileId'] = request.file_id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBatchTaskInfoByVersion',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBatchTaskInfoByVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_batch_task_info_by_version_with_options_async(
        self,
        request: main_models.GetBatchTaskInfoByVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBatchTaskInfoByVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_id):
            query['FileId'] = request.file_id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBatchTaskInfoByVersion',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBatchTaskInfoByVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_batch_task_info_by_version(
        self,
        request: main_models.GetBatchTaskInfoByVersionRequest,
    ) -> main_models.GetBatchTaskInfoByVersionResponse:
        runtime = RuntimeOptions()
        return self.get_batch_task_info_by_version_with_options(request, runtime)

    async def get_batch_task_info_by_version_async(
        self,
        request: main_models.GetBatchTaskInfoByVersionRequest,
    ) -> main_models.GetBatchTaskInfoByVersionResponse:
        runtime = RuntimeOptions()
        return await self.get_batch_task_info_by_version_with_options_async(request, runtime)

    def get_batch_task_udf_lineages_with_options(
        self,
        request: main_models.GetBatchTaskUdfLineagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBatchTaskUdfLineagesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_id):
            query['FileId'] = request.file_id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBatchTaskUdfLineages',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBatchTaskUdfLineagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_batch_task_udf_lineages_with_options_async(
        self,
        request: main_models.GetBatchTaskUdfLineagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBatchTaskUdfLineagesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_id):
            query['FileId'] = request.file_id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBatchTaskUdfLineages',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBatchTaskUdfLineagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_batch_task_udf_lineages(
        self,
        request: main_models.GetBatchTaskUdfLineagesRequest,
    ) -> main_models.GetBatchTaskUdfLineagesResponse:
        runtime = RuntimeOptions()
        return self.get_batch_task_udf_lineages_with_options(request, runtime)

    async def get_batch_task_udf_lineages_async(
        self,
        request: main_models.GetBatchTaskUdfLineagesRequest,
    ) -> main_models.GetBatchTaskUdfLineagesResponse:
        runtime = RuntimeOptions()
        return await self.get_batch_task_udf_lineages_with_options_async(request, runtime)

    def get_batch_task_versions_with_options(
        self,
        request: main_models.GetBatchTaskVersionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBatchTaskVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_id):
            query['FileId'] = request.file_id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBatchTaskVersions',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBatchTaskVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_batch_task_versions_with_options_async(
        self,
        request: main_models.GetBatchTaskVersionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBatchTaskVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_id):
            query['FileId'] = request.file_id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBatchTaskVersions',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBatchTaskVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_batch_task_versions(
        self,
        request: main_models.GetBatchTaskVersionsRequest,
    ) -> main_models.GetBatchTaskVersionsResponse:
        runtime = RuntimeOptions()
        return self.get_batch_task_versions_with_options(request, runtime)

    async def get_batch_task_versions_async(
        self,
        request: main_models.GetBatchTaskVersionsRequest,
    ) -> main_models.GetBatchTaskVersionsResponse:
        runtime = RuntimeOptions()
        return await self.get_batch_task_versions_with_options_async(request, runtime)

    def get_belong_asset_mapping_with_options(
        self,
        tmp_req: main_models.GetBelongAssetMappingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBelongAssetMappingResponse:
        tmp_req.validate()
        request = main_models.GetBelongAssetMappingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.asset_mapping_query):
            request.asset_mapping_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.asset_mapping_query, 'AssetMappingQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.asset_mapping_query_shrink):
            body['AssetMappingQuery'] = request.asset_mapping_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetBelongAssetMapping',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBelongAssetMappingResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_belong_asset_mapping_with_options_async(
        self,
        tmp_req: main_models.GetBelongAssetMappingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBelongAssetMappingResponse:
        tmp_req.validate()
        request = main_models.GetBelongAssetMappingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.asset_mapping_query):
            request.asset_mapping_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.asset_mapping_query, 'AssetMappingQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.asset_mapping_query_shrink):
            body['AssetMappingQuery'] = request.asset_mapping_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetBelongAssetMapping',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBelongAssetMappingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_belong_asset_mapping(
        self,
        request: main_models.GetBelongAssetMappingRequest,
    ) -> main_models.GetBelongAssetMappingResponse:
        runtime = RuntimeOptions()
        return self.get_belong_asset_mapping_with_options(request, runtime)

    async def get_belong_asset_mapping_async(
        self,
        request: main_models.GetBelongAssetMappingRequest,
    ) -> main_models.GetBelongAssetMappingResponse:
        runtime = RuntimeOptions()
        return await self.get_belong_asset_mapping_with_options_async(request, runtime)

    def get_biz_entity_info_with_options(
        self,
        request: main_models.GetBizEntityInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBizEntityInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBizEntityInfo',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBizEntityInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_biz_entity_info_with_options_async(
        self,
        request: main_models.GetBizEntityInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBizEntityInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBizEntityInfo',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBizEntityInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_biz_entity_info(
        self,
        request: main_models.GetBizEntityInfoRequest,
    ) -> main_models.GetBizEntityInfoResponse:
        runtime = RuntimeOptions()
        return self.get_biz_entity_info_with_options(request, runtime)

    async def get_biz_entity_info_async(
        self,
        request: main_models.GetBizEntityInfoRequest,
    ) -> main_models.GetBizEntityInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_biz_entity_info_with_options_async(request, runtime)

    def get_biz_entity_info_by_version_with_options(
        self,
        request: main_models.GetBizEntityInfoByVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBizEntityInfoByVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBizEntityInfoByVersion',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBizEntityInfoByVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_biz_entity_info_by_version_with_options_async(
        self,
        request: main_models.GetBizEntityInfoByVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBizEntityInfoByVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBizEntityInfoByVersion',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBizEntityInfoByVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_biz_entity_info_by_version(
        self,
        request: main_models.GetBizEntityInfoByVersionRequest,
    ) -> main_models.GetBizEntityInfoByVersionResponse:
        runtime = RuntimeOptions()
        return self.get_biz_entity_info_by_version_with_options(request, runtime)

    async def get_biz_entity_info_by_version_async(
        self,
        request: main_models.GetBizEntityInfoByVersionRequest,
    ) -> main_models.GetBizEntityInfoByVersionResponse:
        runtime = RuntimeOptions()
        return await self.get_biz_entity_info_by_version_with_options_async(request, runtime)

    def get_biz_metric_by_name_with_options(
        self,
        tmp_req: main_models.GetBizMetricByNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBizMetricByNameResponse:
        tmp_req.validate()
        request = main_models.GetBizMetricByNameShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.biz_metric_by_name_query):
            request.biz_metric_by_name_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.biz_metric_by_name_query, 'BizMetricByNameQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.biz_metric_by_name_query_shrink):
            body['BizMetricByNameQuery'] = request.biz_metric_by_name_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetBizMetricByName',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBizMetricByNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_biz_metric_by_name_with_options_async(
        self,
        tmp_req: main_models.GetBizMetricByNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBizMetricByNameResponse:
        tmp_req.validate()
        request = main_models.GetBizMetricByNameShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.biz_metric_by_name_query):
            request.biz_metric_by_name_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.biz_metric_by_name_query, 'BizMetricByNameQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.biz_metric_by_name_query_shrink):
            body['BizMetricByNameQuery'] = request.biz_metric_by_name_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetBizMetricByName',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBizMetricByNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_biz_metric_by_name(
        self,
        request: main_models.GetBizMetricByNameRequest,
    ) -> main_models.GetBizMetricByNameResponse:
        runtime = RuntimeOptions()
        return self.get_biz_metric_by_name_with_options(request, runtime)

    async def get_biz_metric_by_name_async(
        self,
        request: main_models.GetBizMetricByNameRequest,
    ) -> main_models.GetBizMetricByNameResponse:
        runtime = RuntimeOptions()
        return await self.get_biz_metric_by_name_with_options_async(request, runtime)

    def get_biz_unit_info_with_options(
        self,
        request: main_models.GetBizUnitInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBizUnitInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBizUnitInfo',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBizUnitInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_biz_unit_info_with_options_async(
        self,
        request: main_models.GetBizUnitInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBizUnitInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBizUnitInfo',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBizUnitInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_biz_unit_info(
        self,
        request: main_models.GetBizUnitInfoRequest,
    ) -> main_models.GetBizUnitInfoResponse:
        runtime = RuntimeOptions()
        return self.get_biz_unit_info_with_options(request, runtime)

    async def get_biz_unit_info_async(
        self,
        request: main_models.GetBizUnitInfoRequest,
    ) -> main_models.GetBizUnitInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_biz_unit_info_with_options_async(request, runtime)

    def get_check_connectivity_jobs_with_options(
        self,
        request: main_models.GetCheckConnectivityJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCheckConnectivityJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCheckConnectivityJobs',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCheckConnectivityJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_check_connectivity_jobs_with_options_async(
        self,
        request: main_models.GetCheckConnectivityJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCheckConnectivityJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCheckConnectivityJobs',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCheckConnectivityJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_check_connectivity_jobs(
        self,
        request: main_models.GetCheckConnectivityJobsRequest,
    ) -> main_models.GetCheckConnectivityJobsResponse:
        runtime = RuntimeOptions()
        return self.get_check_connectivity_jobs_with_options(request, runtime)

    async def get_check_connectivity_jobs_async(
        self,
        request: main_models.GetCheckConnectivityJobsRequest,
    ) -> main_models.GetCheckConnectivityJobsResponse:
        runtime = RuntimeOptions()
        return await self.get_check_connectivity_jobs_with_options_async(request, runtime)

    def get_cluster_queue_info_by_env_with_options(
        self,
        request: main_models.GetClusterQueueInfoByEnvRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetClusterQueueInfoByEnvResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.stream_batch_mode):
            query['StreamBatchMode'] = request.stream_batch_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetClusterQueueInfoByEnv',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetClusterQueueInfoByEnvResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cluster_queue_info_by_env_with_options_async(
        self,
        request: main_models.GetClusterQueueInfoByEnvRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetClusterQueueInfoByEnvResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.stream_batch_mode):
            query['StreamBatchMode'] = request.stream_batch_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetClusterQueueInfoByEnv',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetClusterQueueInfoByEnvResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cluster_queue_info_by_env(
        self,
        request: main_models.GetClusterQueueInfoByEnvRequest,
    ) -> main_models.GetClusterQueueInfoByEnvResponse:
        runtime = RuntimeOptions()
        return self.get_cluster_queue_info_by_env_with_options(request, runtime)

    async def get_cluster_queue_info_by_env_async(
        self,
        request: main_models.GetClusterQueueInfoByEnvRequest,
    ) -> main_models.GetClusterQueueInfoByEnvResponse:
        runtime = RuntimeOptions()
        return await self.get_cluster_queue_info_by_env_with_options_async(request, runtime)

    def get_compute_source_with_options(
        self,
        request: main_models.GetComputeSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetComputeSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetComputeSource',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetComputeSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_compute_source_with_options_async(
        self,
        request: main_models.GetComputeSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetComputeSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetComputeSource',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetComputeSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_compute_source(
        self,
        request: main_models.GetComputeSourceRequest,
    ) -> main_models.GetComputeSourceResponse:
        runtime = RuntimeOptions()
        return self.get_compute_source_with_options(request, runtime)

    async def get_compute_source_async(
        self,
        request: main_models.GetComputeSourceRequest,
    ) -> main_models.GetComputeSourceResponse:
        runtime = RuntimeOptions()
        return await self.get_compute_source_with_options_async(request, runtime)

    def get_data_domain_info_with_options(
        self,
        request: main_models.GetDataDomainInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataDomainInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataDomainInfo',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataDomainInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_domain_info_with_options_async(
        self,
        request: main_models.GetDataDomainInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataDomainInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataDomainInfo',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataDomainInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_domain_info(
        self,
        request: main_models.GetDataDomainInfoRequest,
    ) -> main_models.GetDataDomainInfoResponse:
        runtime = RuntimeOptions()
        return self.get_data_domain_info_with_options(request, runtime)

    async def get_data_domain_info_async(
        self,
        request: main_models.GetDataDomainInfoRequest,
    ) -> main_models.GetDataDomainInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_data_domain_info_with_options_async(request, runtime)

    def get_data_service_api_call_summary_with_options(
        self,
        request: main_models.GetDataServiceApiCallSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataServiceApiCallSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataServiceApiCallSummary',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataServiceApiCallSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_service_api_call_summary_with_options_async(
        self,
        request: main_models.GetDataServiceApiCallSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataServiceApiCallSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataServiceApiCallSummary',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataServiceApiCallSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_service_api_call_summary(
        self,
        request: main_models.GetDataServiceApiCallSummaryRequest,
    ) -> main_models.GetDataServiceApiCallSummaryResponse:
        runtime = RuntimeOptions()
        return self.get_data_service_api_call_summary_with_options(request, runtime)

    async def get_data_service_api_call_summary_async(
        self,
        request: main_models.GetDataServiceApiCallSummaryRequest,
    ) -> main_models.GetDataServiceApiCallSummaryResponse:
        runtime = RuntimeOptions()
        return await self.get_data_service_api_call_summary_with_options_async(request, runtime)

    def get_data_service_api_call_trend_with_options(
        self,
        request: main_models.GetDataServiceApiCallTrendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataServiceApiCallTrendResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataServiceApiCallTrend',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataServiceApiCallTrendResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_service_api_call_trend_with_options_async(
        self,
        request: main_models.GetDataServiceApiCallTrendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataServiceApiCallTrendResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataServiceApiCallTrend',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataServiceApiCallTrendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_service_api_call_trend(
        self,
        request: main_models.GetDataServiceApiCallTrendRequest,
    ) -> main_models.GetDataServiceApiCallTrendResponse:
        runtime = RuntimeOptions()
        return self.get_data_service_api_call_trend_with_options(request, runtime)

    async def get_data_service_api_call_trend_async(
        self,
        request: main_models.GetDataServiceApiCallTrendRequest,
    ) -> main_models.GetDataServiceApiCallTrendResponse:
        runtime = RuntimeOptions()
        return await self.get_data_service_api_call_trend_with_options_async(request, runtime)

    def get_data_service_api_document_with_options(
        self,
        request: main_models.GetDataServiceApiDocumentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataServiceApiDocumentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataServiceApiDocument',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataServiceApiDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_service_api_document_with_options_async(
        self,
        request: main_models.GetDataServiceApiDocumentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataServiceApiDocumentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataServiceApiDocument',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataServiceApiDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_service_api_document(
        self,
        request: main_models.GetDataServiceApiDocumentRequest,
    ) -> main_models.GetDataServiceApiDocumentResponse:
        runtime = RuntimeOptions()
        return self.get_data_service_api_document_with_options(request, runtime)

    async def get_data_service_api_document_async(
        self,
        request: main_models.GetDataServiceApiDocumentRequest,
    ) -> main_models.GetDataServiceApiDocumentResponse:
        runtime = RuntimeOptions()
        return await self.get_data_service_api_document_with_options_async(request, runtime)

    def get_data_service_api_error_impact_with_options(
        self,
        request: main_models.GetDataServiceApiErrorImpactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataServiceApiErrorImpactResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataServiceApiErrorImpact',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataServiceApiErrorImpactResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_service_api_error_impact_with_options_async(
        self,
        request: main_models.GetDataServiceApiErrorImpactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataServiceApiErrorImpactResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataServiceApiErrorImpact',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataServiceApiErrorImpactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_service_api_error_impact(
        self,
        request: main_models.GetDataServiceApiErrorImpactRequest,
    ) -> main_models.GetDataServiceApiErrorImpactResponse:
        runtime = RuntimeOptions()
        return self.get_data_service_api_error_impact_with_options(request, runtime)

    async def get_data_service_api_error_impact_async(
        self,
        request: main_models.GetDataServiceApiErrorImpactRequest,
    ) -> main_models.GetDataServiceApiErrorImpactResponse:
        runtime = RuntimeOptions()
        return await self.get_data_service_api_error_impact_with_options_async(request, runtime)

    def get_data_service_api_groups_with_options(
        self,
        request: main_models.GetDataServiceApiGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataServiceApiGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataServiceApiGroups',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataServiceApiGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_service_api_groups_with_options_async(
        self,
        request: main_models.GetDataServiceApiGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataServiceApiGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataServiceApiGroups',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataServiceApiGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_service_api_groups(
        self,
        request: main_models.GetDataServiceApiGroupsRequest,
    ) -> main_models.GetDataServiceApiGroupsResponse:
        runtime = RuntimeOptions()
        return self.get_data_service_api_groups_with_options(request, runtime)

    async def get_data_service_api_groups_async(
        self,
        request: main_models.GetDataServiceApiGroupsRequest,
    ) -> main_models.GetDataServiceApiGroupsResponse:
        runtime = RuntimeOptions()
        return await self.get_data_service_api_groups_with_options_async(request, runtime)

    def get_data_service_app_authorized_users_with_options(
        self,
        request: main_models.GetDataServiceAppAuthorizedUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataServiceAppAuthorizedUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataServiceAppAuthorizedUsers',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataServiceAppAuthorizedUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_service_app_authorized_users_with_options_async(
        self,
        request: main_models.GetDataServiceAppAuthorizedUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataServiceAppAuthorizedUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataServiceAppAuthorizedUsers',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataServiceAppAuthorizedUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_service_app_authorized_users(
        self,
        request: main_models.GetDataServiceAppAuthorizedUsersRequest,
    ) -> main_models.GetDataServiceAppAuthorizedUsersResponse:
        runtime = RuntimeOptions()
        return self.get_data_service_app_authorized_users_with_options(request, runtime)

    async def get_data_service_app_authorized_users_async(
        self,
        request: main_models.GetDataServiceAppAuthorizedUsersRequest,
    ) -> main_models.GetDataServiceAppAuthorizedUsersResponse:
        runtime = RuntimeOptions()
        return await self.get_data_service_app_authorized_users_with_options_async(request, runtime)

    def get_data_service_app_groups_with_options(
        self,
        request: main_models.GetDataServiceAppGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataServiceAppGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataServiceAppGroups',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataServiceAppGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_service_app_groups_with_options_async(
        self,
        request: main_models.GetDataServiceAppGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataServiceAppGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataServiceAppGroups',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataServiceAppGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_service_app_groups(
        self,
        request: main_models.GetDataServiceAppGroupsRequest,
    ) -> main_models.GetDataServiceAppGroupsResponse:
        runtime = RuntimeOptions()
        return self.get_data_service_app_groups_with_options(request, runtime)

    async def get_data_service_app_groups_async(
        self,
        request: main_models.GetDataServiceAppGroupsRequest,
    ) -> main_models.GetDataServiceAppGroupsResponse:
        runtime = RuntimeOptions()
        return await self.get_data_service_app_groups_with_options_async(request, runtime)

    def get_data_service_apps_by_group_id_with_options(
        self,
        request: main_models.GetDataServiceAppsByGroupIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataServiceAppsByGroupIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataServiceAppsByGroupId',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataServiceAppsByGroupIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_service_apps_by_group_id_with_options_async(
        self,
        request: main_models.GetDataServiceAppsByGroupIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataServiceAppsByGroupIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataServiceAppsByGroupId',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataServiceAppsByGroupIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_service_apps_by_group_id(
        self,
        request: main_models.GetDataServiceAppsByGroupIdRequest,
    ) -> main_models.GetDataServiceAppsByGroupIdResponse:
        runtime = RuntimeOptions()
        return self.get_data_service_apps_by_group_id_with_options(request, runtime)

    async def get_data_service_apps_by_group_id_async(
        self,
        request: main_models.GetDataServiceAppsByGroupIdRequest,
    ) -> main_models.GetDataServiceAppsByGroupIdResponse:
        runtime = RuntimeOptions()
        return await self.get_data_service_apps_by_group_id_with_options_async(request, runtime)

    def get_data_service_authorized_apps_by_group_id_with_options(
        self,
        request: main_models.GetDataServiceAuthorizedAppsByGroupIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataServiceAuthorizedAppsByGroupIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataServiceAuthorizedAppsByGroupId',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataServiceAuthorizedAppsByGroupIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_service_authorized_apps_by_group_id_with_options_async(
        self,
        request: main_models.GetDataServiceAuthorizedAppsByGroupIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataServiceAuthorizedAppsByGroupIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataServiceAuthorizedAppsByGroupId',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataServiceAuthorizedAppsByGroupIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_service_authorized_apps_by_group_id(
        self,
        request: main_models.GetDataServiceAuthorizedAppsByGroupIdRequest,
    ) -> main_models.GetDataServiceAuthorizedAppsByGroupIdResponse:
        runtime = RuntimeOptions()
        return self.get_data_service_authorized_apps_by_group_id_with_options(request, runtime)

    async def get_data_service_authorized_apps_by_group_id_async(
        self,
        request: main_models.GetDataServiceAuthorizedAppsByGroupIdRequest,
    ) -> main_models.GetDataServiceAuthorizedAppsByGroupIdResponse:
        runtime = RuntimeOptions()
        return await self.get_data_service_authorized_apps_by_group_id_with_options_async(request, runtime)

    def get_data_service_authorized_projects_with_options(
        self,
        request: main_models.GetDataServiceAuthorizedProjectsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataServiceAuthorizedProjectsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataServiceAuthorizedProjects',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataServiceAuthorizedProjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_service_authorized_projects_with_options_async(
        self,
        request: main_models.GetDataServiceAuthorizedProjectsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataServiceAuthorizedProjectsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataServiceAuthorizedProjects',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataServiceAuthorizedProjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_service_authorized_projects(
        self,
        request: main_models.GetDataServiceAuthorizedProjectsRequest,
    ) -> main_models.GetDataServiceAuthorizedProjectsResponse:
        runtime = RuntimeOptions()
        return self.get_data_service_authorized_projects_with_options(request, runtime)

    async def get_data_service_authorized_projects_async(
        self,
        request: main_models.GetDataServiceAuthorizedProjectsRequest,
    ) -> main_models.GetDataServiceAuthorizedProjectsResponse:
        runtime = RuntimeOptions()
        return await self.get_data_service_authorized_projects_with_options_async(request, runtime)

    def get_data_service_my_projects_with_options(
        self,
        request: main_models.GetDataServiceMyProjectsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataServiceMyProjectsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataServiceMyProjects',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataServiceMyProjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_service_my_projects_with_options_async(
        self,
        request: main_models.GetDataServiceMyProjectsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataServiceMyProjectsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataServiceMyProjects',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataServiceMyProjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_service_my_projects(
        self,
        request: main_models.GetDataServiceMyProjectsRequest,
    ) -> main_models.GetDataServiceMyProjectsResponse:
        runtime = RuntimeOptions()
        return self.get_data_service_my_projects_with_options(request, runtime)

    async def get_data_service_my_projects_async(
        self,
        request: main_models.GetDataServiceMyProjectsRequest,
    ) -> main_models.GetDataServiceMyProjectsResponse:
        runtime = RuntimeOptions()
        return await self.get_data_service_my_projects_with_options_async(request, runtime)

    def get_data_service_project_addable_users_with_options(
        self,
        request: main_models.GetDataServiceProjectAddableUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataServiceProjectAddableUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataServiceProjectAddableUsers',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataServiceProjectAddableUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_service_project_addable_users_with_options_async(
        self,
        request: main_models.GetDataServiceProjectAddableUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataServiceProjectAddableUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataServiceProjectAddableUsers',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataServiceProjectAddableUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_service_project_addable_users(
        self,
        request: main_models.GetDataServiceProjectAddableUsersRequest,
    ) -> main_models.GetDataServiceProjectAddableUsersResponse:
        runtime = RuntimeOptions()
        return self.get_data_service_project_addable_users_with_options(request, runtime)

    async def get_data_service_project_addable_users_async(
        self,
        request: main_models.GetDataServiceProjectAddableUsersRequest,
    ) -> main_models.GetDataServiceProjectAddableUsersResponse:
        runtime = RuntimeOptions()
        return await self.get_data_service_project_addable_users_with_options_async(request, runtime)

    def get_data_source_dependencies_with_options(
        self,
        request: main_models.GetDataSourceDependenciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataSourceDependenciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataSourceDependencies',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataSourceDependenciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_source_dependencies_with_options_async(
        self,
        request: main_models.GetDataSourceDependenciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataSourceDependenciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataSourceDependencies',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataSourceDependenciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_source_dependencies(
        self,
        request: main_models.GetDataSourceDependenciesRequest,
    ) -> main_models.GetDataSourceDependenciesResponse:
        runtime = RuntimeOptions()
        return self.get_data_source_dependencies_with_options(request, runtime)

    async def get_data_source_dependencies_async(
        self,
        request: main_models.GetDataSourceDependenciesRequest,
    ) -> main_models.GetDataSourceDependenciesResponse:
        runtime = RuntimeOptions()
        return await self.get_data_source_dependencies_with_options_async(request, runtime)

    def get_dev_object_dependency_with_options(
        self,
        request: main_models.GetDevObjectDependencyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDevObjectDependencyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.object_from):
            query['ObjectFrom'] = request.object_from
        if not DaraCore.is_null(request.object_id):
            query['ObjectId'] = request.object_id
        if not DaraCore.is_null(request.object_type):
            query['ObjectType'] = request.object_type
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDevObjectDependency',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDevObjectDependencyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dev_object_dependency_with_options_async(
        self,
        request: main_models.GetDevObjectDependencyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDevObjectDependencyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.object_from):
            query['ObjectFrom'] = request.object_from
        if not DaraCore.is_null(request.object_id):
            query['ObjectId'] = request.object_id
        if not DaraCore.is_null(request.object_type):
            query['ObjectType'] = request.object_type
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDevObjectDependency',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDevObjectDependencyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dev_object_dependency(
        self,
        request: main_models.GetDevObjectDependencyRequest,
    ) -> main_models.GetDevObjectDependencyResponse:
        runtime = RuntimeOptions()
        return self.get_dev_object_dependency_with_options(request, runtime)

    async def get_dev_object_dependency_async(
        self,
        request: main_models.GetDevObjectDependencyRequest,
    ) -> main_models.GetDevObjectDependencyResponse:
        runtime = RuntimeOptions()
        return await self.get_dev_object_dependency_with_options_async(request, runtime)

    def get_directory_tree_with_options(
        self,
        request: main_models.GetDirectoryTreeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDirectoryTreeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDirectoryTree',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDirectoryTreeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_directory_tree_with_options_async(
        self,
        request: main_models.GetDirectoryTreeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDirectoryTreeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDirectoryTree',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDirectoryTreeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_directory_tree(
        self,
        request: main_models.GetDirectoryTreeRequest,
    ) -> main_models.GetDirectoryTreeResponse:
        runtime = RuntimeOptions()
        return self.get_directory_tree_with_options(request, runtime)

    async def get_directory_tree_async(
        self,
        request: main_models.GetDirectoryTreeRequest,
    ) -> main_models.GetDirectoryTreeResponse:
        runtime = RuntimeOptions()
        return await self.get_directory_tree_with_options_async(request, runtime)

    def get_file_storage_credential_with_options(
        self,
        request: main_models.GetFileStorageCredentialRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFileStorageCredentialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.purpose):
            query['Purpose'] = request.purpose
        if not DaraCore.is_null(request.use_vpc_endpoint):
            query['UseVpcEndpoint'] = request.use_vpc_endpoint
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetFileStorageCredential',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFileStorageCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_file_storage_credential_with_options_async(
        self,
        request: main_models.GetFileStorageCredentialRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFileStorageCredentialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.purpose):
            query['Purpose'] = request.purpose
        if not DaraCore.is_null(request.use_vpc_endpoint):
            query['UseVpcEndpoint'] = request.use_vpc_endpoint
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetFileStorageCredential',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFileStorageCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_file_storage_credential(
        self,
        request: main_models.GetFileStorageCredentialRequest,
    ) -> main_models.GetFileStorageCredentialResponse:
        runtime = RuntimeOptions()
        return self.get_file_storage_credential_with_options(request, runtime)

    async def get_file_storage_credential_async(
        self,
        request: main_models.GetFileStorageCredentialRequest,
    ) -> main_models.GetFileStorageCredentialResponse:
        runtime = RuntimeOptions()
        return await self.get_file_storage_credential_with_options_async(request, runtime)

    def get_instance_down_stream_with_options(
        self,
        tmp_req: main_models.GetInstanceDownStreamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceDownStreamResponse:
        tmp_req.validate()
        request = main_models.GetInstanceDownStreamShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.instance_get):
            request.instance_get_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_get, 'InstanceGet', 'json')
        query = {}
        if not DaraCore.is_null(request.down_stream_depth):
            query['DownStreamDepth'] = request.down_stream_depth
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.run_status):
            query['RunStatus'] = request.run_status
        body = {}
        if not DaraCore.is_null(request.instance_get_shrink):
            body['InstanceGet'] = request.instance_get_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceDownStream',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceDownStreamResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_down_stream_with_options_async(
        self,
        tmp_req: main_models.GetInstanceDownStreamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceDownStreamResponse:
        tmp_req.validate()
        request = main_models.GetInstanceDownStreamShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.instance_get):
            request.instance_get_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_get, 'InstanceGet', 'json')
        query = {}
        if not DaraCore.is_null(request.down_stream_depth):
            query['DownStreamDepth'] = request.down_stream_depth
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.run_status):
            query['RunStatus'] = request.run_status
        body = {}
        if not DaraCore.is_null(request.instance_get_shrink):
            body['InstanceGet'] = request.instance_get_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceDownStream',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceDownStreamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_down_stream(
        self,
        request: main_models.GetInstanceDownStreamRequest,
    ) -> main_models.GetInstanceDownStreamResponse:
        runtime = RuntimeOptions()
        return self.get_instance_down_stream_with_options(request, runtime)

    async def get_instance_down_stream_async(
        self,
        request: main_models.GetInstanceDownStreamRequest,
    ) -> main_models.GetInstanceDownStreamResponse:
        runtime = RuntimeOptions()
        return await self.get_instance_down_stream_with_options_async(request, runtime)

    def get_instance_up_down_stream_with_options(
        self,
        tmp_req: main_models.GetInstanceUpDownStreamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceUpDownStreamResponse:
        tmp_req.validate()
        request = main_models.GetInstanceUpDownStreamShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.instance_id):
            request.instance_id_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_id, 'InstanceId', 'json')
        query = {}
        if not DaraCore.is_null(request.down_stream_depth):
            query['DownStreamDepth'] = request.down_stream_depth
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.up_stream_depth):
            query['UpStreamDepth'] = request.up_stream_depth
        body = {}
        if not DaraCore.is_null(request.instance_id_shrink):
            body['InstanceId'] = request.instance_id_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceUpDownStream',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceUpDownStreamResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_up_down_stream_with_options_async(
        self,
        tmp_req: main_models.GetInstanceUpDownStreamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceUpDownStreamResponse:
        tmp_req.validate()
        request = main_models.GetInstanceUpDownStreamShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.instance_id):
            request.instance_id_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_id, 'InstanceId', 'json')
        query = {}
        if not DaraCore.is_null(request.down_stream_depth):
            query['DownStreamDepth'] = request.down_stream_depth
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.up_stream_depth):
            query['UpStreamDepth'] = request.up_stream_depth
        body = {}
        if not DaraCore.is_null(request.instance_id_shrink):
            body['InstanceId'] = request.instance_id_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceUpDownStream',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceUpDownStreamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_up_down_stream(
        self,
        request: main_models.GetInstanceUpDownStreamRequest,
    ) -> main_models.GetInstanceUpDownStreamResponse:
        runtime = RuntimeOptions()
        return self.get_instance_up_down_stream_with_options(request, runtime)

    async def get_instance_up_down_stream_async(
        self,
        request: main_models.GetInstanceUpDownStreamRequest,
    ) -> main_models.GetInstanceUpDownStreamResponse:
        runtime = RuntimeOptions()
        return await self.get_instance_up_down_stream_with_options_async(request, runtime)

    def get_latest_submit_detail_with_options(
        self,
        tmp_req: main_models.GetLatestSubmitDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLatestSubmitDetailResponse:
        tmp_req.validate()
        request = main_models.GetLatestSubmitDetailShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.submit_detail_query):
            request.submit_detail_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.submit_detail_query, 'SubmitDetailQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.submit_detail_query_shrink):
            body['SubmitDetailQuery'] = request.submit_detail_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetLatestSubmitDetail',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLatestSubmitDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_latest_submit_detail_with_options_async(
        self,
        tmp_req: main_models.GetLatestSubmitDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLatestSubmitDetailResponse:
        tmp_req.validate()
        request = main_models.GetLatestSubmitDetailShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.submit_detail_query):
            request.submit_detail_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.submit_detail_query, 'SubmitDetailQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.submit_detail_query_shrink):
            body['SubmitDetailQuery'] = request.submit_detail_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetLatestSubmitDetail',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLatestSubmitDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_latest_submit_detail(
        self,
        request: main_models.GetLatestSubmitDetailRequest,
    ) -> main_models.GetLatestSubmitDetailResponse:
        runtime = RuntimeOptions()
        return self.get_latest_submit_detail_with_options(request, runtime)

    async def get_latest_submit_detail_async(
        self,
        request: main_models.GetLatestSubmitDetailRequest,
    ) -> main_models.GetLatestSubmitDetailResponse:
        runtime = RuntimeOptions()
        return await self.get_latest_submit_detail_with_options_async(request, runtime)

    def get_my_roles_with_options(
        self,
        request: main_models.GetMyRolesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMyRolesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMyRoles',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMyRolesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_my_roles_with_options_async(
        self,
        request: main_models.GetMyRolesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMyRolesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMyRoles',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMyRolesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_my_roles(
        self,
        request: main_models.GetMyRolesRequest,
    ) -> main_models.GetMyRolesResponse:
        runtime = RuntimeOptions()
        return self.get_my_roles_with_options(request, runtime)

    async def get_my_roles_async(
        self,
        request: main_models.GetMyRolesRequest,
    ) -> main_models.GetMyRolesResponse:
        runtime = RuntimeOptions()
        return await self.get_my_roles_with_options_async(request, runtime)

    def get_my_tenants_with_options(
        self,
        tmp_req: main_models.GetMyTenantsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMyTenantsResponse:
        tmp_req.validate()
        request = main_models.GetMyTenantsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.feature_code_list):
            request.feature_code_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.feature_code_list, 'FeatureCodeList', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.feature_code_list_shrink):
            body['FeatureCodeList'] = request.feature_code_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetMyTenants',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMyTenantsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_my_tenants_with_options_async(
        self,
        tmp_req: main_models.GetMyTenantsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMyTenantsResponse:
        tmp_req.validate()
        request = main_models.GetMyTenantsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.feature_code_list):
            request.feature_code_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.feature_code_list, 'FeatureCodeList', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.feature_code_list_shrink):
            body['FeatureCodeList'] = request.feature_code_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetMyTenants',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMyTenantsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_my_tenants(
        self,
        request: main_models.GetMyTenantsRequest,
    ) -> main_models.GetMyTenantsResponse:
        runtime = RuntimeOptions()
        return self.get_my_tenants_with_options(request, runtime)

    async def get_my_tenants_async(
        self,
        request: main_models.GetMyTenantsRequest,
    ) -> main_models.GetMyTenantsResponse:
        runtime = RuntimeOptions()
        return await self.get_my_tenants_with_options_async(request, runtime)

    def get_node_up_down_stream_with_options(
        self,
        tmp_req: main_models.GetNodeUpDownStreamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNodeUpDownStreamResponse:
        tmp_req.validate()
        request = main_models.GetNodeUpDownStreamShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.node_id):
            request.node_id_shrink = Utils.array_to_string_with_specified_style(tmp_req.node_id, 'NodeId', 'json')
        query = {}
        if not DaraCore.is_null(request.down_stream_depth):
            query['DownStreamDepth'] = request.down_stream_depth
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.up_stream_depth):
            query['UpStreamDepth'] = request.up_stream_depth
        body = {}
        if not DaraCore.is_null(request.node_id_shrink):
            body['NodeId'] = request.node_id_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetNodeUpDownStream',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNodeUpDownStreamResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_node_up_down_stream_with_options_async(
        self,
        tmp_req: main_models.GetNodeUpDownStreamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNodeUpDownStreamResponse:
        tmp_req.validate()
        request = main_models.GetNodeUpDownStreamShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.node_id):
            request.node_id_shrink = Utils.array_to_string_with_specified_style(tmp_req.node_id, 'NodeId', 'json')
        query = {}
        if not DaraCore.is_null(request.down_stream_depth):
            query['DownStreamDepth'] = request.down_stream_depth
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.up_stream_depth):
            query['UpStreamDepth'] = request.up_stream_depth
        body = {}
        if not DaraCore.is_null(request.node_id_shrink):
            body['NodeId'] = request.node_id_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetNodeUpDownStream',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNodeUpDownStreamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_node_up_down_stream(
        self,
        request: main_models.GetNodeUpDownStreamRequest,
    ) -> main_models.GetNodeUpDownStreamResponse:
        runtime = RuntimeOptions()
        return self.get_node_up_down_stream_with_options(request, runtime)

    async def get_node_up_down_stream_async(
        self,
        request: main_models.GetNodeUpDownStreamRequest,
    ) -> main_models.GetNodeUpDownStreamResponse:
        runtime = RuntimeOptions()
        return await self.get_node_up_down_stream_with_options_async(request, runtime)

    def get_operation_submit_status_with_options(
        self,
        request: main_models.GetOperationSubmitStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOperationSubmitStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOperationSubmitStatus',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOperationSubmitStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_operation_submit_status_with_options_async(
        self,
        request: main_models.GetOperationSubmitStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOperationSubmitStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOperationSubmitStatus',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOperationSubmitStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_operation_submit_status(
        self,
        request: main_models.GetOperationSubmitStatusRequest,
    ) -> main_models.GetOperationSubmitStatusResponse:
        runtime = RuntimeOptions()
        return self.get_operation_submit_status_with_options(request, runtime)

    async def get_operation_submit_status_async(
        self,
        request: main_models.GetOperationSubmitStatusRequest,
    ) -> main_models.GetOperationSubmitStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_operation_submit_status_with_options_async(request, runtime)

    def get_physical_instance_with_options(
        self,
        request: main_models.GetPhysicalInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPhysicalInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPhysicalInstance',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPhysicalInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_physical_instance_with_options_async(
        self,
        request: main_models.GetPhysicalInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPhysicalInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPhysicalInstance',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPhysicalInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_physical_instance(
        self,
        request: main_models.GetPhysicalInstanceRequest,
    ) -> main_models.GetPhysicalInstanceResponse:
        runtime = RuntimeOptions()
        return self.get_physical_instance_with_options(request, runtime)

    async def get_physical_instance_async(
        self,
        request: main_models.GetPhysicalInstanceRequest,
    ) -> main_models.GetPhysicalInstanceResponse:
        runtime = RuntimeOptions()
        return await self.get_physical_instance_with_options_async(request, runtime)

    def get_physical_instance_log_with_options(
        self,
        request: main_models.GetPhysicalInstanceLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPhysicalInstanceLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPhysicalInstanceLog',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPhysicalInstanceLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_physical_instance_log_with_options_async(
        self,
        request: main_models.GetPhysicalInstanceLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPhysicalInstanceLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPhysicalInstanceLog',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPhysicalInstanceLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_physical_instance_log(
        self,
        request: main_models.GetPhysicalInstanceLogRequest,
    ) -> main_models.GetPhysicalInstanceLogResponse:
        runtime = RuntimeOptions()
        return self.get_physical_instance_log_with_options(request, runtime)

    async def get_physical_instance_log_async(
        self,
        request: main_models.GetPhysicalInstanceLogRequest,
    ) -> main_models.GetPhysicalInstanceLogResponse:
        runtime = RuntimeOptions()
        return await self.get_physical_instance_log_with_options_async(request, runtime)

    def get_physical_node_with_options(
        self,
        request: main_models.GetPhysicalNodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPhysicalNodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPhysicalNode',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPhysicalNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_physical_node_with_options_async(
        self,
        request: main_models.GetPhysicalNodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPhysicalNodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPhysicalNode',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPhysicalNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_physical_node(
        self,
        request: main_models.GetPhysicalNodeRequest,
    ) -> main_models.GetPhysicalNodeResponse:
        runtime = RuntimeOptions()
        return self.get_physical_node_with_options(request, runtime)

    async def get_physical_node_async(
        self,
        request: main_models.GetPhysicalNodeRequest,
    ) -> main_models.GetPhysicalNodeResponse:
        runtime = RuntimeOptions()
        return await self.get_physical_node_with_options_async(request, runtime)

    def get_physical_node_by_output_name_with_options(
        self,
        request: main_models.GetPhysicalNodeByOutputNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPhysicalNodeByOutputNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.output_name):
            query['OutputName'] = request.output_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPhysicalNodeByOutputName',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPhysicalNodeByOutputNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_physical_node_by_output_name_with_options_async(
        self,
        request: main_models.GetPhysicalNodeByOutputNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPhysicalNodeByOutputNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.output_name):
            query['OutputName'] = request.output_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPhysicalNodeByOutputName',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPhysicalNodeByOutputNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_physical_node_by_output_name(
        self,
        request: main_models.GetPhysicalNodeByOutputNameRequest,
    ) -> main_models.GetPhysicalNodeByOutputNameResponse:
        runtime = RuntimeOptions()
        return self.get_physical_node_by_output_name_with_options(request, runtime)

    async def get_physical_node_by_output_name_async(
        self,
        request: main_models.GetPhysicalNodeByOutputNameRequest,
    ) -> main_models.GetPhysicalNodeByOutputNameResponse:
        runtime = RuntimeOptions()
        return await self.get_physical_node_by_output_name_with_options_async(request, runtime)

    def get_physical_node_content_with_options(
        self,
        request: main_models.GetPhysicalNodeContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPhysicalNodeContentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPhysicalNodeContent',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPhysicalNodeContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_physical_node_content_with_options_async(
        self,
        request: main_models.GetPhysicalNodeContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPhysicalNodeContentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPhysicalNodeContent',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPhysicalNodeContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_physical_node_content(
        self,
        request: main_models.GetPhysicalNodeContentRequest,
    ) -> main_models.GetPhysicalNodeContentResponse:
        runtime = RuntimeOptions()
        return self.get_physical_node_content_with_options(request, runtime)

    async def get_physical_node_content_async(
        self,
        request: main_models.GetPhysicalNodeContentRequest,
    ) -> main_models.GetPhysicalNodeContentResponse:
        runtime = RuntimeOptions()
        return await self.get_physical_node_content_with_options_async(request, runtime)

    def get_physical_node_operation_log_with_options(
        self,
        request: main_models.GetPhysicalNodeOperationLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPhysicalNodeOperationLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPhysicalNodeOperationLog',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPhysicalNodeOperationLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_physical_node_operation_log_with_options_async(
        self,
        request: main_models.GetPhysicalNodeOperationLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPhysicalNodeOperationLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPhysicalNodeOperationLog',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPhysicalNodeOperationLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_physical_node_operation_log(
        self,
        request: main_models.GetPhysicalNodeOperationLogRequest,
    ) -> main_models.GetPhysicalNodeOperationLogResponse:
        runtime = RuntimeOptions()
        return self.get_physical_node_operation_log_with_options(request, runtime)

    async def get_physical_node_operation_log_async(
        self,
        request: main_models.GetPhysicalNodeOperationLogRequest,
    ) -> main_models.GetPhysicalNodeOperationLogResponse:
        runtime = RuntimeOptions()
        return await self.get_physical_node_operation_log_with_options_async(request, runtime)

    def get_pipeline_async_result_with_options(
        self,
        tmp_req: main_models.GetPipelineAsyncResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPipelineAsyncResultResponse:
        tmp_req.validate()
        request = main_models.GetPipelineAsyncResultShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.context):
            request.context_shrink = Utils.array_to_string_with_specified_style(tmp_req.context, 'Context', 'json')
        query = {}
        if not DaraCore.is_null(request.async_id):
            query['AsyncId'] = request.async_id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.context_shrink):
            body['Context'] = request.context_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetPipelineAsyncResult',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPipelineAsyncResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pipeline_async_result_with_options_async(
        self,
        tmp_req: main_models.GetPipelineAsyncResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPipelineAsyncResultResponse:
        tmp_req.validate()
        request = main_models.GetPipelineAsyncResultShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.context):
            request.context_shrink = Utils.array_to_string_with_specified_style(tmp_req.context, 'Context', 'json')
        query = {}
        if not DaraCore.is_null(request.async_id):
            query['AsyncId'] = request.async_id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.context_shrink):
            body['Context'] = request.context_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetPipelineAsyncResult',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPipelineAsyncResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pipeline_async_result(
        self,
        request: main_models.GetPipelineAsyncResultRequest,
    ) -> main_models.GetPipelineAsyncResultResponse:
        runtime = RuntimeOptions()
        return self.get_pipeline_async_result_with_options(request, runtime)

    async def get_pipeline_async_result_async(
        self,
        request: main_models.GetPipelineAsyncResultRequest,
    ) -> main_models.GetPipelineAsyncResultResponse:
        runtime = RuntimeOptions()
        return await self.get_pipeline_async_result_with_options_async(request, runtime)

    def get_pipeline_by_id_with_options(
        self,
        tmp_req: main_models.GetPipelineByIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPipelineByIdResponse:
        tmp_req.validate()
        request = main_models.GetPipelineByIdShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.context):
            request.context_shrink = Utils.array_to_string_with_specified_style(tmp_req.context, 'Context', 'json')
        if not DaraCore.is_null(tmp_req.query_id):
            request.query_id_shrink = Utils.array_to_string_with_specified_style(tmp_req.query_id, 'QueryId', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.context_shrink):
            body['Context'] = request.context_shrink
        if not DaraCore.is_null(request.query_id_shrink):
            body['QueryId'] = request.query_id_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetPipelineById',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPipelineByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pipeline_by_id_with_options_async(
        self,
        tmp_req: main_models.GetPipelineByIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPipelineByIdResponse:
        tmp_req.validate()
        request = main_models.GetPipelineByIdShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.context):
            request.context_shrink = Utils.array_to_string_with_specified_style(tmp_req.context, 'Context', 'json')
        if not DaraCore.is_null(tmp_req.query_id):
            request.query_id_shrink = Utils.array_to_string_with_specified_style(tmp_req.query_id, 'QueryId', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.context_shrink):
            body['Context'] = request.context_shrink
        if not DaraCore.is_null(request.query_id_shrink):
            body['QueryId'] = request.query_id_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetPipelineById',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPipelineByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pipeline_by_id(
        self,
        request: main_models.GetPipelineByIdRequest,
    ) -> main_models.GetPipelineByIdResponse:
        runtime = RuntimeOptions()
        return self.get_pipeline_by_id_with_options(request, runtime)

    async def get_pipeline_by_id_async(
        self,
        request: main_models.GetPipelineByIdRequest,
    ) -> main_models.GetPipelineByIdResponse:
        runtime = RuntimeOptions()
        return await self.get_pipeline_by_id_with_options_async(request, runtime)

    def get_project_with_options(
        self,
        request: main_models.GetProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetProject',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_project_with_options_async(
        self,
        request: main_models.GetProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetProject',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_project(
        self,
        request: main_models.GetProjectRequest,
    ) -> main_models.GetProjectResponse:
        runtime = RuntimeOptions()
        return self.get_project_with_options(request, runtime)

    async def get_project_async(
        self,
        request: main_models.GetProjectRequest,
    ) -> main_models.GetProjectResponse:
        runtime = RuntimeOptions()
        return await self.get_project_with_options_async(request, runtime)

    def get_project_by_name_with_options(
        self,
        request: main_models.GetProjectByNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetProjectByNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetProjectByName',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProjectByNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_project_by_name_with_options_async(
        self,
        request: main_models.GetProjectByNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetProjectByNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetProjectByName',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProjectByNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_project_by_name(
        self,
        request: main_models.GetProjectByNameRequest,
    ) -> main_models.GetProjectByNameResponse:
        runtime = RuntimeOptions()
        return self.get_project_by_name_with_options(request, runtime)

    async def get_project_by_name_async(
        self,
        request: main_models.GetProjectByNameRequest,
    ) -> main_models.GetProjectByNameResponse:
        runtime = RuntimeOptions()
        return await self.get_project_by_name_with_options_async(request, runtime)

    def get_project_produce_user_with_options(
        self,
        request: main_models.GetProjectProduceUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetProjectProduceUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetProjectProduceUser',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProjectProduceUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_project_produce_user_with_options_async(
        self,
        request: main_models.GetProjectProduceUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetProjectProduceUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetProjectProduceUser',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProjectProduceUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_project_produce_user(
        self,
        request: main_models.GetProjectProduceUserRequest,
    ) -> main_models.GetProjectProduceUserResponse:
        runtime = RuntimeOptions()
        return self.get_project_produce_user_with_options(request, runtime)

    async def get_project_produce_user_async(
        self,
        request: main_models.GetProjectProduceUserRequest,
    ) -> main_models.GetProjectProduceUserResponse:
        runtime = RuntimeOptions()
        return await self.get_project_produce_user_with_options_async(request, runtime)

    def get_project_white_lists_with_options(
        self,
        request: main_models.GetProjectWhiteListsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetProjectWhiteListsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetProjectWhiteLists',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProjectWhiteListsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_project_white_lists_with_options_async(
        self,
        request: main_models.GetProjectWhiteListsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetProjectWhiteListsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetProjectWhiteLists',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProjectWhiteListsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_project_white_lists(
        self,
        request: main_models.GetProjectWhiteListsRequest,
    ) -> main_models.GetProjectWhiteListsResponse:
        runtime = RuntimeOptions()
        return self.get_project_white_lists_with_options(request, runtime)

    async def get_project_white_lists_async(
        self,
        request: main_models.GetProjectWhiteListsRequest,
    ) -> main_models.GetProjectWhiteListsResponse:
        runtime = RuntimeOptions()
        return await self.get_project_white_lists_with_options_async(request, runtime)

    def get_quality_alert_of_all_rule_scope_by_watch_id_with_options(
        self,
        request: main_models.GetQualityAlertOfAllRuleScopeByWatchIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQualityAlertOfAllRuleScopeByWatchIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.watch_id):
            query['WatchId'] = request.watch_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQualityAlertOfAllRuleScopeByWatchId',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQualityAlertOfAllRuleScopeByWatchIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_quality_alert_of_all_rule_scope_by_watch_id_with_options_async(
        self,
        request: main_models.GetQualityAlertOfAllRuleScopeByWatchIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQualityAlertOfAllRuleScopeByWatchIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.watch_id):
            query['WatchId'] = request.watch_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQualityAlertOfAllRuleScopeByWatchId',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQualityAlertOfAllRuleScopeByWatchIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_quality_alert_of_all_rule_scope_by_watch_id(
        self,
        request: main_models.GetQualityAlertOfAllRuleScopeByWatchIdRequest,
    ) -> main_models.GetQualityAlertOfAllRuleScopeByWatchIdResponse:
        runtime = RuntimeOptions()
        return self.get_quality_alert_of_all_rule_scope_by_watch_id_with_options(request, runtime)

    async def get_quality_alert_of_all_rule_scope_by_watch_id_async(
        self,
        request: main_models.GetQualityAlertOfAllRuleScopeByWatchIdRequest,
    ) -> main_models.GetQualityAlertOfAllRuleScopeByWatchIdResponse:
        runtime = RuntimeOptions()
        return await self.get_quality_alert_of_all_rule_scope_by_watch_id_with_options_async(request, runtime)

    def get_quality_rule_with_options(
        self,
        request: main_models.GetQualityRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQualityRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQualityRule',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQualityRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_quality_rule_with_options_async(
        self,
        request: main_models.GetQualityRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQualityRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQualityRule',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQualityRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_quality_rule(
        self,
        request: main_models.GetQualityRuleRequest,
    ) -> main_models.GetQualityRuleResponse:
        runtime = RuntimeOptions()
        return self.get_quality_rule_with_options(request, runtime)

    async def get_quality_rule_async(
        self,
        request: main_models.GetQualityRuleRequest,
    ) -> main_models.GetQualityRuleResponse:
        runtime = RuntimeOptions()
        return await self.get_quality_rule_with_options_async(request, runtime)

    def get_quality_rule_task_with_options(
        self,
        request: main_models.GetQualityRuleTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQualityRuleTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.rule_task_id):
            query['RuleTaskId'] = request.rule_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQualityRuleTask',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQualityRuleTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_quality_rule_task_with_options_async(
        self,
        request: main_models.GetQualityRuleTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQualityRuleTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.rule_task_id):
            query['RuleTaskId'] = request.rule_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQualityRuleTask',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQualityRuleTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_quality_rule_task(
        self,
        request: main_models.GetQualityRuleTaskRequest,
    ) -> main_models.GetQualityRuleTaskResponse:
        runtime = RuntimeOptions()
        return self.get_quality_rule_task_with_options(request, runtime)

    async def get_quality_rule_task_async(
        self,
        request: main_models.GetQualityRuleTaskRequest,
    ) -> main_models.GetQualityRuleTaskResponse:
        runtime = RuntimeOptions()
        return await self.get_quality_rule_task_with_options_async(request, runtime)

    def get_quality_rule_task_log_with_options(
        self,
        request: main_models.GetQualityRuleTaskLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQualityRuleTaskLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.rule_task_id):
            query['RuleTaskId'] = request.rule_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQualityRuleTaskLog',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQualityRuleTaskLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_quality_rule_task_log_with_options_async(
        self,
        request: main_models.GetQualityRuleTaskLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQualityRuleTaskLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.rule_task_id):
            query['RuleTaskId'] = request.rule_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQualityRuleTaskLog',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQualityRuleTaskLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_quality_rule_task_log(
        self,
        request: main_models.GetQualityRuleTaskLogRequest,
    ) -> main_models.GetQualityRuleTaskLogResponse:
        runtime = RuntimeOptions()
        return self.get_quality_rule_task_log_with_options(request, runtime)

    async def get_quality_rule_task_log_async(
        self,
        request: main_models.GetQualityRuleTaskLogRequest,
    ) -> main_models.GetQualityRuleTaskLogResponse:
        runtime = RuntimeOptions()
        return await self.get_quality_rule_task_log_with_options_async(request, runtime)

    def get_quality_schedule_with_options(
        self,
        request: main_models.GetQualityScheduleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQualityScheduleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQualitySchedule',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQualityScheduleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_quality_schedule_with_options_async(
        self,
        request: main_models.GetQualityScheduleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQualityScheduleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQualitySchedule',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQualityScheduleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_quality_schedule(
        self,
        request: main_models.GetQualityScheduleRequest,
    ) -> main_models.GetQualityScheduleResponse:
        runtime = RuntimeOptions()
        return self.get_quality_schedule_with_options(request, runtime)

    async def get_quality_schedule_async(
        self,
        request: main_models.GetQualityScheduleRequest,
    ) -> main_models.GetQualityScheduleResponse:
        runtime = RuntimeOptions()
        return await self.get_quality_schedule_with_options_async(request, runtime)

    def get_quality_schedules_by_watch_id_with_options(
        self,
        request: main_models.GetQualitySchedulesByWatchIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQualitySchedulesByWatchIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.watch_id):
            query['WatchId'] = request.watch_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQualitySchedulesByWatchId',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQualitySchedulesByWatchIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_quality_schedules_by_watch_id_with_options_async(
        self,
        request: main_models.GetQualitySchedulesByWatchIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQualitySchedulesByWatchIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.watch_id):
            query['WatchId'] = request.watch_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQualitySchedulesByWatchId',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQualitySchedulesByWatchIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_quality_schedules_by_watch_id(
        self,
        request: main_models.GetQualitySchedulesByWatchIdRequest,
    ) -> main_models.GetQualitySchedulesByWatchIdResponse:
        runtime = RuntimeOptions()
        return self.get_quality_schedules_by_watch_id_with_options(request, runtime)

    async def get_quality_schedules_by_watch_id_async(
        self,
        request: main_models.GetQualitySchedulesByWatchIdRequest,
    ) -> main_models.GetQualitySchedulesByWatchIdResponse:
        runtime = RuntimeOptions()
        return await self.get_quality_schedules_by_watch_id_with_options_async(request, runtime)

    def get_quality_template_with_options(
        self,
        request: main_models.GetQualityTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQualityTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQualityTemplate',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQualityTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_quality_template_with_options_async(
        self,
        request: main_models.GetQualityTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQualityTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQualityTemplate',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQualityTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_quality_template(
        self,
        request: main_models.GetQualityTemplateRequest,
    ) -> main_models.GetQualityTemplateResponse:
        runtime = RuntimeOptions()
        return self.get_quality_template_with_options(request, runtime)

    async def get_quality_template_async(
        self,
        request: main_models.GetQualityTemplateRequest,
    ) -> main_models.GetQualityTemplateResponse:
        runtime = RuntimeOptions()
        return await self.get_quality_template_with_options_async(request, runtime)

    def get_quality_watch_with_options(
        self,
        request: main_models.GetQualityWatchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQualityWatchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQualityWatch',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQualityWatchResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_quality_watch_with_options_async(
        self,
        request: main_models.GetQualityWatchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQualityWatchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQualityWatch',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQualityWatchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_quality_watch(
        self,
        request: main_models.GetQualityWatchRequest,
    ) -> main_models.GetQualityWatchResponse:
        runtime = RuntimeOptions()
        return self.get_quality_watch_with_options(request, runtime)

    async def get_quality_watch_async(
        self,
        request: main_models.GetQualityWatchRequest,
    ) -> main_models.GetQualityWatchResponse:
        runtime = RuntimeOptions()
        return await self.get_quality_watch_with_options_async(request, runtime)

    def get_quality_watch_by_object_id_with_options(
        self,
        request: main_models.GetQualityWatchByObjectIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQualityWatchByObjectIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.watch_object_id):
            query['WatchObjectId'] = request.watch_object_id
        if not DaraCore.is_null(request.watch_type):
            query['WatchType'] = request.watch_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQualityWatchByObjectId',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQualityWatchByObjectIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_quality_watch_by_object_id_with_options_async(
        self,
        request: main_models.GetQualityWatchByObjectIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQualityWatchByObjectIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.watch_object_id):
            query['WatchObjectId'] = request.watch_object_id
        if not DaraCore.is_null(request.watch_type):
            query['WatchType'] = request.watch_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQualityWatchByObjectId',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQualityWatchByObjectIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_quality_watch_by_object_id(
        self,
        request: main_models.GetQualityWatchByObjectIdRequest,
    ) -> main_models.GetQualityWatchByObjectIdResponse:
        runtime = RuntimeOptions()
        return self.get_quality_watch_by_object_id_with_options(request, runtime)

    async def get_quality_watch_by_object_id_async(
        self,
        request: main_models.GetQualityWatchByObjectIdRequest,
    ) -> main_models.GetQualityWatchByObjectIdResponse:
        runtime = RuntimeOptions()
        return await self.get_quality_watch_by_object_id_with_options_async(request, runtime)

    def get_quality_watch_task_with_options(
        self,
        request: main_models.GetQualityWatchTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQualityWatchTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.watch_task_id):
            query['WatchTaskId'] = request.watch_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQualityWatchTask',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQualityWatchTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_quality_watch_task_with_options_async(
        self,
        request: main_models.GetQualityWatchTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQualityWatchTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.watch_task_id):
            query['WatchTaskId'] = request.watch_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQualityWatchTask',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQualityWatchTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_quality_watch_task(
        self,
        request: main_models.GetQualityWatchTaskRequest,
    ) -> main_models.GetQualityWatchTaskResponse:
        runtime = RuntimeOptions()
        return self.get_quality_watch_task_with_options(request, runtime)

    async def get_quality_watch_task_async(
        self,
        request: main_models.GetQualityWatchTaskRequest,
    ) -> main_models.GetQualityWatchTaskResponse:
        runtime = RuntimeOptions()
        return await self.get_quality_watch_task_with_options_async(request, runtime)

    def get_quality_watch_task_log_with_options(
        self,
        request: main_models.GetQualityWatchTaskLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQualityWatchTaskLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.watch_task_id):
            query['WatchTaskId'] = request.watch_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQualityWatchTaskLog',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQualityWatchTaskLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_quality_watch_task_log_with_options_async(
        self,
        request: main_models.GetQualityWatchTaskLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQualityWatchTaskLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.watch_task_id):
            query['WatchTaskId'] = request.watch_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQualityWatchTaskLog',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQualityWatchTaskLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_quality_watch_task_log(
        self,
        request: main_models.GetQualityWatchTaskLogRequest,
    ) -> main_models.GetQualityWatchTaskLogResponse:
        runtime = RuntimeOptions()
        return self.get_quality_watch_task_log_with_options(request, runtime)

    async def get_quality_watch_task_log_async(
        self,
        request: main_models.GetQualityWatchTaskLogRequest,
    ) -> main_models.GetQualityWatchTaskLogResponse:
        runtime = RuntimeOptions()
        return await self.get_quality_watch_task_log_with_options_async(request, runtime)

    def get_queue_engine_version_by_env_with_options(
        self,
        request: main_models.GetQueueEngineVersionByEnvRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQueueEngineVersionByEnvResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.queue_name):
            query['QueueName'] = request.queue_name
        if not DaraCore.is_null(request.stream_batch_mode):
            query['StreamBatchMode'] = request.stream_batch_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQueueEngineVersionByEnv',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQueueEngineVersionByEnvResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_queue_engine_version_by_env_with_options_async(
        self,
        request: main_models.GetQueueEngineVersionByEnvRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQueueEngineVersionByEnvResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.queue_name):
            query['QueueName'] = request.queue_name
        if not DaraCore.is_null(request.stream_batch_mode):
            query['StreamBatchMode'] = request.stream_batch_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQueueEngineVersionByEnv',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQueueEngineVersionByEnvResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_queue_engine_version_by_env(
        self,
        request: main_models.GetQueueEngineVersionByEnvRequest,
    ) -> main_models.GetQueueEngineVersionByEnvResponse:
        runtime = RuntimeOptions()
        return self.get_queue_engine_version_by_env_with_options(request, runtime)

    async def get_queue_engine_version_by_env_async(
        self,
        request: main_models.GetQueueEngineVersionByEnvRequest,
    ) -> main_models.GetQueueEngineVersionByEnvResponse:
        runtime = RuntimeOptions()
        return await self.get_queue_engine_version_by_env_with_options_async(request, runtime)

    def get_resource_with_options(
        self,
        request: main_models.GetResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResource',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_with_options_async(
        self,
        request: main_models.GetResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResource',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource(
        self,
        request: main_models.GetResourceRequest,
    ) -> main_models.GetResourceResponse:
        runtime = RuntimeOptions()
        return self.get_resource_with_options(request, runtime)

    async def get_resource_async(
        self,
        request: main_models.GetResourceRequest,
    ) -> main_models.GetResourceResponse:
        runtime = RuntimeOptions()
        return await self.get_resource_with_options_async(request, runtime)

    def get_resource_by_version_with_options(
        self,
        request: main_models.GetResourceByVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceByVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceByVersion',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceByVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_by_version_with_options_async(
        self,
        request: main_models.GetResourceByVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceByVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceByVersion',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceByVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_by_version(
        self,
        request: main_models.GetResourceByVersionRequest,
    ) -> main_models.GetResourceByVersionResponse:
        runtime = RuntimeOptions()
        return self.get_resource_by_version_with_options(request, runtime)

    async def get_resource_by_version_async(
        self,
        request: main_models.GetResourceByVersionRequest,
    ) -> main_models.GetResourceByVersionResponse:
        runtime = RuntimeOptions()
        return await self.get_resource_by_version_with_options_async(request, runtime)

    def get_security_classify_with_options(
        self,
        request: main_models.GetSecurityClassifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSecurityClassifyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSecurityClassify',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSecurityClassifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_security_classify_with_options_async(
        self,
        request: main_models.GetSecurityClassifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSecurityClassifyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSecurityClassify',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSecurityClassifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_security_classify(
        self,
        request: main_models.GetSecurityClassifyRequest,
    ) -> main_models.GetSecurityClassifyResponse:
        runtime = RuntimeOptions()
        return self.get_security_classify_with_options(request, runtime)

    async def get_security_classify_async(
        self,
        request: main_models.GetSecurityClassifyRequest,
    ) -> main_models.GetSecurityClassifyResponse:
        runtime = RuntimeOptions()
        return await self.get_security_classify_with_options_async(request, runtime)

    def get_security_identify_result_with_options(
        self,
        request: main_models.GetSecurityIdentifyResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSecurityIdentifyResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSecurityIdentifyResult',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSecurityIdentifyResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_security_identify_result_with_options_async(
        self,
        request: main_models.GetSecurityIdentifyResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSecurityIdentifyResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSecurityIdentifyResult',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSecurityIdentifyResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_security_identify_result(
        self,
        request: main_models.GetSecurityIdentifyResultRequest,
    ) -> main_models.GetSecurityIdentifyResultResponse:
        runtime = RuntimeOptions()
        return self.get_security_identify_result_with_options(request, runtime)

    async def get_security_identify_result_async(
        self,
        request: main_models.GetSecurityIdentifyResultRequest,
    ) -> main_models.GetSecurityIdentifyResultResponse:
        runtime = RuntimeOptions()
        return await self.get_security_identify_result_with_options_async(request, runtime)

    def get_security_level_with_options(
        self,
        request: main_models.GetSecurityLevelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSecurityLevelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.index):
            query['Index'] = request.index
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSecurityLevel',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSecurityLevelResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_security_level_with_options_async(
        self,
        request: main_models.GetSecurityLevelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSecurityLevelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.index):
            query['Index'] = request.index
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSecurityLevel',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSecurityLevelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_security_level(
        self,
        request: main_models.GetSecurityLevelRequest,
    ) -> main_models.GetSecurityLevelResponse:
        runtime = RuntimeOptions()
        return self.get_security_level_with_options(request, runtime)

    async def get_security_level_async(
        self,
        request: main_models.GetSecurityLevelRequest,
    ) -> main_models.GetSecurityLevelResponse:
        runtime = RuntimeOptions()
        return await self.get_security_level_with_options_async(request, runtime)

    def get_security_secret_key_with_options(
        self,
        request: main_models.GetSecuritySecretKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSecuritySecretKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSecuritySecretKey',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSecuritySecretKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_security_secret_key_with_options_async(
        self,
        request: main_models.GetSecuritySecretKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSecuritySecretKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSecuritySecretKey',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSecuritySecretKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_security_secret_key(
        self,
        request: main_models.GetSecuritySecretKeyRequest,
    ) -> main_models.GetSecuritySecretKeyResponse:
        runtime = RuntimeOptions()
        return self.get_security_secret_key_with_options(request, runtime)

    async def get_security_secret_key_async(
        self,
        request: main_models.GetSecuritySecretKeyRequest,
    ) -> main_models.GetSecuritySecretKeyResponse:
        runtime = RuntimeOptions()
        return await self.get_security_secret_key_with_options_async(request, runtime)

    def get_spark_local_client_info_with_options(
        self,
        request: main_models.GetSparkLocalClientInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSparkLocalClientInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.env_enum):
            query['EnvEnum'] = request.env_enum
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSparkLocalClientInfo',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSparkLocalClientInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_spark_local_client_info_with_options_async(
        self,
        request: main_models.GetSparkLocalClientInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSparkLocalClientInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.env_enum):
            query['EnvEnum'] = request.env_enum
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSparkLocalClientInfo',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSparkLocalClientInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_spark_local_client_info(
        self,
        request: main_models.GetSparkLocalClientInfoRequest,
    ) -> main_models.GetSparkLocalClientInfoResponse:
        runtime = RuntimeOptions()
        return self.get_spark_local_client_info_with_options(request, runtime)

    async def get_spark_local_client_info_async(
        self,
        request: main_models.GetSparkLocalClientInfoRequest,
    ) -> main_models.GetSparkLocalClientInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_spark_local_client_info_with_options_async(request, runtime)

    def get_standard_with_options(
        self,
        tmp_req: main_models.GetStandardRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetStandardResponse:
        tmp_req.validate()
        request = main_models.GetStandardShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.standard_get_query):
            request.standard_get_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.standard_get_query, 'StandardGetQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.standard_get_query_shrink):
            body['StandardGetQuery'] = request.standard_get_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetStandard',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStandardResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_standard_with_options_async(
        self,
        tmp_req: main_models.GetStandardRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetStandardResponse:
        tmp_req.validate()
        request = main_models.GetStandardShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.standard_get_query):
            request.standard_get_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.standard_get_query, 'StandardGetQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.standard_get_query_shrink):
            body['StandardGetQuery'] = request.standard_get_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetStandard',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStandardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_standard(
        self,
        request: main_models.GetStandardRequest,
    ) -> main_models.GetStandardResponse:
        runtime = RuntimeOptions()
        return self.get_standard_with_options(request, runtime)

    async def get_standard_async(
        self,
        request: main_models.GetStandardRequest,
    ) -> main_models.GetStandardResponse:
        runtime = RuntimeOptions()
        return await self.get_standard_with_options_async(request, runtime)

    def get_standard_lookup_table_with_options(
        self,
        request: main_models.GetStandardLookupTableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetStandardLookupTableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.nullable):
            query['Nullable'] = request.nullable
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetStandardLookupTable',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStandardLookupTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_standard_lookup_table_with_options_async(
        self,
        request: main_models.GetStandardLookupTableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetStandardLookupTableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.nullable):
            query['Nullable'] = request.nullable
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetStandardLookupTable',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStandardLookupTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_standard_lookup_table(
        self,
        request: main_models.GetStandardLookupTableRequest,
    ) -> main_models.GetStandardLookupTableResponse:
        runtime = RuntimeOptions()
        return self.get_standard_lookup_table_with_options(request, runtime)

    async def get_standard_lookup_table_async(
        self,
        request: main_models.GetStandardLookupTableRequest,
    ) -> main_models.GetStandardLookupTableResponse:
        runtime = RuntimeOptions()
        return await self.get_standard_lookup_table_with_options_async(request, runtime)

    def get_standard_set_with_options(
        self,
        request: main_models.GetStandardSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetStandardSetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.nullable):
            query['Nullable'] = request.nullable
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetStandardSet',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStandardSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_standard_set_with_options_async(
        self,
        request: main_models.GetStandardSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetStandardSetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.nullable):
            query['Nullable'] = request.nullable
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetStandardSet',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStandardSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_standard_set(
        self,
        request: main_models.GetStandardSetRequest,
    ) -> main_models.GetStandardSetResponse:
        runtime = RuntimeOptions()
        return self.get_standard_set_with_options(request, runtime)

    async def get_standard_set_async(
        self,
        request: main_models.GetStandardSetRequest,
    ) -> main_models.GetStandardSetResponse:
        runtime = RuntimeOptions()
        return await self.get_standard_set_with_options_async(request, runtime)

    def get_standard_statistics_with_options(
        self,
        tmp_req: main_models.GetStandardStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetStandardStatisticsResponse:
        tmp_req.validate()
        request = main_models.GetStandardStatisticsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.statistics_query):
            request.statistics_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.statistics_query, 'StatisticsQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.statistics_query_shrink):
            body['StatisticsQuery'] = request.statistics_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetStandardStatistics',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStandardStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_standard_statistics_with_options_async(
        self,
        tmp_req: main_models.GetStandardStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetStandardStatisticsResponse:
        tmp_req.validate()
        request = main_models.GetStandardStatisticsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.statistics_query):
            request.statistics_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.statistics_query, 'StatisticsQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.statistics_query_shrink):
            body['StatisticsQuery'] = request.statistics_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetStandardStatistics',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStandardStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_standard_statistics(
        self,
        request: main_models.GetStandardStatisticsRequest,
    ) -> main_models.GetStandardStatisticsResponse:
        runtime = RuntimeOptions()
        return self.get_standard_statistics_with_options(request, runtime)

    async def get_standard_statistics_async(
        self,
        request: main_models.GetStandardStatisticsRequest,
    ) -> main_models.GetStandardStatisticsResponse:
        runtime = RuntimeOptions()
        return await self.get_standard_statistics_with_options_async(request, runtime)

    def get_standard_template_with_options(
        self,
        tmp_req: main_models.GetStandardTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetStandardTemplateResponse:
        tmp_req.validate()
        request = main_models.GetStandardTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter_query):
            request.filter_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter_query, 'FilterQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.nullable):
            query['Nullable'] = request.nullable
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.filter_query_shrink):
            body['FilterQuery'] = request.filter_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetStandardTemplate',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStandardTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_standard_template_with_options_async(
        self,
        tmp_req: main_models.GetStandardTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetStandardTemplateResponse:
        tmp_req.validate()
        request = main_models.GetStandardTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter_query):
            request.filter_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter_query, 'FilterQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.nullable):
            query['Nullable'] = request.nullable
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.filter_query_shrink):
            body['FilterQuery'] = request.filter_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetStandardTemplate',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStandardTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_standard_template(
        self,
        request: main_models.GetStandardTemplateRequest,
    ) -> main_models.GetStandardTemplateResponse:
        runtime = RuntimeOptions()
        return self.get_standard_template_with_options(request, runtime)

    async def get_standard_template_async(
        self,
        request: main_models.GetStandardTemplateRequest,
    ) -> main_models.GetStandardTemplateResponse:
        runtime = RuntimeOptions()
        return await self.get_standard_template_with_options_async(request, runtime)

    def get_standard_word_root_with_options(
        self,
        request: main_models.GetStandardWordRootRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetStandardWordRootResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.nullable):
            query['Nullable'] = request.nullable
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetStandardWordRoot',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStandardWordRootResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_standard_word_root_with_options_async(
        self,
        request: main_models.GetStandardWordRootRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetStandardWordRootResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.nullable):
            query['Nullable'] = request.nullable
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetStandardWordRoot',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStandardWordRootResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_standard_word_root(
        self,
        request: main_models.GetStandardWordRootRequest,
    ) -> main_models.GetStandardWordRootResponse:
        runtime = RuntimeOptions()
        return self.get_standard_word_root_with_options(request, runtime)

    async def get_standard_word_root_async(
        self,
        request: main_models.GetStandardWordRootRequest,
    ) -> main_models.GetStandardWordRootResponse:
        runtime = RuntimeOptions()
        return await self.get_standard_word_root_with_options_async(request, runtime)

    def get_stream_jobs_with_options(
        self,
        request: main_models.GetStreamJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetStreamJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetStreamJobs',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStreamJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_stream_jobs_with_options_async(
        self,
        request: main_models.GetStreamJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetStreamJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetStreamJobs',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStreamJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_stream_jobs(
        self,
        request: main_models.GetStreamJobsRequest,
    ) -> main_models.GetStreamJobsResponse:
        runtime = RuntimeOptions()
        return self.get_stream_jobs_with_options(request, runtime)

    async def get_stream_jobs_async(
        self,
        request: main_models.GetStreamJobsRequest,
    ) -> main_models.GetStreamJobsResponse:
        runtime = RuntimeOptions()
        return await self.get_stream_jobs_with_options_async(request, runtime)

    def get_supplement_dagrun_with_options(
        self,
        request: main_models.GetSupplementDagrunRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSupplementDagrunResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.supplement_id):
            query['SupplementId'] = request.supplement_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSupplementDagrun',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSupplementDagrunResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_supplement_dagrun_with_options_async(
        self,
        request: main_models.GetSupplementDagrunRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSupplementDagrunResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.supplement_id):
            query['SupplementId'] = request.supplement_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSupplementDagrun',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSupplementDagrunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_supplement_dagrun(
        self,
        request: main_models.GetSupplementDagrunRequest,
    ) -> main_models.GetSupplementDagrunResponse:
        runtime = RuntimeOptions()
        return self.get_supplement_dagrun_with_options(request, runtime)

    async def get_supplement_dagrun_async(
        self,
        request: main_models.GetSupplementDagrunRequest,
    ) -> main_models.GetSupplementDagrunResponse:
        runtime = RuntimeOptions()
        return await self.get_supplement_dagrun_with_options_async(request, runtime)

    def get_supplement_dagrun_instance_with_options(
        self,
        request: main_models.GetSupplementDagrunInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSupplementDagrunInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dagrun_id):
            query['DagrunId'] = request.dagrun_id
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSupplementDagrunInstance',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSupplementDagrunInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_supplement_dagrun_instance_with_options_async(
        self,
        request: main_models.GetSupplementDagrunInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSupplementDagrunInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dagrun_id):
            query['DagrunId'] = request.dagrun_id
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSupplementDagrunInstance',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSupplementDagrunInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_supplement_dagrun_instance(
        self,
        request: main_models.GetSupplementDagrunInstanceRequest,
    ) -> main_models.GetSupplementDagrunInstanceResponse:
        runtime = RuntimeOptions()
        return self.get_supplement_dagrun_instance_with_options(request, runtime)

    async def get_supplement_dagrun_instance_async(
        self,
        request: main_models.GetSupplementDagrunInstanceRequest,
    ) -> main_models.GetSupplementDagrunInstanceResponse:
        runtime = RuntimeOptions()
        return await self.get_supplement_dagrun_instance_with_options_async(request, runtime)

    def get_table_column_lineage_by_task_id_with_options(
        self,
        tmp_req: main_models.GetTableColumnLineageByTaskIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTableColumnLineageByTaskIdResponse:
        tmp_req.validate()
        request = main_models.GetTableColumnLineageByTaskIdShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.table_column_lineage_by_task_id_query):
            request.table_column_lineage_by_task_id_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.table_column_lineage_by_task_id_query, 'TableColumnLineageByTaskIdQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.table_column_lineage_by_task_id_query_shrink):
            body['TableColumnLineageByTaskIdQuery'] = request.table_column_lineage_by_task_id_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetTableColumnLineageByTaskId',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTableColumnLineageByTaskIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_table_column_lineage_by_task_id_with_options_async(
        self,
        tmp_req: main_models.GetTableColumnLineageByTaskIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTableColumnLineageByTaskIdResponse:
        tmp_req.validate()
        request = main_models.GetTableColumnLineageByTaskIdShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.table_column_lineage_by_task_id_query):
            request.table_column_lineage_by_task_id_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.table_column_lineage_by_task_id_query, 'TableColumnLineageByTaskIdQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.table_column_lineage_by_task_id_query_shrink):
            body['TableColumnLineageByTaskIdQuery'] = request.table_column_lineage_by_task_id_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetTableColumnLineageByTaskId',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTableColumnLineageByTaskIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_table_column_lineage_by_task_id(
        self,
        request: main_models.GetTableColumnLineageByTaskIdRequest,
    ) -> main_models.GetTableColumnLineageByTaskIdResponse:
        runtime = RuntimeOptions()
        return self.get_table_column_lineage_by_task_id_with_options(request, runtime)

    async def get_table_column_lineage_by_task_id_async(
        self,
        request: main_models.GetTableColumnLineageByTaskIdRequest,
    ) -> main_models.GetTableColumnLineageByTaskIdResponse:
        runtime = RuntimeOptions()
        return await self.get_table_column_lineage_by_task_id_with_options_async(request, runtime)

    def get_table_column_lineages_with_options(
        self,
        tmp_req: main_models.GetTableColumnLineagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTableColumnLineagesResponse:
        tmp_req.validate()
        request = main_models.GetTableColumnLineagesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter_query):
            request.filter_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter_query, 'FilterQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.table_guid):
            query['TableGuid'] = request.table_guid
        body = {}
        if not DaraCore.is_null(request.filter_query_shrink):
            body['FilterQuery'] = request.filter_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetTableColumnLineages',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTableColumnLineagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_table_column_lineages_with_options_async(
        self,
        tmp_req: main_models.GetTableColumnLineagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTableColumnLineagesResponse:
        tmp_req.validate()
        request = main_models.GetTableColumnLineagesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter_query):
            request.filter_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter_query, 'FilterQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.table_guid):
            query['TableGuid'] = request.table_guid
        body = {}
        if not DaraCore.is_null(request.filter_query_shrink):
            body['FilterQuery'] = request.filter_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetTableColumnLineages',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTableColumnLineagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_table_column_lineages(
        self,
        request: main_models.GetTableColumnLineagesRequest,
    ) -> main_models.GetTableColumnLineagesResponse:
        runtime = RuntimeOptions()
        return self.get_table_column_lineages_with_options(request, runtime)

    async def get_table_column_lineages_async(
        self,
        request: main_models.GetTableColumnLineagesRequest,
    ) -> main_models.GetTableColumnLineagesResponse:
        runtime = RuntimeOptions()
        return await self.get_table_column_lineages_with_options_async(request, runtime)

    def get_table_columns_with_options(
        self,
        request: main_models.GetTableColumnsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTableColumnsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog):
            query['Catalog'] = request.catalog
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTableColumns',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTableColumnsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_table_columns_with_options_async(
        self,
        request: main_models.GetTableColumnsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTableColumnsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog):
            query['Catalog'] = request.catalog
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTableColumns',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTableColumnsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_table_columns(
        self,
        request: main_models.GetTableColumnsRequest,
    ) -> main_models.GetTableColumnsResponse:
        runtime = RuntimeOptions()
        return self.get_table_columns_with_options(request, runtime)

    async def get_table_columns_async(
        self,
        request: main_models.GetTableColumnsRequest,
    ) -> main_models.GetTableColumnsResponse:
        runtime = RuntimeOptions()
        return await self.get_table_columns_with_options_async(request, runtime)

    def get_table_lineage_by_task_id_with_options(
        self,
        tmp_req: main_models.GetTableLineageByTaskIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTableLineageByTaskIdResponse:
        tmp_req.validate()
        request = main_models.GetTableLineageByTaskIdShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.table_lineage_by_task_id_query):
            request.table_lineage_by_task_id_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.table_lineage_by_task_id_query, 'TableLineageByTaskIdQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.table_lineage_by_task_id_query_shrink):
            body['TableLineageByTaskIdQuery'] = request.table_lineage_by_task_id_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetTableLineageByTaskId',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTableLineageByTaskIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_table_lineage_by_task_id_with_options_async(
        self,
        tmp_req: main_models.GetTableLineageByTaskIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTableLineageByTaskIdResponse:
        tmp_req.validate()
        request = main_models.GetTableLineageByTaskIdShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.table_lineage_by_task_id_query):
            request.table_lineage_by_task_id_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.table_lineage_by_task_id_query, 'TableLineageByTaskIdQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.table_lineage_by_task_id_query_shrink):
            body['TableLineageByTaskIdQuery'] = request.table_lineage_by_task_id_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetTableLineageByTaskId',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTableLineageByTaskIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_table_lineage_by_task_id(
        self,
        request: main_models.GetTableLineageByTaskIdRequest,
    ) -> main_models.GetTableLineageByTaskIdResponse:
        runtime = RuntimeOptions()
        return self.get_table_lineage_by_task_id_with_options(request, runtime)

    async def get_table_lineage_by_task_id_async(
        self,
        request: main_models.GetTableLineageByTaskIdRequest,
    ) -> main_models.GetTableLineageByTaskIdResponse:
        runtime = RuntimeOptions()
        return await self.get_table_lineage_by_task_id_with_options_async(request, runtime)

    def get_table_lineages_with_options(
        self,
        tmp_req: main_models.GetTableLineagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTableLineagesResponse:
        tmp_req.validate()
        request = main_models.GetTableLineagesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter_query):
            request.filter_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter_query, 'FilterQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.table_guid):
            query['TableGuid'] = request.table_guid
        body = {}
        if not DaraCore.is_null(request.filter_query_shrink):
            body['FilterQuery'] = request.filter_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetTableLineages',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTableLineagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_table_lineages_with_options_async(
        self,
        tmp_req: main_models.GetTableLineagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTableLineagesResponse:
        tmp_req.validate()
        request = main_models.GetTableLineagesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter_query):
            request.filter_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter_query, 'FilterQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.table_guid):
            query['TableGuid'] = request.table_guid
        body = {}
        if not DaraCore.is_null(request.filter_query_shrink):
            body['FilterQuery'] = request.filter_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetTableLineages',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTableLineagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_table_lineages(
        self,
        request: main_models.GetTableLineagesRequest,
    ) -> main_models.GetTableLineagesResponse:
        runtime = RuntimeOptions()
        return self.get_table_lineages_with_options(request, runtime)

    async def get_table_lineages_async(
        self,
        request: main_models.GetTableLineagesRequest,
    ) -> main_models.GetTableLineagesResponse:
        runtime = RuntimeOptions()
        return await self.get_table_lineages_with_options_async(request, runtime)

    def get_transfer_info_with_options(
        self,
        request: main_models.GetTransferInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTransferInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.proposal_id):
            query['ProposalId'] = request.proposal_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTransferInfo',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTransferInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_transfer_info_with_options_async(
        self,
        request: main_models.GetTransferInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTransferInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.proposal_id):
            query['ProposalId'] = request.proposal_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTransferInfo',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTransferInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_transfer_info(
        self,
        request: main_models.GetTransferInfoRequest,
    ) -> main_models.GetTransferInfoResponse:
        runtime = RuntimeOptions()
        return self.get_transfer_info_with_options(request, runtime)

    async def get_transfer_info_async(
        self,
        request: main_models.GetTransferInfoRequest,
    ) -> main_models.GetTransferInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_transfer_info_with_options_async(request, runtime)

    def get_udf_with_options(
        self,
        request: main_models.GetUdfRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUdfResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUdf',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUdfResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_udf_with_options_async(
        self,
        request: main_models.GetUdfRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUdfResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUdf',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUdfResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_udf(
        self,
        request: main_models.GetUdfRequest,
    ) -> main_models.GetUdfResponse:
        runtime = RuntimeOptions()
        return self.get_udf_with_options(request, runtime)

    async def get_udf_async(
        self,
        request: main_models.GetUdfRequest,
    ) -> main_models.GetUdfResponse:
        runtime = RuntimeOptions()
        return await self.get_udf_with_options_async(request, runtime)

    def get_udf_by_version_with_options(
        self,
        request: main_models.GetUdfByVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUdfByVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUdfByVersion',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUdfByVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_udf_by_version_with_options_async(
        self,
        request: main_models.GetUdfByVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUdfByVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUdfByVersion',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUdfByVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_udf_by_version(
        self,
        request: main_models.GetUdfByVersionRequest,
    ) -> main_models.GetUdfByVersionResponse:
        runtime = RuntimeOptions()
        return self.get_udf_by_version_with_options(request, runtime)

    async def get_udf_by_version_async(
        self,
        request: main_models.GetUdfByVersionRequest,
    ) -> main_models.GetUdfByVersionResponse:
        runtime = RuntimeOptions()
        return await self.get_udf_by_version_with_options_async(request, runtime)

    def get_user_by_source_id_with_options(
        self,
        request: main_models.GetUserBySourceIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserBySourceIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.source_id):
            query['SourceId'] = request.source_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserBySourceId',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserBySourceIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_by_source_id_with_options_async(
        self,
        request: main_models.GetUserBySourceIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserBySourceIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.source_id):
            query['SourceId'] = request.source_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserBySourceId',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserBySourceIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_by_source_id(
        self,
        request: main_models.GetUserBySourceIdRequest,
    ) -> main_models.GetUserBySourceIdResponse:
        runtime = RuntimeOptions()
        return self.get_user_by_source_id_with_options(request, runtime)

    async def get_user_by_source_id_async(
        self,
        request: main_models.GetUserBySourceIdRequest,
    ) -> main_models.GetUserBySourceIdResponse:
        runtime = RuntimeOptions()
        return await self.get_user_by_source_id_with_options_async(request, runtime)

    def get_user_group_with_options(
        self,
        request: main_models.GetUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserGroup',
            version = '2023-06-30',
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
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserGroup',
            version = '2023-06-30',
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

    def get_users_with_options(
        self,
        tmp_req: main_models.GetUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUsersResponse:
        tmp_req.validate()
        request = main_models.GetUsersShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user_id_list):
            request.user_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_id_list, 'UserIdList', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.user_id_list_shrink):
            body['UserIdList'] = request.user_id_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetUsers',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_users_with_options_async(
        self,
        tmp_req: main_models.GetUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUsersResponse:
        tmp_req.validate()
        request = main_models.GetUsersShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user_id_list):
            request.user_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_id_list, 'UserIdList', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.user_id_list_shrink):
            body['UserIdList'] = request.user_id_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetUsers',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_users(
        self,
        request: main_models.GetUsersRequest,
    ) -> main_models.GetUsersResponse:
        runtime = RuntimeOptions()
        return self.get_users_with_options(request, runtime)

    async def get_users_async(
        self,
        request: main_models.GetUsersRequest,
    ) -> main_models.GetUsersResponse:
        runtime = RuntimeOptions()
        return await self.get_users_with_options_async(request, runtime)

    def grant_data_service_api_with_options(
        self,
        tmp_req: main_models.GrantDataServiceApiRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GrantDataServiceApiResponse:
        tmp_req.validate()
        request = main_models.GrantDataServiceApiShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.grant_command):
            request.grant_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.grant_command, 'GrantCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        body = {}
        if not DaraCore.is_null(request.grant_command_shrink):
            body['GrantCommand'] = request.grant_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GrantDataServiceApi',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GrantDataServiceApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def grant_data_service_api_with_options_async(
        self,
        tmp_req: main_models.GrantDataServiceApiRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GrantDataServiceApiResponse:
        tmp_req.validate()
        request = main_models.GrantDataServiceApiShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.grant_command):
            request.grant_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.grant_command, 'GrantCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        body = {}
        if not DaraCore.is_null(request.grant_command_shrink):
            body['GrantCommand'] = request.grant_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GrantDataServiceApi',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GrantDataServiceApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def grant_data_service_api(
        self,
        request: main_models.GrantDataServiceApiRequest,
    ) -> main_models.GrantDataServiceApiResponse:
        runtime = RuntimeOptions()
        return self.grant_data_service_api_with_options(request, runtime)

    async def grant_data_service_api_async(
        self,
        request: main_models.GrantDataServiceApiRequest,
    ) -> main_models.GrantDataServiceApiResponse:
        runtime = RuntimeOptions()
        return await self.grant_data_service_api_with_options_async(request, runtime)

    def grant_resource_permission_with_options(
        self,
        tmp_req: main_models.GrantResourcePermissionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GrantResourcePermissionResponse:
        tmp_req.validate()
        request = main_models.GrantResourcePermissionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.grant_command):
            request.grant_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.grant_command, 'GrantCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.grant_command_shrink):
            body['GrantCommand'] = request.grant_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GrantResourcePermission',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GrantResourcePermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def grant_resource_permission_with_options_async(
        self,
        tmp_req: main_models.GrantResourcePermissionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GrantResourcePermissionResponse:
        tmp_req.validate()
        request = main_models.GrantResourcePermissionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.grant_command):
            request.grant_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.grant_command, 'GrantCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.grant_command_shrink):
            body['GrantCommand'] = request.grant_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GrantResourcePermission',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GrantResourcePermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def grant_resource_permission(
        self,
        request: main_models.GrantResourcePermissionRequest,
    ) -> main_models.GrantResourcePermissionResponse:
        runtime = RuntimeOptions()
        return self.grant_resource_permission_with_options(request, runtime)

    async def grant_resource_permission_async(
        self,
        request: main_models.GrantResourcePermissionRequest,
    ) -> main_models.GrantResourcePermissionResponse:
        runtime = RuntimeOptions()
        return await self.grant_resource_permission_with_options_async(request, runtime)

    def list_addable_roles_with_options(
        self,
        request: main_models.ListAddableRolesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAddableRolesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAddableRoles',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAddableRolesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_addable_roles_with_options_async(
        self,
        request: main_models.ListAddableRolesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAddableRolesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAddableRoles',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAddableRolesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_addable_roles(
        self,
        request: main_models.ListAddableRolesRequest,
    ) -> main_models.ListAddableRolesResponse:
        runtime = RuntimeOptions()
        return self.list_addable_roles_with_options(request, runtime)

    async def list_addable_roles_async(
        self,
        request: main_models.ListAddableRolesRequest,
    ) -> main_models.ListAddableRolesResponse:
        runtime = RuntimeOptions()
        return await self.list_addable_roles_with_options_async(request, runtime)

    def list_addable_users_with_options(
        self,
        tmp_req: main_models.ListAddableUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAddableUsersResponse:
        tmp_req.validate()
        request = main_models.ListAddableUsersShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAddableUsers',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAddableUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_addable_users_with_options_async(
        self,
        tmp_req: main_models.ListAddableUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAddableUsersResponse:
        tmp_req.validate()
        request = main_models.ListAddableUsersShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAddableUsers',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAddableUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_addable_users(
        self,
        request: main_models.ListAddableUsersRequest,
    ) -> main_models.ListAddableUsersResponse:
        runtime = RuntimeOptions()
        return self.list_addable_users_with_options(request, runtime)

    async def list_addable_users_async(
        self,
        request: main_models.ListAddableUsersRequest,
    ) -> main_models.ListAddableUsersResponse:
        runtime = RuntimeOptions()
        return await self.list_addable_users_with_options_async(request, runtime)

    def list_alert_events_with_options(
        self,
        tmp_req: main_models.ListAlertEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAlertEventsResponse:
        tmp_req.validate()
        request = main_models.ListAlertEventsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAlertEvents',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAlertEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_alert_events_with_options_async(
        self,
        tmp_req: main_models.ListAlertEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAlertEventsResponse:
        tmp_req.validate()
        request = main_models.ListAlertEventsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAlertEvents',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAlertEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_alert_events(
        self,
        request: main_models.ListAlertEventsRequest,
    ) -> main_models.ListAlertEventsResponse:
        runtime = RuntimeOptions()
        return self.list_alert_events_with_options(request, runtime)

    async def list_alert_events_async(
        self,
        request: main_models.ListAlertEventsRequest,
    ) -> main_models.ListAlertEventsResponse:
        runtime = RuntimeOptions()
        return await self.list_alert_events_with_options_async(request, runtime)

    def list_alert_notifications_with_options(
        self,
        tmp_req: main_models.ListAlertNotificationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAlertNotificationsResponse:
        tmp_req.validate()
        request = main_models.ListAlertNotificationsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAlertNotifications',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAlertNotificationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_alert_notifications_with_options_async(
        self,
        tmp_req: main_models.ListAlertNotificationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAlertNotificationsResponse:
        tmp_req.validate()
        request = main_models.ListAlertNotificationsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAlertNotifications',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAlertNotificationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_alert_notifications(
        self,
        request: main_models.ListAlertNotificationsRequest,
    ) -> main_models.ListAlertNotificationsResponse:
        runtime = RuntimeOptions()
        return self.list_alert_notifications_with_options(request, runtime)

    async def list_alert_notifications_async(
        self,
        request: main_models.ListAlertNotificationsRequest,
    ) -> main_models.ListAlertNotificationsResponse:
        runtime = RuntimeOptions()
        return await self.list_alert_notifications_with_options_async(request, runtime)

    def list_api_by_app_with_options(
        self,
        tmp_req: main_models.ListApiByAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApiByAppResponse:
        tmp_req.validate()
        request = main_models.ListApiByAppShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.page_query):
            request.page_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.page_query, 'PageQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.page_query_shrink):
            body['PageQuery'] = request.page_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListApiByApp',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApiByAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_api_by_app_with_options_async(
        self,
        tmp_req: main_models.ListApiByAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApiByAppResponse:
        tmp_req.validate()
        request = main_models.ListApiByAppShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.page_query):
            request.page_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.page_query, 'PageQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.page_query_shrink):
            body['PageQuery'] = request.page_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListApiByApp',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApiByAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_api_by_app(
        self,
        request: main_models.ListApiByAppRequest,
    ) -> main_models.ListApiByAppResponse:
        runtime = RuntimeOptions()
        return self.list_api_by_app_with_options(request, runtime)

    async def list_api_by_app_async(
        self,
        request: main_models.ListApiByAppRequest,
    ) -> main_models.ListApiByAppResponse:
        runtime = RuntimeOptions()
        return await self.list_api_by_app_with_options_async(request, runtime)

    def list_authorized_data_service_api_details_with_options(
        self,
        tmp_req: main_models.ListAuthorizedDataServiceApiDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAuthorizedDataServiceApiDetailsResponse:
        tmp_req.validate()
        request = main_models.ListAuthorizedDataServiceApiDetailsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAuthorizedDataServiceApiDetails',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAuthorizedDataServiceApiDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_authorized_data_service_api_details_with_options_async(
        self,
        tmp_req: main_models.ListAuthorizedDataServiceApiDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAuthorizedDataServiceApiDetailsResponse:
        tmp_req.validate()
        request = main_models.ListAuthorizedDataServiceApiDetailsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListAuthorizedDataServiceApiDetails',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAuthorizedDataServiceApiDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_authorized_data_service_api_details(
        self,
        request: main_models.ListAuthorizedDataServiceApiDetailsRequest,
    ) -> main_models.ListAuthorizedDataServiceApiDetailsResponse:
        runtime = RuntimeOptions()
        return self.list_authorized_data_service_api_details_with_options(request, runtime)

    async def list_authorized_data_service_api_details_async(
        self,
        request: main_models.ListAuthorizedDataServiceApiDetailsRequest,
    ) -> main_models.ListAuthorizedDataServiceApiDetailsResponse:
        runtime = RuntimeOptions()
        return await self.list_authorized_data_service_api_details_with_options_async(request, runtime)

    def list_biz_entities_with_options(
        self,
        tmp_req: main_models.ListBizEntitiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBizEntitiesResponse:
        tmp_req.validate()
        request = main_models.ListBizEntitiesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListBizEntities',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBizEntitiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_biz_entities_with_options_async(
        self,
        tmp_req: main_models.ListBizEntitiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBizEntitiesResponse:
        tmp_req.validate()
        request = main_models.ListBizEntitiesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListBizEntities',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBizEntitiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_biz_entities(
        self,
        request: main_models.ListBizEntitiesRequest,
    ) -> main_models.ListBizEntitiesResponse:
        runtime = RuntimeOptions()
        return self.list_biz_entities_with_options(request, runtime)

    async def list_biz_entities_async(
        self,
        request: main_models.ListBizEntitiesRequest,
    ) -> main_models.ListBizEntitiesResponse:
        runtime = RuntimeOptions()
        return await self.list_biz_entities_with_options_async(request, runtime)

    def list_biz_units_with_options(
        self,
        request: main_models.ListBizUnitsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBizUnitsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBizUnits',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBizUnitsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_biz_units_with_options_async(
        self,
        request: main_models.ListBizUnitsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBizUnitsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBizUnits',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBizUnitsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_biz_units(
        self,
        request: main_models.ListBizUnitsRequest,
    ) -> main_models.ListBizUnitsResponse:
        runtime = RuntimeOptions()
        return self.list_biz_units_with_options(request, runtime)

    async def list_biz_units_async(
        self,
        request: main_models.ListBizUnitsRequest,
    ) -> main_models.ListBizUnitsResponse:
        runtime = RuntimeOptions()
        return await self.list_biz_units_with_options_async(request, runtime)

    def list_compute_sources_with_options(
        self,
        tmp_req: main_models.ListComputeSourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListComputeSourcesResponse:
        tmp_req.validate()
        request = main_models.ListComputeSourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListComputeSources',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListComputeSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_compute_sources_with_options_async(
        self,
        tmp_req: main_models.ListComputeSourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListComputeSourcesResponse:
        tmp_req.validate()
        request = main_models.ListComputeSourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListComputeSources',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListComputeSourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_compute_sources(
        self,
        request: main_models.ListComputeSourcesRequest,
    ) -> main_models.ListComputeSourcesResponse:
        runtime = RuntimeOptions()
        return self.list_compute_sources_with_options(request, runtime)

    async def list_compute_sources_async(
        self,
        request: main_models.ListComputeSourcesRequest,
    ) -> main_models.ListComputeSourcesResponse:
        runtime = RuntimeOptions()
        return await self.list_compute_sources_with_options_async(request, runtime)

    def list_data_domains_with_options(
        self,
        tmp_req: main_models.ListDataDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataDomainsResponse:
        tmp_req.validate()
        request = main_models.ListDataDomainsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDataDomains',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_domains_with_options_async(
        self,
        tmp_req: main_models.ListDataDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataDomainsResponse:
        tmp_req.validate()
        request = main_models.ListDataDomainsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDataDomains',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_domains(
        self,
        request: main_models.ListDataDomainsRequest,
    ) -> main_models.ListDataDomainsResponse:
        runtime = RuntimeOptions()
        return self.list_data_domains_with_options(request, runtime)

    async def list_data_domains_async(
        self,
        request: main_models.ListDataDomainsRequest,
    ) -> main_models.ListDataDomainsResponse:
        runtime = RuntimeOptions()
        return await self.list_data_domains_with_options_async(request, runtime)

    def list_data_service_api_call_statistics_with_options(
        self,
        tmp_req: main_models.ListDataServiceApiCallStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataServiceApiCallStatisticsResponse:
        tmp_req.validate()
        request = main_models.ListDataServiceApiCallStatisticsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDataServiceApiCallStatistics',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataServiceApiCallStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_service_api_call_statistics_with_options_async(
        self,
        tmp_req: main_models.ListDataServiceApiCallStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataServiceApiCallStatisticsResponse:
        tmp_req.validate()
        request = main_models.ListDataServiceApiCallStatisticsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDataServiceApiCallStatistics',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataServiceApiCallStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_service_api_call_statistics(
        self,
        request: main_models.ListDataServiceApiCallStatisticsRequest,
    ) -> main_models.ListDataServiceApiCallStatisticsResponse:
        runtime = RuntimeOptions()
        return self.list_data_service_api_call_statistics_with_options(request, runtime)

    async def list_data_service_api_call_statistics_async(
        self,
        request: main_models.ListDataServiceApiCallStatisticsRequest,
    ) -> main_models.ListDataServiceApiCallStatisticsResponse:
        runtime = RuntimeOptions()
        return await self.list_data_service_api_call_statistics_with_options_async(request, runtime)

    def list_data_service_api_calls_with_options(
        self,
        tmp_req: main_models.ListDataServiceApiCallsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataServiceApiCallsResponse:
        tmp_req.validate()
        request = main_models.ListDataServiceApiCallsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDataServiceApiCalls',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataServiceApiCallsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_service_api_calls_with_options_async(
        self,
        tmp_req: main_models.ListDataServiceApiCallsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataServiceApiCallsResponse:
        tmp_req.validate()
        request = main_models.ListDataServiceApiCallsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDataServiceApiCalls',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataServiceApiCallsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_service_api_calls(
        self,
        request: main_models.ListDataServiceApiCallsRequest,
    ) -> main_models.ListDataServiceApiCallsResponse:
        runtime = RuntimeOptions()
        return self.list_data_service_api_calls_with_options(request, runtime)

    async def list_data_service_api_calls_async(
        self,
        request: main_models.ListDataServiceApiCallsRequest,
    ) -> main_models.ListDataServiceApiCallsResponse:
        runtime = RuntimeOptions()
        return await self.list_data_service_api_calls_with_options_async(request, runtime)

    def list_data_service_api_impacts_with_options(
        self,
        tmp_req: main_models.ListDataServiceApiImpactsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataServiceApiImpactsResponse:
        tmp_req.validate()
        request = main_models.ListDataServiceApiImpactsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDataServiceApiImpacts',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataServiceApiImpactsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_service_api_impacts_with_options_async(
        self,
        tmp_req: main_models.ListDataServiceApiImpactsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataServiceApiImpactsResponse:
        tmp_req.validate()
        request = main_models.ListDataServiceApiImpactsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDataServiceApiImpacts',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataServiceApiImpactsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_service_api_impacts(
        self,
        request: main_models.ListDataServiceApiImpactsRequest,
    ) -> main_models.ListDataServiceApiImpactsResponse:
        runtime = RuntimeOptions()
        return self.list_data_service_api_impacts_with_options(request, runtime)

    async def list_data_service_api_impacts_async(
        self,
        request: main_models.ListDataServiceApiImpactsRequest,
    ) -> main_models.ListDataServiceApiImpactsResponse:
        runtime = RuntimeOptions()
        return await self.list_data_service_api_impacts_with_options_async(request, runtime)

    def list_data_service_authorized_apps_with_options(
        self,
        tmp_req: main_models.ListDataServiceAuthorizedAppsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataServiceAuthorizedAppsResponse:
        tmp_req.validate()
        request = main_models.ListDataServiceAuthorizedAppsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDataServiceAuthorizedApps',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataServiceAuthorizedAppsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_service_authorized_apps_with_options_async(
        self,
        tmp_req: main_models.ListDataServiceAuthorizedAppsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataServiceAuthorizedAppsResponse:
        tmp_req.validate()
        request = main_models.ListDataServiceAuthorizedAppsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDataServiceAuthorizedApps',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataServiceAuthorizedAppsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_service_authorized_apps(
        self,
        request: main_models.ListDataServiceAuthorizedAppsRequest,
    ) -> main_models.ListDataServiceAuthorizedAppsResponse:
        runtime = RuntimeOptions()
        return self.list_data_service_authorized_apps_with_options(request, runtime)

    async def list_data_service_authorized_apps_async(
        self,
        request: main_models.ListDataServiceAuthorizedAppsRequest,
    ) -> main_models.ListDataServiceAuthorizedAppsResponse:
        runtime = RuntimeOptions()
        return await self.list_data_service_authorized_apps_with_options_async(request, runtime)

    def list_data_service_my_api_permissions_with_options(
        self,
        tmp_req: main_models.ListDataServiceMyApiPermissionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataServiceMyApiPermissionsResponse:
        tmp_req.validate()
        request = main_models.ListDataServiceMyApiPermissionsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDataServiceMyApiPermissions',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataServiceMyApiPermissionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_service_my_api_permissions_with_options_async(
        self,
        tmp_req: main_models.ListDataServiceMyApiPermissionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataServiceMyApiPermissionsResponse:
        tmp_req.validate()
        request = main_models.ListDataServiceMyApiPermissionsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDataServiceMyApiPermissions',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataServiceMyApiPermissionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_service_my_api_permissions(
        self,
        request: main_models.ListDataServiceMyApiPermissionsRequest,
    ) -> main_models.ListDataServiceMyApiPermissionsResponse:
        runtime = RuntimeOptions()
        return self.list_data_service_my_api_permissions_with_options(request, runtime)

    async def list_data_service_my_api_permissions_async(
        self,
        request: main_models.ListDataServiceMyApiPermissionsRequest,
    ) -> main_models.ListDataServiceMyApiPermissionsResponse:
        runtime = RuntimeOptions()
        return await self.list_data_service_my_api_permissions_with_options_async(request, runtime)

    def list_data_service_my_app_permissions_with_options(
        self,
        tmp_req: main_models.ListDataServiceMyAppPermissionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataServiceMyAppPermissionsResponse:
        tmp_req.validate()
        request = main_models.ListDataServiceMyAppPermissionsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDataServiceMyAppPermissions',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataServiceMyAppPermissionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_service_my_app_permissions_with_options_async(
        self,
        tmp_req: main_models.ListDataServiceMyAppPermissionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataServiceMyAppPermissionsResponse:
        tmp_req.validate()
        request = main_models.ListDataServiceMyAppPermissionsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDataServiceMyAppPermissions',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataServiceMyAppPermissionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_service_my_app_permissions(
        self,
        request: main_models.ListDataServiceMyAppPermissionsRequest,
    ) -> main_models.ListDataServiceMyAppPermissionsResponse:
        runtime = RuntimeOptions()
        return self.list_data_service_my_app_permissions_with_options(request, runtime)

    async def list_data_service_my_app_permissions_async(
        self,
        request: main_models.ListDataServiceMyAppPermissionsRequest,
    ) -> main_models.ListDataServiceMyAppPermissionsResponse:
        runtime = RuntimeOptions()
        return await self.list_data_service_my_app_permissions_with_options_async(request, runtime)

    def list_data_service_published_apis_with_options(
        self,
        tmp_req: main_models.ListDataServicePublishedApisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataServicePublishedApisResponse:
        tmp_req.validate()
        request = main_models.ListDataServicePublishedApisShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDataServicePublishedApis',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataServicePublishedApisResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_service_published_apis_with_options_async(
        self,
        tmp_req: main_models.ListDataServicePublishedApisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataServicePublishedApisResponse:
        tmp_req.validate()
        request = main_models.ListDataServicePublishedApisShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDataServicePublishedApis',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataServicePublishedApisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_service_published_apis(
        self,
        request: main_models.ListDataServicePublishedApisRequest,
    ) -> main_models.ListDataServicePublishedApisResponse:
        runtime = RuntimeOptions()
        return self.list_data_service_published_apis_with_options(request, runtime)

    async def list_data_service_published_apis_async(
        self,
        request: main_models.ListDataServicePublishedApisRequest,
    ) -> main_models.ListDataServicePublishedApisResponse:
        runtime = RuntimeOptions()
        return await self.list_data_service_published_apis_with_options_async(request, runtime)

    def list_data_source_with_config_with_options(
        self,
        tmp_req: main_models.ListDataSourceWithConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataSourceWithConfigResponse:
        tmp_req.validate()
        request = main_models.ListDataSourceWithConfigShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDataSourceWithConfig',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataSourceWithConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_source_with_config_with_options_async(
        self,
        tmp_req: main_models.ListDataSourceWithConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataSourceWithConfigResponse:
        tmp_req.validate()
        request = main_models.ListDataSourceWithConfigShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDataSourceWithConfig',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataSourceWithConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_source_with_config(
        self,
        request: main_models.ListDataSourceWithConfigRequest,
    ) -> main_models.ListDataSourceWithConfigResponse:
        runtime = RuntimeOptions()
        return self.list_data_source_with_config_with_options(request, runtime)

    async def list_data_source_with_config_async(
        self,
        request: main_models.ListDataSourceWithConfigRequest,
    ) -> main_models.ListDataSourceWithConfigResponse:
        runtime = RuntimeOptions()
        return await self.list_data_source_with_config_with_options_async(request, runtime)

    def list_files_with_options(
        self,
        tmp_req: main_models.ListFilesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFilesResponse:
        tmp_req.validate()
        request = main_models.ListFilesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListFiles',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_files_with_options_async(
        self,
        tmp_req: main_models.ListFilesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFilesResponse:
        tmp_req.validate()
        request = main_models.ListFilesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListFiles',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_files(
        self,
        request: main_models.ListFilesRequest,
    ) -> main_models.ListFilesResponse:
        runtime = RuntimeOptions()
        return self.list_files_with_options(request, runtime)

    async def list_files_async(
        self,
        request: main_models.ListFilesRequest,
    ) -> main_models.ListFilesResponse:
        runtime = RuntimeOptions()
        return await self.list_files_with_options_async(request, runtime)

    def list_instances_with_options(
        self,
        tmp_req: main_models.ListInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstancesResponse:
        tmp_req.validate()
        request = main_models.ListInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListInstances',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        tmp_req: main_models.ListInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstancesResponse:
        tmp_req.validate()
        request = main_models.ListInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListInstances',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instances(
        self,
        request: main_models.ListInstancesRequest,
    ) -> main_models.ListInstancesResponse:
        runtime = RuntimeOptions()
        return self.list_instances_with_options(request, runtime)

    async def list_instances_async(
        self,
        request: main_models.ListInstancesRequest,
    ) -> main_models.ListInstancesResponse:
        runtime = RuntimeOptions()
        return await self.list_instances_with_options_async(request, runtime)

    def list_node_down_stream_with_options(
        self,
        tmp_req: main_models.ListNodeDownStreamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNodeDownStreamResponse:
        tmp_req.validate()
        request = main_models.ListNodeDownStreamShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListNodeDownStream',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNodeDownStreamResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_node_down_stream_with_options_async(
        self,
        tmp_req: main_models.ListNodeDownStreamRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNodeDownStreamResponse:
        tmp_req.validate()
        request = main_models.ListNodeDownStreamShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListNodeDownStream',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNodeDownStreamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_node_down_stream(
        self,
        request: main_models.ListNodeDownStreamRequest,
    ) -> main_models.ListNodeDownStreamResponse:
        runtime = RuntimeOptions()
        return self.list_node_down_stream_with_options(request, runtime)

    async def list_node_down_stream_async(
        self,
        request: main_models.ListNodeDownStreamRequest,
    ) -> main_models.ListNodeDownStreamResponse:
        runtime = RuntimeOptions()
        return await self.list_node_down_stream_with_options_async(request, runtime)

    def list_nodes_with_options(
        self,
        tmp_req: main_models.ListNodesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNodesResponse:
        tmp_req.validate()
        request = main_models.ListNodesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListNodes',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_nodes_with_options_async(
        self,
        tmp_req: main_models.ListNodesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNodesResponse:
        tmp_req.validate()
        request = main_models.ListNodesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListNodes',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_nodes(
        self,
        request: main_models.ListNodesRequest,
    ) -> main_models.ListNodesResponse:
        runtime = RuntimeOptions()
        return self.list_nodes_with_options(request, runtime)

    async def list_nodes_async(
        self,
        request: main_models.ListNodesRequest,
    ) -> main_models.ListNodesResponse:
        runtime = RuntimeOptions()
        return await self.list_nodes_with_options_async(request, runtime)

    def list_project_members_with_options(
        self,
        tmp_req: main_models.ListProjectMembersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListProjectMembersResponse:
        tmp_req.validate()
        request = main_models.ListProjectMembersShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListProjectMembers',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProjectMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_project_members_with_options_async(
        self,
        tmp_req: main_models.ListProjectMembersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListProjectMembersResponse:
        tmp_req.validate()
        request = main_models.ListProjectMembersShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListProjectMembers',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProjectMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_project_members(
        self,
        request: main_models.ListProjectMembersRequest,
    ) -> main_models.ListProjectMembersResponse:
        runtime = RuntimeOptions()
        return self.list_project_members_with_options(request, runtime)

    async def list_project_members_async(
        self,
        request: main_models.ListProjectMembersRequest,
    ) -> main_models.ListProjectMembersResponse:
        runtime = RuntimeOptions()
        return await self.list_project_members_with_options_async(request, runtime)

    def list_projects_with_options(
        self,
        tmp_req: main_models.ListProjectsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListProjectsResponse:
        tmp_req.validate()
        request = main_models.ListProjectsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListProjects',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_projects_with_options_async(
        self,
        tmp_req: main_models.ListProjectsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListProjectsResponse:
        tmp_req.validate()
        request = main_models.ListProjectsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListProjects',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_projects(
        self,
        request: main_models.ListProjectsRequest,
    ) -> main_models.ListProjectsResponse:
        runtime = RuntimeOptions()
        return self.list_projects_with_options(request, runtime)

    async def list_projects_async(
        self,
        request: main_models.ListProjectsRequest,
    ) -> main_models.ListProjectsResponse:
        runtime = RuntimeOptions()
        return await self.list_projects_with_options_async(request, runtime)

    def list_publish_records_with_options(
        self,
        tmp_req: main_models.ListPublishRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPublishRecordsResponse:
        tmp_req.validate()
        request = main_models.ListPublishRecordsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListPublishRecords',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPublishRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_publish_records_with_options_async(
        self,
        tmp_req: main_models.ListPublishRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPublishRecordsResponse:
        tmp_req.validate()
        request = main_models.ListPublishRecordsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListPublishRecords',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPublishRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_publish_records(
        self,
        request: main_models.ListPublishRecordsRequest,
    ) -> main_models.ListPublishRecordsResponse:
        runtime = RuntimeOptions()
        return self.list_publish_records_with_options(request, runtime)

    async def list_publish_records_async(
        self,
        request: main_models.ListPublishRecordsRequest,
    ) -> main_models.ListPublishRecordsResponse:
        runtime = RuntimeOptions()
        return await self.list_publish_records_with_options_async(request, runtime)

    def list_quality_rule_tasks_with_options(
        self,
        tmp_req: main_models.ListQualityRuleTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListQualityRuleTasksResponse:
        tmp_req.validate()
        request = main_models.ListQualityRuleTasksShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListQualityRuleTasks',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQualityRuleTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_quality_rule_tasks_with_options_async(
        self,
        tmp_req: main_models.ListQualityRuleTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListQualityRuleTasksResponse:
        tmp_req.validate()
        request = main_models.ListQualityRuleTasksShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListQualityRuleTasks',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQualityRuleTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_quality_rule_tasks(
        self,
        request: main_models.ListQualityRuleTasksRequest,
    ) -> main_models.ListQualityRuleTasksResponse:
        runtime = RuntimeOptions()
        return self.list_quality_rule_tasks_with_options(request, runtime)

    async def list_quality_rule_tasks_async(
        self,
        request: main_models.ListQualityRuleTasksRequest,
    ) -> main_models.ListQualityRuleTasksResponse:
        runtime = RuntimeOptions()
        return await self.list_quality_rule_tasks_with_options_async(request, runtime)

    def list_quality_rules_with_options(
        self,
        tmp_req: main_models.ListQualityRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListQualityRulesResponse:
        tmp_req.validate()
        request = main_models.ListQualityRulesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListQualityRules',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQualityRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_quality_rules_with_options_async(
        self,
        tmp_req: main_models.ListQualityRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListQualityRulesResponse:
        tmp_req.validate()
        request = main_models.ListQualityRulesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListQualityRules',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQualityRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_quality_rules(
        self,
        request: main_models.ListQualityRulesRequest,
    ) -> main_models.ListQualityRulesResponse:
        runtime = RuntimeOptions()
        return self.list_quality_rules_with_options(request, runtime)

    async def list_quality_rules_async(
        self,
        request: main_models.ListQualityRulesRequest,
    ) -> main_models.ListQualityRulesResponse:
        runtime = RuntimeOptions()
        return await self.list_quality_rules_with_options_async(request, runtime)

    def list_quality_templates_with_options(
        self,
        tmp_req: main_models.ListQualityTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListQualityTemplatesResponse:
        tmp_req.validate()
        request = main_models.ListQualityTemplatesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListQualityTemplates',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQualityTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_quality_templates_with_options_async(
        self,
        tmp_req: main_models.ListQualityTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListQualityTemplatesResponse:
        tmp_req.validate()
        request = main_models.ListQualityTemplatesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListQualityTemplates',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQualityTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_quality_templates(
        self,
        request: main_models.ListQualityTemplatesRequest,
    ) -> main_models.ListQualityTemplatesResponse:
        runtime = RuntimeOptions()
        return self.list_quality_templates_with_options(request, runtime)

    async def list_quality_templates_async(
        self,
        request: main_models.ListQualityTemplatesRequest,
    ) -> main_models.ListQualityTemplatesResponse:
        runtime = RuntimeOptions()
        return await self.list_quality_templates_with_options_async(request, runtime)

    def list_quality_watch_tasks_with_options(
        self,
        tmp_req: main_models.ListQualityWatchTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListQualityWatchTasksResponse:
        tmp_req.validate()
        request = main_models.ListQualityWatchTasksShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListQualityWatchTasks',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQualityWatchTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_quality_watch_tasks_with_options_async(
        self,
        tmp_req: main_models.ListQualityWatchTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListQualityWatchTasksResponse:
        tmp_req.validate()
        request = main_models.ListQualityWatchTasksShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListQualityWatchTasks',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQualityWatchTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_quality_watch_tasks(
        self,
        request: main_models.ListQualityWatchTasksRequest,
    ) -> main_models.ListQualityWatchTasksResponse:
        runtime = RuntimeOptions()
        return self.list_quality_watch_tasks_with_options(request, runtime)

    async def list_quality_watch_tasks_async(
        self,
        request: main_models.ListQualityWatchTasksRequest,
    ) -> main_models.ListQualityWatchTasksResponse:
        runtime = RuntimeOptions()
        return await self.list_quality_watch_tasks_with_options_async(request, runtime)

    def list_quality_watches_with_options(
        self,
        tmp_req: main_models.ListQualityWatchesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListQualityWatchesResponse:
        tmp_req.validate()
        request = main_models.ListQualityWatchesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListQualityWatches',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQualityWatchesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_quality_watches_with_options_async(
        self,
        tmp_req: main_models.ListQualityWatchesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListQualityWatchesResponse:
        tmp_req.validate()
        request = main_models.ListQualityWatchesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListQualityWatches',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQualityWatchesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_quality_watches(
        self,
        request: main_models.ListQualityWatchesRequest,
    ) -> main_models.ListQualityWatchesResponse:
        runtime = RuntimeOptions()
        return self.list_quality_watches_with_options(request, runtime)

    async def list_quality_watches_async(
        self,
        request: main_models.ListQualityWatchesRequest,
    ) -> main_models.ListQualityWatchesResponse:
        runtime = RuntimeOptions()
        return await self.list_quality_watches_with_options_async(request, runtime)

    def list_resource_permission_operation_log_with_options(
        self,
        tmp_req: main_models.ListResourcePermissionOperationLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResourcePermissionOperationLogResponse:
        tmp_req.validate()
        request = main_models.ListResourcePermissionOperationLogShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListResourcePermissionOperationLog',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourcePermissionOperationLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_permission_operation_log_with_options_async(
        self,
        tmp_req: main_models.ListResourcePermissionOperationLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResourcePermissionOperationLogResponse:
        tmp_req.validate()
        request = main_models.ListResourcePermissionOperationLogShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListResourcePermissionOperationLog',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourcePermissionOperationLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_permission_operation_log(
        self,
        request: main_models.ListResourcePermissionOperationLogRequest,
    ) -> main_models.ListResourcePermissionOperationLogResponse:
        runtime = RuntimeOptions()
        return self.list_resource_permission_operation_log_with_options(request, runtime)

    async def list_resource_permission_operation_log_async(
        self,
        request: main_models.ListResourcePermissionOperationLogRequest,
    ) -> main_models.ListResourcePermissionOperationLogResponse:
        runtime = RuntimeOptions()
        return await self.list_resource_permission_operation_log_with_options_async(request, runtime)

    def list_resource_permissions_with_options(
        self,
        tmp_req: main_models.ListResourcePermissionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResourcePermissionsResponse:
        tmp_req.validate()
        request = main_models.ListResourcePermissionsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListResourcePermissions',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourcePermissionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_permissions_with_options_async(
        self,
        tmp_req: main_models.ListResourcePermissionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResourcePermissionsResponse:
        tmp_req.validate()
        request = main_models.ListResourcePermissionsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListResourcePermissions',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourcePermissionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_permissions(
        self,
        request: main_models.ListResourcePermissionsRequest,
    ) -> main_models.ListResourcePermissionsResponse:
        runtime = RuntimeOptions()
        return self.list_resource_permissions_with_options(request, runtime)

    async def list_resource_permissions_async(
        self,
        request: main_models.ListResourcePermissionsRequest,
    ) -> main_models.ListResourcePermissionsResponse:
        runtime = RuntimeOptions()
        return await self.list_resource_permissions_with_options_async(request, runtime)

    def list_row_permission_with_options(
        self,
        tmp_req: main_models.ListRowPermissionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRowPermissionResponse:
        tmp_req.validate()
        request = main_models.ListRowPermissionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.page_row_permission_query):
            request.page_row_permission_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.page_row_permission_query, 'PageRowPermissionQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.page_row_permission_query_shrink):
            body['PageRowPermissionQuery'] = request.page_row_permission_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListRowPermission',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRowPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_row_permission_with_options_async(
        self,
        tmp_req: main_models.ListRowPermissionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRowPermissionResponse:
        tmp_req.validate()
        request = main_models.ListRowPermissionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.page_row_permission_query):
            request.page_row_permission_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.page_row_permission_query, 'PageRowPermissionQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.page_row_permission_query_shrink):
            body['PageRowPermissionQuery'] = request.page_row_permission_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListRowPermission',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRowPermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_row_permission(
        self,
        request: main_models.ListRowPermissionRequest,
    ) -> main_models.ListRowPermissionResponse:
        runtime = RuntimeOptions()
        return self.list_row_permission_with_options(request, runtime)

    async def list_row_permission_async(
        self,
        request: main_models.ListRowPermissionRequest,
    ) -> main_models.ListRowPermissionResponse:
        runtime = RuntimeOptions()
        return await self.list_row_permission_with_options_async(request, runtime)

    def list_row_permission_by_user_id_with_options(
        self,
        tmp_req: main_models.ListRowPermissionByUserIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRowPermissionByUserIdResponse:
        tmp_req.validate()
        request = main_models.ListRowPermissionByUserIdShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_row_permission_by_user_id_query):
            request.list_row_permission_by_user_id_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_row_permission_by_user_id_query, 'ListRowPermissionByUserIdQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_row_permission_by_user_id_query_shrink):
            body['ListRowPermissionByUserIdQuery'] = request.list_row_permission_by_user_id_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListRowPermissionByUserId',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRowPermissionByUserIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_row_permission_by_user_id_with_options_async(
        self,
        tmp_req: main_models.ListRowPermissionByUserIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRowPermissionByUserIdResponse:
        tmp_req.validate()
        request = main_models.ListRowPermissionByUserIdShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_row_permission_by_user_id_query):
            request.list_row_permission_by_user_id_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_row_permission_by_user_id_query, 'ListRowPermissionByUserIdQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_row_permission_by_user_id_query_shrink):
            body['ListRowPermissionByUserIdQuery'] = request.list_row_permission_by_user_id_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListRowPermissionByUserId',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRowPermissionByUserIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_row_permission_by_user_id(
        self,
        request: main_models.ListRowPermissionByUserIdRequest,
    ) -> main_models.ListRowPermissionByUserIdResponse:
        runtime = RuntimeOptions()
        return self.list_row_permission_by_user_id_with_options(request, runtime)

    async def list_row_permission_by_user_id_async(
        self,
        request: main_models.ListRowPermissionByUserIdRequest,
    ) -> main_models.ListRowPermissionByUserIdResponse:
        runtime = RuntimeOptions()
        return await self.list_row_permission_by_user_id_with_options_async(request, runtime)

    def list_security_identify_records_with_options(
        self,
        tmp_req: main_models.ListSecurityIdentifyRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSecurityIdentifyRecordsResponse:
        tmp_req.validate()
        request = main_models.ListSecurityIdentifyRecordsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListSecurityIdentifyRecords',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSecurityIdentifyRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_security_identify_records_with_options_async(
        self,
        tmp_req: main_models.ListSecurityIdentifyRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSecurityIdentifyRecordsResponse:
        tmp_req.validate()
        request = main_models.ListSecurityIdentifyRecordsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListSecurityIdentifyRecords',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSecurityIdentifyRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_security_identify_records(
        self,
        request: main_models.ListSecurityIdentifyRecordsRequest,
    ) -> main_models.ListSecurityIdentifyRecordsResponse:
        runtime = RuntimeOptions()
        return self.list_security_identify_records_with_options(request, runtime)

    async def list_security_identify_records_async(
        self,
        request: main_models.ListSecurityIdentifyRecordsRequest,
    ) -> main_models.ListSecurityIdentifyRecordsResponse:
        runtime = RuntimeOptions()
        return await self.list_security_identify_records_with_options_async(request, runtime)

    def list_security_identify_results_with_options(
        self,
        tmp_req: main_models.ListSecurityIdentifyResultsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSecurityIdentifyResultsResponse:
        tmp_req.validate()
        request = main_models.ListSecurityIdentifyResultsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListSecurityIdentifyResults',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSecurityIdentifyResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_security_identify_results_with_options_async(
        self,
        tmp_req: main_models.ListSecurityIdentifyResultsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSecurityIdentifyResultsResponse:
        tmp_req.validate()
        request = main_models.ListSecurityIdentifyResultsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListSecurityIdentifyResults',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSecurityIdentifyResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_security_identify_results(
        self,
        request: main_models.ListSecurityIdentifyResultsRequest,
    ) -> main_models.ListSecurityIdentifyResultsResponse:
        runtime = RuntimeOptions()
        return self.list_security_identify_results_with_options(request, runtime)

    async def list_security_identify_results_async(
        self,
        request: main_models.ListSecurityIdentifyResultsRequest,
    ) -> main_models.ListSecurityIdentifyResultsResponse:
        runtime = RuntimeOptions()
        return await self.list_security_identify_results_with_options_async(request, runtime)

    def list_standards_with_options(
        self,
        tmp_req: main_models.ListStandardsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListStandardsResponse:
        tmp_req.validate()
        request = main_models.ListStandardsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListStandards',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListStandardsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_standards_with_options_async(
        self,
        tmp_req: main_models.ListStandardsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListStandardsResponse:
        tmp_req.validate()
        request = main_models.ListStandardsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListStandards',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListStandardsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_standards(
        self,
        request: main_models.ListStandardsRequest,
    ) -> main_models.ListStandardsResponse:
        runtime = RuntimeOptions()
        return self.list_standards_with_options(request, runtime)

    async def list_standards_async(
        self,
        request: main_models.ListStandardsRequest,
    ) -> main_models.ListStandardsResponse:
        runtime = RuntimeOptions()
        return await self.list_standards_with_options_async(request, runtime)

    def list_submit_records_with_options(
        self,
        tmp_req: main_models.ListSubmitRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSubmitRecordsResponse:
        tmp_req.validate()
        request = main_models.ListSubmitRecordsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListSubmitRecords',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSubmitRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_submit_records_with_options_async(
        self,
        tmp_req: main_models.ListSubmitRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSubmitRecordsResponse:
        tmp_req.validate()
        request = main_models.ListSubmitRecordsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListSubmitRecords',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSubmitRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_submit_records(
        self,
        request: main_models.ListSubmitRecordsRequest,
    ) -> main_models.ListSubmitRecordsResponse:
        runtime = RuntimeOptions()
        return self.list_submit_records_with_options(request, runtime)

    async def list_submit_records_async(
        self,
        request: main_models.ListSubmitRecordsRequest,
    ) -> main_models.ListSubmitRecordsResponse:
        runtime = RuntimeOptions()
        return await self.list_submit_records_with_options_async(request, runtime)

    def list_tables_with_options(
        self,
        tmp_req: main_models.ListTablesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTablesResponse:
        tmp_req.validate()
        request = main_models.ListTablesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListTables',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tables_with_options_async(
        self,
        tmp_req: main_models.ListTablesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTablesResponse:
        tmp_req.validate()
        request = main_models.ListTablesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListTables',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tables(
        self,
        request: main_models.ListTablesRequest,
    ) -> main_models.ListTablesResponse:
        runtime = RuntimeOptions()
        return self.list_tables_with_options(request, runtime)

    async def list_tables_async(
        self,
        request: main_models.ListTablesRequest,
    ) -> main_models.ListTablesResponse:
        runtime = RuntimeOptions()
        return await self.list_tables_with_options_async(request, runtime)

    def list_tenant_members_with_options(
        self,
        tmp_req: main_models.ListTenantMembersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTenantMembersResponse:
        tmp_req.validate()
        request = main_models.ListTenantMembersShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListTenantMembers',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTenantMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tenant_members_with_options_async(
        self,
        tmp_req: main_models.ListTenantMembersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTenantMembersResponse:
        tmp_req.validate()
        request = main_models.ListTenantMembersShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListTenantMembers',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTenantMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tenant_members(
        self,
        request: main_models.ListTenantMembersRequest,
    ) -> main_models.ListTenantMembersResponse:
        runtime = RuntimeOptions()
        return self.list_tenant_members_with_options(request, runtime)

    async def list_tenant_members_async(
        self,
        request: main_models.ListTenantMembersRequest,
    ) -> main_models.ListTenantMembersResponse:
        runtime = RuntimeOptions()
        return await self.list_tenant_members_with_options_async(request, runtime)

    def list_user_group_members_with_options(
        self,
        tmp_req: main_models.ListUserGroupMembersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserGroupMembersResponse:
        tmp_req.validate()
        request = main_models.ListUserGroupMembersShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListUserGroupMembers',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserGroupMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_group_members_with_options_async(
        self,
        tmp_req: main_models.ListUserGroupMembersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserGroupMembersResponse:
        tmp_req.validate()
        request = main_models.ListUserGroupMembersShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListUserGroupMembers',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserGroupMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_group_members(
        self,
        request: main_models.ListUserGroupMembersRequest,
    ) -> main_models.ListUserGroupMembersResponse:
        runtime = RuntimeOptions()
        return self.list_user_group_members_with_options(request, runtime)

    async def list_user_group_members_async(
        self,
        request: main_models.ListUserGroupMembersRequest,
    ) -> main_models.ListUserGroupMembersResponse:
        runtime = RuntimeOptions()
        return await self.list_user_group_members_with_options_async(request, runtime)

    def list_user_groups_with_options(
        self,
        tmp_req: main_models.ListUserGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserGroupsResponse:
        tmp_req.validate()
        request = main_models.ListUserGroupsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListUserGroups',
            version = '2023-06-30',
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
        tmp_req: main_models.ListUserGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserGroupsResponse:
        tmp_req.validate()
        request = main_models.ListUserGroupsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_query):
            request.list_query_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListUserGroups',
            version = '2023-06-30',
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

    def offline_batch_task_with_options(
        self,
        request: main_models.OfflineBatchTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OfflineBatchTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.file_id):
            query['FileId'] = request.file_id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OfflineBatchTask',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OfflineBatchTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def offline_batch_task_with_options_async(
        self,
        request: main_models.OfflineBatchTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OfflineBatchTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.file_id):
            query['FileId'] = request.file_id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OfflineBatchTask',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OfflineBatchTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def offline_batch_task(
        self,
        request: main_models.OfflineBatchTaskRequest,
    ) -> main_models.OfflineBatchTaskResponse:
        runtime = RuntimeOptions()
        return self.offline_batch_task_with_options(request, runtime)

    async def offline_batch_task_async(
        self,
        request: main_models.OfflineBatchTaskRequest,
    ) -> main_models.OfflineBatchTaskResponse:
        runtime = RuntimeOptions()
        return await self.offline_batch_task_with_options_async(request, runtime)

    def offline_biz_entity_with_options(
        self,
        tmp_req: main_models.OfflineBizEntityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OfflineBizEntityResponse:
        tmp_req.validate()
        request = main_models.OfflineBizEntityShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.offline_command):
            request.offline_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.offline_command, 'OfflineCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.offline_command_shrink):
            body['OfflineCommand'] = request.offline_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OfflineBizEntity',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OfflineBizEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def offline_biz_entity_with_options_async(
        self,
        tmp_req: main_models.OfflineBizEntityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OfflineBizEntityResponse:
        tmp_req.validate()
        request = main_models.OfflineBizEntityShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.offline_command):
            request.offline_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.offline_command, 'OfflineCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.offline_command_shrink):
            body['OfflineCommand'] = request.offline_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OfflineBizEntity',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OfflineBizEntityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def offline_biz_entity(
        self,
        request: main_models.OfflineBizEntityRequest,
    ) -> main_models.OfflineBizEntityResponse:
        runtime = RuntimeOptions()
        return self.offline_biz_entity_with_options(request, runtime)

    async def offline_biz_entity_async(
        self,
        request: main_models.OfflineBizEntityRequest,
    ) -> main_models.OfflineBizEntityResponse:
        runtime = RuntimeOptions()
        return await self.offline_biz_entity_with_options_async(request, runtime)

    def offline_pipeline_with_options(
        self,
        tmp_req: main_models.OfflinePipelineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OfflinePipelineResponse:
        tmp_req.validate()
        request = main_models.OfflinePipelineShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.context):
            request.context_shrink = Utils.array_to_string_with_specified_style(tmp_req.context, 'Context', 'json')
        if not DaraCore.is_null(tmp_req.offline_command):
            request.offline_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.offline_command, 'OfflineCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.context_shrink):
            body['Context'] = request.context_shrink
        if not DaraCore.is_null(request.offline_command_shrink):
            body['OfflineCommand'] = request.offline_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OfflinePipeline',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OfflinePipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def offline_pipeline_with_options_async(
        self,
        tmp_req: main_models.OfflinePipelineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OfflinePipelineResponse:
        tmp_req.validate()
        request = main_models.OfflinePipelineShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.context):
            request.context_shrink = Utils.array_to_string_with_specified_style(tmp_req.context, 'Context', 'json')
        if not DaraCore.is_null(tmp_req.offline_command):
            request.offline_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.offline_command, 'OfflineCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.context_shrink):
            body['Context'] = request.context_shrink
        if not DaraCore.is_null(request.offline_command_shrink):
            body['OfflineCommand'] = request.offline_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OfflinePipeline',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OfflinePipelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def offline_pipeline(
        self,
        request: main_models.OfflinePipelineRequest,
    ) -> main_models.OfflinePipelineResponse:
        runtime = RuntimeOptions()
        return self.offline_pipeline_with_options(request, runtime)

    async def offline_pipeline_async(
        self,
        request: main_models.OfflinePipelineRequest,
    ) -> main_models.OfflinePipelineResponse:
        runtime = RuntimeOptions()
        return await self.offline_pipeline_with_options_async(request, runtime)

    def offline_pipeline_by_async_with_options(
        self,
        tmp_req: main_models.OfflinePipelineByAsyncRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OfflinePipelineByAsyncResponse:
        tmp_req.validate()
        request = main_models.OfflinePipelineByAsyncShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.context):
            request.context_shrink = Utils.array_to_string_with_specified_style(tmp_req.context, 'Context', 'json')
        if not DaraCore.is_null(tmp_req.offline_command):
            request.offline_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.offline_command, 'OfflineCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.context_shrink):
            body['Context'] = request.context_shrink
        if not DaraCore.is_null(request.offline_command_shrink):
            body['OfflineCommand'] = request.offline_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OfflinePipelineByAsync',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OfflinePipelineByAsyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def offline_pipeline_by_async_with_options_async(
        self,
        tmp_req: main_models.OfflinePipelineByAsyncRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OfflinePipelineByAsyncResponse:
        tmp_req.validate()
        request = main_models.OfflinePipelineByAsyncShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.context):
            request.context_shrink = Utils.array_to_string_with_specified_style(tmp_req.context, 'Context', 'json')
        if not DaraCore.is_null(tmp_req.offline_command):
            request.offline_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.offline_command, 'OfflineCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.context_shrink):
            body['Context'] = request.context_shrink
        if not DaraCore.is_null(request.offline_command_shrink):
            body['OfflineCommand'] = request.offline_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OfflinePipelineByAsync',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OfflinePipelineByAsyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def offline_pipeline_by_async(
        self,
        request: main_models.OfflinePipelineByAsyncRequest,
    ) -> main_models.OfflinePipelineByAsyncResponse:
        runtime = RuntimeOptions()
        return self.offline_pipeline_by_async_with_options(request, runtime)

    async def offline_pipeline_by_async_async(
        self,
        request: main_models.OfflinePipelineByAsyncRequest,
    ) -> main_models.OfflinePipelineByAsyncResponse:
        runtime = RuntimeOptions()
        return await self.offline_pipeline_by_async_with_options_async(request, runtime)

    def offline_standard_with_options(
        self,
        tmp_req: main_models.OfflineStandardRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OfflineStandardResponse:
        tmp_req.validate()
        request = main_models.OfflineStandardShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.offline_command):
            request.offline_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.offline_command, 'OfflineCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.offline_command_shrink):
            body['OfflineCommand'] = request.offline_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OfflineStandard',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OfflineStandardResponse(),
            self.call_api(params, req, runtime)
        )

    async def offline_standard_with_options_async(
        self,
        tmp_req: main_models.OfflineStandardRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OfflineStandardResponse:
        tmp_req.validate()
        request = main_models.OfflineStandardShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.offline_command):
            request.offline_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.offline_command, 'OfflineCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.offline_command_shrink):
            body['OfflineCommand'] = request.offline_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OfflineStandard',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OfflineStandardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def offline_standard(
        self,
        request: main_models.OfflineStandardRequest,
    ) -> main_models.OfflineStandardResponse:
        runtime = RuntimeOptions()
        return self.offline_standard_with_options(request, runtime)

    async def offline_standard_async(
        self,
        request: main_models.OfflineStandardRequest,
    ) -> main_models.OfflineStandardResponse:
        runtime = RuntimeOptions()
        return await self.offline_standard_with_options_async(request, runtime)

    def online_biz_entity_with_options(
        self,
        tmp_req: main_models.OnlineBizEntityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnlineBizEntityResponse:
        tmp_req.validate()
        request = main_models.OnlineBizEntityShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.online_command):
            request.online_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.online_command, 'OnlineCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.online_command_shrink):
            body['OnlineCommand'] = request.online_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OnlineBizEntity',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnlineBizEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def online_biz_entity_with_options_async(
        self,
        tmp_req: main_models.OnlineBizEntityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnlineBizEntityResponse:
        tmp_req.validate()
        request = main_models.OnlineBizEntityShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.online_command):
            request.online_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.online_command, 'OnlineCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.online_command_shrink):
            body['OnlineCommand'] = request.online_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OnlineBizEntity',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnlineBizEntityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def online_biz_entity(
        self,
        request: main_models.OnlineBizEntityRequest,
    ) -> main_models.OnlineBizEntityResponse:
        runtime = RuntimeOptions()
        return self.online_biz_entity_with_options(request, runtime)

    async def online_biz_entity_async(
        self,
        request: main_models.OnlineBizEntityRequest,
    ) -> main_models.OnlineBizEntityResponse:
        runtime = RuntimeOptions()
        return await self.online_biz_entity_with_options_async(request, runtime)

    def operate_instance_with_options(
        self,
        tmp_req: main_models.OperateInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateInstanceResponse:
        tmp_req.validate()
        request = main_models.OperateInstanceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.operate_command):
            request.operate_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.operate_command, 'OperateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.operate_command_shrink):
            body['OperateCommand'] = request.operate_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OperateInstance',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_instance_with_options_async(
        self,
        tmp_req: main_models.OperateInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateInstanceResponse:
        tmp_req.validate()
        request = main_models.OperateInstanceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.operate_command):
            request.operate_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.operate_command, 'OperateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.operate_command_shrink):
            body['OperateCommand'] = request.operate_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OperateInstance',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_instance(
        self,
        request: main_models.OperateInstanceRequest,
    ) -> main_models.OperateInstanceResponse:
        runtime = RuntimeOptions()
        return self.operate_instance_with_options(request, runtime)

    async def operate_instance_async(
        self,
        request: main_models.OperateInstanceRequest,
    ) -> main_models.OperateInstanceResponse:
        runtime = RuntimeOptions()
        return await self.operate_instance_with_options_async(request, runtime)

    def parse_batch_task_dependency_with_options(
        self,
        tmp_req: main_models.ParseBatchTaskDependencyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ParseBatchTaskDependencyResponse:
        tmp_req.validate()
        request = main_models.ParseBatchTaskDependencyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.parse_command):
            request.parse_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.parse_command, 'ParseCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.parse_command_shrink):
            body['ParseCommand'] = request.parse_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ParseBatchTaskDependency',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ParseBatchTaskDependencyResponse(),
            self.call_api(params, req, runtime)
        )

    async def parse_batch_task_dependency_with_options_async(
        self,
        tmp_req: main_models.ParseBatchTaskDependencyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ParseBatchTaskDependencyResponse:
        tmp_req.validate()
        request = main_models.ParseBatchTaskDependencyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.parse_command):
            request.parse_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.parse_command, 'ParseCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.parse_command_shrink):
            body['ParseCommand'] = request.parse_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ParseBatchTaskDependency',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ParseBatchTaskDependencyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def parse_batch_task_dependency(
        self,
        request: main_models.ParseBatchTaskDependencyRequest,
    ) -> main_models.ParseBatchTaskDependencyResponse:
        runtime = RuntimeOptions()
        return self.parse_batch_task_dependency_with_options(request, runtime)

    async def parse_batch_task_dependency_async(
        self,
        request: main_models.ParseBatchTaskDependencyRequest,
    ) -> main_models.ParseBatchTaskDependencyResponse:
        runtime = RuntimeOptions()
        return await self.parse_batch_task_dependency_with_options_async(request, runtime)

    def pause_physical_node_with_options(
        self,
        tmp_req: main_models.PausePhysicalNodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PausePhysicalNodeResponse:
        tmp_req.validate()
        request = main_models.PausePhysicalNodeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.pause_command):
            request.pause_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.pause_command, 'PauseCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.pause_command_shrink):
            body['PauseCommand'] = request.pause_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PausePhysicalNode',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PausePhysicalNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def pause_physical_node_with_options_async(
        self,
        tmp_req: main_models.PausePhysicalNodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PausePhysicalNodeResponse:
        tmp_req.validate()
        request = main_models.PausePhysicalNodeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.pause_command):
            request.pause_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.pause_command, 'PauseCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.pause_command_shrink):
            body['PauseCommand'] = request.pause_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PausePhysicalNode',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PausePhysicalNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pause_physical_node(
        self,
        request: main_models.PausePhysicalNodeRequest,
    ) -> main_models.PausePhysicalNodeResponse:
        runtime = RuntimeOptions()
        return self.pause_physical_node_with_options(request, runtime)

    async def pause_physical_node_async(
        self,
        request: main_models.PausePhysicalNodeRequest,
    ) -> main_models.PausePhysicalNodeResponse:
        runtime = RuntimeOptions()
        return await self.pause_physical_node_with_options_async(request, runtime)

    def publish_data_service_api_with_options(
        self,
        request: main_models.PublishDataServiceApiRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PublishDataServiceApiResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PublishDataServiceApi',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishDataServiceApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_data_service_api_with_options_async(
        self,
        request: main_models.PublishDataServiceApiRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PublishDataServiceApiResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_id):
            query['ApiId'] = request.api_id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PublishDataServiceApi',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishDataServiceApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_data_service_api(
        self,
        request: main_models.PublishDataServiceApiRequest,
    ) -> main_models.PublishDataServiceApiResponse:
        runtime = RuntimeOptions()
        return self.publish_data_service_api_with_options(request, runtime)

    async def publish_data_service_api_async(
        self,
        request: main_models.PublishDataServiceApiRequest,
    ) -> main_models.PublishDataServiceApiResponse:
        runtime = RuntimeOptions()
        return await self.publish_data_service_api_with_options_async(request, runtime)

    def publish_object_list_with_options(
        self,
        tmp_req: main_models.PublishObjectListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PublishObjectListResponse:
        tmp_req.validate()
        request = main_models.PublishObjectListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.publish_command):
            request.publish_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.publish_command, 'PublishCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.publish_command_shrink):
            body['PublishCommand'] = request.publish_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PublishObjectList',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishObjectListResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_object_list_with_options_async(
        self,
        tmp_req: main_models.PublishObjectListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PublishObjectListResponse:
        tmp_req.validate()
        request = main_models.PublishObjectListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.publish_command):
            request.publish_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.publish_command, 'PublishCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.publish_command_shrink):
            body['PublishCommand'] = request.publish_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PublishObjectList',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishObjectListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_object_list(
        self,
        request: main_models.PublishObjectListRequest,
    ) -> main_models.PublishObjectListResponse:
        runtime = RuntimeOptions()
        return self.publish_object_list_with_options(request, runtime)

    async def publish_object_list_async(
        self,
        request: main_models.PublishObjectListRequest,
    ) -> main_models.PublishObjectListResponse:
        runtime = RuntimeOptions()
        return await self.publish_object_list_with_options_async(request, runtime)

    def publish_standard_with_options(
        self,
        tmp_req: main_models.PublishStandardRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PublishStandardResponse:
        tmp_req.validate()
        request = main_models.PublishStandardShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.publish_command):
            request.publish_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.publish_command, 'PublishCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.publish_command_shrink):
            body['PublishCommand'] = request.publish_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PublishStandard',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishStandardResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_standard_with_options_async(
        self,
        tmp_req: main_models.PublishStandardRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PublishStandardResponse:
        tmp_req.validate()
        request = main_models.PublishStandardShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.publish_command):
            request.publish_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.publish_command, 'PublishCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.publish_command_shrink):
            body['PublishCommand'] = request.publish_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PublishStandard',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishStandardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_standard(
        self,
        request: main_models.PublishStandardRequest,
    ) -> main_models.PublishStandardResponse:
        runtime = RuntimeOptions()
        return self.publish_standard_with_options(request, runtime)

    async def publish_standard_async(
        self,
        request: main_models.PublishStandardRequest,
    ) -> main_models.PublishStandardResponse:
        runtime = RuntimeOptions()
        return await self.publish_standard_with_options_async(request, runtime)

    def remove_project_member_with_options(
        self,
        tmp_req: main_models.RemoveProjectMemberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveProjectMemberResponse:
        tmp_req.validate()
        request = main_models.RemoveProjectMemberShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.remove_command):
            request.remove_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.remove_command, 'RemoveCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.remove_command_shrink):
            body['RemoveCommand'] = request.remove_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RemoveProjectMember',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveProjectMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_project_member_with_options_async(
        self,
        tmp_req: main_models.RemoveProjectMemberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveProjectMemberResponse:
        tmp_req.validate()
        request = main_models.RemoveProjectMemberShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.remove_command):
            request.remove_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.remove_command, 'RemoveCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.remove_command_shrink):
            body['RemoveCommand'] = request.remove_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RemoveProjectMember',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveProjectMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_project_member(
        self,
        request: main_models.RemoveProjectMemberRequest,
    ) -> main_models.RemoveProjectMemberResponse:
        runtime = RuntimeOptions()
        return self.remove_project_member_with_options(request, runtime)

    async def remove_project_member_async(
        self,
        request: main_models.RemoveProjectMemberRequest,
    ) -> main_models.RemoveProjectMemberResponse:
        runtime = RuntimeOptions()
        return await self.remove_project_member_with_options_async(request, runtime)

    def remove_quality_rule_schedules_with_options(
        self,
        tmp_req: main_models.RemoveQualityRuleSchedulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveQualityRuleSchedulesResponse:
        tmp_req.validate()
        request = main_models.RemoveQualityRuleSchedulesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.remove_command):
            request.remove_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.remove_command, 'RemoveCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.remove_command_shrink):
            body['RemoveCommand'] = request.remove_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RemoveQualityRuleSchedules',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveQualityRuleSchedulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_quality_rule_schedules_with_options_async(
        self,
        tmp_req: main_models.RemoveQualityRuleSchedulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveQualityRuleSchedulesResponse:
        tmp_req.validate()
        request = main_models.RemoveQualityRuleSchedulesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.remove_command):
            request.remove_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.remove_command, 'RemoveCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.remove_command_shrink):
            body['RemoveCommand'] = request.remove_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RemoveQualityRuleSchedules',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveQualityRuleSchedulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_quality_rule_schedules(
        self,
        request: main_models.RemoveQualityRuleSchedulesRequest,
    ) -> main_models.RemoveQualityRuleSchedulesResponse:
        runtime = RuntimeOptions()
        return self.remove_quality_rule_schedules_with_options(request, runtime)

    async def remove_quality_rule_schedules_async(
        self,
        request: main_models.RemoveQualityRuleSchedulesRequest,
    ) -> main_models.RemoveQualityRuleSchedulesResponse:
        runtime = RuntimeOptions()
        return await self.remove_quality_rule_schedules_with_options_async(request, runtime)

    def remove_tenant_member_with_options(
        self,
        tmp_req: main_models.RemoveTenantMemberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveTenantMemberResponse:
        tmp_req.validate()
        request = main_models.RemoveTenantMemberShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.remove_command):
            request.remove_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.remove_command, 'RemoveCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.remove_command_shrink):
            body['RemoveCommand'] = request.remove_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RemoveTenantMember',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveTenantMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_tenant_member_with_options_async(
        self,
        tmp_req: main_models.RemoveTenantMemberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveTenantMemberResponse:
        tmp_req.validate()
        request = main_models.RemoveTenantMemberShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.remove_command):
            request.remove_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.remove_command, 'RemoveCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.remove_command_shrink):
            body['RemoveCommand'] = request.remove_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RemoveTenantMember',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveTenantMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_tenant_member(
        self,
        request: main_models.RemoveTenantMemberRequest,
    ) -> main_models.RemoveTenantMemberResponse:
        runtime = RuntimeOptions()
        return self.remove_tenant_member_with_options(request, runtime)

    async def remove_tenant_member_async(
        self,
        request: main_models.RemoveTenantMemberRequest,
    ) -> main_models.RemoveTenantMemberResponse:
        runtime = RuntimeOptions()
        return await self.remove_tenant_member_with_options_async(request, runtime)

    def remove_user_group_member_with_options(
        self,
        tmp_req: main_models.RemoveUserGroupMemberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveUserGroupMemberResponse:
        tmp_req.validate()
        request = main_models.RemoveUserGroupMemberShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.remove_command):
            request.remove_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.remove_command, 'RemoveCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.remove_command_shrink):
            body['RemoveCommand'] = request.remove_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RemoveUserGroupMember',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveUserGroupMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_user_group_member_with_options_async(
        self,
        tmp_req: main_models.RemoveUserGroupMemberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveUserGroupMemberResponse:
        tmp_req.validate()
        request = main_models.RemoveUserGroupMemberShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.remove_command):
            request.remove_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.remove_command, 'RemoveCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.remove_command_shrink):
            body['RemoveCommand'] = request.remove_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RemoveUserGroupMember',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveUserGroupMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_user_group_member(
        self,
        request: main_models.RemoveUserGroupMemberRequest,
    ) -> main_models.RemoveUserGroupMemberResponse:
        runtime = RuntimeOptions()
        return self.remove_user_group_member_with_options(request, runtime)

    async def remove_user_group_member_async(
        self,
        request: main_models.RemoveUserGroupMemberRequest,
    ) -> main_models.RemoveUserGroupMemberResponse:
        runtime = RuntimeOptions()
        return await self.remove_user_group_member_with_options_async(request, runtime)

    def replace_project_white_lists_with_options(
        self,
        tmp_req: main_models.ReplaceProjectWhiteListsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReplaceProjectWhiteListsResponse:
        tmp_req.validate()
        request = main_models.ReplaceProjectWhiteListsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.replace_command):
            request.replace_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.replace_command, 'ReplaceCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.replace_command_shrink):
            body['ReplaceCommand'] = request.replace_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReplaceProjectWhiteLists',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReplaceProjectWhiteListsResponse(),
            self.call_api(params, req, runtime)
        )

    async def replace_project_white_lists_with_options_async(
        self,
        tmp_req: main_models.ReplaceProjectWhiteListsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReplaceProjectWhiteListsResponse:
        tmp_req.validate()
        request = main_models.ReplaceProjectWhiteListsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.replace_command):
            request.replace_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.replace_command, 'ReplaceCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.replace_command_shrink):
            body['ReplaceCommand'] = request.replace_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReplaceProjectWhiteLists',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReplaceProjectWhiteListsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def replace_project_white_lists(
        self,
        request: main_models.ReplaceProjectWhiteListsRequest,
    ) -> main_models.ReplaceProjectWhiteListsResponse:
        runtime = RuntimeOptions()
        return self.replace_project_white_lists_with_options(request, runtime)

    async def replace_project_white_lists_async(
        self,
        request: main_models.ReplaceProjectWhiteListsRequest,
    ) -> main_models.ReplaceProjectWhiteListsResponse:
        runtime = RuntimeOptions()
        return await self.replace_project_white_lists_with_options_async(request, runtime)

    def resume_physical_node_with_options(
        self,
        tmp_req: main_models.ResumePhysicalNodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResumePhysicalNodeResponse:
        tmp_req.validate()
        request = main_models.ResumePhysicalNodeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resume_command):
            request.resume_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.resume_command, 'ResumeCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.resume_command_shrink):
            body['ResumeCommand'] = request.resume_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ResumePhysicalNode',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResumePhysicalNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_physical_node_with_options_async(
        self,
        tmp_req: main_models.ResumePhysicalNodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResumePhysicalNodeResponse:
        tmp_req.validate()
        request = main_models.ResumePhysicalNodeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resume_command):
            request.resume_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.resume_command, 'ResumeCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.env):
            query['Env'] = request.env
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.resume_command_shrink):
            body['ResumeCommand'] = request.resume_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ResumePhysicalNode',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResumePhysicalNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_physical_node(
        self,
        request: main_models.ResumePhysicalNodeRequest,
    ) -> main_models.ResumePhysicalNodeResponse:
        runtime = RuntimeOptions()
        return self.resume_physical_node_with_options(request, runtime)

    async def resume_physical_node_async(
        self,
        request: main_models.ResumePhysicalNodeRequest,
    ) -> main_models.ResumePhysicalNodeResponse:
        runtime = RuntimeOptions()
        return await self.resume_physical_node_with_options_async(request, runtime)

    def retry_transfer_ownership_with_options(
        self,
        tmp_req: main_models.RetryTransferOwnershipRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RetryTransferOwnershipResponse:
        tmp_req.validate()
        request = main_models.RetryTransferOwnershipShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.privilege_transfer_record):
            request.privilege_transfer_record_shrink = Utils.array_to_string_with_specified_style(tmp_req.privilege_transfer_record, 'PrivilegeTransferRecord', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.privilege_transfer_record_shrink):
            body['PrivilegeTransferRecord'] = request.privilege_transfer_record_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RetryTransferOwnership',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RetryTransferOwnershipResponse(),
            self.call_api(params, req, runtime)
        )

    async def retry_transfer_ownership_with_options_async(
        self,
        tmp_req: main_models.RetryTransferOwnershipRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RetryTransferOwnershipResponse:
        tmp_req.validate()
        request = main_models.RetryTransferOwnershipShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.privilege_transfer_record):
            request.privilege_transfer_record_shrink = Utils.array_to_string_with_specified_style(tmp_req.privilege_transfer_record, 'PrivilegeTransferRecord', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.privilege_transfer_record_shrink):
            body['PrivilegeTransferRecord'] = request.privilege_transfer_record_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RetryTransferOwnership',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RetryTransferOwnershipResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def retry_transfer_ownership(
        self,
        request: main_models.RetryTransferOwnershipRequest,
    ) -> main_models.RetryTransferOwnershipResponse:
        runtime = RuntimeOptions()
        return self.retry_transfer_ownership_with_options(request, runtime)

    async def retry_transfer_ownership_async(
        self,
        request: main_models.RetryTransferOwnershipRequest,
    ) -> main_models.RetryTransferOwnershipResponse:
        runtime = RuntimeOptions()
        return await self.retry_transfer_ownership_with_options_async(request, runtime)

    def revoke_data_service_api_with_options(
        self,
        tmp_req: main_models.RevokeDataServiceApiRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RevokeDataServiceApiResponse:
        tmp_req.validate()
        request = main_models.RevokeDataServiceApiShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.revoke_command):
            request.revoke_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.revoke_command, 'RevokeCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        body = {}
        if not DaraCore.is_null(request.revoke_command_shrink):
            body['RevokeCommand'] = request.revoke_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RevokeDataServiceApi',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokeDataServiceApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_data_service_api_with_options_async(
        self,
        tmp_req: main_models.RevokeDataServiceApiRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RevokeDataServiceApiResponse:
        tmp_req.validate()
        request = main_models.RevokeDataServiceApiShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.revoke_command):
            request.revoke_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.revoke_command, 'RevokeCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        body = {}
        if not DaraCore.is_null(request.revoke_command_shrink):
            body['RevokeCommand'] = request.revoke_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RevokeDataServiceApi',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokeDataServiceApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_data_service_api(
        self,
        request: main_models.RevokeDataServiceApiRequest,
    ) -> main_models.RevokeDataServiceApiResponse:
        runtime = RuntimeOptions()
        return self.revoke_data_service_api_with_options(request, runtime)

    async def revoke_data_service_api_async(
        self,
        request: main_models.RevokeDataServiceApiRequest,
    ) -> main_models.RevokeDataServiceApiResponse:
        runtime = RuntimeOptions()
        return await self.revoke_data_service_api_with_options_async(request, runtime)

    def revoke_resource_permission_with_options(
        self,
        tmp_req: main_models.RevokeResourcePermissionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RevokeResourcePermissionResponse:
        tmp_req.validate()
        request = main_models.RevokeResourcePermissionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.revoke_command):
            request.revoke_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.revoke_command, 'RevokeCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.revoke_command_shrink):
            body['RevokeCommand'] = request.revoke_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RevokeResourcePermission',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokeResourcePermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_resource_permission_with_options_async(
        self,
        tmp_req: main_models.RevokeResourcePermissionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RevokeResourcePermissionResponse:
        tmp_req.validate()
        request = main_models.RevokeResourcePermissionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.revoke_command):
            request.revoke_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.revoke_command, 'RevokeCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.revoke_command_shrink):
            body['RevokeCommand'] = request.revoke_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RevokeResourcePermission',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokeResourcePermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_resource_permission(
        self,
        request: main_models.RevokeResourcePermissionRequest,
    ) -> main_models.RevokeResourcePermissionResponse:
        runtime = RuntimeOptions()
        return self.revoke_resource_permission_with_options(request, runtime)

    async def revoke_resource_permission_async(
        self,
        request: main_models.RevokeResourcePermissionRequest,
    ) -> main_models.RevokeResourcePermissionResponse:
        runtime = RuntimeOptions()
        return await self.revoke_resource_permission_with_options_async(request, runtime)

    def stop_ad_hoc_task_with_options(
        self,
        request: main_models.StopAdHocTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopAdHocTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopAdHocTask',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopAdHocTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_ad_hoc_task_with_options_async(
        self,
        request: main_models.StopAdHocTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopAdHocTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopAdHocTask',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopAdHocTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_ad_hoc_task(
        self,
        request: main_models.StopAdHocTaskRequest,
    ) -> main_models.StopAdHocTaskResponse:
        runtime = RuntimeOptions()
        return self.stop_ad_hoc_task_with_options(request, runtime)

    async def stop_ad_hoc_task_async(
        self,
        request: main_models.StopAdHocTaskRequest,
    ) -> main_models.StopAdHocTaskResponse:
        runtime = RuntimeOptions()
        return await self.stop_ad_hoc_task_with_options_async(request, runtime)

    def submit_batch_task_with_options(
        self,
        tmp_req: main_models.SubmitBatchTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitBatchTaskResponse:
        tmp_req.validate()
        request = main_models.SubmitBatchTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.submit_command):
            request.submit_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.submit_command, 'SubmitCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.submit_command_shrink):
            body['SubmitCommand'] = request.submit_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitBatchTask',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitBatchTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_batch_task_with_options_async(
        self,
        tmp_req: main_models.SubmitBatchTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitBatchTaskResponse:
        tmp_req.validate()
        request = main_models.SubmitBatchTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.submit_command):
            request.submit_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.submit_command, 'SubmitCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.submit_command_shrink):
            body['SubmitCommand'] = request.submit_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitBatchTask',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitBatchTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_batch_task(
        self,
        request: main_models.SubmitBatchTaskRequest,
    ) -> main_models.SubmitBatchTaskResponse:
        runtime = RuntimeOptions()
        return self.submit_batch_task_with_options(request, runtime)

    async def submit_batch_task_async(
        self,
        request: main_models.SubmitBatchTaskRequest,
    ) -> main_models.SubmitBatchTaskResponse:
        runtime = RuntimeOptions()
        return await self.submit_batch_task_with_options_async(request, runtime)

    def submit_quality_rule_tasks_with_options(
        self,
        tmp_req: main_models.SubmitQualityRuleTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitQualityRuleTasksResponse:
        tmp_req.validate()
        request = main_models.SubmitQualityRuleTasksShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.submit_command):
            request.submit_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.submit_command, 'SubmitCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.submit_command_shrink):
            body['SubmitCommand'] = request.submit_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitQualityRuleTasks',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitQualityRuleTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_quality_rule_tasks_with_options_async(
        self,
        tmp_req: main_models.SubmitQualityRuleTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitQualityRuleTasksResponse:
        tmp_req.validate()
        request = main_models.SubmitQualityRuleTasksShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.submit_command):
            request.submit_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.submit_command, 'SubmitCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.submit_command_shrink):
            body['SubmitCommand'] = request.submit_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitQualityRuleTasks',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitQualityRuleTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_quality_rule_tasks(
        self,
        request: main_models.SubmitQualityRuleTasksRequest,
    ) -> main_models.SubmitQualityRuleTasksResponse:
        runtime = RuntimeOptions()
        return self.submit_quality_rule_tasks_with_options(request, runtime)

    async def submit_quality_rule_tasks_async(
        self,
        request: main_models.SubmitQualityRuleTasksRequest,
    ) -> main_models.SubmitQualityRuleTasksResponse:
        runtime = RuntimeOptions()
        return await self.submit_quality_rule_tasks_with_options_async(request, runtime)

    def submit_quality_watch_tasks_with_options(
        self,
        tmp_req: main_models.SubmitQualityWatchTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitQualityWatchTasksResponse:
        tmp_req.validate()
        request = main_models.SubmitQualityWatchTasksShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.submit_command):
            request.submit_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.submit_command, 'SubmitCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.submit_command_shrink):
            body['SubmitCommand'] = request.submit_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitQualityWatchTasks',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitQualityWatchTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_quality_watch_tasks_with_options_async(
        self,
        tmp_req: main_models.SubmitQualityWatchTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitQualityWatchTasksResponse:
        tmp_req.validate()
        request = main_models.SubmitQualityWatchTasksShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.submit_command):
            request.submit_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.submit_command, 'SubmitCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.submit_command_shrink):
            body['SubmitCommand'] = request.submit_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitQualityWatchTasks',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitQualityWatchTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_quality_watch_tasks(
        self,
        request: main_models.SubmitQualityWatchTasksRequest,
    ) -> main_models.SubmitQualityWatchTasksResponse:
        runtime = RuntimeOptions()
        return self.submit_quality_watch_tasks_with_options(request, runtime)

    async def submit_quality_watch_tasks_async(
        self,
        request: main_models.SubmitQualityWatchTasksRequest,
    ) -> main_models.SubmitQualityWatchTasksResponse:
        runtime = RuntimeOptions()
        return await self.submit_quality_watch_tasks_with_options_async(request, runtime)

    def sync_department_with_options(
        self,
        tmp_req: main_models.SyncDepartmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SyncDepartmentResponse:
        tmp_req.validate()
        request = main_models.SyncDepartmentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sync_department_command):
            request.sync_department_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.sync_department_command, 'SyncDepartmentCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.sync_department_command_shrink):
            body['SyncDepartmentCommand'] = request.sync_department_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SyncDepartment',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SyncDepartmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def sync_department_with_options_async(
        self,
        tmp_req: main_models.SyncDepartmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SyncDepartmentResponse:
        tmp_req.validate()
        request = main_models.SyncDepartmentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sync_department_command):
            request.sync_department_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.sync_department_command, 'SyncDepartmentCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.sync_department_command_shrink):
            body['SyncDepartmentCommand'] = request.sync_department_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SyncDepartment',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SyncDepartmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sync_department(
        self,
        request: main_models.SyncDepartmentRequest,
    ) -> main_models.SyncDepartmentResponse:
        runtime = RuntimeOptions()
        return self.sync_department_with_options(request, runtime)

    async def sync_department_async(
        self,
        request: main_models.SyncDepartmentRequest,
    ) -> main_models.SyncDepartmentResponse:
        runtime = RuntimeOptions()
        return await self.sync_department_with_options_async(request, runtime)

    def sync_department_user_with_options(
        self,
        tmp_req: main_models.SyncDepartmentUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SyncDepartmentUserResponse:
        tmp_req.validate()
        request = main_models.SyncDepartmentUserShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sync_department_user_command):
            request.sync_department_user_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.sync_department_user_command, 'SyncDepartmentUserCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.sync_department_user_command_shrink):
            body['SyncDepartmentUserCommand'] = request.sync_department_user_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SyncDepartmentUser',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SyncDepartmentUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def sync_department_user_with_options_async(
        self,
        tmp_req: main_models.SyncDepartmentUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SyncDepartmentUserResponse:
        tmp_req.validate()
        request = main_models.SyncDepartmentUserShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sync_department_user_command):
            request.sync_department_user_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.sync_department_user_command, 'SyncDepartmentUserCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.sync_department_user_command_shrink):
            body['SyncDepartmentUserCommand'] = request.sync_department_user_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SyncDepartmentUser',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SyncDepartmentUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sync_department_user(
        self,
        request: main_models.SyncDepartmentUserRequest,
    ) -> main_models.SyncDepartmentUserResponse:
        runtime = RuntimeOptions()
        return self.sync_department_user_with_options(request, runtime)

    async def sync_department_user_async(
        self,
        request: main_models.SyncDepartmentUserRequest,
    ) -> main_models.SyncDepartmentUserResponse:
        runtime = RuntimeOptions()
        return await self.sync_department_user_with_options_async(request, runtime)

    def transfer_ownership_for_all_object_with_options(
        self,
        tmp_req: main_models.TransferOwnershipForAllObjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TransferOwnershipForAllObjectResponse:
        tmp_req.validate()
        request = main_models.TransferOwnershipForAllObjectShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.privilege_transfer_record):
            request.privilege_transfer_record_shrink = Utils.array_to_string_with_specified_style(tmp_req.privilege_transfer_record, 'PrivilegeTransferRecord', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.privilege_transfer_record_shrink):
            body['PrivilegeTransferRecord'] = request.privilege_transfer_record_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TransferOwnershipForAllObject',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TransferOwnershipForAllObjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def transfer_ownership_for_all_object_with_options_async(
        self,
        tmp_req: main_models.TransferOwnershipForAllObjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TransferOwnershipForAllObjectResponse:
        tmp_req.validate()
        request = main_models.TransferOwnershipForAllObjectShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.privilege_transfer_record):
            request.privilege_transfer_record_shrink = Utils.array_to_string_with_specified_style(tmp_req.privilege_transfer_record, 'PrivilegeTransferRecord', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.privilege_transfer_record_shrink):
            body['PrivilegeTransferRecord'] = request.privilege_transfer_record_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TransferOwnershipForAllObject',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TransferOwnershipForAllObjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def transfer_ownership_for_all_object(
        self,
        request: main_models.TransferOwnershipForAllObjectRequest,
    ) -> main_models.TransferOwnershipForAllObjectResponse:
        runtime = RuntimeOptions()
        return self.transfer_ownership_for_all_object_with_options(request, runtime)

    async def transfer_ownership_for_all_object_async(
        self,
        request: main_models.TransferOwnershipForAllObjectRequest,
    ) -> main_models.TransferOwnershipForAllObjectResponse:
        runtime = RuntimeOptions()
        return await self.transfer_ownership_for_all_object_with_options_async(request, runtime)

    def update_ad_hoc_file_with_options(
        self,
        tmp_req: main_models.UpdateAdHocFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAdHocFileResponse:
        tmp_req.validate()
        request = main_models.UpdateAdHocFileShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_command):
            request.update_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAdHocFile',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAdHocFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ad_hoc_file_with_options_async(
        self,
        tmp_req: main_models.UpdateAdHocFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAdHocFileResponse:
        tmp_req.validate()
        request = main_models.UpdateAdHocFileShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_command):
            request.update_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAdHocFile',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAdHocFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ad_hoc_file(
        self,
        request: main_models.UpdateAdHocFileRequest,
    ) -> main_models.UpdateAdHocFileResponse:
        runtime = RuntimeOptions()
        return self.update_ad_hoc_file_with_options(request, runtime)

    async def update_ad_hoc_file_async(
        self,
        request: main_models.UpdateAdHocFileRequest,
    ) -> main_models.UpdateAdHocFileResponse:
        runtime = RuntimeOptions()
        return await self.update_ad_hoc_file_with_options_async(request, runtime)

    def update_batch_task_with_options(
        self,
        tmp_req: main_models.UpdateBatchTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateBatchTaskResponse:
        tmp_req.validate()
        request = main_models.UpdateBatchTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_command):
            request.update_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateBatchTask',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateBatchTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_batch_task_with_options_async(
        self,
        tmp_req: main_models.UpdateBatchTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateBatchTaskResponse:
        tmp_req.validate()
        request = main_models.UpdateBatchTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_command):
            request.update_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateBatchTask',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateBatchTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_batch_task(
        self,
        request: main_models.UpdateBatchTaskRequest,
    ) -> main_models.UpdateBatchTaskResponse:
        runtime = RuntimeOptions()
        return self.update_batch_task_with_options(request, runtime)

    async def update_batch_task_async(
        self,
        request: main_models.UpdateBatchTaskRequest,
    ) -> main_models.UpdateBatchTaskResponse:
        runtime = RuntimeOptions()
        return await self.update_batch_task_with_options_async(request, runtime)

    def update_batch_task_udf_lineages_with_options(
        self,
        tmp_req: main_models.UpdateBatchTaskUdfLineagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateBatchTaskUdfLineagesResponse:
        tmp_req.validate()
        request = main_models.UpdateBatchTaskUdfLineagesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_command):
            request.update_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateBatchTaskUdfLineages',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateBatchTaskUdfLineagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_batch_task_udf_lineages_with_options_async(
        self,
        tmp_req: main_models.UpdateBatchTaskUdfLineagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateBatchTaskUdfLineagesResponse:
        tmp_req.validate()
        request = main_models.UpdateBatchTaskUdfLineagesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_command):
            request.update_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateBatchTaskUdfLineages',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateBatchTaskUdfLineagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_batch_task_udf_lineages(
        self,
        request: main_models.UpdateBatchTaskUdfLineagesRequest,
    ) -> main_models.UpdateBatchTaskUdfLineagesResponse:
        runtime = RuntimeOptions()
        return self.update_batch_task_udf_lineages_with_options(request, runtime)

    async def update_batch_task_udf_lineages_async(
        self,
        request: main_models.UpdateBatchTaskUdfLineagesRequest,
    ) -> main_models.UpdateBatchTaskUdfLineagesResponse:
        runtime = RuntimeOptions()
        return await self.update_batch_task_udf_lineages_with_options_async(request, runtime)

    def update_biz_entity_with_options(
        self,
        tmp_req: main_models.UpdateBizEntityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateBizEntityResponse:
        tmp_req.validate()
        request = main_models.UpdateBizEntityShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_command):
            request.update_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateBizEntity',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateBizEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_biz_entity_with_options_async(
        self,
        tmp_req: main_models.UpdateBizEntityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateBizEntityResponse:
        tmp_req.validate()
        request = main_models.UpdateBizEntityShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_command):
            request.update_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateBizEntity',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateBizEntityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_biz_entity(
        self,
        request: main_models.UpdateBizEntityRequest,
    ) -> main_models.UpdateBizEntityResponse:
        runtime = RuntimeOptions()
        return self.update_biz_entity_with_options(request, runtime)

    async def update_biz_entity_async(
        self,
        request: main_models.UpdateBizEntityRequest,
    ) -> main_models.UpdateBizEntityResponse:
        runtime = RuntimeOptions()
        return await self.update_biz_entity_with_options_async(request, runtime)

    def update_biz_metric_with_options(
        self,
        tmp_req: main_models.UpdateBizMetricRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateBizMetricResponse:
        tmp_req.validate()
        request = main_models.UpdateBizMetricShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_biz_metric_command):
            request.update_biz_metric_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_biz_metric_command, 'UpdateBizMetricCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.update_biz_metric_command_shrink):
            body['UpdateBizMetricCommand'] = request.update_biz_metric_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateBizMetric',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateBizMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_biz_metric_with_options_async(
        self,
        tmp_req: main_models.UpdateBizMetricRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateBizMetricResponse:
        tmp_req.validate()
        request = main_models.UpdateBizMetricShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_biz_metric_command):
            request.update_biz_metric_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_biz_metric_command, 'UpdateBizMetricCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.update_biz_metric_command_shrink):
            body['UpdateBizMetricCommand'] = request.update_biz_metric_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateBizMetric',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateBizMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_biz_metric(
        self,
        request: main_models.UpdateBizMetricRequest,
    ) -> main_models.UpdateBizMetricResponse:
        runtime = RuntimeOptions()
        return self.update_biz_metric_with_options(request, runtime)

    async def update_biz_metric_async(
        self,
        request: main_models.UpdateBizMetricRequest,
    ) -> main_models.UpdateBizMetricResponse:
        runtime = RuntimeOptions()
        return await self.update_biz_metric_with_options_async(request, runtime)

    def update_biz_unit_with_options(
        self,
        tmp_req: main_models.UpdateBizUnitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateBizUnitResponse:
        tmp_req.validate()
        request = main_models.UpdateBizUnitShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_command):
            request.update_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateBizUnit',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateBizUnitResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_biz_unit_with_options_async(
        self,
        tmp_req: main_models.UpdateBizUnitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateBizUnitResponse:
        tmp_req.validate()
        request = main_models.UpdateBizUnitShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_command):
            request.update_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateBizUnit',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateBizUnitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_biz_unit(
        self,
        request: main_models.UpdateBizUnitRequest,
    ) -> main_models.UpdateBizUnitResponse:
        runtime = RuntimeOptions()
        return self.update_biz_unit_with_options(request, runtime)

    async def update_biz_unit_async(
        self,
        request: main_models.UpdateBizUnitRequest,
    ) -> main_models.UpdateBizUnitResponse:
        runtime = RuntimeOptions()
        return await self.update_biz_unit_with_options_async(request, runtime)

    def update_compute_source_with_options(
        self,
        tmp_req: main_models.UpdateComputeSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateComputeSourceResponse:
        tmp_req.validate()
        request = main_models.UpdateComputeSourceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_command):
            request.update_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateComputeSource',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateComputeSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_compute_source_with_options_async(
        self,
        tmp_req: main_models.UpdateComputeSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateComputeSourceResponse:
        tmp_req.validate()
        request = main_models.UpdateComputeSourceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_command):
            request.update_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateComputeSource',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateComputeSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_compute_source(
        self,
        request: main_models.UpdateComputeSourceRequest,
    ) -> main_models.UpdateComputeSourceResponse:
        runtime = RuntimeOptions()
        return self.update_compute_source_with_options(request, runtime)

    async def update_compute_source_async(
        self,
        request: main_models.UpdateComputeSourceRequest,
    ) -> main_models.UpdateComputeSourceResponse:
        runtime = RuntimeOptions()
        return await self.update_compute_source_with_options_async(request, runtime)

    def update_data_domain_with_options(
        self,
        tmp_req: main_models.UpdateDataDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataDomainResponse:
        tmp_req.validate()
        request = main_models.UpdateDataDomainShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_command):
            request.update_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataDomain',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_data_domain_with_options_async(
        self,
        tmp_req: main_models.UpdateDataDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataDomainResponse:
        tmp_req.validate()
        request = main_models.UpdateDataDomainShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_command):
            request.update_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataDomain',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_data_domain(
        self,
        request: main_models.UpdateDataDomainRequest,
    ) -> main_models.UpdateDataDomainResponse:
        runtime = RuntimeOptions()
        return self.update_data_domain_with_options(request, runtime)

    async def update_data_domain_async(
        self,
        request: main_models.UpdateDataDomainRequest,
    ) -> main_models.UpdateDataDomainResponse:
        runtime = RuntimeOptions()
        return await self.update_data_domain_with_options_async(request, runtime)

    def update_data_source_basic_info_with_options(
        self,
        tmp_req: main_models.UpdateDataSourceBasicInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataSourceBasicInfoResponse:
        tmp_req.validate()
        request = main_models.UpdateDataSourceBasicInfoShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_command):
            request.update_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataSourceBasicInfo',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataSourceBasicInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_data_source_basic_info_with_options_async(
        self,
        tmp_req: main_models.UpdateDataSourceBasicInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataSourceBasicInfoResponse:
        tmp_req.validate()
        request = main_models.UpdateDataSourceBasicInfoShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_command):
            request.update_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataSourceBasicInfo',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataSourceBasicInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_data_source_basic_info(
        self,
        request: main_models.UpdateDataSourceBasicInfoRequest,
    ) -> main_models.UpdateDataSourceBasicInfoResponse:
        runtime = RuntimeOptions()
        return self.update_data_source_basic_info_with_options(request, runtime)

    async def update_data_source_basic_info_async(
        self,
        request: main_models.UpdateDataSourceBasicInfoRequest,
    ) -> main_models.UpdateDataSourceBasicInfoResponse:
        runtime = RuntimeOptions()
        return await self.update_data_source_basic_info_with_options_async(request, runtime)

    def update_data_source_config_with_options(
        self,
        tmp_req: main_models.UpdateDataSourceConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataSourceConfigResponse:
        tmp_req.validate()
        request = main_models.UpdateDataSourceConfigShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_command):
            request.update_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataSourceConfig',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataSourceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_data_source_config_with_options_async(
        self,
        tmp_req: main_models.UpdateDataSourceConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataSourceConfigResponse:
        tmp_req.validate()
        request = main_models.UpdateDataSourceConfigShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_command):
            request.update_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataSourceConfig',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataSourceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_data_source_config(
        self,
        request: main_models.UpdateDataSourceConfigRequest,
    ) -> main_models.UpdateDataSourceConfigResponse:
        runtime = RuntimeOptions()
        return self.update_data_source_config_with_options(request, runtime)

    async def update_data_source_config_async(
        self,
        request: main_models.UpdateDataSourceConfigRequest,
    ) -> main_models.UpdateDataSourceConfigResponse:
        runtime = RuntimeOptions()
        return await self.update_data_source_config_with_options_async(request, runtime)

    def update_file_directory_with_options(
        self,
        request: main_models.UpdateFileDirectoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFileDirectoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory):
            query['Directory'] = request.directory
        if not DaraCore.is_null(request.file_id):
            query['FileId'] = request.file_id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFileDirectory',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFileDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_file_directory_with_options_async(
        self,
        request: main_models.UpdateFileDirectoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFileDirectoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory):
            query['Directory'] = request.directory
        if not DaraCore.is_null(request.file_id):
            query['FileId'] = request.file_id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFileDirectory',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFileDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_file_directory(
        self,
        request: main_models.UpdateFileDirectoryRequest,
    ) -> main_models.UpdateFileDirectoryResponse:
        runtime = RuntimeOptions()
        return self.update_file_directory_with_options(request, runtime)

    async def update_file_directory_async(
        self,
        request: main_models.UpdateFileDirectoryRequest,
    ) -> main_models.UpdateFileDirectoryResponse:
        runtime = RuntimeOptions()
        return await self.update_file_directory_with_options_async(request, runtime)

    def update_file_name_with_options(
        self,
        request: main_models.UpdateFileNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFileNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_id):
            query['FileId'] = request.file_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFileName',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFileNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_file_name_with_options_async(
        self,
        request: main_models.UpdateFileNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFileNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_id):
            query['FileId'] = request.file_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFileName',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFileNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_file_name(
        self,
        request: main_models.UpdateFileNameRequest,
    ) -> main_models.UpdateFileNameResponse:
        runtime = RuntimeOptions()
        return self.update_file_name_with_options(request, runtime)

    async def update_file_name_async(
        self,
        request: main_models.UpdateFileNameRequest,
    ) -> main_models.UpdateFileNameResponse:
        runtime = RuntimeOptions()
        return await self.update_file_name_with_options_async(request, runtime)

    def update_pipeline_with_options(
        self,
        tmp_req: main_models.UpdatePipelineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePipelineResponse:
        tmp_req.validate()
        request = main_models.UpdatePipelineShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.context):
            request.context_shrink = Utils.array_to_string_with_specified_style(tmp_req.context, 'Context', 'json')
        if not DaraCore.is_null(tmp_req.update_command):
            request.update_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.context_shrink):
            body['Context'] = request.context_shrink
        if not DaraCore.is_null(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePipeline',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_pipeline_with_options_async(
        self,
        tmp_req: main_models.UpdatePipelineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePipelineResponse:
        tmp_req.validate()
        request = main_models.UpdatePipelineShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.context):
            request.context_shrink = Utils.array_to_string_with_specified_style(tmp_req.context, 'Context', 'json')
        if not DaraCore.is_null(tmp_req.update_command):
            request.update_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.context_shrink):
            body['Context'] = request.context_shrink
        if not DaraCore.is_null(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePipeline',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePipelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_pipeline(
        self,
        request: main_models.UpdatePipelineRequest,
    ) -> main_models.UpdatePipelineResponse:
        runtime = RuntimeOptions()
        return self.update_pipeline_with_options(request, runtime)

    async def update_pipeline_async(
        self,
        request: main_models.UpdatePipelineRequest,
    ) -> main_models.UpdatePipelineResponse:
        runtime = RuntimeOptions()
        return await self.update_pipeline_with_options_async(request, runtime)

    def update_pipeline_by_async_with_options(
        self,
        tmp_req: main_models.UpdatePipelineByAsyncRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePipelineByAsyncResponse:
        tmp_req.validate()
        request = main_models.UpdatePipelineByAsyncShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.context):
            request.context_shrink = Utils.array_to_string_with_specified_style(tmp_req.context, 'Context', 'json')
        if not DaraCore.is_null(tmp_req.update_command):
            request.update_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.context_shrink):
            body['Context'] = request.context_shrink
        if not DaraCore.is_null(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePipelineByAsync',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePipelineByAsyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_pipeline_by_async_with_options_async(
        self,
        tmp_req: main_models.UpdatePipelineByAsyncRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePipelineByAsyncResponse:
        tmp_req.validate()
        request = main_models.UpdatePipelineByAsyncShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.context):
            request.context_shrink = Utils.array_to_string_with_specified_style(tmp_req.context, 'Context', 'json')
        if not DaraCore.is_null(tmp_req.update_command):
            request.update_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.context_shrink):
            body['Context'] = request.context_shrink
        if not DaraCore.is_null(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePipelineByAsync',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePipelineByAsyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_pipeline_by_async(
        self,
        request: main_models.UpdatePipelineByAsyncRequest,
    ) -> main_models.UpdatePipelineByAsyncResponse:
        runtime = RuntimeOptions()
        return self.update_pipeline_by_async_with_options(request, runtime)

    async def update_pipeline_by_async_async(
        self,
        request: main_models.UpdatePipelineByAsyncRequest,
    ) -> main_models.UpdatePipelineByAsyncResponse:
        runtime = RuntimeOptions()
        return await self.update_pipeline_by_async_with_options_async(request, runtime)

    def update_project_member_with_options(
        self,
        tmp_req: main_models.UpdateProjectMemberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateProjectMemberResponse:
        tmp_req.validate()
        request = main_models.UpdateProjectMemberShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_command):
            request.update_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateProjectMember',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateProjectMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_project_member_with_options_async(
        self,
        tmp_req: main_models.UpdateProjectMemberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateProjectMemberResponse:
        tmp_req.validate()
        request = main_models.UpdateProjectMemberShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_command):
            request.update_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateProjectMember',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateProjectMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_project_member(
        self,
        request: main_models.UpdateProjectMemberRequest,
    ) -> main_models.UpdateProjectMemberResponse:
        runtime = RuntimeOptions()
        return self.update_project_member_with_options(request, runtime)

    async def update_project_member_async(
        self,
        request: main_models.UpdateProjectMemberRequest,
    ) -> main_models.UpdateProjectMemberResponse:
        runtime = RuntimeOptions()
        return await self.update_project_member_with_options_async(request, runtime)

    def update_quality_rule_switch_with_options(
        self,
        tmp_req: main_models.UpdateQualityRuleSwitchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateQualityRuleSwitchResponse:
        tmp_req.validate()
        request = main_models.UpdateQualityRuleSwitchShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_command):
            request.update_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateQualityRuleSwitch',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateQualityRuleSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_quality_rule_switch_with_options_async(
        self,
        tmp_req: main_models.UpdateQualityRuleSwitchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateQualityRuleSwitchResponse:
        tmp_req.validate()
        request = main_models.UpdateQualityRuleSwitchShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_command):
            request.update_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateQualityRuleSwitch',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateQualityRuleSwitchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_quality_rule_switch(
        self,
        request: main_models.UpdateQualityRuleSwitchRequest,
    ) -> main_models.UpdateQualityRuleSwitchResponse:
        runtime = RuntimeOptions()
        return self.update_quality_rule_switch_with_options(request, runtime)

    async def update_quality_rule_switch_async(
        self,
        request: main_models.UpdateQualityRuleSwitchRequest,
    ) -> main_models.UpdateQualityRuleSwitchResponse:
        runtime = RuntimeOptions()
        return await self.update_quality_rule_switch_with_options_async(request, runtime)

    def update_quality_watch_switch_with_options(
        self,
        tmp_req: main_models.UpdateQualityWatchSwitchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateQualityWatchSwitchResponse:
        tmp_req.validate()
        request = main_models.UpdateQualityWatchSwitchShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_command):
            request.update_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateQualityWatchSwitch',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateQualityWatchSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_quality_watch_switch_with_options_async(
        self,
        tmp_req: main_models.UpdateQualityWatchSwitchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateQualityWatchSwitchResponse:
        tmp_req.validate()
        request = main_models.UpdateQualityWatchSwitchShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_command):
            request.update_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateQualityWatchSwitch',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateQualityWatchSwitchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_quality_watch_switch(
        self,
        request: main_models.UpdateQualityWatchSwitchRequest,
    ) -> main_models.UpdateQualityWatchSwitchResponse:
        runtime = RuntimeOptions()
        return self.update_quality_watch_switch_with_options(request, runtime)

    async def update_quality_watch_switch_async(
        self,
        request: main_models.UpdateQualityWatchSwitchRequest,
    ) -> main_models.UpdateQualityWatchSwitchResponse:
        runtime = RuntimeOptions()
        return await self.update_quality_watch_switch_with_options_async(request, runtime)

    def update_resource_with_options(
        self,
        tmp_req: main_models.UpdateResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateResourceResponse:
        tmp_req.validate()
        request = main_models.UpdateResourceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_command):
            request.update_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateResource',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_resource_with_options_async(
        self,
        tmp_req: main_models.UpdateResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateResourceResponse:
        tmp_req.validate()
        request = main_models.UpdateResourceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_command):
            request.update_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateResource',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_resource(
        self,
        request: main_models.UpdateResourceRequest,
    ) -> main_models.UpdateResourceResponse:
        runtime = RuntimeOptions()
        return self.update_resource_with_options(request, runtime)

    async def update_resource_async(
        self,
        request: main_models.UpdateResourceRequest,
    ) -> main_models.UpdateResourceResponse:
        runtime = RuntimeOptions()
        return await self.update_resource_with_options_async(request, runtime)

    def update_row_permission_with_options(
        self,
        tmp_req: main_models.UpdateRowPermissionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRowPermissionResponse:
        tmp_req.validate()
        request = main_models.UpdateRowPermissionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_row_permission_command):
            request.update_row_permission_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_row_permission_command, 'UpdateRowPermissionCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.update_row_permission_command_shrink):
            body['UpdateRowPermissionCommand'] = request.update_row_permission_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRowPermission',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRowPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_row_permission_with_options_async(
        self,
        tmp_req: main_models.UpdateRowPermissionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRowPermissionResponse:
        tmp_req.validate()
        request = main_models.UpdateRowPermissionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_row_permission_command):
            request.update_row_permission_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_row_permission_command, 'UpdateRowPermissionCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.update_row_permission_command_shrink):
            body['UpdateRowPermissionCommand'] = request.update_row_permission_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRowPermission',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRowPermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_row_permission(
        self,
        request: main_models.UpdateRowPermissionRequest,
    ) -> main_models.UpdateRowPermissionResponse:
        runtime = RuntimeOptions()
        return self.update_row_permission_with_options(request, runtime)

    async def update_row_permission_async(
        self,
        request: main_models.UpdateRowPermissionRequest,
    ) -> main_models.UpdateRowPermissionResponse:
        runtime = RuntimeOptions()
        return await self.update_row_permission_with_options_async(request, runtime)

    def update_security_classify_with_options(
        self,
        tmp_req: main_models.UpdateSecurityClassifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSecurityClassifyResponse:
        tmp_req.validate()
        request = main_models.UpdateSecurityClassifyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_command):
            request.update_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSecurityClassify',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSecurityClassifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_security_classify_with_options_async(
        self,
        tmp_req: main_models.UpdateSecurityClassifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSecurityClassifyResponse:
        tmp_req.validate()
        request = main_models.UpdateSecurityClassifyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_command):
            request.update_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSecurityClassify',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSecurityClassifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_security_classify(
        self,
        request: main_models.UpdateSecurityClassifyRequest,
    ) -> main_models.UpdateSecurityClassifyResponse:
        runtime = RuntimeOptions()
        return self.update_security_classify_with_options(request, runtime)

    async def update_security_classify_async(
        self,
        request: main_models.UpdateSecurityClassifyRequest,
    ) -> main_models.UpdateSecurityClassifyResponse:
        runtime = RuntimeOptions()
        return await self.update_security_classify_with_options_async(request, runtime)

    def update_security_classify_catalog_with_options(
        self,
        tmp_req: main_models.UpdateSecurityClassifyCatalogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSecurityClassifyCatalogResponse:
        tmp_req.validate()
        request = main_models.UpdateSecurityClassifyCatalogShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_command):
            request.update_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSecurityClassifyCatalog',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSecurityClassifyCatalogResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_security_classify_catalog_with_options_async(
        self,
        tmp_req: main_models.UpdateSecurityClassifyCatalogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSecurityClassifyCatalogResponse:
        tmp_req.validate()
        request = main_models.UpdateSecurityClassifyCatalogShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_command):
            request.update_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSecurityClassifyCatalog',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSecurityClassifyCatalogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_security_classify_catalog(
        self,
        request: main_models.UpdateSecurityClassifyCatalogRequest,
    ) -> main_models.UpdateSecurityClassifyCatalogResponse:
        runtime = RuntimeOptions()
        return self.update_security_classify_catalog_with_options(request, runtime)

    async def update_security_classify_catalog_async(
        self,
        request: main_models.UpdateSecurityClassifyCatalogRequest,
    ) -> main_models.UpdateSecurityClassifyCatalogResponse:
        runtime = RuntimeOptions()
        return await self.update_security_classify_catalog_with_options_async(request, runtime)

    def update_security_identify_result_status_with_options(
        self,
        tmp_req: main_models.UpdateSecurityIdentifyResultStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSecurityIdentifyResultStatusResponse:
        tmp_req.validate()
        request = main_models.UpdateSecurityIdentifyResultStatusShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_command):
            request.update_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSecurityIdentifyResultStatus',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSecurityIdentifyResultStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_security_identify_result_status_with_options_async(
        self,
        tmp_req: main_models.UpdateSecurityIdentifyResultStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSecurityIdentifyResultStatusResponse:
        tmp_req.validate()
        request = main_models.UpdateSecurityIdentifyResultStatusShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_command):
            request.update_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSecurityIdentifyResultStatus',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSecurityIdentifyResultStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_security_identify_result_status(
        self,
        request: main_models.UpdateSecurityIdentifyResultStatusRequest,
    ) -> main_models.UpdateSecurityIdentifyResultStatusResponse:
        runtime = RuntimeOptions()
        return self.update_security_identify_result_status_with_options(request, runtime)

    async def update_security_identify_result_status_async(
        self,
        request: main_models.UpdateSecurityIdentifyResultStatusRequest,
    ) -> main_models.UpdateSecurityIdentifyResultStatusResponse:
        runtime = RuntimeOptions()
        return await self.update_security_identify_result_status_with_options_async(request, runtime)

    def update_security_level_with_options(
        self,
        tmp_req: main_models.UpdateSecurityLevelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSecurityLevelResponse:
        tmp_req.validate()
        request = main_models.UpdateSecurityLevelShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_command):
            request.update_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSecurityLevel',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSecurityLevelResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_security_level_with_options_async(
        self,
        tmp_req: main_models.UpdateSecurityLevelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSecurityLevelResponse:
        tmp_req.validate()
        request = main_models.UpdateSecurityLevelShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_command):
            request.update_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSecurityLevel',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSecurityLevelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_security_level(
        self,
        request: main_models.UpdateSecurityLevelRequest,
    ) -> main_models.UpdateSecurityLevelResponse:
        runtime = RuntimeOptions()
        return self.update_security_level_with_options(request, runtime)

    async def update_security_level_async(
        self,
        request: main_models.UpdateSecurityLevelRequest,
    ) -> main_models.UpdateSecurityLevelResponse:
        runtime = RuntimeOptions()
        return await self.update_security_level_with_options_async(request, runtime)

    def update_standard_with_options(
        self,
        tmp_req: main_models.UpdateStandardRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateStandardResponse:
        tmp_req.validate()
        request = main_models.UpdateStandardShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_command):
            request.update_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateStandard',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateStandardResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_standard_with_options_async(
        self,
        tmp_req: main_models.UpdateStandardRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateStandardResponse:
        tmp_req.validate()
        request = main_models.UpdateStandardShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_command):
            request.update_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateStandard',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateStandardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_standard(
        self,
        request: main_models.UpdateStandardRequest,
    ) -> main_models.UpdateStandardResponse:
        runtime = RuntimeOptions()
        return self.update_standard_with_options(request, runtime)

    async def update_standard_async(
        self,
        request: main_models.UpdateStandardRequest,
    ) -> main_models.UpdateStandardResponse:
        runtime = RuntimeOptions()
        return await self.update_standard_with_options_async(request, runtime)

    def update_standard_lookup_table_with_options(
        self,
        tmp_req: main_models.UpdateStandardLookupTableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateStandardLookupTableResponse:
        tmp_req.validate()
        request = main_models.UpdateStandardLookupTableShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_command):
            request.update_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateStandardLookupTable',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateStandardLookupTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_standard_lookup_table_with_options_async(
        self,
        tmp_req: main_models.UpdateStandardLookupTableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateStandardLookupTableResponse:
        tmp_req.validate()
        request = main_models.UpdateStandardLookupTableShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_command):
            request.update_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateStandardLookupTable',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateStandardLookupTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_standard_lookup_table(
        self,
        request: main_models.UpdateStandardLookupTableRequest,
    ) -> main_models.UpdateStandardLookupTableResponse:
        runtime = RuntimeOptions()
        return self.update_standard_lookup_table_with_options(request, runtime)

    async def update_standard_lookup_table_async(
        self,
        request: main_models.UpdateStandardLookupTableRequest,
    ) -> main_models.UpdateStandardLookupTableResponse:
        runtime = RuntimeOptions()
        return await self.update_standard_lookup_table_with_options_async(request, runtime)

    def update_standard_mapping_to_invalid_with_options(
        self,
        tmp_req: main_models.UpdateStandardMappingToInvalidRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateStandardMappingToInvalidResponse:
        tmp_req.validate()
        request = main_models.UpdateStandardMappingToInvalidShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_command):
            request.update_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateStandardMappingToInvalid',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateStandardMappingToInvalidResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_standard_mapping_to_invalid_with_options_async(
        self,
        tmp_req: main_models.UpdateStandardMappingToInvalidRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateStandardMappingToInvalidResponse:
        tmp_req.validate()
        request = main_models.UpdateStandardMappingToInvalidShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_command):
            request.update_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateStandardMappingToInvalid',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateStandardMappingToInvalidResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_standard_mapping_to_invalid(
        self,
        request: main_models.UpdateStandardMappingToInvalidRequest,
    ) -> main_models.UpdateStandardMappingToInvalidResponse:
        runtime = RuntimeOptions()
        return self.update_standard_mapping_to_invalid_with_options(request, runtime)

    async def update_standard_mapping_to_invalid_async(
        self,
        request: main_models.UpdateStandardMappingToInvalidRequest,
    ) -> main_models.UpdateStandardMappingToInvalidResponse:
        runtime = RuntimeOptions()
        return await self.update_standard_mapping_to_invalid_with_options_async(request, runtime)

    def update_standard_set_with_options(
        self,
        tmp_req: main_models.UpdateStandardSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateStandardSetResponse:
        tmp_req.validate()
        request = main_models.UpdateStandardSetShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_command):
            request.update_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateStandardSet',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateStandardSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_standard_set_with_options_async(
        self,
        tmp_req: main_models.UpdateStandardSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateStandardSetResponse:
        tmp_req.validate()
        request = main_models.UpdateStandardSetShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_command):
            request.update_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateStandardSet',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateStandardSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_standard_set(
        self,
        request: main_models.UpdateStandardSetRequest,
    ) -> main_models.UpdateStandardSetResponse:
        runtime = RuntimeOptions()
        return self.update_standard_set_with_options(request, runtime)

    async def update_standard_set_async(
        self,
        request: main_models.UpdateStandardSetRequest,
    ) -> main_models.UpdateStandardSetResponse:
        runtime = RuntimeOptions()
        return await self.update_standard_set_with_options_async(request, runtime)

    def update_standard_template_with_options(
        self,
        tmp_req: main_models.UpdateStandardTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateStandardTemplateResponse:
        tmp_req.validate()
        request = main_models.UpdateStandardTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_command):
            request.update_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateStandardTemplate',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateStandardTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_standard_template_with_options_async(
        self,
        tmp_req: main_models.UpdateStandardTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateStandardTemplateResponse:
        tmp_req.validate()
        request = main_models.UpdateStandardTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_command):
            request.update_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateStandardTemplate',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateStandardTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_standard_template(
        self,
        request: main_models.UpdateStandardTemplateRequest,
    ) -> main_models.UpdateStandardTemplateResponse:
        runtime = RuntimeOptions()
        return self.update_standard_template_with_options(request, runtime)

    async def update_standard_template_async(
        self,
        request: main_models.UpdateStandardTemplateRequest,
    ) -> main_models.UpdateStandardTemplateResponse:
        runtime = RuntimeOptions()
        return await self.update_standard_template_with_options_async(request, runtime)

    def update_standard_word_root_with_options(
        self,
        tmp_req: main_models.UpdateStandardWordRootRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateStandardWordRootResponse:
        tmp_req.validate()
        request = main_models.UpdateStandardWordRootShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_command):
            request.update_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateStandardWordRoot',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateStandardWordRootResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_standard_word_root_with_options_async(
        self,
        tmp_req: main_models.UpdateStandardWordRootRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateStandardWordRootResponse:
        tmp_req.validate()
        request = main_models.UpdateStandardWordRootShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_command):
            request.update_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateStandardWordRoot',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateStandardWordRootResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_standard_word_root(
        self,
        request: main_models.UpdateStandardWordRootRequest,
    ) -> main_models.UpdateStandardWordRootResponse:
        runtime = RuntimeOptions()
        return self.update_standard_word_root_with_options(request, runtime)

    async def update_standard_word_root_async(
        self,
        request: main_models.UpdateStandardWordRootRequest,
    ) -> main_models.UpdateStandardWordRootResponse:
        runtime = RuntimeOptions()
        return await self.update_standard_word_root_with_options_async(request, runtime)

    def update_tenant_compute_engine_with_options(
        self,
        tmp_req: main_models.UpdateTenantComputeEngineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTenantComputeEngineResponse:
        tmp_req.validate()
        request = main_models.UpdateTenantComputeEngineShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_command):
            request.update_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTenantComputeEngine',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTenantComputeEngineResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_tenant_compute_engine_with_options_async(
        self,
        tmp_req: main_models.UpdateTenantComputeEngineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTenantComputeEngineResponse:
        tmp_req.validate()
        request = main_models.UpdateTenantComputeEngineShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_command):
            request.update_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTenantComputeEngine',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTenantComputeEngineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_tenant_compute_engine(
        self,
        request: main_models.UpdateTenantComputeEngineRequest,
    ) -> main_models.UpdateTenantComputeEngineResponse:
        runtime = RuntimeOptions()
        return self.update_tenant_compute_engine_with_options(request, runtime)

    async def update_tenant_compute_engine_async(
        self,
        request: main_models.UpdateTenantComputeEngineRequest,
    ) -> main_models.UpdateTenantComputeEngineResponse:
        runtime = RuntimeOptions()
        return await self.update_tenant_compute_engine_with_options_async(request, runtime)

    def update_tenant_member_with_options(
        self,
        tmp_req: main_models.UpdateTenantMemberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTenantMemberResponse:
        tmp_req.validate()
        request = main_models.UpdateTenantMemberShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_command):
            request.update_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTenantMember',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTenantMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_tenant_member_with_options_async(
        self,
        tmp_req: main_models.UpdateTenantMemberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTenantMemberResponse:
        tmp_req.validate()
        request = main_models.UpdateTenantMemberShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_command):
            request.update_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTenantMember',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTenantMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_tenant_member(
        self,
        request: main_models.UpdateTenantMemberRequest,
    ) -> main_models.UpdateTenantMemberResponse:
        runtime = RuntimeOptions()
        return self.update_tenant_member_with_options(request, runtime)

    async def update_tenant_member_async(
        self,
        request: main_models.UpdateTenantMemberRequest,
    ) -> main_models.UpdateTenantMemberResponse:
        runtime = RuntimeOptions()
        return await self.update_tenant_member_with_options_async(request, runtime)

    def update_udf_with_options(
        self,
        tmp_req: main_models.UpdateUdfRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUdfResponse:
        tmp_req.validate()
        request = main_models.UpdateUdfShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_command):
            request.update_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUdf',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUdfResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_udf_with_options_async(
        self,
        tmp_req: main_models.UpdateUdfRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUdfResponse:
        tmp_req.validate()
        request = main_models.UpdateUdfShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_command):
            request.update_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUdf',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUdfResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_udf(
        self,
        request: main_models.UpdateUdfRequest,
    ) -> main_models.UpdateUdfResponse:
        runtime = RuntimeOptions()
        return self.update_udf_with_options(request, runtime)

    async def update_udf_async(
        self,
        request: main_models.UpdateUdfRequest,
    ) -> main_models.UpdateUdfResponse:
        runtime = RuntimeOptions()
        return await self.update_udf_with_options_async(request, runtime)

    def update_user_group_with_options(
        self,
        tmp_req: main_models.UpdateUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserGroupResponse:
        tmp_req.validate()
        request = main_models.UpdateUserGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_command):
            request.update_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUserGroup',
            version = '2023-06-30',
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
        tmp_req: main_models.UpdateUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserGroupResponse:
        tmp_req.validate()
        request = main_models.UpdateUserGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.update_command):
            request.update_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUserGroup',
            version = '2023-06-30',
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

    def update_user_group_switch_with_options(
        self,
        request: main_models.UpdateUserGroupSwitchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserGroupSwitchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.active):
            query['Active'] = request.active
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUserGroupSwitch',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUserGroupSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_group_switch_with_options_async(
        self,
        request: main_models.UpdateUserGroupSwitchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserGroupSwitchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.active):
            query['Active'] = request.active
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not DaraCore.is_null(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUserGroupSwitch',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUserGroupSwitchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user_group_switch(
        self,
        request: main_models.UpdateUserGroupSwitchRequest,
    ) -> main_models.UpdateUserGroupSwitchResponse:
        runtime = RuntimeOptions()
        return self.update_user_group_switch_with_options(request, runtime)

    async def update_user_group_switch_async(
        self,
        request: main_models.UpdateUserGroupSwitchRequest,
    ) -> main_models.UpdateUserGroupSwitchResponse:
        runtime = RuntimeOptions()
        return await self.update_user_group_switch_with_options_async(request, runtime)

    def upsert_quality_rule_with_options(
        self,
        tmp_req: main_models.UpsertQualityRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpsertQualityRuleResponse:
        tmp_req.validate()
        request = main_models.UpsertQualityRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.upsert_command):
            request.upsert_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.upsert_command, 'UpsertCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.upsert_command_shrink):
            body['UpsertCommand'] = request.upsert_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpsertQualityRule',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpsertQualityRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def upsert_quality_rule_with_options_async(
        self,
        tmp_req: main_models.UpsertQualityRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpsertQualityRuleResponse:
        tmp_req.validate()
        request = main_models.UpsertQualityRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.upsert_command):
            request.upsert_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.upsert_command, 'UpsertCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.upsert_command_shrink):
            body['UpsertCommand'] = request.upsert_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpsertQualityRule',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpsertQualityRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upsert_quality_rule(
        self,
        request: main_models.UpsertQualityRuleRequest,
    ) -> main_models.UpsertQualityRuleResponse:
        runtime = RuntimeOptions()
        return self.upsert_quality_rule_with_options(request, runtime)

    async def upsert_quality_rule_async(
        self,
        request: main_models.UpsertQualityRuleRequest,
    ) -> main_models.UpsertQualityRuleResponse:
        runtime = RuntimeOptions()
        return await self.upsert_quality_rule_with_options_async(request, runtime)

    def upsert_quality_schedule_with_options(
        self,
        tmp_req: main_models.UpsertQualityScheduleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpsertQualityScheduleResponse:
        tmp_req.validate()
        request = main_models.UpsertQualityScheduleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.upsert_command):
            request.upsert_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.upsert_command, 'UpsertCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.upsert_command_shrink):
            body['UpsertCommand'] = request.upsert_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpsertQualitySchedule',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpsertQualityScheduleResponse(),
            self.call_api(params, req, runtime)
        )

    async def upsert_quality_schedule_with_options_async(
        self,
        tmp_req: main_models.UpsertQualityScheduleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpsertQualityScheduleResponse:
        tmp_req.validate()
        request = main_models.UpsertQualityScheduleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.upsert_command):
            request.upsert_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.upsert_command, 'UpsertCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.upsert_command_shrink):
            body['UpsertCommand'] = request.upsert_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpsertQualitySchedule',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpsertQualityScheduleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upsert_quality_schedule(
        self,
        request: main_models.UpsertQualityScheduleRequest,
    ) -> main_models.UpsertQualityScheduleResponse:
        runtime = RuntimeOptions()
        return self.upsert_quality_schedule_with_options(request, runtime)

    async def upsert_quality_schedule_async(
        self,
        request: main_models.UpsertQualityScheduleRequest,
    ) -> main_models.UpsertQualityScheduleResponse:
        runtime = RuntimeOptions()
        return await self.upsert_quality_schedule_with_options_async(request, runtime)

    def upsert_quality_template_with_options(
        self,
        tmp_req: main_models.UpsertQualityTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpsertQualityTemplateResponse:
        tmp_req.validate()
        request = main_models.UpsertQualityTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.upsert_command):
            request.upsert_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.upsert_command, 'UpsertCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.upsert_command_shrink):
            body['UpsertCommand'] = request.upsert_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpsertQualityTemplate',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpsertQualityTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def upsert_quality_template_with_options_async(
        self,
        tmp_req: main_models.UpsertQualityTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpsertQualityTemplateResponse:
        tmp_req.validate()
        request = main_models.UpsertQualityTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.upsert_command):
            request.upsert_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.upsert_command, 'UpsertCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.upsert_command_shrink):
            body['UpsertCommand'] = request.upsert_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpsertQualityTemplate',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpsertQualityTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upsert_quality_template(
        self,
        request: main_models.UpsertQualityTemplateRequest,
    ) -> main_models.UpsertQualityTemplateResponse:
        runtime = RuntimeOptions()
        return self.upsert_quality_template_with_options(request, runtime)

    async def upsert_quality_template_async(
        self,
        request: main_models.UpsertQualityTemplateRequest,
    ) -> main_models.UpsertQualityTemplateResponse:
        runtime = RuntimeOptions()
        return await self.upsert_quality_template_with_options_async(request, runtime)

    def upsert_quality_watch_with_options(
        self,
        tmp_req: main_models.UpsertQualityWatchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpsertQualityWatchResponse:
        tmp_req.validate()
        request = main_models.UpsertQualityWatchShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.upsert_command):
            request.upsert_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.upsert_command, 'UpsertCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.upsert_command_shrink):
            body['UpsertCommand'] = request.upsert_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpsertQualityWatch',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpsertQualityWatchResponse(),
            self.call_api(params, req, runtime)
        )

    async def upsert_quality_watch_with_options_async(
        self,
        tmp_req: main_models.UpsertQualityWatchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpsertQualityWatchResponse:
        tmp_req.validate()
        request = main_models.UpsertQualityWatchShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.upsert_command):
            request.upsert_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.upsert_command, 'UpsertCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.upsert_command_shrink):
            body['UpsertCommand'] = request.upsert_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpsertQualityWatch',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpsertQualityWatchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upsert_quality_watch(
        self,
        request: main_models.UpsertQualityWatchRequest,
    ) -> main_models.UpsertQualityWatchResponse:
        runtime = RuntimeOptions()
        return self.upsert_quality_watch_with_options(request, runtime)

    async def upsert_quality_watch_async(
        self,
        request: main_models.UpsertQualityWatchRequest,
    ) -> main_models.UpsertQualityWatchResponse:
        runtime = RuntimeOptions()
        return await self.upsert_quality_watch_with_options_async(request, runtime)

    def upsert_quality_watch_alert_with_options(
        self,
        tmp_req: main_models.UpsertQualityWatchAlertRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpsertQualityWatchAlertResponse:
        tmp_req.validate()
        request = main_models.UpsertQualityWatchAlertShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.upsert_command):
            request.upsert_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.upsert_command, 'UpsertCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.upsert_command_shrink):
            body['UpsertCommand'] = request.upsert_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpsertQualityWatchAlert',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpsertQualityWatchAlertResponse(),
            self.call_api(params, req, runtime)
        )

    async def upsert_quality_watch_alert_with_options_async(
        self,
        tmp_req: main_models.UpsertQualityWatchAlertRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpsertQualityWatchAlertResponse:
        tmp_req.validate()
        request = main_models.UpsertQualityWatchAlertShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.upsert_command):
            request.upsert_command_shrink = Utils.array_to_string_with_specified_style(tmp_req.upsert_command, 'UpsertCommand', 'json')
        query = {}
        if not DaraCore.is_null(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not DaraCore.is_null(request.upsert_command_shrink):
            body['UpsertCommand'] = request.upsert_command_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpsertQualityWatchAlert',
            version = '2023-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpsertQualityWatchAlertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upsert_quality_watch_alert(
        self,
        request: main_models.UpsertQualityWatchAlertRequest,
    ) -> main_models.UpsertQualityWatchAlertResponse:
        runtime = RuntimeOptions()
        return self.upsert_quality_watch_alert_with_options(request, runtime)

    async def upsert_quality_watch_alert_async(
        self,
        request: main_models.UpsertQualityWatchAlertRequest,
    ) -> main_models.UpsertQualityWatchAlertResponse:
        runtime = RuntimeOptions()
        return await self.upsert_quality_watch_alert_with_options_async(request, runtime)
