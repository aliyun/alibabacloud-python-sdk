# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_eiam20211201 import models as main_models
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
        self._endpoint = self.get_endpoint('eiam', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_application_account_to_user_with_options(
        self,
        request: main_models.AddApplicationAccountToUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddApplicationAccountToUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.application_username):
            query['ApplicationUsername'] = request.application_username
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddApplicationAccountToUser',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddApplicationAccountToUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_application_account_to_user_with_options_async(
        self,
        request: main_models.AddApplicationAccountToUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddApplicationAccountToUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.application_username):
            query['ApplicationUsername'] = request.application_username
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddApplicationAccountToUser',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddApplicationAccountToUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_application_account_to_user(
        self,
        request: main_models.AddApplicationAccountToUserRequest,
    ) -> main_models.AddApplicationAccountToUserResponse:
        runtime = RuntimeOptions()
        return self.add_application_account_to_user_with_options(request, runtime)

    async def add_application_account_to_user_async(
        self,
        request: main_models.AddApplicationAccountToUserRequest,
    ) -> main_models.AddApplicationAccountToUserResponse:
        runtime = RuntimeOptions()
        return await self.add_application_account_to_user_with_options_async(request, runtime)

    def add_custom_privacy_policies_to_brand_with_options(
        self,
        request: main_models.AddCustomPrivacyPoliciesToBrandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddCustomPrivacyPoliciesToBrandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.brand_id):
            query['BrandId'] = request.brand_id
        if not DaraCore.is_null(request.custom_privacy_policy_ids):
            query['CustomPrivacyPolicyIds'] = request.custom_privacy_policy_ids
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddCustomPrivacyPoliciesToBrand',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddCustomPrivacyPoliciesToBrandResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_custom_privacy_policies_to_brand_with_options_async(
        self,
        request: main_models.AddCustomPrivacyPoliciesToBrandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddCustomPrivacyPoliciesToBrandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.brand_id):
            query['BrandId'] = request.brand_id
        if not DaraCore.is_null(request.custom_privacy_policy_ids):
            query['CustomPrivacyPolicyIds'] = request.custom_privacy_policy_ids
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddCustomPrivacyPoliciesToBrand',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddCustomPrivacyPoliciesToBrandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_custom_privacy_policies_to_brand(
        self,
        request: main_models.AddCustomPrivacyPoliciesToBrandRequest,
    ) -> main_models.AddCustomPrivacyPoliciesToBrandResponse:
        runtime = RuntimeOptions()
        return self.add_custom_privacy_policies_to_brand_with_options(request, runtime)

    async def add_custom_privacy_policies_to_brand_async(
        self,
        request: main_models.AddCustomPrivacyPoliciesToBrandRequest,
    ) -> main_models.AddCustomPrivacyPoliciesToBrandResponse:
        runtime = RuntimeOptions()
        return await self.add_custom_privacy_policies_to_brand_with_options_async(request, runtime)

    def add_user_to_organizational_units_with_options(
        self,
        request: main_models.AddUserToOrganizationalUnitsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddUserToOrganizationalUnitsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.organizational_unit_ids):
            query['OrganizationalUnitIds'] = request.organizational_unit_ids
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddUserToOrganizationalUnits',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddUserToOrganizationalUnitsResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_user_to_organizational_units_with_options_async(
        self,
        request: main_models.AddUserToOrganizationalUnitsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddUserToOrganizationalUnitsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.organizational_unit_ids):
            query['OrganizationalUnitIds'] = request.organizational_unit_ids
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddUserToOrganizationalUnits',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddUserToOrganizationalUnitsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_user_to_organizational_units(
        self,
        request: main_models.AddUserToOrganizationalUnitsRequest,
    ) -> main_models.AddUserToOrganizationalUnitsResponse:
        runtime = RuntimeOptions()
        return self.add_user_to_organizational_units_with_options(request, runtime)

    async def add_user_to_organizational_units_async(
        self,
        request: main_models.AddUserToOrganizationalUnitsRequest,
    ) -> main_models.AddUserToOrganizationalUnitsResponse:
        runtime = RuntimeOptions()
        return await self.add_user_to_organizational_units_with_options_async(request, runtime)

    def add_users_to_group_with_options(
        self,
        request: main_models.AddUsersToGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddUsersToGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddUsersToGroup',
            version = '2021-12-01',
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
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddUsersToGroup',
            version = '2021-12-01',
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

    def authorize_application_to_groups_with_options(
        self,
        request: main_models.AuthorizeApplicationToGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AuthorizeApplicationToGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.application_role_id):
            query['ApplicationRoleId'] = request.application_role_id
        if not DaraCore.is_null(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AuthorizeApplicationToGroups',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuthorizeApplicationToGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def authorize_application_to_groups_with_options_async(
        self,
        request: main_models.AuthorizeApplicationToGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AuthorizeApplicationToGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.application_role_id):
            query['ApplicationRoleId'] = request.application_role_id
        if not DaraCore.is_null(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AuthorizeApplicationToGroups',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuthorizeApplicationToGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def authorize_application_to_groups(
        self,
        request: main_models.AuthorizeApplicationToGroupsRequest,
    ) -> main_models.AuthorizeApplicationToGroupsResponse:
        runtime = RuntimeOptions()
        return self.authorize_application_to_groups_with_options(request, runtime)

    async def authorize_application_to_groups_async(
        self,
        request: main_models.AuthorizeApplicationToGroupsRequest,
    ) -> main_models.AuthorizeApplicationToGroupsResponse:
        runtime = RuntimeOptions()
        return await self.authorize_application_to_groups_with_options_async(request, runtime)

    def authorize_application_to_organizational_units_with_options(
        self,
        request: main_models.AuthorizeApplicationToOrganizationalUnitsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AuthorizeApplicationToOrganizationalUnitsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.application_role_id):
            query['ApplicationRoleId'] = request.application_role_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.organizational_unit_ids):
            query['OrganizationalUnitIds'] = request.organizational_unit_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AuthorizeApplicationToOrganizationalUnits',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuthorizeApplicationToOrganizationalUnitsResponse(),
            self.call_api(params, req, runtime)
        )

    async def authorize_application_to_organizational_units_with_options_async(
        self,
        request: main_models.AuthorizeApplicationToOrganizationalUnitsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AuthorizeApplicationToOrganizationalUnitsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.application_role_id):
            query['ApplicationRoleId'] = request.application_role_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.organizational_unit_ids):
            query['OrganizationalUnitIds'] = request.organizational_unit_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AuthorizeApplicationToOrganizationalUnits',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuthorizeApplicationToOrganizationalUnitsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def authorize_application_to_organizational_units(
        self,
        request: main_models.AuthorizeApplicationToOrganizationalUnitsRequest,
    ) -> main_models.AuthorizeApplicationToOrganizationalUnitsResponse:
        runtime = RuntimeOptions()
        return self.authorize_application_to_organizational_units_with_options(request, runtime)

    async def authorize_application_to_organizational_units_async(
        self,
        request: main_models.AuthorizeApplicationToOrganizationalUnitsRequest,
    ) -> main_models.AuthorizeApplicationToOrganizationalUnitsResponse:
        runtime = RuntimeOptions()
        return await self.authorize_application_to_organizational_units_with_options_async(request, runtime)

    def authorize_application_to_users_with_options(
        self,
        request: main_models.AuthorizeApplicationToUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AuthorizeApplicationToUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.application_role_id):
            query['ApplicationRoleId'] = request.application_role_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AuthorizeApplicationToUsers',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuthorizeApplicationToUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def authorize_application_to_users_with_options_async(
        self,
        request: main_models.AuthorizeApplicationToUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AuthorizeApplicationToUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.application_role_id):
            query['ApplicationRoleId'] = request.application_role_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AuthorizeApplicationToUsers',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuthorizeApplicationToUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def authorize_application_to_users(
        self,
        request: main_models.AuthorizeApplicationToUsersRequest,
    ) -> main_models.AuthorizeApplicationToUsersResponse:
        runtime = RuntimeOptions()
        return self.authorize_application_to_users_with_options(request, runtime)

    async def authorize_application_to_users_async(
        self,
        request: main_models.AuthorizeApplicationToUsersRequest,
    ) -> main_models.AuthorizeApplicationToUsersResponse:
        runtime = RuntimeOptions()
        return await self.authorize_application_to_users_with_options_async(request, runtime)

    def authorize_resource_server_scopes_to_client_with_options(
        self,
        request: main_models.AuthorizeResourceServerScopesToClientRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AuthorizeResourceServerScopesToClientResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_application_id):
            query['ClientApplicationId'] = request.client_application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.resource_server_application_id):
            query['ResourceServerApplicationId'] = request.resource_server_application_id
        if not DaraCore.is_null(request.resource_server_scope_ids):
            query['ResourceServerScopeIds'] = request.resource_server_scope_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AuthorizeResourceServerScopesToClient',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuthorizeResourceServerScopesToClientResponse(),
            self.call_api(params, req, runtime)
        )

    async def authorize_resource_server_scopes_to_client_with_options_async(
        self,
        request: main_models.AuthorizeResourceServerScopesToClientRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AuthorizeResourceServerScopesToClientResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_application_id):
            query['ClientApplicationId'] = request.client_application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.resource_server_application_id):
            query['ResourceServerApplicationId'] = request.resource_server_application_id
        if not DaraCore.is_null(request.resource_server_scope_ids):
            query['ResourceServerScopeIds'] = request.resource_server_scope_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AuthorizeResourceServerScopesToClient',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuthorizeResourceServerScopesToClientResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def authorize_resource_server_scopes_to_client(
        self,
        request: main_models.AuthorizeResourceServerScopesToClientRequest,
    ) -> main_models.AuthorizeResourceServerScopesToClientResponse:
        runtime = RuntimeOptions()
        return self.authorize_resource_server_scopes_to_client_with_options(request, runtime)

    async def authorize_resource_server_scopes_to_client_async(
        self,
        request: main_models.AuthorizeResourceServerScopesToClientRequest,
    ) -> main_models.AuthorizeResourceServerScopesToClientResponse:
        runtime = RuntimeOptions()
        return await self.authorize_resource_server_scopes_to_client_with_options_async(request, runtime)

    def authorize_resource_server_scopes_to_group_with_options(
        self,
        request: main_models.AuthorizeResourceServerScopesToGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AuthorizeResourceServerScopesToGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.resource_server_scope_ids):
            query['ResourceServerScopeIds'] = request.resource_server_scope_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AuthorizeResourceServerScopesToGroup',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuthorizeResourceServerScopesToGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def authorize_resource_server_scopes_to_group_with_options_async(
        self,
        request: main_models.AuthorizeResourceServerScopesToGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AuthorizeResourceServerScopesToGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.resource_server_scope_ids):
            query['ResourceServerScopeIds'] = request.resource_server_scope_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AuthorizeResourceServerScopesToGroup',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuthorizeResourceServerScopesToGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def authorize_resource_server_scopes_to_group(
        self,
        request: main_models.AuthorizeResourceServerScopesToGroupRequest,
    ) -> main_models.AuthorizeResourceServerScopesToGroupResponse:
        runtime = RuntimeOptions()
        return self.authorize_resource_server_scopes_to_group_with_options(request, runtime)

    async def authorize_resource_server_scopes_to_group_async(
        self,
        request: main_models.AuthorizeResourceServerScopesToGroupRequest,
    ) -> main_models.AuthorizeResourceServerScopesToGroupResponse:
        runtime = RuntimeOptions()
        return await self.authorize_resource_server_scopes_to_group_with_options_async(request, runtime)

    def authorize_resource_server_scopes_to_organizational_unit_with_options(
        self,
        request: main_models.AuthorizeResourceServerScopesToOrganizationalUnitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AuthorizeResourceServerScopesToOrganizationalUnitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.organizational_unit_id):
            query['OrganizationalUnitId'] = request.organizational_unit_id
        if not DaraCore.is_null(request.resource_server_scope_ids):
            query['ResourceServerScopeIds'] = request.resource_server_scope_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AuthorizeResourceServerScopesToOrganizationalUnit',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuthorizeResourceServerScopesToOrganizationalUnitResponse(),
            self.call_api(params, req, runtime)
        )

    async def authorize_resource_server_scopes_to_organizational_unit_with_options_async(
        self,
        request: main_models.AuthorizeResourceServerScopesToOrganizationalUnitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AuthorizeResourceServerScopesToOrganizationalUnitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.organizational_unit_id):
            query['OrganizationalUnitId'] = request.organizational_unit_id
        if not DaraCore.is_null(request.resource_server_scope_ids):
            query['ResourceServerScopeIds'] = request.resource_server_scope_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AuthorizeResourceServerScopesToOrganizationalUnit',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuthorizeResourceServerScopesToOrganizationalUnitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def authorize_resource_server_scopes_to_organizational_unit(
        self,
        request: main_models.AuthorizeResourceServerScopesToOrganizationalUnitRequest,
    ) -> main_models.AuthorizeResourceServerScopesToOrganizationalUnitResponse:
        runtime = RuntimeOptions()
        return self.authorize_resource_server_scopes_to_organizational_unit_with_options(request, runtime)

    async def authorize_resource_server_scopes_to_organizational_unit_async(
        self,
        request: main_models.AuthorizeResourceServerScopesToOrganizationalUnitRequest,
    ) -> main_models.AuthorizeResourceServerScopesToOrganizationalUnitResponse:
        runtime = RuntimeOptions()
        return await self.authorize_resource_server_scopes_to_organizational_unit_with_options_async(request, runtime)

    def authorize_resource_server_scopes_to_user_with_options(
        self,
        request: main_models.AuthorizeResourceServerScopesToUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AuthorizeResourceServerScopesToUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.resource_server_scope_ids):
            query['ResourceServerScopeIds'] = request.resource_server_scope_ids
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AuthorizeResourceServerScopesToUser',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuthorizeResourceServerScopesToUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def authorize_resource_server_scopes_to_user_with_options_async(
        self,
        request: main_models.AuthorizeResourceServerScopesToUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AuthorizeResourceServerScopesToUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.resource_server_scope_ids):
            query['ResourceServerScopeIds'] = request.resource_server_scope_ids
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AuthorizeResourceServerScopesToUser',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuthorizeResourceServerScopesToUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def authorize_resource_server_scopes_to_user(
        self,
        request: main_models.AuthorizeResourceServerScopesToUserRequest,
    ) -> main_models.AuthorizeResourceServerScopesToUserResponse:
        runtime = RuntimeOptions()
        return self.authorize_resource_server_scopes_to_user_with_options(request, runtime)

    async def authorize_resource_server_scopes_to_user_async(
        self,
        request: main_models.AuthorizeResourceServerScopesToUserRequest,
    ) -> main_models.AuthorizeResourceServerScopesToUserResponse:
        runtime = RuntimeOptions()
        return await self.authorize_resource_server_scopes_to_user_with_options_async(request, runtime)

    def authorize_resource_server_to_client_with_options(
        self,
        request: main_models.AuthorizeResourceServerToClientRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AuthorizeResourceServerToClientResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_application_id):
            query['ClientApplicationId'] = request.client_application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.resource_server_application_id):
            query['ResourceServerApplicationId'] = request.resource_server_application_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AuthorizeResourceServerToClient',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuthorizeResourceServerToClientResponse(),
            self.call_api(params, req, runtime)
        )

    async def authorize_resource_server_to_client_with_options_async(
        self,
        request: main_models.AuthorizeResourceServerToClientRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AuthorizeResourceServerToClientResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_application_id):
            query['ClientApplicationId'] = request.client_application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.resource_server_application_id):
            query['ResourceServerApplicationId'] = request.resource_server_application_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AuthorizeResourceServerToClient',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuthorizeResourceServerToClientResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def authorize_resource_server_to_client(
        self,
        request: main_models.AuthorizeResourceServerToClientRequest,
    ) -> main_models.AuthorizeResourceServerToClientResponse:
        runtime = RuntimeOptions()
        return self.authorize_resource_server_to_client_with_options(request, runtime)

    async def authorize_resource_server_to_client_async(
        self,
        request: main_models.AuthorizeResourceServerToClientRequest,
    ) -> main_models.AuthorizeResourceServerToClientResponse:
        runtime = RuntimeOptions()
        return await self.authorize_resource_server_to_client_with_options_async(request, runtime)

    def bind_user_authn_source_mapping_with_options(
        self,
        request: main_models.BindUserAuthnSourceMappingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindUserAuthnSourceMappingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identity_provider_id):
            query['IdentityProviderId'] = request.identity_provider_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_external_id):
            query['UserExternalId'] = request.user_external_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindUserAuthnSourceMapping',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindUserAuthnSourceMappingResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_user_authn_source_mapping_with_options_async(
        self,
        request: main_models.BindUserAuthnSourceMappingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindUserAuthnSourceMappingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identity_provider_id):
            query['IdentityProviderId'] = request.identity_provider_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_external_id):
            query['UserExternalId'] = request.user_external_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindUserAuthnSourceMapping',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindUserAuthnSourceMappingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_user_authn_source_mapping(
        self,
        request: main_models.BindUserAuthnSourceMappingRequest,
    ) -> main_models.BindUserAuthnSourceMappingResponse:
        runtime = RuntimeOptions()
        return self.bind_user_authn_source_mapping_with_options(request, runtime)

    async def bind_user_authn_source_mapping_async(
        self,
        request: main_models.BindUserAuthnSourceMappingRequest,
    ) -> main_models.BindUserAuthnSourceMappingResponse:
        runtime = RuntimeOptions()
        return await self.bind_user_authn_source_mapping_with_options_async(request, runtime)

    def create_application_with_options(
        self,
        request: main_models.CreateApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_name):
            query['ApplicationName'] = request.application_name
        if not DaraCore.is_null(request.application_source_type):
            query['ApplicationSourceType'] = request.application_source_type
        if not DaraCore.is_null(request.application_template_id):
            query['ApplicationTemplateId'] = request.application_template_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.logo_url):
            query['LogoUrl'] = request.logo_url
        if not DaraCore.is_null(request.sso_type):
            query['SsoType'] = request.sso_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateApplication',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_application_with_options_async(
        self,
        request: main_models.CreateApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_name):
            query['ApplicationName'] = request.application_name
        if not DaraCore.is_null(request.application_source_type):
            query['ApplicationSourceType'] = request.application_source_type
        if not DaraCore.is_null(request.application_template_id):
            query['ApplicationTemplateId'] = request.application_template_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.logo_url):
            query['LogoUrl'] = request.logo_url
        if not DaraCore.is_null(request.sso_type):
            query['SsoType'] = request.sso_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateApplication',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_application(
        self,
        request: main_models.CreateApplicationRequest,
    ) -> main_models.CreateApplicationResponse:
        runtime = RuntimeOptions()
        return self.create_application_with_options(request, runtime)

    async def create_application_async(
        self,
        request: main_models.CreateApplicationRequest,
    ) -> main_models.CreateApplicationResponse:
        runtime = RuntimeOptions()
        return await self.create_application_with_options_async(request, runtime)

    def create_application_client_secret_with_options(
        self,
        request: main_models.CreateApplicationClientSecretRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateApplicationClientSecretResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.expiration_time):
            query['ExpirationTime'] = request.expiration_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateApplicationClientSecret',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApplicationClientSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_application_client_secret_with_options_async(
        self,
        request: main_models.CreateApplicationClientSecretRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateApplicationClientSecretResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.expiration_time):
            query['ExpirationTime'] = request.expiration_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateApplicationClientSecret',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApplicationClientSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_application_client_secret(
        self,
        request: main_models.CreateApplicationClientSecretRequest,
    ) -> main_models.CreateApplicationClientSecretResponse:
        runtime = RuntimeOptions()
        return self.create_application_client_secret_with_options(request, runtime)

    async def create_application_client_secret_async(
        self,
        request: main_models.CreateApplicationClientSecretRequest,
    ) -> main_models.CreateApplicationClientSecretResponse:
        runtime = RuntimeOptions()
        return await self.create_application_client_secret_with_options_async(request, runtime)

    def create_application_federated_credential_with_options(
        self,
        request: main_models.CreateApplicationFederatedCredentialRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateApplicationFederatedCredentialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_federated_credential_name):
            query['ApplicationFederatedCredentialName'] = request.application_federated_credential_name
        if not DaraCore.is_null(request.application_federated_credential_type):
            query['ApplicationFederatedCredentialType'] = request.application_federated_credential_type
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.attribute_mappings):
            query['AttributeMappings'] = request.attribute_mappings
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.federated_credential_provider_id):
            query['FederatedCredentialProviderId'] = request.federated_credential_provider_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.verification_condition):
            query['VerificationCondition'] = request.verification_condition
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateApplicationFederatedCredential',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApplicationFederatedCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_application_federated_credential_with_options_async(
        self,
        request: main_models.CreateApplicationFederatedCredentialRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateApplicationFederatedCredentialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_federated_credential_name):
            query['ApplicationFederatedCredentialName'] = request.application_federated_credential_name
        if not DaraCore.is_null(request.application_federated_credential_type):
            query['ApplicationFederatedCredentialType'] = request.application_federated_credential_type
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.attribute_mappings):
            query['AttributeMappings'] = request.attribute_mappings
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.federated_credential_provider_id):
            query['FederatedCredentialProviderId'] = request.federated_credential_provider_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.verification_condition):
            query['VerificationCondition'] = request.verification_condition
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateApplicationFederatedCredential',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApplicationFederatedCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_application_federated_credential(
        self,
        request: main_models.CreateApplicationFederatedCredentialRequest,
    ) -> main_models.CreateApplicationFederatedCredentialResponse:
        runtime = RuntimeOptions()
        return self.create_application_federated_credential_with_options(request, runtime)

    async def create_application_federated_credential_async(
        self,
        request: main_models.CreateApplicationFederatedCredentialRequest,
    ) -> main_models.CreateApplicationFederatedCredentialResponse:
        runtime = RuntimeOptions()
        return await self.create_application_federated_credential_with_options_async(request, runtime)

    def create_application_role_with_options(
        self,
        request: main_models.CreateApplicationRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateApplicationRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.application_role_name):
            query['ApplicationRoleName'] = request.application_role_name
        if not DaraCore.is_null(request.application_role_value):
            query['ApplicationRoleValue'] = request.application_role_value
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateApplicationRole',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApplicationRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_application_role_with_options_async(
        self,
        request: main_models.CreateApplicationRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateApplicationRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.application_role_name):
            query['ApplicationRoleName'] = request.application_role_name
        if not DaraCore.is_null(request.application_role_value):
            query['ApplicationRoleValue'] = request.application_role_value
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateApplicationRole',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApplicationRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_application_role(
        self,
        request: main_models.CreateApplicationRoleRequest,
    ) -> main_models.CreateApplicationRoleResponse:
        runtime = RuntimeOptions()
        return self.create_application_role_with_options(request, runtime)

    async def create_application_role_async(
        self,
        request: main_models.CreateApplicationRoleRequest,
    ) -> main_models.CreateApplicationRoleResponse:
        runtime = RuntimeOptions()
        return await self.create_application_role_with_options_async(request, runtime)

    def create_application_token_with_options(
        self,
        request: main_models.CreateApplicationTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateApplicationTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.application_token_type):
            query['ApplicationTokenType'] = request.application_token_type
        if not DaraCore.is_null(request.expiration_time):
            query['ExpirationTime'] = request.expiration_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateApplicationToken',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApplicationTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_application_token_with_options_async(
        self,
        request: main_models.CreateApplicationTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateApplicationTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.application_token_type):
            query['ApplicationTokenType'] = request.application_token_type
        if not DaraCore.is_null(request.expiration_time):
            query['ExpirationTime'] = request.expiration_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateApplicationToken',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApplicationTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_application_token(
        self,
        request: main_models.CreateApplicationTokenRequest,
    ) -> main_models.CreateApplicationTokenResponse:
        runtime = RuntimeOptions()
        return self.create_application_token_with_options(request, runtime)

    async def create_application_token_async(
        self,
        request: main_models.CreateApplicationTokenRequest,
    ) -> main_models.CreateApplicationTokenResponse:
        runtime = RuntimeOptions()
        return await self.create_application_token_with_options_async(request, runtime)

    def create_brand_with_options(
        self,
        request: main_models.CreateBrandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBrandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.brand_name):
            query['BrandName'] = request.brand_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateBrand',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBrandResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_brand_with_options_async(
        self,
        request: main_models.CreateBrandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBrandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.brand_name):
            query['BrandName'] = request.brand_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateBrand',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBrandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_brand(
        self,
        request: main_models.CreateBrandRequest,
    ) -> main_models.CreateBrandResponse:
        runtime = RuntimeOptions()
        return self.create_brand_with_options(request, runtime)

    async def create_brand_async(
        self,
        request: main_models.CreateBrandRequest,
    ) -> main_models.CreateBrandResponse:
        runtime = RuntimeOptions()
        return await self.create_brand_with_options_async(request, runtime)

    def create_client_public_key_with_options(
        self,
        request: main_models.CreateClientPublicKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateClientPublicKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.algorithm_type):
            query['AlgorithmType'] = request.algorithm_type
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.public_key):
            query['PublicKey'] = request.public_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateClientPublicKey',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateClientPublicKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_client_public_key_with_options_async(
        self,
        request: main_models.CreateClientPublicKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateClientPublicKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.algorithm_type):
            query['AlgorithmType'] = request.algorithm_type
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.public_key):
            query['PublicKey'] = request.public_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateClientPublicKey',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateClientPublicKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_client_public_key(
        self,
        request: main_models.CreateClientPublicKeyRequest,
    ) -> main_models.CreateClientPublicKeyResponse:
        runtime = RuntimeOptions()
        return self.create_client_public_key_with_options(request, runtime)

    async def create_client_public_key_async(
        self,
        request: main_models.CreateClientPublicKeyRequest,
    ) -> main_models.CreateClientPublicKeyResponse:
        runtime = RuntimeOptions()
        return await self.create_client_public_key_with_options_async(request, runtime)

    def create_cloud_account_with_options(
        self,
        request: main_models.CreateCloudAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCloudAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cloud_account_external_id):
            query['CloudAccountExternalId'] = request.cloud_account_external_id
        if not DaraCore.is_null(request.cloud_account_name):
            query['CloudAccountName'] = request.cloud_account_name
        if not DaraCore.is_null(request.cloud_account_provider_name):
            query['CloudAccountProviderName'] = request.cloud_account_provider_name
        if not DaraCore.is_null(request.cloud_account_vendor_type):
            query['CloudAccountVendorType'] = request.cloud_account_vendor_type
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCloudAccount',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCloudAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cloud_account_with_options_async(
        self,
        request: main_models.CreateCloudAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCloudAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cloud_account_external_id):
            query['CloudAccountExternalId'] = request.cloud_account_external_id
        if not DaraCore.is_null(request.cloud_account_name):
            query['CloudAccountName'] = request.cloud_account_name
        if not DaraCore.is_null(request.cloud_account_provider_name):
            query['CloudAccountProviderName'] = request.cloud_account_provider_name
        if not DaraCore.is_null(request.cloud_account_vendor_type):
            query['CloudAccountVendorType'] = request.cloud_account_vendor_type
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCloudAccount',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCloudAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cloud_account(
        self,
        request: main_models.CreateCloudAccountRequest,
    ) -> main_models.CreateCloudAccountResponse:
        runtime = RuntimeOptions()
        return self.create_cloud_account_with_options(request, runtime)

    async def create_cloud_account_async(
        self,
        request: main_models.CreateCloudAccountRequest,
    ) -> main_models.CreateCloudAccountResponse:
        runtime = RuntimeOptions()
        return await self.create_cloud_account_with_options_async(request, runtime)

    def create_cloud_account_role_with_options(
        self,
        request: main_models.CreateCloudAccountRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCloudAccountRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cloud_account_id):
            query['CloudAccountId'] = request.cloud_account_id
        if not DaraCore.is_null(request.cloud_account_role_name):
            query['CloudAccountRoleName'] = request.cloud_account_role_name
        if not DaraCore.is_null(request.cloud_account_role_type):
            query['CloudAccountRoleType'] = request.cloud_account_role_type
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCloudAccountRole',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCloudAccountRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cloud_account_role_with_options_async(
        self,
        request: main_models.CreateCloudAccountRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCloudAccountRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cloud_account_id):
            query['CloudAccountId'] = request.cloud_account_id
        if not DaraCore.is_null(request.cloud_account_role_name):
            query['CloudAccountRoleName'] = request.cloud_account_role_name
        if not DaraCore.is_null(request.cloud_account_role_type):
            query['CloudAccountRoleType'] = request.cloud_account_role_type
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCloudAccountRole',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCloudAccountRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cloud_account_role(
        self,
        request: main_models.CreateCloudAccountRoleRequest,
    ) -> main_models.CreateCloudAccountRoleResponse:
        runtime = RuntimeOptions()
        return self.create_cloud_account_role_with_options(request, runtime)

    async def create_cloud_account_role_async(
        self,
        request: main_models.CreateCloudAccountRoleRequest,
    ) -> main_models.CreateCloudAccountRoleResponse:
        runtime = RuntimeOptions()
        return await self.create_cloud_account_role_with_options_async(request, runtime)

    def create_conditional_access_policy_with_options(
        self,
        request: main_models.CreateConditionalAccessPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateConditionalAccessPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.conditional_access_policy_name):
            query['ConditionalAccessPolicyName'] = request.conditional_access_policy_name
        if not DaraCore.is_null(request.conditional_access_policy_type):
            query['ConditionalAccessPolicyType'] = request.conditional_access_policy_type
        if not DaraCore.is_null(request.conditions_config):
            query['ConditionsConfig'] = request.conditions_config
        if not DaraCore.is_null(request.decision_config):
            query['DecisionConfig'] = request.decision_config
        if not DaraCore.is_null(request.decision_type):
            query['DecisionType'] = request.decision_type
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.evaluate_at):
            query['EvaluateAt'] = request.evaluate_at
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateConditionalAccessPolicy',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateConditionalAccessPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_conditional_access_policy_with_options_async(
        self,
        request: main_models.CreateConditionalAccessPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateConditionalAccessPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.conditional_access_policy_name):
            query['ConditionalAccessPolicyName'] = request.conditional_access_policy_name
        if not DaraCore.is_null(request.conditional_access_policy_type):
            query['ConditionalAccessPolicyType'] = request.conditional_access_policy_type
        if not DaraCore.is_null(request.conditions_config):
            query['ConditionsConfig'] = request.conditions_config
        if not DaraCore.is_null(request.decision_config):
            query['DecisionConfig'] = request.decision_config
        if not DaraCore.is_null(request.decision_type):
            query['DecisionType'] = request.decision_type
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.evaluate_at):
            query['EvaluateAt'] = request.evaluate_at
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateConditionalAccessPolicy',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateConditionalAccessPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_conditional_access_policy(
        self,
        request: main_models.CreateConditionalAccessPolicyRequest,
    ) -> main_models.CreateConditionalAccessPolicyResponse:
        runtime = RuntimeOptions()
        return self.create_conditional_access_policy_with_options(request, runtime)

    async def create_conditional_access_policy_async(
        self,
        request: main_models.CreateConditionalAccessPolicyRequest,
    ) -> main_models.CreateConditionalAccessPolicyResponse:
        runtime = RuntimeOptions()
        return await self.create_conditional_access_policy_with_options_async(request, runtime)

    def create_custom_privacy_policy_with_options(
        self,
        request: main_models.CreateCustomPrivacyPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCustomPrivacyPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.custom_privacy_policy_contents):
            query['CustomPrivacyPolicyContents'] = request.custom_privacy_policy_contents
        if not DaraCore.is_null(request.custom_privacy_policy_name):
            query['CustomPrivacyPolicyName'] = request.custom_privacy_policy_name
        if not DaraCore.is_null(request.default_language_code):
            query['DefaultLanguageCode'] = request.default_language_code
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.user_consent_type):
            query['UserConsentType'] = request.user_consent_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCustomPrivacyPolicy',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCustomPrivacyPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_custom_privacy_policy_with_options_async(
        self,
        request: main_models.CreateCustomPrivacyPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCustomPrivacyPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.custom_privacy_policy_contents):
            query['CustomPrivacyPolicyContents'] = request.custom_privacy_policy_contents
        if not DaraCore.is_null(request.custom_privacy_policy_name):
            query['CustomPrivacyPolicyName'] = request.custom_privacy_policy_name
        if not DaraCore.is_null(request.default_language_code):
            query['DefaultLanguageCode'] = request.default_language_code
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.user_consent_type):
            query['UserConsentType'] = request.user_consent_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCustomPrivacyPolicy',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCustomPrivacyPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_custom_privacy_policy(
        self,
        request: main_models.CreateCustomPrivacyPolicyRequest,
    ) -> main_models.CreateCustomPrivacyPolicyResponse:
        runtime = RuntimeOptions()
        return self.create_custom_privacy_policy_with_options(request, runtime)

    async def create_custom_privacy_policy_async(
        self,
        request: main_models.CreateCustomPrivacyPolicyRequest,
    ) -> main_models.CreateCustomPrivacyPolicyResponse:
        runtime = RuntimeOptions()
        return await self.create_custom_privacy_policy_with_options_async(request, runtime)

    def create_domain_with_options(
        self,
        request: main_models.CreateDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.filing):
            query['Filing'] = request.filing
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDomain',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_domain_with_options_async(
        self,
        request: main_models.CreateDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.filing):
            query['Filing'] = request.filing
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDomain',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_domain(
        self,
        request: main_models.CreateDomainRequest,
    ) -> main_models.CreateDomainResponse:
        runtime = RuntimeOptions()
        return self.create_domain_with_options(request, runtime)

    async def create_domain_async(
        self,
        request: main_models.CreateDomainRequest,
    ) -> main_models.CreateDomainResponse:
        runtime = RuntimeOptions()
        return await self.create_domain_with_options_async(request, runtime)

    def create_domain_proxy_token_with_options(
        self,
        request: main_models.CreateDomainProxyTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDomainProxyTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_id):
            query['DomainId'] = request.domain_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDomainProxyToken',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDomainProxyTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_domain_proxy_token_with_options_async(
        self,
        request: main_models.CreateDomainProxyTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDomainProxyTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_id):
            query['DomainId'] = request.domain_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDomainProxyToken',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDomainProxyTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_domain_proxy_token(
        self,
        request: main_models.CreateDomainProxyTokenRequest,
    ) -> main_models.CreateDomainProxyTokenResponse:
        runtime = RuntimeOptions()
        return self.create_domain_proxy_token_with_options(request, runtime)

    async def create_domain_proxy_token_async(
        self,
        request: main_models.CreateDomainProxyTokenRequest,
    ) -> main_models.CreateDomainProxyTokenResponse:
        runtime = RuntimeOptions()
        return await self.create_domain_proxy_token_with_options_async(request, runtime)

    def create_federated_credential_provider_with_options(
        self,
        request: main_models.CreateFederatedCredentialProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFederatedCredentialProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.federated_credential_provider_name):
            query['FederatedCredentialProviderName'] = request.federated_credential_provider_name
        if not DaraCore.is_null(request.federated_credential_provider_type):
            query['FederatedCredentialProviderType'] = request.federated_credential_provider_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.network_access_endpoint_id):
            query['NetworkAccessEndpointId'] = request.network_access_endpoint_id
        if not DaraCore.is_null(request.oidc_provider_config):
            query['OidcProviderConfig'] = request.oidc_provider_config
        if not DaraCore.is_null(request.pkcs_7provider_config):
            query['Pkcs7ProviderConfig'] = request.pkcs_7provider_config
        if not DaraCore.is_null(request.private_ca_provider_config):
            query['PrivateCaProviderConfig'] = request.private_ca_provider_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateFederatedCredentialProvider',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFederatedCredentialProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_federated_credential_provider_with_options_async(
        self,
        request: main_models.CreateFederatedCredentialProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFederatedCredentialProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.federated_credential_provider_name):
            query['FederatedCredentialProviderName'] = request.federated_credential_provider_name
        if not DaraCore.is_null(request.federated_credential_provider_type):
            query['FederatedCredentialProviderType'] = request.federated_credential_provider_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.network_access_endpoint_id):
            query['NetworkAccessEndpointId'] = request.network_access_endpoint_id
        if not DaraCore.is_null(request.oidc_provider_config):
            query['OidcProviderConfig'] = request.oidc_provider_config
        if not DaraCore.is_null(request.pkcs_7provider_config):
            query['Pkcs7ProviderConfig'] = request.pkcs_7provider_config
        if not DaraCore.is_null(request.private_ca_provider_config):
            query['PrivateCaProviderConfig'] = request.private_ca_provider_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateFederatedCredentialProvider',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFederatedCredentialProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_federated_credential_provider(
        self,
        request: main_models.CreateFederatedCredentialProviderRequest,
    ) -> main_models.CreateFederatedCredentialProviderResponse:
        runtime = RuntimeOptions()
        return self.create_federated_credential_provider_with_options(request, runtime)

    async def create_federated_credential_provider_async(
        self,
        request: main_models.CreateFederatedCredentialProviderRequest,
    ) -> main_models.CreateFederatedCredentialProviderResponse:
        runtime = RuntimeOptions()
        return await self.create_federated_credential_provider_with_options_async(request, runtime)

    def create_group_with_options(
        self,
        request: main_models.CreateGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.group_external_id):
            query['GroupExternalId'] = request.group_external_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateGroup',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_group_with_options_async(
        self,
        request: main_models.CreateGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.group_external_id):
            query['GroupExternalId'] = request.group_external_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateGroup',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_group(
        self,
        request: main_models.CreateGroupRequest,
    ) -> main_models.CreateGroupResponse:
        runtime = RuntimeOptions()
        return self.create_group_with_options(request, runtime)

    async def create_group_async(
        self,
        request: main_models.CreateGroupRequest,
    ) -> main_models.CreateGroupResponse:
        runtime = RuntimeOptions()
        return await self.create_group_with_options_async(request, runtime)

    def create_identity_provider_with_options(
        self,
        request: main_models.CreateIdentityProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateIdentityProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.authn_config):
            query['AuthnConfig'] = request.authn_config
        if not DaraCore.is_null(request.auto_create_user_config):
            query['AutoCreateUserConfig'] = request.auto_create_user_config
        if not DaraCore.is_null(request.auto_update_user_config):
            query['AutoUpdateUserConfig'] = request.auto_update_user_config
        if not DaraCore.is_null(request.binding_config):
            query['BindingConfig'] = request.binding_config
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dingtalk_app_config):
            query['DingtalkAppConfig'] = request.dingtalk_app_config
        if not DaraCore.is_null(request.identity_provider_name):
            query['IdentityProviderName'] = request.identity_provider_name
        if not DaraCore.is_null(request.identity_provider_type):
            query['IdentityProviderType'] = request.identity_provider_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lark_config):
            query['LarkConfig'] = request.lark_config
        if not DaraCore.is_null(request.ldap_config):
            query['LdapConfig'] = request.ldap_config
        if not DaraCore.is_null(request.logo_url):
            query['LogoUrl'] = request.logo_url
        if not DaraCore.is_null(request.network_access_endpoint_id):
            query['NetworkAccessEndpointId'] = request.network_access_endpoint_id
        if not DaraCore.is_null(request.oidc_config):
            query['OidcConfig'] = request.oidc_config
        if not DaraCore.is_null(request.ud_pull_config):
            query['UdPullConfig'] = request.ud_pull_config
        if not DaraCore.is_null(request.ud_push_config):
            query['UdPushConfig'] = request.ud_push_config
        if not DaraCore.is_null(request.we_com_config):
            query['WeComConfig'] = request.we_com_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateIdentityProvider',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIdentityProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_identity_provider_with_options_async(
        self,
        request: main_models.CreateIdentityProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateIdentityProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.authn_config):
            query['AuthnConfig'] = request.authn_config
        if not DaraCore.is_null(request.auto_create_user_config):
            query['AutoCreateUserConfig'] = request.auto_create_user_config
        if not DaraCore.is_null(request.auto_update_user_config):
            query['AutoUpdateUserConfig'] = request.auto_update_user_config
        if not DaraCore.is_null(request.binding_config):
            query['BindingConfig'] = request.binding_config
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dingtalk_app_config):
            query['DingtalkAppConfig'] = request.dingtalk_app_config
        if not DaraCore.is_null(request.identity_provider_name):
            query['IdentityProviderName'] = request.identity_provider_name
        if not DaraCore.is_null(request.identity_provider_type):
            query['IdentityProviderType'] = request.identity_provider_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lark_config):
            query['LarkConfig'] = request.lark_config
        if not DaraCore.is_null(request.ldap_config):
            query['LdapConfig'] = request.ldap_config
        if not DaraCore.is_null(request.logo_url):
            query['LogoUrl'] = request.logo_url
        if not DaraCore.is_null(request.network_access_endpoint_id):
            query['NetworkAccessEndpointId'] = request.network_access_endpoint_id
        if not DaraCore.is_null(request.oidc_config):
            query['OidcConfig'] = request.oidc_config
        if not DaraCore.is_null(request.ud_pull_config):
            query['UdPullConfig'] = request.ud_pull_config
        if not DaraCore.is_null(request.ud_push_config):
            query['UdPushConfig'] = request.ud_push_config
        if not DaraCore.is_null(request.we_com_config):
            query['WeComConfig'] = request.we_com_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateIdentityProvider',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIdentityProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_identity_provider(
        self,
        request: main_models.CreateIdentityProviderRequest,
    ) -> main_models.CreateIdentityProviderResponse:
        runtime = RuntimeOptions()
        return self.create_identity_provider_with_options(request, runtime)

    async def create_identity_provider_async(
        self,
        request: main_models.CreateIdentityProviderRequest,
    ) -> main_models.CreateIdentityProviderResponse:
        runtime = RuntimeOptions()
        return await self.create_identity_provider_with_options_async(request, runtime)

    def create_identity_provider_status_check_job_with_options(
        self,
        request: main_models.CreateIdentityProviderStatusCheckJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateIdentityProviderStatusCheckJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identity_provider_id):
            query['IdentityProviderId'] = request.identity_provider_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateIdentityProviderStatusCheckJob',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIdentityProviderStatusCheckJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_identity_provider_status_check_job_with_options_async(
        self,
        request: main_models.CreateIdentityProviderStatusCheckJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateIdentityProviderStatusCheckJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identity_provider_id):
            query['IdentityProviderId'] = request.identity_provider_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateIdentityProviderStatusCheckJob',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIdentityProviderStatusCheckJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_identity_provider_status_check_job(
        self,
        request: main_models.CreateIdentityProviderStatusCheckJobRequest,
    ) -> main_models.CreateIdentityProviderStatusCheckJobResponse:
        runtime = RuntimeOptions()
        return self.create_identity_provider_status_check_job_with_options(request, runtime)

    async def create_identity_provider_status_check_job_async(
        self,
        request: main_models.CreateIdentityProviderStatusCheckJobRequest,
    ) -> main_models.CreateIdentityProviderStatusCheckJobResponse:
        runtime = RuntimeOptions()
        return await self.create_identity_provider_status_check_job_with_options_async(request, runtime)

    def create_instance_with_options(
        self,
        request: main_models.CreateInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstance',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        request: main_models.CreateInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstance',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance(
        self,
        request: main_models.CreateInstanceRequest,
    ) -> main_models.CreateInstanceResponse:
        runtime = RuntimeOptions()
        return self.create_instance_with_options(request, runtime)

    async def create_instance_async(
        self,
        request: main_models.CreateInstanceRequest,
    ) -> main_models.CreateInstanceResponse:
        runtime = RuntimeOptions()
        return await self.create_instance_with_options_async(request, runtime)

    def create_network_access_endpoint_with_options(
        self,
        request: main_models.CreateNetworkAccessEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNetworkAccessEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.network_access_endpoint_name):
            query['NetworkAccessEndpointName'] = request.network_access_endpoint_name
        if not DaraCore.is_null(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.vpc_region_id):
            query['VpcRegionId'] = request.vpc_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateNetworkAccessEndpoint',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNetworkAccessEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_network_access_endpoint_with_options_async(
        self,
        request: main_models.CreateNetworkAccessEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNetworkAccessEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.network_access_endpoint_name):
            query['NetworkAccessEndpointName'] = request.network_access_endpoint_name
        if not DaraCore.is_null(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.vpc_region_id):
            query['VpcRegionId'] = request.vpc_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateNetworkAccessEndpoint',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNetworkAccessEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_network_access_endpoint(
        self,
        request: main_models.CreateNetworkAccessEndpointRequest,
    ) -> main_models.CreateNetworkAccessEndpointResponse:
        runtime = RuntimeOptions()
        return self.create_network_access_endpoint_with_options(request, runtime)

    async def create_network_access_endpoint_async(
        self,
        request: main_models.CreateNetworkAccessEndpointRequest,
    ) -> main_models.CreateNetworkAccessEndpointResponse:
        runtime = RuntimeOptions()
        return await self.create_network_access_endpoint_with_options_async(request, runtime)

    def create_network_zone_with_options(
        self,
        request: main_models.CreateNetworkZoneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNetworkZoneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ipv_4cidrs):
            query['Ipv4Cidrs'] = request.ipv_4cidrs
        if not DaraCore.is_null(request.ipv_6cidrs):
            query['Ipv6Cidrs'] = request.ipv_6cidrs
        if not DaraCore.is_null(request.network_zone_name):
            query['NetworkZoneName'] = request.network_zone_name
        if not DaraCore.is_null(request.network_zone_type):
            query['NetworkZoneType'] = request.network_zone_type
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateNetworkZone',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNetworkZoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_network_zone_with_options_async(
        self,
        request: main_models.CreateNetworkZoneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNetworkZoneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ipv_4cidrs):
            query['Ipv4Cidrs'] = request.ipv_4cidrs
        if not DaraCore.is_null(request.ipv_6cidrs):
            query['Ipv6Cidrs'] = request.ipv_6cidrs
        if not DaraCore.is_null(request.network_zone_name):
            query['NetworkZoneName'] = request.network_zone_name
        if not DaraCore.is_null(request.network_zone_type):
            query['NetworkZoneType'] = request.network_zone_type
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateNetworkZone',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNetworkZoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_network_zone(
        self,
        request: main_models.CreateNetworkZoneRequest,
    ) -> main_models.CreateNetworkZoneResponse:
        runtime = RuntimeOptions()
        return self.create_network_zone_with_options(request, runtime)

    async def create_network_zone_async(
        self,
        request: main_models.CreateNetworkZoneRequest,
    ) -> main_models.CreateNetworkZoneResponse:
        runtime = RuntimeOptions()
        return await self.create_network_zone_with_options_async(request, runtime)

    def create_organizational_unit_with_options(
        self,
        request: main_models.CreateOrganizationalUnitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOrganizationalUnitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.organizational_unit_external_id):
            query['OrganizationalUnitExternalId'] = request.organizational_unit_external_id
        if not DaraCore.is_null(request.organizational_unit_name):
            query['OrganizationalUnitName'] = request.organizational_unit_name
        if not DaraCore.is_null(request.parent_id):
            query['ParentId'] = request.parent_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateOrganizationalUnit',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOrganizationalUnitResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_organizational_unit_with_options_async(
        self,
        request: main_models.CreateOrganizationalUnitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOrganizationalUnitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.organizational_unit_external_id):
            query['OrganizationalUnitExternalId'] = request.organizational_unit_external_id
        if not DaraCore.is_null(request.organizational_unit_name):
            query['OrganizationalUnitName'] = request.organizational_unit_name
        if not DaraCore.is_null(request.parent_id):
            query['ParentId'] = request.parent_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateOrganizationalUnit',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOrganizationalUnitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_organizational_unit(
        self,
        request: main_models.CreateOrganizationalUnitRequest,
    ) -> main_models.CreateOrganizationalUnitResponse:
        runtime = RuntimeOptions()
        return self.create_organizational_unit_with_options(request, runtime)

    async def create_organizational_unit_async(
        self,
        request: main_models.CreateOrganizationalUnitRequest,
    ) -> main_models.CreateOrganizationalUnitResponse:
        runtime = RuntimeOptions()
        return await self.create_organizational_unit_with_options_async(request, runtime)

    def create_resource_server_scope_with_options(
        self,
        request: main_models.CreateResourceServerScopeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateResourceServerScopeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.authorization_type):
            query['AuthorizationType'] = request.authorization_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.resource_server_scope_name):
            query['ResourceServerScopeName'] = request.resource_server_scope_name
        if not DaraCore.is_null(request.resource_server_scope_type):
            query['ResourceServerScopeType'] = request.resource_server_scope_type
        if not DaraCore.is_null(request.resource_server_scope_value):
            query['ResourceServerScopeValue'] = request.resource_server_scope_value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateResourceServerScope',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateResourceServerScopeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_resource_server_scope_with_options_async(
        self,
        request: main_models.CreateResourceServerScopeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateResourceServerScopeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.authorization_type):
            query['AuthorizationType'] = request.authorization_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.resource_server_scope_name):
            query['ResourceServerScopeName'] = request.resource_server_scope_name
        if not DaraCore.is_null(request.resource_server_scope_type):
            query['ResourceServerScopeType'] = request.resource_server_scope_type
        if not DaraCore.is_null(request.resource_server_scope_value):
            query['ResourceServerScopeValue'] = request.resource_server_scope_value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateResourceServerScope',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateResourceServerScopeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_resource_server_scope(
        self,
        request: main_models.CreateResourceServerScopeRequest,
    ) -> main_models.CreateResourceServerScopeResponse:
        runtime = RuntimeOptions()
        return self.create_resource_server_scope_with_options(request, runtime)

    async def create_resource_server_scope_async(
        self,
        request: main_models.CreateResourceServerScopeRequest,
    ) -> main_models.CreateResourceServerScopeResponse:
        runtime = RuntimeOptions()
        return await self.create_resource_server_scope_with_options_async(request, runtime)

    def create_user_with_options(
        self,
        request: main_models.CreateUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.custom_fields):
            query['CustomFields'] = request.custom_fields
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.display_name):
            query['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.email_verified):
            query['EmailVerified'] = request.email_verified
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.organizational_unit_ids):
            query['OrganizationalUnitIds'] = request.organizational_unit_ids
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.password_initialization_config):
            query['PasswordInitializationConfig'] = request.password_initialization_config
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.phone_number_verified):
            query['PhoneNumberVerified'] = request.phone_number_verified
        if not DaraCore.is_null(request.phone_region):
            query['PhoneRegion'] = request.phone_region
        if not DaraCore.is_null(request.primary_organizational_unit_id):
            query['PrimaryOrganizationalUnitId'] = request.primary_organizational_unit_id
        if not DaraCore.is_null(request.user_external_id):
            query['UserExternalId'] = request.user_external_id
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateUser',
            version = '2021-12-01',
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
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.custom_fields):
            query['CustomFields'] = request.custom_fields
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.display_name):
            query['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.email_verified):
            query['EmailVerified'] = request.email_verified
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.organizational_unit_ids):
            query['OrganizationalUnitIds'] = request.organizational_unit_ids
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.password_initialization_config):
            query['PasswordInitializationConfig'] = request.password_initialization_config
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.phone_number_verified):
            query['PhoneNumberVerified'] = request.phone_number_verified
        if not DaraCore.is_null(request.phone_region):
            query['PhoneRegion'] = request.phone_region
        if not DaraCore.is_null(request.primary_organizational_unit_id):
            query['PrimaryOrganizationalUnitId'] = request.primary_organizational_unit_id
        if not DaraCore.is_null(request.user_external_id):
            query['UserExternalId'] = request.user_external_id
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateUser',
            version = '2021-12-01',
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

    def delete_application_with_options(
        self,
        request: main_models.DeleteApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApplication',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_application_with_options_async(
        self,
        request: main_models.DeleteApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApplication',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_application(
        self,
        request: main_models.DeleteApplicationRequest,
    ) -> main_models.DeleteApplicationResponse:
        runtime = RuntimeOptions()
        return self.delete_application_with_options(request, runtime)

    async def delete_application_async(
        self,
        request: main_models.DeleteApplicationRequest,
    ) -> main_models.DeleteApplicationResponse:
        runtime = RuntimeOptions()
        return await self.delete_application_with_options_async(request, runtime)

    def delete_application_client_secret_with_options(
        self,
        request: main_models.DeleteApplicationClientSecretRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApplicationClientSecretResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.secret_id):
            query['SecretId'] = request.secret_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApplicationClientSecret',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApplicationClientSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_application_client_secret_with_options_async(
        self,
        request: main_models.DeleteApplicationClientSecretRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApplicationClientSecretResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.secret_id):
            query['SecretId'] = request.secret_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApplicationClientSecret',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApplicationClientSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_application_client_secret(
        self,
        request: main_models.DeleteApplicationClientSecretRequest,
    ) -> main_models.DeleteApplicationClientSecretResponse:
        runtime = RuntimeOptions()
        return self.delete_application_client_secret_with_options(request, runtime)

    async def delete_application_client_secret_async(
        self,
        request: main_models.DeleteApplicationClientSecretRequest,
    ) -> main_models.DeleteApplicationClientSecretResponse:
        runtime = RuntimeOptions()
        return await self.delete_application_client_secret_with_options_async(request, runtime)

    def delete_application_federated_credential_with_options(
        self,
        request: main_models.DeleteApplicationFederatedCredentialRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApplicationFederatedCredentialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_federated_credential_id):
            query['ApplicationFederatedCredentialId'] = request.application_federated_credential_id
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApplicationFederatedCredential',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApplicationFederatedCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_application_federated_credential_with_options_async(
        self,
        request: main_models.DeleteApplicationFederatedCredentialRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApplicationFederatedCredentialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_federated_credential_id):
            query['ApplicationFederatedCredentialId'] = request.application_federated_credential_id
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApplicationFederatedCredential',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApplicationFederatedCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_application_federated_credential(
        self,
        request: main_models.DeleteApplicationFederatedCredentialRequest,
    ) -> main_models.DeleteApplicationFederatedCredentialResponse:
        runtime = RuntimeOptions()
        return self.delete_application_federated_credential_with_options(request, runtime)

    async def delete_application_federated_credential_async(
        self,
        request: main_models.DeleteApplicationFederatedCredentialRequest,
    ) -> main_models.DeleteApplicationFederatedCredentialResponse:
        runtime = RuntimeOptions()
        return await self.delete_application_federated_credential_with_options_async(request, runtime)

    def delete_application_role_with_options(
        self,
        request: main_models.DeleteApplicationRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApplicationRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.application_role_id):
            query['ApplicationRoleId'] = request.application_role_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApplicationRole',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApplicationRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_application_role_with_options_async(
        self,
        request: main_models.DeleteApplicationRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApplicationRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.application_role_id):
            query['ApplicationRoleId'] = request.application_role_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApplicationRole',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApplicationRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_application_role(
        self,
        request: main_models.DeleteApplicationRoleRequest,
    ) -> main_models.DeleteApplicationRoleResponse:
        runtime = RuntimeOptions()
        return self.delete_application_role_with_options(request, runtime)

    async def delete_application_role_async(
        self,
        request: main_models.DeleteApplicationRoleRequest,
    ) -> main_models.DeleteApplicationRoleResponse:
        runtime = RuntimeOptions()
        return await self.delete_application_role_with_options_async(request, runtime)

    def delete_application_token_with_options(
        self,
        request: main_models.DeleteApplicationTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApplicationTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.application_token_id):
            query['ApplicationTokenId'] = request.application_token_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApplicationToken',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApplicationTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_application_token_with_options_async(
        self,
        request: main_models.DeleteApplicationTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApplicationTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.application_token_id):
            query['ApplicationTokenId'] = request.application_token_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApplicationToken',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApplicationTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_application_token(
        self,
        request: main_models.DeleteApplicationTokenRequest,
    ) -> main_models.DeleteApplicationTokenResponse:
        runtime = RuntimeOptions()
        return self.delete_application_token_with_options(request, runtime)

    async def delete_application_token_async(
        self,
        request: main_models.DeleteApplicationTokenRequest,
    ) -> main_models.DeleteApplicationTokenResponse:
        runtime = RuntimeOptions()
        return await self.delete_application_token_with_options_async(request, runtime)

    def delete_brand_with_options(
        self,
        request: main_models.DeleteBrandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBrandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.brand_id):
            query['BrandId'] = request.brand_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBrand',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBrandResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_brand_with_options_async(
        self,
        request: main_models.DeleteBrandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBrandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.brand_id):
            query['BrandId'] = request.brand_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBrand',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBrandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_brand(
        self,
        request: main_models.DeleteBrandRequest,
    ) -> main_models.DeleteBrandResponse:
        runtime = RuntimeOptions()
        return self.delete_brand_with_options(request, runtime)

    async def delete_brand_async(
        self,
        request: main_models.DeleteBrandRequest,
    ) -> main_models.DeleteBrandResponse:
        runtime = RuntimeOptions()
        return await self.delete_brand_with_options_async(request, runtime)

    def delete_client_public_key_with_options(
        self,
        request: main_models.DeleteClientPublicKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteClientPublicKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.client_public_key_id):
            query['ClientPublicKeyId'] = request.client_public_key_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteClientPublicKey',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteClientPublicKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_client_public_key_with_options_async(
        self,
        request: main_models.DeleteClientPublicKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteClientPublicKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.client_public_key_id):
            query['ClientPublicKeyId'] = request.client_public_key_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteClientPublicKey',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteClientPublicKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_client_public_key(
        self,
        request: main_models.DeleteClientPublicKeyRequest,
    ) -> main_models.DeleteClientPublicKeyResponse:
        runtime = RuntimeOptions()
        return self.delete_client_public_key_with_options(request, runtime)

    async def delete_client_public_key_async(
        self,
        request: main_models.DeleteClientPublicKeyRequest,
    ) -> main_models.DeleteClientPublicKeyResponse:
        runtime = RuntimeOptions()
        return await self.delete_client_public_key_with_options_async(request, runtime)

    def delete_cloud_account_with_options(
        self,
        request: main_models.DeleteCloudAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCloudAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cloud_account_id):
            query['CloudAccountId'] = request.cloud_account_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCloudAccount',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCloudAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cloud_account_with_options_async(
        self,
        request: main_models.DeleteCloudAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCloudAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cloud_account_id):
            query['CloudAccountId'] = request.cloud_account_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCloudAccount',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCloudAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cloud_account(
        self,
        request: main_models.DeleteCloudAccountRequest,
    ) -> main_models.DeleteCloudAccountResponse:
        runtime = RuntimeOptions()
        return self.delete_cloud_account_with_options(request, runtime)

    async def delete_cloud_account_async(
        self,
        request: main_models.DeleteCloudAccountRequest,
    ) -> main_models.DeleteCloudAccountResponse:
        runtime = RuntimeOptions()
        return await self.delete_cloud_account_with_options_async(request, runtime)

    def delete_cloud_account_role_with_options(
        self,
        request: main_models.DeleteCloudAccountRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCloudAccountRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cloud_account_id):
            query['CloudAccountId'] = request.cloud_account_id
        if not DaraCore.is_null(request.cloud_account_role_id):
            query['CloudAccountRoleId'] = request.cloud_account_role_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCloudAccountRole',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCloudAccountRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cloud_account_role_with_options_async(
        self,
        request: main_models.DeleteCloudAccountRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCloudAccountRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cloud_account_id):
            query['CloudAccountId'] = request.cloud_account_id
        if not DaraCore.is_null(request.cloud_account_role_id):
            query['CloudAccountRoleId'] = request.cloud_account_role_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCloudAccountRole',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCloudAccountRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cloud_account_role(
        self,
        request: main_models.DeleteCloudAccountRoleRequest,
    ) -> main_models.DeleteCloudAccountRoleResponse:
        runtime = RuntimeOptions()
        return self.delete_cloud_account_role_with_options(request, runtime)

    async def delete_cloud_account_role_async(
        self,
        request: main_models.DeleteCloudAccountRoleRequest,
    ) -> main_models.DeleteCloudAccountRoleResponse:
        runtime = RuntimeOptions()
        return await self.delete_cloud_account_role_with_options_async(request, runtime)

    def delete_conditional_access_policy_with_options(
        self,
        request: main_models.DeleteConditionalAccessPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteConditionalAccessPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.conditional_access_policy_id):
            query['ConditionalAccessPolicyId'] = request.conditional_access_policy_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteConditionalAccessPolicy',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteConditionalAccessPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_conditional_access_policy_with_options_async(
        self,
        request: main_models.DeleteConditionalAccessPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteConditionalAccessPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.conditional_access_policy_id):
            query['ConditionalAccessPolicyId'] = request.conditional_access_policy_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteConditionalAccessPolicy',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteConditionalAccessPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_conditional_access_policy(
        self,
        request: main_models.DeleteConditionalAccessPolicyRequest,
    ) -> main_models.DeleteConditionalAccessPolicyResponse:
        runtime = RuntimeOptions()
        return self.delete_conditional_access_policy_with_options(request, runtime)

    async def delete_conditional_access_policy_async(
        self,
        request: main_models.DeleteConditionalAccessPolicyRequest,
    ) -> main_models.DeleteConditionalAccessPolicyResponse:
        runtime = RuntimeOptions()
        return await self.delete_conditional_access_policy_with_options_async(request, runtime)

    def delete_custom_privacy_policy_with_options(
        self,
        request: main_models.DeleteCustomPrivacyPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomPrivacyPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.custom_privacy_policy_id):
            query['CustomPrivacyPolicyId'] = request.custom_privacy_policy_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomPrivacyPolicy',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomPrivacyPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_custom_privacy_policy_with_options_async(
        self,
        request: main_models.DeleteCustomPrivacyPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomPrivacyPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.custom_privacy_policy_id):
            query['CustomPrivacyPolicyId'] = request.custom_privacy_policy_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomPrivacyPolicy',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomPrivacyPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_custom_privacy_policy(
        self,
        request: main_models.DeleteCustomPrivacyPolicyRequest,
    ) -> main_models.DeleteCustomPrivacyPolicyResponse:
        runtime = RuntimeOptions()
        return self.delete_custom_privacy_policy_with_options(request, runtime)

    async def delete_custom_privacy_policy_async(
        self,
        request: main_models.DeleteCustomPrivacyPolicyRequest,
    ) -> main_models.DeleteCustomPrivacyPolicyResponse:
        runtime = RuntimeOptions()
        return await self.delete_custom_privacy_policy_with_options_async(request, runtime)

    def delete_domain_with_options(
        self,
        request: main_models.DeleteDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_id):
            query['DomainId'] = request.domain_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDomain',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_domain_with_options_async(
        self,
        request: main_models.DeleteDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_id):
            query['DomainId'] = request.domain_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDomain',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_domain(
        self,
        request: main_models.DeleteDomainRequest,
    ) -> main_models.DeleteDomainResponse:
        runtime = RuntimeOptions()
        return self.delete_domain_with_options(request, runtime)

    async def delete_domain_async(
        self,
        request: main_models.DeleteDomainRequest,
    ) -> main_models.DeleteDomainResponse:
        runtime = RuntimeOptions()
        return await self.delete_domain_with_options_async(request, runtime)

    def delete_domain_proxy_token_with_options(
        self,
        request: main_models.DeleteDomainProxyTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDomainProxyTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_id):
            query['DomainId'] = request.domain_id
        if not DaraCore.is_null(request.domain_proxy_token_id):
            query['DomainProxyTokenId'] = request.domain_proxy_token_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDomainProxyToken',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDomainProxyTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_domain_proxy_token_with_options_async(
        self,
        request: main_models.DeleteDomainProxyTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDomainProxyTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_id):
            query['DomainId'] = request.domain_id
        if not DaraCore.is_null(request.domain_proxy_token_id):
            query['DomainProxyTokenId'] = request.domain_proxy_token_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDomainProxyToken',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDomainProxyTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_domain_proxy_token(
        self,
        request: main_models.DeleteDomainProxyTokenRequest,
    ) -> main_models.DeleteDomainProxyTokenResponse:
        runtime = RuntimeOptions()
        return self.delete_domain_proxy_token_with_options(request, runtime)

    async def delete_domain_proxy_token_async(
        self,
        request: main_models.DeleteDomainProxyTokenRequest,
    ) -> main_models.DeleteDomainProxyTokenResponse:
        runtime = RuntimeOptions()
        return await self.delete_domain_proxy_token_with_options_async(request, runtime)

    def delete_federated_credential_provider_with_options(
        self,
        request: main_models.DeleteFederatedCredentialProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFederatedCredentialProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.federated_credential_provider_id):
            query['FederatedCredentialProviderId'] = request.federated_credential_provider_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFederatedCredentialProvider',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFederatedCredentialProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_federated_credential_provider_with_options_async(
        self,
        request: main_models.DeleteFederatedCredentialProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFederatedCredentialProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.federated_credential_provider_id):
            query['FederatedCredentialProviderId'] = request.federated_credential_provider_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFederatedCredentialProvider',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFederatedCredentialProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_federated_credential_provider(
        self,
        request: main_models.DeleteFederatedCredentialProviderRequest,
    ) -> main_models.DeleteFederatedCredentialProviderResponse:
        runtime = RuntimeOptions()
        return self.delete_federated_credential_provider_with_options(request, runtime)

    async def delete_federated_credential_provider_async(
        self,
        request: main_models.DeleteFederatedCredentialProviderRequest,
    ) -> main_models.DeleteFederatedCredentialProviderResponse:
        runtime = RuntimeOptions()
        return await self.delete_federated_credential_provider_with_options_async(request, runtime)

    def delete_group_with_options(
        self,
        request: main_models.DeleteGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGroup',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_group_with_options_async(
        self,
        request: main_models.DeleteGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGroup',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_group(
        self,
        request: main_models.DeleteGroupRequest,
    ) -> main_models.DeleteGroupResponse:
        runtime = RuntimeOptions()
        return self.delete_group_with_options(request, runtime)

    async def delete_group_async(
        self,
        request: main_models.DeleteGroupRequest,
    ) -> main_models.DeleteGroupResponse:
        runtime = RuntimeOptions()
        return await self.delete_group_with_options_async(request, runtime)

    def delete_identity_provider_with_options(
        self,
        request: main_models.DeleteIdentityProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIdentityProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identity_provider_id):
            query['IdentityProviderId'] = request.identity_provider_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteIdentityProvider',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIdentityProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_identity_provider_with_options_async(
        self,
        request: main_models.DeleteIdentityProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIdentityProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identity_provider_id):
            query['IdentityProviderId'] = request.identity_provider_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteIdentityProvider',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIdentityProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_identity_provider(
        self,
        request: main_models.DeleteIdentityProviderRequest,
    ) -> main_models.DeleteIdentityProviderResponse:
        runtime = RuntimeOptions()
        return self.delete_identity_provider_with_options(request, runtime)

    async def delete_identity_provider_async(
        self,
        request: main_models.DeleteIdentityProviderRequest,
    ) -> main_models.DeleteIdentityProviderResponse:
        runtime = RuntimeOptions()
        return await self.delete_identity_provider_with_options_async(request, runtime)

    def delete_instance_with_options(
        self,
        request: main_models.DeleteInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstance',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_with_options_async(
        self,
        request: main_models.DeleteInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstance',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance(
        self,
        request: main_models.DeleteInstanceRequest,
    ) -> main_models.DeleteInstanceResponse:
        runtime = RuntimeOptions()
        return self.delete_instance_with_options(request, runtime)

    async def delete_instance_async(
        self,
        request: main_models.DeleteInstanceRequest,
    ) -> main_models.DeleteInstanceResponse:
        runtime = RuntimeOptions()
        return await self.delete_instance_with_options_async(request, runtime)

    def delete_network_access_endpoint_with_options(
        self,
        request: main_models.DeleteNetworkAccessEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNetworkAccessEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.network_access_endpoint_id):
            query['NetworkAccessEndpointId'] = request.network_access_endpoint_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNetworkAccessEndpoint',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNetworkAccessEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_network_access_endpoint_with_options_async(
        self,
        request: main_models.DeleteNetworkAccessEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNetworkAccessEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.network_access_endpoint_id):
            query['NetworkAccessEndpointId'] = request.network_access_endpoint_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNetworkAccessEndpoint',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNetworkAccessEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_network_access_endpoint(
        self,
        request: main_models.DeleteNetworkAccessEndpointRequest,
    ) -> main_models.DeleteNetworkAccessEndpointResponse:
        runtime = RuntimeOptions()
        return self.delete_network_access_endpoint_with_options(request, runtime)

    async def delete_network_access_endpoint_async(
        self,
        request: main_models.DeleteNetworkAccessEndpointRequest,
    ) -> main_models.DeleteNetworkAccessEndpointResponse:
        runtime = RuntimeOptions()
        return await self.delete_network_access_endpoint_with_options_async(request, runtime)

    def delete_network_zone_with_options(
        self,
        request: main_models.DeleteNetworkZoneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNetworkZoneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.network_zone_id):
            query['NetworkZoneId'] = request.network_zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNetworkZone',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNetworkZoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_network_zone_with_options_async(
        self,
        request: main_models.DeleteNetworkZoneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNetworkZoneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.network_zone_id):
            query['NetworkZoneId'] = request.network_zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNetworkZone',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNetworkZoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_network_zone(
        self,
        request: main_models.DeleteNetworkZoneRequest,
    ) -> main_models.DeleteNetworkZoneResponse:
        runtime = RuntimeOptions()
        return self.delete_network_zone_with_options(request, runtime)

    async def delete_network_zone_async(
        self,
        request: main_models.DeleteNetworkZoneRequest,
    ) -> main_models.DeleteNetworkZoneResponse:
        runtime = RuntimeOptions()
        return await self.delete_network_zone_with_options_async(request, runtime)

    def delete_organizational_unit_with_options(
        self,
        request: main_models.DeleteOrganizationalUnitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteOrganizationalUnitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.organizational_unit_id):
            query['OrganizationalUnitId'] = request.organizational_unit_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteOrganizationalUnit',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteOrganizationalUnitResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_organizational_unit_with_options_async(
        self,
        request: main_models.DeleteOrganizationalUnitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteOrganizationalUnitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.organizational_unit_id):
            query['OrganizationalUnitId'] = request.organizational_unit_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteOrganizationalUnit',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteOrganizationalUnitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_organizational_unit(
        self,
        request: main_models.DeleteOrganizationalUnitRequest,
    ) -> main_models.DeleteOrganizationalUnitResponse:
        runtime = RuntimeOptions()
        return self.delete_organizational_unit_with_options(request, runtime)

    async def delete_organizational_unit_async(
        self,
        request: main_models.DeleteOrganizationalUnitRequest,
    ) -> main_models.DeleteOrganizationalUnitResponse:
        runtime = RuntimeOptions()
        return await self.delete_organizational_unit_with_options_async(request, runtime)

    def delete_organizational_unit_children_with_options(
        self,
        request: main_models.DeleteOrganizationalUnitChildrenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteOrganizationalUnitChildrenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.organizational_unit_id):
            query['OrganizationalUnitId'] = request.organizational_unit_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteOrganizationalUnitChildren',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteOrganizationalUnitChildrenResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_organizational_unit_children_with_options_async(
        self,
        request: main_models.DeleteOrganizationalUnitChildrenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteOrganizationalUnitChildrenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.organizational_unit_id):
            query['OrganizationalUnitId'] = request.organizational_unit_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteOrganizationalUnitChildren',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteOrganizationalUnitChildrenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_organizational_unit_children(
        self,
        request: main_models.DeleteOrganizationalUnitChildrenRequest,
    ) -> main_models.DeleteOrganizationalUnitChildrenResponse:
        runtime = RuntimeOptions()
        return self.delete_organizational_unit_children_with_options(request, runtime)

    async def delete_organizational_unit_children_async(
        self,
        request: main_models.DeleteOrganizationalUnitChildrenRequest,
    ) -> main_models.DeleteOrganizationalUnitChildrenResponse:
        runtime = RuntimeOptions()
        return await self.delete_organizational_unit_children_with_options_async(request, runtime)

    def delete_resource_server_scope_with_options(
        self,
        request: main_models.DeleteResourceServerScopeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteResourceServerScopeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.resource_server_scope_id):
            query['ResourceServerScopeId'] = request.resource_server_scope_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteResourceServerScope',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteResourceServerScopeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_resource_server_scope_with_options_async(
        self,
        request: main_models.DeleteResourceServerScopeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteResourceServerScopeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.resource_server_scope_id):
            query['ResourceServerScopeId'] = request.resource_server_scope_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteResourceServerScope',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteResourceServerScopeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_resource_server_scope(
        self,
        request: main_models.DeleteResourceServerScopeRequest,
    ) -> main_models.DeleteResourceServerScopeResponse:
        runtime = RuntimeOptions()
        return self.delete_resource_server_scope_with_options(request, runtime)

    async def delete_resource_server_scope_async(
        self,
        request: main_models.DeleteResourceServerScopeRequest,
    ) -> main_models.DeleteResourceServerScopeResponse:
        runtime = RuntimeOptions()
        return await self.delete_resource_server_scope_with_options_async(request, runtime)

    def delete_user_with_options(
        self,
        request: main_models.DeleteUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUser',
            version = '2021-12-01',
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
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUser',
            version = '2021-12-01',
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

    def delete_users_with_options(
        self,
        request: main_models.DeleteUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUsers',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_users_with_options_async(
        self,
        request: main_models.DeleteUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUsers',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_users(
        self,
        request: main_models.DeleteUsersRequest,
    ) -> main_models.DeleteUsersResponse:
        runtime = RuntimeOptions()
        return self.delete_users_with_options(request, runtime)

    async def delete_users_async(
        self,
        request: main_models.DeleteUsersRequest,
    ) -> main_models.DeleteUsersResponse:
        runtime = RuntimeOptions()
        return await self.delete_users_with_options_async(request, runtime)

    def delete_web_authn_authenticator_with_options(
        self,
        request: main_models.DeleteWebAuthnAuthenticatorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWebAuthnAuthenticatorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.authenticator_id):
            query['AuthenticatorId'] = request.authenticator_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWebAuthnAuthenticator',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWebAuthnAuthenticatorResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_web_authn_authenticator_with_options_async(
        self,
        request: main_models.DeleteWebAuthnAuthenticatorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWebAuthnAuthenticatorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.authenticator_id):
            query['AuthenticatorId'] = request.authenticator_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWebAuthnAuthenticator',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWebAuthnAuthenticatorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_web_authn_authenticator(
        self,
        request: main_models.DeleteWebAuthnAuthenticatorRequest,
    ) -> main_models.DeleteWebAuthnAuthenticatorResponse:
        runtime = RuntimeOptions()
        return self.delete_web_authn_authenticator_with_options(request, runtime)

    async def delete_web_authn_authenticator_async(
        self,
        request: main_models.DeleteWebAuthnAuthenticatorRequest,
    ) -> main_models.DeleteWebAuthnAuthenticatorResponse:
        runtime = RuntimeOptions()
        return await self.delete_web_authn_authenticator_with_options_async(request, runtime)

    def disable_application_with_options(
        self,
        request: main_models.DisableApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableApplication',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_application_with_options_async(
        self,
        request: main_models.DisableApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableApplication',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_application(
        self,
        request: main_models.DisableApplicationRequest,
    ) -> main_models.DisableApplicationResponse:
        runtime = RuntimeOptions()
        return self.disable_application_with_options(request, runtime)

    async def disable_application_async(
        self,
        request: main_models.DisableApplicationRequest,
    ) -> main_models.DisableApplicationResponse:
        runtime = RuntimeOptions()
        return await self.disable_application_with_options_async(request, runtime)

    def disable_application_api_invoke_with_options(
        self,
        request: main_models.DisableApplicationApiInvokeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableApplicationApiInvokeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableApplicationApiInvoke',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableApplicationApiInvokeResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_application_api_invoke_with_options_async(
        self,
        request: main_models.DisableApplicationApiInvokeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableApplicationApiInvokeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableApplicationApiInvoke',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableApplicationApiInvokeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_application_api_invoke(
        self,
        request: main_models.DisableApplicationApiInvokeRequest,
    ) -> main_models.DisableApplicationApiInvokeResponse:
        runtime = RuntimeOptions()
        return self.disable_application_api_invoke_with_options(request, runtime)

    async def disable_application_api_invoke_async(
        self,
        request: main_models.DisableApplicationApiInvokeRequest,
    ) -> main_models.DisableApplicationApiInvokeResponse:
        runtime = RuntimeOptions()
        return await self.disable_application_api_invoke_with_options_async(request, runtime)

    def disable_application_client_secret_with_options(
        self,
        request: main_models.DisableApplicationClientSecretRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableApplicationClientSecretResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.secret_id):
            query['SecretId'] = request.secret_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableApplicationClientSecret',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableApplicationClientSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_application_client_secret_with_options_async(
        self,
        request: main_models.DisableApplicationClientSecretRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableApplicationClientSecretResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.secret_id):
            query['SecretId'] = request.secret_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableApplicationClientSecret',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableApplicationClientSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_application_client_secret(
        self,
        request: main_models.DisableApplicationClientSecretRequest,
    ) -> main_models.DisableApplicationClientSecretResponse:
        runtime = RuntimeOptions()
        return self.disable_application_client_secret_with_options(request, runtime)

    async def disable_application_client_secret_async(
        self,
        request: main_models.DisableApplicationClientSecretRequest,
    ) -> main_models.DisableApplicationClientSecretResponse:
        runtime = RuntimeOptions()
        return await self.disable_application_client_secret_with_options_async(request, runtime)

    def disable_application_federated_credential_with_options(
        self,
        request: main_models.DisableApplicationFederatedCredentialRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableApplicationFederatedCredentialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_federated_credential_id):
            query['ApplicationFederatedCredentialId'] = request.application_federated_credential_id
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableApplicationFederatedCredential',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableApplicationFederatedCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_application_federated_credential_with_options_async(
        self,
        request: main_models.DisableApplicationFederatedCredentialRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableApplicationFederatedCredentialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_federated_credential_id):
            query['ApplicationFederatedCredentialId'] = request.application_federated_credential_id
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableApplicationFederatedCredential',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableApplicationFederatedCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_application_federated_credential(
        self,
        request: main_models.DisableApplicationFederatedCredentialRequest,
    ) -> main_models.DisableApplicationFederatedCredentialResponse:
        runtime = RuntimeOptions()
        return self.disable_application_federated_credential_with_options(request, runtime)

    async def disable_application_federated_credential_async(
        self,
        request: main_models.DisableApplicationFederatedCredentialRequest,
    ) -> main_models.DisableApplicationFederatedCredentialResponse:
        runtime = RuntimeOptions()
        return await self.disable_application_federated_credential_with_options_async(request, runtime)

    def disable_application_m2mclient_with_options(
        self,
        request: main_models.DisableApplicationM2MClientRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableApplicationM2MClientResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableApplicationM2MClient',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableApplicationM2MClientResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_application_m2mclient_with_options_async(
        self,
        request: main_models.DisableApplicationM2MClientRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableApplicationM2MClientResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableApplicationM2MClient',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableApplicationM2MClientResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_application_m2mclient(
        self,
        request: main_models.DisableApplicationM2MClientRequest,
    ) -> main_models.DisableApplicationM2MClientResponse:
        runtime = RuntimeOptions()
        return self.disable_application_m2mclient_with_options(request, runtime)

    async def disable_application_m2mclient_async(
        self,
        request: main_models.DisableApplicationM2MClientRequest,
    ) -> main_models.DisableApplicationM2MClientResponse:
        runtime = RuntimeOptions()
        return await self.disable_application_m2mclient_with_options_async(request, runtime)

    def disable_application_provisioning_with_options(
        self,
        request: main_models.DisableApplicationProvisioningRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableApplicationProvisioningResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableApplicationProvisioning',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableApplicationProvisioningResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_application_provisioning_with_options_async(
        self,
        request: main_models.DisableApplicationProvisioningRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableApplicationProvisioningResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableApplicationProvisioning',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableApplicationProvisioningResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_application_provisioning(
        self,
        request: main_models.DisableApplicationProvisioningRequest,
    ) -> main_models.DisableApplicationProvisioningResponse:
        runtime = RuntimeOptions()
        return self.disable_application_provisioning_with_options(request, runtime)

    async def disable_application_provisioning_async(
        self,
        request: main_models.DisableApplicationProvisioningRequest,
    ) -> main_models.DisableApplicationProvisioningResponse:
        runtime = RuntimeOptions()
        return await self.disable_application_provisioning_with_options_async(request, runtime)

    def disable_application_resource_server_with_options(
        self,
        request: main_models.DisableApplicationResourceServerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableApplicationResourceServerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableApplicationResourceServer',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableApplicationResourceServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_application_resource_server_with_options_async(
        self,
        request: main_models.DisableApplicationResourceServerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableApplicationResourceServerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableApplicationResourceServer',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableApplicationResourceServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_application_resource_server(
        self,
        request: main_models.DisableApplicationResourceServerRequest,
    ) -> main_models.DisableApplicationResourceServerResponse:
        runtime = RuntimeOptions()
        return self.disable_application_resource_server_with_options(request, runtime)

    async def disable_application_resource_server_async(
        self,
        request: main_models.DisableApplicationResourceServerRequest,
    ) -> main_models.DisableApplicationResourceServerResponse:
        runtime = RuntimeOptions()
        return await self.disable_application_resource_server_with_options_async(request, runtime)

    def disable_application_sso_with_options(
        self,
        request: main_models.DisableApplicationSsoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableApplicationSsoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableApplicationSso',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableApplicationSsoResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_application_sso_with_options_async(
        self,
        request: main_models.DisableApplicationSsoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableApplicationSsoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableApplicationSso',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableApplicationSsoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_application_sso(
        self,
        request: main_models.DisableApplicationSsoRequest,
    ) -> main_models.DisableApplicationSsoResponse:
        runtime = RuntimeOptions()
        return self.disable_application_sso_with_options(request, runtime)

    async def disable_application_sso_async(
        self,
        request: main_models.DisableApplicationSsoRequest,
    ) -> main_models.DisableApplicationSsoResponse:
        runtime = RuntimeOptions()
        return await self.disable_application_sso_with_options_async(request, runtime)

    def disable_application_token_with_options(
        self,
        request: main_models.DisableApplicationTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableApplicationTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.application_token_id):
            query['ApplicationTokenId'] = request.application_token_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableApplicationToken',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableApplicationTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_application_token_with_options_async(
        self,
        request: main_models.DisableApplicationTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableApplicationTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.application_token_id):
            query['ApplicationTokenId'] = request.application_token_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableApplicationToken',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableApplicationTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_application_token(
        self,
        request: main_models.DisableApplicationTokenRequest,
    ) -> main_models.DisableApplicationTokenResponse:
        runtime = RuntimeOptions()
        return self.disable_application_token_with_options(request, runtime)

    async def disable_application_token_async(
        self,
        request: main_models.DisableApplicationTokenRequest,
    ) -> main_models.DisableApplicationTokenResponse:
        runtime = RuntimeOptions()
        return await self.disable_application_token_with_options_async(request, runtime)

    def disable_brand_with_options(
        self,
        request: main_models.DisableBrandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableBrandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.brand_id):
            query['BrandId'] = request.brand_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableBrand',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableBrandResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_brand_with_options_async(
        self,
        request: main_models.DisableBrandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableBrandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.brand_id):
            query['BrandId'] = request.brand_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableBrand',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableBrandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_brand(
        self,
        request: main_models.DisableBrandRequest,
    ) -> main_models.DisableBrandResponse:
        runtime = RuntimeOptions()
        return self.disable_brand_with_options(request, runtime)

    async def disable_brand_async(
        self,
        request: main_models.DisableBrandRequest,
    ) -> main_models.DisableBrandResponse:
        runtime = RuntimeOptions()
        return await self.disable_brand_with_options_async(request, runtime)

    def disable_client_public_key_with_options(
        self,
        request: main_models.DisableClientPublicKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableClientPublicKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.client_public_key_id):
            query['ClientPublicKeyId'] = request.client_public_key_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableClientPublicKey',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableClientPublicKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_client_public_key_with_options_async(
        self,
        request: main_models.DisableClientPublicKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableClientPublicKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.client_public_key_id):
            query['ClientPublicKeyId'] = request.client_public_key_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableClientPublicKey',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableClientPublicKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_client_public_key(
        self,
        request: main_models.DisableClientPublicKeyRequest,
    ) -> main_models.DisableClientPublicKeyResponse:
        runtime = RuntimeOptions()
        return self.disable_client_public_key_with_options(request, runtime)

    async def disable_client_public_key_async(
        self,
        request: main_models.DisableClientPublicKeyRequest,
    ) -> main_models.DisableClientPublicKeyResponse:
        runtime = RuntimeOptions()
        return await self.disable_client_public_key_with_options_async(request, runtime)

    def disable_cloud_account_role_with_options(
        self,
        request: main_models.DisableCloudAccountRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableCloudAccountRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cloud_account_id):
            query['CloudAccountId'] = request.cloud_account_id
        if not DaraCore.is_null(request.cloud_account_role_id):
            query['CloudAccountRoleId'] = request.cloud_account_role_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableCloudAccountRole',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableCloudAccountRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_cloud_account_role_with_options_async(
        self,
        request: main_models.DisableCloudAccountRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableCloudAccountRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cloud_account_id):
            query['CloudAccountId'] = request.cloud_account_id
        if not DaraCore.is_null(request.cloud_account_role_id):
            query['CloudAccountRoleId'] = request.cloud_account_role_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableCloudAccountRole',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableCloudAccountRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_cloud_account_role(
        self,
        request: main_models.DisableCloudAccountRoleRequest,
    ) -> main_models.DisableCloudAccountRoleResponse:
        runtime = RuntimeOptions()
        return self.disable_cloud_account_role_with_options(request, runtime)

    async def disable_cloud_account_role_async(
        self,
        request: main_models.DisableCloudAccountRoleRequest,
    ) -> main_models.DisableCloudAccountRoleResponse:
        runtime = RuntimeOptions()
        return await self.disable_cloud_account_role_with_options_async(request, runtime)

    def disable_conditional_access_policy_with_options(
        self,
        request: main_models.DisableConditionalAccessPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableConditionalAccessPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.conditional_access_policy_id):
            query['ConditionalAccessPolicyId'] = request.conditional_access_policy_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableConditionalAccessPolicy',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableConditionalAccessPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_conditional_access_policy_with_options_async(
        self,
        request: main_models.DisableConditionalAccessPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableConditionalAccessPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.conditional_access_policy_id):
            query['ConditionalAccessPolicyId'] = request.conditional_access_policy_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableConditionalAccessPolicy',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableConditionalAccessPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_conditional_access_policy(
        self,
        request: main_models.DisableConditionalAccessPolicyRequest,
    ) -> main_models.DisableConditionalAccessPolicyResponse:
        runtime = RuntimeOptions()
        return self.disable_conditional_access_policy_with_options(request, runtime)

    async def disable_conditional_access_policy_async(
        self,
        request: main_models.DisableConditionalAccessPolicyRequest,
    ) -> main_models.DisableConditionalAccessPolicyResponse:
        runtime = RuntimeOptions()
        return await self.disable_conditional_access_policy_with_options_async(request, runtime)

    def disable_custom_privacy_policy_with_options(
        self,
        request: main_models.DisableCustomPrivacyPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableCustomPrivacyPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.custom_privacy_policy_id):
            query['CustomPrivacyPolicyId'] = request.custom_privacy_policy_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableCustomPrivacyPolicy',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableCustomPrivacyPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_custom_privacy_policy_with_options_async(
        self,
        request: main_models.DisableCustomPrivacyPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableCustomPrivacyPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.custom_privacy_policy_id):
            query['CustomPrivacyPolicyId'] = request.custom_privacy_policy_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableCustomPrivacyPolicy',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableCustomPrivacyPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_custom_privacy_policy(
        self,
        request: main_models.DisableCustomPrivacyPolicyRequest,
    ) -> main_models.DisableCustomPrivacyPolicyResponse:
        runtime = RuntimeOptions()
        return self.disable_custom_privacy_policy_with_options(request, runtime)

    async def disable_custom_privacy_policy_async(
        self,
        request: main_models.DisableCustomPrivacyPolicyRequest,
    ) -> main_models.DisableCustomPrivacyPolicyResponse:
        runtime = RuntimeOptions()
        return await self.disable_custom_privacy_policy_with_options_async(request, runtime)

    def disable_domain_proxy_token_with_options(
        self,
        request: main_models.DisableDomainProxyTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableDomainProxyTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_id):
            query['DomainId'] = request.domain_id
        if not DaraCore.is_null(request.domain_proxy_token_id):
            query['DomainProxyTokenId'] = request.domain_proxy_token_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableDomainProxyToken',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableDomainProxyTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_domain_proxy_token_with_options_async(
        self,
        request: main_models.DisableDomainProxyTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableDomainProxyTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_id):
            query['DomainId'] = request.domain_id
        if not DaraCore.is_null(request.domain_proxy_token_id):
            query['DomainProxyTokenId'] = request.domain_proxy_token_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableDomainProxyToken',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableDomainProxyTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_domain_proxy_token(
        self,
        request: main_models.DisableDomainProxyTokenRequest,
    ) -> main_models.DisableDomainProxyTokenResponse:
        runtime = RuntimeOptions()
        return self.disable_domain_proxy_token_with_options(request, runtime)

    async def disable_domain_proxy_token_async(
        self,
        request: main_models.DisableDomainProxyTokenRequest,
    ) -> main_models.DisableDomainProxyTokenResponse:
        runtime = RuntimeOptions()
        return await self.disable_domain_proxy_token_with_options_async(request, runtime)

    def disable_federated_credential_provider_with_options(
        self,
        request: main_models.DisableFederatedCredentialProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableFederatedCredentialProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.federated_credential_provider_id):
            query['FederatedCredentialProviderId'] = request.federated_credential_provider_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableFederatedCredentialProvider',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableFederatedCredentialProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_federated_credential_provider_with_options_async(
        self,
        request: main_models.DisableFederatedCredentialProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableFederatedCredentialProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.federated_credential_provider_id):
            query['FederatedCredentialProviderId'] = request.federated_credential_provider_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableFederatedCredentialProvider',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableFederatedCredentialProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_federated_credential_provider(
        self,
        request: main_models.DisableFederatedCredentialProviderRequest,
    ) -> main_models.DisableFederatedCredentialProviderResponse:
        runtime = RuntimeOptions()
        return self.disable_federated_credential_provider_with_options(request, runtime)

    async def disable_federated_credential_provider_async(
        self,
        request: main_models.DisableFederatedCredentialProviderRequest,
    ) -> main_models.DisableFederatedCredentialProviderResponse:
        runtime = RuntimeOptions()
        return await self.disable_federated_credential_provider_with_options_async(request, runtime)

    def disable_identity_provider_advanced_ability_with_options(
        self,
        request: main_models.DisableIdentityProviderAdvancedAbilityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableIdentityProviderAdvancedAbilityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identity_provider_id):
            query['IdentityProviderId'] = request.identity_provider_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableIdentityProviderAdvancedAbility',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableIdentityProviderAdvancedAbilityResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_identity_provider_advanced_ability_with_options_async(
        self,
        request: main_models.DisableIdentityProviderAdvancedAbilityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableIdentityProviderAdvancedAbilityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identity_provider_id):
            query['IdentityProviderId'] = request.identity_provider_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableIdentityProviderAdvancedAbility',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableIdentityProviderAdvancedAbilityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_identity_provider_advanced_ability(
        self,
        request: main_models.DisableIdentityProviderAdvancedAbilityRequest,
    ) -> main_models.DisableIdentityProviderAdvancedAbilityResponse:
        runtime = RuntimeOptions()
        return self.disable_identity_provider_advanced_ability_with_options(request, runtime)

    async def disable_identity_provider_advanced_ability_async(
        self,
        request: main_models.DisableIdentityProviderAdvancedAbilityRequest,
    ) -> main_models.DisableIdentityProviderAdvancedAbilityResponse:
        runtime = RuntimeOptions()
        return await self.disable_identity_provider_advanced_ability_with_options_async(request, runtime)

    def disable_identity_provider_authn_with_options(
        self,
        request: main_models.DisableIdentityProviderAuthnRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableIdentityProviderAuthnResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identity_provider_id):
            query['IdentityProviderId'] = request.identity_provider_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableIdentityProviderAuthn',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableIdentityProviderAuthnResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_identity_provider_authn_with_options_async(
        self,
        request: main_models.DisableIdentityProviderAuthnRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableIdentityProviderAuthnResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identity_provider_id):
            query['IdentityProviderId'] = request.identity_provider_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableIdentityProviderAuthn',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableIdentityProviderAuthnResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_identity_provider_authn(
        self,
        request: main_models.DisableIdentityProviderAuthnRequest,
    ) -> main_models.DisableIdentityProviderAuthnResponse:
        runtime = RuntimeOptions()
        return self.disable_identity_provider_authn_with_options(request, runtime)

    async def disable_identity_provider_authn_async(
        self,
        request: main_models.DisableIdentityProviderAuthnRequest,
    ) -> main_models.DisableIdentityProviderAuthnResponse:
        runtime = RuntimeOptions()
        return await self.disable_identity_provider_authn_with_options_async(request, runtime)

    def disable_identity_provider_ud_pull_with_options(
        self,
        request: main_models.DisableIdentityProviderUdPullRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableIdentityProviderUdPullResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identity_provider_id):
            query['IdentityProviderId'] = request.identity_provider_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableIdentityProviderUdPull',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableIdentityProviderUdPullResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_identity_provider_ud_pull_with_options_async(
        self,
        request: main_models.DisableIdentityProviderUdPullRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableIdentityProviderUdPullResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identity_provider_id):
            query['IdentityProviderId'] = request.identity_provider_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableIdentityProviderUdPull',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableIdentityProviderUdPullResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_identity_provider_ud_pull(
        self,
        request: main_models.DisableIdentityProviderUdPullRequest,
    ) -> main_models.DisableIdentityProviderUdPullResponse:
        runtime = RuntimeOptions()
        return self.disable_identity_provider_ud_pull_with_options(request, runtime)

    async def disable_identity_provider_ud_pull_async(
        self,
        request: main_models.DisableIdentityProviderUdPullRequest,
    ) -> main_models.DisableIdentityProviderUdPullResponse:
        runtime = RuntimeOptions()
        return await self.disable_identity_provider_ud_pull_with_options_async(request, runtime)

    def disable_init_domain_auto_redirect_with_options(
        self,
        request: main_models.DisableInitDomainAutoRedirectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableInitDomainAutoRedirectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableInitDomainAutoRedirect',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableInitDomainAutoRedirectResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_init_domain_auto_redirect_with_options_async(
        self,
        request: main_models.DisableInitDomainAutoRedirectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableInitDomainAutoRedirectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableInitDomainAutoRedirect',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableInitDomainAutoRedirectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_init_domain_auto_redirect(
        self,
        request: main_models.DisableInitDomainAutoRedirectRequest,
    ) -> main_models.DisableInitDomainAutoRedirectResponse:
        runtime = RuntimeOptions()
        return self.disable_init_domain_auto_redirect_with_options(request, runtime)

    async def disable_init_domain_auto_redirect_async(
        self,
        request: main_models.DisableInitDomainAutoRedirectRequest,
    ) -> main_models.DisableInitDomainAutoRedirectResponse:
        runtime = RuntimeOptions()
        return await self.disable_init_domain_auto_redirect_with_options_async(request, runtime)

    def disable_internal_authentication_source_with_options(
        self,
        request: main_models.DisableInternalAuthenticationSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableInternalAuthenticationSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.authentication_source_id):
            query['AuthenticationSourceId'] = request.authentication_source_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableInternalAuthenticationSource',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableInternalAuthenticationSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_internal_authentication_source_with_options_async(
        self,
        request: main_models.DisableInternalAuthenticationSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableInternalAuthenticationSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.authentication_source_id):
            query['AuthenticationSourceId'] = request.authentication_source_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableInternalAuthenticationSource',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableInternalAuthenticationSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_internal_authentication_source(
        self,
        request: main_models.DisableInternalAuthenticationSourceRequest,
    ) -> main_models.DisableInternalAuthenticationSourceResponse:
        runtime = RuntimeOptions()
        return self.disable_internal_authentication_source_with_options(request, runtime)

    async def disable_internal_authentication_source_async(
        self,
        request: main_models.DisableInternalAuthenticationSourceRequest,
    ) -> main_models.DisableInternalAuthenticationSourceResponse:
        runtime = RuntimeOptions()
        return await self.disable_internal_authentication_source_with_options_async(request, runtime)

    def disable_resource_server_custom_subject_with_options(
        self,
        request: main_models.DisableResourceServerCustomSubjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableResourceServerCustomSubjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableResourceServerCustomSubject',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableResourceServerCustomSubjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_resource_server_custom_subject_with_options_async(
        self,
        request: main_models.DisableResourceServerCustomSubjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableResourceServerCustomSubjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableResourceServerCustomSubject',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableResourceServerCustomSubjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_resource_server_custom_subject(
        self,
        request: main_models.DisableResourceServerCustomSubjectRequest,
    ) -> main_models.DisableResourceServerCustomSubjectResponse:
        runtime = RuntimeOptions()
        return self.disable_resource_server_custom_subject_with_options(request, runtime)

    async def disable_resource_server_custom_subject_async(
        self,
        request: main_models.DisableResourceServerCustomSubjectRequest,
    ) -> main_models.DisableResourceServerCustomSubjectResponse:
        runtime = RuntimeOptions()
        return await self.disable_resource_server_custom_subject_with_options_async(request, runtime)

    def disable_user_with_options(
        self,
        request: main_models.DisableUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableUser',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_user_with_options_async(
        self,
        request: main_models.DisableUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableUser',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_user(
        self,
        request: main_models.DisableUserRequest,
    ) -> main_models.DisableUserResponse:
        runtime = RuntimeOptions()
        return self.disable_user_with_options(request, runtime)

    async def disable_user_async(
        self,
        request: main_models.DisableUserRequest,
    ) -> main_models.DisableUserResponse:
        runtime = RuntimeOptions()
        return await self.disable_user_with_options_async(request, runtime)

    def enable_application_with_options(
        self,
        request: main_models.EnableApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableApplication',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_application_with_options_async(
        self,
        request: main_models.EnableApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableApplication',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_application(
        self,
        request: main_models.EnableApplicationRequest,
    ) -> main_models.EnableApplicationResponse:
        runtime = RuntimeOptions()
        return self.enable_application_with_options(request, runtime)

    async def enable_application_async(
        self,
        request: main_models.EnableApplicationRequest,
    ) -> main_models.EnableApplicationResponse:
        runtime = RuntimeOptions()
        return await self.enable_application_with_options_async(request, runtime)

    def enable_application_api_invoke_with_options(
        self,
        request: main_models.EnableApplicationApiInvokeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableApplicationApiInvokeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableApplicationApiInvoke',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableApplicationApiInvokeResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_application_api_invoke_with_options_async(
        self,
        request: main_models.EnableApplicationApiInvokeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableApplicationApiInvokeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableApplicationApiInvoke',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableApplicationApiInvokeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_application_api_invoke(
        self,
        request: main_models.EnableApplicationApiInvokeRequest,
    ) -> main_models.EnableApplicationApiInvokeResponse:
        runtime = RuntimeOptions()
        return self.enable_application_api_invoke_with_options(request, runtime)

    async def enable_application_api_invoke_async(
        self,
        request: main_models.EnableApplicationApiInvokeRequest,
    ) -> main_models.EnableApplicationApiInvokeResponse:
        runtime = RuntimeOptions()
        return await self.enable_application_api_invoke_with_options_async(request, runtime)

    def enable_application_client_secret_with_options(
        self,
        request: main_models.EnableApplicationClientSecretRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableApplicationClientSecretResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.secret_id):
            query['SecretId'] = request.secret_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableApplicationClientSecret',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableApplicationClientSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_application_client_secret_with_options_async(
        self,
        request: main_models.EnableApplicationClientSecretRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableApplicationClientSecretResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.secret_id):
            query['SecretId'] = request.secret_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableApplicationClientSecret',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableApplicationClientSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_application_client_secret(
        self,
        request: main_models.EnableApplicationClientSecretRequest,
    ) -> main_models.EnableApplicationClientSecretResponse:
        runtime = RuntimeOptions()
        return self.enable_application_client_secret_with_options(request, runtime)

    async def enable_application_client_secret_async(
        self,
        request: main_models.EnableApplicationClientSecretRequest,
    ) -> main_models.EnableApplicationClientSecretResponse:
        runtime = RuntimeOptions()
        return await self.enable_application_client_secret_with_options_async(request, runtime)

    def enable_application_federated_credential_with_options(
        self,
        request: main_models.EnableApplicationFederatedCredentialRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableApplicationFederatedCredentialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_federated_credential_id):
            query['ApplicationFederatedCredentialId'] = request.application_federated_credential_id
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableApplicationFederatedCredential',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableApplicationFederatedCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_application_federated_credential_with_options_async(
        self,
        request: main_models.EnableApplicationFederatedCredentialRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableApplicationFederatedCredentialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_federated_credential_id):
            query['ApplicationFederatedCredentialId'] = request.application_federated_credential_id
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableApplicationFederatedCredential',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableApplicationFederatedCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_application_federated_credential(
        self,
        request: main_models.EnableApplicationFederatedCredentialRequest,
    ) -> main_models.EnableApplicationFederatedCredentialResponse:
        runtime = RuntimeOptions()
        return self.enable_application_federated_credential_with_options(request, runtime)

    async def enable_application_federated_credential_async(
        self,
        request: main_models.EnableApplicationFederatedCredentialRequest,
    ) -> main_models.EnableApplicationFederatedCredentialResponse:
        runtime = RuntimeOptions()
        return await self.enable_application_federated_credential_with_options_async(request, runtime)

    def enable_application_m2mclient_with_options(
        self,
        request: main_models.EnableApplicationM2MClientRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableApplicationM2MClientResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableApplicationM2MClient',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableApplicationM2MClientResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_application_m2mclient_with_options_async(
        self,
        request: main_models.EnableApplicationM2MClientRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableApplicationM2MClientResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableApplicationM2MClient',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableApplicationM2MClientResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_application_m2mclient(
        self,
        request: main_models.EnableApplicationM2MClientRequest,
    ) -> main_models.EnableApplicationM2MClientResponse:
        runtime = RuntimeOptions()
        return self.enable_application_m2mclient_with_options(request, runtime)

    async def enable_application_m2mclient_async(
        self,
        request: main_models.EnableApplicationM2MClientRequest,
    ) -> main_models.EnableApplicationM2MClientResponse:
        runtime = RuntimeOptions()
        return await self.enable_application_m2mclient_with_options_async(request, runtime)

    def enable_application_provisioning_with_options(
        self,
        request: main_models.EnableApplicationProvisioningRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableApplicationProvisioningResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableApplicationProvisioning',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableApplicationProvisioningResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_application_provisioning_with_options_async(
        self,
        request: main_models.EnableApplicationProvisioningRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableApplicationProvisioningResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableApplicationProvisioning',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableApplicationProvisioningResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_application_provisioning(
        self,
        request: main_models.EnableApplicationProvisioningRequest,
    ) -> main_models.EnableApplicationProvisioningResponse:
        runtime = RuntimeOptions()
        return self.enable_application_provisioning_with_options(request, runtime)

    async def enable_application_provisioning_async(
        self,
        request: main_models.EnableApplicationProvisioningRequest,
    ) -> main_models.EnableApplicationProvisioningResponse:
        runtime = RuntimeOptions()
        return await self.enable_application_provisioning_with_options_async(request, runtime)

    def enable_application_resource_server_with_options(
        self,
        request: main_models.EnableApplicationResourceServerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableApplicationResourceServerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableApplicationResourceServer',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableApplicationResourceServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_application_resource_server_with_options_async(
        self,
        request: main_models.EnableApplicationResourceServerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableApplicationResourceServerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableApplicationResourceServer',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableApplicationResourceServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_application_resource_server(
        self,
        request: main_models.EnableApplicationResourceServerRequest,
    ) -> main_models.EnableApplicationResourceServerResponse:
        runtime = RuntimeOptions()
        return self.enable_application_resource_server_with_options(request, runtime)

    async def enable_application_resource_server_async(
        self,
        request: main_models.EnableApplicationResourceServerRequest,
    ) -> main_models.EnableApplicationResourceServerResponse:
        runtime = RuntimeOptions()
        return await self.enable_application_resource_server_with_options_async(request, runtime)

    def enable_application_sso_with_options(
        self,
        request: main_models.EnableApplicationSsoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableApplicationSsoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableApplicationSso',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableApplicationSsoResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_application_sso_with_options_async(
        self,
        request: main_models.EnableApplicationSsoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableApplicationSsoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableApplicationSso',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableApplicationSsoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_application_sso(
        self,
        request: main_models.EnableApplicationSsoRequest,
    ) -> main_models.EnableApplicationSsoResponse:
        runtime = RuntimeOptions()
        return self.enable_application_sso_with_options(request, runtime)

    async def enable_application_sso_async(
        self,
        request: main_models.EnableApplicationSsoRequest,
    ) -> main_models.EnableApplicationSsoResponse:
        runtime = RuntimeOptions()
        return await self.enable_application_sso_with_options_async(request, runtime)

    def enable_application_token_with_options(
        self,
        request: main_models.EnableApplicationTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableApplicationTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.application_token_id):
            query['ApplicationTokenId'] = request.application_token_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableApplicationToken',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableApplicationTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_application_token_with_options_async(
        self,
        request: main_models.EnableApplicationTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableApplicationTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.application_token_id):
            query['ApplicationTokenId'] = request.application_token_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableApplicationToken',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableApplicationTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_application_token(
        self,
        request: main_models.EnableApplicationTokenRequest,
    ) -> main_models.EnableApplicationTokenResponse:
        runtime = RuntimeOptions()
        return self.enable_application_token_with_options(request, runtime)

    async def enable_application_token_async(
        self,
        request: main_models.EnableApplicationTokenRequest,
    ) -> main_models.EnableApplicationTokenResponse:
        runtime = RuntimeOptions()
        return await self.enable_application_token_with_options_async(request, runtime)

    def enable_brand_with_options(
        self,
        request: main_models.EnableBrandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableBrandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.brand_id):
            query['BrandId'] = request.brand_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableBrand',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableBrandResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_brand_with_options_async(
        self,
        request: main_models.EnableBrandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableBrandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.brand_id):
            query['BrandId'] = request.brand_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableBrand',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableBrandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_brand(
        self,
        request: main_models.EnableBrandRequest,
    ) -> main_models.EnableBrandResponse:
        runtime = RuntimeOptions()
        return self.enable_brand_with_options(request, runtime)

    async def enable_brand_async(
        self,
        request: main_models.EnableBrandRequest,
    ) -> main_models.EnableBrandResponse:
        runtime = RuntimeOptions()
        return await self.enable_brand_with_options_async(request, runtime)

    def enable_client_public_key_with_options(
        self,
        request: main_models.EnableClientPublicKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableClientPublicKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.client_public_key_id):
            query['ClientPublicKeyId'] = request.client_public_key_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableClientPublicKey',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableClientPublicKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_client_public_key_with_options_async(
        self,
        request: main_models.EnableClientPublicKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableClientPublicKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.client_public_key_id):
            query['ClientPublicKeyId'] = request.client_public_key_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableClientPublicKey',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableClientPublicKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_client_public_key(
        self,
        request: main_models.EnableClientPublicKeyRequest,
    ) -> main_models.EnableClientPublicKeyResponse:
        runtime = RuntimeOptions()
        return self.enable_client_public_key_with_options(request, runtime)

    async def enable_client_public_key_async(
        self,
        request: main_models.EnableClientPublicKeyRequest,
    ) -> main_models.EnableClientPublicKeyResponse:
        runtime = RuntimeOptions()
        return await self.enable_client_public_key_with_options_async(request, runtime)

    def enable_cloud_account_role_with_options(
        self,
        request: main_models.EnableCloudAccountRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableCloudAccountRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cloud_account_id):
            query['CloudAccountId'] = request.cloud_account_id
        if not DaraCore.is_null(request.cloud_account_role_id):
            query['CloudAccountRoleId'] = request.cloud_account_role_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableCloudAccountRole',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableCloudAccountRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_cloud_account_role_with_options_async(
        self,
        request: main_models.EnableCloudAccountRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableCloudAccountRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cloud_account_id):
            query['CloudAccountId'] = request.cloud_account_id
        if not DaraCore.is_null(request.cloud_account_role_id):
            query['CloudAccountRoleId'] = request.cloud_account_role_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableCloudAccountRole',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableCloudAccountRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_cloud_account_role(
        self,
        request: main_models.EnableCloudAccountRoleRequest,
    ) -> main_models.EnableCloudAccountRoleResponse:
        runtime = RuntimeOptions()
        return self.enable_cloud_account_role_with_options(request, runtime)

    async def enable_cloud_account_role_async(
        self,
        request: main_models.EnableCloudAccountRoleRequest,
    ) -> main_models.EnableCloudAccountRoleResponse:
        runtime = RuntimeOptions()
        return await self.enable_cloud_account_role_with_options_async(request, runtime)

    def enable_conditional_access_policy_with_options(
        self,
        request: main_models.EnableConditionalAccessPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableConditionalAccessPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.conditional_access_policy_id):
            query['ConditionalAccessPolicyId'] = request.conditional_access_policy_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableConditionalAccessPolicy',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableConditionalAccessPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_conditional_access_policy_with_options_async(
        self,
        request: main_models.EnableConditionalAccessPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableConditionalAccessPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.conditional_access_policy_id):
            query['ConditionalAccessPolicyId'] = request.conditional_access_policy_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableConditionalAccessPolicy',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableConditionalAccessPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_conditional_access_policy(
        self,
        request: main_models.EnableConditionalAccessPolicyRequest,
    ) -> main_models.EnableConditionalAccessPolicyResponse:
        runtime = RuntimeOptions()
        return self.enable_conditional_access_policy_with_options(request, runtime)

    async def enable_conditional_access_policy_async(
        self,
        request: main_models.EnableConditionalAccessPolicyRequest,
    ) -> main_models.EnableConditionalAccessPolicyResponse:
        runtime = RuntimeOptions()
        return await self.enable_conditional_access_policy_with_options_async(request, runtime)

    def enable_custom_privacy_policy_with_options(
        self,
        request: main_models.EnableCustomPrivacyPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableCustomPrivacyPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.custom_privacy_policy_id):
            query['CustomPrivacyPolicyId'] = request.custom_privacy_policy_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableCustomPrivacyPolicy',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableCustomPrivacyPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_custom_privacy_policy_with_options_async(
        self,
        request: main_models.EnableCustomPrivacyPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableCustomPrivacyPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.custom_privacy_policy_id):
            query['CustomPrivacyPolicyId'] = request.custom_privacy_policy_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableCustomPrivacyPolicy',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableCustomPrivacyPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_custom_privacy_policy(
        self,
        request: main_models.EnableCustomPrivacyPolicyRequest,
    ) -> main_models.EnableCustomPrivacyPolicyResponse:
        runtime = RuntimeOptions()
        return self.enable_custom_privacy_policy_with_options(request, runtime)

    async def enable_custom_privacy_policy_async(
        self,
        request: main_models.EnableCustomPrivacyPolicyRequest,
    ) -> main_models.EnableCustomPrivacyPolicyResponse:
        runtime = RuntimeOptions()
        return await self.enable_custom_privacy_policy_with_options_async(request, runtime)

    def enable_domain_proxy_token_with_options(
        self,
        request: main_models.EnableDomainProxyTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableDomainProxyTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_id):
            query['DomainId'] = request.domain_id
        if not DaraCore.is_null(request.domain_proxy_token_id):
            query['DomainProxyTokenId'] = request.domain_proxy_token_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableDomainProxyToken',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableDomainProxyTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_domain_proxy_token_with_options_async(
        self,
        request: main_models.EnableDomainProxyTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableDomainProxyTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_id):
            query['DomainId'] = request.domain_id
        if not DaraCore.is_null(request.domain_proxy_token_id):
            query['DomainProxyTokenId'] = request.domain_proxy_token_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableDomainProxyToken',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableDomainProxyTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_domain_proxy_token(
        self,
        request: main_models.EnableDomainProxyTokenRequest,
    ) -> main_models.EnableDomainProxyTokenResponse:
        runtime = RuntimeOptions()
        return self.enable_domain_proxy_token_with_options(request, runtime)

    async def enable_domain_proxy_token_async(
        self,
        request: main_models.EnableDomainProxyTokenRequest,
    ) -> main_models.EnableDomainProxyTokenResponse:
        runtime = RuntimeOptions()
        return await self.enable_domain_proxy_token_with_options_async(request, runtime)

    def enable_federated_credential_provider_with_options(
        self,
        request: main_models.EnableFederatedCredentialProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableFederatedCredentialProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.federated_credential_provider_id):
            query['FederatedCredentialProviderId'] = request.federated_credential_provider_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableFederatedCredentialProvider',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableFederatedCredentialProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_federated_credential_provider_with_options_async(
        self,
        request: main_models.EnableFederatedCredentialProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableFederatedCredentialProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.federated_credential_provider_id):
            query['FederatedCredentialProviderId'] = request.federated_credential_provider_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableFederatedCredentialProvider',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableFederatedCredentialProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_federated_credential_provider(
        self,
        request: main_models.EnableFederatedCredentialProviderRequest,
    ) -> main_models.EnableFederatedCredentialProviderResponse:
        runtime = RuntimeOptions()
        return self.enable_federated_credential_provider_with_options(request, runtime)

    async def enable_federated_credential_provider_async(
        self,
        request: main_models.EnableFederatedCredentialProviderRequest,
    ) -> main_models.EnableFederatedCredentialProviderResponse:
        runtime = RuntimeOptions()
        return await self.enable_federated_credential_provider_with_options_async(request, runtime)

    def enable_identity_provider_advanced_ability_with_options(
        self,
        request: main_models.EnableIdentityProviderAdvancedAbilityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableIdentityProviderAdvancedAbilityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identity_provider_id):
            query['IdentityProviderId'] = request.identity_provider_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableIdentityProviderAdvancedAbility',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableIdentityProviderAdvancedAbilityResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_identity_provider_advanced_ability_with_options_async(
        self,
        request: main_models.EnableIdentityProviderAdvancedAbilityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableIdentityProviderAdvancedAbilityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identity_provider_id):
            query['IdentityProviderId'] = request.identity_provider_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableIdentityProviderAdvancedAbility',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableIdentityProviderAdvancedAbilityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_identity_provider_advanced_ability(
        self,
        request: main_models.EnableIdentityProviderAdvancedAbilityRequest,
    ) -> main_models.EnableIdentityProviderAdvancedAbilityResponse:
        runtime = RuntimeOptions()
        return self.enable_identity_provider_advanced_ability_with_options(request, runtime)

    async def enable_identity_provider_advanced_ability_async(
        self,
        request: main_models.EnableIdentityProviderAdvancedAbilityRequest,
    ) -> main_models.EnableIdentityProviderAdvancedAbilityResponse:
        runtime = RuntimeOptions()
        return await self.enable_identity_provider_advanced_ability_with_options_async(request, runtime)

    def enable_identity_provider_authn_with_options(
        self,
        request: main_models.EnableIdentityProviderAuthnRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableIdentityProviderAuthnResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identity_provider_id):
            query['IdentityProviderId'] = request.identity_provider_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableIdentityProviderAuthn',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableIdentityProviderAuthnResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_identity_provider_authn_with_options_async(
        self,
        request: main_models.EnableIdentityProviderAuthnRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableIdentityProviderAuthnResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identity_provider_id):
            query['IdentityProviderId'] = request.identity_provider_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableIdentityProviderAuthn',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableIdentityProviderAuthnResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_identity_provider_authn(
        self,
        request: main_models.EnableIdentityProviderAuthnRequest,
    ) -> main_models.EnableIdentityProviderAuthnResponse:
        runtime = RuntimeOptions()
        return self.enable_identity_provider_authn_with_options(request, runtime)

    async def enable_identity_provider_authn_async(
        self,
        request: main_models.EnableIdentityProviderAuthnRequest,
    ) -> main_models.EnableIdentityProviderAuthnResponse:
        runtime = RuntimeOptions()
        return await self.enable_identity_provider_authn_with_options_async(request, runtime)

    def enable_identity_provider_ud_pull_with_options(
        self,
        request: main_models.EnableIdentityProviderUdPullRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableIdentityProviderUdPullResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identity_provider_id):
            query['IdentityProviderId'] = request.identity_provider_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableIdentityProviderUdPull',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableIdentityProviderUdPullResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_identity_provider_ud_pull_with_options_async(
        self,
        request: main_models.EnableIdentityProviderUdPullRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableIdentityProviderUdPullResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identity_provider_id):
            query['IdentityProviderId'] = request.identity_provider_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableIdentityProviderUdPull',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableIdentityProviderUdPullResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_identity_provider_ud_pull(
        self,
        request: main_models.EnableIdentityProviderUdPullRequest,
    ) -> main_models.EnableIdentityProviderUdPullResponse:
        runtime = RuntimeOptions()
        return self.enable_identity_provider_ud_pull_with_options(request, runtime)

    async def enable_identity_provider_ud_pull_async(
        self,
        request: main_models.EnableIdentityProviderUdPullRequest,
    ) -> main_models.EnableIdentityProviderUdPullResponse:
        runtime = RuntimeOptions()
        return await self.enable_identity_provider_ud_pull_with_options_async(request, runtime)

    def enable_init_domain_auto_redirect_with_options(
        self,
        request: main_models.EnableInitDomainAutoRedirectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableInitDomainAutoRedirectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableInitDomainAutoRedirect',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableInitDomainAutoRedirectResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_init_domain_auto_redirect_with_options_async(
        self,
        request: main_models.EnableInitDomainAutoRedirectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableInitDomainAutoRedirectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableInitDomainAutoRedirect',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableInitDomainAutoRedirectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_init_domain_auto_redirect(
        self,
        request: main_models.EnableInitDomainAutoRedirectRequest,
    ) -> main_models.EnableInitDomainAutoRedirectResponse:
        runtime = RuntimeOptions()
        return self.enable_init_domain_auto_redirect_with_options(request, runtime)

    async def enable_init_domain_auto_redirect_async(
        self,
        request: main_models.EnableInitDomainAutoRedirectRequest,
    ) -> main_models.EnableInitDomainAutoRedirectResponse:
        runtime = RuntimeOptions()
        return await self.enable_init_domain_auto_redirect_with_options_async(request, runtime)

    def enable_internal_authentication_source_with_options(
        self,
        request: main_models.EnableInternalAuthenticationSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableInternalAuthenticationSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.authentication_source_id):
            query['AuthenticationSourceId'] = request.authentication_source_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableInternalAuthenticationSource',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableInternalAuthenticationSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_internal_authentication_source_with_options_async(
        self,
        request: main_models.EnableInternalAuthenticationSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableInternalAuthenticationSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.authentication_source_id):
            query['AuthenticationSourceId'] = request.authentication_source_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableInternalAuthenticationSource',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableInternalAuthenticationSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_internal_authentication_source(
        self,
        request: main_models.EnableInternalAuthenticationSourceRequest,
    ) -> main_models.EnableInternalAuthenticationSourceResponse:
        runtime = RuntimeOptions()
        return self.enable_internal_authentication_source_with_options(request, runtime)

    async def enable_internal_authentication_source_async(
        self,
        request: main_models.EnableInternalAuthenticationSourceRequest,
    ) -> main_models.EnableInternalAuthenticationSourceResponse:
        runtime = RuntimeOptions()
        return await self.enable_internal_authentication_source_with_options_async(request, runtime)

    def enable_resource_server_custom_subject_with_options(
        self,
        request: main_models.EnableResourceServerCustomSubjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableResourceServerCustomSubjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableResourceServerCustomSubject',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableResourceServerCustomSubjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_resource_server_custom_subject_with_options_async(
        self,
        request: main_models.EnableResourceServerCustomSubjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableResourceServerCustomSubjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableResourceServerCustomSubject',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableResourceServerCustomSubjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_resource_server_custom_subject(
        self,
        request: main_models.EnableResourceServerCustomSubjectRequest,
    ) -> main_models.EnableResourceServerCustomSubjectResponse:
        runtime = RuntimeOptions()
        return self.enable_resource_server_custom_subject_with_options(request, runtime)

    async def enable_resource_server_custom_subject_async(
        self,
        request: main_models.EnableResourceServerCustomSubjectRequest,
    ) -> main_models.EnableResourceServerCustomSubjectResponse:
        runtime = RuntimeOptions()
        return await self.enable_resource_server_custom_subject_with_options_async(request, runtime)

    def enable_user_with_options(
        self,
        request: main_models.EnableUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableUser',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_user_with_options_async(
        self,
        request: main_models.EnableUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableUser',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_user(
        self,
        request: main_models.EnableUserRequest,
    ) -> main_models.EnableUserResponse:
        runtime = RuntimeOptions()
        return self.enable_user_with_options(request, runtime)

    async def enable_user_async(
        self,
        request: main_models.EnableUserRequest,
    ) -> main_models.EnableUserResponse:
        runtime = RuntimeOptions()
        return await self.enable_user_with_options_async(request, runtime)

    def generate_download_url_for_synchronization_job_with_options(
        self,
        request: main_models.GenerateDownloadUrlForSynchronizationJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateDownloadUrlForSynchronizationJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateDownloadUrlForSynchronizationJob',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateDownloadUrlForSynchronizationJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_download_url_for_synchronization_job_with_options_async(
        self,
        request: main_models.GenerateDownloadUrlForSynchronizationJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateDownloadUrlForSynchronizationJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateDownloadUrlForSynchronizationJob',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateDownloadUrlForSynchronizationJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_download_url_for_synchronization_job(
        self,
        request: main_models.GenerateDownloadUrlForSynchronizationJobRequest,
    ) -> main_models.GenerateDownloadUrlForSynchronizationJobResponse:
        runtime = RuntimeOptions()
        return self.generate_download_url_for_synchronization_job_with_options(request, runtime)

    async def generate_download_url_for_synchronization_job_async(
        self,
        request: main_models.GenerateDownloadUrlForSynchronizationJobRequest,
    ) -> main_models.GenerateDownloadUrlForSynchronizationJobResponse:
        runtime = RuntimeOptions()
        return await self.generate_download_url_for_synchronization_job_with_options_async(request, runtime)

    def generate_file_import_template_with_options(
        self,
        request: main_models.GenerateFileImportTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateFileImportTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateFileImportTemplate',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateFileImportTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_file_import_template_with_options_async(
        self,
        request: main_models.GenerateFileImportTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateFileImportTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateFileImportTemplate',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateFileImportTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_file_import_template(
        self,
        request: main_models.GenerateFileImportTemplateRequest,
    ) -> main_models.GenerateFileImportTemplateResponse:
        runtime = RuntimeOptions()
        return self.generate_file_import_template_with_options(request, runtime)

    async def generate_file_import_template_async(
        self,
        request: main_models.GenerateFileImportTemplateRequest,
    ) -> main_models.GenerateFileImportTemplateResponse:
        runtime = RuntimeOptions()
        return await self.generate_file_import_template_with_options_async(request, runtime)

    def generate_upload_auth_with_options(
        self,
        request: main_models.GenerateUploadAuthRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateUploadAuthResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.purpose):
            query['Purpose'] = request.purpose
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateUploadAuth',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateUploadAuthResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_upload_auth_with_options_async(
        self,
        request: main_models.GenerateUploadAuthRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateUploadAuthResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.purpose):
            query['Purpose'] = request.purpose
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateUploadAuth',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateUploadAuthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_upload_auth(
        self,
        request: main_models.GenerateUploadAuthRequest,
    ) -> main_models.GenerateUploadAuthResponse:
        runtime = RuntimeOptions()
        return self.generate_upload_auth_with_options(request, runtime)

    async def generate_upload_auth_async(
        self,
        request: main_models.GenerateUploadAuthRequest,
    ) -> main_models.GenerateUploadAuthResponse:
        runtime = RuntimeOptions()
        return await self.generate_upload_auth_with_options_async(request, runtime)

    def get_application_with_options(
        self,
        request: main_models.GetApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApplication',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_application_with_options_async(
        self,
        request: main_models.GetApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApplication',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_application(
        self,
        request: main_models.GetApplicationRequest,
    ) -> main_models.GetApplicationResponse:
        runtime = RuntimeOptions()
        return self.get_application_with_options(request, runtime)

    async def get_application_async(
        self,
        request: main_models.GetApplicationRequest,
    ) -> main_models.GetApplicationResponse:
        runtime = RuntimeOptions()
        return await self.get_application_with_options_async(request, runtime)

    def get_application_advanced_config_with_options(
        self,
        request: main_models.GetApplicationAdvancedConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApplicationAdvancedConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApplicationAdvancedConfig',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApplicationAdvancedConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_application_advanced_config_with_options_async(
        self,
        request: main_models.GetApplicationAdvancedConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApplicationAdvancedConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApplicationAdvancedConfig',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApplicationAdvancedConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_application_advanced_config(
        self,
        request: main_models.GetApplicationAdvancedConfigRequest,
    ) -> main_models.GetApplicationAdvancedConfigResponse:
        runtime = RuntimeOptions()
        return self.get_application_advanced_config_with_options(request, runtime)

    async def get_application_advanced_config_async(
        self,
        request: main_models.GetApplicationAdvancedConfigRequest,
    ) -> main_models.GetApplicationAdvancedConfigResponse:
        runtime = RuntimeOptions()
        return await self.get_application_advanced_config_with_options_async(request, runtime)

    def get_application_federated_credential_with_options(
        self,
        request: main_models.GetApplicationFederatedCredentialRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApplicationFederatedCredentialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_federated_credential_id):
            query['ApplicationFederatedCredentialId'] = request.application_federated_credential_id
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApplicationFederatedCredential',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApplicationFederatedCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_application_federated_credential_with_options_async(
        self,
        request: main_models.GetApplicationFederatedCredentialRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApplicationFederatedCredentialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_federated_credential_id):
            query['ApplicationFederatedCredentialId'] = request.application_federated_credential_id
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApplicationFederatedCredential',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApplicationFederatedCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_application_federated_credential(
        self,
        request: main_models.GetApplicationFederatedCredentialRequest,
    ) -> main_models.GetApplicationFederatedCredentialResponse:
        runtime = RuntimeOptions()
        return self.get_application_federated_credential_with_options(request, runtime)

    async def get_application_federated_credential_async(
        self,
        request: main_models.GetApplicationFederatedCredentialRequest,
    ) -> main_models.GetApplicationFederatedCredentialResponse:
        runtime = RuntimeOptions()
        return await self.get_application_federated_credential_with_options_async(request, runtime)

    def get_application_grant_scope_with_options(
        self,
        request: main_models.GetApplicationGrantScopeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApplicationGrantScopeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApplicationGrantScope',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApplicationGrantScopeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_application_grant_scope_with_options_async(
        self,
        request: main_models.GetApplicationGrantScopeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApplicationGrantScopeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApplicationGrantScope',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApplicationGrantScopeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_application_grant_scope(
        self,
        request: main_models.GetApplicationGrantScopeRequest,
    ) -> main_models.GetApplicationGrantScopeResponse:
        runtime = RuntimeOptions()
        return self.get_application_grant_scope_with_options(request, runtime)

    async def get_application_grant_scope_async(
        self,
        request: main_models.GetApplicationGrantScopeRequest,
    ) -> main_models.GetApplicationGrantScopeResponse:
        runtime = RuntimeOptions()
        return await self.get_application_grant_scope_with_options_async(request, runtime)

    def get_application_provisioning_config_with_options(
        self,
        request: main_models.GetApplicationProvisioningConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApplicationProvisioningConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApplicationProvisioningConfig',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApplicationProvisioningConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_application_provisioning_config_with_options_async(
        self,
        request: main_models.GetApplicationProvisioningConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApplicationProvisioningConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApplicationProvisioningConfig',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApplicationProvisioningConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_application_provisioning_config(
        self,
        request: main_models.GetApplicationProvisioningConfigRequest,
    ) -> main_models.GetApplicationProvisioningConfigResponse:
        runtime = RuntimeOptions()
        return self.get_application_provisioning_config_with_options(request, runtime)

    async def get_application_provisioning_config_async(
        self,
        request: main_models.GetApplicationProvisioningConfigRequest,
    ) -> main_models.GetApplicationProvisioningConfigResponse:
        runtime = RuntimeOptions()
        return await self.get_application_provisioning_config_with_options_async(request, runtime)

    def get_application_provisioning_scope_with_options(
        self,
        request: main_models.GetApplicationProvisioningScopeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApplicationProvisioningScopeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApplicationProvisioningScope',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApplicationProvisioningScopeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_application_provisioning_scope_with_options_async(
        self,
        request: main_models.GetApplicationProvisioningScopeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApplicationProvisioningScopeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApplicationProvisioningScope',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApplicationProvisioningScopeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_application_provisioning_scope(
        self,
        request: main_models.GetApplicationProvisioningScopeRequest,
    ) -> main_models.GetApplicationProvisioningScopeResponse:
        runtime = RuntimeOptions()
        return self.get_application_provisioning_scope_with_options(request, runtime)

    async def get_application_provisioning_scope_async(
        self,
        request: main_models.GetApplicationProvisioningScopeRequest,
    ) -> main_models.GetApplicationProvisioningScopeResponse:
        runtime = RuntimeOptions()
        return await self.get_application_provisioning_scope_with_options_async(request, runtime)

    def get_application_role_with_options(
        self,
        request: main_models.GetApplicationRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApplicationRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.application_role_id):
            query['ApplicationRoleId'] = request.application_role_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApplicationRole',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApplicationRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_application_role_with_options_async(
        self,
        request: main_models.GetApplicationRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApplicationRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.application_role_id):
            query['ApplicationRoleId'] = request.application_role_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApplicationRole',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApplicationRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_application_role(
        self,
        request: main_models.GetApplicationRoleRequest,
    ) -> main_models.GetApplicationRoleResponse:
        runtime = RuntimeOptions()
        return self.get_application_role_with_options(request, runtime)

    async def get_application_role_async(
        self,
        request: main_models.GetApplicationRoleRequest,
    ) -> main_models.GetApplicationRoleResponse:
        runtime = RuntimeOptions()
        return await self.get_application_role_with_options_async(request, runtime)

    def get_application_sso_config_with_options(
        self,
        request: main_models.GetApplicationSsoConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApplicationSsoConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApplicationSsoConfig',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApplicationSsoConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_application_sso_config_with_options_async(
        self,
        request: main_models.GetApplicationSsoConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApplicationSsoConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApplicationSsoConfig',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApplicationSsoConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_application_sso_config(
        self,
        request: main_models.GetApplicationSsoConfigRequest,
    ) -> main_models.GetApplicationSsoConfigResponse:
        runtime = RuntimeOptions()
        return self.get_application_sso_config_with_options(request, runtime)

    async def get_application_sso_config_async(
        self,
        request: main_models.GetApplicationSsoConfigRequest,
    ) -> main_models.GetApplicationSsoConfigResponse:
        runtime = RuntimeOptions()
        return await self.get_application_sso_config_with_options_async(request, runtime)

    def get_application_template_with_options(
        self,
        request: main_models.GetApplicationTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApplicationTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_template_id):
            query['ApplicationTemplateId'] = request.application_template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApplicationTemplate',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApplicationTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_application_template_with_options_async(
        self,
        request: main_models.GetApplicationTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApplicationTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_template_id):
            query['ApplicationTemplateId'] = request.application_template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApplicationTemplate',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApplicationTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_application_template(
        self,
        request: main_models.GetApplicationTemplateRequest,
    ) -> main_models.GetApplicationTemplateResponse:
        runtime = RuntimeOptions()
        return self.get_application_template_with_options(request, runtime)

    async def get_application_template_async(
        self,
        request: main_models.GetApplicationTemplateRequest,
    ) -> main_models.GetApplicationTemplateResponse:
        runtime = RuntimeOptions()
        return await self.get_application_template_with_options_async(request, runtime)

    def get_brand_with_options(
        self,
        request: main_models.GetBrandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBrandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.brand_id):
            query['BrandId'] = request.brand_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBrand',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBrandResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_brand_with_options_async(
        self,
        request: main_models.GetBrandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBrandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.brand_id):
            query['BrandId'] = request.brand_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBrand',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBrandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_brand(
        self,
        request: main_models.GetBrandRequest,
    ) -> main_models.GetBrandResponse:
        runtime = RuntimeOptions()
        return self.get_brand_with_options(request, runtime)

    async def get_brand_async(
        self,
        request: main_models.GetBrandRequest,
    ) -> main_models.GetBrandResponse:
        runtime = RuntimeOptions()
        return await self.get_brand_with_options_async(request, runtime)

    def get_client_public_key_with_options(
        self,
        request: main_models.GetClientPublicKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetClientPublicKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.client_public_key_id):
            query['ClientPublicKeyId'] = request.client_public_key_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetClientPublicKey',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetClientPublicKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_client_public_key_with_options_async(
        self,
        request: main_models.GetClientPublicKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetClientPublicKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.client_public_key_id):
            query['ClientPublicKeyId'] = request.client_public_key_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetClientPublicKey',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetClientPublicKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_client_public_key(
        self,
        request: main_models.GetClientPublicKeyRequest,
    ) -> main_models.GetClientPublicKeyResponse:
        runtime = RuntimeOptions()
        return self.get_client_public_key_with_options(request, runtime)

    async def get_client_public_key_async(
        self,
        request: main_models.GetClientPublicKeyRequest,
    ) -> main_models.GetClientPublicKeyResponse:
        runtime = RuntimeOptions()
        return await self.get_client_public_key_with_options_async(request, runtime)

    def get_cloud_account_with_options(
        self,
        request: main_models.GetCloudAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCloudAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cloud_account_id):
            query['CloudAccountId'] = request.cloud_account_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCloudAccount',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCloudAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cloud_account_with_options_async(
        self,
        request: main_models.GetCloudAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCloudAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cloud_account_id):
            query['CloudAccountId'] = request.cloud_account_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCloudAccount',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCloudAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cloud_account(
        self,
        request: main_models.GetCloudAccountRequest,
    ) -> main_models.GetCloudAccountResponse:
        runtime = RuntimeOptions()
        return self.get_cloud_account_with_options(request, runtime)

    async def get_cloud_account_async(
        self,
        request: main_models.GetCloudAccountRequest,
    ) -> main_models.GetCloudAccountResponse:
        runtime = RuntimeOptions()
        return await self.get_cloud_account_with_options_async(request, runtime)

    def get_cloud_account_role_with_options(
        self,
        request: main_models.GetCloudAccountRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCloudAccountRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cloud_account_id):
            query['CloudAccountId'] = request.cloud_account_id
        if not DaraCore.is_null(request.cloud_account_role_id):
            query['CloudAccountRoleId'] = request.cloud_account_role_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCloudAccountRole',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCloudAccountRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cloud_account_role_with_options_async(
        self,
        request: main_models.GetCloudAccountRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCloudAccountRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cloud_account_id):
            query['CloudAccountId'] = request.cloud_account_id
        if not DaraCore.is_null(request.cloud_account_role_id):
            query['CloudAccountRoleId'] = request.cloud_account_role_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCloudAccountRole',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCloudAccountRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cloud_account_role(
        self,
        request: main_models.GetCloudAccountRoleRequest,
    ) -> main_models.GetCloudAccountRoleResponse:
        runtime = RuntimeOptions()
        return self.get_cloud_account_role_with_options(request, runtime)

    async def get_cloud_account_role_async(
        self,
        request: main_models.GetCloudAccountRoleRequest,
    ) -> main_models.GetCloudAccountRoleResponse:
        runtime = RuntimeOptions()
        return await self.get_cloud_account_role_with_options_async(request, runtime)

    def get_conditional_access_policy_with_options(
        self,
        request: main_models.GetConditionalAccessPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetConditionalAccessPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.conditional_access_policy_id):
            query['ConditionalAccessPolicyId'] = request.conditional_access_policy_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetConditionalAccessPolicy',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConditionalAccessPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_conditional_access_policy_with_options_async(
        self,
        request: main_models.GetConditionalAccessPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetConditionalAccessPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.conditional_access_policy_id):
            query['ConditionalAccessPolicyId'] = request.conditional_access_policy_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetConditionalAccessPolicy',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConditionalAccessPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_conditional_access_policy(
        self,
        request: main_models.GetConditionalAccessPolicyRequest,
    ) -> main_models.GetConditionalAccessPolicyResponse:
        runtime = RuntimeOptions()
        return self.get_conditional_access_policy_with_options(request, runtime)

    async def get_conditional_access_policy_async(
        self,
        request: main_models.GetConditionalAccessPolicyRequest,
    ) -> main_models.GetConditionalAccessPolicyResponse:
        runtime = RuntimeOptions()
        return await self.get_conditional_access_policy_with_options_async(request, runtime)

    def get_custom_privacy_policy_with_options(
        self,
        request: main_models.GetCustomPrivacyPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCustomPrivacyPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.custom_privacy_policy_id):
            query['CustomPrivacyPolicyId'] = request.custom_privacy_policy_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCustomPrivacyPolicy',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCustomPrivacyPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_custom_privacy_policy_with_options_async(
        self,
        request: main_models.GetCustomPrivacyPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCustomPrivacyPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.custom_privacy_policy_id):
            query['CustomPrivacyPolicyId'] = request.custom_privacy_policy_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCustomPrivacyPolicy',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCustomPrivacyPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_custom_privacy_policy(
        self,
        request: main_models.GetCustomPrivacyPolicyRequest,
    ) -> main_models.GetCustomPrivacyPolicyResponse:
        runtime = RuntimeOptions()
        return self.get_custom_privacy_policy_with_options(request, runtime)

    async def get_custom_privacy_policy_async(
        self,
        request: main_models.GetCustomPrivacyPolicyRequest,
    ) -> main_models.GetCustomPrivacyPolicyResponse:
        runtime = RuntimeOptions()
        return await self.get_custom_privacy_policy_with_options_async(request, runtime)

    def get_domain_with_options(
        self,
        request: main_models.GetDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_id):
            query['DomainId'] = request.domain_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDomain',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_domain_with_options_async(
        self,
        request: main_models.GetDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_id):
            query['DomainId'] = request.domain_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDomain',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_domain(
        self,
        request: main_models.GetDomainRequest,
    ) -> main_models.GetDomainResponse:
        runtime = RuntimeOptions()
        return self.get_domain_with_options(request, runtime)

    async def get_domain_async(
        self,
        request: main_models.GetDomainRequest,
    ) -> main_models.GetDomainResponse:
        runtime = RuntimeOptions()
        return await self.get_domain_with_options_async(request, runtime)

    def get_domain_dns_challenge_with_options(
        self,
        request: main_models.GetDomainDnsChallengeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDomainDnsChallengeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDomainDnsChallenge',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDomainDnsChallengeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_domain_dns_challenge_with_options_async(
        self,
        request: main_models.GetDomainDnsChallengeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDomainDnsChallengeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDomainDnsChallenge',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDomainDnsChallengeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_domain_dns_challenge(
        self,
        request: main_models.GetDomainDnsChallengeRequest,
    ) -> main_models.GetDomainDnsChallengeResponse:
        runtime = RuntimeOptions()
        return self.get_domain_dns_challenge_with_options(request, runtime)

    async def get_domain_dns_challenge_async(
        self,
        request: main_models.GetDomainDnsChallengeRequest,
    ) -> main_models.GetDomainDnsChallengeResponse:
        runtime = RuntimeOptions()
        return await self.get_domain_dns_challenge_with_options_async(request, runtime)

    def get_federated_credential_provider_with_options(
        self,
        request: main_models.GetFederatedCredentialProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFederatedCredentialProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.federated_credential_provider_id):
            query['FederatedCredentialProviderId'] = request.federated_credential_provider_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetFederatedCredentialProvider',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFederatedCredentialProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_federated_credential_provider_with_options_async(
        self,
        request: main_models.GetFederatedCredentialProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFederatedCredentialProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.federated_credential_provider_id):
            query['FederatedCredentialProviderId'] = request.federated_credential_provider_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetFederatedCredentialProvider',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFederatedCredentialProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_federated_credential_provider(
        self,
        request: main_models.GetFederatedCredentialProviderRequest,
    ) -> main_models.GetFederatedCredentialProviderResponse:
        runtime = RuntimeOptions()
        return self.get_federated_credential_provider_with_options(request, runtime)

    async def get_federated_credential_provider_async(
        self,
        request: main_models.GetFederatedCredentialProviderRequest,
    ) -> main_models.GetFederatedCredentialProviderResponse:
        runtime = RuntimeOptions()
        return await self.get_federated_credential_provider_with_options_async(request, runtime)

    def get_forget_password_configuration_with_options(
        self,
        request: main_models.GetForgetPasswordConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetForgetPasswordConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetForgetPasswordConfiguration',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetForgetPasswordConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_forget_password_configuration_with_options_async(
        self,
        request: main_models.GetForgetPasswordConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetForgetPasswordConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetForgetPasswordConfiguration',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetForgetPasswordConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_forget_password_configuration(
        self,
        request: main_models.GetForgetPasswordConfigurationRequest,
    ) -> main_models.GetForgetPasswordConfigurationResponse:
        runtime = RuntimeOptions()
        return self.get_forget_password_configuration_with_options(request, runtime)

    async def get_forget_password_configuration_async(
        self,
        request: main_models.GetForgetPasswordConfigurationRequest,
    ) -> main_models.GetForgetPasswordConfigurationResponse:
        runtime = RuntimeOptions()
        return await self.get_forget_password_configuration_with_options_async(request, runtime)

    def get_group_with_options(
        self,
        request: main_models.GetGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetGroup',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_group_with_options_async(
        self,
        request: main_models.GetGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetGroup',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_group(
        self,
        request: main_models.GetGroupRequest,
    ) -> main_models.GetGroupResponse:
        runtime = RuntimeOptions()
        return self.get_group_with_options(request, runtime)

    async def get_group_async(
        self,
        request: main_models.GetGroupRequest,
    ) -> main_models.GetGroupResponse:
        runtime = RuntimeOptions()
        return await self.get_group_with_options_async(request, runtime)

    def get_identity_provider_with_options(
        self,
        request: main_models.GetIdentityProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetIdentityProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identity_provider_id):
            query['IdentityProviderId'] = request.identity_provider_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetIdentityProvider',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIdentityProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_identity_provider_with_options_async(
        self,
        request: main_models.GetIdentityProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetIdentityProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identity_provider_id):
            query['IdentityProviderId'] = request.identity_provider_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetIdentityProvider',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIdentityProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_identity_provider(
        self,
        request: main_models.GetIdentityProviderRequest,
    ) -> main_models.GetIdentityProviderResponse:
        runtime = RuntimeOptions()
        return self.get_identity_provider_with_options(request, runtime)

    async def get_identity_provider_async(
        self,
        request: main_models.GetIdentityProviderRequest,
    ) -> main_models.GetIdentityProviderResponse:
        runtime = RuntimeOptions()
        return await self.get_identity_provider_with_options_async(request, runtime)

    def get_identity_provider_ud_pull_configuration_with_options(
        self,
        request: main_models.GetIdentityProviderUdPullConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetIdentityProviderUdPullConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identity_provider_id):
            query['IdentityProviderId'] = request.identity_provider_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetIdentityProviderUdPullConfiguration',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIdentityProviderUdPullConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_identity_provider_ud_pull_configuration_with_options_async(
        self,
        request: main_models.GetIdentityProviderUdPullConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetIdentityProviderUdPullConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identity_provider_id):
            query['IdentityProviderId'] = request.identity_provider_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetIdentityProviderUdPullConfiguration',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIdentityProviderUdPullConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_identity_provider_ud_pull_configuration(
        self,
        request: main_models.GetIdentityProviderUdPullConfigurationRequest,
    ) -> main_models.GetIdentityProviderUdPullConfigurationResponse:
        runtime = RuntimeOptions()
        return self.get_identity_provider_ud_pull_configuration_with_options(request, runtime)

    async def get_identity_provider_ud_pull_configuration_async(
        self,
        request: main_models.GetIdentityProviderUdPullConfigurationRequest,
    ) -> main_models.GetIdentityProviderUdPullConfigurationResponse:
        runtime = RuntimeOptions()
        return await self.get_identity_provider_ud_pull_configuration_with_options_async(request, runtime)

    def get_instance_with_options(
        self,
        request: main_models.GetInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstance',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_with_options_async(
        self,
        request: main_models.GetInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstance',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance(
        self,
        request: main_models.GetInstanceRequest,
    ) -> main_models.GetInstanceResponse:
        runtime = RuntimeOptions()
        return self.get_instance_with_options(request, runtime)

    async def get_instance_async(
        self,
        request: main_models.GetInstanceRequest,
    ) -> main_models.GetInstanceResponse:
        runtime = RuntimeOptions()
        return await self.get_instance_with_options_async(request, runtime)

    def get_instance_license_with_options(
        self,
        request: main_models.GetInstanceLicenseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceLicenseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceLicense',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceLicenseResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_license_with_options_async(
        self,
        request: main_models.GetInstanceLicenseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceLicenseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceLicense',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceLicenseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_license(
        self,
        request: main_models.GetInstanceLicenseRequest,
    ) -> main_models.GetInstanceLicenseResponse:
        runtime = RuntimeOptions()
        return self.get_instance_license_with_options(request, runtime)

    async def get_instance_license_async(
        self,
        request: main_models.GetInstanceLicenseRequest,
    ) -> main_models.GetInstanceLicenseResponse:
        runtime = RuntimeOptions()
        return await self.get_instance_license_with_options_async(request, runtime)

    def get_login_redirect_application_for_brand_with_options(
        self,
        request: main_models.GetLoginRedirectApplicationForBrandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLoginRedirectApplicationForBrandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.brand_id):
            query['BrandId'] = request.brand_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLoginRedirectApplicationForBrand',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLoginRedirectApplicationForBrandResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_login_redirect_application_for_brand_with_options_async(
        self,
        request: main_models.GetLoginRedirectApplicationForBrandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLoginRedirectApplicationForBrandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.brand_id):
            query['BrandId'] = request.brand_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLoginRedirectApplicationForBrand',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLoginRedirectApplicationForBrandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_login_redirect_application_for_brand(
        self,
        request: main_models.GetLoginRedirectApplicationForBrandRequest,
    ) -> main_models.GetLoginRedirectApplicationForBrandResponse:
        runtime = RuntimeOptions()
        return self.get_login_redirect_application_for_brand_with_options(request, runtime)

    async def get_login_redirect_application_for_brand_async(
        self,
        request: main_models.GetLoginRedirectApplicationForBrandRequest,
    ) -> main_models.GetLoginRedirectApplicationForBrandResponse:
        runtime = RuntimeOptions()
        return await self.get_login_redirect_application_for_brand_with_options_async(request, runtime)

    def get_network_access_endpoint_with_options(
        self,
        request: main_models.GetNetworkAccessEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNetworkAccessEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.network_access_endpoint_id):
            query['NetworkAccessEndpointId'] = request.network_access_endpoint_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetNetworkAccessEndpoint',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNetworkAccessEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_network_access_endpoint_with_options_async(
        self,
        request: main_models.GetNetworkAccessEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNetworkAccessEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.network_access_endpoint_id):
            query['NetworkAccessEndpointId'] = request.network_access_endpoint_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetNetworkAccessEndpoint',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNetworkAccessEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_network_access_endpoint(
        self,
        request: main_models.GetNetworkAccessEndpointRequest,
    ) -> main_models.GetNetworkAccessEndpointResponse:
        runtime = RuntimeOptions()
        return self.get_network_access_endpoint_with_options(request, runtime)

    async def get_network_access_endpoint_async(
        self,
        request: main_models.GetNetworkAccessEndpointRequest,
    ) -> main_models.GetNetworkAccessEndpointResponse:
        runtime = RuntimeOptions()
        return await self.get_network_access_endpoint_with_options_async(request, runtime)

    def get_network_zone_with_options(
        self,
        request: main_models.GetNetworkZoneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNetworkZoneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.network_zone_id):
            query['NetworkZoneId'] = request.network_zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetNetworkZone',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNetworkZoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_network_zone_with_options_async(
        self,
        request: main_models.GetNetworkZoneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNetworkZoneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.network_zone_id):
            query['NetworkZoneId'] = request.network_zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetNetworkZone',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNetworkZoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_network_zone(
        self,
        request: main_models.GetNetworkZoneRequest,
    ) -> main_models.GetNetworkZoneResponse:
        runtime = RuntimeOptions()
        return self.get_network_zone_with_options(request, runtime)

    async def get_network_zone_async(
        self,
        request: main_models.GetNetworkZoneRequest,
    ) -> main_models.GetNetworkZoneResponse:
        runtime = RuntimeOptions()
        return await self.get_network_zone_with_options_async(request, runtime)

    def get_organizational_unit_with_options(
        self,
        request: main_models.GetOrganizationalUnitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOrganizationalUnitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.organizational_unit_id):
            query['OrganizationalUnitId'] = request.organizational_unit_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOrganizationalUnit',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOrganizationalUnitResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_organizational_unit_with_options_async(
        self,
        request: main_models.GetOrganizationalUnitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOrganizationalUnitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.organizational_unit_id):
            query['OrganizationalUnitId'] = request.organizational_unit_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOrganizationalUnit',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOrganizationalUnitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_organizational_unit(
        self,
        request: main_models.GetOrganizationalUnitRequest,
    ) -> main_models.GetOrganizationalUnitResponse:
        runtime = RuntimeOptions()
        return self.get_organizational_unit_with_options(request, runtime)

    async def get_organizational_unit_async(
        self,
        request: main_models.GetOrganizationalUnitRequest,
    ) -> main_models.GetOrganizationalUnitResponse:
        runtime = RuntimeOptions()
        return await self.get_organizational_unit_with_options_async(request, runtime)

    def get_password_complexity_configuration_with_options(
        self,
        request: main_models.GetPasswordComplexityConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPasswordComplexityConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPasswordComplexityConfiguration',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPasswordComplexityConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_password_complexity_configuration_with_options_async(
        self,
        request: main_models.GetPasswordComplexityConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPasswordComplexityConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPasswordComplexityConfiguration',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPasswordComplexityConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_password_complexity_configuration(
        self,
        request: main_models.GetPasswordComplexityConfigurationRequest,
    ) -> main_models.GetPasswordComplexityConfigurationResponse:
        runtime = RuntimeOptions()
        return self.get_password_complexity_configuration_with_options(request, runtime)

    async def get_password_complexity_configuration_async(
        self,
        request: main_models.GetPasswordComplexityConfigurationRequest,
    ) -> main_models.GetPasswordComplexityConfigurationResponse:
        runtime = RuntimeOptions()
        return await self.get_password_complexity_configuration_with_options_async(request, runtime)

    def get_password_expiration_configuration_with_options(
        self,
        request: main_models.GetPasswordExpirationConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPasswordExpirationConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPasswordExpirationConfiguration',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPasswordExpirationConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_password_expiration_configuration_with_options_async(
        self,
        request: main_models.GetPasswordExpirationConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPasswordExpirationConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPasswordExpirationConfiguration',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPasswordExpirationConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_password_expiration_configuration(
        self,
        request: main_models.GetPasswordExpirationConfigurationRequest,
    ) -> main_models.GetPasswordExpirationConfigurationResponse:
        runtime = RuntimeOptions()
        return self.get_password_expiration_configuration_with_options(request, runtime)

    async def get_password_expiration_configuration_async(
        self,
        request: main_models.GetPasswordExpirationConfigurationRequest,
    ) -> main_models.GetPasswordExpirationConfigurationResponse:
        runtime = RuntimeOptions()
        return await self.get_password_expiration_configuration_with_options_async(request, runtime)

    def get_password_history_configuration_with_options(
        self,
        request: main_models.GetPasswordHistoryConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPasswordHistoryConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPasswordHistoryConfiguration',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPasswordHistoryConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_password_history_configuration_with_options_async(
        self,
        request: main_models.GetPasswordHistoryConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPasswordHistoryConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPasswordHistoryConfiguration',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPasswordHistoryConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_password_history_configuration(
        self,
        request: main_models.GetPasswordHistoryConfigurationRequest,
    ) -> main_models.GetPasswordHistoryConfigurationResponse:
        runtime = RuntimeOptions()
        return self.get_password_history_configuration_with_options(request, runtime)

    async def get_password_history_configuration_async(
        self,
        request: main_models.GetPasswordHistoryConfigurationRequest,
    ) -> main_models.GetPasswordHistoryConfigurationResponse:
        runtime = RuntimeOptions()
        return await self.get_password_history_configuration_with_options_async(request, runtime)

    def get_password_initialization_configuration_with_options(
        self,
        request: main_models.GetPasswordInitializationConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPasswordInitializationConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPasswordInitializationConfiguration',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPasswordInitializationConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_password_initialization_configuration_with_options_async(
        self,
        request: main_models.GetPasswordInitializationConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPasswordInitializationConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPasswordInitializationConfiguration',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPasswordInitializationConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_password_initialization_configuration(
        self,
        request: main_models.GetPasswordInitializationConfigurationRequest,
    ) -> main_models.GetPasswordInitializationConfigurationResponse:
        runtime = RuntimeOptions()
        return self.get_password_initialization_configuration_with_options(request, runtime)

    async def get_password_initialization_configuration_async(
        self,
        request: main_models.GetPasswordInitializationConfigurationRequest,
    ) -> main_models.GetPasswordInitializationConfigurationResponse:
        runtime = RuntimeOptions()
        return await self.get_password_initialization_configuration_with_options_async(request, runtime)

    def get_resource_server_scope_with_options(
        self,
        request: main_models.GetResourceServerScopeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceServerScopeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.resource_server_scope_id):
            query['ResourceServerScopeId'] = request.resource_server_scope_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceServerScope',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceServerScopeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_server_scope_with_options_async(
        self,
        request: main_models.GetResourceServerScopeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceServerScopeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.resource_server_scope_id):
            query['ResourceServerScopeId'] = request.resource_server_scope_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceServerScope',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceServerScopeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_server_scope(
        self,
        request: main_models.GetResourceServerScopeRequest,
    ) -> main_models.GetResourceServerScopeResponse:
        runtime = RuntimeOptions()
        return self.get_resource_server_scope_with_options(request, runtime)

    async def get_resource_server_scope_async(
        self,
        request: main_models.GetResourceServerScopeRequest,
    ) -> main_models.GetResourceServerScopeResponse:
        runtime = RuntimeOptions()
        return await self.get_resource_server_scope_with_options_async(request, runtime)

    def get_root_organizational_unit_with_options(
        self,
        request: main_models.GetRootOrganizationalUnitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRootOrganizationalUnitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRootOrganizationalUnit',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRootOrganizationalUnitResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_root_organizational_unit_with_options_async(
        self,
        request: main_models.GetRootOrganizationalUnitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRootOrganizationalUnitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRootOrganizationalUnit',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRootOrganizationalUnitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_root_organizational_unit(
        self,
        request: main_models.GetRootOrganizationalUnitRequest,
    ) -> main_models.GetRootOrganizationalUnitResponse:
        runtime = RuntimeOptions()
        return self.get_root_organizational_unit_with_options(request, runtime)

    async def get_root_organizational_unit_async(
        self,
        request: main_models.GetRootOrganizationalUnitRequest,
    ) -> main_models.GetRootOrganizationalUnitResponse:
        runtime = RuntimeOptions()
        return await self.get_root_organizational_unit_with_options_async(request, runtime)

    def get_synchronization_job_with_options(
        self,
        request: main_models.GetSynchronizationJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSynchronizationJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSynchronizationJob',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSynchronizationJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_synchronization_job_with_options_async(
        self,
        request: main_models.GetSynchronizationJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSynchronizationJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSynchronizationJob',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSynchronizationJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_synchronization_job(
        self,
        request: main_models.GetSynchronizationJobRequest,
    ) -> main_models.GetSynchronizationJobResponse:
        runtime = RuntimeOptions()
        return self.get_synchronization_job_with_options(request, runtime)

    async def get_synchronization_job_async(
        self,
        request: main_models.GetSynchronizationJobRequest,
    ) -> main_models.GetSynchronizationJobResponse:
        runtime = RuntimeOptions()
        return await self.get_synchronization_job_with_options_async(request, runtime)

    def get_user_with_options(
        self,
        request: main_models.GetUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUser',
            version = '2021-12-01',
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
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUser',
            version = '2021-12-01',
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

    def list_application_accounts_with_options(
        self,
        request: main_models.ListApplicationAccountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationAccountsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApplicationAccounts',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_application_accounts_with_options_async(
        self,
        request: main_models.ListApplicationAccountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationAccountsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApplicationAccounts',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_application_accounts(
        self,
        request: main_models.ListApplicationAccountsRequest,
    ) -> main_models.ListApplicationAccountsResponse:
        runtime = RuntimeOptions()
        return self.list_application_accounts_with_options(request, runtime)

    async def list_application_accounts_async(
        self,
        request: main_models.ListApplicationAccountsRequest,
    ) -> main_models.ListApplicationAccountsResponse:
        runtime = RuntimeOptions()
        return await self.list_application_accounts_with_options_async(request, runtime)

    def list_application_accounts_for_user_with_options(
        self,
        request: main_models.ListApplicationAccountsForUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationAccountsForUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApplicationAccountsForUser',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationAccountsForUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_application_accounts_for_user_with_options_async(
        self,
        request: main_models.ListApplicationAccountsForUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationAccountsForUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApplicationAccountsForUser',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationAccountsForUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_application_accounts_for_user(
        self,
        request: main_models.ListApplicationAccountsForUserRequest,
    ) -> main_models.ListApplicationAccountsForUserResponse:
        runtime = RuntimeOptions()
        return self.list_application_accounts_for_user_with_options(request, runtime)

    async def list_application_accounts_for_user_async(
        self,
        request: main_models.ListApplicationAccountsForUserRequest,
    ) -> main_models.ListApplicationAccountsForUserResponse:
        runtime = RuntimeOptions()
        return await self.list_application_accounts_for_user_with_options_async(request, runtime)

    def list_application_client_secrets_with_options(
        self,
        request: main_models.ListApplicationClientSecretsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationClientSecretsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApplicationClientSecrets',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationClientSecretsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_application_client_secrets_with_options_async(
        self,
        request: main_models.ListApplicationClientSecretsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationClientSecretsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApplicationClientSecrets',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationClientSecretsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_application_client_secrets(
        self,
        request: main_models.ListApplicationClientSecretsRequest,
    ) -> main_models.ListApplicationClientSecretsResponse:
        runtime = RuntimeOptions()
        return self.list_application_client_secrets_with_options(request, runtime)

    async def list_application_client_secrets_async(
        self,
        request: main_models.ListApplicationClientSecretsRequest,
    ) -> main_models.ListApplicationClientSecretsResponse:
        runtime = RuntimeOptions()
        return await self.list_application_client_secrets_with_options_async(request, runtime)

    def list_application_federated_credentials_with_options(
        self,
        request: main_models.ListApplicationFederatedCredentialsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationFederatedCredentialsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_federated_credential_type):
            query['ApplicationFederatedCredentialType'] = request.application_federated_credential_type
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.previous_token):
            query['PreviousToken'] = request.previous_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApplicationFederatedCredentials',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationFederatedCredentialsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_application_federated_credentials_with_options_async(
        self,
        request: main_models.ListApplicationFederatedCredentialsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationFederatedCredentialsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_federated_credential_type):
            query['ApplicationFederatedCredentialType'] = request.application_federated_credential_type
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.previous_token):
            query['PreviousToken'] = request.previous_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApplicationFederatedCredentials',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationFederatedCredentialsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_application_federated_credentials(
        self,
        request: main_models.ListApplicationFederatedCredentialsRequest,
    ) -> main_models.ListApplicationFederatedCredentialsResponse:
        runtime = RuntimeOptions()
        return self.list_application_federated_credentials_with_options(request, runtime)

    async def list_application_federated_credentials_async(
        self,
        request: main_models.ListApplicationFederatedCredentialsRequest,
    ) -> main_models.ListApplicationFederatedCredentialsResponse:
        runtime = RuntimeOptions()
        return await self.list_application_federated_credentials_with_options_async(request, runtime)

    def list_application_federated_credentials_for_provider_with_options(
        self,
        request: main_models.ListApplicationFederatedCredentialsForProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationFederatedCredentialsForProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.federated_credential_provider_id):
            query['FederatedCredentialProviderId'] = request.federated_credential_provider_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.previous_token):
            query['PreviousToken'] = request.previous_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApplicationFederatedCredentialsForProvider',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationFederatedCredentialsForProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_application_federated_credentials_for_provider_with_options_async(
        self,
        request: main_models.ListApplicationFederatedCredentialsForProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationFederatedCredentialsForProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.federated_credential_provider_id):
            query['FederatedCredentialProviderId'] = request.federated_credential_provider_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.previous_token):
            query['PreviousToken'] = request.previous_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApplicationFederatedCredentialsForProvider',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationFederatedCredentialsForProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_application_federated_credentials_for_provider(
        self,
        request: main_models.ListApplicationFederatedCredentialsForProviderRequest,
    ) -> main_models.ListApplicationFederatedCredentialsForProviderResponse:
        runtime = RuntimeOptions()
        return self.list_application_federated_credentials_for_provider_with_options(request, runtime)

    async def list_application_federated_credentials_for_provider_async(
        self,
        request: main_models.ListApplicationFederatedCredentialsForProviderRequest,
    ) -> main_models.ListApplicationFederatedCredentialsForProviderResponse:
        runtime = RuntimeOptions()
        return await self.list_application_federated_credentials_for_provider_with_options_async(request, runtime)

    def list_application_roles_with_options(
        self,
        request: main_models.ListApplicationRolesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationRolesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApplicationRoles',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationRolesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_application_roles_with_options_async(
        self,
        request: main_models.ListApplicationRolesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationRolesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApplicationRoles',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationRolesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_application_roles(
        self,
        request: main_models.ListApplicationRolesRequest,
    ) -> main_models.ListApplicationRolesResponse:
        runtime = RuntimeOptions()
        return self.list_application_roles_with_options(request, runtime)

    async def list_application_roles_async(
        self,
        request: main_models.ListApplicationRolesRequest,
    ) -> main_models.ListApplicationRolesResponse:
        runtime = RuntimeOptions()
        return await self.list_application_roles_with_options_async(request, runtime)

    def list_application_supported_provision_protocol_types_with_options(
        self,
        request: main_models.ListApplicationSupportedProvisionProtocolTypesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationSupportedProvisionProtocolTypesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApplicationSupportedProvisionProtocolTypes',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationSupportedProvisionProtocolTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_application_supported_provision_protocol_types_with_options_async(
        self,
        request: main_models.ListApplicationSupportedProvisionProtocolTypesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationSupportedProvisionProtocolTypesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApplicationSupportedProvisionProtocolTypes',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationSupportedProvisionProtocolTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_application_supported_provision_protocol_types(
        self,
        request: main_models.ListApplicationSupportedProvisionProtocolTypesRequest,
    ) -> main_models.ListApplicationSupportedProvisionProtocolTypesResponse:
        runtime = RuntimeOptions()
        return self.list_application_supported_provision_protocol_types_with_options(request, runtime)

    async def list_application_supported_provision_protocol_types_async(
        self,
        request: main_models.ListApplicationSupportedProvisionProtocolTypesRequest,
    ) -> main_models.ListApplicationSupportedProvisionProtocolTypesResponse:
        runtime = RuntimeOptions()
        return await self.list_application_supported_provision_protocol_types_with_options_async(request, runtime)

    def list_application_tokens_with_options(
        self,
        request: main_models.ListApplicationTokensRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationTokensResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.application_token_type):
            query['ApplicationTokenType'] = request.application_token_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApplicationTokens',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationTokensResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_application_tokens_with_options_async(
        self,
        request: main_models.ListApplicationTokensRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationTokensResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.application_token_type):
            query['ApplicationTokenType'] = request.application_token_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApplicationTokens',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationTokensResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_application_tokens(
        self,
        request: main_models.ListApplicationTokensRequest,
    ) -> main_models.ListApplicationTokensResponse:
        runtime = RuntimeOptions()
        return self.list_application_tokens_with_options(request, runtime)

    async def list_application_tokens_async(
        self,
        request: main_models.ListApplicationTokensRequest,
    ) -> main_models.ListApplicationTokensResponse:
        runtime = RuntimeOptions()
        return await self.list_application_tokens_with_options_async(request, runtime)

    def list_applications_with_options(
        self,
        request: main_models.ListApplicationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_creation_type):
            query['ApplicationCreationType'] = request.application_creation_type
        if not DaraCore.is_null(request.application_ids):
            query['ApplicationIds'] = request.application_ids
        if not DaraCore.is_null(request.application_name):
            query['ApplicationName'] = request.application_name
        if not DaraCore.is_null(request.authorization_type):
            query['AuthorizationType'] = request.authorization_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.m_2mclient_status):
            query['M2MClientStatus'] = request.m_2mclient_status
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_server_status):
            query['ResourceServerStatus'] = request.resource_server_status
        if not DaraCore.is_null(request.sso_type):
            query['SsoType'] = request.sso_type
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApplications',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_applications_with_options_async(
        self,
        request: main_models.ListApplicationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_creation_type):
            query['ApplicationCreationType'] = request.application_creation_type
        if not DaraCore.is_null(request.application_ids):
            query['ApplicationIds'] = request.application_ids
        if not DaraCore.is_null(request.application_name):
            query['ApplicationName'] = request.application_name
        if not DaraCore.is_null(request.authorization_type):
            query['AuthorizationType'] = request.authorization_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.m_2mclient_status):
            query['M2MClientStatus'] = request.m_2mclient_status
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_server_status):
            query['ResourceServerStatus'] = request.resource_server_status
        if not DaraCore.is_null(request.sso_type):
            query['SsoType'] = request.sso_type
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApplications',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_applications(
        self,
        request: main_models.ListApplicationsRequest,
    ) -> main_models.ListApplicationsResponse:
        runtime = RuntimeOptions()
        return self.list_applications_with_options(request, runtime)

    async def list_applications_async(
        self,
        request: main_models.ListApplicationsRequest,
    ) -> main_models.ListApplicationsResponse:
        runtime = RuntimeOptions()
        return await self.list_applications_with_options_async(request, runtime)

    def list_applications_for_group_with_options(
        self,
        request: main_models.ListApplicationsForGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationsForGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_ids):
            query['ApplicationIds'] = request.application_ids
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApplicationsForGroup',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationsForGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_applications_for_group_with_options_async(
        self,
        request: main_models.ListApplicationsForGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationsForGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_ids):
            query['ApplicationIds'] = request.application_ids
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApplicationsForGroup',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationsForGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_applications_for_group(
        self,
        request: main_models.ListApplicationsForGroupRequest,
    ) -> main_models.ListApplicationsForGroupResponse:
        runtime = RuntimeOptions()
        return self.list_applications_for_group_with_options(request, runtime)

    async def list_applications_for_group_async(
        self,
        request: main_models.ListApplicationsForGroupRequest,
    ) -> main_models.ListApplicationsForGroupResponse:
        runtime = RuntimeOptions()
        return await self.list_applications_for_group_with_options_async(request, runtime)

    def list_applications_for_network_access_endpoint_with_options(
        self,
        request: main_models.ListApplicationsForNetworkAccessEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationsForNetworkAccessEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.network_access_endpoint_id):
            query['NetworkAccessEndpointId'] = request.network_access_endpoint_id
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApplicationsForNetworkAccessEndpoint',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationsForNetworkAccessEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_applications_for_network_access_endpoint_with_options_async(
        self,
        request: main_models.ListApplicationsForNetworkAccessEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationsForNetworkAccessEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.network_access_endpoint_id):
            query['NetworkAccessEndpointId'] = request.network_access_endpoint_id
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApplicationsForNetworkAccessEndpoint',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationsForNetworkAccessEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_applications_for_network_access_endpoint(
        self,
        request: main_models.ListApplicationsForNetworkAccessEndpointRequest,
    ) -> main_models.ListApplicationsForNetworkAccessEndpointResponse:
        runtime = RuntimeOptions()
        return self.list_applications_for_network_access_endpoint_with_options(request, runtime)

    async def list_applications_for_network_access_endpoint_async(
        self,
        request: main_models.ListApplicationsForNetworkAccessEndpointRequest,
    ) -> main_models.ListApplicationsForNetworkAccessEndpointResponse:
        runtime = RuntimeOptions()
        return await self.list_applications_for_network_access_endpoint_with_options_async(request, runtime)

    def list_applications_for_network_zone_with_options(
        self,
        request: main_models.ListApplicationsForNetworkZoneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationsForNetworkZoneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.network_zone_id):
            query['NetworkZoneId'] = request.network_zone_id
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.previous_token):
            query['PreviousToken'] = request.previous_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApplicationsForNetworkZone',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationsForNetworkZoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_applications_for_network_zone_with_options_async(
        self,
        request: main_models.ListApplicationsForNetworkZoneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationsForNetworkZoneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.network_zone_id):
            query['NetworkZoneId'] = request.network_zone_id
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.previous_token):
            query['PreviousToken'] = request.previous_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApplicationsForNetworkZone',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationsForNetworkZoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_applications_for_network_zone(
        self,
        request: main_models.ListApplicationsForNetworkZoneRequest,
    ) -> main_models.ListApplicationsForNetworkZoneResponse:
        runtime = RuntimeOptions()
        return self.list_applications_for_network_zone_with_options(request, runtime)

    async def list_applications_for_network_zone_async(
        self,
        request: main_models.ListApplicationsForNetworkZoneRequest,
    ) -> main_models.ListApplicationsForNetworkZoneResponse:
        runtime = RuntimeOptions()
        return await self.list_applications_for_network_zone_with_options_async(request, runtime)

    def list_applications_for_organizational_unit_with_options(
        self,
        request: main_models.ListApplicationsForOrganizationalUnitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationsForOrganizationalUnitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_ids):
            query['ApplicationIds'] = request.application_ids
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.organizational_unit_id):
            query['OrganizationalUnitId'] = request.organizational_unit_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApplicationsForOrganizationalUnit',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationsForOrganizationalUnitResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_applications_for_organizational_unit_with_options_async(
        self,
        request: main_models.ListApplicationsForOrganizationalUnitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationsForOrganizationalUnitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_ids):
            query['ApplicationIds'] = request.application_ids
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.organizational_unit_id):
            query['OrganizationalUnitId'] = request.organizational_unit_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApplicationsForOrganizationalUnit',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationsForOrganizationalUnitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_applications_for_organizational_unit(
        self,
        request: main_models.ListApplicationsForOrganizationalUnitRequest,
    ) -> main_models.ListApplicationsForOrganizationalUnitResponse:
        runtime = RuntimeOptions()
        return self.list_applications_for_organizational_unit_with_options(request, runtime)

    async def list_applications_for_organizational_unit_async(
        self,
        request: main_models.ListApplicationsForOrganizationalUnitRequest,
    ) -> main_models.ListApplicationsForOrganizationalUnitResponse:
        runtime = RuntimeOptions()
        return await self.list_applications_for_organizational_unit_with_options_async(request, runtime)

    def list_applications_for_user_with_options(
        self,
        request: main_models.ListApplicationsForUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationsForUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_ids):
            query['ApplicationIds'] = request.application_ids
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_mode):
            query['QueryMode'] = request.query_mode
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApplicationsForUser',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationsForUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_applications_for_user_with_options_async(
        self,
        request: main_models.ListApplicationsForUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationsForUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_ids):
            query['ApplicationIds'] = request.application_ids
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_mode):
            query['QueryMode'] = request.query_mode
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApplicationsForUser',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationsForUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_applications_for_user(
        self,
        request: main_models.ListApplicationsForUserRequest,
    ) -> main_models.ListApplicationsForUserResponse:
        runtime = RuntimeOptions()
        return self.list_applications_for_user_with_options(request, runtime)

    async def list_applications_for_user_async(
        self,
        request: main_models.ListApplicationsForUserRequest,
    ) -> main_models.ListApplicationsForUserResponse:
        runtime = RuntimeOptions()
        return await self.list_applications_for_user_with_options_async(request, runtime)

    def list_brands_with_options(
        self,
        request: main_models.ListBrandsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBrandsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.previous_token):
            query['PreviousToken'] = request.previous_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBrands',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBrandsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_brands_with_options_async(
        self,
        request: main_models.ListBrandsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBrandsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.previous_token):
            query['PreviousToken'] = request.previous_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBrands',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBrandsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_brands(
        self,
        request: main_models.ListBrandsRequest,
    ) -> main_models.ListBrandsResponse:
        runtime = RuntimeOptions()
        return self.list_brands_with_options(request, runtime)

    async def list_brands_async(
        self,
        request: main_models.ListBrandsRequest,
    ) -> main_models.ListBrandsResponse:
        runtime = RuntimeOptions()
        return await self.list_brands_with_options_async(request, runtime)

    def list_client_public_keys_with_options(
        self,
        request: main_models.ListClientPublicKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListClientPublicKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListClientPublicKeys',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListClientPublicKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_client_public_keys_with_options_async(
        self,
        request: main_models.ListClientPublicKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListClientPublicKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListClientPublicKeys',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListClientPublicKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_client_public_keys(
        self,
        request: main_models.ListClientPublicKeysRequest,
    ) -> main_models.ListClientPublicKeysResponse:
        runtime = RuntimeOptions()
        return self.list_client_public_keys_with_options(request, runtime)

    async def list_client_public_keys_async(
        self,
        request: main_models.ListClientPublicKeysRequest,
    ) -> main_models.ListClientPublicKeysResponse:
        runtime = RuntimeOptions()
        return await self.list_client_public_keys_with_options_async(request, runtime)

    def list_cloud_account_roles_with_options(
        self,
        request: main_models.ListCloudAccountRolesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCloudAccountRolesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cloud_account_id):
            query['CloudAccountId'] = request.cloud_account_id
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCloudAccountRoles',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCloudAccountRolesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cloud_account_roles_with_options_async(
        self,
        request: main_models.ListCloudAccountRolesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCloudAccountRolesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cloud_account_id):
            query['CloudAccountId'] = request.cloud_account_id
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCloudAccountRoles',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCloudAccountRolesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cloud_account_roles(
        self,
        request: main_models.ListCloudAccountRolesRequest,
    ) -> main_models.ListCloudAccountRolesResponse:
        runtime = RuntimeOptions()
        return self.list_cloud_account_roles_with_options(request, runtime)

    async def list_cloud_account_roles_async(
        self,
        request: main_models.ListCloudAccountRolesRequest,
    ) -> main_models.ListCloudAccountRolesResponse:
        runtime = RuntimeOptions()
        return await self.list_cloud_account_roles_with_options_async(request, runtime)

    def list_cloud_accounts_with_options(
        self,
        request: main_models.ListCloudAccountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCloudAccountsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCloudAccounts',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCloudAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cloud_accounts_with_options_async(
        self,
        request: main_models.ListCloudAccountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCloudAccountsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCloudAccounts',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCloudAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cloud_accounts(
        self,
        request: main_models.ListCloudAccountsRequest,
    ) -> main_models.ListCloudAccountsResponse:
        runtime = RuntimeOptions()
        return self.list_cloud_accounts_with_options(request, runtime)

    async def list_cloud_accounts_async(
        self,
        request: main_models.ListCloudAccountsRequest,
    ) -> main_models.ListCloudAccountsResponse:
        runtime = RuntimeOptions()
        return await self.list_cloud_accounts_with_options_async(request, runtime)

    def list_conditional_access_policies_with_options(
        self,
        request: main_models.ListConditionalAccessPoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListConditionalAccessPoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.previous_token):
            query['PreviousToken'] = request.previous_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConditionalAccessPolicies',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConditionalAccessPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_conditional_access_policies_with_options_async(
        self,
        request: main_models.ListConditionalAccessPoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListConditionalAccessPoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.previous_token):
            query['PreviousToken'] = request.previous_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConditionalAccessPolicies',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConditionalAccessPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_conditional_access_policies(
        self,
        request: main_models.ListConditionalAccessPoliciesRequest,
    ) -> main_models.ListConditionalAccessPoliciesResponse:
        runtime = RuntimeOptions()
        return self.list_conditional_access_policies_with_options(request, runtime)

    async def list_conditional_access_policies_async(
        self,
        request: main_models.ListConditionalAccessPoliciesRequest,
    ) -> main_models.ListConditionalAccessPoliciesResponse:
        runtime = RuntimeOptions()
        return await self.list_conditional_access_policies_with_options_async(request, runtime)

    def list_conditional_access_policies_for_application_with_options(
        self,
        request: main_models.ListConditionalAccessPoliciesForApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListConditionalAccessPoliciesForApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConditionalAccessPoliciesForApplication',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConditionalAccessPoliciesForApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_conditional_access_policies_for_application_with_options_async(
        self,
        request: main_models.ListConditionalAccessPoliciesForApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListConditionalAccessPoliciesForApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConditionalAccessPoliciesForApplication',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConditionalAccessPoliciesForApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_conditional_access_policies_for_application(
        self,
        request: main_models.ListConditionalAccessPoliciesForApplicationRequest,
    ) -> main_models.ListConditionalAccessPoliciesForApplicationResponse:
        runtime = RuntimeOptions()
        return self.list_conditional_access_policies_for_application_with_options(request, runtime)

    async def list_conditional_access_policies_for_application_async(
        self,
        request: main_models.ListConditionalAccessPoliciesForApplicationRequest,
    ) -> main_models.ListConditionalAccessPoliciesForApplicationResponse:
        runtime = RuntimeOptions()
        return await self.list_conditional_access_policies_for_application_with_options_async(request, runtime)

    def list_conditional_access_policies_for_network_zone_with_options(
        self,
        request: main_models.ListConditionalAccessPoliciesForNetworkZoneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListConditionalAccessPoliciesForNetworkZoneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.network_zone_id):
            query['NetworkZoneId'] = request.network_zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConditionalAccessPoliciesForNetworkZone',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConditionalAccessPoliciesForNetworkZoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_conditional_access_policies_for_network_zone_with_options_async(
        self,
        request: main_models.ListConditionalAccessPoliciesForNetworkZoneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListConditionalAccessPoliciesForNetworkZoneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.network_zone_id):
            query['NetworkZoneId'] = request.network_zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConditionalAccessPoliciesForNetworkZone',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConditionalAccessPoliciesForNetworkZoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_conditional_access_policies_for_network_zone(
        self,
        request: main_models.ListConditionalAccessPoliciesForNetworkZoneRequest,
    ) -> main_models.ListConditionalAccessPoliciesForNetworkZoneResponse:
        runtime = RuntimeOptions()
        return self.list_conditional_access_policies_for_network_zone_with_options(request, runtime)

    async def list_conditional_access_policies_for_network_zone_async(
        self,
        request: main_models.ListConditionalAccessPoliciesForNetworkZoneRequest,
    ) -> main_models.ListConditionalAccessPoliciesForNetworkZoneResponse:
        runtime = RuntimeOptions()
        return await self.list_conditional_access_policies_for_network_zone_with_options_async(request, runtime)

    def list_conditional_access_policies_for_user_with_options(
        self,
        request: main_models.ListConditionalAccessPoliciesForUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListConditionalAccessPoliciesForUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConditionalAccessPoliciesForUser',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConditionalAccessPoliciesForUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_conditional_access_policies_for_user_with_options_async(
        self,
        request: main_models.ListConditionalAccessPoliciesForUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListConditionalAccessPoliciesForUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConditionalAccessPoliciesForUser',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConditionalAccessPoliciesForUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_conditional_access_policies_for_user(
        self,
        request: main_models.ListConditionalAccessPoliciesForUserRequest,
    ) -> main_models.ListConditionalAccessPoliciesForUserResponse:
        runtime = RuntimeOptions()
        return self.list_conditional_access_policies_for_user_with_options(request, runtime)

    async def list_conditional_access_policies_for_user_async(
        self,
        request: main_models.ListConditionalAccessPoliciesForUserRequest,
    ) -> main_models.ListConditionalAccessPoliciesForUserResponse:
        runtime = RuntimeOptions()
        return await self.list_conditional_access_policies_for_user_with_options_async(request, runtime)

    def list_custom_privacy_policies_with_options(
        self,
        request: main_models.ListCustomPrivacyPoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCustomPrivacyPoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.custom_privacy_policy_name_starts_with):
            query['CustomPrivacyPolicyNameStartsWith'] = request.custom_privacy_policy_name_starts_with
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.previous_token):
            query['PreviousToken'] = request.previous_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCustomPrivacyPolicies',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCustomPrivacyPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_custom_privacy_policies_with_options_async(
        self,
        request: main_models.ListCustomPrivacyPoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCustomPrivacyPoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.custom_privacy_policy_name_starts_with):
            query['CustomPrivacyPolicyNameStartsWith'] = request.custom_privacy_policy_name_starts_with
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.previous_token):
            query['PreviousToken'] = request.previous_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCustomPrivacyPolicies',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCustomPrivacyPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_custom_privacy_policies(
        self,
        request: main_models.ListCustomPrivacyPoliciesRequest,
    ) -> main_models.ListCustomPrivacyPoliciesResponse:
        runtime = RuntimeOptions()
        return self.list_custom_privacy_policies_with_options(request, runtime)

    async def list_custom_privacy_policies_async(
        self,
        request: main_models.ListCustomPrivacyPoliciesRequest,
    ) -> main_models.ListCustomPrivacyPoliciesResponse:
        runtime = RuntimeOptions()
        return await self.list_custom_privacy_policies_with_options_async(request, runtime)

    def list_custom_privacy_policies_for_brand_with_options(
        self,
        request: main_models.ListCustomPrivacyPoliciesForBrandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCustomPrivacyPoliciesForBrandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.brand_id):
            query['BrandId'] = request.brand_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.previous_token):
            query['PreviousToken'] = request.previous_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCustomPrivacyPoliciesForBrand',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCustomPrivacyPoliciesForBrandResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_custom_privacy_policies_for_brand_with_options_async(
        self,
        request: main_models.ListCustomPrivacyPoliciesForBrandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCustomPrivacyPoliciesForBrandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.brand_id):
            query['BrandId'] = request.brand_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.previous_token):
            query['PreviousToken'] = request.previous_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCustomPrivacyPoliciesForBrand',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCustomPrivacyPoliciesForBrandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_custom_privacy_policies_for_brand(
        self,
        request: main_models.ListCustomPrivacyPoliciesForBrandRequest,
    ) -> main_models.ListCustomPrivacyPoliciesForBrandResponse:
        runtime = RuntimeOptions()
        return self.list_custom_privacy_policies_for_brand_with_options(request, runtime)

    async def list_custom_privacy_policies_for_brand_async(
        self,
        request: main_models.ListCustomPrivacyPoliciesForBrandRequest,
    ) -> main_models.ListCustomPrivacyPoliciesForBrandResponse:
        runtime = RuntimeOptions()
        return await self.list_custom_privacy_policies_for_brand_with_options_async(request, runtime)

    def list_domain_proxy_tokens_with_options(
        self,
        request: main_models.ListDomainProxyTokensRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDomainProxyTokensResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_id):
            query['DomainId'] = request.domain_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDomainProxyTokens',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDomainProxyTokensResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_domain_proxy_tokens_with_options_async(
        self,
        request: main_models.ListDomainProxyTokensRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDomainProxyTokensResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_id):
            query['DomainId'] = request.domain_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDomainProxyTokens',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDomainProxyTokensResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_domain_proxy_tokens(
        self,
        request: main_models.ListDomainProxyTokensRequest,
    ) -> main_models.ListDomainProxyTokensResponse:
        runtime = RuntimeOptions()
        return self.list_domain_proxy_tokens_with_options(request, runtime)

    async def list_domain_proxy_tokens_async(
        self,
        request: main_models.ListDomainProxyTokensRequest,
    ) -> main_models.ListDomainProxyTokensResponse:
        runtime = RuntimeOptions()
        return await self.list_domain_proxy_tokens_with_options_async(request, runtime)

    def list_domains_with_options(
        self,
        request: main_models.ListDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.brand_id):
            query['BrandId'] = request.brand_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDomains',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_domains_with_options_async(
        self,
        request: main_models.ListDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.brand_id):
            query['BrandId'] = request.brand_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDomains',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_domains(
        self,
        request: main_models.ListDomainsRequest,
    ) -> main_models.ListDomainsResponse:
        runtime = RuntimeOptions()
        return self.list_domains_with_options(request, runtime)

    async def list_domains_async(
        self,
        request: main_models.ListDomainsRequest,
    ) -> main_models.ListDomainsResponse:
        runtime = RuntimeOptions()
        return await self.list_domains_with_options_async(request, runtime)

    def list_eiam_instances_with_options(
        self,
        request: main_models.ListEiamInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEiamInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.instance_region_id):
            query['InstanceRegionId'] = request.instance_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEiamInstances',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEiamInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_eiam_instances_with_options_async(
        self,
        request: main_models.ListEiamInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEiamInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.instance_region_id):
            query['InstanceRegionId'] = request.instance_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEiamInstances',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEiamInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_eiam_instances(
        self,
        request: main_models.ListEiamInstancesRequest,
    ) -> main_models.ListEiamInstancesResponse:
        runtime = RuntimeOptions()
        return self.list_eiam_instances_with_options(request, runtime)

    async def list_eiam_instances_async(
        self,
        request: main_models.ListEiamInstancesRequest,
    ) -> main_models.ListEiamInstancesResponse:
        runtime = RuntimeOptions()
        return await self.list_eiam_instances_with_options_async(request, runtime)

    def list_eiam_regions_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListEiamRegionsResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListEiamRegions',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEiamRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_eiam_regions_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListEiamRegionsResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListEiamRegions',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEiamRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_eiam_regions(self) -> main_models.ListEiamRegionsResponse:
        runtime = RuntimeOptions()
        return self.list_eiam_regions_with_options(runtime)

    async def list_eiam_regions_async(self) -> main_models.ListEiamRegionsResponse:
        runtime = RuntimeOptions()
        return await self.list_eiam_regions_with_options_async(runtime)

    def list_federated_credential_providers_with_options(
        self,
        request: main_models.ListFederatedCredentialProvidersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFederatedCredentialProvidersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.federated_credential_provider_name):
            query['FederatedCredentialProviderName'] = request.federated_credential_provider_name
        if not DaraCore.is_null(request.federated_credential_provider_type):
            query['FederatedCredentialProviderType'] = request.federated_credential_provider_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.previous_token):
            query['PreviousToken'] = request.previous_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFederatedCredentialProviders',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFederatedCredentialProvidersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_federated_credential_providers_with_options_async(
        self,
        request: main_models.ListFederatedCredentialProvidersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFederatedCredentialProvidersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.federated_credential_provider_name):
            query['FederatedCredentialProviderName'] = request.federated_credential_provider_name
        if not DaraCore.is_null(request.federated_credential_provider_type):
            query['FederatedCredentialProviderType'] = request.federated_credential_provider_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.previous_token):
            query['PreviousToken'] = request.previous_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFederatedCredentialProviders',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFederatedCredentialProvidersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_federated_credential_providers(
        self,
        request: main_models.ListFederatedCredentialProvidersRequest,
    ) -> main_models.ListFederatedCredentialProvidersResponse:
        runtime = RuntimeOptions()
        return self.list_federated_credential_providers_with_options(request, runtime)

    async def list_federated_credential_providers_async(
        self,
        request: main_models.ListFederatedCredentialProvidersRequest,
    ) -> main_models.ListFederatedCredentialProvidersResponse:
        runtime = RuntimeOptions()
        return await self.list_federated_credential_providers_with_options_async(request, runtime)

    def list_groups_with_options(
        self,
        request: main_models.ListGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_external_id):
            query['GroupExternalId'] = request.group_external_id
        if not DaraCore.is_null(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.group_name_starts_with):
            query['GroupNameStartsWith'] = request.group_name_starts_with
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGroups',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_groups_with_options_async(
        self,
        request: main_models.ListGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_external_id):
            query['GroupExternalId'] = request.group_external_id
        if not DaraCore.is_null(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.group_name_starts_with):
            query['GroupNameStartsWith'] = request.group_name_starts_with
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGroups',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_groups(
        self,
        request: main_models.ListGroupsRequest,
    ) -> main_models.ListGroupsResponse:
        runtime = RuntimeOptions()
        return self.list_groups_with_options(request, runtime)

    async def list_groups_async(
        self,
        request: main_models.ListGroupsRequest,
    ) -> main_models.ListGroupsResponse:
        runtime = RuntimeOptions()
        return await self.list_groups_with_options_async(request, runtime)

    def list_groups_for_application_with_options(
        self,
        request: main_models.ListGroupsForApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGroupsForApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.application_role_id):
            query['ApplicationRoleId'] = request.application_role_id
        if not DaraCore.is_null(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGroupsForApplication',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGroupsForApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_groups_for_application_with_options_async(
        self,
        request: main_models.ListGroupsForApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGroupsForApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.application_role_id):
            query['ApplicationRoleId'] = request.application_role_id
        if not DaraCore.is_null(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGroupsForApplication',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGroupsForApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_groups_for_application(
        self,
        request: main_models.ListGroupsForApplicationRequest,
    ) -> main_models.ListGroupsForApplicationResponse:
        runtime = RuntimeOptions()
        return self.list_groups_for_application_with_options(request, runtime)

    async def list_groups_for_application_async(
        self,
        request: main_models.ListGroupsForApplicationRequest,
    ) -> main_models.ListGroupsForApplicationResponse:
        runtime = RuntimeOptions()
        return await self.list_groups_for_application_with_options_async(request, runtime)

    def list_groups_for_resource_server_with_options(
        self,
        request: main_models.ListGroupsForResourceServerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGroupsForResourceServerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGroupsForResourceServer',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGroupsForResourceServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_groups_for_resource_server_with_options_async(
        self,
        request: main_models.ListGroupsForResourceServerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGroupsForResourceServerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGroupsForResourceServer',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGroupsForResourceServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_groups_for_resource_server(
        self,
        request: main_models.ListGroupsForResourceServerRequest,
    ) -> main_models.ListGroupsForResourceServerResponse:
        runtime = RuntimeOptions()
        return self.list_groups_for_resource_server_with_options(request, runtime)

    async def list_groups_for_resource_server_async(
        self,
        request: main_models.ListGroupsForResourceServerRequest,
    ) -> main_models.ListGroupsForResourceServerResponse:
        runtime = RuntimeOptions()
        return await self.list_groups_for_resource_server_with_options_async(request, runtime)

    def list_groups_for_user_with_options(
        self,
        request: main_models.ListGroupsForUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGroupsForUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGroupsForUser',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGroupsForUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_groups_for_user_with_options_async(
        self,
        request: main_models.ListGroupsForUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGroupsForUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGroupsForUser',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGroupsForUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_groups_for_user(
        self,
        request: main_models.ListGroupsForUserRequest,
    ) -> main_models.ListGroupsForUserResponse:
        runtime = RuntimeOptions()
        return self.list_groups_for_user_with_options(request, runtime)

    async def list_groups_for_user_async(
        self,
        request: main_models.ListGroupsForUserRequest,
    ) -> main_models.ListGroupsForUserResponse:
        runtime = RuntimeOptions()
        return await self.list_groups_for_user_with_options_async(request, runtime)

    def list_identity_providers_with_options(
        self,
        request: main_models.ListIdentityProvidersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIdentityProvidersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIdentityProviders',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIdentityProvidersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_identity_providers_with_options_async(
        self,
        request: main_models.ListIdentityProvidersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIdentityProvidersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIdentityProviders',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIdentityProvidersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_identity_providers(
        self,
        request: main_models.ListIdentityProvidersRequest,
    ) -> main_models.ListIdentityProvidersResponse:
        runtime = RuntimeOptions()
        return self.list_identity_providers_with_options(request, runtime)

    async def list_identity_providers_async(
        self,
        request: main_models.ListIdentityProvidersRequest,
    ) -> main_models.ListIdentityProvidersResponse:
        runtime = RuntimeOptions()
        return await self.list_identity_providers_with_options_async(request, runtime)

    def list_identity_providers_for_network_access_endpoint_with_options(
        self,
        request: main_models.ListIdentityProvidersForNetworkAccessEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIdentityProvidersForNetworkAccessEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.network_access_endpoint_id):
            query['NetworkAccessEndpointId'] = request.network_access_endpoint_id
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIdentityProvidersForNetworkAccessEndpoint',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIdentityProvidersForNetworkAccessEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_identity_providers_for_network_access_endpoint_with_options_async(
        self,
        request: main_models.ListIdentityProvidersForNetworkAccessEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIdentityProvidersForNetworkAccessEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.network_access_endpoint_id):
            query['NetworkAccessEndpointId'] = request.network_access_endpoint_id
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIdentityProvidersForNetworkAccessEndpoint',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIdentityProvidersForNetworkAccessEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_identity_providers_for_network_access_endpoint(
        self,
        request: main_models.ListIdentityProvidersForNetworkAccessEndpointRequest,
    ) -> main_models.ListIdentityProvidersForNetworkAccessEndpointResponse:
        runtime = RuntimeOptions()
        return self.list_identity_providers_for_network_access_endpoint_with_options(request, runtime)

    async def list_identity_providers_for_network_access_endpoint_async(
        self,
        request: main_models.ListIdentityProvidersForNetworkAccessEndpointRequest,
    ) -> main_models.ListIdentityProvidersForNetworkAccessEndpointResponse:
        runtime = RuntimeOptions()
        return await self.list_identity_providers_for_network_access_endpoint_with_options_async(request, runtime)

    def list_instances_with_options(
        self,
        request: main_models.ListInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstances',
            version = '2021-12-01',
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
        request: main_models.ListInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstances',
            version = '2021-12-01',
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

    def list_network_access_endpoint_available_regions_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListNetworkAccessEndpointAvailableRegionsResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListNetworkAccessEndpointAvailableRegions',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNetworkAccessEndpointAvailableRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_network_access_endpoint_available_regions_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListNetworkAccessEndpointAvailableRegionsResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListNetworkAccessEndpointAvailableRegions',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNetworkAccessEndpointAvailableRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_network_access_endpoint_available_regions(self) -> main_models.ListNetworkAccessEndpointAvailableRegionsResponse:
        runtime = RuntimeOptions()
        return self.list_network_access_endpoint_available_regions_with_options(runtime)

    async def list_network_access_endpoint_available_regions_async(self) -> main_models.ListNetworkAccessEndpointAvailableRegionsResponse:
        runtime = RuntimeOptions()
        return await self.list_network_access_endpoint_available_regions_with_options_async(runtime)

    def list_network_access_endpoint_available_zones_with_options(
        self,
        request: main_models.ListNetworkAccessEndpointAvailableZonesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNetworkAccessEndpointAvailableZonesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.nae_region_id):
            query['NaeRegionId'] = request.nae_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNetworkAccessEndpointAvailableZones',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNetworkAccessEndpointAvailableZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_network_access_endpoint_available_zones_with_options_async(
        self,
        request: main_models.ListNetworkAccessEndpointAvailableZonesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNetworkAccessEndpointAvailableZonesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.nae_region_id):
            query['NaeRegionId'] = request.nae_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNetworkAccessEndpointAvailableZones',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNetworkAccessEndpointAvailableZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_network_access_endpoint_available_zones(
        self,
        request: main_models.ListNetworkAccessEndpointAvailableZonesRequest,
    ) -> main_models.ListNetworkAccessEndpointAvailableZonesResponse:
        runtime = RuntimeOptions()
        return self.list_network_access_endpoint_available_zones_with_options(request, runtime)

    async def list_network_access_endpoint_available_zones_async(
        self,
        request: main_models.ListNetworkAccessEndpointAvailableZonesRequest,
    ) -> main_models.ListNetworkAccessEndpointAvailableZonesResponse:
        runtime = RuntimeOptions()
        return await self.list_network_access_endpoint_available_zones_with_options_async(request, runtime)

    def list_network_access_endpoints_with_options(
        self,
        request: main_models.ListNetworkAccessEndpointsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNetworkAccessEndpointsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.network_access_endpoint_status):
            query['NetworkAccessEndpointStatus'] = request.network_access_endpoint_status
        if not DaraCore.is_null(request.network_access_endpoint_type):
            query['NetworkAccessEndpointType'] = request.network_access_endpoint_type
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.vpc_region_id):
            query['VpcRegionId'] = request.vpc_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNetworkAccessEndpoints',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNetworkAccessEndpointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_network_access_endpoints_with_options_async(
        self,
        request: main_models.ListNetworkAccessEndpointsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNetworkAccessEndpointsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.network_access_endpoint_status):
            query['NetworkAccessEndpointStatus'] = request.network_access_endpoint_status
        if not DaraCore.is_null(request.network_access_endpoint_type):
            query['NetworkAccessEndpointType'] = request.network_access_endpoint_type
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.vpc_region_id):
            query['VpcRegionId'] = request.vpc_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNetworkAccessEndpoints',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNetworkAccessEndpointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_network_access_endpoints(
        self,
        request: main_models.ListNetworkAccessEndpointsRequest,
    ) -> main_models.ListNetworkAccessEndpointsResponse:
        runtime = RuntimeOptions()
        return self.list_network_access_endpoints_with_options(request, runtime)

    async def list_network_access_endpoints_async(
        self,
        request: main_models.ListNetworkAccessEndpointsRequest,
    ) -> main_models.ListNetworkAccessEndpointsResponse:
        runtime = RuntimeOptions()
        return await self.list_network_access_endpoints_with_options_async(request, runtime)

    def list_network_access_paths_with_options(
        self,
        request: main_models.ListNetworkAccessPathsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNetworkAccessPathsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.network_access_endpoint_id):
            query['NetworkAccessEndpointId'] = request.network_access_endpoint_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNetworkAccessPaths',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNetworkAccessPathsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_network_access_paths_with_options_async(
        self,
        request: main_models.ListNetworkAccessPathsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNetworkAccessPathsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.network_access_endpoint_id):
            query['NetworkAccessEndpointId'] = request.network_access_endpoint_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNetworkAccessPaths',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNetworkAccessPathsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_network_access_paths(
        self,
        request: main_models.ListNetworkAccessPathsRequest,
    ) -> main_models.ListNetworkAccessPathsResponse:
        runtime = RuntimeOptions()
        return self.list_network_access_paths_with_options(request, runtime)

    async def list_network_access_paths_async(
        self,
        request: main_models.ListNetworkAccessPathsRequest,
    ) -> main_models.ListNetworkAccessPathsResponse:
        runtime = RuntimeOptions()
        return await self.list_network_access_paths_with_options_async(request, runtime)

    def list_network_zones_with_options(
        self,
        request: main_models.ListNetworkZonesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNetworkZonesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.network_zone_ids):
            query['NetworkZoneIds'] = request.network_zone_ids
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.previous_token):
            query['PreviousToken'] = request.previous_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNetworkZones',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNetworkZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_network_zones_with_options_async(
        self,
        request: main_models.ListNetworkZonesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNetworkZonesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.network_zone_ids):
            query['NetworkZoneIds'] = request.network_zone_ids
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.previous_token):
            query['PreviousToken'] = request.previous_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNetworkZones',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNetworkZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_network_zones(
        self,
        request: main_models.ListNetworkZonesRequest,
    ) -> main_models.ListNetworkZonesResponse:
        runtime = RuntimeOptions()
        return self.list_network_zones_with_options(request, runtime)

    async def list_network_zones_async(
        self,
        request: main_models.ListNetworkZonesRequest,
    ) -> main_models.ListNetworkZonesResponse:
        runtime = RuntimeOptions()
        return await self.list_network_zones_with_options_async(request, runtime)

    def list_organizational_unit_parents_with_options(
        self,
        request: main_models.ListOrganizationalUnitParentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListOrganizationalUnitParentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.organizational_unit_id):
            query['OrganizationalUnitId'] = request.organizational_unit_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOrganizationalUnitParents',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOrganizationalUnitParentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_organizational_unit_parents_with_options_async(
        self,
        request: main_models.ListOrganizationalUnitParentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListOrganizationalUnitParentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.organizational_unit_id):
            query['OrganizationalUnitId'] = request.organizational_unit_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOrganizationalUnitParents',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOrganizationalUnitParentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_organizational_unit_parents(
        self,
        request: main_models.ListOrganizationalUnitParentsRequest,
    ) -> main_models.ListOrganizationalUnitParentsResponse:
        runtime = RuntimeOptions()
        return self.list_organizational_unit_parents_with_options(request, runtime)

    async def list_organizational_unit_parents_async(
        self,
        request: main_models.ListOrganizationalUnitParentsRequest,
    ) -> main_models.ListOrganizationalUnitParentsResponse:
        runtime = RuntimeOptions()
        return await self.list_organizational_unit_parents_with_options_async(request, runtime)

    def list_organizational_units_with_options(
        self,
        request: main_models.ListOrganizationalUnitsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListOrganizationalUnitsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.organizational_unit_ids):
            query['OrganizationalUnitIds'] = request.organizational_unit_ids
        if not DaraCore.is_null(request.organizational_unit_name):
            query['OrganizationalUnitName'] = request.organizational_unit_name
        if not DaraCore.is_null(request.organizational_unit_name_starts_with):
            query['OrganizationalUnitNameStartsWith'] = request.organizational_unit_name_starts_with
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.parent_id):
            query['ParentId'] = request.parent_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOrganizationalUnits',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOrganizationalUnitsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_organizational_units_with_options_async(
        self,
        request: main_models.ListOrganizationalUnitsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListOrganizationalUnitsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.organizational_unit_ids):
            query['OrganizationalUnitIds'] = request.organizational_unit_ids
        if not DaraCore.is_null(request.organizational_unit_name):
            query['OrganizationalUnitName'] = request.organizational_unit_name
        if not DaraCore.is_null(request.organizational_unit_name_starts_with):
            query['OrganizationalUnitNameStartsWith'] = request.organizational_unit_name_starts_with
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.parent_id):
            query['ParentId'] = request.parent_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOrganizationalUnits',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOrganizationalUnitsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_organizational_units(
        self,
        request: main_models.ListOrganizationalUnitsRequest,
    ) -> main_models.ListOrganizationalUnitsResponse:
        runtime = RuntimeOptions()
        return self.list_organizational_units_with_options(request, runtime)

    async def list_organizational_units_async(
        self,
        request: main_models.ListOrganizationalUnitsRequest,
    ) -> main_models.ListOrganizationalUnitsResponse:
        runtime = RuntimeOptions()
        return await self.list_organizational_units_with_options_async(request, runtime)

    def list_organizational_units_for_application_with_options(
        self,
        request: main_models.ListOrganizationalUnitsForApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListOrganizationalUnitsForApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.application_role_id):
            query['ApplicationRoleId'] = request.application_role_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.organizational_unit_ids):
            query['OrganizationalUnitIds'] = request.organizational_unit_ids
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOrganizationalUnitsForApplication',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOrganizationalUnitsForApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_organizational_units_for_application_with_options_async(
        self,
        request: main_models.ListOrganizationalUnitsForApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListOrganizationalUnitsForApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.application_role_id):
            query['ApplicationRoleId'] = request.application_role_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.organizational_unit_ids):
            query['OrganizationalUnitIds'] = request.organizational_unit_ids
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOrganizationalUnitsForApplication',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOrganizationalUnitsForApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_organizational_units_for_application(
        self,
        request: main_models.ListOrganizationalUnitsForApplicationRequest,
    ) -> main_models.ListOrganizationalUnitsForApplicationResponse:
        runtime = RuntimeOptions()
        return self.list_organizational_units_for_application_with_options(request, runtime)

    async def list_organizational_units_for_application_async(
        self,
        request: main_models.ListOrganizationalUnitsForApplicationRequest,
    ) -> main_models.ListOrganizationalUnitsForApplicationResponse:
        runtime = RuntimeOptions()
        return await self.list_organizational_units_for_application_with_options_async(request, runtime)

    def list_organizational_units_for_resource_server_with_options(
        self,
        request: main_models.ListOrganizationalUnitsForResourceServerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListOrganizationalUnitsForResourceServerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOrganizationalUnitsForResourceServer',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOrganizationalUnitsForResourceServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_organizational_units_for_resource_server_with_options_async(
        self,
        request: main_models.ListOrganizationalUnitsForResourceServerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListOrganizationalUnitsForResourceServerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOrganizationalUnitsForResourceServer',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOrganizationalUnitsForResourceServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_organizational_units_for_resource_server(
        self,
        request: main_models.ListOrganizationalUnitsForResourceServerRequest,
    ) -> main_models.ListOrganizationalUnitsForResourceServerResponse:
        runtime = RuntimeOptions()
        return self.list_organizational_units_for_resource_server_with_options(request, runtime)

    async def list_organizational_units_for_resource_server_async(
        self,
        request: main_models.ListOrganizationalUnitsForResourceServerRequest,
    ) -> main_models.ListOrganizationalUnitsForResourceServerResponse:
        runtime = RuntimeOptions()
        return await self.list_organizational_units_for_resource_server_with_options_async(request, runtime)

    def list_regions_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListRegionsResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListRegions',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_regions_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListRegionsResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListRegions',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_regions(self) -> main_models.ListRegionsResponse:
        runtime = RuntimeOptions()
        return self.list_regions_with_options(runtime)

    async def list_regions_async(self) -> main_models.ListRegionsResponse:
        runtime = RuntimeOptions()
        return await self.list_regions_with_options_async(runtime)

    def list_resource_servers_for_user_with_options(
        self,
        request: main_models.ListResourceServersForUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceServersForUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceServersForUser',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceServersForUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_servers_for_user_with_options_async(
        self,
        request: main_models.ListResourceServersForUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceServersForUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceServersForUser',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceServersForUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_servers_for_user(
        self,
        request: main_models.ListResourceServersForUserRequest,
    ) -> main_models.ListResourceServersForUserResponse:
        runtime = RuntimeOptions()
        return self.list_resource_servers_for_user_with_options(request, runtime)

    async def list_resource_servers_for_user_async(
        self,
        request: main_models.ListResourceServersForUserRequest,
    ) -> main_models.ListResourceServersForUserResponse:
        runtime = RuntimeOptions()
        return await self.list_resource_servers_for_user_with_options_async(request, runtime)

    def list_synchronization_jobs_with_options(
        self,
        request: main_models.ListSynchronizationJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSynchronizationJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.target_ids):
            query['TargetIds'] = request.target_ids
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSynchronizationJobs',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSynchronizationJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_synchronization_jobs_with_options_async(
        self,
        request: main_models.ListSynchronizationJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSynchronizationJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.target_ids):
            query['TargetIds'] = request.target_ids
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSynchronizationJobs',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSynchronizationJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_synchronization_jobs(
        self,
        request: main_models.ListSynchronizationJobsRequest,
    ) -> main_models.ListSynchronizationJobsResponse:
        runtime = RuntimeOptions()
        return self.list_synchronization_jobs_with_options(request, runtime)

    async def list_synchronization_jobs_async(
        self,
        request: main_models.ListSynchronizationJobsRequest,
    ) -> main_models.ListSynchronizationJobsResponse:
        runtime = RuntimeOptions()
        return await self.list_synchronization_jobs_with_options_async(request, runtime)

    def list_user_authn_source_mappings_with_options(
        self,
        request: main_models.ListUserAuthnSourceMappingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserAuthnSourceMappingsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identity_provider_id):
            query['IdentityProviderId'] = request.identity_provider_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.previous_token):
            query['PreviousToken'] = request.previous_token
        if not DaraCore.is_null(request.user_external_id):
            query['UserExternalId'] = request.user_external_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserAuthnSourceMappings',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserAuthnSourceMappingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_authn_source_mappings_with_options_async(
        self,
        request: main_models.ListUserAuthnSourceMappingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserAuthnSourceMappingsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identity_provider_id):
            query['IdentityProviderId'] = request.identity_provider_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.previous_token):
            query['PreviousToken'] = request.previous_token
        if not DaraCore.is_null(request.user_external_id):
            query['UserExternalId'] = request.user_external_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserAuthnSourceMappings',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserAuthnSourceMappingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_authn_source_mappings(
        self,
        request: main_models.ListUserAuthnSourceMappingsRequest,
    ) -> main_models.ListUserAuthnSourceMappingsResponse:
        runtime = RuntimeOptions()
        return self.list_user_authn_source_mappings_with_options(request, runtime)

    async def list_user_authn_source_mappings_async(
        self,
        request: main_models.ListUserAuthnSourceMappingsRequest,
    ) -> main_models.ListUserAuthnSourceMappingsResponse:
        runtime = RuntimeOptions()
        return await self.list_user_authn_source_mappings_with_options_async(request, runtime)

    def list_users_with_options(
        self,
        request: main_models.ListUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.display_name_starts_with):
            query['DisplayNameStartsWith'] = request.display_name_starts_with
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.organizational_unit_id):
            query['OrganizationalUnitId'] = request.organizational_unit_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.phone_region):
            query['PhoneRegion'] = request.phone_region
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.user_external_id):
            query['UserExternalId'] = request.user_external_id
        if not DaraCore.is_null(request.user_ids):
            query['UserIds'] = request.user_ids
        if not DaraCore.is_null(request.user_source_id):
            query['UserSourceId'] = request.user_source_id
        if not DaraCore.is_null(request.user_source_type):
            query['UserSourceType'] = request.user_source_type
        if not DaraCore.is_null(request.username_starts_with):
            query['UsernameStartsWith'] = request.username_starts_with
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUsers',
            version = '2021-12-01',
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
        if not DaraCore.is_null(request.display_name_starts_with):
            query['DisplayNameStartsWith'] = request.display_name_starts_with
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.organizational_unit_id):
            query['OrganizationalUnitId'] = request.organizational_unit_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.phone_region):
            query['PhoneRegion'] = request.phone_region
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.user_external_id):
            query['UserExternalId'] = request.user_external_id
        if not DaraCore.is_null(request.user_ids):
            query['UserIds'] = request.user_ids
        if not DaraCore.is_null(request.user_source_id):
            query['UserSourceId'] = request.user_source_id
        if not DaraCore.is_null(request.user_source_type):
            query['UserSourceType'] = request.user_source_type
        if not DaraCore.is_null(request.username_starts_with):
            query['UsernameStartsWith'] = request.username_starts_with
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUsers',
            version = '2021-12-01',
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

    def list_users_for_application_with_options(
        self,
        request: main_models.ListUsersForApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUsersForApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.application_role_id):
            query['ApplicationRoleId'] = request.application_role_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUsersForApplication',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUsersForApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_users_for_application_with_options_async(
        self,
        request: main_models.ListUsersForApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUsersForApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.application_role_id):
            query['ApplicationRoleId'] = request.application_role_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUsersForApplication',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUsersForApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_users_for_application(
        self,
        request: main_models.ListUsersForApplicationRequest,
    ) -> main_models.ListUsersForApplicationResponse:
        runtime = RuntimeOptions()
        return self.list_users_for_application_with_options(request, runtime)

    async def list_users_for_application_async(
        self,
        request: main_models.ListUsersForApplicationRequest,
    ) -> main_models.ListUsersForApplicationResponse:
        runtime = RuntimeOptions()
        return await self.list_users_for_application_with_options_async(request, runtime)

    def list_users_for_group_with_options(
        self,
        request: main_models.ListUsersForGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUsersForGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUsersForGroup',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUsersForGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_users_for_group_with_options_async(
        self,
        request: main_models.ListUsersForGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUsersForGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUsersForGroup',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUsersForGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_users_for_group(
        self,
        request: main_models.ListUsersForGroupRequest,
    ) -> main_models.ListUsersForGroupResponse:
        runtime = RuntimeOptions()
        return self.list_users_for_group_with_options(request, runtime)

    async def list_users_for_group_async(
        self,
        request: main_models.ListUsersForGroupRequest,
    ) -> main_models.ListUsersForGroupResponse:
        runtime = RuntimeOptions()
        return await self.list_users_for_group_with_options_async(request, runtime)

    def list_users_for_resource_server_with_options(
        self,
        request: main_models.ListUsersForResourceServerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUsersForResourceServerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUsersForResourceServer',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUsersForResourceServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_users_for_resource_server_with_options_async(
        self,
        request: main_models.ListUsersForResourceServerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUsersForResourceServerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUsersForResourceServer',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUsersForResourceServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_users_for_resource_server(
        self,
        request: main_models.ListUsersForResourceServerRequest,
    ) -> main_models.ListUsersForResourceServerResponse:
        runtime = RuntimeOptions()
        return self.list_users_for_resource_server_with_options(request, runtime)

    async def list_users_for_resource_server_async(
        self,
        request: main_models.ListUsersForResourceServerRequest,
    ) -> main_models.ListUsersForResourceServerResponse:
        runtime = RuntimeOptions()
        return await self.list_users_for_resource_server_with_options_async(request, runtime)

    def obtain_application_client_secret_with_options(
        self,
        request: main_models.ObtainApplicationClientSecretRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ObtainApplicationClientSecretResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.secret_id):
            query['SecretId'] = request.secret_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ObtainApplicationClientSecret',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ObtainApplicationClientSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def obtain_application_client_secret_with_options_async(
        self,
        request: main_models.ObtainApplicationClientSecretRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ObtainApplicationClientSecretResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.secret_id):
            query['SecretId'] = request.secret_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ObtainApplicationClientSecret',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ObtainApplicationClientSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def obtain_application_client_secret(
        self,
        request: main_models.ObtainApplicationClientSecretRequest,
    ) -> main_models.ObtainApplicationClientSecretResponse:
        runtime = RuntimeOptions()
        return self.obtain_application_client_secret_with_options(request, runtime)

    async def obtain_application_client_secret_async(
        self,
        request: main_models.ObtainApplicationClientSecretRequest,
    ) -> main_models.ObtainApplicationClientSecretResponse:
        runtime = RuntimeOptions()
        return await self.obtain_application_client_secret_with_options_async(request, runtime)

    def obtain_application_token_with_options(
        self,
        request: main_models.ObtainApplicationTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ObtainApplicationTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.application_token_id):
            query['ApplicationTokenId'] = request.application_token_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ObtainApplicationToken',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ObtainApplicationTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def obtain_application_token_with_options_async(
        self,
        request: main_models.ObtainApplicationTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ObtainApplicationTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.application_token_id):
            query['ApplicationTokenId'] = request.application_token_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ObtainApplicationToken',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ObtainApplicationTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def obtain_application_token(
        self,
        request: main_models.ObtainApplicationTokenRequest,
    ) -> main_models.ObtainApplicationTokenResponse:
        runtime = RuntimeOptions()
        return self.obtain_application_token_with_options(request, runtime)

    async def obtain_application_token_async(
        self,
        request: main_models.ObtainApplicationTokenRequest,
    ) -> main_models.ObtainApplicationTokenResponse:
        runtime = RuntimeOptions()
        return await self.obtain_application_token_with_options_async(request, runtime)

    def obtain_domain_proxy_token_with_options(
        self,
        request: main_models.ObtainDomainProxyTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ObtainDomainProxyTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_id):
            query['DomainId'] = request.domain_id
        if not DaraCore.is_null(request.domain_proxy_token_id):
            query['DomainProxyTokenId'] = request.domain_proxy_token_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ObtainDomainProxyToken',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ObtainDomainProxyTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def obtain_domain_proxy_token_with_options_async(
        self,
        request: main_models.ObtainDomainProxyTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ObtainDomainProxyTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_id):
            query['DomainId'] = request.domain_id
        if not DaraCore.is_null(request.domain_proxy_token_id):
            query['DomainProxyTokenId'] = request.domain_proxy_token_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ObtainDomainProxyToken',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ObtainDomainProxyTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def obtain_domain_proxy_token(
        self,
        request: main_models.ObtainDomainProxyTokenRequest,
    ) -> main_models.ObtainDomainProxyTokenResponse:
        runtime = RuntimeOptions()
        return self.obtain_domain_proxy_token_with_options(request, runtime)

    async def obtain_domain_proxy_token_async(
        self,
        request: main_models.ObtainDomainProxyTokenRequest,
    ) -> main_models.ObtainDomainProxyTokenResponse:
        runtime = RuntimeOptions()
        return await self.obtain_domain_proxy_token_with_options_async(request, runtime)

    def remove_application_account_from_user_with_options(
        self,
        request: main_models.RemoveApplicationAccountFromUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveApplicationAccountFromUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_account_id):
            query['ApplicationAccountId'] = request.application_account_id
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveApplicationAccountFromUser',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveApplicationAccountFromUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_application_account_from_user_with_options_async(
        self,
        request: main_models.RemoveApplicationAccountFromUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveApplicationAccountFromUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_account_id):
            query['ApplicationAccountId'] = request.application_account_id
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveApplicationAccountFromUser',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveApplicationAccountFromUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_application_account_from_user(
        self,
        request: main_models.RemoveApplicationAccountFromUserRequest,
    ) -> main_models.RemoveApplicationAccountFromUserResponse:
        runtime = RuntimeOptions()
        return self.remove_application_account_from_user_with_options(request, runtime)

    async def remove_application_account_from_user_async(
        self,
        request: main_models.RemoveApplicationAccountFromUserRequest,
    ) -> main_models.RemoveApplicationAccountFromUserResponse:
        runtime = RuntimeOptions()
        return await self.remove_application_account_from_user_with_options_async(request, runtime)

    def remove_custom_privacy_policies_from_brand_with_options(
        self,
        request: main_models.RemoveCustomPrivacyPoliciesFromBrandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveCustomPrivacyPoliciesFromBrandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.brand_id):
            query['BrandId'] = request.brand_id
        if not DaraCore.is_null(request.custom_privacy_policy_ids):
            query['CustomPrivacyPolicyIds'] = request.custom_privacy_policy_ids
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveCustomPrivacyPoliciesFromBrand',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveCustomPrivacyPoliciesFromBrandResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_custom_privacy_policies_from_brand_with_options_async(
        self,
        request: main_models.RemoveCustomPrivacyPoliciesFromBrandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveCustomPrivacyPoliciesFromBrandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.brand_id):
            query['BrandId'] = request.brand_id
        if not DaraCore.is_null(request.custom_privacy_policy_ids):
            query['CustomPrivacyPolicyIds'] = request.custom_privacy_policy_ids
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveCustomPrivacyPoliciesFromBrand',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveCustomPrivacyPoliciesFromBrandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_custom_privacy_policies_from_brand(
        self,
        request: main_models.RemoveCustomPrivacyPoliciesFromBrandRequest,
    ) -> main_models.RemoveCustomPrivacyPoliciesFromBrandResponse:
        runtime = RuntimeOptions()
        return self.remove_custom_privacy_policies_from_brand_with_options(request, runtime)

    async def remove_custom_privacy_policies_from_brand_async(
        self,
        request: main_models.RemoveCustomPrivacyPoliciesFromBrandRequest,
    ) -> main_models.RemoveCustomPrivacyPoliciesFromBrandResponse:
        runtime = RuntimeOptions()
        return await self.remove_custom_privacy_policies_from_brand_with_options_async(request, runtime)

    def remove_user_from_organizational_units_with_options(
        self,
        request: main_models.RemoveUserFromOrganizationalUnitsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveUserFromOrganizationalUnitsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.organizational_unit_ids):
            query['OrganizationalUnitIds'] = request.organizational_unit_ids
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveUserFromOrganizationalUnits',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveUserFromOrganizationalUnitsResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_user_from_organizational_units_with_options_async(
        self,
        request: main_models.RemoveUserFromOrganizationalUnitsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveUserFromOrganizationalUnitsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.organizational_unit_ids):
            query['OrganizationalUnitIds'] = request.organizational_unit_ids
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveUserFromOrganizationalUnits',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveUserFromOrganizationalUnitsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_user_from_organizational_units(
        self,
        request: main_models.RemoveUserFromOrganizationalUnitsRequest,
    ) -> main_models.RemoveUserFromOrganizationalUnitsResponse:
        runtime = RuntimeOptions()
        return self.remove_user_from_organizational_units_with_options(request, runtime)

    async def remove_user_from_organizational_units_async(
        self,
        request: main_models.RemoveUserFromOrganizationalUnitsRequest,
    ) -> main_models.RemoveUserFromOrganizationalUnitsResponse:
        runtime = RuntimeOptions()
        return await self.remove_user_from_organizational_units_with_options_async(request, runtime)

    def remove_users_from_group_with_options(
        self,
        request: main_models.RemoveUsersFromGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveUsersFromGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveUsersFromGroup',
            version = '2021-12-01',
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
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveUsersFromGroup',
            version = '2021-12-01',
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

    def revoke_application_from_groups_with_options(
        self,
        request: main_models.RevokeApplicationFromGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RevokeApplicationFromGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.application_role_id):
            query['ApplicationRoleId'] = request.application_role_id
        if not DaraCore.is_null(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RevokeApplicationFromGroups',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokeApplicationFromGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_application_from_groups_with_options_async(
        self,
        request: main_models.RevokeApplicationFromGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RevokeApplicationFromGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.application_role_id):
            query['ApplicationRoleId'] = request.application_role_id
        if not DaraCore.is_null(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RevokeApplicationFromGroups',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokeApplicationFromGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_application_from_groups(
        self,
        request: main_models.RevokeApplicationFromGroupsRequest,
    ) -> main_models.RevokeApplicationFromGroupsResponse:
        runtime = RuntimeOptions()
        return self.revoke_application_from_groups_with_options(request, runtime)

    async def revoke_application_from_groups_async(
        self,
        request: main_models.RevokeApplicationFromGroupsRequest,
    ) -> main_models.RevokeApplicationFromGroupsResponse:
        runtime = RuntimeOptions()
        return await self.revoke_application_from_groups_with_options_async(request, runtime)

    def revoke_application_from_organizational_units_with_options(
        self,
        request: main_models.RevokeApplicationFromOrganizationalUnitsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RevokeApplicationFromOrganizationalUnitsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.application_role_id):
            query['ApplicationRoleId'] = request.application_role_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.organizational_unit_ids):
            query['OrganizationalUnitIds'] = request.organizational_unit_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RevokeApplicationFromOrganizationalUnits',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokeApplicationFromOrganizationalUnitsResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_application_from_organizational_units_with_options_async(
        self,
        request: main_models.RevokeApplicationFromOrganizationalUnitsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RevokeApplicationFromOrganizationalUnitsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.application_role_id):
            query['ApplicationRoleId'] = request.application_role_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.organizational_unit_ids):
            query['OrganizationalUnitIds'] = request.organizational_unit_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RevokeApplicationFromOrganizationalUnits',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokeApplicationFromOrganizationalUnitsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_application_from_organizational_units(
        self,
        request: main_models.RevokeApplicationFromOrganizationalUnitsRequest,
    ) -> main_models.RevokeApplicationFromOrganizationalUnitsResponse:
        runtime = RuntimeOptions()
        return self.revoke_application_from_organizational_units_with_options(request, runtime)

    async def revoke_application_from_organizational_units_async(
        self,
        request: main_models.RevokeApplicationFromOrganizationalUnitsRequest,
    ) -> main_models.RevokeApplicationFromOrganizationalUnitsResponse:
        runtime = RuntimeOptions()
        return await self.revoke_application_from_organizational_units_with_options_async(request, runtime)

    def revoke_application_from_users_with_options(
        self,
        request: main_models.RevokeApplicationFromUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RevokeApplicationFromUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.application_role_id):
            query['ApplicationRoleId'] = request.application_role_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RevokeApplicationFromUsers',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokeApplicationFromUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_application_from_users_with_options_async(
        self,
        request: main_models.RevokeApplicationFromUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RevokeApplicationFromUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.application_role_id):
            query['ApplicationRoleId'] = request.application_role_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RevokeApplicationFromUsers',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokeApplicationFromUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_application_from_users(
        self,
        request: main_models.RevokeApplicationFromUsersRequest,
    ) -> main_models.RevokeApplicationFromUsersResponse:
        runtime = RuntimeOptions()
        return self.revoke_application_from_users_with_options(request, runtime)

    async def revoke_application_from_users_async(
        self,
        request: main_models.RevokeApplicationFromUsersRequest,
    ) -> main_models.RevokeApplicationFromUsersResponse:
        runtime = RuntimeOptions()
        return await self.revoke_application_from_users_with_options_async(request, runtime)

    def revoke_resource_server_from_client_with_options(
        self,
        request: main_models.RevokeResourceServerFromClientRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RevokeResourceServerFromClientResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_application_id):
            query['ClientApplicationId'] = request.client_application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.resource_server_application_id):
            query['ResourceServerApplicationId'] = request.resource_server_application_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RevokeResourceServerFromClient',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokeResourceServerFromClientResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_resource_server_from_client_with_options_async(
        self,
        request: main_models.RevokeResourceServerFromClientRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RevokeResourceServerFromClientResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_application_id):
            query['ClientApplicationId'] = request.client_application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.resource_server_application_id):
            query['ResourceServerApplicationId'] = request.resource_server_application_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RevokeResourceServerFromClient',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokeResourceServerFromClientResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_resource_server_from_client(
        self,
        request: main_models.RevokeResourceServerFromClientRequest,
    ) -> main_models.RevokeResourceServerFromClientResponse:
        runtime = RuntimeOptions()
        return self.revoke_resource_server_from_client_with_options(request, runtime)

    async def revoke_resource_server_from_client_async(
        self,
        request: main_models.RevokeResourceServerFromClientRequest,
    ) -> main_models.RevokeResourceServerFromClientResponse:
        runtime = RuntimeOptions()
        return await self.revoke_resource_server_from_client_with_options_async(request, runtime)

    def revoke_resource_server_scopes_from_client_with_options(
        self,
        request: main_models.RevokeResourceServerScopesFromClientRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RevokeResourceServerScopesFromClientResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_application_id):
            query['ClientApplicationId'] = request.client_application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.resource_server_application_id):
            query['ResourceServerApplicationId'] = request.resource_server_application_id
        if not DaraCore.is_null(request.resource_server_scope_ids):
            query['ResourceServerScopeIds'] = request.resource_server_scope_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RevokeResourceServerScopesFromClient',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokeResourceServerScopesFromClientResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_resource_server_scopes_from_client_with_options_async(
        self,
        request: main_models.RevokeResourceServerScopesFromClientRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RevokeResourceServerScopesFromClientResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_application_id):
            query['ClientApplicationId'] = request.client_application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.resource_server_application_id):
            query['ResourceServerApplicationId'] = request.resource_server_application_id
        if not DaraCore.is_null(request.resource_server_scope_ids):
            query['ResourceServerScopeIds'] = request.resource_server_scope_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RevokeResourceServerScopesFromClient',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokeResourceServerScopesFromClientResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_resource_server_scopes_from_client(
        self,
        request: main_models.RevokeResourceServerScopesFromClientRequest,
    ) -> main_models.RevokeResourceServerScopesFromClientResponse:
        runtime = RuntimeOptions()
        return self.revoke_resource_server_scopes_from_client_with_options(request, runtime)

    async def revoke_resource_server_scopes_from_client_async(
        self,
        request: main_models.RevokeResourceServerScopesFromClientRequest,
    ) -> main_models.RevokeResourceServerScopesFromClientResponse:
        runtime = RuntimeOptions()
        return await self.revoke_resource_server_scopes_from_client_with_options_async(request, runtime)

    def revoke_resource_server_scopes_from_group_with_options(
        self,
        request: main_models.RevokeResourceServerScopesFromGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RevokeResourceServerScopesFromGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.resource_server_scope_ids):
            query['ResourceServerScopeIds'] = request.resource_server_scope_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RevokeResourceServerScopesFromGroup',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokeResourceServerScopesFromGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_resource_server_scopes_from_group_with_options_async(
        self,
        request: main_models.RevokeResourceServerScopesFromGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RevokeResourceServerScopesFromGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.resource_server_scope_ids):
            query['ResourceServerScopeIds'] = request.resource_server_scope_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RevokeResourceServerScopesFromGroup',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokeResourceServerScopesFromGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_resource_server_scopes_from_group(
        self,
        request: main_models.RevokeResourceServerScopesFromGroupRequest,
    ) -> main_models.RevokeResourceServerScopesFromGroupResponse:
        runtime = RuntimeOptions()
        return self.revoke_resource_server_scopes_from_group_with_options(request, runtime)

    async def revoke_resource_server_scopes_from_group_async(
        self,
        request: main_models.RevokeResourceServerScopesFromGroupRequest,
    ) -> main_models.RevokeResourceServerScopesFromGroupResponse:
        runtime = RuntimeOptions()
        return await self.revoke_resource_server_scopes_from_group_with_options_async(request, runtime)

    def revoke_resource_server_scopes_from_organizational_unit_with_options(
        self,
        request: main_models.RevokeResourceServerScopesFromOrganizationalUnitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RevokeResourceServerScopesFromOrganizationalUnitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.organizational_unit_id):
            query['OrganizationalUnitId'] = request.organizational_unit_id
        if not DaraCore.is_null(request.resource_server_scope_ids):
            query['ResourceServerScopeIds'] = request.resource_server_scope_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RevokeResourceServerScopesFromOrganizationalUnit',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokeResourceServerScopesFromOrganizationalUnitResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_resource_server_scopes_from_organizational_unit_with_options_async(
        self,
        request: main_models.RevokeResourceServerScopesFromOrganizationalUnitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RevokeResourceServerScopesFromOrganizationalUnitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.organizational_unit_id):
            query['OrganizationalUnitId'] = request.organizational_unit_id
        if not DaraCore.is_null(request.resource_server_scope_ids):
            query['ResourceServerScopeIds'] = request.resource_server_scope_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RevokeResourceServerScopesFromOrganizationalUnit',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokeResourceServerScopesFromOrganizationalUnitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_resource_server_scopes_from_organizational_unit(
        self,
        request: main_models.RevokeResourceServerScopesFromOrganizationalUnitRequest,
    ) -> main_models.RevokeResourceServerScopesFromOrganizationalUnitResponse:
        runtime = RuntimeOptions()
        return self.revoke_resource_server_scopes_from_organizational_unit_with_options(request, runtime)

    async def revoke_resource_server_scopes_from_organizational_unit_async(
        self,
        request: main_models.RevokeResourceServerScopesFromOrganizationalUnitRequest,
    ) -> main_models.RevokeResourceServerScopesFromOrganizationalUnitResponse:
        runtime = RuntimeOptions()
        return await self.revoke_resource_server_scopes_from_organizational_unit_with_options_async(request, runtime)

    def revoke_resource_server_scopes_from_user_with_options(
        self,
        request: main_models.RevokeResourceServerScopesFromUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RevokeResourceServerScopesFromUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.resource_server_scope_ids):
            query['ResourceServerScopeIds'] = request.resource_server_scope_ids
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RevokeResourceServerScopesFromUser',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokeResourceServerScopesFromUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_resource_server_scopes_from_user_with_options_async(
        self,
        request: main_models.RevokeResourceServerScopesFromUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RevokeResourceServerScopesFromUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.resource_server_scope_ids):
            query['ResourceServerScopeIds'] = request.resource_server_scope_ids
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RevokeResourceServerScopesFromUser',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokeResourceServerScopesFromUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_resource_server_scopes_from_user(
        self,
        request: main_models.RevokeResourceServerScopesFromUserRequest,
    ) -> main_models.RevokeResourceServerScopesFromUserResponse:
        runtime = RuntimeOptions()
        return self.revoke_resource_server_scopes_from_user_with_options(request, runtime)

    async def revoke_resource_server_scopes_from_user_async(
        self,
        request: main_models.RevokeResourceServerScopesFromUserRequest,
    ) -> main_models.RevokeResourceServerScopesFromUserResponse:
        runtime = RuntimeOptions()
        return await self.revoke_resource_server_scopes_from_user_with_options_async(request, runtime)

    def run_synchronization_job_with_options(
        self,
        request: main_models.RunSynchronizationJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunSynchronizationJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.password_initialization):
            query['PasswordInitialization'] = request.password_initialization
        if not DaraCore.is_null(request.synchronization_scope_config):
            query['SynchronizationScopeConfig'] = request.synchronization_scope_config
        if not DaraCore.is_null(request.target_id):
            query['TargetId'] = request.target_id
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        if not DaraCore.is_null(request.user_identity_types):
            query['UserIdentityTypes'] = request.user_identity_types
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RunSynchronizationJob',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunSynchronizationJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_synchronization_job_with_options_async(
        self,
        request: main_models.RunSynchronizationJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunSynchronizationJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.password_initialization):
            query['PasswordInitialization'] = request.password_initialization
        if not DaraCore.is_null(request.synchronization_scope_config):
            query['SynchronizationScopeConfig'] = request.synchronization_scope_config
        if not DaraCore.is_null(request.target_id):
            query['TargetId'] = request.target_id
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        if not DaraCore.is_null(request.user_identity_types):
            query['UserIdentityTypes'] = request.user_identity_types
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RunSynchronizationJob',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunSynchronizationJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_synchronization_job(
        self,
        request: main_models.RunSynchronizationJobRequest,
    ) -> main_models.RunSynchronizationJobResponse:
        runtime = RuntimeOptions()
        return self.run_synchronization_job_with_options(request, runtime)

    async def run_synchronization_job_async(
        self,
        request: main_models.RunSynchronizationJobRequest,
    ) -> main_models.RunSynchronizationJobResponse:
        runtime = RuntimeOptions()
        return await self.run_synchronization_job_with_options_async(request, runtime)

    def set_application_grant_scope_with_options(
        self,
        request: main_models.SetApplicationGrantScopeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetApplicationGrantScopeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.grant_scopes):
            query['GrantScopes'] = request.grant_scopes
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetApplicationGrantScope',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetApplicationGrantScopeResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_application_grant_scope_with_options_async(
        self,
        request: main_models.SetApplicationGrantScopeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetApplicationGrantScopeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.grant_scopes):
            query['GrantScopes'] = request.grant_scopes
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetApplicationGrantScope',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetApplicationGrantScopeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_application_grant_scope(
        self,
        request: main_models.SetApplicationGrantScopeRequest,
    ) -> main_models.SetApplicationGrantScopeResponse:
        runtime = RuntimeOptions()
        return self.set_application_grant_scope_with_options(request, runtime)

    async def set_application_grant_scope_async(
        self,
        request: main_models.SetApplicationGrantScopeRequest,
    ) -> main_models.SetApplicationGrantScopeResponse:
        runtime = RuntimeOptions()
        return await self.set_application_grant_scope_with_options_async(request, runtime)

    def set_application_provisioning_config_with_options(
        self,
        request: main_models.SetApplicationProvisioningConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetApplicationProvisioningConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.callback_provisioning_config):
            query['CallbackProvisioningConfig'] = request.callback_provisioning_config
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.network_access_endpoint_id):
            query['NetworkAccessEndpointId'] = request.network_access_endpoint_id
        if not DaraCore.is_null(request.provision_password):
            query['ProvisionPassword'] = request.provision_password
        if not DaraCore.is_null(request.provision_protocol_type):
            query['ProvisionProtocolType'] = request.provision_protocol_type
        if not DaraCore.is_null(request.scim_provisioning_config):
            query['ScimProvisioningConfig'] = request.scim_provisioning_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetApplicationProvisioningConfig',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetApplicationProvisioningConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_application_provisioning_config_with_options_async(
        self,
        request: main_models.SetApplicationProvisioningConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetApplicationProvisioningConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.callback_provisioning_config):
            query['CallbackProvisioningConfig'] = request.callback_provisioning_config
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.network_access_endpoint_id):
            query['NetworkAccessEndpointId'] = request.network_access_endpoint_id
        if not DaraCore.is_null(request.provision_password):
            query['ProvisionPassword'] = request.provision_password
        if not DaraCore.is_null(request.provision_protocol_type):
            query['ProvisionProtocolType'] = request.provision_protocol_type
        if not DaraCore.is_null(request.scim_provisioning_config):
            query['ScimProvisioningConfig'] = request.scim_provisioning_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetApplicationProvisioningConfig',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetApplicationProvisioningConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_application_provisioning_config(
        self,
        request: main_models.SetApplicationProvisioningConfigRequest,
    ) -> main_models.SetApplicationProvisioningConfigResponse:
        runtime = RuntimeOptions()
        return self.set_application_provisioning_config_with_options(request, runtime)

    async def set_application_provisioning_config_async(
        self,
        request: main_models.SetApplicationProvisioningConfigRequest,
    ) -> main_models.SetApplicationProvisioningConfigResponse:
        runtime = RuntimeOptions()
        return await self.set_application_provisioning_config_with_options_async(request, runtime)

    def set_application_provisioning_scope_with_options(
        self,
        request: main_models.SetApplicationProvisioningScopeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetApplicationProvisioningScopeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.organizational_unit_ids):
            query['OrganizationalUnitIds'] = request.organizational_unit_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetApplicationProvisioningScope',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetApplicationProvisioningScopeResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_application_provisioning_scope_with_options_async(
        self,
        request: main_models.SetApplicationProvisioningScopeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetApplicationProvisioningScopeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.organizational_unit_ids):
            query['OrganizationalUnitIds'] = request.organizational_unit_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetApplicationProvisioningScope',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetApplicationProvisioningScopeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_application_provisioning_scope(
        self,
        request: main_models.SetApplicationProvisioningScopeRequest,
    ) -> main_models.SetApplicationProvisioningScopeResponse:
        runtime = RuntimeOptions()
        return self.set_application_provisioning_scope_with_options(request, runtime)

    async def set_application_provisioning_scope_async(
        self,
        request: main_models.SetApplicationProvisioningScopeRequest,
    ) -> main_models.SetApplicationProvisioningScopeResponse:
        runtime = RuntimeOptions()
        return await self.set_application_provisioning_scope_with_options_async(request, runtime)

    def set_application_provisioning_user_primary_organizational_unit_with_options(
        self,
        request: main_models.SetApplicationProvisioningUserPrimaryOrganizationalUnitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetApplicationProvisioningUserPrimaryOrganizationalUnitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_primary_organizational_unit_id):
            query['UserPrimaryOrganizationalUnitId'] = request.user_primary_organizational_unit_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetApplicationProvisioningUserPrimaryOrganizationalUnit',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetApplicationProvisioningUserPrimaryOrganizationalUnitResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_application_provisioning_user_primary_organizational_unit_with_options_async(
        self,
        request: main_models.SetApplicationProvisioningUserPrimaryOrganizationalUnitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetApplicationProvisioningUserPrimaryOrganizationalUnitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_primary_organizational_unit_id):
            query['UserPrimaryOrganizationalUnitId'] = request.user_primary_organizational_unit_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetApplicationProvisioningUserPrimaryOrganizationalUnit',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetApplicationProvisioningUserPrimaryOrganizationalUnitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_application_provisioning_user_primary_organizational_unit(
        self,
        request: main_models.SetApplicationProvisioningUserPrimaryOrganizationalUnitRequest,
    ) -> main_models.SetApplicationProvisioningUserPrimaryOrganizationalUnitResponse:
        runtime = RuntimeOptions()
        return self.set_application_provisioning_user_primary_organizational_unit_with_options(request, runtime)

    async def set_application_provisioning_user_primary_organizational_unit_async(
        self,
        request: main_models.SetApplicationProvisioningUserPrimaryOrganizationalUnitRequest,
    ) -> main_models.SetApplicationProvisioningUserPrimaryOrganizationalUnitResponse:
        runtime = RuntimeOptions()
        return await self.set_application_provisioning_user_primary_organizational_unit_with_options_async(request, runtime)

    def set_application_resource_server_identifier_with_options(
        self,
        request: main_models.SetApplicationResourceServerIdentifierRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetApplicationResourceServerIdentifierResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.resource_server_identifier):
            query['ResourceServerIdentifier'] = request.resource_server_identifier
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetApplicationResourceServerIdentifier',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetApplicationResourceServerIdentifierResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_application_resource_server_identifier_with_options_async(
        self,
        request: main_models.SetApplicationResourceServerIdentifierRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetApplicationResourceServerIdentifierResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.resource_server_identifier):
            query['ResourceServerIdentifier'] = request.resource_server_identifier
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetApplicationResourceServerIdentifier',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetApplicationResourceServerIdentifierResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_application_resource_server_identifier(
        self,
        request: main_models.SetApplicationResourceServerIdentifierRequest,
    ) -> main_models.SetApplicationResourceServerIdentifierResponse:
        runtime = RuntimeOptions()
        return self.set_application_resource_server_identifier_with_options(request, runtime)

    async def set_application_resource_server_identifier_async(
        self,
        request: main_models.SetApplicationResourceServerIdentifierRequest,
    ) -> main_models.SetApplicationResourceServerIdentifierResponse:
        runtime = RuntimeOptions()
        return await self.set_application_resource_server_identifier_with_options_async(request, runtime)

    def set_application_sso_config_with_options(
        self,
        request: main_models.SetApplicationSsoConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetApplicationSsoConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.init_login_type):
            query['InitLoginType'] = request.init_login_type
        if not DaraCore.is_null(request.init_login_url):
            query['InitLoginUrl'] = request.init_login_url
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.oidc_sso_config):
            query['OidcSsoConfig'] = request.oidc_sso_config
        if not DaraCore.is_null(request.saml_sso_config):
            query['SamlSsoConfig'] = request.saml_sso_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetApplicationSsoConfig',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetApplicationSsoConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_application_sso_config_with_options_async(
        self,
        request: main_models.SetApplicationSsoConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetApplicationSsoConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.init_login_type):
            query['InitLoginType'] = request.init_login_type
        if not DaraCore.is_null(request.init_login_url):
            query['InitLoginUrl'] = request.init_login_url
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.oidc_sso_config):
            query['OidcSsoConfig'] = request.oidc_sso_config
        if not DaraCore.is_null(request.saml_sso_config):
            query['SamlSsoConfig'] = request.saml_sso_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetApplicationSsoConfig',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetApplicationSsoConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_application_sso_config(
        self,
        request: main_models.SetApplicationSsoConfigRequest,
    ) -> main_models.SetApplicationSsoConfigResponse:
        runtime = RuntimeOptions()
        return self.set_application_sso_config_with_options(request, runtime)

    async def set_application_sso_config_async(
        self,
        request: main_models.SetApplicationSsoConfigRequest,
    ) -> main_models.SetApplicationSsoConfigResponse:
        runtime = RuntimeOptions()
        return await self.set_application_sso_config_with_options_async(request, runtime)

    def set_default_domain_with_options(
        self,
        request: main_models.SetDefaultDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDefaultDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_id):
            query['DomainId'] = request.domain_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDefaultDomain',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDefaultDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_default_domain_with_options_async(
        self,
        request: main_models.SetDefaultDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDefaultDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_id):
            query['DomainId'] = request.domain_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDefaultDomain',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDefaultDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_default_domain(
        self,
        request: main_models.SetDefaultDomainRequest,
    ) -> main_models.SetDefaultDomainResponse:
        runtime = RuntimeOptions()
        return self.set_default_domain_with_options(request, runtime)

    async def set_default_domain_async(
        self,
        request: main_models.SetDefaultDomainRequest,
    ) -> main_models.SetDefaultDomainResponse:
        runtime = RuntimeOptions()
        return await self.set_default_domain_with_options_async(request, runtime)

    def set_forget_password_configuration_with_options(
        self,
        request: main_models.SetForgetPasswordConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetForgetPasswordConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.authentication_channels):
            query['AuthenticationChannels'] = request.authentication_channels
        if not DaraCore.is_null(request.forget_password_status):
            query['ForgetPasswordStatus'] = request.forget_password_status
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetForgetPasswordConfiguration',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetForgetPasswordConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_forget_password_configuration_with_options_async(
        self,
        request: main_models.SetForgetPasswordConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetForgetPasswordConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.authentication_channels):
            query['AuthenticationChannels'] = request.authentication_channels
        if not DaraCore.is_null(request.forget_password_status):
            query['ForgetPasswordStatus'] = request.forget_password_status
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetForgetPasswordConfiguration',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetForgetPasswordConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_forget_password_configuration(
        self,
        request: main_models.SetForgetPasswordConfigurationRequest,
    ) -> main_models.SetForgetPasswordConfigurationResponse:
        runtime = RuntimeOptions()
        return self.set_forget_password_configuration_with_options(request, runtime)

    async def set_forget_password_configuration_async(
        self,
        request: main_models.SetForgetPasswordConfigurationRequest,
    ) -> main_models.SetForgetPasswordConfigurationResponse:
        runtime = RuntimeOptions()
        return await self.set_forget_password_configuration_with_options_async(request, runtime)

    def set_identity_provider_ud_pull_configuration_with_options(
        self,
        request: main_models.SetIdentityProviderUdPullConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetIdentityProviderUdPullConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_sync_status):
            query['GroupSyncStatus'] = request.group_sync_status
        if not DaraCore.is_null(request.identity_provider_id):
            query['IdentityProviderId'] = request.identity_provider_id
        if not DaraCore.is_null(request.incremental_callback_status):
            query['IncrementalCallbackStatus'] = request.incremental_callback_status
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ldap_ud_pull_config):
            query['LdapUdPullConfig'] = request.ldap_ud_pull_config
        if not DaraCore.is_null(request.periodic_sync_config):
            query['PeriodicSyncConfig'] = request.periodic_sync_config
        if not DaraCore.is_null(request.periodic_sync_status):
            query['PeriodicSyncStatus'] = request.periodic_sync_status
        if not DaraCore.is_null(request.pull_protected_rule):
            query['PullProtectedRule'] = request.pull_protected_rule
        if not DaraCore.is_null(request.ud_sync_scope_config):
            query['UdSyncScopeConfig'] = request.ud_sync_scope_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetIdentityProviderUdPullConfiguration',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetIdentityProviderUdPullConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_identity_provider_ud_pull_configuration_with_options_async(
        self,
        request: main_models.SetIdentityProviderUdPullConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetIdentityProviderUdPullConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_sync_status):
            query['GroupSyncStatus'] = request.group_sync_status
        if not DaraCore.is_null(request.identity_provider_id):
            query['IdentityProviderId'] = request.identity_provider_id
        if not DaraCore.is_null(request.incremental_callback_status):
            query['IncrementalCallbackStatus'] = request.incremental_callback_status
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ldap_ud_pull_config):
            query['LdapUdPullConfig'] = request.ldap_ud_pull_config
        if not DaraCore.is_null(request.periodic_sync_config):
            query['PeriodicSyncConfig'] = request.periodic_sync_config
        if not DaraCore.is_null(request.periodic_sync_status):
            query['PeriodicSyncStatus'] = request.periodic_sync_status
        if not DaraCore.is_null(request.pull_protected_rule):
            query['PullProtectedRule'] = request.pull_protected_rule
        if not DaraCore.is_null(request.ud_sync_scope_config):
            query['UdSyncScopeConfig'] = request.ud_sync_scope_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetIdentityProviderUdPullConfiguration',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetIdentityProviderUdPullConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_identity_provider_ud_pull_configuration(
        self,
        request: main_models.SetIdentityProviderUdPullConfigurationRequest,
    ) -> main_models.SetIdentityProviderUdPullConfigurationResponse:
        runtime = RuntimeOptions()
        return self.set_identity_provider_ud_pull_configuration_with_options(request, runtime)

    async def set_identity_provider_ud_pull_configuration_async(
        self,
        request: main_models.SetIdentityProviderUdPullConfigurationRequest,
    ) -> main_models.SetIdentityProviderUdPullConfigurationResponse:
        runtime = RuntimeOptions()
        return await self.set_identity_provider_ud_pull_configuration_with_options_async(request, runtime)

    def set_login_redirect_application_for_brand_with_options(
        self,
        request: main_models.SetLoginRedirectApplicationForBrandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetLoginRedirectApplicationForBrandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.brand_id):
            query['BrandId'] = request.brand_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetLoginRedirectApplicationForBrand',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetLoginRedirectApplicationForBrandResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_login_redirect_application_for_brand_with_options_async(
        self,
        request: main_models.SetLoginRedirectApplicationForBrandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetLoginRedirectApplicationForBrandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.brand_id):
            query['BrandId'] = request.brand_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetLoginRedirectApplicationForBrand',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetLoginRedirectApplicationForBrandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_login_redirect_application_for_brand(
        self,
        request: main_models.SetLoginRedirectApplicationForBrandRequest,
    ) -> main_models.SetLoginRedirectApplicationForBrandResponse:
        runtime = RuntimeOptions()
        return self.set_login_redirect_application_for_brand_with_options(request, runtime)

    async def set_login_redirect_application_for_brand_async(
        self,
        request: main_models.SetLoginRedirectApplicationForBrandRequest,
    ) -> main_models.SetLoginRedirectApplicationForBrandResponse:
        runtime = RuntimeOptions()
        return await self.set_login_redirect_application_for_brand_with_options_async(request, runtime)

    def set_password_complexity_configuration_with_options(
        self,
        request: main_models.SetPasswordComplexityConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetPasswordComplexityConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.password_complexity_rules):
            query['PasswordComplexityRules'] = request.password_complexity_rules
        if not DaraCore.is_null(request.password_min_length):
            query['PasswordMinLength'] = request.password_min_length
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetPasswordComplexityConfiguration',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetPasswordComplexityConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_password_complexity_configuration_with_options_async(
        self,
        request: main_models.SetPasswordComplexityConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetPasswordComplexityConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.password_complexity_rules):
            query['PasswordComplexityRules'] = request.password_complexity_rules
        if not DaraCore.is_null(request.password_min_length):
            query['PasswordMinLength'] = request.password_min_length
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetPasswordComplexityConfiguration',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetPasswordComplexityConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_password_complexity_configuration(
        self,
        request: main_models.SetPasswordComplexityConfigurationRequest,
    ) -> main_models.SetPasswordComplexityConfigurationResponse:
        runtime = RuntimeOptions()
        return self.set_password_complexity_configuration_with_options(request, runtime)

    async def set_password_complexity_configuration_async(
        self,
        request: main_models.SetPasswordComplexityConfigurationRequest,
    ) -> main_models.SetPasswordComplexityConfigurationResponse:
        runtime = RuntimeOptions()
        return await self.set_password_complexity_configuration_with_options_async(request, runtime)

    def set_password_expiration_configuration_with_options(
        self,
        request: main_models.SetPasswordExpirationConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetPasswordExpirationConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.effective_authentication_source_ids):
            query['EffectiveAuthenticationSourceIds'] = request.effective_authentication_source_ids
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.password_expiration_action):
            query['PasswordExpirationAction'] = request.password_expiration_action
        if not DaraCore.is_null(request.password_expiration_notification_channels):
            query['PasswordExpirationNotificationChannels'] = request.password_expiration_notification_channels
        if not DaraCore.is_null(request.password_expiration_notification_duration):
            query['PasswordExpirationNotificationDuration'] = request.password_expiration_notification_duration
        if not DaraCore.is_null(request.password_expiration_notification_status):
            query['PasswordExpirationNotificationStatus'] = request.password_expiration_notification_status
        if not DaraCore.is_null(request.password_expiration_status):
            query['PasswordExpirationStatus'] = request.password_expiration_status
        if not DaraCore.is_null(request.password_forced_update_duration):
            query['PasswordForcedUpdateDuration'] = request.password_forced_update_duration
        if not DaraCore.is_null(request.password_valid_max_day):
            query['PasswordValidMaxDay'] = request.password_valid_max_day
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetPasswordExpirationConfiguration',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetPasswordExpirationConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_password_expiration_configuration_with_options_async(
        self,
        request: main_models.SetPasswordExpirationConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetPasswordExpirationConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.effective_authentication_source_ids):
            query['EffectiveAuthenticationSourceIds'] = request.effective_authentication_source_ids
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.password_expiration_action):
            query['PasswordExpirationAction'] = request.password_expiration_action
        if not DaraCore.is_null(request.password_expiration_notification_channels):
            query['PasswordExpirationNotificationChannels'] = request.password_expiration_notification_channels
        if not DaraCore.is_null(request.password_expiration_notification_duration):
            query['PasswordExpirationNotificationDuration'] = request.password_expiration_notification_duration
        if not DaraCore.is_null(request.password_expiration_notification_status):
            query['PasswordExpirationNotificationStatus'] = request.password_expiration_notification_status
        if not DaraCore.is_null(request.password_expiration_status):
            query['PasswordExpirationStatus'] = request.password_expiration_status
        if not DaraCore.is_null(request.password_forced_update_duration):
            query['PasswordForcedUpdateDuration'] = request.password_forced_update_duration
        if not DaraCore.is_null(request.password_valid_max_day):
            query['PasswordValidMaxDay'] = request.password_valid_max_day
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetPasswordExpirationConfiguration',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetPasswordExpirationConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_password_expiration_configuration(
        self,
        request: main_models.SetPasswordExpirationConfigurationRequest,
    ) -> main_models.SetPasswordExpirationConfigurationResponse:
        runtime = RuntimeOptions()
        return self.set_password_expiration_configuration_with_options(request, runtime)

    async def set_password_expiration_configuration_async(
        self,
        request: main_models.SetPasswordExpirationConfigurationRequest,
    ) -> main_models.SetPasswordExpirationConfigurationResponse:
        runtime = RuntimeOptions()
        return await self.set_password_expiration_configuration_with_options_async(request, runtime)

    def set_password_history_configuration_with_options(
        self,
        request: main_models.SetPasswordHistoryConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetPasswordHistoryConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.password_history_max_retention):
            query['PasswordHistoryMaxRetention'] = request.password_history_max_retention
        if not DaraCore.is_null(request.password_history_status):
            query['PasswordHistoryStatus'] = request.password_history_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetPasswordHistoryConfiguration',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetPasswordHistoryConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_password_history_configuration_with_options_async(
        self,
        request: main_models.SetPasswordHistoryConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetPasswordHistoryConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.password_history_max_retention):
            query['PasswordHistoryMaxRetention'] = request.password_history_max_retention
        if not DaraCore.is_null(request.password_history_status):
            query['PasswordHistoryStatus'] = request.password_history_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetPasswordHistoryConfiguration',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetPasswordHistoryConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_password_history_configuration(
        self,
        request: main_models.SetPasswordHistoryConfigurationRequest,
    ) -> main_models.SetPasswordHistoryConfigurationResponse:
        runtime = RuntimeOptions()
        return self.set_password_history_configuration_with_options(request, runtime)

    async def set_password_history_configuration_async(
        self,
        request: main_models.SetPasswordHistoryConfigurationRequest,
    ) -> main_models.SetPasswordHistoryConfigurationResponse:
        runtime = RuntimeOptions()
        return await self.set_password_history_configuration_with_options_async(request, runtime)

    def set_password_initialization_configuration_with_options(
        self,
        request: main_models.SetPasswordInitializationConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetPasswordInitializationConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.password_forced_update_status):
            query['PasswordForcedUpdateStatus'] = request.password_forced_update_status
        if not DaraCore.is_null(request.password_initialization_notification_channels):
            query['PasswordInitializationNotificationChannels'] = request.password_initialization_notification_channels
        if not DaraCore.is_null(request.password_initialization_status):
            query['PasswordInitializationStatus'] = request.password_initialization_status
        if not DaraCore.is_null(request.password_initialization_type):
            query['PasswordInitializationType'] = request.password_initialization_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetPasswordInitializationConfiguration',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetPasswordInitializationConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_password_initialization_configuration_with_options_async(
        self,
        request: main_models.SetPasswordInitializationConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetPasswordInitializationConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.password_forced_update_status):
            query['PasswordForcedUpdateStatus'] = request.password_forced_update_status
        if not DaraCore.is_null(request.password_initialization_notification_channels):
            query['PasswordInitializationNotificationChannels'] = request.password_initialization_notification_channels
        if not DaraCore.is_null(request.password_initialization_status):
            query['PasswordInitializationStatus'] = request.password_initialization_status
        if not DaraCore.is_null(request.password_initialization_type):
            query['PasswordInitializationType'] = request.password_initialization_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetPasswordInitializationConfiguration',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetPasswordInitializationConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_password_initialization_configuration(
        self,
        request: main_models.SetPasswordInitializationConfigurationRequest,
    ) -> main_models.SetPasswordInitializationConfigurationResponse:
        runtime = RuntimeOptions()
        return self.set_password_initialization_configuration_with_options(request, runtime)

    async def set_password_initialization_configuration_async(
        self,
        request: main_models.SetPasswordInitializationConfigurationRequest,
    ) -> main_models.SetPasswordInitializationConfigurationResponse:
        runtime = RuntimeOptions()
        return await self.set_password_initialization_configuration_with_options_async(request, runtime)

    def set_primary_client_public_key_with_options(
        self,
        request: main_models.SetPrimaryClientPublicKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetPrimaryClientPublicKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.client_public_key_id):
            query['ClientPublicKeyId'] = request.client_public_key_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetPrimaryClientPublicKey',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetPrimaryClientPublicKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_primary_client_public_key_with_options_async(
        self,
        request: main_models.SetPrimaryClientPublicKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetPrimaryClientPublicKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.client_public_key_id):
            query['ClientPublicKeyId'] = request.client_public_key_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetPrimaryClientPublicKey',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetPrimaryClientPublicKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_primary_client_public_key(
        self,
        request: main_models.SetPrimaryClientPublicKeyRequest,
    ) -> main_models.SetPrimaryClientPublicKeyResponse:
        runtime = RuntimeOptions()
        return self.set_primary_client_public_key_with_options(request, runtime)

    async def set_primary_client_public_key_async(
        self,
        request: main_models.SetPrimaryClientPublicKeyRequest,
    ) -> main_models.SetPrimaryClientPublicKeyResponse:
        runtime = RuntimeOptions()
        return await self.set_primary_client_public_key_with_options_async(request, runtime)

    def set_user_primary_organizational_unit_with_options(
        self,
        request: main_models.SetUserPrimaryOrganizationalUnitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetUserPrimaryOrganizationalUnitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.organizational_unit_id):
            query['OrganizationalUnitId'] = request.organizational_unit_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetUserPrimaryOrganizationalUnit',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetUserPrimaryOrganizationalUnitResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_user_primary_organizational_unit_with_options_async(
        self,
        request: main_models.SetUserPrimaryOrganizationalUnitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetUserPrimaryOrganizationalUnitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.organizational_unit_id):
            query['OrganizationalUnitId'] = request.organizational_unit_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetUserPrimaryOrganizationalUnit',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetUserPrimaryOrganizationalUnitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_user_primary_organizational_unit(
        self,
        request: main_models.SetUserPrimaryOrganizationalUnitRequest,
    ) -> main_models.SetUserPrimaryOrganizationalUnitResponse:
        runtime = RuntimeOptions()
        return self.set_user_primary_organizational_unit_with_options(request, runtime)

    async def set_user_primary_organizational_unit_async(
        self,
        request: main_models.SetUserPrimaryOrganizationalUnitRequest,
    ) -> main_models.SetUserPrimaryOrganizationalUnitResponse:
        runtime = RuntimeOptions()
        return await self.set_user_primary_organizational_unit_with_options_async(request, runtime)

    def unbind_user_authn_source_mapping_with_options(
        self,
        request: main_models.UnbindUserAuthnSourceMappingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindUserAuthnSourceMappingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identity_provider_id):
            query['IdentityProviderId'] = request.identity_provider_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_external_id):
            query['UserExternalId'] = request.user_external_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindUserAuthnSourceMapping',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindUserAuthnSourceMappingResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_user_authn_source_mapping_with_options_async(
        self,
        request: main_models.UnbindUserAuthnSourceMappingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindUserAuthnSourceMappingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identity_provider_id):
            query['IdentityProviderId'] = request.identity_provider_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_external_id):
            query['UserExternalId'] = request.user_external_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindUserAuthnSourceMapping',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindUserAuthnSourceMappingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_user_authn_source_mapping(
        self,
        request: main_models.UnbindUserAuthnSourceMappingRequest,
    ) -> main_models.UnbindUserAuthnSourceMappingResponse:
        runtime = RuntimeOptions()
        return self.unbind_user_authn_source_mapping_with_options(request, runtime)

    async def unbind_user_authn_source_mapping_async(
        self,
        request: main_models.UnbindUserAuthnSourceMappingRequest,
    ) -> main_models.UnbindUserAuthnSourceMappingResponse:
        runtime = RuntimeOptions()
        return await self.unbind_user_authn_source_mapping_with_options_async(request, runtime)

    def unlock_user_with_options(
        self,
        request: main_models.UnlockUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnlockUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnlockUser',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnlockUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def unlock_user_with_options_async(
        self,
        request: main_models.UnlockUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnlockUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnlockUser',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnlockUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unlock_user(
        self,
        request: main_models.UnlockUserRequest,
    ) -> main_models.UnlockUserResponse:
        runtime = RuntimeOptions()
        return self.unlock_user_with_options(request, runtime)

    async def unlock_user_async(
        self,
        request: main_models.UnlockUserRequest,
    ) -> main_models.UnlockUserResponse:
        runtime = RuntimeOptions()
        return await self.unlock_user_with_options_async(request, runtime)

    def update_application_advanced_config_with_options(
        self,
        request: main_models.UpdateApplicationAdvancedConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApplicationAdvancedConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.scim_server_advanced_config):
            query['ScimServerAdvancedConfig'] = request.scim_server_advanced_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApplicationAdvancedConfig',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApplicationAdvancedConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_application_advanced_config_with_options_async(
        self,
        request: main_models.UpdateApplicationAdvancedConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApplicationAdvancedConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.scim_server_advanced_config):
            query['ScimServerAdvancedConfig'] = request.scim_server_advanced_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApplicationAdvancedConfig',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApplicationAdvancedConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_application_advanced_config(
        self,
        request: main_models.UpdateApplicationAdvancedConfigRequest,
    ) -> main_models.UpdateApplicationAdvancedConfigResponse:
        runtime = RuntimeOptions()
        return self.update_application_advanced_config_with_options(request, runtime)

    async def update_application_advanced_config_async(
        self,
        request: main_models.UpdateApplicationAdvancedConfigRequest,
    ) -> main_models.UpdateApplicationAdvancedConfigResponse:
        runtime = RuntimeOptions()
        return await self.update_application_advanced_config_with_options_async(request, runtime)

    def update_application_authorization_type_with_options(
        self,
        request: main_models.UpdateApplicationAuthorizationTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApplicationAuthorizationTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.authorization_type):
            query['AuthorizationType'] = request.authorization_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApplicationAuthorizationType',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApplicationAuthorizationTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_application_authorization_type_with_options_async(
        self,
        request: main_models.UpdateApplicationAuthorizationTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApplicationAuthorizationTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.authorization_type):
            query['AuthorizationType'] = request.authorization_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApplicationAuthorizationType',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApplicationAuthorizationTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_application_authorization_type(
        self,
        request: main_models.UpdateApplicationAuthorizationTypeRequest,
    ) -> main_models.UpdateApplicationAuthorizationTypeResponse:
        runtime = RuntimeOptions()
        return self.update_application_authorization_type_with_options(request, runtime)

    async def update_application_authorization_type_async(
        self,
        request: main_models.UpdateApplicationAuthorizationTypeRequest,
    ) -> main_models.UpdateApplicationAuthorizationTypeResponse:
        runtime = RuntimeOptions()
        return await self.update_application_authorization_type_with_options_async(request, runtime)

    def update_application_client_secret_expiration_time_with_options(
        self,
        request: main_models.UpdateApplicationClientSecretExpirationTimeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApplicationClientSecretExpirationTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.expiration_time):
            query['ExpirationTime'] = request.expiration_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.secret_id):
            query['SecretId'] = request.secret_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApplicationClientSecretExpirationTime',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApplicationClientSecretExpirationTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_application_client_secret_expiration_time_with_options_async(
        self,
        request: main_models.UpdateApplicationClientSecretExpirationTimeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApplicationClientSecretExpirationTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.expiration_time):
            query['ExpirationTime'] = request.expiration_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.secret_id):
            query['SecretId'] = request.secret_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApplicationClientSecretExpirationTime',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApplicationClientSecretExpirationTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_application_client_secret_expiration_time(
        self,
        request: main_models.UpdateApplicationClientSecretExpirationTimeRequest,
    ) -> main_models.UpdateApplicationClientSecretExpirationTimeResponse:
        runtime = RuntimeOptions()
        return self.update_application_client_secret_expiration_time_with_options(request, runtime)

    async def update_application_client_secret_expiration_time_async(
        self,
        request: main_models.UpdateApplicationClientSecretExpirationTimeRequest,
    ) -> main_models.UpdateApplicationClientSecretExpirationTimeResponse:
        runtime = RuntimeOptions()
        return await self.update_application_client_secret_expiration_time_with_options_async(request, runtime)

    def update_application_description_with_options(
        self,
        request: main_models.UpdateApplicationDescriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApplicationDescriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApplicationDescription',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApplicationDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_application_description_with_options_async(
        self,
        request: main_models.UpdateApplicationDescriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApplicationDescriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApplicationDescription',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApplicationDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_application_description(
        self,
        request: main_models.UpdateApplicationDescriptionRequest,
    ) -> main_models.UpdateApplicationDescriptionResponse:
        runtime = RuntimeOptions()
        return self.update_application_description_with_options(request, runtime)

    async def update_application_description_async(
        self,
        request: main_models.UpdateApplicationDescriptionRequest,
    ) -> main_models.UpdateApplicationDescriptionResponse:
        runtime = RuntimeOptions()
        return await self.update_application_description_with_options_async(request, runtime)

    def update_application_federated_credential_with_options(
        self,
        request: main_models.UpdateApplicationFederatedCredentialRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApplicationFederatedCredentialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_federated_credential_id):
            query['ApplicationFederatedCredentialId'] = request.application_federated_credential_id
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.attribute_mappings):
            query['AttributeMappings'] = request.attribute_mappings
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.verification_condition):
            query['VerificationCondition'] = request.verification_condition
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApplicationFederatedCredential',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApplicationFederatedCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_application_federated_credential_with_options_async(
        self,
        request: main_models.UpdateApplicationFederatedCredentialRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApplicationFederatedCredentialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_federated_credential_id):
            query['ApplicationFederatedCredentialId'] = request.application_federated_credential_id
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.attribute_mappings):
            query['AttributeMappings'] = request.attribute_mappings
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.verification_condition):
            query['VerificationCondition'] = request.verification_condition
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApplicationFederatedCredential',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApplicationFederatedCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_application_federated_credential(
        self,
        request: main_models.UpdateApplicationFederatedCredentialRequest,
    ) -> main_models.UpdateApplicationFederatedCredentialResponse:
        runtime = RuntimeOptions()
        return self.update_application_federated_credential_with_options(request, runtime)

    async def update_application_federated_credential_async(
        self,
        request: main_models.UpdateApplicationFederatedCredentialRequest,
    ) -> main_models.UpdateApplicationFederatedCredentialResponse:
        runtime = RuntimeOptions()
        return await self.update_application_federated_credential_with_options_async(request, runtime)

    def update_application_federated_credential_description_with_options(
        self,
        request: main_models.UpdateApplicationFederatedCredentialDescriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApplicationFederatedCredentialDescriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_federated_credential_id):
            query['ApplicationFederatedCredentialId'] = request.application_federated_credential_id
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApplicationFederatedCredentialDescription',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApplicationFederatedCredentialDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_application_federated_credential_description_with_options_async(
        self,
        request: main_models.UpdateApplicationFederatedCredentialDescriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApplicationFederatedCredentialDescriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_federated_credential_id):
            query['ApplicationFederatedCredentialId'] = request.application_federated_credential_id
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApplicationFederatedCredentialDescription',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApplicationFederatedCredentialDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_application_federated_credential_description(
        self,
        request: main_models.UpdateApplicationFederatedCredentialDescriptionRequest,
    ) -> main_models.UpdateApplicationFederatedCredentialDescriptionResponse:
        runtime = RuntimeOptions()
        return self.update_application_federated_credential_description_with_options(request, runtime)

    async def update_application_federated_credential_description_async(
        self,
        request: main_models.UpdateApplicationFederatedCredentialDescriptionRequest,
    ) -> main_models.UpdateApplicationFederatedCredentialDescriptionResponse:
        runtime = RuntimeOptions()
        return await self.update_application_federated_credential_description_with_options_async(request, runtime)

    def update_application_info_with_options(
        self,
        request: main_models.UpdateApplicationInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApplicationInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.application_name):
            query['ApplicationName'] = request.application_name
        if not DaraCore.is_null(request.application_visibility):
            query['ApplicationVisibility'] = request.application_visibility
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.logo_url):
            query['LogoUrl'] = request.logo_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApplicationInfo',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApplicationInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_application_info_with_options_async(
        self,
        request: main_models.UpdateApplicationInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApplicationInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.application_name):
            query['ApplicationName'] = request.application_name
        if not DaraCore.is_null(request.application_visibility):
            query['ApplicationVisibility'] = request.application_visibility
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.logo_url):
            query['LogoUrl'] = request.logo_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApplicationInfo',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApplicationInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_application_info(
        self,
        request: main_models.UpdateApplicationInfoRequest,
    ) -> main_models.UpdateApplicationInfoResponse:
        runtime = RuntimeOptions()
        return self.update_application_info_with_options(request, runtime)

    async def update_application_info_async(
        self,
        request: main_models.UpdateApplicationInfoRequest,
    ) -> main_models.UpdateApplicationInfoResponse:
        runtime = RuntimeOptions()
        return await self.update_application_info_with_options_async(request, runtime)

    def update_application_role_with_options(
        self,
        request: main_models.UpdateApplicationRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApplicationRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.application_role_id):
            query['ApplicationRoleId'] = request.application_role_id
        if not DaraCore.is_null(request.application_role_name):
            query['ApplicationRoleName'] = request.application_role_name
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApplicationRole',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApplicationRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_application_role_with_options_async(
        self,
        request: main_models.UpdateApplicationRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApplicationRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.application_role_id):
            query['ApplicationRoleId'] = request.application_role_id
        if not DaraCore.is_null(request.application_role_name):
            query['ApplicationRoleName'] = request.application_role_name
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApplicationRole',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApplicationRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_application_role(
        self,
        request: main_models.UpdateApplicationRoleRequest,
    ) -> main_models.UpdateApplicationRoleResponse:
        runtime = RuntimeOptions()
        return self.update_application_role_with_options(request, runtime)

    async def update_application_role_async(
        self,
        request: main_models.UpdateApplicationRoleRequest,
    ) -> main_models.UpdateApplicationRoleResponse:
        runtime = RuntimeOptions()
        return await self.update_application_role_with_options_async(request, runtime)

    def update_application_role_description_with_options(
        self,
        request: main_models.UpdateApplicationRoleDescriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApplicationRoleDescriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.application_role_id):
            query['ApplicationRoleId'] = request.application_role_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApplicationRoleDescription',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApplicationRoleDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_application_role_description_with_options_async(
        self,
        request: main_models.UpdateApplicationRoleDescriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApplicationRoleDescriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.application_role_id):
            query['ApplicationRoleId'] = request.application_role_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApplicationRoleDescription',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApplicationRoleDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_application_role_description(
        self,
        request: main_models.UpdateApplicationRoleDescriptionRequest,
    ) -> main_models.UpdateApplicationRoleDescriptionResponse:
        runtime = RuntimeOptions()
        return self.update_application_role_description_with_options(request, runtime)

    async def update_application_role_description_async(
        self,
        request: main_models.UpdateApplicationRoleDescriptionRequest,
    ) -> main_models.UpdateApplicationRoleDescriptionResponse:
        runtime = RuntimeOptions()
        return await self.update_application_role_description_with_options_async(request, runtime)

    def update_application_sso_form_params_with_options(
        self,
        request: main_models.UpdateApplicationSsoFormParamsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApplicationSsoFormParamsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.application_template_params):
            query['ApplicationTemplateParams'] = request.application_template_params
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApplicationSsoFormParams',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApplicationSsoFormParamsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_application_sso_form_params_with_options_async(
        self,
        request: main_models.UpdateApplicationSsoFormParamsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApplicationSsoFormParamsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.application_template_params):
            query['ApplicationTemplateParams'] = request.application_template_params
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApplicationSsoFormParams',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApplicationSsoFormParamsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_application_sso_form_params(
        self,
        request: main_models.UpdateApplicationSsoFormParamsRequest,
    ) -> main_models.UpdateApplicationSsoFormParamsResponse:
        runtime = RuntimeOptions()
        return self.update_application_sso_form_params_with_options(request, runtime)

    async def update_application_sso_form_params_async(
        self,
        request: main_models.UpdateApplicationSsoFormParamsRequest,
    ) -> main_models.UpdateApplicationSsoFormParamsResponse:
        runtime = RuntimeOptions()
        return await self.update_application_sso_form_params_with_options_async(request, runtime)

    def update_application_token_expiration_time_with_options(
        self,
        request: main_models.UpdateApplicationTokenExpirationTimeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApplicationTokenExpirationTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.application_token_id):
            query['ApplicationTokenId'] = request.application_token_id
        if not DaraCore.is_null(request.expiration_time):
            query['ExpirationTime'] = request.expiration_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApplicationTokenExpirationTime',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApplicationTokenExpirationTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_application_token_expiration_time_with_options_async(
        self,
        request: main_models.UpdateApplicationTokenExpirationTimeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApplicationTokenExpirationTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.application_token_id):
            query['ApplicationTokenId'] = request.application_token_id
        if not DaraCore.is_null(request.expiration_time):
            query['ExpirationTime'] = request.expiration_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApplicationTokenExpirationTime',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApplicationTokenExpirationTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_application_token_expiration_time(
        self,
        request: main_models.UpdateApplicationTokenExpirationTimeRequest,
    ) -> main_models.UpdateApplicationTokenExpirationTimeResponse:
        runtime = RuntimeOptions()
        return self.update_application_token_expiration_time_with_options(request, runtime)

    async def update_application_token_expiration_time_async(
        self,
        request: main_models.UpdateApplicationTokenExpirationTimeRequest,
    ) -> main_models.UpdateApplicationTokenExpirationTimeResponse:
        runtime = RuntimeOptions()
        return await self.update_application_token_expiration_time_with_options_async(request, runtime)

    def update_brand_with_options(
        self,
        request: main_models.UpdateBrandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateBrandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.brand_id):
            query['BrandId'] = request.brand_id
        if not DaraCore.is_null(request.brand_name):
            query['BrandName'] = request.brand_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateBrand',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateBrandResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_brand_with_options_async(
        self,
        request: main_models.UpdateBrandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateBrandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.brand_id):
            query['BrandId'] = request.brand_id
        if not DaraCore.is_null(request.brand_name):
            query['BrandName'] = request.brand_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateBrand',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateBrandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_brand(
        self,
        request: main_models.UpdateBrandRequest,
    ) -> main_models.UpdateBrandResponse:
        runtime = RuntimeOptions()
        return self.update_brand_with_options(request, runtime)

    async def update_brand_async(
        self,
        request: main_models.UpdateBrandRequest,
    ) -> main_models.UpdateBrandResponse:
        runtime = RuntimeOptions()
        return await self.update_brand_with_options_async(request, runtime)

    def update_cloud_account_with_options(
        self,
        request: main_models.UpdateCloudAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCloudAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cloud_account_id):
            query['CloudAccountId'] = request.cloud_account_id
        if not DaraCore.is_null(request.cloud_account_name):
            query['CloudAccountName'] = request.cloud_account_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCloudAccount',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCloudAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cloud_account_with_options_async(
        self,
        request: main_models.UpdateCloudAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCloudAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cloud_account_id):
            query['CloudAccountId'] = request.cloud_account_id
        if not DaraCore.is_null(request.cloud_account_name):
            query['CloudAccountName'] = request.cloud_account_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCloudAccount',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCloudAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cloud_account(
        self,
        request: main_models.UpdateCloudAccountRequest,
    ) -> main_models.UpdateCloudAccountResponse:
        runtime = RuntimeOptions()
        return self.update_cloud_account_with_options(request, runtime)

    async def update_cloud_account_async(
        self,
        request: main_models.UpdateCloudAccountRequest,
    ) -> main_models.UpdateCloudAccountResponse:
        runtime = RuntimeOptions()
        return await self.update_cloud_account_with_options_async(request, runtime)

    def update_cloud_account_description_with_options(
        self,
        request: main_models.UpdateCloudAccountDescriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCloudAccountDescriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cloud_account_id):
            query['CloudAccountId'] = request.cloud_account_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCloudAccountDescription',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCloudAccountDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cloud_account_description_with_options_async(
        self,
        request: main_models.UpdateCloudAccountDescriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCloudAccountDescriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cloud_account_id):
            query['CloudAccountId'] = request.cloud_account_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCloudAccountDescription',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCloudAccountDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cloud_account_description(
        self,
        request: main_models.UpdateCloudAccountDescriptionRequest,
    ) -> main_models.UpdateCloudAccountDescriptionResponse:
        runtime = RuntimeOptions()
        return self.update_cloud_account_description_with_options(request, runtime)

    async def update_cloud_account_description_async(
        self,
        request: main_models.UpdateCloudAccountDescriptionRequest,
    ) -> main_models.UpdateCloudAccountDescriptionResponse:
        runtime = RuntimeOptions()
        return await self.update_cloud_account_description_with_options_async(request, runtime)

    def update_cloud_account_role_description_with_options(
        self,
        request: main_models.UpdateCloudAccountRoleDescriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCloudAccountRoleDescriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cloud_account_id):
            query['CloudAccountId'] = request.cloud_account_id
        if not DaraCore.is_null(request.cloud_account_role_id):
            query['CloudAccountRoleId'] = request.cloud_account_role_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCloudAccountRoleDescription',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCloudAccountRoleDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cloud_account_role_description_with_options_async(
        self,
        request: main_models.UpdateCloudAccountRoleDescriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCloudAccountRoleDescriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cloud_account_id):
            query['CloudAccountId'] = request.cloud_account_id
        if not DaraCore.is_null(request.cloud_account_role_id):
            query['CloudAccountRoleId'] = request.cloud_account_role_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCloudAccountRoleDescription',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCloudAccountRoleDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cloud_account_role_description(
        self,
        request: main_models.UpdateCloudAccountRoleDescriptionRequest,
    ) -> main_models.UpdateCloudAccountRoleDescriptionResponse:
        runtime = RuntimeOptions()
        return self.update_cloud_account_role_description_with_options(request, runtime)

    async def update_cloud_account_role_description_async(
        self,
        request: main_models.UpdateCloudAccountRoleDescriptionRequest,
    ) -> main_models.UpdateCloudAccountRoleDescriptionResponse:
        runtime = RuntimeOptions()
        return await self.update_cloud_account_role_description_with_options_async(request, runtime)

    def update_conditional_access_policy_with_options(
        self,
        request: main_models.UpdateConditionalAccessPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateConditionalAccessPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.conditional_access_policy_id):
            query['ConditionalAccessPolicyId'] = request.conditional_access_policy_id
        if not DaraCore.is_null(request.conditional_access_policy_name):
            query['ConditionalAccessPolicyName'] = request.conditional_access_policy_name
        if not DaraCore.is_null(request.conditions_config):
            query['ConditionsConfig'] = request.conditions_config
        if not DaraCore.is_null(request.decision_config):
            query['DecisionConfig'] = request.decision_config
        if not DaraCore.is_null(request.decision_type):
            query['DecisionType'] = request.decision_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateConditionalAccessPolicy',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateConditionalAccessPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_conditional_access_policy_with_options_async(
        self,
        request: main_models.UpdateConditionalAccessPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateConditionalAccessPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.conditional_access_policy_id):
            query['ConditionalAccessPolicyId'] = request.conditional_access_policy_id
        if not DaraCore.is_null(request.conditional_access_policy_name):
            query['ConditionalAccessPolicyName'] = request.conditional_access_policy_name
        if not DaraCore.is_null(request.conditions_config):
            query['ConditionsConfig'] = request.conditions_config
        if not DaraCore.is_null(request.decision_config):
            query['DecisionConfig'] = request.decision_config
        if not DaraCore.is_null(request.decision_type):
            query['DecisionType'] = request.decision_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateConditionalAccessPolicy',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateConditionalAccessPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_conditional_access_policy(
        self,
        request: main_models.UpdateConditionalAccessPolicyRequest,
    ) -> main_models.UpdateConditionalAccessPolicyResponse:
        runtime = RuntimeOptions()
        return self.update_conditional_access_policy_with_options(request, runtime)

    async def update_conditional_access_policy_async(
        self,
        request: main_models.UpdateConditionalAccessPolicyRequest,
    ) -> main_models.UpdateConditionalAccessPolicyResponse:
        runtime = RuntimeOptions()
        return await self.update_conditional_access_policy_with_options_async(request, runtime)

    def update_conditional_access_policy_description_with_options(
        self,
        request: main_models.UpdateConditionalAccessPolicyDescriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateConditionalAccessPolicyDescriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.conditional_access_policy_id):
            query['ConditionalAccessPolicyId'] = request.conditional_access_policy_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateConditionalAccessPolicyDescription',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateConditionalAccessPolicyDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_conditional_access_policy_description_with_options_async(
        self,
        request: main_models.UpdateConditionalAccessPolicyDescriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateConditionalAccessPolicyDescriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.conditional_access_policy_id):
            query['ConditionalAccessPolicyId'] = request.conditional_access_policy_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateConditionalAccessPolicyDescription',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateConditionalAccessPolicyDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_conditional_access_policy_description(
        self,
        request: main_models.UpdateConditionalAccessPolicyDescriptionRequest,
    ) -> main_models.UpdateConditionalAccessPolicyDescriptionResponse:
        runtime = RuntimeOptions()
        return self.update_conditional_access_policy_description_with_options(request, runtime)

    async def update_conditional_access_policy_description_async(
        self,
        request: main_models.UpdateConditionalAccessPolicyDescriptionRequest,
    ) -> main_models.UpdateConditionalAccessPolicyDescriptionResponse:
        runtime = RuntimeOptions()
        return await self.update_conditional_access_policy_description_with_options_async(request, runtime)

    def update_custom_privacy_policy_with_options(
        self,
        request: main_models.UpdateCustomPrivacyPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCustomPrivacyPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.custom_privacy_policy_contents):
            query['CustomPrivacyPolicyContents'] = request.custom_privacy_policy_contents
        if not DaraCore.is_null(request.custom_privacy_policy_id):
            query['CustomPrivacyPolicyId'] = request.custom_privacy_policy_id
        if not DaraCore.is_null(request.custom_privacy_policy_name):
            query['CustomPrivacyPolicyName'] = request.custom_privacy_policy_name
        if not DaraCore.is_null(request.default_language_code):
            query['DefaultLanguageCode'] = request.default_language_code
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_consent_type):
            query['UserConsentType'] = request.user_consent_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCustomPrivacyPolicy',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCustomPrivacyPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_custom_privacy_policy_with_options_async(
        self,
        request: main_models.UpdateCustomPrivacyPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCustomPrivacyPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.custom_privacy_policy_contents):
            query['CustomPrivacyPolicyContents'] = request.custom_privacy_policy_contents
        if not DaraCore.is_null(request.custom_privacy_policy_id):
            query['CustomPrivacyPolicyId'] = request.custom_privacy_policy_id
        if not DaraCore.is_null(request.custom_privacy_policy_name):
            query['CustomPrivacyPolicyName'] = request.custom_privacy_policy_name
        if not DaraCore.is_null(request.default_language_code):
            query['DefaultLanguageCode'] = request.default_language_code
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_consent_type):
            query['UserConsentType'] = request.user_consent_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCustomPrivacyPolicy',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCustomPrivacyPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_custom_privacy_policy(
        self,
        request: main_models.UpdateCustomPrivacyPolicyRequest,
    ) -> main_models.UpdateCustomPrivacyPolicyResponse:
        runtime = RuntimeOptions()
        return self.update_custom_privacy_policy_with_options(request, runtime)

    async def update_custom_privacy_policy_async(
        self,
        request: main_models.UpdateCustomPrivacyPolicyRequest,
    ) -> main_models.UpdateCustomPrivacyPolicyResponse:
        runtime = RuntimeOptions()
        return await self.update_custom_privacy_policy_with_options_async(request, runtime)

    def update_domain_brand_with_options(
        self,
        request: main_models.UpdateDomainBrandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDomainBrandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.brand_id):
            query['BrandId'] = request.brand_id
        if not DaraCore.is_null(request.domain_id):
            query['DomainId'] = request.domain_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDomainBrand',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDomainBrandResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_domain_brand_with_options_async(
        self,
        request: main_models.UpdateDomainBrandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDomainBrandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.brand_id):
            query['BrandId'] = request.brand_id
        if not DaraCore.is_null(request.domain_id):
            query['DomainId'] = request.domain_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDomainBrand',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDomainBrandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_domain_brand(
        self,
        request: main_models.UpdateDomainBrandRequest,
    ) -> main_models.UpdateDomainBrandResponse:
        runtime = RuntimeOptions()
        return self.update_domain_brand_with_options(request, runtime)

    async def update_domain_brand_async(
        self,
        request: main_models.UpdateDomainBrandRequest,
    ) -> main_models.UpdateDomainBrandResponse:
        runtime = RuntimeOptions()
        return await self.update_domain_brand_with_options_async(request, runtime)

    def update_domain_icp_number_with_options(
        self,
        request: main_models.UpdateDomainIcpNumberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDomainIcpNumberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_id):
            query['DomainId'] = request.domain_id
        if not DaraCore.is_null(request.icp_number):
            query['IcpNumber'] = request.icp_number
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDomainIcpNumber',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDomainIcpNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_domain_icp_number_with_options_async(
        self,
        request: main_models.UpdateDomainIcpNumberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDomainIcpNumberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_id):
            query['DomainId'] = request.domain_id
        if not DaraCore.is_null(request.icp_number):
            query['IcpNumber'] = request.icp_number
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDomainIcpNumber',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDomainIcpNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_domain_icp_number(
        self,
        request: main_models.UpdateDomainIcpNumberRequest,
    ) -> main_models.UpdateDomainIcpNumberResponse:
        runtime = RuntimeOptions()
        return self.update_domain_icp_number_with_options(request, runtime)

    async def update_domain_icp_number_async(
        self,
        request: main_models.UpdateDomainIcpNumberRequest,
    ) -> main_models.UpdateDomainIcpNumberResponse:
        runtime = RuntimeOptions()
        return await self.update_domain_icp_number_with_options_async(request, runtime)

    def update_federated_credential_provider_with_options(
        self,
        request: main_models.UpdateFederatedCredentialProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFederatedCredentialProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.federated_credential_provider_id):
            query['FederatedCredentialProviderId'] = request.federated_credential_provider_id
        if not DaraCore.is_null(request.federated_credential_provider_name):
            query['FederatedCredentialProviderName'] = request.federated_credential_provider_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.network_access_endpoint_id):
            query['NetworkAccessEndpointId'] = request.network_access_endpoint_id
        if not DaraCore.is_null(request.oidc_provider_config):
            query['OidcProviderConfig'] = request.oidc_provider_config
        if not DaraCore.is_null(request.pkcs_7provider_config):
            query['Pkcs7ProviderConfig'] = request.pkcs_7provider_config
        if not DaraCore.is_null(request.private_ca_provider_config):
            query['PrivateCaProviderConfig'] = request.private_ca_provider_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFederatedCredentialProvider',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFederatedCredentialProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_federated_credential_provider_with_options_async(
        self,
        request: main_models.UpdateFederatedCredentialProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFederatedCredentialProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.federated_credential_provider_id):
            query['FederatedCredentialProviderId'] = request.federated_credential_provider_id
        if not DaraCore.is_null(request.federated_credential_provider_name):
            query['FederatedCredentialProviderName'] = request.federated_credential_provider_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.network_access_endpoint_id):
            query['NetworkAccessEndpointId'] = request.network_access_endpoint_id
        if not DaraCore.is_null(request.oidc_provider_config):
            query['OidcProviderConfig'] = request.oidc_provider_config
        if not DaraCore.is_null(request.pkcs_7provider_config):
            query['Pkcs7ProviderConfig'] = request.pkcs_7provider_config
        if not DaraCore.is_null(request.private_ca_provider_config):
            query['PrivateCaProviderConfig'] = request.private_ca_provider_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFederatedCredentialProvider',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFederatedCredentialProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_federated_credential_provider(
        self,
        request: main_models.UpdateFederatedCredentialProviderRequest,
    ) -> main_models.UpdateFederatedCredentialProviderResponse:
        runtime = RuntimeOptions()
        return self.update_federated_credential_provider_with_options(request, runtime)

    async def update_federated_credential_provider_async(
        self,
        request: main_models.UpdateFederatedCredentialProviderRequest,
    ) -> main_models.UpdateFederatedCredentialProviderResponse:
        runtime = RuntimeOptions()
        return await self.update_federated_credential_provider_with_options_async(request, runtime)

    def update_federated_credential_provider_description_with_options(
        self,
        request: main_models.UpdateFederatedCredentialProviderDescriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFederatedCredentialProviderDescriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.federated_credential_provider_id):
            query['FederatedCredentialProviderId'] = request.federated_credential_provider_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFederatedCredentialProviderDescription',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFederatedCredentialProviderDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_federated_credential_provider_description_with_options_async(
        self,
        request: main_models.UpdateFederatedCredentialProviderDescriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFederatedCredentialProviderDescriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.federated_credential_provider_id):
            query['FederatedCredentialProviderId'] = request.federated_credential_provider_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFederatedCredentialProviderDescription',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFederatedCredentialProviderDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_federated_credential_provider_description(
        self,
        request: main_models.UpdateFederatedCredentialProviderDescriptionRequest,
    ) -> main_models.UpdateFederatedCredentialProviderDescriptionResponse:
        runtime = RuntimeOptions()
        return self.update_federated_credential_provider_description_with_options(request, runtime)

    async def update_federated_credential_provider_description_async(
        self,
        request: main_models.UpdateFederatedCredentialProviderDescriptionRequest,
    ) -> main_models.UpdateFederatedCredentialProviderDescriptionResponse:
        runtime = RuntimeOptions()
        return await self.update_federated_credential_provider_description_with_options_async(request, runtime)

    def update_group_with_options(
        self,
        request: main_models.UpdateGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_external_id):
            query['GroupExternalId'] = request.group_external_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGroup',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_group_with_options_async(
        self,
        request: main_models.UpdateGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_external_id):
            query['GroupExternalId'] = request.group_external_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGroup',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_group(
        self,
        request: main_models.UpdateGroupRequest,
    ) -> main_models.UpdateGroupResponse:
        runtime = RuntimeOptions()
        return self.update_group_with_options(request, runtime)

    async def update_group_async(
        self,
        request: main_models.UpdateGroupRequest,
    ) -> main_models.UpdateGroupResponse:
        runtime = RuntimeOptions()
        return await self.update_group_with_options_async(request, runtime)

    def update_group_description_with_options(
        self,
        request: main_models.UpdateGroupDescriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGroupDescriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGroupDescription',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGroupDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_group_description_with_options_async(
        self,
        request: main_models.UpdateGroupDescriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGroupDescriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGroupDescription',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGroupDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_group_description(
        self,
        request: main_models.UpdateGroupDescriptionRequest,
    ) -> main_models.UpdateGroupDescriptionResponse:
        runtime = RuntimeOptions()
        return self.update_group_description_with_options(request, runtime)

    async def update_group_description_async(
        self,
        request: main_models.UpdateGroupDescriptionRequest,
    ) -> main_models.UpdateGroupDescriptionResponse:
        runtime = RuntimeOptions()
        return await self.update_group_description_with_options_async(request, runtime)

    def update_identity_provider_with_options(
        self,
        request: main_models.UpdateIdentityProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateIdentityProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dingtalk_app_config):
            query['DingtalkAppConfig'] = request.dingtalk_app_config
        if not DaraCore.is_null(request.identity_provider_id):
            query['IdentityProviderId'] = request.identity_provider_id
        if not DaraCore.is_null(request.identity_provider_name):
            query['IdentityProviderName'] = request.identity_provider_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lark_config):
            query['LarkConfig'] = request.lark_config
        if not DaraCore.is_null(request.ldap_config):
            query['LdapConfig'] = request.ldap_config
        if not DaraCore.is_null(request.logo_url):
            query['LogoUrl'] = request.logo_url
        if not DaraCore.is_null(request.network_access_endpoint_id):
            query['NetworkAccessEndpointId'] = request.network_access_endpoint_id
        if not DaraCore.is_null(request.oidc_config):
            query['OidcConfig'] = request.oidc_config
        if not DaraCore.is_null(request.we_com_config):
            query['WeComConfig'] = request.we_com_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateIdentityProvider',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateIdentityProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_identity_provider_with_options_async(
        self,
        request: main_models.UpdateIdentityProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateIdentityProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dingtalk_app_config):
            query['DingtalkAppConfig'] = request.dingtalk_app_config
        if not DaraCore.is_null(request.identity_provider_id):
            query['IdentityProviderId'] = request.identity_provider_id
        if not DaraCore.is_null(request.identity_provider_name):
            query['IdentityProviderName'] = request.identity_provider_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lark_config):
            query['LarkConfig'] = request.lark_config
        if not DaraCore.is_null(request.ldap_config):
            query['LdapConfig'] = request.ldap_config
        if not DaraCore.is_null(request.logo_url):
            query['LogoUrl'] = request.logo_url
        if not DaraCore.is_null(request.network_access_endpoint_id):
            query['NetworkAccessEndpointId'] = request.network_access_endpoint_id
        if not DaraCore.is_null(request.oidc_config):
            query['OidcConfig'] = request.oidc_config
        if not DaraCore.is_null(request.we_com_config):
            query['WeComConfig'] = request.we_com_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateIdentityProvider',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateIdentityProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_identity_provider(
        self,
        request: main_models.UpdateIdentityProviderRequest,
    ) -> main_models.UpdateIdentityProviderResponse:
        runtime = RuntimeOptions()
        return self.update_identity_provider_with_options(request, runtime)

    async def update_identity_provider_async(
        self,
        request: main_models.UpdateIdentityProviderRequest,
    ) -> main_models.UpdateIdentityProviderResponse:
        runtime = RuntimeOptions()
        return await self.update_identity_provider_with_options_async(request, runtime)

    def update_instance_description_with_options(
        self,
        request: main_models.UpdateInstanceDescriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceDescriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstanceDescription',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_description_with_options_async(
        self,
        request: main_models.UpdateInstanceDescriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceDescriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstanceDescription',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance_description(
        self,
        request: main_models.UpdateInstanceDescriptionRequest,
    ) -> main_models.UpdateInstanceDescriptionResponse:
        runtime = RuntimeOptions()
        return self.update_instance_description_with_options(request, runtime)

    async def update_instance_description_async(
        self,
        request: main_models.UpdateInstanceDescriptionRequest,
    ) -> main_models.UpdateInstanceDescriptionResponse:
        runtime = RuntimeOptions()
        return await self.update_instance_description_with_options_async(request, runtime)

    def update_network_access_endpoint_name_with_options(
        self,
        request: main_models.UpdateNetworkAccessEndpointNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateNetworkAccessEndpointNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.network_access_endpoint_id):
            query['NetworkAccessEndpointId'] = request.network_access_endpoint_id
        if not DaraCore.is_null(request.network_access_endpoint_name):
            query['NetworkAccessEndpointName'] = request.network_access_endpoint_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateNetworkAccessEndpointName',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateNetworkAccessEndpointNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_network_access_endpoint_name_with_options_async(
        self,
        request: main_models.UpdateNetworkAccessEndpointNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateNetworkAccessEndpointNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.network_access_endpoint_id):
            query['NetworkAccessEndpointId'] = request.network_access_endpoint_id
        if not DaraCore.is_null(request.network_access_endpoint_name):
            query['NetworkAccessEndpointName'] = request.network_access_endpoint_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateNetworkAccessEndpointName',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateNetworkAccessEndpointNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_network_access_endpoint_name(
        self,
        request: main_models.UpdateNetworkAccessEndpointNameRequest,
    ) -> main_models.UpdateNetworkAccessEndpointNameResponse:
        runtime = RuntimeOptions()
        return self.update_network_access_endpoint_name_with_options(request, runtime)

    async def update_network_access_endpoint_name_async(
        self,
        request: main_models.UpdateNetworkAccessEndpointNameRequest,
    ) -> main_models.UpdateNetworkAccessEndpointNameResponse:
        runtime = RuntimeOptions()
        return await self.update_network_access_endpoint_name_with_options_async(request, runtime)

    def update_network_zone_with_options(
        self,
        request: main_models.UpdateNetworkZoneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateNetworkZoneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ipv_4cidrs):
            query['Ipv4Cidrs'] = request.ipv_4cidrs
        if not DaraCore.is_null(request.ipv_6cidrs):
            query['Ipv6Cidrs'] = request.ipv_6cidrs
        if not DaraCore.is_null(request.network_zone_id):
            query['NetworkZoneId'] = request.network_zone_id
        if not DaraCore.is_null(request.network_zone_name):
            query['NetworkZoneName'] = request.network_zone_name
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateNetworkZone',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateNetworkZoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_network_zone_with_options_async(
        self,
        request: main_models.UpdateNetworkZoneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateNetworkZoneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.ipv_4cidrs):
            query['Ipv4Cidrs'] = request.ipv_4cidrs
        if not DaraCore.is_null(request.ipv_6cidrs):
            query['Ipv6Cidrs'] = request.ipv_6cidrs
        if not DaraCore.is_null(request.network_zone_id):
            query['NetworkZoneId'] = request.network_zone_id
        if not DaraCore.is_null(request.network_zone_name):
            query['NetworkZoneName'] = request.network_zone_name
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateNetworkZone',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateNetworkZoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_network_zone(
        self,
        request: main_models.UpdateNetworkZoneRequest,
    ) -> main_models.UpdateNetworkZoneResponse:
        runtime = RuntimeOptions()
        return self.update_network_zone_with_options(request, runtime)

    async def update_network_zone_async(
        self,
        request: main_models.UpdateNetworkZoneRequest,
    ) -> main_models.UpdateNetworkZoneResponse:
        runtime = RuntimeOptions()
        return await self.update_network_zone_with_options_async(request, runtime)

    def update_network_zone_description_with_options(
        self,
        request: main_models.UpdateNetworkZoneDescriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateNetworkZoneDescriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.network_zone_id):
            query['NetworkZoneId'] = request.network_zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateNetworkZoneDescription',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateNetworkZoneDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_network_zone_description_with_options_async(
        self,
        request: main_models.UpdateNetworkZoneDescriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateNetworkZoneDescriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.network_zone_id):
            query['NetworkZoneId'] = request.network_zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateNetworkZoneDescription',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateNetworkZoneDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_network_zone_description(
        self,
        request: main_models.UpdateNetworkZoneDescriptionRequest,
    ) -> main_models.UpdateNetworkZoneDescriptionResponse:
        runtime = RuntimeOptions()
        return self.update_network_zone_description_with_options(request, runtime)

    async def update_network_zone_description_async(
        self,
        request: main_models.UpdateNetworkZoneDescriptionRequest,
    ) -> main_models.UpdateNetworkZoneDescriptionResponse:
        runtime = RuntimeOptions()
        return await self.update_network_zone_description_with_options_async(request, runtime)

    def update_organizational_unit_with_options(
        self,
        request: main_models.UpdateOrganizationalUnitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateOrganizationalUnitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.organizational_unit_id):
            query['OrganizationalUnitId'] = request.organizational_unit_id
        if not DaraCore.is_null(request.organizational_unit_name):
            query['OrganizationalUnitName'] = request.organizational_unit_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateOrganizationalUnit',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateOrganizationalUnitResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_organizational_unit_with_options_async(
        self,
        request: main_models.UpdateOrganizationalUnitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateOrganizationalUnitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.organizational_unit_id):
            query['OrganizationalUnitId'] = request.organizational_unit_id
        if not DaraCore.is_null(request.organizational_unit_name):
            query['OrganizationalUnitName'] = request.organizational_unit_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateOrganizationalUnit',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateOrganizationalUnitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_organizational_unit(
        self,
        request: main_models.UpdateOrganizationalUnitRequest,
    ) -> main_models.UpdateOrganizationalUnitResponse:
        runtime = RuntimeOptions()
        return self.update_organizational_unit_with_options(request, runtime)

    async def update_organizational_unit_async(
        self,
        request: main_models.UpdateOrganizationalUnitRequest,
    ) -> main_models.UpdateOrganizationalUnitResponse:
        runtime = RuntimeOptions()
        return await self.update_organizational_unit_with_options_async(request, runtime)

    def update_organizational_unit_description_with_options(
        self,
        request: main_models.UpdateOrganizationalUnitDescriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateOrganizationalUnitDescriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.organizational_unit_id):
            query['OrganizationalUnitId'] = request.organizational_unit_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateOrganizationalUnitDescription',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateOrganizationalUnitDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_organizational_unit_description_with_options_async(
        self,
        request: main_models.UpdateOrganizationalUnitDescriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateOrganizationalUnitDescriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.organizational_unit_id):
            query['OrganizationalUnitId'] = request.organizational_unit_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateOrganizationalUnitDescription',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateOrganizationalUnitDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_organizational_unit_description(
        self,
        request: main_models.UpdateOrganizationalUnitDescriptionRequest,
    ) -> main_models.UpdateOrganizationalUnitDescriptionResponse:
        runtime = RuntimeOptions()
        return self.update_organizational_unit_description_with_options(request, runtime)

    async def update_organizational_unit_description_async(
        self,
        request: main_models.UpdateOrganizationalUnitDescriptionRequest,
    ) -> main_models.UpdateOrganizationalUnitDescriptionResponse:
        runtime = RuntimeOptions()
        return await self.update_organizational_unit_description_with_options_async(request, runtime)

    def update_organizational_unit_parent_id_with_options(
        self,
        request: main_models.UpdateOrganizationalUnitParentIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateOrganizationalUnitParentIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.organizational_unit_id):
            query['OrganizationalUnitId'] = request.organizational_unit_id
        if not DaraCore.is_null(request.parent_id):
            query['ParentId'] = request.parent_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateOrganizationalUnitParentId',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateOrganizationalUnitParentIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_organizational_unit_parent_id_with_options_async(
        self,
        request: main_models.UpdateOrganizationalUnitParentIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateOrganizationalUnitParentIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.organizational_unit_id):
            query['OrganizationalUnitId'] = request.organizational_unit_id
        if not DaraCore.is_null(request.parent_id):
            query['ParentId'] = request.parent_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateOrganizationalUnitParentId',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateOrganizationalUnitParentIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_organizational_unit_parent_id(
        self,
        request: main_models.UpdateOrganizationalUnitParentIdRequest,
    ) -> main_models.UpdateOrganizationalUnitParentIdResponse:
        runtime = RuntimeOptions()
        return self.update_organizational_unit_parent_id_with_options(request, runtime)

    async def update_organizational_unit_parent_id_async(
        self,
        request: main_models.UpdateOrganizationalUnitParentIdRequest,
    ) -> main_models.UpdateOrganizationalUnitParentIdResponse:
        runtime = RuntimeOptions()
        return await self.update_organizational_unit_parent_id_with_options_async(request, runtime)

    def update_resource_server_scope_with_options(
        self,
        request: main_models.UpdateResourceServerScopeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateResourceServerScopeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.resource_server_scope_id):
            query['ResourceServerScopeId'] = request.resource_server_scope_id
        if not DaraCore.is_null(request.resource_server_scope_name):
            query['ResourceServerScopeName'] = request.resource_server_scope_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateResourceServerScope',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateResourceServerScopeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_resource_server_scope_with_options_async(
        self,
        request: main_models.UpdateResourceServerScopeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateResourceServerScopeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.resource_server_scope_id):
            query['ResourceServerScopeId'] = request.resource_server_scope_id
        if not DaraCore.is_null(request.resource_server_scope_name):
            query['ResourceServerScopeName'] = request.resource_server_scope_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateResourceServerScope',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateResourceServerScopeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_resource_server_scope(
        self,
        request: main_models.UpdateResourceServerScopeRequest,
    ) -> main_models.UpdateResourceServerScopeResponse:
        runtime = RuntimeOptions()
        return self.update_resource_server_scope_with_options(request, runtime)

    async def update_resource_server_scope_async(
        self,
        request: main_models.UpdateResourceServerScopeRequest,
    ) -> main_models.UpdateResourceServerScopeResponse:
        runtime = RuntimeOptions()
        return await self.update_resource_server_scope_with_options_async(request, runtime)

    def update_user_with_options(
        self,
        request: main_models.UpdateUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.custom_fields):
            query['CustomFields'] = request.custom_fields
        if not DaraCore.is_null(request.display_name):
            query['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.email_verified):
            query['EmailVerified'] = request.email_verified
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.phone_number_verified):
            query['PhoneNumberVerified'] = request.phone_number_verified
        if not DaraCore.is_null(request.phone_region):
            query['PhoneRegion'] = request.phone_region
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUser',
            version = '2021-12-01',
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
        if not DaraCore.is_null(request.custom_fields):
            query['CustomFields'] = request.custom_fields
        if not DaraCore.is_null(request.display_name):
            query['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.email_verified):
            query['EmailVerified'] = request.email_verified
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.phone_number_verified):
            query['PhoneNumberVerified'] = request.phone_number_verified
        if not DaraCore.is_null(request.phone_region):
            query['PhoneRegion'] = request.phone_region
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUser',
            version = '2021-12-01',
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

    def update_user_description_with_options(
        self,
        request: main_models.UpdateUserDescriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserDescriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUserDescription',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUserDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_description_with_options_async(
        self,
        request: main_models.UpdateUserDescriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserDescriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUserDescription',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUserDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user_description(
        self,
        request: main_models.UpdateUserDescriptionRequest,
    ) -> main_models.UpdateUserDescriptionResponse:
        runtime = RuntimeOptions()
        return self.update_user_description_with_options(request, runtime)

    async def update_user_description_async(
        self,
        request: main_models.UpdateUserDescriptionRequest,
    ) -> main_models.UpdateUserDescriptionResponse:
        runtime = RuntimeOptions()
        return await self.update_user_description_with_options_async(request, runtime)

    def update_user_password_with_options(
        self,
        request: main_models.UpdateUserPasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserPasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.password_forced_update_status):
            query['PasswordForcedUpdateStatus'] = request.password_forced_update_status
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.user_notification_channels):
            query['UserNotificationChannels'] = request.user_notification_channels
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUserPassword',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUserPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_password_with_options_async(
        self,
        request: main_models.UpdateUserPasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserPasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.password_forced_update_status):
            query['PasswordForcedUpdateStatus'] = request.password_forced_update_status
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.user_notification_channels):
            query['UserNotificationChannels'] = request.user_notification_channels
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUserPassword',
            version = '2021-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUserPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user_password(
        self,
        request: main_models.UpdateUserPasswordRequest,
    ) -> main_models.UpdateUserPasswordResponse:
        runtime = RuntimeOptions()
        return self.update_user_password_with_options(request, runtime)

    async def update_user_password_async(
        self,
        request: main_models.UpdateUserPasswordRequest,
    ) -> main_models.UpdateUserPasswordResponse:
        runtime = RuntimeOptions()
        return await self.update_user_password_with_options_async(request, runtime)
