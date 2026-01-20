# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_eiam_developerapi20220225 import models as main_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('eiam-developerapi', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_user_to_organizational_units_with_options(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        request: main_models.AddUserToOrganizationalUnitsRequest,
        headers: main_models.AddUserToOrganizationalUnitsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.AddUserToOrganizationalUnitsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.organizational_unit_ids):
            body['organizationalUnitIds'] = request.organizational_unit_ids
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddUserToOrganizationalUnits',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/users/{DaraURL.percent_encode(user_id)}/actions/addUserToOrganizationalUnits',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.AddUserToOrganizationalUnitsResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def add_user_to_organizational_units_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        request: main_models.AddUserToOrganizationalUnitsRequest,
        headers: main_models.AddUserToOrganizationalUnitsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.AddUserToOrganizationalUnitsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.organizational_unit_ids):
            body['organizationalUnitIds'] = request.organizational_unit_ids
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddUserToOrganizationalUnits',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/users/{DaraURL.percent_encode(user_id)}/actions/addUserToOrganizationalUnits',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.AddUserToOrganizationalUnitsResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def add_user_to_organizational_units(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        request: main_models.AddUserToOrganizationalUnitsRequest,
    ) -> main_models.AddUserToOrganizationalUnitsResponse:
        runtime = RuntimeOptions()
        headers = main_models.AddUserToOrganizationalUnitsHeaders()
        return self.add_user_to_organizational_units_with_options(instance_id, application_id, user_id, request, headers, runtime)

    async def add_user_to_organizational_units_async(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        request: main_models.AddUserToOrganizationalUnitsRequest,
    ) -> main_models.AddUserToOrganizationalUnitsResponse:
        runtime = RuntimeOptions()
        headers = main_models.AddUserToOrganizationalUnitsHeaders()
        return await self.add_user_to_organizational_units_with_options_async(instance_id, application_id, user_id, request, headers, runtime)

    def add_users_to_group_with_options(
        self,
        instance_id: str,
        application_id: str,
        group_id: str,
        request: main_models.AddUsersToGroupRequest,
        headers: main_models.AddUsersToGroupHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.AddUsersToGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.user_ids):
            body['userIds'] = request.user_ids
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddUsersToGroup',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/groups/{DaraURL.percent_encode(group_id)}/actions/addUsersToGroup',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.AddUsersToGroupResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def add_users_to_group_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        group_id: str,
        request: main_models.AddUsersToGroupRequest,
        headers: main_models.AddUsersToGroupHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.AddUsersToGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.user_ids):
            body['userIds'] = request.user_ids
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddUsersToGroup',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/groups/{DaraURL.percent_encode(group_id)}/actions/addUsersToGroup',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.AddUsersToGroupResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def add_users_to_group(
        self,
        instance_id: str,
        application_id: str,
        group_id: str,
        request: main_models.AddUsersToGroupRequest,
    ) -> main_models.AddUsersToGroupResponse:
        runtime = RuntimeOptions()
        headers = main_models.AddUsersToGroupHeaders()
        return self.add_users_to_group_with_options(instance_id, application_id, group_id, request, headers, runtime)

    async def add_users_to_group_async(
        self,
        instance_id: str,
        application_id: str,
        group_id: str,
        request: main_models.AddUsersToGroupRequest,
    ) -> main_models.AddUsersToGroupResponse:
        runtime = RuntimeOptions()
        headers = main_models.AddUsersToGroupHeaders()
        return await self.add_users_to_group_with_options_async(instance_id, application_id, group_id, request, headers, runtime)

    def create_group_with_options(
        self,
        instance_id: str,
        application_id: str,
        request: main_models.CreateGroupRequest,
        headers: main_models.CreateGroupHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CreateGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.group_external_id):
            body['groupExternalId'] = request.group_external_id
        if not DaraCore.is_null(request.group_name):
            body['groupName'] = request.group_name
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateGroup',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/groups',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGroupResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def create_group_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        request: main_models.CreateGroupRequest,
        headers: main_models.CreateGroupHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CreateGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.group_external_id):
            body['groupExternalId'] = request.group_external_id
        if not DaraCore.is_null(request.group_name):
            body['groupName'] = request.group_name
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateGroup',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/groups',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGroupResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def create_group(
        self,
        instance_id: str,
        application_id: str,
        request: main_models.CreateGroupRequest,
    ) -> main_models.CreateGroupResponse:
        runtime = RuntimeOptions()
        headers = main_models.CreateGroupHeaders()
        return self.create_group_with_options(instance_id, application_id, request, headers, runtime)

    async def create_group_async(
        self,
        instance_id: str,
        application_id: str,
        request: main_models.CreateGroupRequest,
    ) -> main_models.CreateGroupResponse:
        runtime = RuntimeOptions()
        headers = main_models.CreateGroupHeaders()
        return await self.create_group_with_options_async(instance_id, application_id, request, headers, runtime)

    def create_organizational_unit_with_options(
        self,
        instance_id: str,
        application_id: str,
        request: main_models.CreateOrganizationalUnitRequest,
        headers: main_models.CreateOrganizationalUnitHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOrganizationalUnitResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.organizational_unit_external_id):
            body['organizationalUnitExternalId'] = request.organizational_unit_external_id
        if not DaraCore.is_null(request.organizational_unit_name):
            body['organizationalUnitName'] = request.organizational_unit_name
        if not DaraCore.is_null(request.parent_id):
            body['parentId'] = request.parent_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateOrganizationalUnit',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/organizationalUnits',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOrganizationalUnitResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def create_organizational_unit_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        request: main_models.CreateOrganizationalUnitRequest,
        headers: main_models.CreateOrganizationalUnitHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOrganizationalUnitResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.organizational_unit_external_id):
            body['organizationalUnitExternalId'] = request.organizational_unit_external_id
        if not DaraCore.is_null(request.organizational_unit_name):
            body['organizationalUnitName'] = request.organizational_unit_name
        if not DaraCore.is_null(request.parent_id):
            body['parentId'] = request.parent_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateOrganizationalUnit',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/organizationalUnits',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOrganizationalUnitResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def create_organizational_unit(
        self,
        instance_id: str,
        application_id: str,
        request: main_models.CreateOrganizationalUnitRequest,
    ) -> main_models.CreateOrganizationalUnitResponse:
        runtime = RuntimeOptions()
        headers = main_models.CreateOrganizationalUnitHeaders()
        return self.create_organizational_unit_with_options(instance_id, application_id, request, headers, runtime)

    async def create_organizational_unit_async(
        self,
        instance_id: str,
        application_id: str,
        request: main_models.CreateOrganizationalUnitRequest,
    ) -> main_models.CreateOrganizationalUnitResponse:
        runtime = RuntimeOptions()
        headers = main_models.CreateOrganizationalUnitHeaders()
        return await self.create_organizational_unit_with_options_async(instance_id, application_id, request, headers, runtime)

    def create_user_with_options(
        self,
        instance_id: str,
        application_id: str,
        request: main_models.CreateUserRequest,
        headers: main_models.CreateUserHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUserResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.custom_fields):
            body['customFields'] = request.custom_fields
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.email):
            body['email'] = request.email
        if not DaraCore.is_null(request.email_verified):
            body['emailVerified'] = request.email_verified
        if not DaraCore.is_null(request.password):
            body['password'] = request.password
        if not DaraCore.is_null(request.password_initialization_config):
            body['passwordInitializationConfig'] = request.password_initialization_config
        if not DaraCore.is_null(request.phone_number):
            body['phoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.phone_number_verified):
            body['phoneNumberVerified'] = request.phone_number_verified
        if not DaraCore.is_null(request.phone_region):
            body['phoneRegion'] = request.phone_region
        if not DaraCore.is_null(request.primary_organizational_unit_id):
            body['primaryOrganizationalUnitId'] = request.primary_organizational_unit_id
        if not DaraCore.is_null(request.user_external_id):
            body['userExternalId'] = request.user_external_id
        if not DaraCore.is_null(request.username):
            body['username'] = request.username
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateUser',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/users',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUserResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def create_user_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        request: main_models.CreateUserRequest,
        headers: main_models.CreateUserHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUserResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.custom_fields):
            body['customFields'] = request.custom_fields
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.email):
            body['email'] = request.email
        if not DaraCore.is_null(request.email_verified):
            body['emailVerified'] = request.email_verified
        if not DaraCore.is_null(request.password):
            body['password'] = request.password
        if not DaraCore.is_null(request.password_initialization_config):
            body['passwordInitializationConfig'] = request.password_initialization_config
        if not DaraCore.is_null(request.phone_number):
            body['phoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.phone_number_verified):
            body['phoneNumberVerified'] = request.phone_number_verified
        if not DaraCore.is_null(request.phone_region):
            body['phoneRegion'] = request.phone_region
        if not DaraCore.is_null(request.primary_organizational_unit_id):
            body['primaryOrganizationalUnitId'] = request.primary_organizational_unit_id
        if not DaraCore.is_null(request.user_external_id):
            body['userExternalId'] = request.user_external_id
        if not DaraCore.is_null(request.username):
            body['username'] = request.username
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateUser',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/users',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUserResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def create_user(
        self,
        instance_id: str,
        application_id: str,
        request: main_models.CreateUserRequest,
    ) -> main_models.CreateUserResponse:
        runtime = RuntimeOptions()
        headers = main_models.CreateUserHeaders()
        return self.create_user_with_options(instance_id, application_id, request, headers, runtime)

    async def create_user_async(
        self,
        instance_id: str,
        application_id: str,
        request: main_models.CreateUserRequest,
    ) -> main_models.CreateUserResponse:
        runtime = RuntimeOptions()
        headers = main_models.CreateUserHeaders()
        return await self.create_user_with_options_async(instance_id, application_id, request, headers, runtime)

    def delete_group_with_options(
        self,
        instance_id: str,
        application_id: str,
        group_id: str,
        headers: main_models.DeleteGroupHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGroupResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteGroup',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/groups/{DaraURL.percent_encode(group_id)}',
            method = 'DELETE',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteGroupResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def delete_group_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        group_id: str,
        headers: main_models.DeleteGroupHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGroupResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteGroup',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/groups/{DaraURL.percent_encode(group_id)}',
            method = 'DELETE',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteGroupResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def delete_group(
        self,
        instance_id: str,
        application_id: str,
        group_id: str,
    ) -> main_models.DeleteGroupResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeleteGroupHeaders()
        return self.delete_group_with_options(instance_id, application_id, group_id, headers, runtime)

    async def delete_group_async(
        self,
        instance_id: str,
        application_id: str,
        group_id: str,
    ) -> main_models.DeleteGroupResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeleteGroupHeaders()
        return await self.delete_group_with_options_async(instance_id, application_id, group_id, headers, runtime)

    def delete_organizational_unit_with_options(
        self,
        instance_id: str,
        application_id: str,
        organizational_unit_id: str,
        headers: main_models.DeleteOrganizationalUnitHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteOrganizationalUnitResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteOrganizationalUnit',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/organizationalUnits/{DaraURL.percent_encode(organizational_unit_id)}',
            method = 'DELETE',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteOrganizationalUnitResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def delete_organizational_unit_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        organizational_unit_id: str,
        headers: main_models.DeleteOrganizationalUnitHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteOrganizationalUnitResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteOrganizationalUnit',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/organizationalUnits/{DaraURL.percent_encode(organizational_unit_id)}',
            method = 'DELETE',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteOrganizationalUnitResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def delete_organizational_unit(
        self,
        instance_id: str,
        application_id: str,
        organizational_unit_id: str,
    ) -> main_models.DeleteOrganizationalUnitResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeleteOrganizationalUnitHeaders()
        return self.delete_organizational_unit_with_options(instance_id, application_id, organizational_unit_id, headers, runtime)

    async def delete_organizational_unit_async(
        self,
        instance_id: str,
        application_id: str,
        organizational_unit_id: str,
    ) -> main_models.DeleteOrganizationalUnitResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeleteOrganizationalUnitHeaders()
        return await self.delete_organizational_unit_with_options_async(instance_id, application_id, organizational_unit_id, headers, runtime)

    def delete_user_with_options(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        headers: main_models.DeleteUserHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteUser',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/users/{DaraURL.percent_encode(user_id)}',
            method = 'DELETE',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteUserResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def delete_user_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        headers: main_models.DeleteUserHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteUser',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/users/{DaraURL.percent_encode(user_id)}',
            method = 'DELETE',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteUserResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def delete_user(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
    ) -> main_models.DeleteUserResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeleteUserHeaders()
        return self.delete_user_with_options(instance_id, application_id, user_id, headers, runtime)

    async def delete_user_async(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
    ) -> main_models.DeleteUserResponse:
        runtime = RuntimeOptions()
        headers = main_models.DeleteUserHeaders()
        return await self.delete_user_with_options_async(instance_id, application_id, user_id, headers, runtime)

    def disable_user_with_options(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        headers: main_models.DisableUserHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DisableUserResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'DisableUser',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/users/{DaraURL.percent_encode(user_id)}/actions/disable',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DisableUserResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def disable_user_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        headers: main_models.DisableUserHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.DisableUserResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'DisableUser',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/users/{DaraURL.percent_encode(user_id)}/actions/disable',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DisableUserResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def disable_user(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
    ) -> main_models.DisableUserResponse:
        runtime = RuntimeOptions()
        headers = main_models.DisableUserHeaders()
        return self.disable_user_with_options(instance_id, application_id, user_id, headers, runtime)

    async def disable_user_async(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
    ) -> main_models.DisableUserResponse:
        runtime = RuntimeOptions()
        headers = main_models.DisableUserHeaders()
        return await self.disable_user_with_options_async(instance_id, application_id, user_id, headers, runtime)

    def enable_user_with_options(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        headers: main_models.EnableUserHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.EnableUserResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'EnableUser',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/users/{DaraURL.percent_encode(user_id)}/actions/enable',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.EnableUserResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def enable_user_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        headers: main_models.EnableUserHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.EnableUserResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'EnableUser',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/users/{DaraURL.percent_encode(user_id)}/actions/enable',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.EnableUserResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def enable_user(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
    ) -> main_models.EnableUserResponse:
        runtime = RuntimeOptions()
        headers = main_models.EnableUserHeaders()
        return self.enable_user_with_options(instance_id, application_id, user_id, headers, runtime)

    async def enable_user_async(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
    ) -> main_models.EnableUserResponse:
        runtime = RuntimeOptions()
        headers = main_models.EnableUserHeaders()
        return await self.enable_user_with_options_async(instance_id, application_id, user_id, headers, runtime)

    def generate_device_code_with_options(
        self,
        instance_id: str,
        application_id: str,
        request: main_models.GenerateDeviceCodeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GenerateDeviceCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.scope):
            query['scope'] = request.scope
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateDeviceCode',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/oauth2/device/code',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateDeviceCodeResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def generate_device_code_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        request: main_models.GenerateDeviceCodeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GenerateDeviceCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.scope):
            query['scope'] = request.scope
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateDeviceCode',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/oauth2/device/code',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateDeviceCodeResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def generate_device_code(
        self,
        instance_id: str,
        application_id: str,
        request: main_models.GenerateDeviceCodeRequest,
    ) -> main_models.GenerateDeviceCodeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.generate_device_code_with_options(instance_id, application_id, request, headers, runtime)

    async def generate_device_code_async(
        self,
        instance_id: str,
        application_id: str,
        request: main_models.GenerateDeviceCodeRequest,
    ) -> main_models.GenerateDeviceCodeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.generate_device_code_with_options_async(instance_id, application_id, request, headers, runtime)

    def generate_token_with_options(
        self,
        instance_id: str,
        application_id: str,
        request: main_models.GenerateTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GenerateTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['client_id'] = request.client_id
        if not DaraCore.is_null(request.client_secret):
            query['client_secret'] = request.client_secret
        if not DaraCore.is_null(request.code):
            query['code'] = request.code
        if not DaraCore.is_null(request.code_verifier):
            query['code_verifier'] = request.code_verifier
        if not DaraCore.is_null(request.device_code):
            query['device_code'] = request.device_code
        if not DaraCore.is_null(request.exclusive_tag):
            query['exclusive_tag'] = request.exclusive_tag
        if not DaraCore.is_null(request.grant_type):
            query['grant_type'] = request.grant_type
        if not DaraCore.is_null(request.password):
            query['password'] = request.password
        if not DaraCore.is_null(request.redirect_uri):
            query['redirect_uri'] = request.redirect_uri
        if not DaraCore.is_null(request.refresh_token):
            query['refresh_token'] = request.refresh_token
        if not DaraCore.is_null(request.scope):
            query['scope'] = request.scope
        if not DaraCore.is_null(request.username):
            query['username'] = request.username
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateToken',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/oauth2/token',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateTokenResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def generate_token_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        request: main_models.GenerateTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GenerateTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['client_id'] = request.client_id
        if not DaraCore.is_null(request.client_secret):
            query['client_secret'] = request.client_secret
        if not DaraCore.is_null(request.code):
            query['code'] = request.code
        if not DaraCore.is_null(request.code_verifier):
            query['code_verifier'] = request.code_verifier
        if not DaraCore.is_null(request.device_code):
            query['device_code'] = request.device_code
        if not DaraCore.is_null(request.exclusive_tag):
            query['exclusive_tag'] = request.exclusive_tag
        if not DaraCore.is_null(request.grant_type):
            query['grant_type'] = request.grant_type
        if not DaraCore.is_null(request.password):
            query['password'] = request.password
        if not DaraCore.is_null(request.redirect_uri):
            query['redirect_uri'] = request.redirect_uri
        if not DaraCore.is_null(request.refresh_token):
            query['refresh_token'] = request.refresh_token
        if not DaraCore.is_null(request.scope):
            query['scope'] = request.scope
        if not DaraCore.is_null(request.username):
            query['username'] = request.username
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateToken',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/oauth2/token',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateTokenResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def generate_token(
        self,
        instance_id: str,
        application_id: str,
        request: main_models.GenerateTokenRequest,
    ) -> main_models.GenerateTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.generate_token_with_options(instance_id, application_id, request, headers, runtime)

    async def generate_token_async(
        self,
        instance_id: str,
        application_id: str,
        request: main_models.GenerateTokenRequest,
    ) -> main_models.GenerateTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.generate_token_with_options_async(instance_id, application_id, request, headers, runtime)

    def get_application_provisioning_scope_with_options(
        self,
        instance_id: str,
        application_id: str,
        headers: main_models.GetApplicationProvisioningScopeHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetApplicationProvisioningScopeResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'GetApplicationProvisioningScope',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/provisioningScope',
            method = 'GET',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApplicationProvisioningScopeResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def get_application_provisioning_scope_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        headers: main_models.GetApplicationProvisioningScopeHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetApplicationProvisioningScopeResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'GetApplicationProvisioningScope',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/provisioningScope',
            method = 'GET',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApplicationProvisioningScopeResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def get_application_provisioning_scope(
        self,
        instance_id: str,
        application_id: str,
    ) -> main_models.GetApplicationProvisioningScopeResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetApplicationProvisioningScopeHeaders()
        return self.get_application_provisioning_scope_with_options(instance_id, application_id, headers, runtime)

    async def get_application_provisioning_scope_async(
        self,
        instance_id: str,
        application_id: str,
    ) -> main_models.GetApplicationProvisioningScopeResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetApplicationProvisioningScopeHeaders()
        return await self.get_application_provisioning_scope_with_options_async(instance_id, application_id, headers, runtime)

    def get_group_with_options(
        self,
        instance_id: str,
        application_id: str,
        group_id: str,
        headers: main_models.GetGroupHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetGroupResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'GetGroup',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/groups/{DaraURL.percent_encode(group_id)}',
            method = 'GET',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGroupResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def get_group_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        group_id: str,
        headers: main_models.GetGroupHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetGroupResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'GetGroup',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/groups/{DaraURL.percent_encode(group_id)}',
            method = 'GET',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGroupResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def get_group(
        self,
        instance_id: str,
        application_id: str,
        group_id: str,
    ) -> main_models.GetGroupResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetGroupHeaders()
        return self.get_group_with_options(instance_id, application_id, group_id, headers, runtime)

    async def get_group_async(
        self,
        instance_id: str,
        application_id: str,
        group_id: str,
    ) -> main_models.GetGroupResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetGroupHeaders()
        return await self.get_group_with_options_async(instance_id, application_id, group_id, headers, runtime)

    def get_organizational_unit_with_options(
        self,
        instance_id: str,
        application_id: str,
        organizational_unit_id: str,
        headers: main_models.GetOrganizationalUnitHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetOrganizationalUnitResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'GetOrganizationalUnit',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/organizationalUnits/{DaraURL.percent_encode(organizational_unit_id)}',
            method = 'GET',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOrganizationalUnitResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def get_organizational_unit_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        organizational_unit_id: str,
        headers: main_models.GetOrganizationalUnitHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetOrganizationalUnitResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'GetOrganizationalUnit',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/organizationalUnits/{DaraURL.percent_encode(organizational_unit_id)}',
            method = 'GET',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOrganizationalUnitResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def get_organizational_unit(
        self,
        instance_id: str,
        application_id: str,
        organizational_unit_id: str,
    ) -> main_models.GetOrganizationalUnitResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetOrganizationalUnitHeaders()
        return self.get_organizational_unit_with_options(instance_id, application_id, organizational_unit_id, headers, runtime)

    async def get_organizational_unit_async(
        self,
        instance_id: str,
        application_id: str,
        organizational_unit_id: str,
    ) -> main_models.GetOrganizationalUnitResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetOrganizationalUnitHeaders()
        return await self.get_organizational_unit_with_options_async(instance_id, application_id, organizational_unit_id, headers, runtime)

    def get_organizational_unit_id_by_external_id_with_options(
        self,
        instance_id: str,
        application_id: str,
        request: main_models.GetOrganizationalUnitIdByExternalIdRequest,
        headers: main_models.GetOrganizationalUnitIdByExternalIdHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetOrganizationalUnitIdByExternalIdResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.organizational_unit_external_id):
            body['organizationalUnitExternalId'] = request.organizational_unit_external_id
        if not DaraCore.is_null(request.organizational_unit_source_id):
            body['organizationalUnitSourceId'] = request.organizational_unit_source_id
        if not DaraCore.is_null(request.organizational_unit_source_type):
            body['organizationalUnitSourceType'] = request.organizational_unit_source_type
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetOrganizationalUnitIdByExternalId',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/organizationalUnits/_/actions/getOrganizationalUnitIdByExternalId',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOrganizationalUnitIdByExternalIdResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def get_organizational_unit_id_by_external_id_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        request: main_models.GetOrganizationalUnitIdByExternalIdRequest,
        headers: main_models.GetOrganizationalUnitIdByExternalIdHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetOrganizationalUnitIdByExternalIdResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.organizational_unit_external_id):
            body['organizationalUnitExternalId'] = request.organizational_unit_external_id
        if not DaraCore.is_null(request.organizational_unit_source_id):
            body['organizationalUnitSourceId'] = request.organizational_unit_source_id
        if not DaraCore.is_null(request.organizational_unit_source_type):
            body['organizationalUnitSourceType'] = request.organizational_unit_source_type
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetOrganizationalUnitIdByExternalId',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/organizationalUnits/_/actions/getOrganizationalUnitIdByExternalId',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOrganizationalUnitIdByExternalIdResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def get_organizational_unit_id_by_external_id(
        self,
        instance_id: str,
        application_id: str,
        request: main_models.GetOrganizationalUnitIdByExternalIdRequest,
    ) -> main_models.GetOrganizationalUnitIdByExternalIdResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetOrganizationalUnitIdByExternalIdHeaders()
        return self.get_organizational_unit_id_by_external_id_with_options(instance_id, application_id, request, headers, runtime)

    async def get_organizational_unit_id_by_external_id_async(
        self,
        instance_id: str,
        application_id: str,
        request: main_models.GetOrganizationalUnitIdByExternalIdRequest,
    ) -> main_models.GetOrganizationalUnitIdByExternalIdResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetOrganizationalUnitIdByExternalIdHeaders()
        return await self.get_organizational_unit_id_by_external_id_with_options_async(instance_id, application_id, request, headers, runtime)

    def get_user_with_options(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        headers: main_models.GetUserHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'GetUser',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/users/{DaraURL.percent_encode(user_id)}',
            method = 'GET',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def get_user_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        headers: main_models.GetUserHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'GetUser',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/users/{DaraURL.percent_encode(user_id)}',
            method = 'GET',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def get_user(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
    ) -> main_models.GetUserResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetUserHeaders()
        return self.get_user_with_options(instance_id, application_id, user_id, headers, runtime)

    async def get_user_async(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
    ) -> main_models.GetUserResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetUserHeaders()
        return await self.get_user_with_options_async(instance_id, application_id, user_id, headers, runtime)

    def get_user_id_by_email_with_options(
        self,
        instance_id: str,
        application_id: str,
        request: main_models.GetUserIdByEmailRequest,
        headers: main_models.GetUserIdByEmailHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserIdByEmailResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.email):
            body['email'] = request.email
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetUserIdByEmail',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/users/_/actions/getUserIdByEmail',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserIdByEmailResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def get_user_id_by_email_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        request: main_models.GetUserIdByEmailRequest,
        headers: main_models.GetUserIdByEmailHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserIdByEmailResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.email):
            body['email'] = request.email
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetUserIdByEmail',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/users/_/actions/getUserIdByEmail',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserIdByEmailResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def get_user_id_by_email(
        self,
        instance_id: str,
        application_id: str,
        request: main_models.GetUserIdByEmailRequest,
    ) -> main_models.GetUserIdByEmailResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetUserIdByEmailHeaders()
        return self.get_user_id_by_email_with_options(instance_id, application_id, request, headers, runtime)

    async def get_user_id_by_email_async(
        self,
        instance_id: str,
        application_id: str,
        request: main_models.GetUserIdByEmailRequest,
    ) -> main_models.GetUserIdByEmailResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetUserIdByEmailHeaders()
        return await self.get_user_id_by_email_with_options_async(instance_id, application_id, request, headers, runtime)

    def get_user_id_by_phone_number_with_options(
        self,
        instance_id: str,
        application_id: str,
        request: main_models.GetUserIdByPhoneNumberRequest,
        headers: main_models.GetUserIdByPhoneNumberHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserIdByPhoneNumberResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.phone_number):
            body['phoneNumber'] = request.phone_number
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetUserIdByPhoneNumber',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/users/_/actions/getUserIdByPhoneNumber',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserIdByPhoneNumberResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def get_user_id_by_phone_number_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        request: main_models.GetUserIdByPhoneNumberRequest,
        headers: main_models.GetUserIdByPhoneNumberHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserIdByPhoneNumberResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.phone_number):
            body['phoneNumber'] = request.phone_number
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetUserIdByPhoneNumber',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/users/_/actions/getUserIdByPhoneNumber',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserIdByPhoneNumberResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def get_user_id_by_phone_number(
        self,
        instance_id: str,
        application_id: str,
        request: main_models.GetUserIdByPhoneNumberRequest,
    ) -> main_models.GetUserIdByPhoneNumberResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetUserIdByPhoneNumberHeaders()
        return self.get_user_id_by_phone_number_with_options(instance_id, application_id, request, headers, runtime)

    async def get_user_id_by_phone_number_async(
        self,
        instance_id: str,
        application_id: str,
        request: main_models.GetUserIdByPhoneNumberRequest,
    ) -> main_models.GetUserIdByPhoneNumberResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetUserIdByPhoneNumberHeaders()
        return await self.get_user_id_by_phone_number_with_options_async(instance_id, application_id, request, headers, runtime)

    def get_user_id_by_user_external_id_with_options(
        self,
        instance_id: str,
        application_id: str,
        request: main_models.GetUserIdByUserExternalIdRequest,
        headers: main_models.GetUserIdByUserExternalIdHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserIdByUserExternalIdResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.user_external_id):
            body['userExternalId'] = request.user_external_id
        if not DaraCore.is_null(request.user_source_id):
            body['userSourceId'] = request.user_source_id
        if not DaraCore.is_null(request.user_source_type):
            body['userSourceType'] = request.user_source_type
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetUserIdByUserExternalId',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/users/_/actions/getUserIdByExternalId',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserIdByUserExternalIdResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def get_user_id_by_user_external_id_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        request: main_models.GetUserIdByUserExternalIdRequest,
        headers: main_models.GetUserIdByUserExternalIdHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserIdByUserExternalIdResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.user_external_id):
            body['userExternalId'] = request.user_external_id
        if not DaraCore.is_null(request.user_source_id):
            body['userSourceId'] = request.user_source_id
        if not DaraCore.is_null(request.user_source_type):
            body['userSourceType'] = request.user_source_type
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetUserIdByUserExternalId',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/users/_/actions/getUserIdByExternalId',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserIdByUserExternalIdResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def get_user_id_by_user_external_id(
        self,
        instance_id: str,
        application_id: str,
        request: main_models.GetUserIdByUserExternalIdRequest,
    ) -> main_models.GetUserIdByUserExternalIdResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetUserIdByUserExternalIdHeaders()
        return self.get_user_id_by_user_external_id_with_options(instance_id, application_id, request, headers, runtime)

    async def get_user_id_by_user_external_id_async(
        self,
        instance_id: str,
        application_id: str,
        request: main_models.GetUserIdByUserExternalIdRequest,
    ) -> main_models.GetUserIdByUserExternalIdResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetUserIdByUserExternalIdHeaders()
        return await self.get_user_id_by_user_external_id_with_options_async(instance_id, application_id, request, headers, runtime)

    def get_user_id_by_username_with_options(
        self,
        instance_id: str,
        application_id: str,
        request: main_models.GetUserIdByUsernameRequest,
        headers: main_models.GetUserIdByUsernameHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserIdByUsernameResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.username):
            body['username'] = request.username
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetUserIdByUsername',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/users/_/actions/getUserIdByUsername',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserIdByUsernameResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def get_user_id_by_username_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        request: main_models.GetUserIdByUsernameRequest,
        headers: main_models.GetUserIdByUsernameHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserIdByUsernameResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.username):
            body['username'] = request.username
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetUserIdByUsername',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/users/_/actions/getUserIdByUsername',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserIdByUsernameResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def get_user_id_by_username(
        self,
        instance_id: str,
        application_id: str,
        request: main_models.GetUserIdByUsernameRequest,
    ) -> main_models.GetUserIdByUsernameResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetUserIdByUsernameHeaders()
        return self.get_user_id_by_username_with_options(instance_id, application_id, request, headers, runtime)

    async def get_user_id_by_username_async(
        self,
        instance_id: str,
        application_id: str,
        request: main_models.GetUserIdByUsernameRequest,
    ) -> main_models.GetUserIdByUsernameResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetUserIdByUsernameHeaders()
        return await self.get_user_id_by_username_with_options_async(instance_id, application_id, request, headers, runtime)

    def get_user_info_with_options(
        self,
        instance_id: str,
        application_id: str,
        headers: main_models.GetUserInfoHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserInfoResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'GetUserInfo',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/oauth2/userinfo',
            method = 'GET',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserInfoResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def get_user_info_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        headers: main_models.GetUserInfoHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserInfoResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'GetUserInfo',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/oauth2/userinfo',
            method = 'GET',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserInfoResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def get_user_info(
        self,
        instance_id: str,
        application_id: str,
    ) -> main_models.GetUserInfoResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetUserInfoHeaders()
        return self.get_user_info_with_options(instance_id, application_id, headers, runtime)

    async def get_user_info_async(
        self,
        instance_id: str,
        application_id: str,
    ) -> main_models.GetUserInfoResponse:
        runtime = RuntimeOptions()
        headers = main_models.GetUserInfoHeaders()
        return await self.get_user_info_with_options_async(instance_id, application_id, headers, runtime)

    def list_groups_with_options(
        self,
        instance_id: str,
        application_id: str,
        request: main_models.ListGroupsRequest,
        headers: main_models.ListGroupsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_name_start_with):
            query['groupNameStartWith'] = request.group_name_start_with
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGroups',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/groups',
            method = 'GET',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGroupsResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def list_groups_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        request: main_models.ListGroupsRequest,
        headers: main_models.ListGroupsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_name_start_with):
            query['groupNameStartWith'] = request.group_name_start_with
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGroups',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/groups',
            method = 'GET',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGroupsResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def list_groups(
        self,
        instance_id: str,
        application_id: str,
        request: main_models.ListGroupsRequest,
    ) -> main_models.ListGroupsResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListGroupsHeaders()
        return self.list_groups_with_options(instance_id, application_id, request, headers, runtime)

    async def list_groups_async(
        self,
        instance_id: str,
        application_id: str,
        request: main_models.ListGroupsRequest,
    ) -> main_models.ListGroupsResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListGroupsHeaders()
        return await self.list_groups_with_options_async(instance_id, application_id, request, headers, runtime)

    def list_groups_for_user_with_options(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        request: main_models.ListGroupsForUserRequest,
        headers: main_models.ListGroupsForUserHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListGroupsForUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGroupsForUser',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/users/{DaraURL.percent_encode(user_id)}/actions/listGroupsForUser',
            method = 'GET',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGroupsForUserResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def list_groups_for_user_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        request: main_models.ListGroupsForUserRequest,
        headers: main_models.ListGroupsForUserHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListGroupsForUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGroupsForUser',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/users/{DaraURL.percent_encode(user_id)}/actions/listGroupsForUser',
            method = 'GET',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGroupsForUserResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def list_groups_for_user(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        request: main_models.ListGroupsForUserRequest,
    ) -> main_models.ListGroupsForUserResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListGroupsForUserHeaders()
        return self.list_groups_for_user_with_options(instance_id, application_id, user_id, request, headers, runtime)

    async def list_groups_for_user_async(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        request: main_models.ListGroupsForUserRequest,
    ) -> main_models.ListGroupsForUserResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListGroupsForUserHeaders()
        return await self.list_groups_for_user_with_options_async(instance_id, application_id, user_id, request, headers, runtime)

    def list_organizational_unit_parent_ids_with_options(
        self,
        instance_id: str,
        application_id: str,
        organizational_unit_id: str,
        headers: main_models.ListOrganizationalUnitParentIdsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListOrganizationalUnitParentIdsResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'ListOrganizationalUnitParentIds',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/organizationalUnits/{DaraURL.percent_encode(organizational_unit_id)}/parentIds',
            method = 'GET',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOrganizationalUnitParentIdsResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def list_organizational_unit_parent_ids_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        organizational_unit_id: str,
        headers: main_models.ListOrganizationalUnitParentIdsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListOrganizationalUnitParentIdsResponse:
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers
        )
        params = open_api_util_models.Params(
            action = 'ListOrganizationalUnitParentIds',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/organizationalUnits/{DaraURL.percent_encode(organizational_unit_id)}/parentIds',
            method = 'GET',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOrganizationalUnitParentIdsResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def list_organizational_unit_parent_ids(
        self,
        instance_id: str,
        application_id: str,
        organizational_unit_id: str,
    ) -> main_models.ListOrganizationalUnitParentIdsResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListOrganizationalUnitParentIdsHeaders()
        return self.list_organizational_unit_parent_ids_with_options(instance_id, application_id, organizational_unit_id, headers, runtime)

    async def list_organizational_unit_parent_ids_async(
        self,
        instance_id: str,
        application_id: str,
        organizational_unit_id: str,
    ) -> main_models.ListOrganizationalUnitParentIdsResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListOrganizationalUnitParentIdsHeaders()
        return await self.list_organizational_unit_parent_ids_with_options_async(instance_id, application_id, organizational_unit_id, headers, runtime)

    def list_organizational_units_with_options(
        self,
        instance_id: str,
        application_id: str,
        request: main_models.ListOrganizationalUnitsRequest,
        headers: main_models.ListOrganizationalUnitsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListOrganizationalUnitsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.parent_id):
            query['parentId'] = request.parent_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOrganizationalUnits',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/organizationalUnits',
            method = 'GET',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOrganizationalUnitsResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def list_organizational_units_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        request: main_models.ListOrganizationalUnitsRequest,
        headers: main_models.ListOrganizationalUnitsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListOrganizationalUnitsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.parent_id):
            query['parentId'] = request.parent_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOrganizationalUnits',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/organizationalUnits',
            method = 'GET',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOrganizationalUnitsResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def list_organizational_units(
        self,
        instance_id: str,
        application_id: str,
        request: main_models.ListOrganizationalUnitsRequest,
    ) -> main_models.ListOrganizationalUnitsResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListOrganizationalUnitsHeaders()
        return self.list_organizational_units_with_options(instance_id, application_id, request, headers, runtime)

    async def list_organizational_units_async(
        self,
        instance_id: str,
        application_id: str,
        request: main_models.ListOrganizationalUnitsRequest,
    ) -> main_models.ListOrganizationalUnitsResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListOrganizationalUnitsHeaders()
        return await self.list_organizational_units_with_options_async(instance_id, application_id, request, headers, runtime)

    def list_users_with_options(
        self,
        instance_id: str,
        application_id: str,
        request: main_models.ListUsersRequest,
        headers: main_models.ListUsersHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.organizational_unit_id):
            query['organizationalUnitId'] = request.organizational_unit_id
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUsers',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/users',
            method = 'GET',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUsersResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def list_users_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        request: main_models.ListUsersRequest,
        headers: main_models.ListUsersHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.organizational_unit_id):
            query['organizationalUnitId'] = request.organizational_unit_id
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUsers',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/users',
            method = 'GET',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUsersResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def list_users(
        self,
        instance_id: str,
        application_id: str,
        request: main_models.ListUsersRequest,
    ) -> main_models.ListUsersResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListUsersHeaders()
        return self.list_users_with_options(instance_id, application_id, request, headers, runtime)

    async def list_users_async(
        self,
        instance_id: str,
        application_id: str,
        request: main_models.ListUsersRequest,
    ) -> main_models.ListUsersResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListUsersHeaders()
        return await self.list_users_with_options_async(instance_id, application_id, request, headers, runtime)

    def list_users_for_group_with_options(
        self,
        instance_id: str,
        application_id: str,
        group_id: str,
        request: main_models.ListUsersForGroupRequest,
        headers: main_models.ListUsersForGroupHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListUsersForGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUsersForGroup',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/groups/{DaraURL.percent_encode(group_id)}/actions/listUsersForGroup',
            method = 'GET',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUsersForGroupResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def list_users_for_group_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        group_id: str,
        request: main_models.ListUsersForGroupRequest,
        headers: main_models.ListUsersForGroupHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ListUsersForGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUsersForGroup',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/groups/{DaraURL.percent_encode(group_id)}/actions/listUsersForGroup',
            method = 'GET',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUsersForGroupResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def list_users_for_group(
        self,
        instance_id: str,
        application_id: str,
        group_id: str,
        request: main_models.ListUsersForGroupRequest,
    ) -> main_models.ListUsersForGroupResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListUsersForGroupHeaders()
        return self.list_users_for_group_with_options(instance_id, application_id, group_id, request, headers, runtime)

    async def list_users_for_group_async(
        self,
        instance_id: str,
        application_id: str,
        group_id: str,
        request: main_models.ListUsersForGroupRequest,
    ) -> main_models.ListUsersForGroupResponse:
        runtime = RuntimeOptions()
        headers = main_models.ListUsersForGroupHeaders()
        return await self.list_users_for_group_with_options_async(instance_id, application_id, group_id, request, headers, runtime)

    def obtain_cloud_account_role_access_credential_with_options(
        self,
        instance_id: str,
        request: main_models.ObtainCloudAccountRoleAccessCredentialRequest,
        headers: main_models.ObtainCloudAccountRoleAccessCredentialHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ObtainCloudAccountRoleAccessCredentialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cloud_account_role_external_id):
            query['cloudAccountRoleExternalId'] = request.cloud_account_role_external_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ObtainCloudAccountRoleAccessCredential',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/cloudAccountRoles/_/actions/obtainAccessCredential',
            method = 'GET',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ObtainCloudAccountRoleAccessCredentialResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def obtain_cloud_account_role_access_credential_with_options_async(
        self,
        instance_id: str,
        request: main_models.ObtainCloudAccountRoleAccessCredentialRequest,
        headers: main_models.ObtainCloudAccountRoleAccessCredentialHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.ObtainCloudAccountRoleAccessCredentialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cloud_account_role_external_id):
            query['cloudAccountRoleExternalId'] = request.cloud_account_role_external_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ObtainCloudAccountRoleAccessCredential',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/cloudAccountRoles/_/actions/obtainAccessCredential',
            method = 'GET',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ObtainCloudAccountRoleAccessCredentialResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def obtain_cloud_account_role_access_credential(
        self,
        instance_id: str,
        request: main_models.ObtainCloudAccountRoleAccessCredentialRequest,
    ) -> main_models.ObtainCloudAccountRoleAccessCredentialResponse:
        runtime = RuntimeOptions()
        headers = main_models.ObtainCloudAccountRoleAccessCredentialHeaders()
        return self.obtain_cloud_account_role_access_credential_with_options(instance_id, request, headers, runtime)

    async def obtain_cloud_account_role_access_credential_async(
        self,
        instance_id: str,
        request: main_models.ObtainCloudAccountRoleAccessCredentialRequest,
    ) -> main_models.ObtainCloudAccountRoleAccessCredentialResponse:
        runtime = RuntimeOptions()
        headers = main_models.ObtainCloudAccountRoleAccessCredentialHeaders()
        return await self.obtain_cloud_account_role_access_credential_with_options_async(instance_id, request, headers, runtime)

    def patch_group_with_options(
        self,
        instance_id: str,
        application_id: str,
        group_id: str,
        request: main_models.PatchGroupRequest,
        headers: main_models.PatchGroupHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.PatchGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.group_name):
            body['groupName'] = request.group_name
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PatchGroup',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/groups/{DaraURL.percent_encode(group_id)}',
            method = 'PATCH',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.PatchGroupResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def patch_group_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        group_id: str,
        request: main_models.PatchGroupRequest,
        headers: main_models.PatchGroupHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.PatchGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.group_name):
            body['groupName'] = request.group_name
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PatchGroup',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/groups/{DaraURL.percent_encode(group_id)}',
            method = 'PATCH',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.PatchGroupResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def patch_group(
        self,
        instance_id: str,
        application_id: str,
        group_id: str,
        request: main_models.PatchGroupRequest,
    ) -> main_models.PatchGroupResponse:
        runtime = RuntimeOptions()
        headers = main_models.PatchGroupHeaders()
        return self.patch_group_with_options(instance_id, application_id, group_id, request, headers, runtime)

    async def patch_group_async(
        self,
        instance_id: str,
        application_id: str,
        group_id: str,
        request: main_models.PatchGroupRequest,
    ) -> main_models.PatchGroupResponse:
        runtime = RuntimeOptions()
        headers = main_models.PatchGroupHeaders()
        return await self.patch_group_with_options_async(instance_id, application_id, group_id, request, headers, runtime)

    def patch_organizational_unit_with_options(
        self,
        instance_id: str,
        application_id: str,
        organizational_unit_id: str,
        request: main_models.PatchOrganizationalUnitRequest,
        headers: main_models.PatchOrganizationalUnitHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.PatchOrganizationalUnitResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.organizational_unit_name):
            body['organizationalUnitName'] = request.organizational_unit_name
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PatchOrganizationalUnit',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/organizationalUnits/{DaraURL.percent_encode(organizational_unit_id)}',
            method = 'PATCH',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.PatchOrganizationalUnitResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def patch_organizational_unit_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        organizational_unit_id: str,
        request: main_models.PatchOrganizationalUnitRequest,
        headers: main_models.PatchOrganizationalUnitHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.PatchOrganizationalUnitResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.organizational_unit_name):
            body['organizationalUnitName'] = request.organizational_unit_name
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PatchOrganizationalUnit',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/organizationalUnits/{DaraURL.percent_encode(organizational_unit_id)}',
            method = 'PATCH',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.PatchOrganizationalUnitResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def patch_organizational_unit(
        self,
        instance_id: str,
        application_id: str,
        organizational_unit_id: str,
        request: main_models.PatchOrganizationalUnitRequest,
    ) -> main_models.PatchOrganizationalUnitResponse:
        runtime = RuntimeOptions()
        headers = main_models.PatchOrganizationalUnitHeaders()
        return self.patch_organizational_unit_with_options(instance_id, application_id, organizational_unit_id, request, headers, runtime)

    async def patch_organizational_unit_async(
        self,
        instance_id: str,
        application_id: str,
        organizational_unit_id: str,
        request: main_models.PatchOrganizationalUnitRequest,
    ) -> main_models.PatchOrganizationalUnitResponse:
        runtime = RuntimeOptions()
        headers = main_models.PatchOrganizationalUnitHeaders()
        return await self.patch_organizational_unit_with_options_async(instance_id, application_id, organizational_unit_id, request, headers, runtime)

    def patch_user_with_options(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        request: main_models.PatchUserRequest,
        headers: main_models.PatchUserHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.PatchUserResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.custom_fields):
            body['customFields'] = request.custom_fields
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.email):
            body['email'] = request.email
        if not DaraCore.is_null(request.email_verified):
            body['emailVerified'] = request.email_verified
        if not DaraCore.is_null(request.phone_number):
            body['phoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.phone_number_verified):
            body['phoneNumberVerified'] = request.phone_number_verified
        if not DaraCore.is_null(request.phone_region):
            body['phoneRegion'] = request.phone_region
        if not DaraCore.is_null(request.username):
            body['username'] = request.username
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PatchUser',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/users/{DaraURL.percent_encode(user_id)}',
            method = 'PATCH',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.PatchUserResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def patch_user_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        request: main_models.PatchUserRequest,
        headers: main_models.PatchUserHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.PatchUserResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.custom_fields):
            body['customFields'] = request.custom_fields
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.email):
            body['email'] = request.email
        if not DaraCore.is_null(request.email_verified):
            body['emailVerified'] = request.email_verified
        if not DaraCore.is_null(request.phone_number):
            body['phoneNumber'] = request.phone_number
        if not DaraCore.is_null(request.phone_number_verified):
            body['phoneNumberVerified'] = request.phone_number_verified
        if not DaraCore.is_null(request.phone_region):
            body['phoneRegion'] = request.phone_region
        if not DaraCore.is_null(request.username):
            body['username'] = request.username
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PatchUser',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/users/{DaraURL.percent_encode(user_id)}',
            method = 'PATCH',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.PatchUserResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def patch_user(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        request: main_models.PatchUserRequest,
    ) -> main_models.PatchUserResponse:
        runtime = RuntimeOptions()
        headers = main_models.PatchUserHeaders()
        return self.patch_user_with_options(instance_id, application_id, user_id, request, headers, runtime)

    async def patch_user_async(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        request: main_models.PatchUserRequest,
    ) -> main_models.PatchUserResponse:
        runtime = RuntimeOptions()
        headers = main_models.PatchUserHeaders()
        return await self.patch_user_with_options_async(instance_id, application_id, user_id, request, headers, runtime)

    def remove_user_from_organizational_units_with_options(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        request: main_models.RemoveUserFromOrganizationalUnitsRequest,
        headers: main_models.RemoveUserFromOrganizationalUnitsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveUserFromOrganizationalUnitsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.organizational_unit_ids):
            body['organizationalUnitIds'] = request.organizational_unit_ids
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RemoveUserFromOrganizationalUnits',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/users/{DaraURL.percent_encode(user_id)}/actions/removeUserFromOrganizationalUnits',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.RemoveUserFromOrganizationalUnitsResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def remove_user_from_organizational_units_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        request: main_models.RemoveUserFromOrganizationalUnitsRequest,
        headers: main_models.RemoveUserFromOrganizationalUnitsHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveUserFromOrganizationalUnitsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.organizational_unit_ids):
            body['organizationalUnitIds'] = request.organizational_unit_ids
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RemoveUserFromOrganizationalUnits',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/users/{DaraURL.percent_encode(user_id)}/actions/removeUserFromOrganizationalUnits',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.RemoveUserFromOrganizationalUnitsResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def remove_user_from_organizational_units(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        request: main_models.RemoveUserFromOrganizationalUnitsRequest,
    ) -> main_models.RemoveUserFromOrganizationalUnitsResponse:
        runtime = RuntimeOptions()
        headers = main_models.RemoveUserFromOrganizationalUnitsHeaders()
        return self.remove_user_from_organizational_units_with_options(instance_id, application_id, user_id, request, headers, runtime)

    async def remove_user_from_organizational_units_async(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        request: main_models.RemoveUserFromOrganizationalUnitsRequest,
    ) -> main_models.RemoveUserFromOrganizationalUnitsResponse:
        runtime = RuntimeOptions()
        headers = main_models.RemoveUserFromOrganizationalUnitsHeaders()
        return await self.remove_user_from_organizational_units_with_options_async(instance_id, application_id, user_id, request, headers, runtime)

    def remove_users_from_group_with_options(
        self,
        instance_id: str,
        application_id: str,
        group_id: str,
        request: main_models.RemoveUsersFromGroupRequest,
        headers: main_models.RemoveUsersFromGroupHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveUsersFromGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.user_ids):
            body['userIds'] = request.user_ids
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RemoveUsersFromGroup',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/groups/{DaraURL.percent_encode(group_id)}/actions/removeUsersFromGroup',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.RemoveUsersFromGroupResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def remove_users_from_group_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        group_id: str,
        request: main_models.RemoveUsersFromGroupRequest,
        headers: main_models.RemoveUsersFromGroupHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveUsersFromGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.user_ids):
            body['userIds'] = request.user_ids
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RemoveUsersFromGroup',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/groups/{DaraURL.percent_encode(group_id)}/actions/removeUsersFromGroup',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.RemoveUsersFromGroupResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def remove_users_from_group(
        self,
        instance_id: str,
        application_id: str,
        group_id: str,
        request: main_models.RemoveUsersFromGroupRequest,
    ) -> main_models.RemoveUsersFromGroupResponse:
        runtime = RuntimeOptions()
        headers = main_models.RemoveUsersFromGroupHeaders()
        return self.remove_users_from_group_with_options(instance_id, application_id, group_id, request, headers, runtime)

    async def remove_users_from_group_async(
        self,
        instance_id: str,
        application_id: str,
        group_id: str,
        request: main_models.RemoveUsersFromGroupRequest,
    ) -> main_models.RemoveUsersFromGroupResponse:
        runtime = RuntimeOptions()
        headers = main_models.RemoveUsersFromGroupHeaders()
        return await self.remove_users_from_group_with_options_async(instance_id, application_id, group_id, request, headers, runtime)

    def revoke_token_with_options(
        self,
        instance_id: str,
        application_id: str,
        request: main_models.RevokeTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RevokeTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['client_id'] = request.client_id
        if not DaraCore.is_null(request.client_secret):
            query['client_secret'] = request.client_secret
        if not DaraCore.is_null(request.token):
            query['token'] = request.token
        if not DaraCore.is_null(request.token_type_hint):
            query['token_type_hint'] = request.token_type_hint
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RevokeToken',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/oauth2/revoke',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokeTokenResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def revoke_token_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        request: main_models.RevokeTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RevokeTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['client_id'] = request.client_id
        if not DaraCore.is_null(request.client_secret):
            query['client_secret'] = request.client_secret
        if not DaraCore.is_null(request.token):
            query['token'] = request.token
        if not DaraCore.is_null(request.token_type_hint):
            query['token_type_hint'] = request.token_type_hint
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RevokeToken',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/oauth2/revoke',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokeTokenResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def revoke_token(
        self,
        instance_id: str,
        application_id: str,
        request: main_models.RevokeTokenRequest,
    ) -> main_models.RevokeTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.revoke_token_with_options(instance_id, application_id, request, headers, runtime)

    async def revoke_token_async(
        self,
        instance_id: str,
        application_id: str,
        request: main_models.RevokeTokenRequest,
    ) -> main_models.RevokeTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.revoke_token_with_options_async(instance_id, application_id, request, headers, runtime)

    def set_user_primary_organizational_unit_with_options(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        request: main_models.SetUserPrimaryOrganizationalUnitRequest,
        headers: main_models.SetUserPrimaryOrganizationalUnitHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.SetUserPrimaryOrganizationalUnitResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.organizational_unit_id):
            body['organizationalUnitId'] = request.organizational_unit_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SetUserPrimaryOrganizationalUnit',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/users/{DaraURL.percent_encode(user_id)}/actions/setUserPrimaryOrganizationalUnit',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.SetUserPrimaryOrganizationalUnitResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def set_user_primary_organizational_unit_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        request: main_models.SetUserPrimaryOrganizationalUnitRequest,
        headers: main_models.SetUserPrimaryOrganizationalUnitHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.SetUserPrimaryOrganizationalUnitResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.organizational_unit_id):
            body['organizationalUnitId'] = request.organizational_unit_id
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SetUserPrimaryOrganizationalUnit',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/users/{DaraURL.percent_encode(user_id)}/actions/setUserPrimaryOrganizationalUnit',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.SetUserPrimaryOrganizationalUnitResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def set_user_primary_organizational_unit(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        request: main_models.SetUserPrimaryOrganizationalUnitRequest,
    ) -> main_models.SetUserPrimaryOrganizationalUnitResponse:
        runtime = RuntimeOptions()
        headers = main_models.SetUserPrimaryOrganizationalUnitHeaders()
        return self.set_user_primary_organizational_unit_with_options(instance_id, application_id, user_id, request, headers, runtime)

    async def set_user_primary_organizational_unit_async(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        request: main_models.SetUserPrimaryOrganizationalUnitRequest,
    ) -> main_models.SetUserPrimaryOrganizationalUnitResponse:
        runtime = RuntimeOptions()
        headers = main_models.SetUserPrimaryOrganizationalUnitHeaders()
        return await self.set_user_primary_organizational_unit_with_options_async(instance_id, application_id, user_id, request, headers, runtime)

    def update_user_password_with_options(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        request: main_models.UpdateUserPasswordRequest,
        headers: main_models.UpdateUserPasswordHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserPasswordResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.password):
            body['password'] = request.password
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUserPassword',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/users/{DaraURL.percent_encode(user_id)}/actions/updateUserPassword',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateUserPasswordResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def update_user_password_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        request: main_models.UpdateUserPasswordRequest,
        headers: main_models.UpdateUserPasswordHeaders,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserPasswordResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.password):
            body['password'] = request.password
        real_headers = {}
        if not DaraCore.is_null(headers.common_headers):
            real_headers = headers.common_headers
        if not DaraCore.is_null(headers.authorization):
            real_headers['Authorization'] = str(headers.authorization)
        req = open_api_util_models.OpenApiRequest(
            headers = real_headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUserPassword',
            version = '2022-02-25',
            protocol = 'HTTPS',
            pathname = f'/v2/{DaraURL.percent_encode(instance_id)}/{DaraURL.percent_encode(application_id)}/users/{DaraURL.percent_encode(user_id)}/actions/updateUserPassword',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateUserPasswordResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def update_user_password(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        request: main_models.UpdateUserPasswordRequest,
    ) -> main_models.UpdateUserPasswordResponse:
        runtime = RuntimeOptions()
        headers = main_models.UpdateUserPasswordHeaders()
        return self.update_user_password_with_options(instance_id, application_id, user_id, request, headers, runtime)

    async def update_user_password_async(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        request: main_models.UpdateUserPasswordRequest,
    ) -> main_models.UpdateUserPasswordResponse:
        runtime = RuntimeOptions()
        headers = main_models.UpdateUserPasswordHeaders()
        return await self.update_user_password_with_options_async(instance_id, application_id, user_id, request, headers, runtime)
