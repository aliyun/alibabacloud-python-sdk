# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dataphin_public20230630 import models as dataphin_public_20230630_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_tenant_members_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.AddTenantMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.AddTenantMembersResponse:
        """
        @summary 新增租户成员
        
        @param tmp_req: AddTenantMembersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddTenantMembersResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.AddTenantMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.add_command):
            request.add_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.add_command, 'AddCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.add_command_shrink):
            body['AddCommand'] = request.add_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddTenantMembers',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.AddTenantMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_tenant_members_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.AddTenantMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.AddTenantMembersResponse:
        """
        @summary 新增租户成员
        
        @param tmp_req: AddTenantMembersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddTenantMembersResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.AddTenantMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.add_command):
            request.add_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.add_command, 'AddCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.add_command_shrink):
            body['AddCommand'] = request.add_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddTenantMembers',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.AddTenantMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_tenant_members(
        self,
        request: dataphin_public_20230630_models.AddTenantMembersRequest,
    ) -> dataphin_public_20230630_models.AddTenantMembersResponse:
        """
        @summary 新增租户成员
        
        @param request: AddTenantMembersRequest
        @return: AddTenantMembersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_tenant_members_with_options(request, runtime)

    async def add_tenant_members_async(
        self,
        request: dataphin_public_20230630_models.AddTenantMembersRequest,
    ) -> dataphin_public_20230630_models.AddTenantMembersResponse:
        """
        @summary 新增租户成员
        
        @param request: AddTenantMembersRequest
        @return: AddTenantMembersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_tenant_members_with_options_async(request, runtime)

    def add_tenant_members_by_source_user_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.AddTenantMembersBySourceUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.AddTenantMembersBySourceUserResponse:
        """
        @summary 通过原始用户添加租户成员.
        
        @param tmp_req: AddTenantMembersBySourceUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddTenantMembersBySourceUserResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.AddTenantMembersBySourceUserShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.add_command):
            request.add_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.add_command, 'AddCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.add_command_shrink):
            body['AddCommand'] = request.add_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddTenantMembersBySourceUser',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.AddTenantMembersBySourceUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_tenant_members_by_source_user_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.AddTenantMembersBySourceUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.AddTenantMembersBySourceUserResponse:
        """
        @summary 通过原始用户添加租户成员.
        
        @param tmp_req: AddTenantMembersBySourceUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddTenantMembersBySourceUserResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.AddTenantMembersBySourceUserShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.add_command):
            request.add_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.add_command, 'AddCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.add_command_shrink):
            body['AddCommand'] = request.add_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddTenantMembersBySourceUser',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.AddTenantMembersBySourceUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_tenant_members_by_source_user(
        self,
        request: dataphin_public_20230630_models.AddTenantMembersBySourceUserRequest,
    ) -> dataphin_public_20230630_models.AddTenantMembersBySourceUserResponse:
        """
        @summary 通过原始用户添加租户成员.
        
        @param request: AddTenantMembersBySourceUserRequest
        @return: AddTenantMembersBySourceUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_tenant_members_by_source_user_with_options(request, runtime)

    async def add_tenant_members_by_source_user_async(
        self,
        request: dataphin_public_20230630_models.AddTenantMembersBySourceUserRequest,
    ) -> dataphin_public_20230630_models.AddTenantMembersBySourceUserResponse:
        """
        @summary 通过原始用户添加租户成员.
        
        @param request: AddTenantMembersBySourceUserRequest
        @return: AddTenantMembersBySourceUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_tenant_members_by_source_user_with_options_async(request, runtime)

    def add_user_group_member_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.AddUserGroupMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.AddUserGroupMemberResponse:
        """
        @summary 添加用户组成员.
        
        @param tmp_req: AddUserGroupMemberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddUserGroupMemberResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.AddUserGroupMemberShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.add_command):
            request.add_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.add_command, 'AddCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.add_command_shrink):
            body['AddCommand'] = request.add_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddUserGroupMember',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.AddUserGroupMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_user_group_member_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.AddUserGroupMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.AddUserGroupMemberResponse:
        """
        @summary 添加用户组成员.
        
        @param tmp_req: AddUserGroupMemberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddUserGroupMemberResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.AddUserGroupMemberShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.add_command):
            request.add_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.add_command, 'AddCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.add_command_shrink):
            body['AddCommand'] = request.add_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddUserGroupMember',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.AddUserGroupMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_user_group_member(
        self,
        request: dataphin_public_20230630_models.AddUserGroupMemberRequest,
    ) -> dataphin_public_20230630_models.AddUserGroupMemberResponse:
        """
        @summary 添加用户组成员.
        
        @param request: AddUserGroupMemberRequest
        @return: AddUserGroupMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_user_group_member_with_options(request, runtime)

    async def add_user_group_member_async(
        self,
        request: dataphin_public_20230630_models.AddUserGroupMemberRequest,
    ) -> dataphin_public_20230630_models.AddUserGroupMemberResponse:
        """
        @summary 添加用户组成员.
        
        @param request: AddUserGroupMemberRequest
        @return: AddUserGroupMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_user_group_member_with_options_async(request, runtime)

    def check_data_source_connectivity_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.CheckDataSourceConnectivityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.CheckDataSourceConnectivityResponse:
        """
        @summary 检查数据源连通性
        
        @param tmp_req: CheckDataSourceConnectivityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckDataSourceConnectivityResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.CheckDataSourceConnectivityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.check_command):
            request.check_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.check_command, 'CheckCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.check_command_shrink):
            body['CheckCommand'] = request.check_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CheckDataSourceConnectivity',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.CheckDataSourceConnectivityResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_data_source_connectivity_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.CheckDataSourceConnectivityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.CheckDataSourceConnectivityResponse:
        """
        @summary 检查数据源连通性
        
        @param tmp_req: CheckDataSourceConnectivityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckDataSourceConnectivityResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.CheckDataSourceConnectivityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.check_command):
            request.check_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.check_command, 'CheckCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.check_command_shrink):
            body['CheckCommand'] = request.check_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CheckDataSourceConnectivity',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.CheckDataSourceConnectivityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_data_source_connectivity(
        self,
        request: dataphin_public_20230630_models.CheckDataSourceConnectivityRequest,
    ) -> dataphin_public_20230630_models.CheckDataSourceConnectivityResponse:
        """
        @summary 检查数据源连通性
        
        @param request: CheckDataSourceConnectivityRequest
        @return: CheckDataSourceConnectivityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_data_source_connectivity_with_options(request, runtime)

    async def check_data_source_connectivity_async(
        self,
        request: dataphin_public_20230630_models.CheckDataSourceConnectivityRequest,
    ) -> dataphin_public_20230630_models.CheckDataSourceConnectivityResponse:
        """
        @summary 检查数据源连通性
        
        @param request: CheckDataSourceConnectivityRequest
        @return: CheckDataSourceConnectivityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_data_source_connectivity_with_options_async(request, runtime)

    def check_data_source_connectivity_by_id_with_options(
        self,
        request: dataphin_public_20230630_models.CheckDataSourceConnectivityByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.CheckDataSourceConnectivityByIdResponse:
        """
        @summary 检查已创建的数据源是否正常连通
        
        @param request: CheckDataSourceConnectivityByIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckDataSourceConnectivityByIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckDataSourceConnectivityById',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.CheckDataSourceConnectivityByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_data_source_connectivity_by_id_with_options_async(
        self,
        request: dataphin_public_20230630_models.CheckDataSourceConnectivityByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.CheckDataSourceConnectivityByIdResponse:
        """
        @summary 检查已创建的数据源是否正常连通
        
        @param request: CheckDataSourceConnectivityByIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckDataSourceConnectivityByIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckDataSourceConnectivityById',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.CheckDataSourceConnectivityByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_data_source_connectivity_by_id(
        self,
        request: dataphin_public_20230630_models.CheckDataSourceConnectivityByIdRequest,
    ) -> dataphin_public_20230630_models.CheckDataSourceConnectivityByIdResponse:
        """
        @summary 检查已创建的数据源是否正常连通
        
        @param request: CheckDataSourceConnectivityByIdRequest
        @return: CheckDataSourceConnectivityByIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_data_source_connectivity_by_id_with_options(request, runtime)

    async def check_data_source_connectivity_by_id_async(
        self,
        request: dataphin_public_20230630_models.CheckDataSourceConnectivityByIdRequest,
    ) -> dataphin_public_20230630_models.CheckDataSourceConnectivityByIdResponse:
        """
        @summary 检查已创建的数据源是否正常连通
        
        @param request: CheckDataSourceConnectivityByIdRequest
        @return: CheckDataSourceConnectivityByIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_data_source_connectivity_by_id_with_options_async(request, runtime)

    def check_resource_permission_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.CheckResourcePermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.CheckResourcePermissionResponse:
        """
        @summary 校验用户是否有指定资源权限点.
        
        @param tmp_req: CheckResourcePermissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckResourcePermissionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.CheckResourcePermissionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.check_command):
            request.check_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.check_command, 'CheckCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.check_command_shrink):
            body['CheckCommand'] = request.check_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CheckResourcePermission',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.CheckResourcePermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_resource_permission_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.CheckResourcePermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.CheckResourcePermissionResponse:
        """
        @summary 校验用户是否有指定资源权限点.
        
        @param tmp_req: CheckResourcePermissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckResourcePermissionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.CheckResourcePermissionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.check_command):
            request.check_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.check_command, 'CheckCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.check_command_shrink):
            body['CheckCommand'] = request.check_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CheckResourcePermission',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.CheckResourcePermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_resource_permission(
        self,
        request: dataphin_public_20230630_models.CheckResourcePermissionRequest,
    ) -> dataphin_public_20230630_models.CheckResourcePermissionResponse:
        """
        @summary 校验用户是否有指定资源权限点.
        
        @param request: CheckResourcePermissionRequest
        @return: CheckResourcePermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_resource_permission_with_options(request, runtime)

    async def check_resource_permission_async(
        self,
        request: dataphin_public_20230630_models.CheckResourcePermissionRequest,
    ) -> dataphin_public_20230630_models.CheckResourcePermissionResponse:
        """
        @summary 校验用户是否有指定资源权限点.
        
        @param request: CheckResourcePermissionRequest
        @return: CheckResourcePermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_resource_permission_with_options_async(request, runtime)

    def create_ad_hoc_file_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.CreateAdHocFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.CreateAdHocFileResponse:
        """
        @summary 创建即席查询文件
        
        @param tmp_req: CreateAdHocFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAdHocFileResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.CreateAdHocFileShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_command):
            request.create_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAdHocFile',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.CreateAdHocFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ad_hoc_file_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.CreateAdHocFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.CreateAdHocFileResponse:
        """
        @summary 创建即席查询文件
        
        @param tmp_req: CreateAdHocFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAdHocFileResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.CreateAdHocFileShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_command):
            request.create_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAdHocFile',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.CreateAdHocFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ad_hoc_file(
        self,
        request: dataphin_public_20230630_models.CreateAdHocFileRequest,
    ) -> dataphin_public_20230630_models.CreateAdHocFileResponse:
        """
        @summary 创建即席查询文件
        
        @param request: CreateAdHocFileRequest
        @return: CreateAdHocFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_ad_hoc_file_with_options(request, runtime)

    async def create_ad_hoc_file_async(
        self,
        request: dataphin_public_20230630_models.CreateAdHocFileRequest,
    ) -> dataphin_public_20230630_models.CreateAdHocFileResponse:
        """
        @summary 创建即席查询文件
        
        @param request: CreateAdHocFileRequest
        @return: CreateAdHocFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_ad_hoc_file_with_options_async(request, runtime)

    def create_batch_task_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.CreateBatchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.CreateBatchTaskResponse:
        """
        @summary 创建离线计算任务。
        
        @param tmp_req: CreateBatchTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBatchTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.CreateBatchTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_command):
            request.create_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateBatchTask',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.CreateBatchTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_batch_task_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.CreateBatchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.CreateBatchTaskResponse:
        """
        @summary 创建离线计算任务。
        
        @param tmp_req: CreateBatchTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBatchTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.CreateBatchTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_command):
            request.create_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateBatchTask',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.CreateBatchTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_batch_task(
        self,
        request: dataphin_public_20230630_models.CreateBatchTaskRequest,
    ) -> dataphin_public_20230630_models.CreateBatchTaskResponse:
        """
        @summary 创建离线计算任务。
        
        @param request: CreateBatchTaskRequest
        @return: CreateBatchTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_batch_task_with_options(request, runtime)

    async def create_batch_task_async(
        self,
        request: dataphin_public_20230630_models.CreateBatchTaskRequest,
    ) -> dataphin_public_20230630_models.CreateBatchTaskResponse:
        """
        @summary 创建离线计算任务。
        
        @param request: CreateBatchTaskRequest
        @return: CreateBatchTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_batch_task_with_options_async(request, runtime)

    def create_biz_entity_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.CreateBizEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.CreateBizEntityResponse:
        """
        @summary 创建业务实体。
        
        @param tmp_req: CreateBizEntityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBizEntityResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.CreateBizEntityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_command):
            request.create_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateBizEntity',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.CreateBizEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_biz_entity_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.CreateBizEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.CreateBizEntityResponse:
        """
        @summary 创建业务实体。
        
        @param tmp_req: CreateBizEntityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBizEntityResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.CreateBizEntityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_command):
            request.create_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateBizEntity',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.CreateBizEntityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_biz_entity(
        self,
        request: dataphin_public_20230630_models.CreateBizEntityRequest,
    ) -> dataphin_public_20230630_models.CreateBizEntityResponse:
        """
        @summary 创建业务实体。
        
        @param request: CreateBizEntityRequest
        @return: CreateBizEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_biz_entity_with_options(request, runtime)

    async def create_biz_entity_async(
        self,
        request: dataphin_public_20230630_models.CreateBizEntityRequest,
    ) -> dataphin_public_20230630_models.CreateBizEntityResponse:
        """
        @summary 创建业务实体。
        
        @param request: CreateBizEntityRequest
        @return: CreateBizEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_biz_entity_with_options_async(request, runtime)

    def create_biz_unit_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.CreateBizUnitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.CreateBizUnitResponse:
        """
        @summary 创建数据板块。
        
        @param tmp_req: CreateBizUnitRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBizUnitResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.CreateBizUnitShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_command):
            request.create_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateBizUnit',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.CreateBizUnitResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_biz_unit_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.CreateBizUnitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.CreateBizUnitResponse:
        """
        @summary 创建数据板块。
        
        @param tmp_req: CreateBizUnitRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBizUnitResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.CreateBizUnitShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_command):
            request.create_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateBizUnit',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.CreateBizUnitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_biz_unit(
        self,
        request: dataphin_public_20230630_models.CreateBizUnitRequest,
    ) -> dataphin_public_20230630_models.CreateBizUnitResponse:
        """
        @summary 创建数据板块。
        
        @param request: CreateBizUnitRequest
        @return: CreateBizUnitResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_biz_unit_with_options(request, runtime)

    async def create_biz_unit_async(
        self,
        request: dataphin_public_20230630_models.CreateBizUnitRequest,
    ) -> dataphin_public_20230630_models.CreateBizUnitResponse:
        """
        @summary 创建数据板块。
        
        @param request: CreateBizUnitRequest
        @return: CreateBizUnitResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_biz_unit_with_options_async(request, runtime)

    def create_data_domain_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.CreateDataDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.CreateDataDomainResponse:
        """
        @summary 创建主题域。
        
        @param tmp_req: CreateDataDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDataDomainResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.CreateDataDomainShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_command):
            request.create_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDataDomain',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.CreateDataDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_domain_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.CreateDataDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.CreateDataDomainResponse:
        """
        @summary 创建主题域。
        
        @param tmp_req: CreateDataDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDataDomainResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.CreateDataDomainShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_command):
            request.create_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDataDomain',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.CreateDataDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_domain(
        self,
        request: dataphin_public_20230630_models.CreateDataDomainRequest,
    ) -> dataphin_public_20230630_models.CreateDataDomainResponse:
        """
        @summary 创建主题域。
        
        @param request: CreateDataDomainRequest
        @return: CreateDataDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_data_domain_with_options(request, runtime)

    async def create_data_domain_async(
        self,
        request: dataphin_public_20230630_models.CreateDataDomainRequest,
    ) -> dataphin_public_20230630_models.CreateDataDomainResponse:
        """
        @summary 创建主题域。
        
        @param request: CreateDataDomainRequest
        @return: CreateDataDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_data_domain_with_options_async(request, runtime)

    def create_data_source_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.CreateDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.CreateDataSourceResponse:
        """
        @summary 新建数据源
        
        @param tmp_req: CreateDataSourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDataSourceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.CreateDataSourceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_command):
            request.create_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDataSource',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.CreateDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_source_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.CreateDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.CreateDataSourceResponse:
        """
        @summary 新建数据源
        
        @param tmp_req: CreateDataSourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDataSourceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.CreateDataSourceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_command):
            request.create_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDataSource',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.CreateDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_source(
        self,
        request: dataphin_public_20230630_models.CreateDataSourceRequest,
    ) -> dataphin_public_20230630_models.CreateDataSourceResponse:
        """
        @summary 新建数据源
        
        @param request: CreateDataSourceRequest
        @return: CreateDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_data_source_with_options(request, runtime)

    async def create_data_source_async(
        self,
        request: dataphin_public_20230630_models.CreateDataSourceRequest,
    ) -> dataphin_public_20230630_models.CreateDataSourceResponse:
        """
        @summary 新建数据源
        
        @param request: CreateDataSourceRequest
        @return: CreateDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_data_source_with_options_async(request, runtime)

    def create_directory_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.CreateDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.CreateDirectoryResponse:
        """
        @summary 创建菜单树文件目录
        
        @param tmp_req: CreateDirectoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDirectoryResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.CreateDirectoryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_command):
            request.create_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDirectory',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.CreateDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_directory_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.CreateDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.CreateDirectoryResponse:
        """
        @summary 创建菜单树文件目录
        
        @param tmp_req: CreateDirectoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDirectoryResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.CreateDirectoryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_command):
            request.create_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDirectory',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.CreateDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_directory(
        self,
        request: dataphin_public_20230630_models.CreateDirectoryRequest,
    ) -> dataphin_public_20230630_models.CreateDirectoryResponse:
        """
        @summary 创建菜单树文件目录
        
        @param request: CreateDirectoryRequest
        @return: CreateDirectoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_directory_with_options(request, runtime)

    async def create_directory_async(
        self,
        request: dataphin_public_20230630_models.CreateDirectoryRequest,
    ) -> dataphin_public_20230630_models.CreateDirectoryResponse:
        """
        @summary 创建菜单树文件目录
        
        @param request: CreateDirectoryRequest
        @return: CreateDirectoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_directory_with_options_async(request, runtime)

    def create_node_supplement_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.CreateNodeSupplementRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.CreateNodeSupplementResponse:
        """
        @summary 通用补数据接口 1.会生成补数据实例运行：影响相关产产出表数据 2.会进行任务运行：造成计算的费用以及存储的费用
        
        @param tmp_req: CreateNodeSupplementRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateNodeSupplementResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.CreateNodeSupplementShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_command):
            request.create_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateNodeSupplement',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.CreateNodeSupplementResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_node_supplement_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.CreateNodeSupplementRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.CreateNodeSupplementResponse:
        """
        @summary 通用补数据接口 1.会生成补数据实例运行：影响相关产产出表数据 2.会进行任务运行：造成计算的费用以及存储的费用
        
        @param tmp_req: CreateNodeSupplementRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateNodeSupplementResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.CreateNodeSupplementShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_command):
            request.create_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateNodeSupplement',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.CreateNodeSupplementResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_node_supplement(
        self,
        request: dataphin_public_20230630_models.CreateNodeSupplementRequest,
    ) -> dataphin_public_20230630_models.CreateNodeSupplementResponse:
        """
        @summary 通用补数据接口 1.会生成补数据实例运行：影响相关产产出表数据 2.会进行任务运行：造成计算的费用以及存储的费用
        
        @param request: CreateNodeSupplementRequest
        @return: CreateNodeSupplementResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_node_supplement_with_options(request, runtime)

    async def create_node_supplement_async(
        self,
        request: dataphin_public_20230630_models.CreateNodeSupplementRequest,
    ) -> dataphin_public_20230630_models.CreateNodeSupplementResponse:
        """
        @summary 通用补数据接口 1.会生成补数据实例运行：影响相关产产出表数据 2.会进行任务运行：造成计算的费用以及存储的费用
        
        @param request: CreateNodeSupplementRequest
        @return: CreateNodeSupplementResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_node_supplement_with_options_async(request, runtime)

    def create_pipeline_node_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.CreatePipelineNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.CreatePipelineNodeResponse:
        """
        @summary 创建数据集成任务。
        
        @param tmp_req: CreatePipelineNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePipelineNodeResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.CreatePipelineNodeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_pipeline_node_command):
            request.create_pipeline_node_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.create_pipeline_node_command, 'CreatePipelineNodeCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.create_pipeline_node_command_shrink):
            body['CreatePipelineNodeCommand'] = request.create_pipeline_node_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePipelineNode',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.CreatePipelineNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_pipeline_node_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.CreatePipelineNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.CreatePipelineNodeResponse:
        """
        @summary 创建数据集成任务。
        
        @param tmp_req: CreatePipelineNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePipelineNodeResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.CreatePipelineNodeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_pipeline_node_command):
            request.create_pipeline_node_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.create_pipeline_node_command, 'CreatePipelineNodeCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.create_pipeline_node_command_shrink):
            body['CreatePipelineNodeCommand'] = request.create_pipeline_node_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePipelineNode',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.CreatePipelineNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_pipeline_node(
        self,
        request: dataphin_public_20230630_models.CreatePipelineNodeRequest,
    ) -> dataphin_public_20230630_models.CreatePipelineNodeResponse:
        """
        @summary 创建数据集成任务。
        
        @param request: CreatePipelineNodeRequest
        @return: CreatePipelineNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_pipeline_node_with_options(request, runtime)

    async def create_pipeline_node_async(
        self,
        request: dataphin_public_20230630_models.CreatePipelineNodeRequest,
    ) -> dataphin_public_20230630_models.CreatePipelineNodeResponse:
        """
        @summary 创建数据集成任务。
        
        @param request: CreatePipelineNodeRequest
        @return: CreatePipelineNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_pipeline_node_with_options_async(request, runtime)

    def create_stream_batch_job_mapping_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.CreateStreamBatchJobMappingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.CreateStreamBatchJobMappingResponse:
        """
        @summary 创建流批一体任务
        
        @param tmp_req: CreateStreamBatchJobMappingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateStreamBatchJobMappingResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.CreateStreamBatchJobMappingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.stream_batch_job_mapping_create_command):
            request.stream_batch_job_mapping_create_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.stream_batch_job_mapping_create_command, 'StreamBatchJobMappingCreateCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.stream_batch_job_mapping_create_command_shrink):
            body['StreamBatchJobMappingCreateCommand'] = request.stream_batch_job_mapping_create_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateStreamBatchJobMapping',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.CreateStreamBatchJobMappingResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_stream_batch_job_mapping_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.CreateStreamBatchJobMappingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.CreateStreamBatchJobMappingResponse:
        """
        @summary 创建流批一体任务
        
        @param tmp_req: CreateStreamBatchJobMappingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateStreamBatchJobMappingResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.CreateStreamBatchJobMappingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.stream_batch_job_mapping_create_command):
            request.stream_batch_job_mapping_create_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.stream_batch_job_mapping_create_command, 'StreamBatchJobMappingCreateCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.stream_batch_job_mapping_create_command_shrink):
            body['StreamBatchJobMappingCreateCommand'] = request.stream_batch_job_mapping_create_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateStreamBatchJobMapping',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.CreateStreamBatchJobMappingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_stream_batch_job_mapping(
        self,
        request: dataphin_public_20230630_models.CreateStreamBatchJobMappingRequest,
    ) -> dataphin_public_20230630_models.CreateStreamBatchJobMappingResponse:
        """
        @summary 创建流批一体任务
        
        @param request: CreateStreamBatchJobMappingRequest
        @return: CreateStreamBatchJobMappingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_stream_batch_job_mapping_with_options(request, runtime)

    async def create_stream_batch_job_mapping_async(
        self,
        request: dataphin_public_20230630_models.CreateStreamBatchJobMappingRequest,
    ) -> dataphin_public_20230630_models.CreateStreamBatchJobMappingResponse:
        """
        @summary 创建流批一体任务
        
        @param request: CreateStreamBatchJobMappingRequest
        @return: CreateStreamBatchJobMappingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_stream_batch_job_mapping_with_options_async(request, runtime)

    def create_user_group_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.CreateUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.CreateUserGroupResponse:
        """
        @summary 新建用户组.
        
        @param tmp_req: CreateUserGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateUserGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.CreateUserGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_command):
            request.create_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateUserGroup',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.CreateUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_user_group_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.CreateUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.CreateUserGroupResponse:
        """
        @summary 新建用户组.
        
        @param tmp_req: CreateUserGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateUserGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.CreateUserGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_command):
            request.create_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.create_command, 'CreateCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.create_command_shrink):
            body['CreateCommand'] = request.create_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateUserGroup',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.CreateUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_user_group(
        self,
        request: dataphin_public_20230630_models.CreateUserGroupRequest,
    ) -> dataphin_public_20230630_models.CreateUserGroupResponse:
        """
        @summary 新建用户组.
        
        @param request: CreateUserGroupRequest
        @return: CreateUserGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_user_group_with_options(request, runtime)

    async def create_user_group_async(
        self,
        request: dataphin_public_20230630_models.CreateUserGroupRequest,
    ) -> dataphin_public_20230630_models.CreateUserGroupResponse:
        """
        @summary 新建用户组.
        
        @param request: CreateUserGroupRequest
        @return: CreateUserGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_user_group_with_options_async(request, runtime)

    def delete_ad_hoc_file_with_options(
        self,
        request: dataphin_public_20230630_models.DeleteAdHocFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.DeleteAdHocFileResponse:
        """
        @summary 删除菜单树即席查询文件
        
        @param request: DeleteAdHocFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAdHocFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_id):
            query['FileId'] = request.file_id
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAdHocFile',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.DeleteAdHocFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ad_hoc_file_with_options_async(
        self,
        request: dataphin_public_20230630_models.DeleteAdHocFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.DeleteAdHocFileResponse:
        """
        @summary 删除菜单树即席查询文件
        
        @param request: DeleteAdHocFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAdHocFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_id):
            query['FileId'] = request.file_id
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAdHocFile',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.DeleteAdHocFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ad_hoc_file(
        self,
        request: dataphin_public_20230630_models.DeleteAdHocFileRequest,
    ) -> dataphin_public_20230630_models.DeleteAdHocFileResponse:
        """
        @summary 删除菜单树即席查询文件
        
        @param request: DeleteAdHocFileRequest
        @return: DeleteAdHocFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_ad_hoc_file_with_options(request, runtime)

    async def delete_ad_hoc_file_async(
        self,
        request: dataphin_public_20230630_models.DeleteAdHocFileRequest,
    ) -> dataphin_public_20230630_models.DeleteAdHocFileResponse:
        """
        @summary 删除菜单树即席查询文件
        
        @param request: DeleteAdHocFileRequest
        @return: DeleteAdHocFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_ad_hoc_file_with_options_async(request, runtime)

    def delete_batch_task_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.DeleteBatchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.DeleteBatchTaskResponse:
        """
        @summary 删除离线计算任务，如果任务还没下线需要先下线再删除。
        
        @param tmp_req: DeleteBatchTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteBatchTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.DeleteBatchTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.delete_command):
            request.delete_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.delete_command, 'DeleteCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.delete_command_shrink):
            body['DeleteCommand'] = request.delete_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteBatchTask',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.DeleteBatchTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_batch_task_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.DeleteBatchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.DeleteBatchTaskResponse:
        """
        @summary 删除离线计算任务，如果任务还没下线需要先下线再删除。
        
        @param tmp_req: DeleteBatchTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteBatchTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.DeleteBatchTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.delete_command):
            request.delete_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.delete_command, 'DeleteCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.delete_command_shrink):
            body['DeleteCommand'] = request.delete_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteBatchTask',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.DeleteBatchTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_batch_task(
        self,
        request: dataphin_public_20230630_models.DeleteBatchTaskRequest,
    ) -> dataphin_public_20230630_models.DeleteBatchTaskResponse:
        """
        @summary 删除离线计算任务，如果任务还没下线需要先下线再删除。
        
        @param request: DeleteBatchTaskRequest
        @return: DeleteBatchTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_batch_task_with_options(request, runtime)

    async def delete_batch_task_async(
        self,
        request: dataphin_public_20230630_models.DeleteBatchTaskRequest,
    ) -> dataphin_public_20230630_models.DeleteBatchTaskResponse:
        """
        @summary 删除离线计算任务，如果任务还没下线需要先下线再删除。
        
        @param request: DeleteBatchTaskRequest
        @return: DeleteBatchTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_batch_task_with_options_async(request, runtime)

    def delete_biz_entity_with_options(
        self,
        request: dataphin_public_20230630_models.DeleteBizEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.DeleteBizEntityResponse:
        """
        @summary 删除业务实体。
        
        @param request: DeleteBizEntityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteBizEntityResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_unit_id):
            query['BizUnitId'] = request.biz_unit_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBizEntity',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.DeleteBizEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_biz_entity_with_options_async(
        self,
        request: dataphin_public_20230630_models.DeleteBizEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.DeleteBizEntityResponse:
        """
        @summary 删除业务实体。
        
        @param request: DeleteBizEntityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteBizEntityResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_unit_id):
            query['BizUnitId'] = request.biz_unit_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBizEntity',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.DeleteBizEntityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_biz_entity(
        self,
        request: dataphin_public_20230630_models.DeleteBizEntityRequest,
    ) -> dataphin_public_20230630_models.DeleteBizEntityResponse:
        """
        @summary 删除业务实体。
        
        @param request: DeleteBizEntityRequest
        @return: DeleteBizEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_biz_entity_with_options(request, runtime)

    async def delete_biz_entity_async(
        self,
        request: dataphin_public_20230630_models.DeleteBizEntityRequest,
    ) -> dataphin_public_20230630_models.DeleteBizEntityResponse:
        """
        @summary 删除业务实体。
        
        @param request: DeleteBizEntityRequest
        @return: DeleteBizEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_biz_entity_with_options_async(request, runtime)

    def delete_biz_unit_with_options(
        self,
        request: dataphin_public_20230630_models.DeleteBizUnitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.DeleteBizUnitResponse:
        """
        @summary 删除数据板块。
        
        @param request: DeleteBizUnitRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteBizUnitResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBizUnit',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.DeleteBizUnitResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_biz_unit_with_options_async(
        self,
        request: dataphin_public_20230630_models.DeleteBizUnitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.DeleteBizUnitResponse:
        """
        @summary 删除数据板块。
        
        @param request: DeleteBizUnitRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteBizUnitResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBizUnit',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.DeleteBizUnitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_biz_unit(
        self,
        request: dataphin_public_20230630_models.DeleteBizUnitRequest,
    ) -> dataphin_public_20230630_models.DeleteBizUnitResponse:
        """
        @summary 删除数据板块。
        
        @param request: DeleteBizUnitRequest
        @return: DeleteBizUnitResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_biz_unit_with_options(request, runtime)

    async def delete_biz_unit_async(
        self,
        request: dataphin_public_20230630_models.DeleteBizUnitRequest,
    ) -> dataphin_public_20230630_models.DeleteBizUnitResponse:
        """
        @summary 删除数据板块。
        
        @param request: DeleteBizUnitRequest
        @return: DeleteBizUnitResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_biz_unit_with_options_async(request, runtime)

    def delete_data_domain_with_options(
        self,
        request: dataphin_public_20230630_models.DeleteDataDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.DeleteDataDomainResponse:
        """
        @summary 删除主题域。
        
        @param request: DeleteDataDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDataDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_unit_id):
            query['BizUnitId'] = request.biz_unit_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDataDomain',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.DeleteDataDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_domain_with_options_async(
        self,
        request: dataphin_public_20230630_models.DeleteDataDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.DeleteDataDomainResponse:
        """
        @summary 删除主题域。
        
        @param request: DeleteDataDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDataDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_unit_id):
            query['BizUnitId'] = request.biz_unit_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDataDomain',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.DeleteDataDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_domain(
        self,
        request: dataphin_public_20230630_models.DeleteDataDomainRequest,
    ) -> dataphin_public_20230630_models.DeleteDataDomainResponse:
        """
        @summary 删除主题域。
        
        @param request: DeleteDataDomainRequest
        @return: DeleteDataDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_data_domain_with_options(request, runtime)

    async def delete_data_domain_async(
        self,
        request: dataphin_public_20230630_models.DeleteDataDomainRequest,
    ) -> dataphin_public_20230630_models.DeleteDataDomainResponse:
        """
        @summary 删除主题域。
        
        @param request: DeleteDataDomainRequest
        @return: DeleteDataDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_data_domain_with_options_async(request, runtime)

    def delete_data_source_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.DeleteDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.DeleteDataSourceResponse:
        """
        @summary 删除数据源
        
        @param tmp_req: DeleteDataSourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDataSourceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.DeleteDataSourceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.delete_command):
            request.delete_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.delete_command, 'DeleteCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.delete_command_shrink):
            body['DeleteCommand'] = request.delete_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDataSource',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.DeleteDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_source_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.DeleteDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.DeleteDataSourceResponse:
        """
        @summary 删除数据源
        
        @param tmp_req: DeleteDataSourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDataSourceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.DeleteDataSourceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.delete_command):
            request.delete_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.delete_command, 'DeleteCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.delete_command_shrink):
            body['DeleteCommand'] = request.delete_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDataSource',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.DeleteDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_source(
        self,
        request: dataphin_public_20230630_models.DeleteDataSourceRequest,
    ) -> dataphin_public_20230630_models.DeleteDataSourceResponse:
        """
        @summary 删除数据源
        
        @param request: DeleteDataSourceRequest
        @return: DeleteDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_data_source_with_options(request, runtime)

    async def delete_data_source_async(
        self,
        request: dataphin_public_20230630_models.DeleteDataSourceRequest,
    ) -> dataphin_public_20230630_models.DeleteDataSourceResponse:
        """
        @summary 删除数据源
        
        @param request: DeleteDataSourceRequest
        @return: DeleteDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_data_source_with_options_async(request, runtime)

    def delete_directory_with_options(
        self,
        request: dataphin_public_20230630_models.DeleteDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.DeleteDirectoryResponse:
        """
        @summary 删除菜单树文件目录
        
        @param request: DeleteDirectoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDirectoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_id):
            query['FileId'] = request.file_id
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDirectory',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.DeleteDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_directory_with_options_async(
        self,
        request: dataphin_public_20230630_models.DeleteDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.DeleteDirectoryResponse:
        """
        @summary 删除菜单树文件目录
        
        @param request: DeleteDirectoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDirectoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_id):
            query['FileId'] = request.file_id
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDirectory',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.DeleteDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_directory(
        self,
        request: dataphin_public_20230630_models.DeleteDirectoryRequest,
    ) -> dataphin_public_20230630_models.DeleteDirectoryResponse:
        """
        @summary 删除菜单树文件目录
        
        @param request: DeleteDirectoryRequest
        @return: DeleteDirectoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_directory_with_options(request, runtime)

    async def delete_directory_async(
        self,
        request: dataphin_public_20230630_models.DeleteDirectoryRequest,
    ) -> dataphin_public_20230630_models.DeleteDirectoryResponse:
        """
        @summary 删除菜单树文件目录
        
        @param request: DeleteDirectoryRequest
        @return: DeleteDirectoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_directory_with_options_async(request, runtime)

    def delete_user_group_with_options(
        self,
        request: dataphin_public_20230630_models.DeleteUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.DeleteUserGroupResponse:
        """
        @summary 删除用户组.
        
        @param request: DeleteUserGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUserGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUserGroup',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.DeleteUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_group_with_options_async(
        self,
        request: dataphin_public_20230630_models.DeleteUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.DeleteUserGroupResponse:
        """
        @summary 删除用户组.
        
        @param request: DeleteUserGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUserGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUserGroup',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.DeleteUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user_group(
        self,
        request: dataphin_public_20230630_models.DeleteUserGroupRequest,
    ) -> dataphin_public_20230630_models.DeleteUserGroupResponse:
        """
        @summary 删除用户组.
        
        @param request: DeleteUserGroupRequest
        @return: DeleteUserGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_user_group_with_options(request, runtime)

    async def delete_user_group_async(
        self,
        request: dataphin_public_20230630_models.DeleteUserGroupRequest,
    ) -> dataphin_public_20230630_models.DeleteUserGroupResponse:
        """
        @summary 删除用户组.
        
        @param request: DeleteUserGroupRequest
        @return: DeleteUserGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_group_with_options_async(request, runtime)

    def execute_ad_hoc_task_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.ExecuteAdHocTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.ExecuteAdHocTaskResponse:
        """
        @summary 执行即席查询任务。
        
        @param tmp_req: ExecuteAdHocTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteAdHocTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.ExecuteAdHocTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.execute_command):
            request.execute_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.execute_command, 'ExecuteCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.execute_command_shrink):
            body['ExecuteCommand'] = request.execute_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteAdHocTask',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.ExecuteAdHocTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_ad_hoc_task_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.ExecuteAdHocTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.ExecuteAdHocTaskResponse:
        """
        @summary 执行即席查询任务。
        
        @param tmp_req: ExecuteAdHocTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteAdHocTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.ExecuteAdHocTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.execute_command):
            request.execute_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.execute_command, 'ExecuteCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.execute_command_shrink):
            body['ExecuteCommand'] = request.execute_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteAdHocTask',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.ExecuteAdHocTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_ad_hoc_task(
        self,
        request: dataphin_public_20230630_models.ExecuteAdHocTaskRequest,
    ) -> dataphin_public_20230630_models.ExecuteAdHocTaskResponse:
        """
        @summary 执行即席查询任务。
        
        @param request: ExecuteAdHocTaskRequest
        @return: ExecuteAdHocTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.execute_ad_hoc_task_with_options(request, runtime)

    async def execute_ad_hoc_task_async(
        self,
        request: dataphin_public_20230630_models.ExecuteAdHocTaskRequest,
    ) -> dataphin_public_20230630_models.ExecuteAdHocTaskResponse:
        """
        @summary 执行即席查询任务。
        
        @param request: ExecuteAdHocTaskRequest
        @return: ExecuteAdHocTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.execute_ad_hoc_task_with_options_async(request, runtime)

    def execute_manual_node_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.ExecuteManualNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.ExecuteManualNodeResponse:
        """
        @summary 运行手动调度节点。
        
        @param tmp_req: ExecuteManualNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteManualNodeResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.ExecuteManualNodeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.execute_command):
            request.execute_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.execute_command, 'ExecuteCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.execute_command_shrink):
            body['ExecuteCommand'] = request.execute_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteManualNode',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.ExecuteManualNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_manual_node_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.ExecuteManualNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.ExecuteManualNodeResponse:
        """
        @summary 运行手动调度节点。
        
        @param tmp_req: ExecuteManualNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteManualNodeResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.ExecuteManualNodeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.execute_command):
            request.execute_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.execute_command, 'ExecuteCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.execute_command_shrink):
            body['ExecuteCommand'] = request.execute_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteManualNode',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.ExecuteManualNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_manual_node(
        self,
        request: dataphin_public_20230630_models.ExecuteManualNodeRequest,
    ) -> dataphin_public_20230630_models.ExecuteManualNodeResponse:
        """
        @summary 运行手动调度节点。
        
        @param request: ExecuteManualNodeRequest
        @return: ExecuteManualNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.execute_manual_node_with_options(request, runtime)

    async def execute_manual_node_async(
        self,
        request: dataphin_public_20230630_models.ExecuteManualNodeRequest,
    ) -> dataphin_public_20230630_models.ExecuteManualNodeResponse:
        """
        @summary 运行手动调度节点。
        
        @param request: ExecuteManualNodeRequest
        @return: ExecuteManualNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.execute_manual_node_with_options_async(request, runtime)

    def fix_data_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.FixDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.FixDataResponse:
        """
        @summary 重跑下游(修复链路数据), 支持强制重跑下游。影响范围: 1. 会产生计算成本；2. 会影响数据产出
        
        @param tmp_req: FixDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FixDataResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.FixDataShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.fix_data_command):
            request.fix_data_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.fix_data_command, 'FixDataCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.fix_data_command_shrink):
            body['FixDataCommand'] = request.fix_data_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FixData',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.FixDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def fix_data_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.FixDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.FixDataResponse:
        """
        @summary 重跑下游(修复链路数据), 支持强制重跑下游。影响范围: 1. 会产生计算成本；2. 会影响数据产出
        
        @param tmp_req: FixDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FixDataResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.FixDataShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.fix_data_command):
            request.fix_data_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.fix_data_command, 'FixDataCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.fix_data_command_shrink):
            body['FixDataCommand'] = request.fix_data_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FixData',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.FixDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def fix_data(
        self,
        request: dataphin_public_20230630_models.FixDataRequest,
    ) -> dataphin_public_20230630_models.FixDataResponse:
        """
        @summary 重跑下游(修复链路数据), 支持强制重跑下游。影响范围: 1. 会产生计算成本；2. 会影响数据产出
        
        @param request: FixDataRequest
        @return: FixDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.fix_data_with_options(request, runtime)

    async def fix_data_async(
        self,
        request: dataphin_public_20230630_models.FixDataRequest,
    ) -> dataphin_public_20230630_models.FixDataResponse:
        """
        @summary 重跑下游(修复链路数据), 支持强制重跑下游。影响范围: 1. 会产生计算成本；2. 会影响数据产出
        
        @param request: FixDataRequest
        @return: FixDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.fix_data_with_options_async(request, runtime)

    def get_ad_hoc_file_with_options(
        self,
        request: dataphin_public_20230630_models.GetAdHocFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetAdHocFileResponse:
        """
        @summary 查询即席查询文件。
        
        @param request: GetAdHocFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAdHocFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_id):
            query['FileId'] = request.file_id
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAdHocFile',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetAdHocFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ad_hoc_file_with_options_async(
        self,
        request: dataphin_public_20230630_models.GetAdHocFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetAdHocFileResponse:
        """
        @summary 查询即席查询文件。
        
        @param request: GetAdHocFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAdHocFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_id):
            query['FileId'] = request.file_id
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAdHocFile',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetAdHocFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ad_hoc_file(
        self,
        request: dataphin_public_20230630_models.GetAdHocFileRequest,
    ) -> dataphin_public_20230630_models.GetAdHocFileResponse:
        """
        @summary 查询即席查询文件。
        
        @param request: GetAdHocFileRequest
        @return: GetAdHocFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_ad_hoc_file_with_options(request, runtime)

    async def get_ad_hoc_file_async(
        self,
        request: dataphin_public_20230630_models.GetAdHocFileRequest,
    ) -> dataphin_public_20230630_models.GetAdHocFileResponse:
        """
        @summary 查询即席查询文件。
        
        @param request: GetAdHocFileRequest
        @return: GetAdHocFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_ad_hoc_file_with_options_async(request, runtime)

    def get_ad_hoc_task_log_with_options(
        self,
        request: dataphin_public_20230630_models.GetAdHocTaskLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetAdHocTaskLogResponse:
        """
        @summary 获取即席查询任务运行日志。
        
        @param request: GetAdHocTaskLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAdHocTaskLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.offset):
            query['Offset'] = request.offset
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.sub_task_id):
            query['SubTaskId'] = request.sub_task_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAdHocTaskLog',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetAdHocTaskLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ad_hoc_task_log_with_options_async(
        self,
        request: dataphin_public_20230630_models.GetAdHocTaskLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetAdHocTaskLogResponse:
        """
        @summary 获取即席查询任务运行日志。
        
        @param request: GetAdHocTaskLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAdHocTaskLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.offset):
            query['Offset'] = request.offset
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.sub_task_id):
            query['SubTaskId'] = request.sub_task_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAdHocTaskLog',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetAdHocTaskLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ad_hoc_task_log(
        self,
        request: dataphin_public_20230630_models.GetAdHocTaskLogRequest,
    ) -> dataphin_public_20230630_models.GetAdHocTaskLogResponse:
        """
        @summary 获取即席查询任务运行日志。
        
        @param request: GetAdHocTaskLogRequest
        @return: GetAdHocTaskLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_ad_hoc_task_log_with_options(request, runtime)

    async def get_ad_hoc_task_log_async(
        self,
        request: dataphin_public_20230630_models.GetAdHocTaskLogRequest,
    ) -> dataphin_public_20230630_models.GetAdHocTaskLogResponse:
        """
        @summary 获取即席查询任务运行日志。
        
        @param request: GetAdHocTaskLogRequest
        @return: GetAdHocTaskLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_ad_hoc_task_log_with_options_async(request, runtime)

    def get_ad_hoc_task_result_with_options(
        self,
        request: dataphin_public_20230630_models.GetAdHocTaskResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetAdHocTaskResultResponse:
        """
        @summary 获取即席查询的任务运行结果。
        
        @param request: GetAdHocTaskResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAdHocTaskResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.sub_task_id):
            query['SubTaskId'] = request.sub_task_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAdHocTaskResult',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetAdHocTaskResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ad_hoc_task_result_with_options_async(
        self,
        request: dataphin_public_20230630_models.GetAdHocTaskResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetAdHocTaskResultResponse:
        """
        @summary 获取即席查询的任务运行结果。
        
        @param request: GetAdHocTaskResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAdHocTaskResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.sub_task_id):
            query['SubTaskId'] = request.sub_task_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAdHocTaskResult',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetAdHocTaskResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ad_hoc_task_result(
        self,
        request: dataphin_public_20230630_models.GetAdHocTaskResultRequest,
    ) -> dataphin_public_20230630_models.GetAdHocTaskResultResponse:
        """
        @summary 获取即席查询的任务运行结果。
        
        @param request: GetAdHocTaskResultRequest
        @return: GetAdHocTaskResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_ad_hoc_task_result_with_options(request, runtime)

    async def get_ad_hoc_task_result_async(
        self,
        request: dataphin_public_20230630_models.GetAdHocTaskResultRequest,
    ) -> dataphin_public_20230630_models.GetAdHocTaskResultResponse:
        """
        @summary 获取即席查询的任务运行结果。
        
        @param request: GetAdHocTaskResultRequest
        @return: GetAdHocTaskResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_ad_hoc_task_result_with_options_async(request, runtime)

    def get_alert_event_with_options(
        self,
        request: dataphin_public_20230630_models.GetAlertEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetAlertEventResponse:
        """
        @summary 获取告警事件详情
        
        @param request: GetAlertEventRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAlertEventResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAlertEvent',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetAlertEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_alert_event_with_options_async(
        self,
        request: dataphin_public_20230630_models.GetAlertEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetAlertEventResponse:
        """
        @summary 获取告警事件详情
        
        @param request: GetAlertEventRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAlertEventResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAlertEvent',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetAlertEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_alert_event(
        self,
        request: dataphin_public_20230630_models.GetAlertEventRequest,
    ) -> dataphin_public_20230630_models.GetAlertEventResponse:
        """
        @summary 获取告警事件详情
        
        @param request: GetAlertEventRequest
        @return: GetAlertEventResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_alert_event_with_options(request, runtime)

    async def get_alert_event_async(
        self,
        request: dataphin_public_20230630_models.GetAlertEventRequest,
    ) -> dataphin_public_20230630_models.GetAlertEventResponse:
        """
        @summary 获取告警事件详情
        
        @param request: GetAlertEventRequest
        @return: GetAlertEventResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_alert_event_with_options_async(request, runtime)

    def get_batch_task_info_with_options(
        self,
        request: dataphin_public_20230630_models.GetBatchTaskInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetBatchTaskInfoResponse:
        """
        @summary 获取离线计算任务详情。
        
        @param request: GetBatchTaskInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBatchTaskInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
        if not UtilClient.is_unset(request.file_id):
            query['FileId'] = request.file_id
        if not UtilClient.is_unset(request.include_all_up_streams):
            query['IncludeAllUpStreams'] = request.include_all_up_streams
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBatchTaskInfo',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetBatchTaskInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_batch_task_info_with_options_async(
        self,
        request: dataphin_public_20230630_models.GetBatchTaskInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetBatchTaskInfoResponse:
        """
        @summary 获取离线计算任务详情。
        
        @param request: GetBatchTaskInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBatchTaskInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
        if not UtilClient.is_unset(request.file_id):
            query['FileId'] = request.file_id
        if not UtilClient.is_unset(request.include_all_up_streams):
            query['IncludeAllUpStreams'] = request.include_all_up_streams
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBatchTaskInfo',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetBatchTaskInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_batch_task_info(
        self,
        request: dataphin_public_20230630_models.GetBatchTaskInfoRequest,
    ) -> dataphin_public_20230630_models.GetBatchTaskInfoResponse:
        """
        @summary 获取离线计算任务详情。
        
        @param request: GetBatchTaskInfoRequest
        @return: GetBatchTaskInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_batch_task_info_with_options(request, runtime)

    async def get_batch_task_info_async(
        self,
        request: dataphin_public_20230630_models.GetBatchTaskInfoRequest,
    ) -> dataphin_public_20230630_models.GetBatchTaskInfoResponse:
        """
        @summary 获取离线计算任务详情。
        
        @param request: GetBatchTaskInfoRequest
        @return: GetBatchTaskInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_batch_task_info_with_options_async(request, runtime)

    def get_batch_task_info_by_version_with_options(
        self,
        request: dataphin_public_20230630_models.GetBatchTaskInfoByVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetBatchTaskInfoByVersionResponse:
        """
        @summary 获取离线计算任务指定版本任务详情。
        
        @param request: GetBatchTaskInfoByVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBatchTaskInfoByVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_id):
            query['FileId'] = request.file_id
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBatchTaskInfoByVersion',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetBatchTaskInfoByVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_batch_task_info_by_version_with_options_async(
        self,
        request: dataphin_public_20230630_models.GetBatchTaskInfoByVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetBatchTaskInfoByVersionResponse:
        """
        @summary 获取离线计算任务指定版本任务详情。
        
        @param request: GetBatchTaskInfoByVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBatchTaskInfoByVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_id):
            query['FileId'] = request.file_id
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBatchTaskInfoByVersion',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetBatchTaskInfoByVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_batch_task_info_by_version(
        self,
        request: dataphin_public_20230630_models.GetBatchTaskInfoByVersionRequest,
    ) -> dataphin_public_20230630_models.GetBatchTaskInfoByVersionResponse:
        """
        @summary 获取离线计算任务指定版本任务详情。
        
        @param request: GetBatchTaskInfoByVersionRequest
        @return: GetBatchTaskInfoByVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_batch_task_info_by_version_with_options(request, runtime)

    async def get_batch_task_info_by_version_async(
        self,
        request: dataphin_public_20230630_models.GetBatchTaskInfoByVersionRequest,
    ) -> dataphin_public_20230630_models.GetBatchTaskInfoByVersionResponse:
        """
        @summary 获取离线计算任务指定版本任务详情。
        
        @param request: GetBatchTaskInfoByVersionRequest
        @return: GetBatchTaskInfoByVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_batch_task_info_by_version_with_options_async(request, runtime)

    def get_batch_task_udf_lineages_with_options(
        self,
        request: dataphin_public_20230630_models.GetBatchTaskUdfLineagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetBatchTaskUdfLineagesResponse:
        """
        @summary 获取离线任务自定义血缘。
        
        @param request: GetBatchTaskUdfLineagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBatchTaskUdfLineagesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_id):
            query['FileId'] = request.file_id
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBatchTaskUdfLineages',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetBatchTaskUdfLineagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_batch_task_udf_lineages_with_options_async(
        self,
        request: dataphin_public_20230630_models.GetBatchTaskUdfLineagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetBatchTaskUdfLineagesResponse:
        """
        @summary 获取离线任务自定义血缘。
        
        @param request: GetBatchTaskUdfLineagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBatchTaskUdfLineagesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_id):
            query['FileId'] = request.file_id
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBatchTaskUdfLineages',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetBatchTaskUdfLineagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_batch_task_udf_lineages(
        self,
        request: dataphin_public_20230630_models.GetBatchTaskUdfLineagesRequest,
    ) -> dataphin_public_20230630_models.GetBatchTaskUdfLineagesResponse:
        """
        @summary 获取离线任务自定义血缘。
        
        @param request: GetBatchTaskUdfLineagesRequest
        @return: GetBatchTaskUdfLineagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_batch_task_udf_lineages_with_options(request, runtime)

    async def get_batch_task_udf_lineages_async(
        self,
        request: dataphin_public_20230630_models.GetBatchTaskUdfLineagesRequest,
    ) -> dataphin_public_20230630_models.GetBatchTaskUdfLineagesResponse:
        """
        @summary 获取离线任务自定义血缘。
        
        @param request: GetBatchTaskUdfLineagesRequest
        @return: GetBatchTaskUdfLineagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_batch_task_udf_lineages_with_options_async(request, runtime)

    def get_batch_task_versions_with_options(
        self,
        request: dataphin_public_20230630_models.GetBatchTaskVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetBatchTaskVersionsResponse:
        """
        @summary 获取离线计算任务版本列表。
        
        @param request: GetBatchTaskVersionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBatchTaskVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_id):
            query['FileId'] = request.file_id
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBatchTaskVersions',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetBatchTaskVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_batch_task_versions_with_options_async(
        self,
        request: dataphin_public_20230630_models.GetBatchTaskVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetBatchTaskVersionsResponse:
        """
        @summary 获取离线计算任务版本列表。
        
        @param request: GetBatchTaskVersionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBatchTaskVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_id):
            query['FileId'] = request.file_id
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBatchTaskVersions',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetBatchTaskVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_batch_task_versions(
        self,
        request: dataphin_public_20230630_models.GetBatchTaskVersionsRequest,
    ) -> dataphin_public_20230630_models.GetBatchTaskVersionsResponse:
        """
        @summary 获取离线计算任务版本列表。
        
        @param request: GetBatchTaskVersionsRequest
        @return: GetBatchTaskVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_batch_task_versions_with_options(request, runtime)

    async def get_batch_task_versions_async(
        self,
        request: dataphin_public_20230630_models.GetBatchTaskVersionsRequest,
    ) -> dataphin_public_20230630_models.GetBatchTaskVersionsResponse:
        """
        @summary 获取离线计算任务版本列表。
        
        @param request: GetBatchTaskVersionsRequest
        @return: GetBatchTaskVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_batch_task_versions_with_options_async(request, runtime)

    def get_biz_entity_info_with_options(
        self,
        request: dataphin_public_20230630_models.GetBizEntityInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetBizEntityInfoResponse:
        """
        @summary 获取业务实体详情。
        
        @param request: GetBizEntityInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBizEntityInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBizEntityInfo',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetBizEntityInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_biz_entity_info_with_options_async(
        self,
        request: dataphin_public_20230630_models.GetBizEntityInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetBizEntityInfoResponse:
        """
        @summary 获取业务实体详情。
        
        @param request: GetBizEntityInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBizEntityInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBizEntityInfo',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetBizEntityInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_biz_entity_info(
        self,
        request: dataphin_public_20230630_models.GetBizEntityInfoRequest,
    ) -> dataphin_public_20230630_models.GetBizEntityInfoResponse:
        """
        @summary 获取业务实体详情。
        
        @param request: GetBizEntityInfoRequest
        @return: GetBizEntityInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_biz_entity_info_with_options(request, runtime)

    async def get_biz_entity_info_async(
        self,
        request: dataphin_public_20230630_models.GetBizEntityInfoRequest,
    ) -> dataphin_public_20230630_models.GetBizEntityInfoResponse:
        """
        @summary 获取业务实体详情。
        
        @param request: GetBizEntityInfoRequest
        @return: GetBizEntityInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_biz_entity_info_with_options_async(request, runtime)

    def get_biz_entity_info_by_version_with_options(
        self,
        request: dataphin_public_20230630_models.GetBizEntityInfoByVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetBizEntityInfoByVersionResponse:
        """
        @summary 查询指定版本的业务实体的详情。
        
        @param request: GetBizEntityInfoByVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBizEntityInfoByVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBizEntityInfoByVersion',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetBizEntityInfoByVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_biz_entity_info_by_version_with_options_async(
        self,
        request: dataphin_public_20230630_models.GetBizEntityInfoByVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetBizEntityInfoByVersionResponse:
        """
        @summary 查询指定版本的业务实体的详情。
        
        @param request: GetBizEntityInfoByVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBizEntityInfoByVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBizEntityInfoByVersion',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetBizEntityInfoByVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_biz_entity_info_by_version(
        self,
        request: dataphin_public_20230630_models.GetBizEntityInfoByVersionRequest,
    ) -> dataphin_public_20230630_models.GetBizEntityInfoByVersionResponse:
        """
        @summary 查询指定版本的业务实体的详情。
        
        @param request: GetBizEntityInfoByVersionRequest
        @return: GetBizEntityInfoByVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_biz_entity_info_by_version_with_options(request, runtime)

    async def get_biz_entity_info_by_version_async(
        self,
        request: dataphin_public_20230630_models.GetBizEntityInfoByVersionRequest,
    ) -> dataphin_public_20230630_models.GetBizEntityInfoByVersionResponse:
        """
        @summary 查询指定版本的业务实体的详情。
        
        @param request: GetBizEntityInfoByVersionRequest
        @return: GetBizEntityInfoByVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_biz_entity_info_by_version_with_options_async(request, runtime)

    def get_biz_unit_info_with_options(
        self,
        request: dataphin_public_20230630_models.GetBizUnitInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetBizUnitInfoResponse:
        """
        @summary 获取数据板块详情。
        
        @param request: GetBizUnitInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBizUnitInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBizUnitInfo',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetBizUnitInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_biz_unit_info_with_options_async(
        self,
        request: dataphin_public_20230630_models.GetBizUnitInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetBizUnitInfoResponse:
        """
        @summary 获取数据板块详情。
        
        @param request: GetBizUnitInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBizUnitInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBizUnitInfo',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetBizUnitInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_biz_unit_info(
        self,
        request: dataphin_public_20230630_models.GetBizUnitInfoRequest,
    ) -> dataphin_public_20230630_models.GetBizUnitInfoResponse:
        """
        @summary 获取数据板块详情。
        
        @param request: GetBizUnitInfoRequest
        @return: GetBizUnitInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_biz_unit_info_with_options(request, runtime)

    async def get_biz_unit_info_async(
        self,
        request: dataphin_public_20230630_models.GetBizUnitInfoRequest,
    ) -> dataphin_public_20230630_models.GetBizUnitInfoResponse:
        """
        @summary 获取数据板块详情。
        
        @param request: GetBizUnitInfoRequest
        @return: GetBizUnitInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_biz_unit_info_with_options_async(request, runtime)

    def get_cluster_queue_info_by_env_with_options(
        self,
        request: dataphin_public_20230630_models.GetClusterQueueInfoByEnvRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetClusterQueueInfoByEnvResponse:
        """
        @summary 根据环境获取集群信息
        
        @param request: GetClusterQueueInfoByEnvRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetClusterQueueInfoByEnvResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.stream_batch_mode):
            query['StreamBatchMode'] = request.stream_batch_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetClusterQueueInfoByEnv',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetClusterQueueInfoByEnvResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cluster_queue_info_by_env_with_options_async(
        self,
        request: dataphin_public_20230630_models.GetClusterQueueInfoByEnvRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetClusterQueueInfoByEnvResponse:
        """
        @summary 根据环境获取集群信息
        
        @param request: GetClusterQueueInfoByEnvRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetClusterQueueInfoByEnvResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.stream_batch_mode):
            query['StreamBatchMode'] = request.stream_batch_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetClusterQueueInfoByEnv',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetClusterQueueInfoByEnvResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cluster_queue_info_by_env(
        self,
        request: dataphin_public_20230630_models.GetClusterQueueInfoByEnvRequest,
    ) -> dataphin_public_20230630_models.GetClusterQueueInfoByEnvResponse:
        """
        @summary 根据环境获取集群信息
        
        @param request: GetClusterQueueInfoByEnvRequest
        @return: GetClusterQueueInfoByEnvResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_cluster_queue_info_by_env_with_options(request, runtime)

    async def get_cluster_queue_info_by_env_async(
        self,
        request: dataphin_public_20230630_models.GetClusterQueueInfoByEnvRequest,
    ) -> dataphin_public_20230630_models.GetClusterQueueInfoByEnvResponse:
        """
        @summary 根据环境获取集群信息
        
        @param request: GetClusterQueueInfoByEnvRequest
        @return: GetClusterQueueInfoByEnvResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_cluster_queue_info_by_env_with_options_async(request, runtime)

    def get_data_domain_info_with_options(
        self,
        request: dataphin_public_20230630_models.GetDataDomainInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetDataDomainInfoResponse:
        """
        @summary 获取主题域详情。
        
        @param request: GetDataDomainInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDataDomainInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDataDomainInfo',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetDataDomainInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_domain_info_with_options_async(
        self,
        request: dataphin_public_20230630_models.GetDataDomainInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetDataDomainInfoResponse:
        """
        @summary 获取主题域详情。
        
        @param request: GetDataDomainInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDataDomainInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDataDomainInfo',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetDataDomainInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_domain_info(
        self,
        request: dataphin_public_20230630_models.GetDataDomainInfoRequest,
    ) -> dataphin_public_20230630_models.GetDataDomainInfoResponse:
        """
        @summary 获取主题域详情。
        
        @param request: GetDataDomainInfoRequest
        @return: GetDataDomainInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_data_domain_info_with_options(request, runtime)

    async def get_data_domain_info_async(
        self,
        request: dataphin_public_20230630_models.GetDataDomainInfoRequest,
    ) -> dataphin_public_20230630_models.GetDataDomainInfoResponse:
        """
        @summary 获取主题域详情。
        
        @param request: GetDataDomainInfoRequest
        @return: GetDataDomainInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_data_domain_info_with_options_async(request, runtime)

    def get_dev_object_dependency_with_options(
        self,
        request: dataphin_public_20230630_models.GetDevObjectDependencyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetDevObjectDependencyResponse:
        """
        @summary 查询开发态对象上游依赖。
        
        @param request: GetDevObjectDependencyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDevObjectDependencyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.object_from):
            query['ObjectFrom'] = request.object_from
        if not UtilClient.is_unset(request.object_id):
            query['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.object_type):
            query['ObjectType'] = request.object_type
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDevObjectDependency',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetDevObjectDependencyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dev_object_dependency_with_options_async(
        self,
        request: dataphin_public_20230630_models.GetDevObjectDependencyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetDevObjectDependencyResponse:
        """
        @summary 查询开发态对象上游依赖。
        
        @param request: GetDevObjectDependencyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDevObjectDependencyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.object_from):
            query['ObjectFrom'] = request.object_from
        if not UtilClient.is_unset(request.object_id):
            query['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.object_type):
            query['ObjectType'] = request.object_type
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDevObjectDependency',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetDevObjectDependencyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dev_object_dependency(
        self,
        request: dataphin_public_20230630_models.GetDevObjectDependencyRequest,
    ) -> dataphin_public_20230630_models.GetDevObjectDependencyResponse:
        """
        @summary 查询开发态对象上游依赖。
        
        @param request: GetDevObjectDependencyRequest
        @return: GetDevObjectDependencyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_dev_object_dependency_with_options(request, runtime)

    async def get_dev_object_dependency_async(
        self,
        request: dataphin_public_20230630_models.GetDevObjectDependencyRequest,
    ) -> dataphin_public_20230630_models.GetDevObjectDependencyResponse:
        """
        @summary 查询开发态对象上游依赖。
        
        @param request: GetDevObjectDependencyRequest
        @return: GetDevObjectDependencyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_dev_object_dependency_with_options_async(request, runtime)

    def get_directory_tree_with_options(
        self,
        request: dataphin_public_20230630_models.GetDirectoryTreeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetDirectoryTreeResponse:
        """
        @summary 获取文件夹目录树
        
        @param request: GetDirectoryTreeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDirectoryTreeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDirectoryTree',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetDirectoryTreeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_directory_tree_with_options_async(
        self,
        request: dataphin_public_20230630_models.GetDirectoryTreeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetDirectoryTreeResponse:
        """
        @summary 获取文件夹目录树
        
        @param request: GetDirectoryTreeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDirectoryTreeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDirectoryTree',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetDirectoryTreeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_directory_tree(
        self,
        request: dataphin_public_20230630_models.GetDirectoryTreeRequest,
    ) -> dataphin_public_20230630_models.GetDirectoryTreeResponse:
        """
        @summary 获取文件夹目录树
        
        @param request: GetDirectoryTreeRequest
        @return: GetDirectoryTreeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_directory_tree_with_options(request, runtime)

    async def get_directory_tree_async(
        self,
        request: dataphin_public_20230630_models.GetDirectoryTreeRequest,
    ) -> dataphin_public_20230630_models.GetDirectoryTreeResponse:
        """
        @summary 获取文件夹目录树
        
        @param request: GetDirectoryTreeRequest
        @return: GetDirectoryTreeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_directory_tree_with_options_async(request, runtime)

    def get_instance_down_stream_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.GetInstanceDownStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetInstanceDownStreamResponse:
        """
        @summary 根据起始的实例查询该实例的下游
        
        @param tmp_req: GetInstanceDownStreamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceDownStreamResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.GetInstanceDownStreamShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_get):
            request.instance_get_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_get, 'InstanceGet', 'json')
        query = {}
        if not UtilClient.is_unset(request.down_stream_depth):
            query['DownStreamDepth'] = request.down_stream_depth
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.run_status):
            query['RunStatus'] = request.run_status
        body = {}
        if not UtilClient.is_unset(request.instance_get_shrink):
            body['InstanceGet'] = request.instance_get_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetInstanceDownStream',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetInstanceDownStreamResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_down_stream_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.GetInstanceDownStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetInstanceDownStreamResponse:
        """
        @summary 根据起始的实例查询该实例的下游
        
        @param tmp_req: GetInstanceDownStreamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceDownStreamResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.GetInstanceDownStreamShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_get):
            request.instance_get_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_get, 'InstanceGet', 'json')
        query = {}
        if not UtilClient.is_unset(request.down_stream_depth):
            query['DownStreamDepth'] = request.down_stream_depth
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.run_status):
            query['RunStatus'] = request.run_status
        body = {}
        if not UtilClient.is_unset(request.instance_get_shrink):
            body['InstanceGet'] = request.instance_get_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetInstanceDownStream',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetInstanceDownStreamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_down_stream(
        self,
        request: dataphin_public_20230630_models.GetInstanceDownStreamRequest,
    ) -> dataphin_public_20230630_models.GetInstanceDownStreamResponse:
        """
        @summary 根据起始的实例查询该实例的下游
        
        @param request: GetInstanceDownStreamRequest
        @return: GetInstanceDownStreamResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_instance_down_stream_with_options(request, runtime)

    async def get_instance_down_stream_async(
        self,
        request: dataphin_public_20230630_models.GetInstanceDownStreamRequest,
    ) -> dataphin_public_20230630_models.GetInstanceDownStreamResponse:
        """
        @summary 根据起始的实例查询该实例的下游
        
        @param request: GetInstanceDownStreamRequest
        @return: GetInstanceDownStreamResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_down_stream_with_options_async(request, runtime)

    def get_instance_up_down_stream_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.GetInstanceUpDownStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetInstanceUpDownStreamResponse:
        """
        @summary 查询实例的上下游，支持逻辑表和代码任务。
        
        @param tmp_req: GetInstanceUpDownStreamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceUpDownStreamResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.GetInstanceUpDownStreamShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_id):
            request.instance_id_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_id, 'InstanceId', 'json')
        query = {}
        if not UtilClient.is_unset(request.down_stream_depth):
            query['DownStreamDepth'] = request.down_stream_depth
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.up_stream_depth):
            query['UpStreamDepth'] = request.up_stream_depth
        body = {}
        if not UtilClient.is_unset(request.instance_id_shrink):
            body['InstanceId'] = request.instance_id_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetInstanceUpDownStream',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetInstanceUpDownStreamResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_up_down_stream_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.GetInstanceUpDownStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetInstanceUpDownStreamResponse:
        """
        @summary 查询实例的上下游，支持逻辑表和代码任务。
        
        @param tmp_req: GetInstanceUpDownStreamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceUpDownStreamResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.GetInstanceUpDownStreamShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_id):
            request.instance_id_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_id, 'InstanceId', 'json')
        query = {}
        if not UtilClient.is_unset(request.down_stream_depth):
            query['DownStreamDepth'] = request.down_stream_depth
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.up_stream_depth):
            query['UpStreamDepth'] = request.up_stream_depth
        body = {}
        if not UtilClient.is_unset(request.instance_id_shrink):
            body['InstanceId'] = request.instance_id_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetInstanceUpDownStream',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetInstanceUpDownStreamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_up_down_stream(
        self,
        request: dataphin_public_20230630_models.GetInstanceUpDownStreamRequest,
    ) -> dataphin_public_20230630_models.GetInstanceUpDownStreamResponse:
        """
        @summary 查询实例的上下游，支持逻辑表和代码任务。
        
        @param request: GetInstanceUpDownStreamRequest
        @return: GetInstanceUpDownStreamResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_instance_up_down_stream_with_options(request, runtime)

    async def get_instance_up_down_stream_async(
        self,
        request: dataphin_public_20230630_models.GetInstanceUpDownStreamRequest,
    ) -> dataphin_public_20230630_models.GetInstanceUpDownStreamResponse:
        """
        @summary 查询实例的上下游，支持逻辑表和代码任务。
        
        @param request: GetInstanceUpDownStreamRequest
        @return: GetInstanceUpDownStreamResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_up_down_stream_with_options_async(request, runtime)

    def get_latest_submit_detail_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.GetLatestSubmitDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetLatestSubmitDetailResponse:
        """
        @summary 获取最新的待发布记录详情
        
        @param tmp_req: GetLatestSubmitDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLatestSubmitDetailResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.GetLatestSubmitDetailShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.submit_detail_query):
            request.submit_detail_query_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.submit_detail_query, 'SubmitDetailQuery', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.submit_detail_query_shrink):
            body['SubmitDetailQuery'] = request.submit_detail_query_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLatestSubmitDetail',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetLatestSubmitDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_latest_submit_detail_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.GetLatestSubmitDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetLatestSubmitDetailResponse:
        """
        @summary 获取最新的待发布记录详情
        
        @param tmp_req: GetLatestSubmitDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLatestSubmitDetailResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.GetLatestSubmitDetailShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.submit_detail_query):
            request.submit_detail_query_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.submit_detail_query, 'SubmitDetailQuery', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.submit_detail_query_shrink):
            body['SubmitDetailQuery'] = request.submit_detail_query_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLatestSubmitDetail',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetLatestSubmitDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_latest_submit_detail(
        self,
        request: dataphin_public_20230630_models.GetLatestSubmitDetailRequest,
    ) -> dataphin_public_20230630_models.GetLatestSubmitDetailResponse:
        """
        @summary 获取最新的待发布记录详情
        
        @param request: GetLatestSubmitDetailRequest
        @return: GetLatestSubmitDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_latest_submit_detail_with_options(request, runtime)

    async def get_latest_submit_detail_async(
        self,
        request: dataphin_public_20230630_models.GetLatestSubmitDetailRequest,
    ) -> dataphin_public_20230630_models.GetLatestSubmitDetailResponse:
        """
        @summary 获取最新的待发布记录详情
        
        @param request: GetLatestSubmitDetailRequest
        @return: GetLatestSubmitDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_latest_submit_detail_with_options_async(request, runtime)

    def get_my_roles_with_options(
        self,
        request: dataphin_public_20230630_models.GetMyRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetMyRolesResponse:
        """
        @summary 获取用户角色列表
        
        @param request: GetMyRolesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMyRolesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMyRoles',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetMyRolesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_my_roles_with_options_async(
        self,
        request: dataphin_public_20230630_models.GetMyRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetMyRolesResponse:
        """
        @summary 获取用户角色列表
        
        @param request: GetMyRolesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMyRolesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMyRoles',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetMyRolesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_my_roles(
        self,
        request: dataphin_public_20230630_models.GetMyRolesRequest,
    ) -> dataphin_public_20230630_models.GetMyRolesResponse:
        """
        @summary 获取用户角色列表
        
        @param request: GetMyRolesRequest
        @return: GetMyRolesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_my_roles_with_options(request, runtime)

    async def get_my_roles_async(
        self,
        request: dataphin_public_20230630_models.GetMyRolesRequest,
    ) -> dataphin_public_20230630_models.GetMyRolesResponse:
        """
        @summary 获取用户角色列表
        
        @param request: GetMyRolesRequest
        @return: GetMyRolesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_my_roles_with_options_async(request, runtime)

    def get_my_tenants_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.GetMyTenantsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetMyTenantsResponse:
        """
        @summary 获取当前用户归属租户.
        
        @param tmp_req: GetMyTenantsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMyTenantsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.GetMyTenantsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.feature_code_list):
            request.feature_code_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.feature_code_list, 'FeatureCodeList', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.feature_code_list_shrink):
            body['FeatureCodeList'] = request.feature_code_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMyTenants',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetMyTenantsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_my_tenants_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.GetMyTenantsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetMyTenantsResponse:
        """
        @summary 获取当前用户归属租户.
        
        @param tmp_req: GetMyTenantsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMyTenantsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.GetMyTenantsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.feature_code_list):
            request.feature_code_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.feature_code_list, 'FeatureCodeList', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.feature_code_list_shrink):
            body['FeatureCodeList'] = request.feature_code_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMyTenants',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetMyTenantsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_my_tenants(
        self,
        request: dataphin_public_20230630_models.GetMyTenantsRequest,
    ) -> dataphin_public_20230630_models.GetMyTenantsResponse:
        """
        @summary 获取当前用户归属租户.
        
        @param request: GetMyTenantsRequest
        @return: GetMyTenantsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_my_tenants_with_options(request, runtime)

    async def get_my_tenants_async(
        self,
        request: dataphin_public_20230630_models.GetMyTenantsRequest,
    ) -> dataphin_public_20230630_models.GetMyTenantsResponse:
        """
        @summary 获取当前用户归属租户.
        
        @param request: GetMyTenantsRequest
        @return: GetMyTenantsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_my_tenants_with_options_async(request, runtime)

    def get_node_up_down_stream_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.GetNodeUpDownStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetNodeUpDownStreamResponse:
        """
        @summary 通用查询节点上下游接口
        
        @param tmp_req: GetNodeUpDownStreamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNodeUpDownStreamResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.GetNodeUpDownStreamShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.node_id):
            request.node_id_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.node_id, 'NodeId', 'json')
        query = {}
        if not UtilClient.is_unset(request.down_stream_depth):
            query['DownStreamDepth'] = request.down_stream_depth
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.up_stream_depth):
            query['UpStreamDepth'] = request.up_stream_depth
        body = {}
        if not UtilClient.is_unset(request.node_id_shrink):
            body['NodeId'] = request.node_id_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetNodeUpDownStream',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetNodeUpDownStreamResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_node_up_down_stream_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.GetNodeUpDownStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetNodeUpDownStreamResponse:
        """
        @summary 通用查询节点上下游接口
        
        @param tmp_req: GetNodeUpDownStreamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNodeUpDownStreamResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.GetNodeUpDownStreamShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.node_id):
            request.node_id_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.node_id, 'NodeId', 'json')
        query = {}
        if not UtilClient.is_unset(request.down_stream_depth):
            query['DownStreamDepth'] = request.down_stream_depth
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.up_stream_depth):
            query['UpStreamDepth'] = request.up_stream_depth
        body = {}
        if not UtilClient.is_unset(request.node_id_shrink):
            body['NodeId'] = request.node_id_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetNodeUpDownStream',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetNodeUpDownStreamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_node_up_down_stream(
        self,
        request: dataphin_public_20230630_models.GetNodeUpDownStreamRequest,
    ) -> dataphin_public_20230630_models.GetNodeUpDownStreamResponse:
        """
        @summary 通用查询节点上下游接口
        
        @param request: GetNodeUpDownStreamRequest
        @return: GetNodeUpDownStreamResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_node_up_down_stream_with_options(request, runtime)

    async def get_node_up_down_stream_async(
        self,
        request: dataphin_public_20230630_models.GetNodeUpDownStreamRequest,
    ) -> dataphin_public_20230630_models.GetNodeUpDownStreamResponse:
        """
        @summary 通用查询节点上下游接口
        
        @param request: GetNodeUpDownStreamRequest
        @return: GetNodeUpDownStreamResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_node_up_down_stream_with_options_async(request, runtime)

    def get_operation_submit_status_with_options(
        self,
        request: dataphin_public_20230630_models.GetOperationSubmitStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetOperationSubmitStatusResponse:
        """
        @summary 查询补数据提交的状态
        
        @param request: GetOperationSubmitStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOperationSubmitStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOperationSubmitStatus',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetOperationSubmitStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_operation_submit_status_with_options_async(
        self,
        request: dataphin_public_20230630_models.GetOperationSubmitStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetOperationSubmitStatusResponse:
        """
        @summary 查询补数据提交的状态
        
        @param request: GetOperationSubmitStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOperationSubmitStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOperationSubmitStatus',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetOperationSubmitStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_operation_submit_status(
        self,
        request: dataphin_public_20230630_models.GetOperationSubmitStatusRequest,
    ) -> dataphin_public_20230630_models.GetOperationSubmitStatusResponse:
        """
        @summary 查询补数据提交的状态
        
        @param request: GetOperationSubmitStatusRequest
        @return: GetOperationSubmitStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_operation_submit_status_with_options(request, runtime)

    async def get_operation_submit_status_async(
        self,
        request: dataphin_public_20230630_models.GetOperationSubmitStatusRequest,
    ) -> dataphin_public_20230630_models.GetOperationSubmitStatusResponse:
        """
        @summary 查询补数据提交的状态
        
        @param request: GetOperationSubmitStatusRequest
        @return: GetOperationSubmitStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_operation_submit_status_with_options_async(request, runtime)

    def get_physical_instance_with_options(
        self,
        request: dataphin_public_20230630_models.GetPhysicalInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetPhysicalInstanceResponse:
        """
        @summary 查询脚本的实例信息, 包括实例状态、运行时间等信息.
        
        @param request: GetPhysicalInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPhysicalInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPhysicalInstance',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetPhysicalInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_physical_instance_with_options_async(
        self,
        request: dataphin_public_20230630_models.GetPhysicalInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetPhysicalInstanceResponse:
        """
        @summary 查询脚本的实例信息, 包括实例状态、运行时间等信息.
        
        @param request: GetPhysicalInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPhysicalInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPhysicalInstance',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetPhysicalInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_physical_instance(
        self,
        request: dataphin_public_20230630_models.GetPhysicalInstanceRequest,
    ) -> dataphin_public_20230630_models.GetPhysicalInstanceResponse:
        """
        @summary 查询脚本的实例信息, 包括实例状态、运行时间等信息.
        
        @param request: GetPhysicalInstanceRequest
        @return: GetPhysicalInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_physical_instance_with_options(request, runtime)

    async def get_physical_instance_async(
        self,
        request: dataphin_public_20230630_models.GetPhysicalInstanceRequest,
    ) -> dataphin_public_20230630_models.GetPhysicalInstanceResponse:
        """
        @summary 查询脚本的实例信息, 包括实例状态、运行时间等信息.
        
        @param request: GetPhysicalInstanceRequest
        @return: GetPhysicalInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_physical_instance_with_options_async(request, runtime)

    def get_physical_instance_log_with_options(
        self,
        request: dataphin_public_20230630_models.GetPhysicalInstanceLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetPhysicalInstanceLogResponse:
        """
        @summary 获取实例执行的日志，如果实例重跑了多次，则会有多条日志
        
        @param request: GetPhysicalInstanceLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPhysicalInstanceLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPhysicalInstanceLog',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetPhysicalInstanceLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_physical_instance_log_with_options_async(
        self,
        request: dataphin_public_20230630_models.GetPhysicalInstanceLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetPhysicalInstanceLogResponse:
        """
        @summary 获取实例执行的日志，如果实例重跑了多次，则会有多条日志
        
        @param request: GetPhysicalInstanceLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPhysicalInstanceLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPhysicalInstanceLog',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetPhysicalInstanceLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_physical_instance_log(
        self,
        request: dataphin_public_20230630_models.GetPhysicalInstanceLogRequest,
    ) -> dataphin_public_20230630_models.GetPhysicalInstanceLogResponse:
        """
        @summary 获取实例执行的日志，如果实例重跑了多次，则会有多条日志
        
        @param request: GetPhysicalInstanceLogRequest
        @return: GetPhysicalInstanceLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_physical_instance_log_with_options(request, runtime)

    async def get_physical_instance_log_async(
        self,
        request: dataphin_public_20230630_models.GetPhysicalInstanceLogRequest,
    ) -> dataphin_public_20230630_models.GetPhysicalInstanceLogResponse:
        """
        @summary 获取实例执行的日志，如果实例重跑了多次，则会有多条日志
        
        @param request: GetPhysicalInstanceLogRequest
        @return: GetPhysicalInstanceLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_physical_instance_log_with_options_async(request, runtime)

    def get_physical_node_with_options(
        self,
        request: dataphin_public_20230630_models.GetPhysicalNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetPhysicalNodeResponse:
        """
        @summary 查询物理调度节点。
        
        @param request: GetPhysicalNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPhysicalNodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPhysicalNode',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetPhysicalNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_physical_node_with_options_async(
        self,
        request: dataphin_public_20230630_models.GetPhysicalNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetPhysicalNodeResponse:
        """
        @summary 查询物理调度节点。
        
        @param request: GetPhysicalNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPhysicalNodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPhysicalNode',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetPhysicalNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_physical_node(
        self,
        request: dataphin_public_20230630_models.GetPhysicalNodeRequest,
    ) -> dataphin_public_20230630_models.GetPhysicalNodeResponse:
        """
        @summary 查询物理调度节点。
        
        @param request: GetPhysicalNodeRequest
        @return: GetPhysicalNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_physical_node_with_options(request, runtime)

    async def get_physical_node_async(
        self,
        request: dataphin_public_20230630_models.GetPhysicalNodeRequest,
    ) -> dataphin_public_20230630_models.GetPhysicalNodeResponse:
        """
        @summary 查询物理调度节点。
        
        @param request: GetPhysicalNodeRequest
        @return: GetPhysicalNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_physical_node_with_options_async(request, runtime)

    def get_physical_node_by_output_name_with_options(
        self,
        request: dataphin_public_20230630_models.GetPhysicalNodeByOutputNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetPhysicalNodeByOutputNameResponse:
        """
        @summary 根据输出名查询对应的物理节点。
        
        @param request: GetPhysicalNodeByOutputNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPhysicalNodeByOutputNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.output_name):
            query['OutputName'] = request.output_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPhysicalNodeByOutputName',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetPhysicalNodeByOutputNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_physical_node_by_output_name_with_options_async(
        self,
        request: dataphin_public_20230630_models.GetPhysicalNodeByOutputNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetPhysicalNodeByOutputNameResponse:
        """
        @summary 根据输出名查询对应的物理节点。
        
        @param request: GetPhysicalNodeByOutputNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPhysicalNodeByOutputNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.output_name):
            query['OutputName'] = request.output_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPhysicalNodeByOutputName',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetPhysicalNodeByOutputNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_physical_node_by_output_name(
        self,
        request: dataphin_public_20230630_models.GetPhysicalNodeByOutputNameRequest,
    ) -> dataphin_public_20230630_models.GetPhysicalNodeByOutputNameResponse:
        """
        @summary 根据输出名查询对应的物理节点。
        
        @param request: GetPhysicalNodeByOutputNameRequest
        @return: GetPhysicalNodeByOutputNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_physical_node_by_output_name_with_options(request, runtime)

    async def get_physical_node_by_output_name_async(
        self,
        request: dataphin_public_20230630_models.GetPhysicalNodeByOutputNameRequest,
    ) -> dataphin_public_20230630_models.GetPhysicalNodeByOutputNameResponse:
        """
        @summary 根据输出名查询对应的物理节点。
        
        @param request: GetPhysicalNodeByOutputNameRequest
        @return: GetPhysicalNodeByOutputNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_physical_node_by_output_name_with_options_async(request, runtime)

    def get_physical_node_content_with_options(
        self,
        request: dataphin_public_20230630_models.GetPhysicalNodeContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetPhysicalNodeContentResponse:
        """
        @summary 查询调度节点代码内容。
        
        @param request: GetPhysicalNodeContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPhysicalNodeContentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPhysicalNodeContent',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetPhysicalNodeContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_physical_node_content_with_options_async(
        self,
        request: dataphin_public_20230630_models.GetPhysicalNodeContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetPhysicalNodeContentResponse:
        """
        @summary 查询调度节点代码内容。
        
        @param request: GetPhysicalNodeContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPhysicalNodeContentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPhysicalNodeContent',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetPhysicalNodeContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_physical_node_content(
        self,
        request: dataphin_public_20230630_models.GetPhysicalNodeContentRequest,
    ) -> dataphin_public_20230630_models.GetPhysicalNodeContentResponse:
        """
        @summary 查询调度节点代码内容。
        
        @param request: GetPhysicalNodeContentRequest
        @return: GetPhysicalNodeContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_physical_node_content_with_options(request, runtime)

    async def get_physical_node_content_async(
        self,
        request: dataphin_public_20230630_models.GetPhysicalNodeContentRequest,
    ) -> dataphin_public_20230630_models.GetPhysicalNodeContentResponse:
        """
        @summary 查询调度节点代码内容。
        
        @param request: GetPhysicalNodeContentRequest
        @return: GetPhysicalNodeContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_physical_node_content_with_options_async(request, runtime)

    def get_physical_node_operation_log_with_options(
        self,
        request: dataphin_public_20230630_models.GetPhysicalNodeOperationLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetPhysicalNodeOperationLogResponse:
        """
        @summary 查询节点的操作日志。
        
        @param request: GetPhysicalNodeOperationLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPhysicalNodeOperationLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPhysicalNodeOperationLog',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetPhysicalNodeOperationLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_physical_node_operation_log_with_options_async(
        self,
        request: dataphin_public_20230630_models.GetPhysicalNodeOperationLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetPhysicalNodeOperationLogResponse:
        """
        @summary 查询节点的操作日志。
        
        @param request: GetPhysicalNodeOperationLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPhysicalNodeOperationLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPhysicalNodeOperationLog',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetPhysicalNodeOperationLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_physical_node_operation_log(
        self,
        request: dataphin_public_20230630_models.GetPhysicalNodeOperationLogRequest,
    ) -> dataphin_public_20230630_models.GetPhysicalNodeOperationLogResponse:
        """
        @summary 查询节点的操作日志。
        
        @param request: GetPhysicalNodeOperationLogRequest
        @return: GetPhysicalNodeOperationLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_physical_node_operation_log_with_options(request, runtime)

    async def get_physical_node_operation_log_async(
        self,
        request: dataphin_public_20230630_models.GetPhysicalNodeOperationLogRequest,
    ) -> dataphin_public_20230630_models.GetPhysicalNodeOperationLogResponse:
        """
        @summary 查询节点的操作日志。
        
        @param request: GetPhysicalNodeOperationLogRequest
        @return: GetPhysicalNodeOperationLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_physical_node_operation_log_with_options_async(request, runtime)

    def get_project_produce_user_with_options(
        self,
        request: dataphin_public_20230630_models.GetProjectProduceUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetProjectProduceUserResponse:
        """
        @summary 获取项目生产账号
        
        @param request: GetProjectProduceUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetProjectProduceUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProjectProduceUser',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetProjectProduceUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_project_produce_user_with_options_async(
        self,
        request: dataphin_public_20230630_models.GetProjectProduceUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetProjectProduceUserResponse:
        """
        @summary 获取项目生产账号
        
        @param request: GetProjectProduceUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetProjectProduceUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProjectProduceUser',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetProjectProduceUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_project_produce_user(
        self,
        request: dataphin_public_20230630_models.GetProjectProduceUserRequest,
    ) -> dataphin_public_20230630_models.GetProjectProduceUserResponse:
        """
        @summary 获取项目生产账号
        
        @param request: GetProjectProduceUserRequest
        @return: GetProjectProduceUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_project_produce_user_with_options(request, runtime)

    async def get_project_produce_user_async(
        self,
        request: dataphin_public_20230630_models.GetProjectProduceUserRequest,
    ) -> dataphin_public_20230630_models.GetProjectProduceUserResponse:
        """
        @summary 获取项目生产账号
        
        @param request: GetProjectProduceUserRequest
        @return: GetProjectProduceUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_project_produce_user_with_options_async(request, runtime)

    def get_queue_engine_version_by_env_with_options(
        self,
        request: dataphin_public_20230630_models.GetQueueEngineVersionByEnvRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetQueueEngineVersionByEnvResponse:
        """
        @summary 根据集群ID获取集群版本
        
        @param request: GetQueueEngineVersionByEnvRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQueueEngineVersionByEnvResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.queue_name):
            query['QueueName'] = request.queue_name
        if not UtilClient.is_unset(request.stream_batch_mode):
            query['StreamBatchMode'] = request.stream_batch_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQueueEngineVersionByEnv',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetQueueEngineVersionByEnvResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_queue_engine_version_by_env_with_options_async(
        self,
        request: dataphin_public_20230630_models.GetQueueEngineVersionByEnvRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetQueueEngineVersionByEnvResponse:
        """
        @summary 根据集群ID获取集群版本
        
        @param request: GetQueueEngineVersionByEnvRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQueueEngineVersionByEnvResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.queue_name):
            query['QueueName'] = request.queue_name
        if not UtilClient.is_unset(request.stream_batch_mode):
            query['StreamBatchMode'] = request.stream_batch_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQueueEngineVersionByEnv',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetQueueEngineVersionByEnvResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_queue_engine_version_by_env(
        self,
        request: dataphin_public_20230630_models.GetQueueEngineVersionByEnvRequest,
    ) -> dataphin_public_20230630_models.GetQueueEngineVersionByEnvResponse:
        """
        @summary 根据集群ID获取集群版本
        
        @param request: GetQueueEngineVersionByEnvRequest
        @return: GetQueueEngineVersionByEnvResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_queue_engine_version_by_env_with_options(request, runtime)

    async def get_queue_engine_version_by_env_async(
        self,
        request: dataphin_public_20230630_models.GetQueueEngineVersionByEnvRequest,
    ) -> dataphin_public_20230630_models.GetQueueEngineVersionByEnvResponse:
        """
        @summary 根据集群ID获取集群版本
        
        @param request: GetQueueEngineVersionByEnvRequest
        @return: GetQueueEngineVersionByEnvResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_queue_engine_version_by_env_with_options_async(request, runtime)

    def get_supplement_dagrun_with_options(
        self,
        request: dataphin_public_20230630_models.GetSupplementDagrunRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetSupplementDagrunResponse:
        """
        @summary 获取补数据工作流所有业务日期的Dagrun信息。
        
        @param request: GetSupplementDagrunRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSupplementDagrunResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.supplement_id):
            query['SupplementId'] = request.supplement_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSupplementDagrun',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetSupplementDagrunResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_supplement_dagrun_with_options_async(
        self,
        request: dataphin_public_20230630_models.GetSupplementDagrunRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetSupplementDagrunResponse:
        """
        @summary 获取补数据工作流所有业务日期的Dagrun信息。
        
        @param request: GetSupplementDagrunRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSupplementDagrunResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.supplement_id):
            query['SupplementId'] = request.supplement_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSupplementDagrun',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetSupplementDagrunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_supplement_dagrun(
        self,
        request: dataphin_public_20230630_models.GetSupplementDagrunRequest,
    ) -> dataphin_public_20230630_models.GetSupplementDagrunResponse:
        """
        @summary 获取补数据工作流所有业务日期的Dagrun信息。
        
        @param request: GetSupplementDagrunRequest
        @return: GetSupplementDagrunResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_supplement_dagrun_with_options(request, runtime)

    async def get_supplement_dagrun_async(
        self,
        request: dataphin_public_20230630_models.GetSupplementDagrunRequest,
    ) -> dataphin_public_20230630_models.GetSupplementDagrunResponse:
        """
        @summary 获取补数据工作流所有业务日期的Dagrun信息。
        
        @param request: GetSupplementDagrunRequest
        @return: GetSupplementDagrunResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_supplement_dagrun_with_options_async(request, runtime)

    def get_supplement_dagrun_instance_with_options(
        self,
        request: dataphin_public_20230630_models.GetSupplementDagrunInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetSupplementDagrunInstanceResponse:
        """
        @summary 列出补数据工作流下具体一个业务日期的所有节点的实例。
        
        @param request: GetSupplementDagrunInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSupplementDagrunInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dagrun_id):
            query['DagrunId'] = request.dagrun_id
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSupplementDagrunInstance',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetSupplementDagrunInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_supplement_dagrun_instance_with_options_async(
        self,
        request: dataphin_public_20230630_models.GetSupplementDagrunInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetSupplementDagrunInstanceResponse:
        """
        @summary 列出补数据工作流下具体一个业务日期的所有节点的实例。
        
        @param request: GetSupplementDagrunInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSupplementDagrunInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dagrun_id):
            query['DagrunId'] = request.dagrun_id
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSupplementDagrunInstance',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetSupplementDagrunInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_supplement_dagrun_instance(
        self,
        request: dataphin_public_20230630_models.GetSupplementDagrunInstanceRequest,
    ) -> dataphin_public_20230630_models.GetSupplementDagrunInstanceResponse:
        """
        @summary 列出补数据工作流下具体一个业务日期的所有节点的实例。
        
        @param request: GetSupplementDagrunInstanceRequest
        @return: GetSupplementDagrunInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_supplement_dagrun_instance_with_options(request, runtime)

    async def get_supplement_dagrun_instance_async(
        self,
        request: dataphin_public_20230630_models.GetSupplementDagrunInstanceRequest,
    ) -> dataphin_public_20230630_models.GetSupplementDagrunInstanceResponse:
        """
        @summary 列出补数据工作流下具体一个业务日期的所有节点的实例。
        
        @param request: GetSupplementDagrunInstanceRequest
        @return: GetSupplementDagrunInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_supplement_dagrun_instance_with_options_async(request, runtime)

    def get_user_by_source_id_with_options(
        self,
        request: dataphin_public_20230630_models.GetUserBySourceIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetUserBySourceIdResponse:
        """
        @summary 通过用户原始Id（如阿里云Id）获取用户详情
        
        @param request: GetUserBySourceIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserBySourceIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.source_id):
            query['SourceId'] = request.source_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserBySourceId',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetUserBySourceIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_by_source_id_with_options_async(
        self,
        request: dataphin_public_20230630_models.GetUserBySourceIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetUserBySourceIdResponse:
        """
        @summary 通过用户原始Id（如阿里云Id）获取用户详情
        
        @param request: GetUserBySourceIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserBySourceIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.source_id):
            query['SourceId'] = request.source_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserBySourceId',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetUserBySourceIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_by_source_id(
        self,
        request: dataphin_public_20230630_models.GetUserBySourceIdRequest,
    ) -> dataphin_public_20230630_models.GetUserBySourceIdResponse:
        """
        @summary 通过用户原始Id（如阿里云Id）获取用户详情
        
        @param request: GetUserBySourceIdRequest
        @return: GetUserBySourceIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_user_by_source_id_with_options(request, runtime)

    async def get_user_by_source_id_async(
        self,
        request: dataphin_public_20230630_models.GetUserBySourceIdRequest,
    ) -> dataphin_public_20230630_models.GetUserBySourceIdResponse:
        """
        @summary 通过用户原始Id（如阿里云Id）获取用户详情
        
        @param request: GetUserBySourceIdRequest
        @return: GetUserBySourceIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_user_by_source_id_with_options_async(request, runtime)

    def get_user_group_with_options(
        self,
        request: dataphin_public_20230630_models.GetUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetUserGroupResponse:
        """
        @summary 获取用户组详情.
        
        @param request: GetUserGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserGroup',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_group_with_options_async(
        self,
        request: dataphin_public_20230630_models.GetUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetUserGroupResponse:
        """
        @summary 获取用户组详情.
        
        @param request: GetUserGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserGroup',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_group(
        self,
        request: dataphin_public_20230630_models.GetUserGroupRequest,
    ) -> dataphin_public_20230630_models.GetUserGroupResponse:
        """
        @summary 获取用户组详情.
        
        @param request: GetUserGroupRequest
        @return: GetUserGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_user_group_with_options(request, runtime)

    async def get_user_group_async(
        self,
        request: dataphin_public_20230630_models.GetUserGroupRequest,
    ) -> dataphin_public_20230630_models.GetUserGroupResponse:
        """
        @summary 获取用户组详情.
        
        @param request: GetUserGroupRequest
        @return: GetUserGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_user_group_with_options_async(request, runtime)

    def get_users_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.GetUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetUsersResponse:
        """
        @summary 获取用户详情
        
        @param tmp_req: GetUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUsersResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.GetUsersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_id_list):
            request.user_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_id_list, 'UserIdList', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.user_id_list_shrink):
            body['UserIdList'] = request.user_id_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUsers',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_users_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.GetUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GetUsersResponse:
        """
        @summary 获取用户详情
        
        @param tmp_req: GetUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUsersResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.GetUsersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_id_list):
            request.user_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_id_list, 'UserIdList', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.user_id_list_shrink):
            body['UserIdList'] = request.user_id_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUsers',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GetUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_users(
        self,
        request: dataphin_public_20230630_models.GetUsersRequest,
    ) -> dataphin_public_20230630_models.GetUsersResponse:
        """
        @summary 获取用户详情
        
        @param request: GetUsersRequest
        @return: GetUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_users_with_options(request, runtime)

    async def get_users_async(
        self,
        request: dataphin_public_20230630_models.GetUsersRequest,
    ) -> dataphin_public_20230630_models.GetUsersResponse:
        """
        @summary 获取用户详情
        
        @param request: GetUsersRequest
        @return: GetUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_users_with_options_async(request, runtime)

    def grant_resource_permission_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.GrantResourcePermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GrantResourcePermissionResponse:
        """
        @summary 通过资源点对用户授权
        
        @param tmp_req: GrantResourcePermissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GrantResourcePermissionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.GrantResourcePermissionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.grant_command):
            request.grant_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.grant_command, 'GrantCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.grant_command_shrink):
            body['GrantCommand'] = request.grant_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GrantResourcePermission',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GrantResourcePermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def grant_resource_permission_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.GrantResourcePermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.GrantResourcePermissionResponse:
        """
        @summary 通过资源点对用户授权
        
        @param tmp_req: GrantResourcePermissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GrantResourcePermissionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.GrantResourcePermissionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.grant_command):
            request.grant_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.grant_command, 'GrantCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.grant_command_shrink):
            body['GrantCommand'] = request.grant_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GrantResourcePermission',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.GrantResourcePermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def grant_resource_permission(
        self,
        request: dataphin_public_20230630_models.GrantResourcePermissionRequest,
    ) -> dataphin_public_20230630_models.GrantResourcePermissionResponse:
        """
        @summary 通过资源点对用户授权
        
        @param request: GrantResourcePermissionRequest
        @return: GrantResourcePermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.grant_resource_permission_with_options(request, runtime)

    async def grant_resource_permission_async(
        self,
        request: dataphin_public_20230630_models.GrantResourcePermissionRequest,
    ) -> dataphin_public_20230630_models.GrantResourcePermissionResponse:
        """
        @summary 通过资源点对用户授权
        
        @param request: GrantResourcePermissionRequest
        @return: GrantResourcePermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.grant_resource_permission_with_options_async(request, runtime)

    def list_addable_roles_with_options(
        self,
        request: dataphin_public_20230630_models.ListAddableRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.ListAddableRolesResponse:
        """
        @summary 获取用户角色列表
        
        @param request: ListAddableRolesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAddableRolesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAddableRoles',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.ListAddableRolesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_addable_roles_with_options_async(
        self,
        request: dataphin_public_20230630_models.ListAddableRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.ListAddableRolesResponse:
        """
        @summary 获取用户角色列表
        
        @param request: ListAddableRolesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAddableRolesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAddableRoles',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.ListAddableRolesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_addable_roles(
        self,
        request: dataphin_public_20230630_models.ListAddableRolesRequest,
    ) -> dataphin_public_20230630_models.ListAddableRolesResponse:
        """
        @summary 获取用户角色列表
        
        @param request: ListAddableRolesRequest
        @return: ListAddableRolesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_addable_roles_with_options(request, runtime)

    async def list_addable_roles_async(
        self,
        request: dataphin_public_20230630_models.ListAddableRolesRequest,
    ) -> dataphin_public_20230630_models.ListAddableRolesResponse:
        """
        @summary 获取用户角色列表
        
        @param request: ListAddableRolesRequest
        @return: ListAddableRolesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_addable_roles_with_options_async(request, runtime)

    def list_addable_users_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.ListAddableUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.ListAddableUsersResponse:
        """
        @summary 获取可加入租户成员列表的用户
        
        @param tmp_req: ListAddableUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAddableUsersResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.ListAddableUsersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_query):
            request.list_query_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAddableUsers',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.ListAddableUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_addable_users_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.ListAddableUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.ListAddableUsersResponse:
        """
        @summary 获取可加入租户成员列表的用户
        
        @param tmp_req: ListAddableUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAddableUsersResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.ListAddableUsersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_query):
            request.list_query_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAddableUsers',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.ListAddableUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_addable_users(
        self,
        request: dataphin_public_20230630_models.ListAddableUsersRequest,
    ) -> dataphin_public_20230630_models.ListAddableUsersResponse:
        """
        @summary 获取可加入租户成员列表的用户
        
        @param request: ListAddableUsersRequest
        @return: ListAddableUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_addable_users_with_options(request, runtime)

    async def list_addable_users_async(
        self,
        request: dataphin_public_20230630_models.ListAddableUsersRequest,
    ) -> dataphin_public_20230630_models.ListAddableUsersResponse:
        """
        @summary 获取可加入租户成员列表的用户
        
        @param request: ListAddableUsersRequest
        @return: ListAddableUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_addable_users_with_options_async(request, runtime)

    def list_alert_events_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.ListAlertEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.ListAlertEventsResponse:
        """
        @summary 根据条件查询多个告警事件
        
        @param tmp_req: ListAlertEventsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAlertEventsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.ListAlertEventsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_query):
            request.list_query_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAlertEvents',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.ListAlertEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_alert_events_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.ListAlertEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.ListAlertEventsResponse:
        """
        @summary 根据条件查询多个告警事件
        
        @param tmp_req: ListAlertEventsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAlertEventsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.ListAlertEventsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_query):
            request.list_query_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAlertEvents',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.ListAlertEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_alert_events(
        self,
        request: dataphin_public_20230630_models.ListAlertEventsRequest,
    ) -> dataphin_public_20230630_models.ListAlertEventsResponse:
        """
        @summary 根据条件查询多个告警事件
        
        @param request: ListAlertEventsRequest
        @return: ListAlertEventsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_alert_events_with_options(request, runtime)

    async def list_alert_events_async(
        self,
        request: dataphin_public_20230630_models.ListAlertEventsRequest,
    ) -> dataphin_public_20230630_models.ListAlertEventsResponse:
        """
        @summary 根据条件查询多个告警事件
        
        @param request: ListAlertEventsRequest
        @return: ListAlertEventsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_alert_events_with_options_async(request, runtime)

    def list_alert_notifications_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.ListAlertNotificationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.ListAlertNotificationsResponse:
        """
        @summary 根据条件查询多个推送记录
        
        @param tmp_req: ListAlertNotificationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAlertNotificationsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.ListAlertNotificationsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_query):
            request.list_query_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAlertNotifications',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.ListAlertNotificationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_alert_notifications_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.ListAlertNotificationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.ListAlertNotificationsResponse:
        """
        @summary 根据条件查询多个推送记录
        
        @param tmp_req: ListAlertNotificationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAlertNotificationsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.ListAlertNotificationsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_query):
            request.list_query_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAlertNotifications',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.ListAlertNotificationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_alert_notifications(
        self,
        request: dataphin_public_20230630_models.ListAlertNotificationsRequest,
    ) -> dataphin_public_20230630_models.ListAlertNotificationsResponse:
        """
        @summary 根据条件查询多个推送记录
        
        @param request: ListAlertNotificationsRequest
        @return: ListAlertNotificationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_alert_notifications_with_options(request, runtime)

    async def list_alert_notifications_async(
        self,
        request: dataphin_public_20230630_models.ListAlertNotificationsRequest,
    ) -> dataphin_public_20230630_models.ListAlertNotificationsResponse:
        """
        @summary 根据条件查询多个推送记录
        
        @param request: ListAlertNotificationsRequest
        @return: ListAlertNotificationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_alert_notifications_with_options_async(request, runtime)

    def list_biz_entities_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.ListBizEntitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.ListBizEntitiesResponse:
        """
        @summary 查询业务实体列表。
        
        @param tmp_req: ListBizEntitiesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBizEntitiesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.ListBizEntitiesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_query):
            request.list_query_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListBizEntities',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.ListBizEntitiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_biz_entities_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.ListBizEntitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.ListBizEntitiesResponse:
        """
        @summary 查询业务实体列表。
        
        @param tmp_req: ListBizEntitiesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBizEntitiesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.ListBizEntitiesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_query):
            request.list_query_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListBizEntities',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.ListBizEntitiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_biz_entities(
        self,
        request: dataphin_public_20230630_models.ListBizEntitiesRequest,
    ) -> dataphin_public_20230630_models.ListBizEntitiesResponse:
        """
        @summary 查询业务实体列表。
        
        @param request: ListBizEntitiesRequest
        @return: ListBizEntitiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_biz_entities_with_options(request, runtime)

    async def list_biz_entities_async(
        self,
        request: dataphin_public_20230630_models.ListBizEntitiesRequest,
    ) -> dataphin_public_20230630_models.ListBizEntitiesResponse:
        """
        @summary 查询业务实体列表。
        
        @param request: ListBizEntitiesRequest
        @return: ListBizEntitiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_biz_entities_with_options_async(request, runtime)

    def list_biz_units_with_options(
        self,
        request: dataphin_public_20230630_models.ListBizUnitsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.ListBizUnitsResponse:
        """
        @summary 获取当前租户下的所有数据板块
        
        @param request: ListBizUnitsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBizUnitsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBizUnits',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.ListBizUnitsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_biz_units_with_options_async(
        self,
        request: dataphin_public_20230630_models.ListBizUnitsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.ListBizUnitsResponse:
        """
        @summary 获取当前租户下的所有数据板块
        
        @param request: ListBizUnitsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBizUnitsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBizUnits',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.ListBizUnitsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_biz_units(
        self,
        request: dataphin_public_20230630_models.ListBizUnitsRequest,
    ) -> dataphin_public_20230630_models.ListBizUnitsResponse:
        """
        @summary 获取当前租户下的所有数据板块
        
        @param request: ListBizUnitsRequest
        @return: ListBizUnitsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_biz_units_with_options(request, runtime)

    async def list_biz_units_async(
        self,
        request: dataphin_public_20230630_models.ListBizUnitsRequest,
    ) -> dataphin_public_20230630_models.ListBizUnitsResponse:
        """
        @summary 获取当前租户下的所有数据板块
        
        @param request: ListBizUnitsRequest
        @return: ListBizUnitsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_biz_units_with_options_async(request, runtime)

    def list_data_domains_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.ListDataDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.ListDataDomainsResponse:
        """
        @summary 获取主题域列表。
        
        @param tmp_req: ListDataDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataDomainsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.ListDataDomainsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_query):
            request.list_query_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDataDomains',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.ListDataDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_domains_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.ListDataDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.ListDataDomainsResponse:
        """
        @summary 获取主题域列表。
        
        @param tmp_req: ListDataDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataDomainsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.ListDataDomainsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_query):
            request.list_query_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDataDomains',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.ListDataDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_domains(
        self,
        request: dataphin_public_20230630_models.ListDataDomainsRequest,
    ) -> dataphin_public_20230630_models.ListDataDomainsResponse:
        """
        @summary 获取主题域列表。
        
        @param request: ListDataDomainsRequest
        @return: ListDataDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_data_domains_with_options(request, runtime)

    async def list_data_domains_async(
        self,
        request: dataphin_public_20230630_models.ListDataDomainsRequest,
    ) -> dataphin_public_20230630_models.ListDataDomainsResponse:
        """
        @summary 获取主题域列表。
        
        @param request: ListDataDomainsRequest
        @return: ListDataDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_data_domains_with_options_async(request, runtime)

    def list_data_source_with_config_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.ListDataSourceWithConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.ListDataSourceWithConfigResponse:
        """
        @summary 搜索数据源，所属结果包含数据源配置项
        
        @param tmp_req: ListDataSourceWithConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataSourceWithConfigResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.ListDataSourceWithConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_query):
            request.list_query_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDataSourceWithConfig',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.ListDataSourceWithConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_source_with_config_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.ListDataSourceWithConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.ListDataSourceWithConfigResponse:
        """
        @summary 搜索数据源，所属结果包含数据源配置项
        
        @param tmp_req: ListDataSourceWithConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataSourceWithConfigResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.ListDataSourceWithConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_query):
            request.list_query_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDataSourceWithConfig',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.ListDataSourceWithConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_source_with_config(
        self,
        request: dataphin_public_20230630_models.ListDataSourceWithConfigRequest,
    ) -> dataphin_public_20230630_models.ListDataSourceWithConfigResponse:
        """
        @summary 搜索数据源，所属结果包含数据源配置项
        
        @param request: ListDataSourceWithConfigRequest
        @return: ListDataSourceWithConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_data_source_with_config_with_options(request, runtime)

    async def list_data_source_with_config_async(
        self,
        request: dataphin_public_20230630_models.ListDataSourceWithConfigRequest,
    ) -> dataphin_public_20230630_models.ListDataSourceWithConfigResponse:
        """
        @summary 搜索数据源，所属结果包含数据源配置项
        
        @param request: ListDataSourceWithConfigRequest
        @return: ListDataSourceWithConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_data_source_with_config_with_options_async(request, runtime)

    def list_files_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.ListFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.ListFilesResponse:
        """
        @summary 遍历菜单树目录文件。
        
        @param tmp_req: ListFilesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFilesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.ListFilesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_query):
            request.list_query_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListFiles',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.ListFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_files_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.ListFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.ListFilesResponse:
        """
        @summary 遍历菜单树目录文件。
        
        @param tmp_req: ListFilesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFilesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.ListFilesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_query):
            request.list_query_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListFiles',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.ListFilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_files(
        self,
        request: dataphin_public_20230630_models.ListFilesRequest,
    ) -> dataphin_public_20230630_models.ListFilesResponse:
        """
        @summary 遍历菜单树目录文件。
        
        @param request: ListFilesRequest
        @return: ListFilesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_files_with_options(request, runtime)

    async def list_files_async(
        self,
        request: dataphin_public_20230630_models.ListFilesRequest,
    ) -> dataphin_public_20230630_models.ListFilesResponse:
        """
        @summary 遍历菜单树目录文件。
        
        @param request: ListFilesRequest
        @return: ListFilesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_files_with_options_async(request, runtime)

    def list_instances_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.ListInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.ListInstancesResponse:
        """
        @summary 分页查询实例。
        
        @param tmp_req: ListInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.ListInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_query):
            request.list_query_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.ListInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.ListInstancesResponse:
        """
        @summary 分页查询实例。
        
        @param tmp_req: ListInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.ListInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_query):
            request.list_query_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.ListInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instances(
        self,
        request: dataphin_public_20230630_models.ListInstancesRequest,
    ) -> dataphin_public_20230630_models.ListInstancesResponse:
        """
        @summary 分页查询实例。
        
        @param request: ListInstancesRequest
        @return: ListInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_instances_with_options(request, runtime)

    async def list_instances_async(
        self,
        request: dataphin_public_20230630_models.ListInstancesRequest,
    ) -> dataphin_public_20230630_models.ListInstancesResponse:
        """
        @summary 分页查询实例。
        
        @param request: ListInstancesRequest
        @return: ListInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_instances_with_options_async(request, runtime)

    def list_node_down_stream_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.ListNodeDownStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.ListNodeDownStreamResponse:
        """
        @summary 查询节点下游，创建补数据工作流时可以作为数据参考
        
        @param tmp_req: ListNodeDownStreamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNodeDownStreamResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.ListNodeDownStreamShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_query):
            request.list_query_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListNodeDownStream',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.ListNodeDownStreamResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_node_down_stream_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.ListNodeDownStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.ListNodeDownStreamResponse:
        """
        @summary 查询节点下游，创建补数据工作流时可以作为数据参考
        
        @param tmp_req: ListNodeDownStreamRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNodeDownStreamResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.ListNodeDownStreamShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_query):
            request.list_query_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListNodeDownStream',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.ListNodeDownStreamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_node_down_stream(
        self,
        request: dataphin_public_20230630_models.ListNodeDownStreamRequest,
    ) -> dataphin_public_20230630_models.ListNodeDownStreamResponse:
        """
        @summary 查询节点下游，创建补数据工作流时可以作为数据参考
        
        @param request: ListNodeDownStreamRequest
        @return: ListNodeDownStreamResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_node_down_stream_with_options(request, runtime)

    async def list_node_down_stream_async(
        self,
        request: dataphin_public_20230630_models.ListNodeDownStreamRequest,
    ) -> dataphin_public_20230630_models.ListNodeDownStreamResponse:
        """
        @summary 查询节点下游，创建补数据工作流时可以作为数据参考
        
        @param request: ListNodeDownStreamRequest
        @return: ListNodeDownStreamResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_node_down_stream_with_options_async(request, runtime)

    def list_nodes_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.ListNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.ListNodesResponse:
        """
        @summary 查询调度节点列表。
        
        @param tmp_req: ListNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNodesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.ListNodesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_query):
            request.list_query_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListNodes',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.ListNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_nodes_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.ListNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.ListNodesResponse:
        """
        @summary 查询调度节点列表。
        
        @param tmp_req: ListNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNodesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.ListNodesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_query):
            request.list_query_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListNodes',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.ListNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_nodes(
        self,
        request: dataphin_public_20230630_models.ListNodesRequest,
    ) -> dataphin_public_20230630_models.ListNodesResponse:
        """
        @summary 查询调度节点列表。
        
        @param request: ListNodesRequest
        @return: ListNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_nodes_with_options(request, runtime)

    async def list_nodes_async(
        self,
        request: dataphin_public_20230630_models.ListNodesRequest,
    ) -> dataphin_public_20230630_models.ListNodesResponse:
        """
        @summary 查询调度节点列表。
        
        @param request: ListNodesRequest
        @return: ListNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_nodes_with_options_async(request, runtime)

    def list_publish_records_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.ListPublishRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.ListPublishRecordsResponse:
        """
        @summary 分页获取发布记录列表
        
        @param tmp_req: ListPublishRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPublishRecordsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.ListPublishRecordsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_query):
            request.list_query_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListPublishRecords',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.ListPublishRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_publish_records_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.ListPublishRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.ListPublishRecordsResponse:
        """
        @summary 分页获取发布记录列表
        
        @param tmp_req: ListPublishRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPublishRecordsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.ListPublishRecordsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_query):
            request.list_query_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListPublishRecords',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.ListPublishRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_publish_records(
        self,
        request: dataphin_public_20230630_models.ListPublishRecordsRequest,
    ) -> dataphin_public_20230630_models.ListPublishRecordsResponse:
        """
        @summary 分页获取发布记录列表
        
        @param request: ListPublishRecordsRequest
        @return: ListPublishRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_publish_records_with_options(request, runtime)

    async def list_publish_records_async(
        self,
        request: dataphin_public_20230630_models.ListPublishRecordsRequest,
    ) -> dataphin_public_20230630_models.ListPublishRecordsResponse:
        """
        @summary 分页获取发布记录列表
        
        @param request: ListPublishRecordsRequest
        @return: ListPublishRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_publish_records_with_options_async(request, runtime)

    def list_resource_permission_operation_log_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.ListResourcePermissionOperationLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.ListResourcePermissionOperationLogResponse:
        """
        @summary 分页获取权限操作列表
        
        @param tmp_req: ListResourcePermissionOperationLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourcePermissionOperationLogResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.ListResourcePermissionOperationLogShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_query):
            request.list_query_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListResourcePermissionOperationLog',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.ListResourcePermissionOperationLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_permission_operation_log_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.ListResourcePermissionOperationLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.ListResourcePermissionOperationLogResponse:
        """
        @summary 分页获取权限操作列表
        
        @param tmp_req: ListResourcePermissionOperationLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourcePermissionOperationLogResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.ListResourcePermissionOperationLogShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_query):
            request.list_query_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListResourcePermissionOperationLog',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.ListResourcePermissionOperationLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_permission_operation_log(
        self,
        request: dataphin_public_20230630_models.ListResourcePermissionOperationLogRequest,
    ) -> dataphin_public_20230630_models.ListResourcePermissionOperationLogResponse:
        """
        @summary 分页获取权限操作列表
        
        @param request: ListResourcePermissionOperationLogRequest
        @return: ListResourcePermissionOperationLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_resource_permission_operation_log_with_options(request, runtime)

    async def list_resource_permission_operation_log_async(
        self,
        request: dataphin_public_20230630_models.ListResourcePermissionOperationLogRequest,
    ) -> dataphin_public_20230630_models.ListResourcePermissionOperationLogResponse:
        """
        @summary 分页获取权限操作列表
        
        @param request: ListResourcePermissionOperationLogRequest
        @return: ListResourcePermissionOperationLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_resource_permission_operation_log_with_options_async(request, runtime)

    def list_resource_permissions_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.ListResourcePermissionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.ListResourcePermissionsResponse:
        """
        @summary 分页获取权限记录列表
        
        @param tmp_req: ListResourcePermissionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourcePermissionsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.ListResourcePermissionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_query):
            request.list_query_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListResourcePermissions',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.ListResourcePermissionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_permissions_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.ListResourcePermissionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.ListResourcePermissionsResponse:
        """
        @summary 分页获取权限记录列表
        
        @param tmp_req: ListResourcePermissionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourcePermissionsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.ListResourcePermissionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_query):
            request.list_query_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListResourcePermissions',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.ListResourcePermissionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_permissions(
        self,
        request: dataphin_public_20230630_models.ListResourcePermissionsRequest,
    ) -> dataphin_public_20230630_models.ListResourcePermissionsResponse:
        """
        @summary 分页获取权限记录列表
        
        @param request: ListResourcePermissionsRequest
        @return: ListResourcePermissionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_resource_permissions_with_options(request, runtime)

    async def list_resource_permissions_async(
        self,
        request: dataphin_public_20230630_models.ListResourcePermissionsRequest,
    ) -> dataphin_public_20230630_models.ListResourcePermissionsResponse:
        """
        @summary 分页获取权限记录列表
        
        @param request: ListResourcePermissionsRequest
        @return: ListResourcePermissionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_resource_permissions_with_options_async(request, runtime)

    def list_submit_records_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.ListSubmitRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.ListSubmitRecordsResponse:
        """
        @summary 分页获取待发布记录列表
        
        @param tmp_req: ListSubmitRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSubmitRecordsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.ListSubmitRecordsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_query):
            request.list_query_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSubmitRecords',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.ListSubmitRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_submit_records_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.ListSubmitRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.ListSubmitRecordsResponse:
        """
        @summary 分页获取待发布记录列表
        
        @param tmp_req: ListSubmitRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSubmitRecordsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.ListSubmitRecordsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_query):
            request.list_query_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSubmitRecords',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.ListSubmitRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_submit_records(
        self,
        request: dataphin_public_20230630_models.ListSubmitRecordsRequest,
    ) -> dataphin_public_20230630_models.ListSubmitRecordsResponse:
        """
        @summary 分页获取待发布记录列表
        
        @param request: ListSubmitRecordsRequest
        @return: ListSubmitRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_submit_records_with_options(request, runtime)

    async def list_submit_records_async(
        self,
        request: dataphin_public_20230630_models.ListSubmitRecordsRequest,
    ) -> dataphin_public_20230630_models.ListSubmitRecordsResponse:
        """
        @summary 分页获取待发布记录列表
        
        @param request: ListSubmitRecordsRequest
        @return: ListSubmitRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_submit_records_with_options_async(request, runtime)

    def list_tenant_members_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.ListTenantMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.ListTenantMembersResponse:
        """
        @summary 查询租户成员列表
        
        @param tmp_req: ListTenantMembersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTenantMembersResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.ListTenantMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_query):
            request.list_query_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTenantMembers',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.ListTenantMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tenant_members_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.ListTenantMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.ListTenantMembersResponse:
        """
        @summary 查询租户成员列表
        
        @param tmp_req: ListTenantMembersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTenantMembersResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.ListTenantMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_query):
            request.list_query_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTenantMembers',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.ListTenantMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tenant_members(
        self,
        request: dataphin_public_20230630_models.ListTenantMembersRequest,
    ) -> dataphin_public_20230630_models.ListTenantMembersResponse:
        """
        @summary 查询租户成员列表
        
        @param request: ListTenantMembersRequest
        @return: ListTenantMembersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tenant_members_with_options(request, runtime)

    async def list_tenant_members_async(
        self,
        request: dataphin_public_20230630_models.ListTenantMembersRequest,
    ) -> dataphin_public_20230630_models.ListTenantMembersResponse:
        """
        @summary 查询租户成员列表
        
        @param request: ListTenantMembersRequest
        @return: ListTenantMembersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tenant_members_with_options_async(request, runtime)

    def list_user_group_members_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.ListUserGroupMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.ListUserGroupMembersResponse:
        """
        @summary 用户组成员列表分页查询.
        
        @param tmp_req: ListUserGroupMembersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserGroupMembersResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.ListUserGroupMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_query):
            request.list_query_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListUserGroupMembers',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.ListUserGroupMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_group_members_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.ListUserGroupMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.ListUserGroupMembersResponse:
        """
        @summary 用户组成员列表分页查询.
        
        @param tmp_req: ListUserGroupMembersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserGroupMembersResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.ListUserGroupMembersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_query):
            request.list_query_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListUserGroupMembers',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.ListUserGroupMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_group_members(
        self,
        request: dataphin_public_20230630_models.ListUserGroupMembersRequest,
    ) -> dataphin_public_20230630_models.ListUserGroupMembersResponse:
        """
        @summary 用户组成员列表分页查询.
        
        @param request: ListUserGroupMembersRequest
        @return: ListUserGroupMembersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_user_group_members_with_options(request, runtime)

    async def list_user_group_members_async(
        self,
        request: dataphin_public_20230630_models.ListUserGroupMembersRequest,
    ) -> dataphin_public_20230630_models.ListUserGroupMembersResponse:
        """
        @summary 用户组成员列表分页查询.
        
        @param request: ListUserGroupMembersRequest
        @return: ListUserGroupMembersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_user_group_members_with_options_async(request, runtime)

    def list_user_groups_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.ListUserGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.ListUserGroupsResponse:
        """
        @summary 用户组列表分页查询.
        
        @param tmp_req: ListUserGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserGroupsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.ListUserGroupsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_query):
            request.list_query_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListUserGroups',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.ListUserGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_groups_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.ListUserGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.ListUserGroupsResponse:
        """
        @summary 用户组列表分页查询.
        
        @param tmp_req: ListUserGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserGroupsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.ListUserGroupsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_query):
            request.list_query_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.list_query, 'ListQuery', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.list_query_shrink):
            body['ListQuery'] = request.list_query_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListUserGroups',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.ListUserGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_groups(
        self,
        request: dataphin_public_20230630_models.ListUserGroupsRequest,
    ) -> dataphin_public_20230630_models.ListUserGroupsResponse:
        """
        @summary 用户组列表分页查询.
        
        @param request: ListUserGroupsRequest
        @return: ListUserGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_user_groups_with_options(request, runtime)

    async def list_user_groups_async(
        self,
        request: dataphin_public_20230630_models.ListUserGroupsRequest,
    ) -> dataphin_public_20230630_models.ListUserGroupsResponse:
        """
        @summary 用户组列表分页查询.
        
        @param request: ListUserGroupsRequest
        @return: ListUserGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_user_groups_with_options_async(request, runtime)

    def offline_batch_task_with_options(
        self,
        request: dataphin_public_20230630_models.OfflineBatchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.OfflineBatchTaskResponse:
        """
        @summary 下线离线计算任务。
        
        @param request: OfflineBatchTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OfflineBatchTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.file_id):
            query['FileId'] = request.file_id
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OfflineBatchTask',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.OfflineBatchTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def offline_batch_task_with_options_async(
        self,
        request: dataphin_public_20230630_models.OfflineBatchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.OfflineBatchTaskResponse:
        """
        @summary 下线离线计算任务。
        
        @param request: OfflineBatchTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OfflineBatchTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.file_id):
            query['FileId'] = request.file_id
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OfflineBatchTask',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.OfflineBatchTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def offline_batch_task(
        self,
        request: dataphin_public_20230630_models.OfflineBatchTaskRequest,
    ) -> dataphin_public_20230630_models.OfflineBatchTaskResponse:
        """
        @summary 下线离线计算任务。
        
        @param request: OfflineBatchTaskRequest
        @return: OfflineBatchTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.offline_batch_task_with_options(request, runtime)

    async def offline_batch_task_async(
        self,
        request: dataphin_public_20230630_models.OfflineBatchTaskRequest,
    ) -> dataphin_public_20230630_models.OfflineBatchTaskResponse:
        """
        @summary 下线离线计算任务。
        
        @param request: OfflineBatchTaskRequest
        @return: OfflineBatchTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.offline_batch_task_with_options_async(request, runtime)

    def offline_biz_entity_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.OfflineBizEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.OfflineBizEntityResponse:
        """
        @summary 下线业务实体、
        
        @param tmp_req: OfflineBizEntityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OfflineBizEntityResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.OfflineBizEntityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.offline_command):
            request.offline_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.offline_command, 'OfflineCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.offline_command_shrink):
            body['OfflineCommand'] = request.offline_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OfflineBizEntity',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.OfflineBizEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def offline_biz_entity_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.OfflineBizEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.OfflineBizEntityResponse:
        """
        @summary 下线业务实体、
        
        @param tmp_req: OfflineBizEntityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OfflineBizEntityResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.OfflineBizEntityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.offline_command):
            request.offline_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.offline_command, 'OfflineCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.offline_command_shrink):
            body['OfflineCommand'] = request.offline_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OfflineBizEntity',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.OfflineBizEntityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def offline_biz_entity(
        self,
        request: dataphin_public_20230630_models.OfflineBizEntityRequest,
    ) -> dataphin_public_20230630_models.OfflineBizEntityResponse:
        """
        @summary 下线业务实体、
        
        @param request: OfflineBizEntityRequest
        @return: OfflineBizEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.offline_biz_entity_with_options(request, runtime)

    async def offline_biz_entity_async(
        self,
        request: dataphin_public_20230630_models.OfflineBizEntityRequest,
    ) -> dataphin_public_20230630_models.OfflineBizEntityResponse:
        """
        @summary 下线业务实体、
        
        @param request: OfflineBizEntityRequest
        @return: OfflineBizEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.offline_biz_entity_with_options_async(request, runtime)

    def online_biz_entity_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.OnlineBizEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.OnlineBizEntityResponse:
        """
        @summary 上线业务实体。
        
        @param tmp_req: OnlineBizEntityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnlineBizEntityResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.OnlineBizEntityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.online_command):
            request.online_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.online_command, 'OnlineCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.online_command_shrink):
            body['OnlineCommand'] = request.online_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OnlineBizEntity',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.OnlineBizEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def online_biz_entity_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.OnlineBizEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.OnlineBizEntityResponse:
        """
        @summary 上线业务实体。
        
        @param tmp_req: OnlineBizEntityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OnlineBizEntityResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.OnlineBizEntityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.online_command):
            request.online_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.online_command, 'OnlineCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.online_command_shrink):
            body['OnlineCommand'] = request.online_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OnlineBizEntity',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.OnlineBizEntityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def online_biz_entity(
        self,
        request: dataphin_public_20230630_models.OnlineBizEntityRequest,
    ) -> dataphin_public_20230630_models.OnlineBizEntityResponse:
        """
        @summary 上线业务实体。
        
        @param request: OnlineBizEntityRequest
        @return: OnlineBizEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.online_biz_entity_with_options(request, runtime)

    async def online_biz_entity_async(
        self,
        request: dataphin_public_20230630_models.OnlineBizEntityRequest,
    ) -> dataphin_public_20230630_models.OnlineBizEntityResponse:
        """
        @summary 上线业务实体。
        
        @param request: OnlineBizEntityRequest
        @return: OnlineBizEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.online_biz_entity_with_options_async(request, runtime)

    def operate_instance_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.OperateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.OperateInstanceResponse:
        """
        @summary 运维实例。
        
        @param tmp_req: OperateInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OperateInstanceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.OperateInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.operate_command):
            request.operate_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.operate_command, 'OperateCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.operate_command_shrink):
            body['OperateCommand'] = request.operate_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OperateInstance',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.OperateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_instance_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.OperateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.OperateInstanceResponse:
        """
        @summary 运维实例。
        
        @param tmp_req: OperateInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OperateInstanceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.OperateInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.operate_command):
            request.operate_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.operate_command, 'OperateCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.operate_command_shrink):
            body['OperateCommand'] = request.operate_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OperateInstance',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.OperateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_instance(
        self,
        request: dataphin_public_20230630_models.OperateInstanceRequest,
    ) -> dataphin_public_20230630_models.OperateInstanceResponse:
        """
        @summary 运维实例。
        
        @param request: OperateInstanceRequest
        @return: OperateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.operate_instance_with_options(request, runtime)

    async def operate_instance_async(
        self,
        request: dataphin_public_20230630_models.OperateInstanceRequest,
    ) -> dataphin_public_20230630_models.OperateInstanceResponse:
        """
        @summary 运维实例。
        
        @param request: OperateInstanceRequest
        @return: OperateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.operate_instance_with_options_async(request, runtime)

    def parse_batch_task_dependency_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.ParseBatchTaskDependencyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.ParseBatchTaskDependencyResponse:
        """
        @summary 解析离线计算任务的逻辑表依赖，注意解析结果上游依赖信息中可能包含自依赖节点（上游节点ID和解析代码的任务节点ID相同）需要用户自己进行处理。
        
        @param tmp_req: ParseBatchTaskDependencyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ParseBatchTaskDependencyResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.ParseBatchTaskDependencyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parse_command):
            request.parse_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parse_command, 'ParseCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.parse_command_shrink):
            body['ParseCommand'] = request.parse_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ParseBatchTaskDependency',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.ParseBatchTaskDependencyResponse(),
            self.call_api(params, req, runtime)
        )

    async def parse_batch_task_dependency_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.ParseBatchTaskDependencyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.ParseBatchTaskDependencyResponse:
        """
        @summary 解析离线计算任务的逻辑表依赖，注意解析结果上游依赖信息中可能包含自依赖节点（上游节点ID和解析代码的任务节点ID相同）需要用户自己进行处理。
        
        @param tmp_req: ParseBatchTaskDependencyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ParseBatchTaskDependencyResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.ParseBatchTaskDependencyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parse_command):
            request.parse_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parse_command, 'ParseCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.parse_command_shrink):
            body['ParseCommand'] = request.parse_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ParseBatchTaskDependency',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.ParseBatchTaskDependencyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def parse_batch_task_dependency(
        self,
        request: dataphin_public_20230630_models.ParseBatchTaskDependencyRequest,
    ) -> dataphin_public_20230630_models.ParseBatchTaskDependencyResponse:
        """
        @summary 解析离线计算任务的逻辑表依赖，注意解析结果上游依赖信息中可能包含自依赖节点（上游节点ID和解析代码的任务节点ID相同）需要用户自己进行处理。
        
        @param request: ParseBatchTaskDependencyRequest
        @return: ParseBatchTaskDependencyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.parse_batch_task_dependency_with_options(request, runtime)

    async def parse_batch_task_dependency_async(
        self,
        request: dataphin_public_20230630_models.ParseBatchTaskDependencyRequest,
    ) -> dataphin_public_20230630_models.ParseBatchTaskDependencyResponse:
        """
        @summary 解析离线计算任务的逻辑表依赖，注意解析结果上游依赖信息中可能包含自依赖节点（上游节点ID和解析代码的任务节点ID相同）需要用户自己进行处理。
        
        @param request: ParseBatchTaskDependencyRequest
        @return: ParseBatchTaskDependencyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.parse_batch_task_dependency_with_options_async(request, runtime)

    def pause_physical_node_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.PausePhysicalNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.PausePhysicalNodeResponse:
        """
        @summary 暂停物理节点调度。
        
        @param tmp_req: PausePhysicalNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PausePhysicalNodeResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.PausePhysicalNodeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.pause_command):
            request.pause_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.pause_command, 'PauseCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.pause_command_shrink):
            body['PauseCommand'] = request.pause_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PausePhysicalNode',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.PausePhysicalNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def pause_physical_node_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.PausePhysicalNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.PausePhysicalNodeResponse:
        """
        @summary 暂停物理节点调度。
        
        @param tmp_req: PausePhysicalNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PausePhysicalNodeResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.PausePhysicalNodeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.pause_command):
            request.pause_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.pause_command, 'PauseCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.pause_command_shrink):
            body['PauseCommand'] = request.pause_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PausePhysicalNode',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.PausePhysicalNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pause_physical_node(
        self,
        request: dataphin_public_20230630_models.PausePhysicalNodeRequest,
    ) -> dataphin_public_20230630_models.PausePhysicalNodeResponse:
        """
        @summary 暂停物理节点调度。
        
        @param request: PausePhysicalNodeRequest
        @return: PausePhysicalNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.pause_physical_node_with_options(request, runtime)

    async def pause_physical_node_async(
        self,
        request: dataphin_public_20230630_models.PausePhysicalNodeRequest,
    ) -> dataphin_public_20230630_models.PausePhysicalNodeResponse:
        """
        @summary 暂停物理节点调度。
        
        @param request: PausePhysicalNodeRequest
        @return: PausePhysicalNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.pause_physical_node_with_options_async(request, runtime)

    def publish_object_list_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.PublishObjectListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.PublishObjectListResponse:
        """
        @summary 批量发布对象
        
        @param tmp_req: PublishObjectListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PublishObjectListResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.PublishObjectListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.publish_command):
            request.publish_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.publish_command, 'PublishCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.publish_command_shrink):
            body['PublishCommand'] = request.publish_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PublishObjectList',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.PublishObjectListResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_object_list_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.PublishObjectListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.PublishObjectListResponse:
        """
        @summary 批量发布对象
        
        @param tmp_req: PublishObjectListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PublishObjectListResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.PublishObjectListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.publish_command):
            request.publish_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.publish_command, 'PublishCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.publish_command_shrink):
            body['PublishCommand'] = request.publish_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PublishObjectList',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.PublishObjectListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_object_list(
        self,
        request: dataphin_public_20230630_models.PublishObjectListRequest,
    ) -> dataphin_public_20230630_models.PublishObjectListResponse:
        """
        @summary 批量发布对象
        
        @param request: PublishObjectListRequest
        @return: PublishObjectListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.publish_object_list_with_options(request, runtime)

    async def publish_object_list_async(
        self,
        request: dataphin_public_20230630_models.PublishObjectListRequest,
    ) -> dataphin_public_20230630_models.PublishObjectListResponse:
        """
        @summary 批量发布对象
        
        @param request: PublishObjectListRequest
        @return: PublishObjectListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.publish_object_list_with_options_async(request, runtime)

    def remove_tenant_member_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.RemoveTenantMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.RemoveTenantMemberResponse:
        """
        @summary 删除租户成员
        
        @param tmp_req: RemoveTenantMemberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveTenantMemberResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.RemoveTenantMemberShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.remove_command):
            request.remove_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.remove_command, 'RemoveCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.remove_command_shrink):
            body['RemoveCommand'] = request.remove_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveTenantMember',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.RemoveTenantMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_tenant_member_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.RemoveTenantMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.RemoveTenantMemberResponse:
        """
        @summary 删除租户成员
        
        @param tmp_req: RemoveTenantMemberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveTenantMemberResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.RemoveTenantMemberShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.remove_command):
            request.remove_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.remove_command, 'RemoveCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.remove_command_shrink):
            body['RemoveCommand'] = request.remove_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveTenantMember',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.RemoveTenantMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_tenant_member(
        self,
        request: dataphin_public_20230630_models.RemoveTenantMemberRequest,
    ) -> dataphin_public_20230630_models.RemoveTenantMemberResponse:
        """
        @summary 删除租户成员
        
        @param request: RemoveTenantMemberRequest
        @return: RemoveTenantMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_tenant_member_with_options(request, runtime)

    async def remove_tenant_member_async(
        self,
        request: dataphin_public_20230630_models.RemoveTenantMemberRequest,
    ) -> dataphin_public_20230630_models.RemoveTenantMemberResponse:
        """
        @summary 删除租户成员
        
        @param request: RemoveTenantMemberRequest
        @return: RemoveTenantMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_tenant_member_with_options_async(request, runtime)

    def remove_user_group_member_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.RemoveUserGroupMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.RemoveUserGroupMemberResponse:
        """
        @summary 移除用户组成员.
        
        @param tmp_req: RemoveUserGroupMemberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveUserGroupMemberResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.RemoveUserGroupMemberShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.remove_command):
            request.remove_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.remove_command, 'RemoveCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.remove_command_shrink):
            body['RemoveCommand'] = request.remove_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveUserGroupMember',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.RemoveUserGroupMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_user_group_member_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.RemoveUserGroupMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.RemoveUserGroupMemberResponse:
        """
        @summary 移除用户组成员.
        
        @param tmp_req: RemoveUserGroupMemberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveUserGroupMemberResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.RemoveUserGroupMemberShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.remove_command):
            request.remove_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.remove_command, 'RemoveCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.remove_command_shrink):
            body['RemoveCommand'] = request.remove_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveUserGroupMember',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.RemoveUserGroupMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_user_group_member(
        self,
        request: dataphin_public_20230630_models.RemoveUserGroupMemberRequest,
    ) -> dataphin_public_20230630_models.RemoveUserGroupMemberResponse:
        """
        @summary 移除用户组成员.
        
        @param request: RemoveUserGroupMemberRequest
        @return: RemoveUserGroupMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_user_group_member_with_options(request, runtime)

    async def remove_user_group_member_async(
        self,
        request: dataphin_public_20230630_models.RemoveUserGroupMemberRequest,
    ) -> dataphin_public_20230630_models.RemoveUserGroupMemberResponse:
        """
        @summary 移除用户组成员.
        
        @param request: RemoveUserGroupMemberRequest
        @return: RemoveUserGroupMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_user_group_member_with_options_async(request, runtime)

    def resume_physical_node_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.ResumePhysicalNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.ResumePhysicalNodeResponse:
        """
        @summary 恢复物理节点调度。
        
        @param tmp_req: ResumePhysicalNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResumePhysicalNodeResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.ResumePhysicalNodeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resume_command):
            request.resume_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resume_command, 'ResumeCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.resume_command_shrink):
            body['ResumeCommand'] = request.resume_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResumePhysicalNode',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.ResumePhysicalNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_physical_node_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.ResumePhysicalNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.ResumePhysicalNodeResponse:
        """
        @summary 恢复物理节点调度。
        
        @param tmp_req: ResumePhysicalNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResumePhysicalNodeResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.ResumePhysicalNodeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resume_command):
            request.resume_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resume_command, 'ResumeCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.env):
            query['Env'] = request.env
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.resume_command_shrink):
            body['ResumeCommand'] = request.resume_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResumePhysicalNode',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.ResumePhysicalNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_physical_node(
        self,
        request: dataphin_public_20230630_models.ResumePhysicalNodeRequest,
    ) -> dataphin_public_20230630_models.ResumePhysicalNodeResponse:
        """
        @summary 恢复物理节点调度。
        
        @param request: ResumePhysicalNodeRequest
        @return: ResumePhysicalNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.resume_physical_node_with_options(request, runtime)

    async def resume_physical_node_async(
        self,
        request: dataphin_public_20230630_models.ResumePhysicalNodeRequest,
    ) -> dataphin_public_20230630_models.ResumePhysicalNodeResponse:
        """
        @summary 恢复物理节点调度。
        
        @param request: ResumePhysicalNodeRequest
        @return: ResumePhysicalNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.resume_physical_node_with_options_async(request, runtime)

    def revoke_resource_permission_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.RevokeResourcePermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.RevokeResourcePermissionResponse:
        """
        @summary 回收用户资源授权
        
        @param tmp_req: RevokeResourcePermissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RevokeResourcePermissionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.RevokeResourcePermissionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.revoke_command):
            request.revoke_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.revoke_command, 'RevokeCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.revoke_command_shrink):
            body['RevokeCommand'] = request.revoke_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RevokeResourcePermission',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.RevokeResourcePermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_resource_permission_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.RevokeResourcePermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.RevokeResourcePermissionResponse:
        """
        @summary 回收用户资源授权
        
        @param tmp_req: RevokeResourcePermissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RevokeResourcePermissionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.RevokeResourcePermissionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.revoke_command):
            request.revoke_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.revoke_command, 'RevokeCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.revoke_command_shrink):
            body['RevokeCommand'] = request.revoke_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RevokeResourcePermission',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.RevokeResourcePermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_resource_permission(
        self,
        request: dataphin_public_20230630_models.RevokeResourcePermissionRequest,
    ) -> dataphin_public_20230630_models.RevokeResourcePermissionResponse:
        """
        @summary 回收用户资源授权
        
        @param request: RevokeResourcePermissionRequest
        @return: RevokeResourcePermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.revoke_resource_permission_with_options(request, runtime)

    async def revoke_resource_permission_async(
        self,
        request: dataphin_public_20230630_models.RevokeResourcePermissionRequest,
    ) -> dataphin_public_20230630_models.RevokeResourcePermissionResponse:
        """
        @summary 回收用户资源授权
        
        @param request: RevokeResourcePermissionRequest
        @return: RevokeResourcePermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.revoke_resource_permission_with_options_async(request, runtime)

    def stop_ad_hoc_task_with_options(
        self,
        request: dataphin_public_20230630_models.StopAdHocTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.StopAdHocTaskResponse:
        """
        @summary 终止即席查询任务。
        
        @param request: StopAdHocTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopAdHocTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopAdHocTask',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.StopAdHocTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_ad_hoc_task_with_options_async(
        self,
        request: dataphin_public_20230630_models.StopAdHocTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.StopAdHocTaskResponse:
        """
        @summary 终止即席查询任务。
        
        @param request: StopAdHocTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopAdHocTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopAdHocTask',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.StopAdHocTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_ad_hoc_task(
        self,
        request: dataphin_public_20230630_models.StopAdHocTaskRequest,
    ) -> dataphin_public_20230630_models.StopAdHocTaskResponse:
        """
        @summary 终止即席查询任务。
        
        @param request: StopAdHocTaskRequest
        @return: StopAdHocTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_ad_hoc_task_with_options(request, runtime)

    async def stop_ad_hoc_task_async(
        self,
        request: dataphin_public_20230630_models.StopAdHocTaskRequest,
    ) -> dataphin_public_20230630_models.StopAdHocTaskResponse:
        """
        @summary 终止即席查询任务。
        
        @param request: StopAdHocTaskRequest
        @return: StopAdHocTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_ad_hoc_task_with_options_async(request, runtime)

    def submit_batch_task_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.SubmitBatchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.SubmitBatchTaskResponse:
        """
        @summary 提交离线计算任务。
        
        @param tmp_req: SubmitBatchTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitBatchTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.SubmitBatchTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.submit_command):
            request.submit_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.submit_command, 'SubmitCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.submit_command_shrink):
            body['SubmitCommand'] = request.submit_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitBatchTask',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.SubmitBatchTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_batch_task_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.SubmitBatchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.SubmitBatchTaskResponse:
        """
        @summary 提交离线计算任务。
        
        @param tmp_req: SubmitBatchTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitBatchTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.SubmitBatchTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.submit_command):
            request.submit_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.submit_command, 'SubmitCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.submit_command_shrink):
            body['SubmitCommand'] = request.submit_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitBatchTask',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.SubmitBatchTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_batch_task(
        self,
        request: dataphin_public_20230630_models.SubmitBatchTaskRequest,
    ) -> dataphin_public_20230630_models.SubmitBatchTaskResponse:
        """
        @summary 提交离线计算任务。
        
        @param request: SubmitBatchTaskRequest
        @return: SubmitBatchTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_batch_task_with_options(request, runtime)

    async def submit_batch_task_async(
        self,
        request: dataphin_public_20230630_models.SubmitBatchTaskRequest,
    ) -> dataphin_public_20230630_models.SubmitBatchTaskResponse:
        """
        @summary 提交离线计算任务。
        
        @param request: SubmitBatchTaskRequest
        @return: SubmitBatchTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_batch_task_with_options_async(request, runtime)

    def update_ad_hoc_file_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.UpdateAdHocFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.UpdateAdHocFileResponse:
        """
        @summary 编辑即席查询文件。
        
        @param tmp_req: UpdateAdHocFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAdHocFileResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.UpdateAdHocFileShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.update_command):
            request.update_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAdHocFile',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.UpdateAdHocFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ad_hoc_file_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.UpdateAdHocFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.UpdateAdHocFileResponse:
        """
        @summary 编辑即席查询文件。
        
        @param tmp_req: UpdateAdHocFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAdHocFileResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.UpdateAdHocFileShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.update_command):
            request.update_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAdHocFile',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.UpdateAdHocFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ad_hoc_file(
        self,
        request: dataphin_public_20230630_models.UpdateAdHocFileRequest,
    ) -> dataphin_public_20230630_models.UpdateAdHocFileResponse:
        """
        @summary 编辑即席查询文件。
        
        @param request: UpdateAdHocFileRequest
        @return: UpdateAdHocFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_ad_hoc_file_with_options(request, runtime)

    async def update_ad_hoc_file_async(
        self,
        request: dataphin_public_20230630_models.UpdateAdHocFileRequest,
    ) -> dataphin_public_20230630_models.UpdateAdHocFileResponse:
        """
        @summary 编辑即席查询文件。
        
        @param request: UpdateAdHocFileRequest
        @return: UpdateAdHocFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_ad_hoc_file_with_options_async(request, runtime)

    def update_batch_task_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.UpdateBatchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.UpdateBatchTaskResponse:
        """
        @summary 编辑离线计算任务。
        
        @param tmp_req: UpdateBatchTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateBatchTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.UpdateBatchTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.update_command):
            request.update_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateBatchTask',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.UpdateBatchTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_batch_task_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.UpdateBatchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.UpdateBatchTaskResponse:
        """
        @summary 编辑离线计算任务。
        
        @param tmp_req: UpdateBatchTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateBatchTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.UpdateBatchTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.update_command):
            request.update_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateBatchTask',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.UpdateBatchTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_batch_task(
        self,
        request: dataphin_public_20230630_models.UpdateBatchTaskRequest,
    ) -> dataphin_public_20230630_models.UpdateBatchTaskResponse:
        """
        @summary 编辑离线计算任务。
        
        @param request: UpdateBatchTaskRequest
        @return: UpdateBatchTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_batch_task_with_options(request, runtime)

    async def update_batch_task_async(
        self,
        request: dataphin_public_20230630_models.UpdateBatchTaskRequest,
    ) -> dataphin_public_20230630_models.UpdateBatchTaskResponse:
        """
        @summary 编辑离线计算任务。
        
        @param request: UpdateBatchTaskRequest
        @return: UpdateBatchTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_batch_task_with_options_async(request, runtime)

    def update_batch_task_udf_lineages_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.UpdateBatchTaskUdfLineagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.UpdateBatchTaskUdfLineagesResponse:
        """
        @summary 编辑离线计算任务自定义血缘。
        
        @param tmp_req: UpdateBatchTaskUdfLineagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateBatchTaskUdfLineagesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.UpdateBatchTaskUdfLineagesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.update_command):
            request.update_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateBatchTaskUdfLineages',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.UpdateBatchTaskUdfLineagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_batch_task_udf_lineages_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.UpdateBatchTaskUdfLineagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.UpdateBatchTaskUdfLineagesResponse:
        """
        @summary 编辑离线计算任务自定义血缘。
        
        @param tmp_req: UpdateBatchTaskUdfLineagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateBatchTaskUdfLineagesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.UpdateBatchTaskUdfLineagesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.update_command):
            request.update_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateBatchTaskUdfLineages',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.UpdateBatchTaskUdfLineagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_batch_task_udf_lineages(
        self,
        request: dataphin_public_20230630_models.UpdateBatchTaskUdfLineagesRequest,
    ) -> dataphin_public_20230630_models.UpdateBatchTaskUdfLineagesResponse:
        """
        @summary 编辑离线计算任务自定义血缘。
        
        @param request: UpdateBatchTaskUdfLineagesRequest
        @return: UpdateBatchTaskUdfLineagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_batch_task_udf_lineages_with_options(request, runtime)

    async def update_batch_task_udf_lineages_async(
        self,
        request: dataphin_public_20230630_models.UpdateBatchTaskUdfLineagesRequest,
    ) -> dataphin_public_20230630_models.UpdateBatchTaskUdfLineagesResponse:
        """
        @summary 编辑离线计算任务自定义血缘。
        
        @param request: UpdateBatchTaskUdfLineagesRequest
        @return: UpdateBatchTaskUdfLineagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_batch_task_udf_lineages_with_options_async(request, runtime)

    def update_biz_entity_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.UpdateBizEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.UpdateBizEntityResponse:
        """
        @summary 更新业务实体、
        
        @param tmp_req: UpdateBizEntityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateBizEntityResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.UpdateBizEntityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.update_command):
            request.update_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateBizEntity',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.UpdateBizEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_biz_entity_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.UpdateBizEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.UpdateBizEntityResponse:
        """
        @summary 更新业务实体、
        
        @param tmp_req: UpdateBizEntityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateBizEntityResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.UpdateBizEntityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.update_command):
            request.update_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateBizEntity',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.UpdateBizEntityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_biz_entity(
        self,
        request: dataphin_public_20230630_models.UpdateBizEntityRequest,
    ) -> dataphin_public_20230630_models.UpdateBizEntityResponse:
        """
        @summary 更新业务实体、
        
        @param request: UpdateBizEntityRequest
        @return: UpdateBizEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_biz_entity_with_options(request, runtime)

    async def update_biz_entity_async(
        self,
        request: dataphin_public_20230630_models.UpdateBizEntityRequest,
    ) -> dataphin_public_20230630_models.UpdateBizEntityResponse:
        """
        @summary 更新业务实体、
        
        @param request: UpdateBizEntityRequest
        @return: UpdateBizEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_biz_entity_with_options_async(request, runtime)

    def update_biz_unit_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.UpdateBizUnitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.UpdateBizUnitResponse:
        """
        @summary 更新数据板块。
        
        @param tmp_req: UpdateBizUnitRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateBizUnitResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.UpdateBizUnitShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.update_command):
            request.update_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateBizUnit',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.UpdateBizUnitResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_biz_unit_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.UpdateBizUnitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.UpdateBizUnitResponse:
        """
        @summary 更新数据板块。
        
        @param tmp_req: UpdateBizUnitRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateBizUnitResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.UpdateBizUnitShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.update_command):
            request.update_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateBizUnit',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.UpdateBizUnitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_biz_unit(
        self,
        request: dataphin_public_20230630_models.UpdateBizUnitRequest,
    ) -> dataphin_public_20230630_models.UpdateBizUnitResponse:
        """
        @summary 更新数据板块。
        
        @param request: UpdateBizUnitRequest
        @return: UpdateBizUnitResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_biz_unit_with_options(request, runtime)

    async def update_biz_unit_async(
        self,
        request: dataphin_public_20230630_models.UpdateBizUnitRequest,
    ) -> dataphin_public_20230630_models.UpdateBizUnitResponse:
        """
        @summary 更新数据板块。
        
        @param request: UpdateBizUnitRequest
        @return: UpdateBizUnitResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_biz_unit_with_options_async(request, runtime)

    def update_data_domain_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.UpdateDataDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.UpdateDataDomainResponse:
        """
        @summary 更新主题域。
        
        @param tmp_req: UpdateDataDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDataDomainResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.UpdateDataDomainShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.update_command):
            request.update_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDataDomain',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.UpdateDataDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_data_domain_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.UpdateDataDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.UpdateDataDomainResponse:
        """
        @summary 更新主题域。
        
        @param tmp_req: UpdateDataDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDataDomainResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.UpdateDataDomainShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.update_command):
            request.update_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDataDomain',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.UpdateDataDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_data_domain(
        self,
        request: dataphin_public_20230630_models.UpdateDataDomainRequest,
    ) -> dataphin_public_20230630_models.UpdateDataDomainResponse:
        """
        @summary 更新主题域。
        
        @param request: UpdateDataDomainRequest
        @return: UpdateDataDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_data_domain_with_options(request, runtime)

    async def update_data_domain_async(
        self,
        request: dataphin_public_20230630_models.UpdateDataDomainRequest,
    ) -> dataphin_public_20230630_models.UpdateDataDomainResponse:
        """
        @summary 更新主题域。
        
        @param request: UpdateDataDomainRequest
        @return: UpdateDataDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_data_domain_with_options_async(request, runtime)

    def update_data_source_basic_info_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.UpdateDataSourceBasicInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.UpdateDataSourceBasicInfoResponse:
        """
        @summary 编辑数据源基本信息
        
        @param tmp_req: UpdateDataSourceBasicInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDataSourceBasicInfoResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.UpdateDataSourceBasicInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.update_command):
            request.update_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDataSourceBasicInfo',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.UpdateDataSourceBasicInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_data_source_basic_info_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.UpdateDataSourceBasicInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.UpdateDataSourceBasicInfoResponse:
        """
        @summary 编辑数据源基本信息
        
        @param tmp_req: UpdateDataSourceBasicInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDataSourceBasicInfoResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.UpdateDataSourceBasicInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.update_command):
            request.update_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDataSourceBasicInfo',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.UpdateDataSourceBasicInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_data_source_basic_info(
        self,
        request: dataphin_public_20230630_models.UpdateDataSourceBasicInfoRequest,
    ) -> dataphin_public_20230630_models.UpdateDataSourceBasicInfoResponse:
        """
        @summary 编辑数据源基本信息
        
        @param request: UpdateDataSourceBasicInfoRequest
        @return: UpdateDataSourceBasicInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_data_source_basic_info_with_options(request, runtime)

    async def update_data_source_basic_info_async(
        self,
        request: dataphin_public_20230630_models.UpdateDataSourceBasicInfoRequest,
    ) -> dataphin_public_20230630_models.UpdateDataSourceBasicInfoResponse:
        """
        @summary 编辑数据源基本信息
        
        @param request: UpdateDataSourceBasicInfoRequest
        @return: UpdateDataSourceBasicInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_data_source_basic_info_with_options_async(request, runtime)

    def update_data_source_config_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.UpdateDataSourceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.UpdateDataSourceConfigResponse:
        """
        @summary 编辑数据源连接配置项
        
        @param tmp_req: UpdateDataSourceConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDataSourceConfigResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.UpdateDataSourceConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.update_command):
            request.update_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDataSourceConfig',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.UpdateDataSourceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_data_source_config_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.UpdateDataSourceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.UpdateDataSourceConfigResponse:
        """
        @summary 编辑数据源连接配置项
        
        @param tmp_req: UpdateDataSourceConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDataSourceConfigResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.UpdateDataSourceConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.update_command):
            request.update_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDataSourceConfig',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.UpdateDataSourceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_data_source_config(
        self,
        request: dataphin_public_20230630_models.UpdateDataSourceConfigRequest,
    ) -> dataphin_public_20230630_models.UpdateDataSourceConfigResponse:
        """
        @summary 编辑数据源连接配置项
        
        @param request: UpdateDataSourceConfigRequest
        @return: UpdateDataSourceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_data_source_config_with_options(request, runtime)

    async def update_data_source_config_async(
        self,
        request: dataphin_public_20230630_models.UpdateDataSourceConfigRequest,
    ) -> dataphin_public_20230630_models.UpdateDataSourceConfigResponse:
        """
        @summary 编辑数据源连接配置项
        
        @param request: UpdateDataSourceConfigRequest
        @return: UpdateDataSourceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_data_source_config_with_options_async(request, runtime)

    def update_file_directory_with_options(
        self,
        request: dataphin_public_20230630_models.UpdateFileDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.UpdateFileDirectoryResponse:
        """
        @summary 修改菜单树文件所在目录
        
        @param request: UpdateFileDirectoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFileDirectoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory):
            query['Directory'] = request.directory
        if not UtilClient.is_unset(request.file_id):
            query['FileId'] = request.file_id
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFileDirectory',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.UpdateFileDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_file_directory_with_options_async(
        self,
        request: dataphin_public_20230630_models.UpdateFileDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.UpdateFileDirectoryResponse:
        """
        @summary 修改菜单树文件所在目录
        
        @param request: UpdateFileDirectoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFileDirectoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory):
            query['Directory'] = request.directory
        if not UtilClient.is_unset(request.file_id):
            query['FileId'] = request.file_id
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFileDirectory',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.UpdateFileDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_file_directory(
        self,
        request: dataphin_public_20230630_models.UpdateFileDirectoryRequest,
    ) -> dataphin_public_20230630_models.UpdateFileDirectoryResponse:
        """
        @summary 修改菜单树文件所在目录
        
        @param request: UpdateFileDirectoryRequest
        @return: UpdateFileDirectoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_file_directory_with_options(request, runtime)

    async def update_file_directory_async(
        self,
        request: dataphin_public_20230630_models.UpdateFileDirectoryRequest,
    ) -> dataphin_public_20230630_models.UpdateFileDirectoryResponse:
        """
        @summary 修改菜单树文件所在目录
        
        @param request: UpdateFileDirectoryRequest
        @return: UpdateFileDirectoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_file_directory_with_options_async(request, runtime)

    def update_file_name_with_options(
        self,
        request: dataphin_public_20230630_models.UpdateFileNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.UpdateFileNameResponse:
        """
        @summary 修改菜单树文件名称
        
        @param request: UpdateFileNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFileNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_id):
            query['FileId'] = request.file_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFileName',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.UpdateFileNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_file_name_with_options_async(
        self,
        request: dataphin_public_20230630_models.UpdateFileNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.UpdateFileNameResponse:
        """
        @summary 修改菜单树文件名称
        
        @param request: UpdateFileNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFileNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_id):
            query['FileId'] = request.file_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFileName',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.UpdateFileNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_file_name(
        self,
        request: dataphin_public_20230630_models.UpdateFileNameRequest,
    ) -> dataphin_public_20230630_models.UpdateFileNameResponse:
        """
        @summary 修改菜单树文件名称
        
        @param request: UpdateFileNameRequest
        @return: UpdateFileNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_file_name_with_options(request, runtime)

    async def update_file_name_async(
        self,
        request: dataphin_public_20230630_models.UpdateFileNameRequest,
    ) -> dataphin_public_20230630_models.UpdateFileNameResponse:
        """
        @summary 修改菜单树文件名称
        
        @param request: UpdateFileNameRequest
        @return: UpdateFileNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_file_name_with_options_async(request, runtime)

    def update_tenant_member_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.UpdateTenantMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.UpdateTenantMemberResponse:
        """
        @summary 编辑租户成员
        
        @param tmp_req: UpdateTenantMemberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTenantMemberResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.UpdateTenantMemberShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.update_command):
            request.update_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTenantMember',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.UpdateTenantMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_tenant_member_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.UpdateTenantMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.UpdateTenantMemberResponse:
        """
        @summary 编辑租户成员
        
        @param tmp_req: UpdateTenantMemberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTenantMemberResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.UpdateTenantMemberShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.update_command):
            request.update_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTenantMember',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.UpdateTenantMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_tenant_member(
        self,
        request: dataphin_public_20230630_models.UpdateTenantMemberRequest,
    ) -> dataphin_public_20230630_models.UpdateTenantMemberResponse:
        """
        @summary 编辑租户成员
        
        @param request: UpdateTenantMemberRequest
        @return: UpdateTenantMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_tenant_member_with_options(request, runtime)

    async def update_tenant_member_async(
        self,
        request: dataphin_public_20230630_models.UpdateTenantMemberRequest,
    ) -> dataphin_public_20230630_models.UpdateTenantMemberResponse:
        """
        @summary 编辑租户成员
        
        @param request: UpdateTenantMemberRequest
        @return: UpdateTenantMemberResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_tenant_member_with_options_async(request, runtime)

    def update_user_group_with_options(
        self,
        tmp_req: dataphin_public_20230630_models.UpdateUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.UpdateUserGroupResponse:
        """
        @summary 编辑用户组.
        
        @param tmp_req: UpdateUserGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUserGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.UpdateUserGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.update_command):
            request.update_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateUserGroup',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.UpdateUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_group_with_options_async(
        self,
        tmp_req: dataphin_public_20230630_models.UpdateUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.UpdateUserGroupResponse:
        """
        @summary 编辑用户组.
        
        @param tmp_req: UpdateUserGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUserGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dataphin_public_20230630_models.UpdateUserGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.update_command):
            request.update_command_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.update_command, 'UpdateCommand', 'json')
        query = {}
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        body = {}
        if not UtilClient.is_unset(request.update_command_shrink):
            body['UpdateCommand'] = request.update_command_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateUserGroup',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.UpdateUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user_group(
        self,
        request: dataphin_public_20230630_models.UpdateUserGroupRequest,
    ) -> dataphin_public_20230630_models.UpdateUserGroupResponse:
        """
        @summary 编辑用户组.
        
        @param request: UpdateUserGroupRequest
        @return: UpdateUserGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_user_group_with_options(request, runtime)

    async def update_user_group_async(
        self,
        request: dataphin_public_20230630_models.UpdateUserGroupRequest,
    ) -> dataphin_public_20230630_models.UpdateUserGroupResponse:
        """
        @summary 编辑用户组.
        
        @param request: UpdateUserGroupRequest
        @return: UpdateUserGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_user_group_with_options_async(request, runtime)

    def update_user_group_switch_with_options(
        self,
        request: dataphin_public_20230630_models.UpdateUserGroupSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.UpdateUserGroupSwitchResponse:
        """
        @summary 编辑用户组启用开关.
        
        @param request: UpdateUserGroupSwitchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUserGroupSwitchResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.active):
            query['Active'] = request.active
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUserGroupSwitch',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.UpdateUserGroupSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_group_switch_with_options_async(
        self,
        request: dataphin_public_20230630_models.UpdateUserGroupSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataphin_public_20230630_models.UpdateUserGroupSwitchResponse:
        """
        @summary 编辑用户组启用开关.
        
        @param request: UpdateUserGroupSwitchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUserGroupSwitchResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.active):
            query['Active'] = request.active
        if not UtilClient.is_unset(request.op_tenant_id):
            query['OpTenantId'] = request.op_tenant_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUserGroupSwitch',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dataphin_public_20230630_models.UpdateUserGroupSwitchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user_group_switch(
        self,
        request: dataphin_public_20230630_models.UpdateUserGroupSwitchRequest,
    ) -> dataphin_public_20230630_models.UpdateUserGroupSwitchResponse:
        """
        @summary 编辑用户组启用开关.
        
        @param request: UpdateUserGroupSwitchRequest
        @return: UpdateUserGroupSwitchResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_user_group_switch_with_options(request, runtime)

    async def update_user_group_switch_async(
        self,
        request: dataphin_public_20230630_models.UpdateUserGroupSwitchRequest,
    ) -> dataphin_public_20230630_models.UpdateUserGroupSwitchResponse:
        """
        @summary 编辑用户组启用开关.
        
        @param request: UpdateUserGroupSwitchRequest
        @return: UpdateUserGroupSwitchResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_user_group_switch_with_options_async(request, runtime)
