# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_eiam_developerapi20220225 import models as eiam_developerapi_20220225_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_user_to_organizational_units_with_options(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        request: eiam_developerapi_20220225_models.AddUserToOrganizationalUnitsRequest,
        headers: eiam_developerapi_20220225_models.AddUserToOrganizationalUnitsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.AddUserToOrganizationalUnitsResponse:
        """
        @summary 将账户加入多个组织
        
        @param request: AddUserToOrganizationalUnitsRequest
        @param headers: AddUserToOrganizationalUnitsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddUserToOrganizationalUnitsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.organizational_unit_ids):
            body['organizationalUnitIds'] = request.organizational_unit_ids
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddUserToOrganizationalUnits',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/users/{OpenApiUtilClient.get_encode_param(user_id)}/actions/addUserToOrganizationalUnits',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.AddUserToOrganizationalUnitsResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def add_user_to_organizational_units_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        request: eiam_developerapi_20220225_models.AddUserToOrganizationalUnitsRequest,
        headers: eiam_developerapi_20220225_models.AddUserToOrganizationalUnitsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.AddUserToOrganizationalUnitsResponse:
        """
        @summary 将账户加入多个组织
        
        @param request: AddUserToOrganizationalUnitsRequest
        @param headers: AddUserToOrganizationalUnitsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddUserToOrganizationalUnitsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.organizational_unit_ids):
            body['organizationalUnitIds'] = request.organizational_unit_ids
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddUserToOrganizationalUnits',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/users/{OpenApiUtilClient.get_encode_param(user_id)}/actions/addUserToOrganizationalUnits',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.AddUserToOrganizationalUnitsResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def add_user_to_organizational_units(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        request: eiam_developerapi_20220225_models.AddUserToOrganizationalUnitsRequest,
    ) -> eiam_developerapi_20220225_models.AddUserToOrganizationalUnitsResponse:
        """
        @summary 将账户加入多个组织
        
        @param request: AddUserToOrganizationalUnitsRequest
        @return: AddUserToOrganizationalUnitsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.AddUserToOrganizationalUnitsHeaders()
        return self.add_user_to_organizational_units_with_options(instance_id, application_id, user_id, request, headers, runtime)

    async def add_user_to_organizational_units_async(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        request: eiam_developerapi_20220225_models.AddUserToOrganizationalUnitsRequest,
    ) -> eiam_developerapi_20220225_models.AddUserToOrganizationalUnitsResponse:
        """
        @summary 将账户加入多个组织
        
        @param request: AddUserToOrganizationalUnitsRequest
        @return: AddUserToOrganizationalUnitsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.AddUserToOrganizationalUnitsHeaders()
        return await self.add_user_to_organizational_units_with_options_async(instance_id, application_id, user_id, request, headers, runtime)

    def add_users_to_group_with_options(
        self,
        instance_id: str,
        application_id: str,
        group_id: str,
        request: eiam_developerapi_20220225_models.AddUsersToGroupRequest,
        headers: eiam_developerapi_20220225_models.AddUsersToGroupHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.AddUsersToGroupResponse:
        """
        @summary Adds multiple Employee Identity and Access Management (EIAM) accounts to an EIAM group. If the accounts are already added to the specified group, no update is performed.
        
        @param request: AddUsersToGroupRequest
        @param headers: AddUsersToGroupHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddUsersToGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.user_ids):
            body['userIds'] = request.user_ids
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddUsersToGroup',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/groups/{OpenApiUtilClient.get_encode_param(group_id)}/actions/addUsersToGroup',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.AddUsersToGroupResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def add_users_to_group_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        group_id: str,
        request: eiam_developerapi_20220225_models.AddUsersToGroupRequest,
        headers: eiam_developerapi_20220225_models.AddUsersToGroupHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.AddUsersToGroupResponse:
        """
        @summary Adds multiple Employee Identity and Access Management (EIAM) accounts to an EIAM group. If the accounts are already added to the specified group, no update is performed.
        
        @param request: AddUsersToGroupRequest
        @param headers: AddUsersToGroupHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddUsersToGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.user_ids):
            body['userIds'] = request.user_ids
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddUsersToGroup',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/groups/{OpenApiUtilClient.get_encode_param(group_id)}/actions/addUsersToGroup',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.AddUsersToGroupResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def add_users_to_group(
        self,
        instance_id: str,
        application_id: str,
        group_id: str,
        request: eiam_developerapi_20220225_models.AddUsersToGroupRequest,
    ) -> eiam_developerapi_20220225_models.AddUsersToGroupResponse:
        """
        @summary Adds multiple Employee Identity and Access Management (EIAM) accounts to an EIAM group. If the accounts are already added to the specified group, no update is performed.
        
        @param request: AddUsersToGroupRequest
        @return: AddUsersToGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.AddUsersToGroupHeaders()
        return self.add_users_to_group_with_options(instance_id, application_id, group_id, request, headers, runtime)

    async def add_users_to_group_async(
        self,
        instance_id: str,
        application_id: str,
        group_id: str,
        request: eiam_developerapi_20220225_models.AddUsersToGroupRequest,
    ) -> eiam_developerapi_20220225_models.AddUsersToGroupResponse:
        """
        @summary Adds multiple Employee Identity and Access Management (EIAM) accounts to an EIAM group. If the accounts are already added to the specified group, no update is performed.
        
        @param request: AddUsersToGroupRequest
        @return: AddUsersToGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.AddUsersToGroupHeaders()
        return await self.add_users_to_group_with_options_async(instance_id, application_id, group_id, request, headers, runtime)

    def create_group_with_options(
        self,
        instance_id: str,
        application_id: str,
        request: eiam_developerapi_20220225_models.CreateGroupRequest,
        headers: eiam_developerapi_20220225_models.CreateGroupHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.CreateGroupResponse:
        """
        @summary Creates a group.
        
        @param request: CreateGroupRequest
        @param headers: CreateGroupHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_external_id):
            body['groupExternalId'] = request.group_external_id
        if not UtilClient.is_unset(request.group_name):
            body['groupName'] = request.group_name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateGroup',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/groups',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.CreateGroupResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def create_group_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        request: eiam_developerapi_20220225_models.CreateGroupRequest,
        headers: eiam_developerapi_20220225_models.CreateGroupHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.CreateGroupResponse:
        """
        @summary Creates a group.
        
        @param request: CreateGroupRequest
        @param headers: CreateGroupHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_external_id):
            body['groupExternalId'] = request.group_external_id
        if not UtilClient.is_unset(request.group_name):
            body['groupName'] = request.group_name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateGroup',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/groups',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.CreateGroupResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def create_group(
        self,
        instance_id: str,
        application_id: str,
        request: eiam_developerapi_20220225_models.CreateGroupRequest,
    ) -> eiam_developerapi_20220225_models.CreateGroupResponse:
        """
        @summary Creates a group.
        
        @param request: CreateGroupRequest
        @return: CreateGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.CreateGroupHeaders()
        return self.create_group_with_options(instance_id, application_id, request, headers, runtime)

    async def create_group_async(
        self,
        instance_id: str,
        application_id: str,
        request: eiam_developerapi_20220225_models.CreateGroupRequest,
    ) -> eiam_developerapi_20220225_models.CreateGroupResponse:
        """
        @summary Creates a group.
        
        @param request: CreateGroupRequest
        @return: CreateGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.CreateGroupHeaders()
        return await self.create_group_with_options_async(instance_id, application_id, request, headers, runtime)

    def create_organizational_unit_with_options(
        self,
        instance_id: str,
        application_id: str,
        request: eiam_developerapi_20220225_models.CreateOrganizationalUnitRequest,
        headers: eiam_developerapi_20220225_models.CreateOrganizationalUnitHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.CreateOrganizationalUnitResponse:
        """
        @summary Creates an organizational unit.
        
        @param request: CreateOrganizationalUnitRequest
        @param headers: CreateOrganizationalUnitHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateOrganizationalUnitResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.organizational_unit_external_id):
            body['organizationalUnitExternalId'] = request.organizational_unit_external_id
        if not UtilClient.is_unset(request.organizational_unit_name):
            body['organizationalUnitName'] = request.organizational_unit_name
        if not UtilClient.is_unset(request.parent_id):
            body['parentId'] = request.parent_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOrganizationalUnit',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/organizationalUnits',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.CreateOrganizationalUnitResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def create_organizational_unit_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        request: eiam_developerapi_20220225_models.CreateOrganizationalUnitRequest,
        headers: eiam_developerapi_20220225_models.CreateOrganizationalUnitHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.CreateOrganizationalUnitResponse:
        """
        @summary Creates an organizational unit.
        
        @param request: CreateOrganizationalUnitRequest
        @param headers: CreateOrganizationalUnitHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateOrganizationalUnitResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.organizational_unit_external_id):
            body['organizationalUnitExternalId'] = request.organizational_unit_external_id
        if not UtilClient.is_unset(request.organizational_unit_name):
            body['organizationalUnitName'] = request.organizational_unit_name
        if not UtilClient.is_unset(request.parent_id):
            body['parentId'] = request.parent_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOrganizationalUnit',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/organizationalUnits',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.CreateOrganizationalUnitResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def create_organizational_unit(
        self,
        instance_id: str,
        application_id: str,
        request: eiam_developerapi_20220225_models.CreateOrganizationalUnitRequest,
    ) -> eiam_developerapi_20220225_models.CreateOrganizationalUnitResponse:
        """
        @summary Creates an organizational unit.
        
        @param request: CreateOrganizationalUnitRequest
        @return: CreateOrganizationalUnitResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.CreateOrganizationalUnitHeaders()
        return self.create_organizational_unit_with_options(instance_id, application_id, request, headers, runtime)

    async def create_organizational_unit_async(
        self,
        instance_id: str,
        application_id: str,
        request: eiam_developerapi_20220225_models.CreateOrganizationalUnitRequest,
    ) -> eiam_developerapi_20220225_models.CreateOrganizationalUnitResponse:
        """
        @summary Creates an organizational unit.
        
        @param request: CreateOrganizationalUnitRequest
        @return: CreateOrganizationalUnitResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.CreateOrganizationalUnitHeaders()
        return await self.create_organizational_unit_with_options_async(instance_id, application_id, request, headers, runtime)

    def create_user_with_options(
        self,
        instance_id: str,
        application_id: str,
        request: eiam_developerapi_20220225_models.CreateUserRequest,
        headers: eiam_developerapi_20220225_models.CreateUserHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.CreateUserResponse:
        """
        @summary Creates an Employee Identity and Access Management (EIAM) account in an organizational unit.
        
        @param request: CreateUserRequest
        @param headers: CreateUserHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateUserResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.custom_fields):
            body['customFields'] = request.custom_fields
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['displayName'] = request.display_name
        if not UtilClient.is_unset(request.email):
            body['email'] = request.email
        if not UtilClient.is_unset(request.email_verified):
            body['emailVerified'] = request.email_verified
        if not UtilClient.is_unset(request.password):
            body['password'] = request.password
        if not UtilClient.is_unset(request.password_initialization_config):
            body['passwordInitializationConfig'] = request.password_initialization_config
        if not UtilClient.is_unset(request.phone_number):
            body['phoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.phone_number_verified):
            body['phoneNumberVerified'] = request.phone_number_verified
        if not UtilClient.is_unset(request.phone_region):
            body['phoneRegion'] = request.phone_region
        if not UtilClient.is_unset(request.primary_organizational_unit_id):
            body['primaryOrganizationalUnitId'] = request.primary_organizational_unit_id
        if not UtilClient.is_unset(request.user_external_id):
            body['userExternalId'] = request.user_external_id
        if not UtilClient.is_unset(request.username):
            body['username'] = request.username
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateUser',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/users',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.CreateUserResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def create_user_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        request: eiam_developerapi_20220225_models.CreateUserRequest,
        headers: eiam_developerapi_20220225_models.CreateUserHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.CreateUserResponse:
        """
        @summary Creates an Employee Identity and Access Management (EIAM) account in an organizational unit.
        
        @param request: CreateUserRequest
        @param headers: CreateUserHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateUserResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.custom_fields):
            body['customFields'] = request.custom_fields
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['displayName'] = request.display_name
        if not UtilClient.is_unset(request.email):
            body['email'] = request.email
        if not UtilClient.is_unset(request.email_verified):
            body['emailVerified'] = request.email_verified
        if not UtilClient.is_unset(request.password):
            body['password'] = request.password
        if not UtilClient.is_unset(request.password_initialization_config):
            body['passwordInitializationConfig'] = request.password_initialization_config
        if not UtilClient.is_unset(request.phone_number):
            body['phoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.phone_number_verified):
            body['phoneNumberVerified'] = request.phone_number_verified
        if not UtilClient.is_unset(request.phone_region):
            body['phoneRegion'] = request.phone_region
        if not UtilClient.is_unset(request.primary_organizational_unit_id):
            body['primaryOrganizationalUnitId'] = request.primary_organizational_unit_id
        if not UtilClient.is_unset(request.user_external_id):
            body['userExternalId'] = request.user_external_id
        if not UtilClient.is_unset(request.username):
            body['username'] = request.username
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateUser',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/users',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.CreateUserResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def create_user(
        self,
        instance_id: str,
        application_id: str,
        request: eiam_developerapi_20220225_models.CreateUserRequest,
    ) -> eiam_developerapi_20220225_models.CreateUserResponse:
        """
        @summary Creates an Employee Identity and Access Management (EIAM) account in an organizational unit.
        
        @param request: CreateUserRequest
        @return: CreateUserResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.CreateUserHeaders()
        return self.create_user_with_options(instance_id, application_id, request, headers, runtime)

    async def create_user_async(
        self,
        instance_id: str,
        application_id: str,
        request: eiam_developerapi_20220225_models.CreateUserRequest,
    ) -> eiam_developerapi_20220225_models.CreateUserResponse:
        """
        @summary Creates an Employee Identity and Access Management (EIAM) account in an organizational unit.
        
        @param request: CreateUserRequest
        @return: CreateUserResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.CreateUserHeaders()
        return await self.create_user_with_options_async(instance_id, application_id, request, headers, runtime)

    def delete_group_with_options(
        self,
        instance_id: str,
        application_id: str,
        group_id: str,
        headers: eiam_developerapi_20220225_models.DeleteGroupHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.DeleteGroupResponse:
        """
        @summary Deletes a group.
        
        @param headers: DeleteGroupHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGroupResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteGroup',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/groups/{OpenApiUtilClient.get_encode_param(group_id)}',
            method='DELETE',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.DeleteGroupResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def delete_group_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        group_id: str,
        headers: eiam_developerapi_20220225_models.DeleteGroupHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.DeleteGroupResponse:
        """
        @summary Deletes a group.
        
        @param headers: DeleteGroupHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGroupResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteGroup',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/groups/{OpenApiUtilClient.get_encode_param(group_id)}',
            method='DELETE',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.DeleteGroupResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def delete_group(
        self,
        instance_id: str,
        application_id: str,
        group_id: str,
    ) -> eiam_developerapi_20220225_models.DeleteGroupResponse:
        """
        @summary Deletes a group.
        
        @return: DeleteGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.DeleteGroupHeaders()
        return self.delete_group_with_options(instance_id, application_id, group_id, headers, runtime)

    async def delete_group_async(
        self,
        instance_id: str,
        application_id: str,
        group_id: str,
    ) -> eiam_developerapi_20220225_models.DeleteGroupResponse:
        """
        @summary Deletes a group.
        
        @return: DeleteGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.DeleteGroupHeaders()
        return await self.delete_group_with_options_async(instance_id, application_id, group_id, headers, runtime)

    def delete_organizational_unit_with_options(
        self,
        instance_id: str,
        application_id: str,
        organizational_unit_id: str,
        headers: eiam_developerapi_20220225_models.DeleteOrganizationalUnitHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.DeleteOrganizationalUnitResponse:
        """
        @summary Deletes an organizational unit.
        
        @param headers: DeleteOrganizationalUnitHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteOrganizationalUnitResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteOrganizationalUnit',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/organizationalUnits/{OpenApiUtilClient.get_encode_param(organizational_unit_id)}',
            method='DELETE',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.DeleteOrganizationalUnitResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def delete_organizational_unit_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        organizational_unit_id: str,
        headers: eiam_developerapi_20220225_models.DeleteOrganizationalUnitHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.DeleteOrganizationalUnitResponse:
        """
        @summary Deletes an organizational unit.
        
        @param headers: DeleteOrganizationalUnitHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteOrganizationalUnitResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteOrganizationalUnit',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/organizationalUnits/{OpenApiUtilClient.get_encode_param(organizational_unit_id)}',
            method='DELETE',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.DeleteOrganizationalUnitResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def delete_organizational_unit(
        self,
        instance_id: str,
        application_id: str,
        organizational_unit_id: str,
    ) -> eiam_developerapi_20220225_models.DeleteOrganizationalUnitResponse:
        """
        @summary Deletes an organizational unit.
        
        @return: DeleteOrganizationalUnitResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.DeleteOrganizationalUnitHeaders()
        return self.delete_organizational_unit_with_options(instance_id, application_id, organizational_unit_id, headers, runtime)

    async def delete_organizational_unit_async(
        self,
        instance_id: str,
        application_id: str,
        organizational_unit_id: str,
    ) -> eiam_developerapi_20220225_models.DeleteOrganizationalUnitResponse:
        """
        @summary Deletes an organizational unit.
        
        @return: DeleteOrganizationalUnitResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.DeleteOrganizationalUnitHeaders()
        return await self.delete_organizational_unit_with_options_async(instance_id, application_id, organizational_unit_id, headers, runtime)

    def delete_user_with_options(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        headers: eiam_developerapi_20220225_models.DeleteUserHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.DeleteUserResponse:
        """
        @summary Deletes an Employee Identity and Access Management (EIAM) account.
        
        @param headers: DeleteUserHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUserResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteUser',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/users/{OpenApiUtilClient.get_encode_param(user_id)}',
            method='DELETE',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.DeleteUserResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def delete_user_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        headers: eiam_developerapi_20220225_models.DeleteUserHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.DeleteUserResponse:
        """
        @summary Deletes an Employee Identity and Access Management (EIAM) account.
        
        @param headers: DeleteUserHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUserResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DeleteUser',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/users/{OpenApiUtilClient.get_encode_param(user_id)}',
            method='DELETE',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.DeleteUserResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def delete_user(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
    ) -> eiam_developerapi_20220225_models.DeleteUserResponse:
        """
        @summary Deletes an Employee Identity and Access Management (EIAM) account.
        
        @return: DeleteUserResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.DeleteUserHeaders()
        return self.delete_user_with_options(instance_id, application_id, user_id, headers, runtime)

    async def delete_user_async(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
    ) -> eiam_developerapi_20220225_models.DeleteUserResponse:
        """
        @summary Deletes an Employee Identity and Access Management (EIAM) account.
        
        @return: DeleteUserResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.DeleteUserHeaders()
        return await self.delete_user_with_options_async(instance_id, application_id, user_id, headers, runtime)

    def disable_user_with_options(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        headers: eiam_developerapi_20220225_models.DisableUserHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.DisableUserResponse:
        """
        @summary Disables an Employee Identity and Access Management (EIAM) account.
        
        @param headers: DisableUserHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableUserResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DisableUser',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/users/{OpenApiUtilClient.get_encode_param(user_id)}/actions/disable',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.DisableUserResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def disable_user_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        headers: eiam_developerapi_20220225_models.DisableUserHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.DisableUserResponse:
        """
        @summary Disables an Employee Identity and Access Management (EIAM) account.
        
        @param headers: DisableUserHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableUserResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='DisableUser',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/users/{OpenApiUtilClient.get_encode_param(user_id)}/actions/disable',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.DisableUserResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def disable_user(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
    ) -> eiam_developerapi_20220225_models.DisableUserResponse:
        """
        @summary Disables an Employee Identity and Access Management (EIAM) account.
        
        @return: DisableUserResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.DisableUserHeaders()
        return self.disable_user_with_options(instance_id, application_id, user_id, headers, runtime)

    async def disable_user_async(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
    ) -> eiam_developerapi_20220225_models.DisableUserResponse:
        """
        @summary Disables an Employee Identity and Access Management (EIAM) account.
        
        @return: DisableUserResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.DisableUserHeaders()
        return await self.disable_user_with_options_async(instance_id, application_id, user_id, headers, runtime)

    def enable_user_with_options(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        headers: eiam_developerapi_20220225_models.EnableUserHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.EnableUserResponse:
        """
        @summary Enables an Employee Identity and Access Management (EIAM) account.
        
        @param headers: EnableUserHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableUserResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='EnableUser',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/users/{OpenApiUtilClient.get_encode_param(user_id)}/actions/enable',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.EnableUserResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def enable_user_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        headers: eiam_developerapi_20220225_models.EnableUserHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.EnableUserResponse:
        """
        @summary Enables an Employee Identity and Access Management (EIAM) account.
        
        @param headers: EnableUserHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableUserResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='EnableUser',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/users/{OpenApiUtilClient.get_encode_param(user_id)}/actions/enable',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.EnableUserResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def enable_user(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
    ) -> eiam_developerapi_20220225_models.EnableUserResponse:
        """
        @summary Enables an Employee Identity and Access Management (EIAM) account.
        
        @return: EnableUserResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.EnableUserHeaders()
        return self.enable_user_with_options(instance_id, application_id, user_id, headers, runtime)

    async def enable_user_async(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
    ) -> eiam_developerapi_20220225_models.EnableUserResponse:
        """
        @summary Enables an Employee Identity and Access Management (EIAM) account.
        
        @return: EnableUserResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.EnableUserHeaders()
        return await self.enable_user_with_options_async(instance_id, application_id, user_id, headers, runtime)

    def generate_device_code_with_options(
        self,
        instance_id: str,
        application_id: str,
        request: eiam_developerapi_20220225_models.GenerateDeviceCodeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.GenerateDeviceCodeResponse:
        """
        @summary Generates a device code.
        
        @param request: GenerateDeviceCodeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateDeviceCodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scope):
            query['scope'] = request.scope
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateDeviceCode',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/oauth2/device/code',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.GenerateDeviceCodeResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def generate_device_code_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        request: eiam_developerapi_20220225_models.GenerateDeviceCodeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.GenerateDeviceCodeResponse:
        """
        @summary Generates a device code.
        
        @param request: GenerateDeviceCodeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateDeviceCodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scope):
            query['scope'] = request.scope
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateDeviceCode',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/oauth2/device/code',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.GenerateDeviceCodeResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def generate_device_code(
        self,
        instance_id: str,
        application_id: str,
        request: eiam_developerapi_20220225_models.GenerateDeviceCodeRequest,
    ) -> eiam_developerapi_20220225_models.GenerateDeviceCodeResponse:
        """
        @summary Generates a device code.
        
        @param request: GenerateDeviceCodeRequest
        @return: GenerateDeviceCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.generate_device_code_with_options(instance_id, application_id, request, headers, runtime)

    async def generate_device_code_async(
        self,
        instance_id: str,
        application_id: str,
        request: eiam_developerapi_20220225_models.GenerateDeviceCodeRequest,
    ) -> eiam_developerapi_20220225_models.GenerateDeviceCodeResponse:
        """
        @summary Generates a device code.
        
        @param request: GenerateDeviceCodeRequest
        @return: GenerateDeviceCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.generate_device_code_with_options_async(instance_id, application_id, request, headers, runtime)

    def generate_token_with_options(
        self,
        instance_id: str,
        application_id: str,
        request: eiam_developerapi_20220225_models.GenerateTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.GenerateTokenResponse:
        """
        @summary Generates a token for accessing an application in an instance.
        
        @description The following authorization types are supported: authorization code, device code, refresh token, and client credentials.
        
        @param request: GenerateTokenRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['client_id'] = request.client_id
        if not UtilClient.is_unset(request.client_secret):
            query['client_secret'] = request.client_secret
        if not UtilClient.is_unset(request.code):
            query['code'] = request.code
        if not UtilClient.is_unset(request.code_verifier):
            query['code_verifier'] = request.code_verifier
        if not UtilClient.is_unset(request.device_code):
            query['device_code'] = request.device_code
        if not UtilClient.is_unset(request.exclusive_tag):
            query['exclusive_tag'] = request.exclusive_tag
        if not UtilClient.is_unset(request.grant_type):
            query['grant_type'] = request.grant_type
        if not UtilClient.is_unset(request.password):
            query['password'] = request.password
        if not UtilClient.is_unset(request.redirect_uri):
            query['redirect_uri'] = request.redirect_uri
        if not UtilClient.is_unset(request.refresh_token):
            query['refresh_token'] = request.refresh_token
        if not UtilClient.is_unset(request.scope):
            query['scope'] = request.scope
        if not UtilClient.is_unset(request.username):
            query['username'] = request.username
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateToken',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/oauth2/token',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.GenerateTokenResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def generate_token_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        request: eiam_developerapi_20220225_models.GenerateTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.GenerateTokenResponse:
        """
        @summary Generates a token for accessing an application in an instance.
        
        @description The following authorization types are supported: authorization code, device code, refresh token, and client credentials.
        
        @param request: GenerateTokenRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['client_id'] = request.client_id
        if not UtilClient.is_unset(request.client_secret):
            query['client_secret'] = request.client_secret
        if not UtilClient.is_unset(request.code):
            query['code'] = request.code
        if not UtilClient.is_unset(request.code_verifier):
            query['code_verifier'] = request.code_verifier
        if not UtilClient.is_unset(request.device_code):
            query['device_code'] = request.device_code
        if not UtilClient.is_unset(request.exclusive_tag):
            query['exclusive_tag'] = request.exclusive_tag
        if not UtilClient.is_unset(request.grant_type):
            query['grant_type'] = request.grant_type
        if not UtilClient.is_unset(request.password):
            query['password'] = request.password
        if not UtilClient.is_unset(request.redirect_uri):
            query['redirect_uri'] = request.redirect_uri
        if not UtilClient.is_unset(request.refresh_token):
            query['refresh_token'] = request.refresh_token
        if not UtilClient.is_unset(request.scope):
            query['scope'] = request.scope
        if not UtilClient.is_unset(request.username):
            query['username'] = request.username
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateToken',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/oauth2/token',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.GenerateTokenResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def generate_token(
        self,
        instance_id: str,
        application_id: str,
        request: eiam_developerapi_20220225_models.GenerateTokenRequest,
    ) -> eiam_developerapi_20220225_models.GenerateTokenResponse:
        """
        @summary Generates a token for accessing an application in an instance.
        
        @description The following authorization types are supported: authorization code, device code, refresh token, and client credentials.
        
        @param request: GenerateTokenRequest
        @return: GenerateTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.generate_token_with_options(instance_id, application_id, request, headers, runtime)

    async def generate_token_async(
        self,
        instance_id: str,
        application_id: str,
        request: eiam_developerapi_20220225_models.GenerateTokenRequest,
    ) -> eiam_developerapi_20220225_models.GenerateTokenResponse:
        """
        @summary Generates a token for accessing an application in an instance.
        
        @description The following authorization types are supported: authorization code, device code, refresh token, and client credentials.
        
        @param request: GenerateTokenRequest
        @return: GenerateTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.generate_token_with_options_async(instance_id, application_id, request, headers, runtime)

    def get_application_provisioning_scope_with_options(
        self,
        instance_id: str,
        application_id: str,
        headers: eiam_developerapi_20220225_models.GetApplicationProvisioningScopeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.GetApplicationProvisioningScopeResponse:
        """
        @summary Queries the synchronization scope of an application in an instance.
        
        @description >
        You can go to the Applications page in the IDaaS console to set the synchronization scope. After an application is created, the application has the permission to call this operation by default.
        
        @param headers: GetApplicationProvisioningScopeHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetApplicationProvisioningScopeResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetApplicationProvisioningScope',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/provisioningScope',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.GetApplicationProvisioningScopeResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def get_application_provisioning_scope_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        headers: eiam_developerapi_20220225_models.GetApplicationProvisioningScopeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.GetApplicationProvisioningScopeResponse:
        """
        @summary Queries the synchronization scope of an application in an instance.
        
        @description >
        You can go to the Applications page in the IDaaS console to set the synchronization scope. After an application is created, the application has the permission to call this operation by default.
        
        @param headers: GetApplicationProvisioningScopeHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetApplicationProvisioningScopeResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetApplicationProvisioningScope',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/provisioningScope',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.GetApplicationProvisioningScopeResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def get_application_provisioning_scope(
        self,
        instance_id: str,
        application_id: str,
    ) -> eiam_developerapi_20220225_models.GetApplicationProvisioningScopeResponse:
        """
        @summary Queries the synchronization scope of an application in an instance.
        
        @description >
        You can go to the Applications page in the IDaaS console to set the synchronization scope. After an application is created, the application has the permission to call this operation by default.
        
        @return: GetApplicationProvisioningScopeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.GetApplicationProvisioningScopeHeaders()
        return self.get_application_provisioning_scope_with_options(instance_id, application_id, headers, runtime)

    async def get_application_provisioning_scope_async(
        self,
        instance_id: str,
        application_id: str,
    ) -> eiam_developerapi_20220225_models.GetApplicationProvisioningScopeResponse:
        """
        @summary Queries the synchronization scope of an application in an instance.
        
        @description >
        You can go to the Applications page in the IDaaS console to set the synchronization scope. After an application is created, the application has the permission to call this operation by default.
        
        @return: GetApplicationProvisioningScopeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.GetApplicationProvisioningScopeHeaders()
        return await self.get_application_provisioning_scope_with_options_async(instance_id, application_id, headers, runtime)

    def get_group_with_options(
        self,
        instance_id: str,
        application_id: str,
        group_id: str,
        headers: eiam_developerapi_20220225_models.GetGroupHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.GetGroupResponse:
        """
        @summary Queries the details of a group.
        
        @param headers: GetGroupHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetGroupResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetGroup',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/groups/{OpenApiUtilClient.get_encode_param(group_id)}',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.GetGroupResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def get_group_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        group_id: str,
        headers: eiam_developerapi_20220225_models.GetGroupHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.GetGroupResponse:
        """
        @summary Queries the details of a group.
        
        @param headers: GetGroupHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetGroupResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetGroup',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/groups/{OpenApiUtilClient.get_encode_param(group_id)}',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.GetGroupResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def get_group(
        self,
        instance_id: str,
        application_id: str,
        group_id: str,
    ) -> eiam_developerapi_20220225_models.GetGroupResponse:
        """
        @summary Queries the details of a group.
        
        @return: GetGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.GetGroupHeaders()
        return self.get_group_with_options(instance_id, application_id, group_id, headers, runtime)

    async def get_group_async(
        self,
        instance_id: str,
        application_id: str,
        group_id: str,
    ) -> eiam_developerapi_20220225_models.GetGroupResponse:
        """
        @summary Queries the details of a group.
        
        @return: GetGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.GetGroupHeaders()
        return await self.get_group_with_options_async(instance_id, application_id, group_id, headers, runtime)

    def get_organizational_unit_with_options(
        self,
        instance_id: str,
        application_id: str,
        organizational_unit_id: str,
        headers: eiam_developerapi_20220225_models.GetOrganizationalUnitHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.GetOrganizationalUnitResponse:
        """
        @summary Queries the information of an organizational unit.
        
        @param headers: GetOrganizationalUnitHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOrganizationalUnitResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetOrganizationalUnit',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/organizationalUnits/{OpenApiUtilClient.get_encode_param(organizational_unit_id)}',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.GetOrganizationalUnitResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def get_organizational_unit_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        organizational_unit_id: str,
        headers: eiam_developerapi_20220225_models.GetOrganizationalUnitHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.GetOrganizationalUnitResponse:
        """
        @summary Queries the information of an organizational unit.
        
        @param headers: GetOrganizationalUnitHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOrganizationalUnitResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetOrganizationalUnit',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/organizationalUnits/{OpenApiUtilClient.get_encode_param(organizational_unit_id)}',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.GetOrganizationalUnitResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def get_organizational_unit(
        self,
        instance_id: str,
        application_id: str,
        organizational_unit_id: str,
    ) -> eiam_developerapi_20220225_models.GetOrganizationalUnitResponse:
        """
        @summary Queries the information of an organizational unit.
        
        @return: GetOrganizationalUnitResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.GetOrganizationalUnitHeaders()
        return self.get_organizational_unit_with_options(instance_id, application_id, organizational_unit_id, headers, runtime)

    async def get_organizational_unit_async(
        self,
        instance_id: str,
        application_id: str,
        organizational_unit_id: str,
    ) -> eiam_developerapi_20220225_models.GetOrganizationalUnitResponse:
        """
        @summary Queries the information of an organizational unit.
        
        @return: GetOrganizationalUnitResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.GetOrganizationalUnitHeaders()
        return await self.get_organizational_unit_with_options_async(instance_id, application_id, organizational_unit_id, headers, runtime)

    def get_organizational_unit_id_by_external_id_with_options(
        self,
        instance_id: str,
        application_id: str,
        request: eiam_developerapi_20220225_models.GetOrganizationalUnitIdByExternalIdRequest,
        headers: eiam_developerapi_20220225_models.GetOrganizationalUnitIdByExternalIdHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.GetOrganizationalUnitIdByExternalIdResponse:
        """
        @summary Obtains the ID of an organizational unit based on the external ID
        
        @param request: GetOrganizationalUnitIdByExternalIdRequest
        @param headers: GetOrganizationalUnitIdByExternalIdHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOrganizationalUnitIdByExternalIdResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.organizational_unit_external_id):
            body['organizationalUnitExternalId'] = request.organizational_unit_external_id
        if not UtilClient.is_unset(request.organizational_unit_source_id):
            body['organizationalUnitSourceId'] = request.organizational_unit_source_id
        if not UtilClient.is_unset(request.organizational_unit_source_type):
            body['organizationalUnitSourceType'] = request.organizational_unit_source_type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOrganizationalUnitIdByExternalId',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/organizationalUnits/_/actions/getOrganizationalUnitIdByExternalId',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.GetOrganizationalUnitIdByExternalIdResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def get_organizational_unit_id_by_external_id_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        request: eiam_developerapi_20220225_models.GetOrganizationalUnitIdByExternalIdRequest,
        headers: eiam_developerapi_20220225_models.GetOrganizationalUnitIdByExternalIdHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.GetOrganizationalUnitIdByExternalIdResponse:
        """
        @summary Obtains the ID of an organizational unit based on the external ID
        
        @param request: GetOrganizationalUnitIdByExternalIdRequest
        @param headers: GetOrganizationalUnitIdByExternalIdHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOrganizationalUnitIdByExternalIdResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.organizational_unit_external_id):
            body['organizationalUnitExternalId'] = request.organizational_unit_external_id
        if not UtilClient.is_unset(request.organizational_unit_source_id):
            body['organizationalUnitSourceId'] = request.organizational_unit_source_id
        if not UtilClient.is_unset(request.organizational_unit_source_type):
            body['organizationalUnitSourceType'] = request.organizational_unit_source_type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOrganizationalUnitIdByExternalId',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/organizationalUnits/_/actions/getOrganizationalUnitIdByExternalId',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.GetOrganizationalUnitIdByExternalIdResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def get_organizational_unit_id_by_external_id(
        self,
        instance_id: str,
        application_id: str,
        request: eiam_developerapi_20220225_models.GetOrganizationalUnitIdByExternalIdRequest,
    ) -> eiam_developerapi_20220225_models.GetOrganizationalUnitIdByExternalIdResponse:
        """
        @summary Obtains the ID of an organizational unit based on the external ID
        
        @param request: GetOrganizationalUnitIdByExternalIdRequest
        @return: GetOrganizationalUnitIdByExternalIdResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.GetOrganizationalUnitIdByExternalIdHeaders()
        return self.get_organizational_unit_id_by_external_id_with_options(instance_id, application_id, request, headers, runtime)

    async def get_organizational_unit_id_by_external_id_async(
        self,
        instance_id: str,
        application_id: str,
        request: eiam_developerapi_20220225_models.GetOrganizationalUnitIdByExternalIdRequest,
    ) -> eiam_developerapi_20220225_models.GetOrganizationalUnitIdByExternalIdResponse:
        """
        @summary Obtains the ID of an organizational unit based on the external ID
        
        @param request: GetOrganizationalUnitIdByExternalIdRequest
        @return: GetOrganizationalUnitIdByExternalIdResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.GetOrganizationalUnitIdByExternalIdHeaders()
        return await self.get_organizational_unit_id_by_external_id_with_options_async(instance_id, application_id, request, headers, runtime)

    def get_user_with_options(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        headers: eiam_developerapi_20220225_models.GetUserHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.GetUserResponse:
        """
        @summary Queries the details of an Employee Identity and Access Management (EIAM) account.
        
        @param headers: GetUserHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetUser',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/users/{OpenApiUtilClient.get_encode_param(user_id)}',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.GetUserResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def get_user_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        headers: eiam_developerapi_20220225_models.GetUserHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.GetUserResponse:
        """
        @summary Queries the details of an Employee Identity and Access Management (EIAM) account.
        
        @param headers: GetUserHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetUser',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/users/{OpenApiUtilClient.get_encode_param(user_id)}',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.GetUserResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def get_user(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
    ) -> eiam_developerapi_20220225_models.GetUserResponse:
        """
        @summary Queries the details of an Employee Identity and Access Management (EIAM) account.
        
        @return: GetUserResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.GetUserHeaders()
        return self.get_user_with_options(instance_id, application_id, user_id, headers, runtime)

    async def get_user_async(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
    ) -> eiam_developerapi_20220225_models.GetUserResponse:
        """
        @summary Queries the details of an Employee Identity and Access Management (EIAM) account.
        
        @return: GetUserResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.GetUserHeaders()
        return await self.get_user_with_options_async(instance_id, application_id, user_id, headers, runtime)

    def get_user_id_by_email_with_options(
        self,
        instance_id: str,
        application_id: str,
        request: eiam_developerapi_20220225_models.GetUserIdByEmailRequest,
        headers: eiam_developerapi_20220225_models.GetUserIdByEmailHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.GetUserIdByEmailResponse:
        """
        @summary Queries the ID of an Employee Identity and Access Management (EIAM) account by email address.
        
        @param request: GetUserIdByEmailRequest
        @param headers: GetUserIdByEmailHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserIdByEmailResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.email):
            body['email'] = request.email
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUserIdByEmail',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/users/_/actions/getUserIdByEmail',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.GetUserIdByEmailResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def get_user_id_by_email_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        request: eiam_developerapi_20220225_models.GetUserIdByEmailRequest,
        headers: eiam_developerapi_20220225_models.GetUserIdByEmailHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.GetUserIdByEmailResponse:
        """
        @summary Queries the ID of an Employee Identity and Access Management (EIAM) account by email address.
        
        @param request: GetUserIdByEmailRequest
        @param headers: GetUserIdByEmailHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserIdByEmailResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.email):
            body['email'] = request.email
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUserIdByEmail',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/users/_/actions/getUserIdByEmail',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.GetUserIdByEmailResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def get_user_id_by_email(
        self,
        instance_id: str,
        application_id: str,
        request: eiam_developerapi_20220225_models.GetUserIdByEmailRequest,
    ) -> eiam_developerapi_20220225_models.GetUserIdByEmailResponse:
        """
        @summary Queries the ID of an Employee Identity and Access Management (EIAM) account by email address.
        
        @param request: GetUserIdByEmailRequest
        @return: GetUserIdByEmailResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.GetUserIdByEmailHeaders()
        return self.get_user_id_by_email_with_options(instance_id, application_id, request, headers, runtime)

    async def get_user_id_by_email_async(
        self,
        instance_id: str,
        application_id: str,
        request: eiam_developerapi_20220225_models.GetUserIdByEmailRequest,
    ) -> eiam_developerapi_20220225_models.GetUserIdByEmailResponse:
        """
        @summary Queries the ID of an Employee Identity and Access Management (EIAM) account by email address.
        
        @param request: GetUserIdByEmailRequest
        @return: GetUserIdByEmailResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.GetUserIdByEmailHeaders()
        return await self.get_user_id_by_email_with_options_async(instance_id, application_id, request, headers, runtime)

    def get_user_id_by_phone_number_with_options(
        self,
        instance_id: str,
        application_id: str,
        request: eiam_developerapi_20220225_models.GetUserIdByPhoneNumberRequest,
        headers: eiam_developerapi_20220225_models.GetUserIdByPhoneNumberHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.GetUserIdByPhoneNumberResponse:
        """
        @summary Queries the ID of an Employee Identity and Access Management (EIAM) account based on the mobile number.
        
        @param request: GetUserIdByPhoneNumberRequest
        @param headers: GetUserIdByPhoneNumberHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserIdByPhoneNumberResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.phone_number):
            body['phoneNumber'] = request.phone_number
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUserIdByPhoneNumber',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/users/_/actions/getUserIdByPhoneNumber',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.GetUserIdByPhoneNumberResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def get_user_id_by_phone_number_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        request: eiam_developerapi_20220225_models.GetUserIdByPhoneNumberRequest,
        headers: eiam_developerapi_20220225_models.GetUserIdByPhoneNumberHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.GetUserIdByPhoneNumberResponse:
        """
        @summary Queries the ID of an Employee Identity and Access Management (EIAM) account based on the mobile number.
        
        @param request: GetUserIdByPhoneNumberRequest
        @param headers: GetUserIdByPhoneNumberHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserIdByPhoneNumberResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.phone_number):
            body['phoneNumber'] = request.phone_number
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUserIdByPhoneNumber',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/users/_/actions/getUserIdByPhoneNumber',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.GetUserIdByPhoneNumberResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def get_user_id_by_phone_number(
        self,
        instance_id: str,
        application_id: str,
        request: eiam_developerapi_20220225_models.GetUserIdByPhoneNumberRequest,
    ) -> eiam_developerapi_20220225_models.GetUserIdByPhoneNumberResponse:
        """
        @summary Queries the ID of an Employee Identity and Access Management (EIAM) account based on the mobile number.
        
        @param request: GetUserIdByPhoneNumberRequest
        @return: GetUserIdByPhoneNumberResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.GetUserIdByPhoneNumberHeaders()
        return self.get_user_id_by_phone_number_with_options(instance_id, application_id, request, headers, runtime)

    async def get_user_id_by_phone_number_async(
        self,
        instance_id: str,
        application_id: str,
        request: eiam_developerapi_20220225_models.GetUserIdByPhoneNumberRequest,
    ) -> eiam_developerapi_20220225_models.GetUserIdByPhoneNumberResponse:
        """
        @summary Queries the ID of an Employee Identity and Access Management (EIAM) account based on the mobile number.
        
        @param request: GetUserIdByPhoneNumberRequest
        @return: GetUserIdByPhoneNumberResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.GetUserIdByPhoneNumberHeaders()
        return await self.get_user_id_by_phone_number_with_options_async(instance_id, application_id, request, headers, runtime)

    def get_user_id_by_user_external_id_with_options(
        self,
        instance_id: str,
        application_id: str,
        request: eiam_developerapi_20220225_models.GetUserIdByUserExternalIdRequest,
        headers: eiam_developerapi_20220225_models.GetUserIdByUserExternalIdHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.GetUserIdByUserExternalIdResponse:
        """
        @summary Queries the ID of an Employee Identity and Access Management (EIAM) account based on the external ID.
        
        @param request: GetUserIdByUserExternalIdRequest
        @param headers: GetUserIdByUserExternalIdHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserIdByUserExternalIdResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.user_external_id):
            body['userExternalId'] = request.user_external_id
        if not UtilClient.is_unset(request.user_source_id):
            body['userSourceId'] = request.user_source_id
        if not UtilClient.is_unset(request.user_source_type):
            body['userSourceType'] = request.user_source_type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUserIdByUserExternalId',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/users/_/actions/getUserIdByExternalId',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.GetUserIdByUserExternalIdResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def get_user_id_by_user_external_id_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        request: eiam_developerapi_20220225_models.GetUserIdByUserExternalIdRequest,
        headers: eiam_developerapi_20220225_models.GetUserIdByUserExternalIdHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.GetUserIdByUserExternalIdResponse:
        """
        @summary Queries the ID of an Employee Identity and Access Management (EIAM) account based on the external ID.
        
        @param request: GetUserIdByUserExternalIdRequest
        @param headers: GetUserIdByUserExternalIdHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserIdByUserExternalIdResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.user_external_id):
            body['userExternalId'] = request.user_external_id
        if not UtilClient.is_unset(request.user_source_id):
            body['userSourceId'] = request.user_source_id
        if not UtilClient.is_unset(request.user_source_type):
            body['userSourceType'] = request.user_source_type
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUserIdByUserExternalId',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/users/_/actions/getUserIdByExternalId',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.GetUserIdByUserExternalIdResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def get_user_id_by_user_external_id(
        self,
        instance_id: str,
        application_id: str,
        request: eiam_developerapi_20220225_models.GetUserIdByUserExternalIdRequest,
    ) -> eiam_developerapi_20220225_models.GetUserIdByUserExternalIdResponse:
        """
        @summary Queries the ID of an Employee Identity and Access Management (EIAM) account based on the external ID.
        
        @param request: GetUserIdByUserExternalIdRequest
        @return: GetUserIdByUserExternalIdResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.GetUserIdByUserExternalIdHeaders()
        return self.get_user_id_by_user_external_id_with_options(instance_id, application_id, request, headers, runtime)

    async def get_user_id_by_user_external_id_async(
        self,
        instance_id: str,
        application_id: str,
        request: eiam_developerapi_20220225_models.GetUserIdByUserExternalIdRequest,
    ) -> eiam_developerapi_20220225_models.GetUserIdByUserExternalIdResponse:
        """
        @summary Queries the ID of an Employee Identity and Access Management (EIAM) account based on the external ID.
        
        @param request: GetUserIdByUserExternalIdRequest
        @return: GetUserIdByUserExternalIdResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.GetUserIdByUserExternalIdHeaders()
        return await self.get_user_id_by_user_external_id_with_options_async(instance_id, application_id, request, headers, runtime)

    def get_user_id_by_username_with_options(
        self,
        instance_id: str,
        application_id: str,
        request: eiam_developerapi_20220225_models.GetUserIdByUsernameRequest,
        headers: eiam_developerapi_20220225_models.GetUserIdByUsernameHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.GetUserIdByUsernameResponse:
        """
        @summary Queries the ID of an Employee Identity and Access Management (EIAM) account based on the username.
        
        @param request: GetUserIdByUsernameRequest
        @param headers: GetUserIdByUsernameHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserIdByUsernameResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.username):
            body['username'] = request.username
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUserIdByUsername',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/users/_/actions/getUserIdByUsername',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.GetUserIdByUsernameResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def get_user_id_by_username_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        request: eiam_developerapi_20220225_models.GetUserIdByUsernameRequest,
        headers: eiam_developerapi_20220225_models.GetUserIdByUsernameHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.GetUserIdByUsernameResponse:
        """
        @summary Queries the ID of an Employee Identity and Access Management (EIAM) account based on the username.
        
        @param request: GetUserIdByUsernameRequest
        @param headers: GetUserIdByUsernameHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserIdByUsernameResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.username):
            body['username'] = request.username
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUserIdByUsername',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/users/_/actions/getUserIdByUsername',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.GetUserIdByUsernameResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def get_user_id_by_username(
        self,
        instance_id: str,
        application_id: str,
        request: eiam_developerapi_20220225_models.GetUserIdByUsernameRequest,
    ) -> eiam_developerapi_20220225_models.GetUserIdByUsernameResponse:
        """
        @summary Queries the ID of an Employee Identity and Access Management (EIAM) account based on the username.
        
        @param request: GetUserIdByUsernameRequest
        @return: GetUserIdByUsernameResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.GetUserIdByUsernameHeaders()
        return self.get_user_id_by_username_with_options(instance_id, application_id, request, headers, runtime)

    async def get_user_id_by_username_async(
        self,
        instance_id: str,
        application_id: str,
        request: eiam_developerapi_20220225_models.GetUserIdByUsernameRequest,
    ) -> eiam_developerapi_20220225_models.GetUserIdByUsernameResponse:
        """
        @summary Queries the ID of an Employee Identity and Access Management (EIAM) account based on the username.
        
        @param request: GetUserIdByUsernameRequest
        @return: GetUserIdByUsernameResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.GetUserIdByUsernameHeaders()
        return await self.get_user_id_by_username_with_options_async(instance_id, application_id, request, headers, runtime)

    def get_user_info_with_options(
        self,
        instance_id: str,
        application_id: str,
        headers: eiam_developerapi_20220225_models.GetUserInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.GetUserInfoResponse:
        """
        @summary Queries the information of a user by using the user token.
        
        @param headers: GetUserInfoHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserInfoResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetUserInfo',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/oauth2/userinfo',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.GetUserInfoResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def get_user_info_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        headers: eiam_developerapi_20220225_models.GetUserInfoHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.GetUserInfoResponse:
        """
        @summary Queries the information of a user by using the user token.
        
        @param headers: GetUserInfoHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserInfoResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetUserInfo',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/oauth2/userinfo',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.GetUserInfoResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def get_user_info(
        self,
        instance_id: str,
        application_id: str,
    ) -> eiam_developerapi_20220225_models.GetUserInfoResponse:
        """
        @summary Queries the information of a user by using the user token.
        
        @return: GetUserInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.GetUserInfoHeaders()
        return self.get_user_info_with_options(instance_id, application_id, headers, runtime)

    async def get_user_info_async(
        self,
        instance_id: str,
        application_id: str,
    ) -> eiam_developerapi_20220225_models.GetUserInfoResponse:
        """
        @summary Queries the information of a user by using the user token.
        
        @return: GetUserInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.GetUserInfoHeaders()
        return await self.get_user_info_with_options_async(instance_id, application_id, headers, runtime)

    def list_groups_with_options(
        self,
        instance_id: str,
        application_id: str,
        request: eiam_developerapi_20220225_models.ListGroupsRequest,
        headers: eiam_developerapi_20220225_models.ListGroupsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.ListGroupsResponse:
        """
        @summary Queries information about Employee Identity and Access Management (EIAM) groups by page.
        
        @param request: ListGroupsRequest
        @param headers: ListGroupsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name_start_with):
            query['groupNameStartWith'] = request.group_name_start_with
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroups',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/groups',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.ListGroupsResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def list_groups_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        request: eiam_developerapi_20220225_models.ListGroupsRequest,
        headers: eiam_developerapi_20220225_models.ListGroupsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.ListGroupsResponse:
        """
        @summary Queries information about Employee Identity and Access Management (EIAM) groups by page.
        
        @param request: ListGroupsRequest
        @param headers: ListGroupsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name_start_with):
            query['groupNameStartWith'] = request.group_name_start_with
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroups',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/groups',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.ListGroupsResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def list_groups(
        self,
        instance_id: str,
        application_id: str,
        request: eiam_developerapi_20220225_models.ListGroupsRequest,
    ) -> eiam_developerapi_20220225_models.ListGroupsResponse:
        """
        @summary Queries information about Employee Identity and Access Management (EIAM) groups by page.
        
        @param request: ListGroupsRequest
        @return: ListGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.ListGroupsHeaders()
        return self.list_groups_with_options(instance_id, application_id, request, headers, runtime)

    async def list_groups_async(
        self,
        instance_id: str,
        application_id: str,
        request: eiam_developerapi_20220225_models.ListGroupsRequest,
    ) -> eiam_developerapi_20220225_models.ListGroupsResponse:
        """
        @summary Queries information about Employee Identity and Access Management (EIAM) groups by page.
        
        @param request: ListGroupsRequest
        @return: ListGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.ListGroupsHeaders()
        return await self.list_groups_with_options_async(instance_id, application_id, request, headers, runtime)

    def list_groups_for_user_with_options(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        request: eiam_developerapi_20220225_models.ListGroupsForUserRequest,
        headers: eiam_developerapi_20220225_models.ListGroupsForUserHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.ListGroupsForUserResponse:
        """
        @summary 获取账户关联组列表
        
        @param request: ListGroupsForUserRequest
        @param headers: ListGroupsForUserHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGroupsForUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroupsForUser',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/users/{OpenApiUtilClient.get_encode_param(user_id)}/actions/listGroupsForUser',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.ListGroupsForUserResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def list_groups_for_user_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        request: eiam_developerapi_20220225_models.ListGroupsForUserRequest,
        headers: eiam_developerapi_20220225_models.ListGroupsForUserHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.ListGroupsForUserResponse:
        """
        @summary 获取账户关联组列表
        
        @param request: ListGroupsForUserRequest
        @param headers: ListGroupsForUserHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGroupsForUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroupsForUser',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/users/{OpenApiUtilClient.get_encode_param(user_id)}/actions/listGroupsForUser',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.ListGroupsForUserResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def list_groups_for_user(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        request: eiam_developerapi_20220225_models.ListGroupsForUserRequest,
    ) -> eiam_developerapi_20220225_models.ListGroupsForUserResponse:
        """
        @summary 获取账户关联组列表
        
        @param request: ListGroupsForUserRequest
        @return: ListGroupsForUserResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.ListGroupsForUserHeaders()
        return self.list_groups_for_user_with_options(instance_id, application_id, user_id, request, headers, runtime)

    async def list_groups_for_user_async(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        request: eiam_developerapi_20220225_models.ListGroupsForUserRequest,
    ) -> eiam_developerapi_20220225_models.ListGroupsForUserResponse:
        """
        @summary 获取账户关联组列表
        
        @param request: ListGroupsForUserRequest
        @return: ListGroupsForUserResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.ListGroupsForUserHeaders()
        return await self.list_groups_for_user_with_options_async(instance_id, application_id, user_id, request, headers, runtime)

    def list_organizational_unit_parent_ids_with_options(
        self,
        instance_id: str,
        application_id: str,
        organizational_unit_id: str,
        headers: eiam_developerapi_20220225_models.ListOrganizationalUnitParentIdsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.ListOrganizationalUnitParentIdsResponse:
        """
        @summary Queries the information of all the parent organizational units of an organizational unit.
        
        @param headers: ListOrganizationalUnitParentIdsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOrganizationalUnitParentIdsResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='ListOrganizationalUnitParentIds',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/organizationalUnits/{OpenApiUtilClient.get_encode_param(organizational_unit_id)}/parentIds',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.ListOrganizationalUnitParentIdsResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def list_organizational_unit_parent_ids_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        organizational_unit_id: str,
        headers: eiam_developerapi_20220225_models.ListOrganizationalUnitParentIdsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.ListOrganizationalUnitParentIdsResponse:
        """
        @summary Queries the information of all the parent organizational units of an organizational unit.
        
        @param headers: ListOrganizationalUnitParentIdsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOrganizationalUnitParentIdsResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='ListOrganizationalUnitParentIds',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/organizationalUnits/{OpenApiUtilClient.get_encode_param(organizational_unit_id)}/parentIds',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.ListOrganizationalUnitParentIdsResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def list_organizational_unit_parent_ids(
        self,
        instance_id: str,
        application_id: str,
        organizational_unit_id: str,
    ) -> eiam_developerapi_20220225_models.ListOrganizationalUnitParentIdsResponse:
        """
        @summary Queries the information of all the parent organizational units of an organizational unit.
        
        @return: ListOrganizationalUnitParentIdsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.ListOrganizationalUnitParentIdsHeaders()
        return self.list_organizational_unit_parent_ids_with_options(instance_id, application_id, organizational_unit_id, headers, runtime)

    async def list_organizational_unit_parent_ids_async(
        self,
        instance_id: str,
        application_id: str,
        organizational_unit_id: str,
    ) -> eiam_developerapi_20220225_models.ListOrganizationalUnitParentIdsResponse:
        """
        @summary Queries the information of all the parent organizational units of an organizational unit.
        
        @return: ListOrganizationalUnitParentIdsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.ListOrganizationalUnitParentIdsHeaders()
        return await self.list_organizational_unit_parent_ids_with_options_async(instance_id, application_id, organizational_unit_id, headers, runtime)

    def list_organizational_units_with_options(
        self,
        instance_id: str,
        application_id: str,
        request: eiam_developerapi_20220225_models.ListOrganizationalUnitsRequest,
        headers: eiam_developerapi_20220225_models.ListOrganizationalUnitsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.ListOrganizationalUnitsResponse:
        """
        @summary Queries the information of Employee Identity and Access Management (EIAM) organizational units by page.
        
        @param request: ListOrganizationalUnitsRequest
        @param headers: ListOrganizationalUnitsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOrganizationalUnitsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_id):
            query['parentId'] = request.parent_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOrganizationalUnits',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/organizationalUnits',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.ListOrganizationalUnitsResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def list_organizational_units_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        request: eiam_developerapi_20220225_models.ListOrganizationalUnitsRequest,
        headers: eiam_developerapi_20220225_models.ListOrganizationalUnitsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.ListOrganizationalUnitsResponse:
        """
        @summary Queries the information of Employee Identity and Access Management (EIAM) organizational units by page.
        
        @param request: ListOrganizationalUnitsRequest
        @param headers: ListOrganizationalUnitsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOrganizationalUnitsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_id):
            query['parentId'] = request.parent_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOrganizationalUnits',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/organizationalUnits',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.ListOrganizationalUnitsResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def list_organizational_units(
        self,
        instance_id: str,
        application_id: str,
        request: eiam_developerapi_20220225_models.ListOrganizationalUnitsRequest,
    ) -> eiam_developerapi_20220225_models.ListOrganizationalUnitsResponse:
        """
        @summary Queries the information of Employee Identity and Access Management (EIAM) organizational units by page.
        
        @param request: ListOrganizationalUnitsRequest
        @return: ListOrganizationalUnitsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.ListOrganizationalUnitsHeaders()
        return self.list_organizational_units_with_options(instance_id, application_id, request, headers, runtime)

    async def list_organizational_units_async(
        self,
        instance_id: str,
        application_id: str,
        request: eiam_developerapi_20220225_models.ListOrganizationalUnitsRequest,
    ) -> eiam_developerapi_20220225_models.ListOrganizationalUnitsResponse:
        """
        @summary Queries the information of Employee Identity and Access Management (EIAM) organizational units by page.
        
        @param request: ListOrganizationalUnitsRequest
        @return: ListOrganizationalUnitsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.ListOrganizationalUnitsHeaders()
        return await self.list_organizational_units_with_options_async(instance_id, application_id, request, headers, runtime)

    def list_users_with_options(
        self,
        instance_id: str,
        application_id: str,
        request: eiam_developerapi_20220225_models.ListUsersRequest,
        headers: eiam_developerapi_20220225_models.ListUsersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.ListUsersResponse:
        """
        @summary Queries the information of Employee Identity and Access Management (EIAM) accounts by page.
        
        @param request: ListUsersRequest
        @param headers: ListUsersHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organizational_unit_id):
            query['organizationalUnitId'] = request.organizational_unit_id
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsers',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/users',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.ListUsersResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def list_users_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        request: eiam_developerapi_20220225_models.ListUsersRequest,
        headers: eiam_developerapi_20220225_models.ListUsersHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.ListUsersResponse:
        """
        @summary Queries the information of Employee Identity and Access Management (EIAM) accounts by page.
        
        @param request: ListUsersRequest
        @param headers: ListUsersHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.organizational_unit_id):
            query['organizationalUnitId'] = request.organizational_unit_id
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsers',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/users',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.ListUsersResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def list_users(
        self,
        instance_id: str,
        application_id: str,
        request: eiam_developerapi_20220225_models.ListUsersRequest,
    ) -> eiam_developerapi_20220225_models.ListUsersResponse:
        """
        @summary Queries the information of Employee Identity and Access Management (EIAM) accounts by page.
        
        @param request: ListUsersRequest
        @return: ListUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.ListUsersHeaders()
        return self.list_users_with_options(instance_id, application_id, request, headers, runtime)

    async def list_users_async(
        self,
        instance_id: str,
        application_id: str,
        request: eiam_developerapi_20220225_models.ListUsersRequest,
    ) -> eiam_developerapi_20220225_models.ListUsersResponse:
        """
        @summary Queries the information of Employee Identity and Access Management (EIAM) accounts by page.
        
        @param request: ListUsersRequest
        @return: ListUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.ListUsersHeaders()
        return await self.list_users_with_options_async(instance_id, application_id, request, headers, runtime)

    def list_users_for_group_with_options(
        self,
        instance_id: str,
        application_id: str,
        group_id: str,
        request: eiam_developerapi_20220225_models.ListUsersForGroupRequest,
        headers: eiam_developerapi_20220225_models.ListUsersForGroupHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.ListUsersForGroupResponse:
        """
        @summary Queries accounts in an Employee Identity and Access Management (EIAM) group.
        
        @param request: ListUsersForGroupRequest
        @param headers: ListUsersForGroupHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUsersForGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsersForGroup',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/groups/{OpenApiUtilClient.get_encode_param(group_id)}/actions/listUsersForGroup',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.ListUsersForGroupResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def list_users_for_group_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        group_id: str,
        request: eiam_developerapi_20220225_models.ListUsersForGroupRequest,
        headers: eiam_developerapi_20220225_models.ListUsersForGroupHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.ListUsersForGroupResponse:
        """
        @summary Queries accounts in an Employee Identity and Access Management (EIAM) group.
        
        @param request: ListUsersForGroupRequest
        @param headers: ListUsersForGroupHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUsersForGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsersForGroup',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/groups/{OpenApiUtilClient.get_encode_param(group_id)}/actions/listUsersForGroup',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.ListUsersForGroupResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def list_users_for_group(
        self,
        instance_id: str,
        application_id: str,
        group_id: str,
        request: eiam_developerapi_20220225_models.ListUsersForGroupRequest,
    ) -> eiam_developerapi_20220225_models.ListUsersForGroupResponse:
        """
        @summary Queries accounts in an Employee Identity and Access Management (EIAM) group.
        
        @param request: ListUsersForGroupRequest
        @return: ListUsersForGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.ListUsersForGroupHeaders()
        return self.list_users_for_group_with_options(instance_id, application_id, group_id, request, headers, runtime)

    async def list_users_for_group_async(
        self,
        instance_id: str,
        application_id: str,
        group_id: str,
        request: eiam_developerapi_20220225_models.ListUsersForGroupRequest,
    ) -> eiam_developerapi_20220225_models.ListUsersForGroupResponse:
        """
        @summary Queries accounts in an Employee Identity and Access Management (EIAM) group.
        
        @param request: ListUsersForGroupRequest
        @return: ListUsersForGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.ListUsersForGroupHeaders()
        return await self.list_users_for_group_with_options_async(instance_id, application_id, group_id, request, headers, runtime)

    def patch_group_with_options(
        self,
        instance_id: str,
        application_id: str,
        group_id: str,
        request: eiam_developerapi_20220225_models.PatchGroupRequest,
        headers: eiam_developerapi_20220225_models.PatchGroupHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.PatchGroupResponse:
        """
        @summary Modifies information about an Employee Identity and Access Management (EIAM) group.
        
        @param request: PatchGroupRequest
        @param headers: PatchGroupHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: PatchGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_name):
            body['groupName'] = request.group_name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PatchGroup',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/groups/{OpenApiUtilClient.get_encode_param(group_id)}',
            method='PATCH',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.PatchGroupResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def patch_group_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        group_id: str,
        request: eiam_developerapi_20220225_models.PatchGroupRequest,
        headers: eiam_developerapi_20220225_models.PatchGroupHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.PatchGroupResponse:
        """
        @summary Modifies information about an Employee Identity and Access Management (EIAM) group.
        
        @param request: PatchGroupRequest
        @param headers: PatchGroupHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: PatchGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_name):
            body['groupName'] = request.group_name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PatchGroup',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/groups/{OpenApiUtilClient.get_encode_param(group_id)}',
            method='PATCH',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.PatchGroupResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def patch_group(
        self,
        instance_id: str,
        application_id: str,
        group_id: str,
        request: eiam_developerapi_20220225_models.PatchGroupRequest,
    ) -> eiam_developerapi_20220225_models.PatchGroupResponse:
        """
        @summary Modifies information about an Employee Identity and Access Management (EIAM) group.
        
        @param request: PatchGroupRequest
        @return: PatchGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.PatchGroupHeaders()
        return self.patch_group_with_options(instance_id, application_id, group_id, request, headers, runtime)

    async def patch_group_async(
        self,
        instance_id: str,
        application_id: str,
        group_id: str,
        request: eiam_developerapi_20220225_models.PatchGroupRequest,
    ) -> eiam_developerapi_20220225_models.PatchGroupResponse:
        """
        @summary Modifies information about an Employee Identity and Access Management (EIAM) group.
        
        @param request: PatchGroupRequest
        @return: PatchGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.PatchGroupHeaders()
        return await self.patch_group_with_options_async(instance_id, application_id, group_id, request, headers, runtime)

    def patch_organizational_unit_with_options(
        self,
        instance_id: str,
        application_id: str,
        organizational_unit_id: str,
        request: eiam_developerapi_20220225_models.PatchOrganizationalUnitRequest,
        headers: eiam_developerapi_20220225_models.PatchOrganizationalUnitHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.PatchOrganizationalUnitResponse:
        """
        @summary Modifies an EIAM organizational unit.
        
        @description The operation conforms to the HTTP PATCH request method. The value of a parameter is modified only if the parameter is specified in the request.
        
        @param request: PatchOrganizationalUnitRequest
        @param headers: PatchOrganizationalUnitHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: PatchOrganizationalUnitResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.organizational_unit_name):
            body['organizationalUnitName'] = request.organizational_unit_name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PatchOrganizationalUnit',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/organizationalUnits/{OpenApiUtilClient.get_encode_param(organizational_unit_id)}',
            method='PATCH',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.PatchOrganizationalUnitResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def patch_organizational_unit_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        organizational_unit_id: str,
        request: eiam_developerapi_20220225_models.PatchOrganizationalUnitRequest,
        headers: eiam_developerapi_20220225_models.PatchOrganizationalUnitHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.PatchOrganizationalUnitResponse:
        """
        @summary Modifies an EIAM organizational unit.
        
        @description The operation conforms to the HTTP PATCH request method. The value of a parameter is modified only if the parameter is specified in the request.
        
        @param request: PatchOrganizationalUnitRequest
        @param headers: PatchOrganizationalUnitHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: PatchOrganizationalUnitResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.organizational_unit_name):
            body['organizationalUnitName'] = request.organizational_unit_name
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PatchOrganizationalUnit',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/organizationalUnits/{OpenApiUtilClient.get_encode_param(organizational_unit_id)}',
            method='PATCH',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.PatchOrganizationalUnitResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def patch_organizational_unit(
        self,
        instance_id: str,
        application_id: str,
        organizational_unit_id: str,
        request: eiam_developerapi_20220225_models.PatchOrganizationalUnitRequest,
    ) -> eiam_developerapi_20220225_models.PatchOrganizationalUnitResponse:
        """
        @summary Modifies an EIAM organizational unit.
        
        @description The operation conforms to the HTTP PATCH request method. The value of a parameter is modified only if the parameter is specified in the request.
        
        @param request: PatchOrganizationalUnitRequest
        @return: PatchOrganizationalUnitResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.PatchOrganizationalUnitHeaders()
        return self.patch_organizational_unit_with_options(instance_id, application_id, organizational_unit_id, request, headers, runtime)

    async def patch_organizational_unit_async(
        self,
        instance_id: str,
        application_id: str,
        organizational_unit_id: str,
        request: eiam_developerapi_20220225_models.PatchOrganizationalUnitRequest,
    ) -> eiam_developerapi_20220225_models.PatchOrganizationalUnitResponse:
        """
        @summary Modifies an EIAM organizational unit.
        
        @description The operation conforms to the HTTP PATCH request method. The value of a parameter is modified only if the parameter is specified in the request.
        
        @param request: PatchOrganizationalUnitRequest
        @return: PatchOrganizationalUnitResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.PatchOrganizationalUnitHeaders()
        return await self.patch_organizational_unit_with_options_async(instance_id, application_id, organizational_unit_id, request, headers, runtime)

    def patch_user_with_options(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        request: eiam_developerapi_20220225_models.PatchUserRequest,
        headers: eiam_developerapi_20220225_models.PatchUserHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.PatchUserResponse:
        """
        @summary Modifies an Employee Identity and Access Management (EIAM) account.
        
        @description The operation conforms to the HTTP PATCH request method. The value of a parameter is modified only if the parameter is specified in the request.
        
        @param request: PatchUserRequest
        @param headers: PatchUserHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: PatchUserResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.custom_fields):
            body['customFields'] = request.custom_fields
        if not UtilClient.is_unset(request.display_name):
            body['displayName'] = request.display_name
        if not UtilClient.is_unset(request.email):
            body['email'] = request.email
        if not UtilClient.is_unset(request.email_verified):
            body['emailVerified'] = request.email_verified
        if not UtilClient.is_unset(request.phone_number):
            body['phoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.phone_number_verified):
            body['phoneNumberVerified'] = request.phone_number_verified
        if not UtilClient.is_unset(request.phone_region):
            body['phoneRegion'] = request.phone_region
        if not UtilClient.is_unset(request.username):
            body['username'] = request.username
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PatchUser',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/users/{OpenApiUtilClient.get_encode_param(user_id)}',
            method='PATCH',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.PatchUserResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def patch_user_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        request: eiam_developerapi_20220225_models.PatchUserRequest,
        headers: eiam_developerapi_20220225_models.PatchUserHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.PatchUserResponse:
        """
        @summary Modifies an Employee Identity and Access Management (EIAM) account.
        
        @description The operation conforms to the HTTP PATCH request method. The value of a parameter is modified only if the parameter is specified in the request.
        
        @param request: PatchUserRequest
        @param headers: PatchUserHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: PatchUserResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.custom_fields):
            body['customFields'] = request.custom_fields
        if not UtilClient.is_unset(request.display_name):
            body['displayName'] = request.display_name
        if not UtilClient.is_unset(request.email):
            body['email'] = request.email
        if not UtilClient.is_unset(request.email_verified):
            body['emailVerified'] = request.email_verified
        if not UtilClient.is_unset(request.phone_number):
            body['phoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.phone_number_verified):
            body['phoneNumberVerified'] = request.phone_number_verified
        if not UtilClient.is_unset(request.phone_region):
            body['phoneRegion'] = request.phone_region
        if not UtilClient.is_unset(request.username):
            body['username'] = request.username
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PatchUser',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/users/{OpenApiUtilClient.get_encode_param(user_id)}',
            method='PATCH',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.PatchUserResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def patch_user(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        request: eiam_developerapi_20220225_models.PatchUserRequest,
    ) -> eiam_developerapi_20220225_models.PatchUserResponse:
        """
        @summary Modifies an Employee Identity and Access Management (EIAM) account.
        
        @description The operation conforms to the HTTP PATCH request method. The value of a parameter is modified only if the parameter is specified in the request.
        
        @param request: PatchUserRequest
        @return: PatchUserResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.PatchUserHeaders()
        return self.patch_user_with_options(instance_id, application_id, user_id, request, headers, runtime)

    async def patch_user_async(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        request: eiam_developerapi_20220225_models.PatchUserRequest,
    ) -> eiam_developerapi_20220225_models.PatchUserResponse:
        """
        @summary Modifies an Employee Identity and Access Management (EIAM) account.
        
        @description The operation conforms to the HTTP PATCH request method. The value of a parameter is modified only if the parameter is specified in the request.
        
        @param request: PatchUserRequest
        @return: PatchUserResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.PatchUserHeaders()
        return await self.patch_user_with_options_async(instance_id, application_id, user_id, request, headers, runtime)

    def remove_user_from_organizational_units_with_options(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        request: eiam_developerapi_20220225_models.RemoveUserFromOrganizationalUnitsRequest,
        headers: eiam_developerapi_20220225_models.RemoveUserFromOrganizationalUnitsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.RemoveUserFromOrganizationalUnitsResponse:
        """
        @summary 将账户从多个组织移除【不支持移除主组织】
        
        @param request: RemoveUserFromOrganizationalUnitsRequest
        @param headers: RemoveUserFromOrganizationalUnitsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveUserFromOrganizationalUnitsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.organizational_unit_ids):
            body['organizationalUnitIds'] = request.organizational_unit_ids
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveUserFromOrganizationalUnits',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/users/{OpenApiUtilClient.get_encode_param(user_id)}/actions/removeUserFromOrganizationalUnits',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.RemoveUserFromOrganizationalUnitsResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def remove_user_from_organizational_units_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        request: eiam_developerapi_20220225_models.RemoveUserFromOrganizationalUnitsRequest,
        headers: eiam_developerapi_20220225_models.RemoveUserFromOrganizationalUnitsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.RemoveUserFromOrganizationalUnitsResponse:
        """
        @summary 将账户从多个组织移除【不支持移除主组织】
        
        @param request: RemoveUserFromOrganizationalUnitsRequest
        @param headers: RemoveUserFromOrganizationalUnitsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveUserFromOrganizationalUnitsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.organizational_unit_ids):
            body['organizationalUnitIds'] = request.organizational_unit_ids
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveUserFromOrganizationalUnits',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/users/{OpenApiUtilClient.get_encode_param(user_id)}/actions/removeUserFromOrganizationalUnits',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.RemoveUserFromOrganizationalUnitsResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def remove_user_from_organizational_units(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        request: eiam_developerapi_20220225_models.RemoveUserFromOrganizationalUnitsRequest,
    ) -> eiam_developerapi_20220225_models.RemoveUserFromOrganizationalUnitsResponse:
        """
        @summary 将账户从多个组织移除【不支持移除主组织】
        
        @param request: RemoveUserFromOrganizationalUnitsRequest
        @return: RemoveUserFromOrganizationalUnitsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.RemoveUserFromOrganizationalUnitsHeaders()
        return self.remove_user_from_organizational_units_with_options(instance_id, application_id, user_id, request, headers, runtime)

    async def remove_user_from_organizational_units_async(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        request: eiam_developerapi_20220225_models.RemoveUserFromOrganizationalUnitsRequest,
    ) -> eiam_developerapi_20220225_models.RemoveUserFromOrganizationalUnitsResponse:
        """
        @summary 将账户从多个组织移除【不支持移除主组织】
        
        @param request: RemoveUserFromOrganizationalUnitsRequest
        @return: RemoveUserFromOrganizationalUnitsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.RemoveUserFromOrganizationalUnitsHeaders()
        return await self.remove_user_from_organizational_units_with_options_async(instance_id, application_id, user_id, request, headers, runtime)

    def remove_users_from_group_with_options(
        self,
        instance_id: str,
        application_id: str,
        group_id: str,
        request: eiam_developerapi_20220225_models.RemoveUsersFromGroupRequest,
        headers: eiam_developerapi_20220225_models.RemoveUsersFromGroupHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.RemoveUsersFromGroupResponse:
        """
        @summary Removes multiple Employee Identity and Access Management (EIAM) accounts from an EIAM group. If an account does not belong to the group, the removal succeeds by default.
        
        @param request: RemoveUsersFromGroupRequest
        @param headers: RemoveUsersFromGroupHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveUsersFromGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.user_ids):
            body['userIds'] = request.user_ids
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveUsersFromGroup',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/groups/{OpenApiUtilClient.get_encode_param(group_id)}/actions/removeUsersFromGroup',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.RemoveUsersFromGroupResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def remove_users_from_group_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        group_id: str,
        request: eiam_developerapi_20220225_models.RemoveUsersFromGroupRequest,
        headers: eiam_developerapi_20220225_models.RemoveUsersFromGroupHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.RemoveUsersFromGroupResponse:
        """
        @summary Removes multiple Employee Identity and Access Management (EIAM) accounts from an EIAM group. If an account does not belong to the group, the removal succeeds by default.
        
        @param request: RemoveUsersFromGroupRequest
        @param headers: RemoveUsersFromGroupHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveUsersFromGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.user_ids):
            body['userIds'] = request.user_ids
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveUsersFromGroup',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/groups/{OpenApiUtilClient.get_encode_param(group_id)}/actions/removeUsersFromGroup',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.RemoveUsersFromGroupResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def remove_users_from_group(
        self,
        instance_id: str,
        application_id: str,
        group_id: str,
        request: eiam_developerapi_20220225_models.RemoveUsersFromGroupRequest,
    ) -> eiam_developerapi_20220225_models.RemoveUsersFromGroupResponse:
        """
        @summary Removes multiple Employee Identity and Access Management (EIAM) accounts from an EIAM group. If an account does not belong to the group, the removal succeeds by default.
        
        @param request: RemoveUsersFromGroupRequest
        @return: RemoveUsersFromGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.RemoveUsersFromGroupHeaders()
        return self.remove_users_from_group_with_options(instance_id, application_id, group_id, request, headers, runtime)

    async def remove_users_from_group_async(
        self,
        instance_id: str,
        application_id: str,
        group_id: str,
        request: eiam_developerapi_20220225_models.RemoveUsersFromGroupRequest,
    ) -> eiam_developerapi_20220225_models.RemoveUsersFromGroupResponse:
        """
        @summary Removes multiple Employee Identity and Access Management (EIAM) accounts from an EIAM group. If an account does not belong to the group, the removal succeeds by default.
        
        @param request: RemoveUsersFromGroupRequest
        @return: RemoveUsersFromGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.RemoveUsersFromGroupHeaders()
        return await self.remove_users_from_group_with_options_async(instance_id, application_id, group_id, request, headers, runtime)

    def revoke_token_with_options(
        self,
        instance_id: str,
        application_id: str,
        request: eiam_developerapi_20220225_models.RevokeTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.RevokeTokenResponse:
        """
        @summary Revokes an access token or refresh token.
        
        @param request: RevokeTokenRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RevokeTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['client_id'] = request.client_id
        if not UtilClient.is_unset(request.client_secret):
            query['client_secret'] = request.client_secret
        if not UtilClient.is_unset(request.token):
            query['token'] = request.token
        if not UtilClient.is_unset(request.token_type_hint):
            query['token_type_hint'] = request.token_type_hint
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevokeToken',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/oauth2/revoke',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.RevokeTokenResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def revoke_token_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        request: eiam_developerapi_20220225_models.RevokeTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.RevokeTokenResponse:
        """
        @summary Revokes an access token or refresh token.
        
        @param request: RevokeTokenRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RevokeTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['client_id'] = request.client_id
        if not UtilClient.is_unset(request.client_secret):
            query['client_secret'] = request.client_secret
        if not UtilClient.is_unset(request.token):
            query['token'] = request.token
        if not UtilClient.is_unset(request.token_type_hint):
            query['token_type_hint'] = request.token_type_hint
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevokeToken',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/oauth2/revoke',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.RevokeTokenResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def revoke_token(
        self,
        instance_id: str,
        application_id: str,
        request: eiam_developerapi_20220225_models.RevokeTokenRequest,
    ) -> eiam_developerapi_20220225_models.RevokeTokenResponse:
        """
        @summary Revokes an access token or refresh token.
        
        @param request: RevokeTokenRequest
        @return: RevokeTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.revoke_token_with_options(instance_id, application_id, request, headers, runtime)

    async def revoke_token_async(
        self,
        instance_id: str,
        application_id: str,
        request: eiam_developerapi_20220225_models.RevokeTokenRequest,
    ) -> eiam_developerapi_20220225_models.RevokeTokenResponse:
        """
        @summary Revokes an access token or refresh token.
        
        @param request: RevokeTokenRequest
        @return: RevokeTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.revoke_token_with_options_async(instance_id, application_id, request, headers, runtime)

    def set_user_primary_organizational_unit_with_options(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        request: eiam_developerapi_20220225_models.SetUserPrimaryOrganizationalUnitRequest,
        headers: eiam_developerapi_20220225_models.SetUserPrimaryOrganizationalUnitHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.SetUserPrimaryOrganizationalUnitResponse:
        """
        @summary 将指定组织设置为账户主组织，移除旧主组织，加入新主组织。
        
        @param request: SetUserPrimaryOrganizationalUnitRequest
        @param headers: SetUserPrimaryOrganizationalUnitHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetUserPrimaryOrganizationalUnitResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.organizational_unit_id):
            body['organizationalUnitId'] = request.organizational_unit_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetUserPrimaryOrganizationalUnit',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/users/{OpenApiUtilClient.get_encode_param(user_id)}/actions/setUserPrimaryOrganizationalUnit',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.SetUserPrimaryOrganizationalUnitResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def set_user_primary_organizational_unit_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        request: eiam_developerapi_20220225_models.SetUserPrimaryOrganizationalUnitRequest,
        headers: eiam_developerapi_20220225_models.SetUserPrimaryOrganizationalUnitHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.SetUserPrimaryOrganizationalUnitResponse:
        """
        @summary 将指定组织设置为账户主组织，移除旧主组织，加入新主组织。
        
        @param request: SetUserPrimaryOrganizationalUnitRequest
        @param headers: SetUserPrimaryOrganizationalUnitHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetUserPrimaryOrganizationalUnitResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.organizational_unit_id):
            body['organizationalUnitId'] = request.organizational_unit_id
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetUserPrimaryOrganizationalUnit',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/users/{OpenApiUtilClient.get_encode_param(user_id)}/actions/setUserPrimaryOrganizationalUnit',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.SetUserPrimaryOrganizationalUnitResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def set_user_primary_organizational_unit(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        request: eiam_developerapi_20220225_models.SetUserPrimaryOrganizationalUnitRequest,
    ) -> eiam_developerapi_20220225_models.SetUserPrimaryOrganizationalUnitResponse:
        """
        @summary 将指定组织设置为账户主组织，移除旧主组织，加入新主组织。
        
        @param request: SetUserPrimaryOrganizationalUnitRequest
        @return: SetUserPrimaryOrganizationalUnitResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.SetUserPrimaryOrganizationalUnitHeaders()
        return self.set_user_primary_organizational_unit_with_options(instance_id, application_id, user_id, request, headers, runtime)

    async def set_user_primary_organizational_unit_async(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        request: eiam_developerapi_20220225_models.SetUserPrimaryOrganizationalUnitRequest,
    ) -> eiam_developerapi_20220225_models.SetUserPrimaryOrganizationalUnitResponse:
        """
        @summary 将指定组织设置为账户主组织，移除旧主组织，加入新主组织。
        
        @param request: SetUserPrimaryOrganizationalUnitRequest
        @return: SetUserPrimaryOrganizationalUnitResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.SetUserPrimaryOrganizationalUnitHeaders()
        return await self.set_user_primary_organizational_unit_with_options_async(instance_id, application_id, user_id, request, headers, runtime)

    def update_user_password_with_options(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        request: eiam_developerapi_20220225_models.UpdateUserPasswordRequest,
        headers: eiam_developerapi_20220225_models.UpdateUserPasswordHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.UpdateUserPasswordResponse:
        """
        @summary 更新账户密码
        
        @param request: UpdateUserPasswordRequest
        @param headers: UpdateUserPasswordHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUserPasswordResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.password):
            body['password'] = request.password
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateUserPassword',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/users/{OpenApiUtilClient.get_encode_param(user_id)}/actions/updateUserPassword',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.UpdateUserPasswordResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def update_user_password_with_options_async(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        request: eiam_developerapi_20220225_models.UpdateUserPasswordRequest,
        headers: eiam_developerapi_20220225_models.UpdateUserPasswordHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_developerapi_20220225_models.UpdateUserPasswordResponse:
        """
        @summary 更新账户密码
        
        @param request: UpdateUserPasswordRequest
        @param headers: UpdateUserPasswordHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUserPasswordResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.password):
            body['password'] = request.password
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.authorization):
            real_headers['Authorization'] = UtilClient.to_jsonstring(headers.authorization)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateUserPassword',
            version='2022-02-25',
            protocol='HTTPS',
            pathname=f'/v2/{OpenApiUtilClient.get_encode_param(instance_id)}/{OpenApiUtilClient.get_encode_param(application_id)}/users/{OpenApiUtilClient.get_encode_param(user_id)}/actions/updateUserPassword',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='none'
        )
        return TeaCore.from_map(
            eiam_developerapi_20220225_models.UpdateUserPasswordResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def update_user_password(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        request: eiam_developerapi_20220225_models.UpdateUserPasswordRequest,
    ) -> eiam_developerapi_20220225_models.UpdateUserPasswordResponse:
        """
        @summary 更新账户密码
        
        @param request: UpdateUserPasswordRequest
        @return: UpdateUserPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.UpdateUserPasswordHeaders()
        return self.update_user_password_with_options(instance_id, application_id, user_id, request, headers, runtime)

    async def update_user_password_async(
        self,
        instance_id: str,
        application_id: str,
        user_id: str,
        request: eiam_developerapi_20220225_models.UpdateUserPasswordRequest,
    ) -> eiam_developerapi_20220225_models.UpdateUserPasswordResponse:
        """
        @summary 更新账户密码
        
        @param request: UpdateUserPasswordRequest
        @return: UpdateUserPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = eiam_developerapi_20220225_models.UpdateUserPasswordHeaders()
        return await self.update_user_password_with_options_async(instance_id, application_id, user_id, request, headers, runtime)
