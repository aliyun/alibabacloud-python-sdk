# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_eiam20211201 import models as eiam_20211201_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_application_account_to_user_with_options(
        self,
        request: eiam_20211201_models.AddApplicationAccountToUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.AddApplicationAccountToUserResponse:
        """
        @summary 在当前应用下给指定员工添加一个应用账号
        
        @param request: AddApplicationAccountToUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddApplicationAccountToUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.application_username):
            query['ApplicationUsername'] = request.application_username
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddApplicationAccountToUser',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.AddApplicationAccountToUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_application_account_to_user_with_options_async(
        self,
        request: eiam_20211201_models.AddApplicationAccountToUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.AddApplicationAccountToUserResponse:
        """
        @summary 在当前应用下给指定员工添加一个应用账号
        
        @param request: AddApplicationAccountToUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddApplicationAccountToUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.application_username):
            query['ApplicationUsername'] = request.application_username
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddApplicationAccountToUser',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.AddApplicationAccountToUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_application_account_to_user(
        self,
        request: eiam_20211201_models.AddApplicationAccountToUserRequest,
    ) -> eiam_20211201_models.AddApplicationAccountToUserResponse:
        """
        @summary 在当前应用下给指定员工添加一个应用账号
        
        @param request: AddApplicationAccountToUserRequest
        @return: AddApplicationAccountToUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_application_account_to_user_with_options(request, runtime)

    async def add_application_account_to_user_async(
        self,
        request: eiam_20211201_models.AddApplicationAccountToUserRequest,
    ) -> eiam_20211201_models.AddApplicationAccountToUserResponse:
        """
        @summary 在当前应用下给指定员工添加一个应用账号
        
        @param request: AddApplicationAccountToUserRequest
        @return: AddApplicationAccountToUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_application_account_to_user_with_options_async(request, runtime)

    def add_custom_privacy_policies_to_brand_with_options(
        self,
        request: eiam_20211201_models.AddCustomPrivacyPoliciesToBrandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.AddCustomPrivacyPoliciesToBrandResponse:
        """
        @summary 添加条款到品牌
        
        @param request: AddCustomPrivacyPoliciesToBrandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddCustomPrivacyPoliciesToBrandResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.brand_id):
            query['BrandId'] = request.brand_id
        if not UtilClient.is_unset(request.custom_privacy_policy_ids):
            query['CustomPrivacyPolicyIds'] = request.custom_privacy_policy_ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddCustomPrivacyPoliciesToBrand',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.AddCustomPrivacyPoliciesToBrandResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_custom_privacy_policies_to_brand_with_options_async(
        self,
        request: eiam_20211201_models.AddCustomPrivacyPoliciesToBrandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.AddCustomPrivacyPoliciesToBrandResponse:
        """
        @summary 添加条款到品牌
        
        @param request: AddCustomPrivacyPoliciesToBrandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddCustomPrivacyPoliciesToBrandResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.brand_id):
            query['BrandId'] = request.brand_id
        if not UtilClient.is_unset(request.custom_privacy_policy_ids):
            query['CustomPrivacyPolicyIds'] = request.custom_privacy_policy_ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddCustomPrivacyPoliciesToBrand',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.AddCustomPrivacyPoliciesToBrandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_custom_privacy_policies_to_brand(
        self,
        request: eiam_20211201_models.AddCustomPrivacyPoliciesToBrandRequest,
    ) -> eiam_20211201_models.AddCustomPrivacyPoliciesToBrandResponse:
        """
        @summary 添加条款到品牌
        
        @param request: AddCustomPrivacyPoliciesToBrandRequest
        @return: AddCustomPrivacyPoliciesToBrandResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_custom_privacy_policies_to_brand_with_options(request, runtime)

    async def add_custom_privacy_policies_to_brand_async(
        self,
        request: eiam_20211201_models.AddCustomPrivacyPoliciesToBrandRequest,
    ) -> eiam_20211201_models.AddCustomPrivacyPoliciesToBrandResponse:
        """
        @summary 添加条款到品牌
        
        @param request: AddCustomPrivacyPoliciesToBrandRequest
        @return: AddCustomPrivacyPoliciesToBrandResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_custom_privacy_policies_to_brand_with_options_async(request, runtime)

    def add_user_to_organizational_units_with_options(
        self,
        request: eiam_20211201_models.AddUserToOrganizationalUnitsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.AddUserToOrganizationalUnitsResponse:
        """
        @summary Adds an Employee Identity and Access Management (EIAM) account to multiple EIAM organizations of Identity as a Service (IDaaS). If the account already exists in the organizational unit, the system directly returns a success response.
        
        @param request: AddUserToOrganizationalUnitsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddUserToOrganizationalUnitsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.organizational_unit_ids):
            query['OrganizationalUnitIds'] = request.organizational_unit_ids
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddUserToOrganizationalUnits',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.AddUserToOrganizationalUnitsResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_user_to_organizational_units_with_options_async(
        self,
        request: eiam_20211201_models.AddUserToOrganizationalUnitsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.AddUserToOrganizationalUnitsResponse:
        """
        @summary Adds an Employee Identity and Access Management (EIAM) account to multiple EIAM organizations of Identity as a Service (IDaaS). If the account already exists in the organizational unit, the system directly returns a success response.
        
        @param request: AddUserToOrganizationalUnitsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddUserToOrganizationalUnitsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.organizational_unit_ids):
            query['OrganizationalUnitIds'] = request.organizational_unit_ids
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddUserToOrganizationalUnits',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.AddUserToOrganizationalUnitsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_user_to_organizational_units(
        self,
        request: eiam_20211201_models.AddUserToOrganizationalUnitsRequest,
    ) -> eiam_20211201_models.AddUserToOrganizationalUnitsResponse:
        """
        @summary Adds an Employee Identity and Access Management (EIAM) account to multiple EIAM organizations of Identity as a Service (IDaaS). If the account already exists in the organizational unit, the system directly returns a success response.
        
        @param request: AddUserToOrganizationalUnitsRequest
        @return: AddUserToOrganizationalUnitsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_user_to_organizational_units_with_options(request, runtime)

    async def add_user_to_organizational_units_async(
        self,
        request: eiam_20211201_models.AddUserToOrganizationalUnitsRequest,
    ) -> eiam_20211201_models.AddUserToOrganizationalUnitsResponse:
        """
        @summary Adds an Employee Identity and Access Management (EIAM) account to multiple EIAM organizations of Identity as a Service (IDaaS). If the account already exists in the organizational unit, the system directly returns a success response.
        
        @param request: AddUserToOrganizationalUnitsRequest
        @return: AddUserToOrganizationalUnitsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_user_to_organizational_units_with_options_async(request, runtime)

    def add_users_to_group_with_options(
        self,
        request: eiam_20211201_models.AddUsersToGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.AddUsersToGroupResponse:
        """
        @summary Adds Employee Identity and Access Management (EIAM) accounts to an EIAM group of Identity as a Service (IDaaS).
        
        @param request: AddUsersToGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddUsersToGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddUsersToGroup',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.AddUsersToGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_users_to_group_with_options_async(
        self,
        request: eiam_20211201_models.AddUsersToGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.AddUsersToGroupResponse:
        """
        @summary Adds Employee Identity and Access Management (EIAM) accounts to an EIAM group of Identity as a Service (IDaaS).
        
        @param request: AddUsersToGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddUsersToGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddUsersToGroup',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.AddUsersToGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_users_to_group(
        self,
        request: eiam_20211201_models.AddUsersToGroupRequest,
    ) -> eiam_20211201_models.AddUsersToGroupResponse:
        """
        @summary Adds Employee Identity and Access Management (EIAM) accounts to an EIAM group of Identity as a Service (IDaaS).
        
        @param request: AddUsersToGroupRequest
        @return: AddUsersToGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_users_to_group_with_options(request, runtime)

    async def add_users_to_group_async(
        self,
        request: eiam_20211201_models.AddUsersToGroupRequest,
    ) -> eiam_20211201_models.AddUsersToGroupResponse:
        """
        @summary Adds Employee Identity and Access Management (EIAM) accounts to an EIAM group of Identity as a Service (IDaaS).
        
        @param request: AddUsersToGroupRequest
        @return: AddUsersToGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_users_to_group_with_options_async(request, runtime)

    def authorize_application_to_groups_with_options(
        self,
        request: eiam_20211201_models.AuthorizeApplicationToGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.AuthorizeApplicationToGroupsResponse:
        """
        @summary Grants the permissions to access an application to multiple account groups at a time in Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM).
        
        @param request: AuthorizeApplicationToGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AuthorizeApplicationToGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AuthorizeApplicationToGroups',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.AuthorizeApplicationToGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def authorize_application_to_groups_with_options_async(
        self,
        request: eiam_20211201_models.AuthorizeApplicationToGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.AuthorizeApplicationToGroupsResponse:
        """
        @summary Grants the permissions to access an application to multiple account groups at a time in Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM).
        
        @param request: AuthorizeApplicationToGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AuthorizeApplicationToGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AuthorizeApplicationToGroups',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.AuthorizeApplicationToGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def authorize_application_to_groups(
        self,
        request: eiam_20211201_models.AuthorizeApplicationToGroupsRequest,
    ) -> eiam_20211201_models.AuthorizeApplicationToGroupsResponse:
        """
        @summary Grants the permissions to access an application to multiple account groups at a time in Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM).
        
        @param request: AuthorizeApplicationToGroupsRequest
        @return: AuthorizeApplicationToGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.authorize_application_to_groups_with_options(request, runtime)

    async def authorize_application_to_groups_async(
        self,
        request: eiam_20211201_models.AuthorizeApplicationToGroupsRequest,
    ) -> eiam_20211201_models.AuthorizeApplicationToGroupsResponse:
        """
        @summary Grants the permissions to access an application to multiple account groups at a time in Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM).
        
        @param request: AuthorizeApplicationToGroupsRequest
        @return: AuthorizeApplicationToGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.authorize_application_to_groups_with_options_async(request, runtime)

    def authorize_application_to_organizational_units_with_options(
        self,
        request: eiam_20211201_models.AuthorizeApplicationToOrganizationalUnitsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.AuthorizeApplicationToOrganizationalUnitsResponse:
        """
        @summary Grants the access permissions on an application to multiple Employee Identity and Access Management (EIAM) organizations at a time.
        
        @param request: AuthorizeApplicationToOrganizationalUnitsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AuthorizeApplicationToOrganizationalUnitsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.organizational_unit_ids):
            query['OrganizationalUnitIds'] = request.organizational_unit_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AuthorizeApplicationToOrganizationalUnits',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.AuthorizeApplicationToOrganizationalUnitsResponse(),
            self.call_api(params, req, runtime)
        )

    async def authorize_application_to_organizational_units_with_options_async(
        self,
        request: eiam_20211201_models.AuthorizeApplicationToOrganizationalUnitsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.AuthorizeApplicationToOrganizationalUnitsResponse:
        """
        @summary Grants the access permissions on an application to multiple Employee Identity and Access Management (EIAM) organizations at a time.
        
        @param request: AuthorizeApplicationToOrganizationalUnitsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AuthorizeApplicationToOrganizationalUnitsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.organizational_unit_ids):
            query['OrganizationalUnitIds'] = request.organizational_unit_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AuthorizeApplicationToOrganizationalUnits',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.AuthorizeApplicationToOrganizationalUnitsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def authorize_application_to_organizational_units(
        self,
        request: eiam_20211201_models.AuthorizeApplicationToOrganizationalUnitsRequest,
    ) -> eiam_20211201_models.AuthorizeApplicationToOrganizationalUnitsResponse:
        """
        @summary Grants the access permissions on an application to multiple Employee Identity and Access Management (EIAM) organizations at a time.
        
        @param request: AuthorizeApplicationToOrganizationalUnitsRequest
        @return: AuthorizeApplicationToOrganizationalUnitsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.authorize_application_to_organizational_units_with_options(request, runtime)

    async def authorize_application_to_organizational_units_async(
        self,
        request: eiam_20211201_models.AuthorizeApplicationToOrganizationalUnitsRequest,
    ) -> eiam_20211201_models.AuthorizeApplicationToOrganizationalUnitsResponse:
        """
        @summary Grants the access permissions on an application to multiple Employee Identity and Access Management (EIAM) organizations at a time.
        
        @param request: AuthorizeApplicationToOrganizationalUnitsRequest
        @return: AuthorizeApplicationToOrganizationalUnitsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.authorize_application_to_organizational_units_with_options_async(request, runtime)

    def authorize_application_to_users_with_options(
        self,
        request: eiam_20211201_models.AuthorizeApplicationToUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.AuthorizeApplicationToUsersResponse:
        """
        @summary Grants the access permissions on an application to multiple Employee Identity and Access Management (EIAM) accounts at a time.
        
        @param request: AuthorizeApplicationToUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AuthorizeApplicationToUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AuthorizeApplicationToUsers',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.AuthorizeApplicationToUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def authorize_application_to_users_with_options_async(
        self,
        request: eiam_20211201_models.AuthorizeApplicationToUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.AuthorizeApplicationToUsersResponse:
        """
        @summary Grants the access permissions on an application to multiple Employee Identity and Access Management (EIAM) accounts at a time.
        
        @param request: AuthorizeApplicationToUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AuthorizeApplicationToUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AuthorizeApplicationToUsers',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.AuthorizeApplicationToUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def authorize_application_to_users(
        self,
        request: eiam_20211201_models.AuthorizeApplicationToUsersRequest,
    ) -> eiam_20211201_models.AuthorizeApplicationToUsersResponse:
        """
        @summary Grants the access permissions on an application to multiple Employee Identity and Access Management (EIAM) accounts at a time.
        
        @param request: AuthorizeApplicationToUsersRequest
        @return: AuthorizeApplicationToUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.authorize_application_to_users_with_options(request, runtime)

    async def authorize_application_to_users_async(
        self,
        request: eiam_20211201_models.AuthorizeApplicationToUsersRequest,
    ) -> eiam_20211201_models.AuthorizeApplicationToUsersResponse:
        """
        @summary Grants the access permissions on an application to multiple Employee Identity and Access Management (EIAM) accounts at a time.
        
        @param request: AuthorizeApplicationToUsersRequest
        @return: AuthorizeApplicationToUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.authorize_application_to_users_with_options_async(request, runtime)

    def bind_user_authn_source_mapping_with_options(
        self,
        request: eiam_20211201_models.BindUserAuthnSourceMappingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.BindUserAuthnSourceMappingResponse:
        """
        @summary 绑定三方登录账户
        
        @param request: BindUserAuthnSourceMappingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindUserAuthnSourceMappingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identity_provider_id):
            query['IdentityProviderId'] = request.identity_provider_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_external_id):
            query['UserExternalId'] = request.user_external_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindUserAuthnSourceMapping',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.BindUserAuthnSourceMappingResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_user_authn_source_mapping_with_options_async(
        self,
        request: eiam_20211201_models.BindUserAuthnSourceMappingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.BindUserAuthnSourceMappingResponse:
        """
        @summary 绑定三方登录账户
        
        @param request: BindUserAuthnSourceMappingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindUserAuthnSourceMappingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identity_provider_id):
            query['IdentityProviderId'] = request.identity_provider_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_external_id):
            query['UserExternalId'] = request.user_external_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindUserAuthnSourceMapping',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.BindUserAuthnSourceMappingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_user_authn_source_mapping(
        self,
        request: eiam_20211201_models.BindUserAuthnSourceMappingRequest,
    ) -> eiam_20211201_models.BindUserAuthnSourceMappingResponse:
        """
        @summary 绑定三方登录账户
        
        @param request: BindUserAuthnSourceMappingRequest
        @return: BindUserAuthnSourceMappingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.bind_user_authn_source_mapping_with_options(request, runtime)

    async def bind_user_authn_source_mapping_async(
        self,
        request: eiam_20211201_models.BindUserAuthnSourceMappingRequest,
    ) -> eiam_20211201_models.BindUserAuthnSourceMappingResponse:
        """
        @summary 绑定三方登录账户
        
        @param request: BindUserAuthnSourceMappingRequest
        @return: BindUserAuthnSourceMappingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.bind_user_authn_source_mapping_with_options_async(request, runtime)

    def create_application_with_options(
        self,
        request: eiam_20211201_models.CreateApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.CreateApplicationResponse:
        """
        @summary Adds an application to an Enterprise Identity Access Management (EIAM) instance of Identity as a Service (IDaaS).
        
        @description IDaaS EIAM supports the following two standard single sign-on (SSO) protocols for adding applications: SAML 2.0 and OIDC. You can select an SSO protocol based on your business requirements when you add an application. You cannot change the SSO protocol that you selected after the application is added.
        
        @param request: CreateApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_name):
            query['ApplicationName'] = request.application_name
        if not UtilClient.is_unset(request.application_source_type):
            query['ApplicationSourceType'] = request.application_source_type
        if not UtilClient.is_unset(request.application_template_id):
            query['ApplicationTemplateId'] = request.application_template_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.logo_url):
            query['LogoUrl'] = request.logo_url
        if not UtilClient.is_unset(request.sso_type):
            query['SsoType'] = request.sso_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApplication',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.CreateApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_application_with_options_async(
        self,
        request: eiam_20211201_models.CreateApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.CreateApplicationResponse:
        """
        @summary Adds an application to an Enterprise Identity Access Management (EIAM) instance of Identity as a Service (IDaaS).
        
        @description IDaaS EIAM supports the following two standard single sign-on (SSO) protocols for adding applications: SAML 2.0 and OIDC. You can select an SSO protocol based on your business requirements when you add an application. You cannot change the SSO protocol that you selected after the application is added.
        
        @param request: CreateApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_name):
            query['ApplicationName'] = request.application_name
        if not UtilClient.is_unset(request.application_source_type):
            query['ApplicationSourceType'] = request.application_source_type
        if not UtilClient.is_unset(request.application_template_id):
            query['ApplicationTemplateId'] = request.application_template_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.logo_url):
            query['LogoUrl'] = request.logo_url
        if not UtilClient.is_unset(request.sso_type):
            query['SsoType'] = request.sso_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApplication',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.CreateApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_application(
        self,
        request: eiam_20211201_models.CreateApplicationRequest,
    ) -> eiam_20211201_models.CreateApplicationResponse:
        """
        @summary Adds an application to an Enterprise Identity Access Management (EIAM) instance of Identity as a Service (IDaaS).
        
        @description IDaaS EIAM supports the following two standard single sign-on (SSO) protocols for adding applications: SAML 2.0 and OIDC. You can select an SSO protocol based on your business requirements when you add an application. You cannot change the SSO protocol that you selected after the application is added.
        
        @param request: CreateApplicationRequest
        @return: CreateApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_application_with_options(request, runtime)

    async def create_application_async(
        self,
        request: eiam_20211201_models.CreateApplicationRequest,
    ) -> eiam_20211201_models.CreateApplicationResponse:
        """
        @summary Adds an application to an Enterprise Identity Access Management (EIAM) instance of Identity as a Service (IDaaS).
        
        @description IDaaS EIAM supports the following two standard single sign-on (SSO) protocols for adding applications: SAML 2.0 and OIDC. You can select an SSO protocol based on your business requirements when you add an application. You cannot change the SSO protocol that you selected after the application is added.
        
        @param request: CreateApplicationRequest
        @return: CreateApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_application_with_options_async(request, runtime)

    def create_application_client_secret_with_options(
        self,
        request: eiam_20211201_models.CreateApplicationClientSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.CreateApplicationClientSecretResponse:
        """
        @summary Creates a client key for an Employee Identity and Access Management (EIAM) application. An EIAM application can have up to two client keys.
        
        @param request: CreateApplicationClientSecretRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateApplicationClientSecretResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.expiration_time):
            query['ExpirationTime'] = request.expiration_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApplicationClientSecret',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.CreateApplicationClientSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_application_client_secret_with_options_async(
        self,
        request: eiam_20211201_models.CreateApplicationClientSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.CreateApplicationClientSecretResponse:
        """
        @summary Creates a client key for an Employee Identity and Access Management (EIAM) application. An EIAM application can have up to two client keys.
        
        @param request: CreateApplicationClientSecretRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateApplicationClientSecretResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.expiration_time):
            query['ExpirationTime'] = request.expiration_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApplicationClientSecret',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.CreateApplicationClientSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_application_client_secret(
        self,
        request: eiam_20211201_models.CreateApplicationClientSecretRequest,
    ) -> eiam_20211201_models.CreateApplicationClientSecretResponse:
        """
        @summary Creates a client key for an Employee Identity and Access Management (EIAM) application. An EIAM application can have up to two client keys.
        
        @param request: CreateApplicationClientSecretRequest
        @return: CreateApplicationClientSecretResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_application_client_secret_with_options(request, runtime)

    async def create_application_client_secret_async(
        self,
        request: eiam_20211201_models.CreateApplicationClientSecretRequest,
    ) -> eiam_20211201_models.CreateApplicationClientSecretResponse:
        """
        @summary Creates a client key for an Employee Identity and Access Management (EIAM) application. An EIAM application can have up to two client keys.
        
        @param request: CreateApplicationClientSecretRequest
        @return: CreateApplicationClientSecretResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_application_client_secret_with_options_async(request, runtime)

    def create_application_federated_credential_with_options(
        self,
        request: eiam_20211201_models.CreateApplicationFederatedCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.CreateApplicationFederatedCredentialResponse:
        """
        @summary 创建应用联邦凭证
        
        @param request: CreateApplicationFederatedCredentialRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateApplicationFederatedCredentialResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_federated_credential_name):
            query['ApplicationFederatedCredentialName'] = request.application_federated_credential_name
        if not UtilClient.is_unset(request.application_federated_credential_type):
            query['ApplicationFederatedCredentialType'] = request.application_federated_credential_type
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.attribute_mappings):
            query['AttributeMappings'] = request.attribute_mappings
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.federated_credential_provider_id):
            query['FederatedCredentialProviderId'] = request.federated_credential_provider_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.verification_condition):
            query['VerificationCondition'] = request.verification_condition
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApplicationFederatedCredential',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.CreateApplicationFederatedCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_application_federated_credential_with_options_async(
        self,
        request: eiam_20211201_models.CreateApplicationFederatedCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.CreateApplicationFederatedCredentialResponse:
        """
        @summary 创建应用联邦凭证
        
        @param request: CreateApplicationFederatedCredentialRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateApplicationFederatedCredentialResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_federated_credential_name):
            query['ApplicationFederatedCredentialName'] = request.application_federated_credential_name
        if not UtilClient.is_unset(request.application_federated_credential_type):
            query['ApplicationFederatedCredentialType'] = request.application_federated_credential_type
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.attribute_mappings):
            query['AttributeMappings'] = request.attribute_mappings
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.federated_credential_provider_id):
            query['FederatedCredentialProviderId'] = request.federated_credential_provider_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.verification_condition):
            query['VerificationCondition'] = request.verification_condition
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApplicationFederatedCredential',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.CreateApplicationFederatedCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_application_federated_credential(
        self,
        request: eiam_20211201_models.CreateApplicationFederatedCredentialRequest,
    ) -> eiam_20211201_models.CreateApplicationFederatedCredentialResponse:
        """
        @summary 创建应用联邦凭证
        
        @param request: CreateApplicationFederatedCredentialRequest
        @return: CreateApplicationFederatedCredentialResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_application_federated_credential_with_options(request, runtime)

    async def create_application_federated_credential_async(
        self,
        request: eiam_20211201_models.CreateApplicationFederatedCredentialRequest,
    ) -> eiam_20211201_models.CreateApplicationFederatedCredentialResponse:
        """
        @summary 创建应用联邦凭证
        
        @param request: CreateApplicationFederatedCredentialRequest
        @return: CreateApplicationFederatedCredentialResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_application_federated_credential_with_options_async(request, runtime)

    def create_application_token_with_options(
        self,
        request: eiam_20211201_models.CreateApplicationTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.CreateApplicationTokenResponse:
        """
        @summary 创建应用Token
        
        @param request: CreateApplicationTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateApplicationTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.application_token_type):
            query['ApplicationTokenType'] = request.application_token_type
        if not UtilClient.is_unset(request.expiration_time):
            query['ExpirationTime'] = request.expiration_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApplicationToken',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.CreateApplicationTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_application_token_with_options_async(
        self,
        request: eiam_20211201_models.CreateApplicationTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.CreateApplicationTokenResponse:
        """
        @summary 创建应用Token
        
        @param request: CreateApplicationTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateApplicationTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.application_token_type):
            query['ApplicationTokenType'] = request.application_token_type
        if not UtilClient.is_unset(request.expiration_time):
            query['ExpirationTime'] = request.expiration_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApplicationToken',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.CreateApplicationTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_application_token(
        self,
        request: eiam_20211201_models.CreateApplicationTokenRequest,
    ) -> eiam_20211201_models.CreateApplicationTokenResponse:
        """
        @summary 创建应用Token
        
        @param request: CreateApplicationTokenRequest
        @return: CreateApplicationTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_application_token_with_options(request, runtime)

    async def create_application_token_async(
        self,
        request: eiam_20211201_models.CreateApplicationTokenRequest,
    ) -> eiam_20211201_models.CreateApplicationTokenResponse:
        """
        @summary 创建应用Token
        
        @param request: CreateApplicationTokenRequest
        @return: CreateApplicationTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_application_token_with_options_async(request, runtime)

    def create_brand_with_options(
        self,
        request: eiam_20211201_models.CreateBrandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.CreateBrandResponse:
        """
        @summary 创建品牌
        
        @param request: CreateBrandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBrandResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.brand_name):
            query['BrandName'] = request.brand_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBrand',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.CreateBrandResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_brand_with_options_async(
        self,
        request: eiam_20211201_models.CreateBrandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.CreateBrandResponse:
        """
        @summary 创建品牌
        
        @param request: CreateBrandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBrandResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.brand_name):
            query['BrandName'] = request.brand_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBrand',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.CreateBrandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_brand(
        self,
        request: eiam_20211201_models.CreateBrandRequest,
    ) -> eiam_20211201_models.CreateBrandResponse:
        """
        @summary 创建品牌
        
        @param request: CreateBrandRequest
        @return: CreateBrandResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_brand_with_options(request, runtime)

    async def create_brand_async(
        self,
        request: eiam_20211201_models.CreateBrandRequest,
    ) -> eiam_20211201_models.CreateBrandResponse:
        """
        @summary 创建品牌
        
        @param request: CreateBrandRequest
        @return: CreateBrandResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_brand_with_options_async(request, runtime)

    def create_conditional_access_policy_with_options(
        self,
        request: eiam_20211201_models.CreateConditionalAccessPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.CreateConditionalAccessPolicyResponse:
        """
        @summary Create Conditional Access Policy
        
        @description Create Conditional Access Policy
        
        @param request: CreateConditionalAccessPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateConditionalAccessPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.conditional_access_policy_name):
            query['ConditionalAccessPolicyName'] = request.conditional_access_policy_name
        if not UtilClient.is_unset(request.conditional_access_policy_type):
            query['ConditionalAccessPolicyType'] = request.conditional_access_policy_type
        if not UtilClient.is_unset(request.conditions_config):
            query['ConditionsConfig'] = request.conditions_config
        if not UtilClient.is_unset(request.decision_config):
            query['DecisionConfig'] = request.decision_config
        if not UtilClient.is_unset(request.decision_type):
            query['DecisionType'] = request.decision_type
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.evaluate_at):
            query['EvaluateAt'] = request.evaluate_at
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateConditionalAccessPolicy',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.CreateConditionalAccessPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_conditional_access_policy_with_options_async(
        self,
        request: eiam_20211201_models.CreateConditionalAccessPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.CreateConditionalAccessPolicyResponse:
        """
        @summary Create Conditional Access Policy
        
        @description Create Conditional Access Policy
        
        @param request: CreateConditionalAccessPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateConditionalAccessPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.conditional_access_policy_name):
            query['ConditionalAccessPolicyName'] = request.conditional_access_policy_name
        if not UtilClient.is_unset(request.conditional_access_policy_type):
            query['ConditionalAccessPolicyType'] = request.conditional_access_policy_type
        if not UtilClient.is_unset(request.conditions_config):
            query['ConditionsConfig'] = request.conditions_config
        if not UtilClient.is_unset(request.decision_config):
            query['DecisionConfig'] = request.decision_config
        if not UtilClient.is_unset(request.decision_type):
            query['DecisionType'] = request.decision_type
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.evaluate_at):
            query['EvaluateAt'] = request.evaluate_at
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateConditionalAccessPolicy',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.CreateConditionalAccessPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_conditional_access_policy(
        self,
        request: eiam_20211201_models.CreateConditionalAccessPolicyRequest,
    ) -> eiam_20211201_models.CreateConditionalAccessPolicyResponse:
        """
        @summary Create Conditional Access Policy
        
        @description Create Conditional Access Policy
        
        @param request: CreateConditionalAccessPolicyRequest
        @return: CreateConditionalAccessPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_conditional_access_policy_with_options(request, runtime)

    async def create_conditional_access_policy_async(
        self,
        request: eiam_20211201_models.CreateConditionalAccessPolicyRequest,
    ) -> eiam_20211201_models.CreateConditionalAccessPolicyResponse:
        """
        @summary Create Conditional Access Policy
        
        @description Create Conditional Access Policy
        
        @param request: CreateConditionalAccessPolicyRequest
        @return: CreateConditionalAccessPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_conditional_access_policy_with_options_async(request, runtime)

    def create_custom_privacy_policy_with_options(
        self,
        request: eiam_20211201_models.CreateCustomPrivacyPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.CreateCustomPrivacyPolicyResponse:
        """
        @summary 创建自定义条款
        
        @param request: CreateCustomPrivacyPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCustomPrivacyPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.custom_privacy_policy_contents):
            query['CustomPrivacyPolicyContents'] = request.custom_privacy_policy_contents
        if not UtilClient.is_unset(request.custom_privacy_policy_name):
            query['CustomPrivacyPolicyName'] = request.custom_privacy_policy_name
        if not UtilClient.is_unset(request.default_language_code):
            query['DefaultLanguageCode'] = request.default_language_code
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.user_consent_type):
            query['UserConsentType'] = request.user_consent_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCustomPrivacyPolicy',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.CreateCustomPrivacyPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_custom_privacy_policy_with_options_async(
        self,
        request: eiam_20211201_models.CreateCustomPrivacyPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.CreateCustomPrivacyPolicyResponse:
        """
        @summary 创建自定义条款
        
        @param request: CreateCustomPrivacyPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCustomPrivacyPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.custom_privacy_policy_contents):
            query['CustomPrivacyPolicyContents'] = request.custom_privacy_policy_contents
        if not UtilClient.is_unset(request.custom_privacy_policy_name):
            query['CustomPrivacyPolicyName'] = request.custom_privacy_policy_name
        if not UtilClient.is_unset(request.default_language_code):
            query['DefaultLanguageCode'] = request.default_language_code
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.user_consent_type):
            query['UserConsentType'] = request.user_consent_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCustomPrivacyPolicy',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.CreateCustomPrivacyPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_custom_privacy_policy(
        self,
        request: eiam_20211201_models.CreateCustomPrivacyPolicyRequest,
    ) -> eiam_20211201_models.CreateCustomPrivacyPolicyResponse:
        """
        @summary 创建自定义条款
        
        @param request: CreateCustomPrivacyPolicyRequest
        @return: CreateCustomPrivacyPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_custom_privacy_policy_with_options(request, runtime)

    async def create_custom_privacy_policy_async(
        self,
        request: eiam_20211201_models.CreateCustomPrivacyPolicyRequest,
    ) -> eiam_20211201_models.CreateCustomPrivacyPolicyResponse:
        """
        @summary 创建自定义条款
        
        @param request: CreateCustomPrivacyPolicyRequest
        @return: CreateCustomPrivacyPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_custom_privacy_policy_with_options_async(request, runtime)

    def create_domain_with_options(
        self,
        request: eiam_20211201_models.CreateDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.CreateDomainResponse:
        """
        @summary Creates a custom domain name for an Employee Identity and Access Management (EIAM) instance.
        
        @param request: CreateDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.filing):
            query['Filing'] = request.filing
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDomain',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.CreateDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_domain_with_options_async(
        self,
        request: eiam_20211201_models.CreateDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.CreateDomainResponse:
        """
        @summary Creates a custom domain name for an Employee Identity and Access Management (EIAM) instance.
        
        @param request: CreateDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.filing):
            query['Filing'] = request.filing
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDomain',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.CreateDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_domain(
        self,
        request: eiam_20211201_models.CreateDomainRequest,
    ) -> eiam_20211201_models.CreateDomainResponse:
        """
        @summary Creates a custom domain name for an Employee Identity and Access Management (EIAM) instance.
        
        @param request: CreateDomainRequest
        @return: CreateDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_domain_with_options(request, runtime)

    async def create_domain_async(
        self,
        request: eiam_20211201_models.CreateDomainRequest,
    ) -> eiam_20211201_models.CreateDomainResponse:
        """
        @summary Creates a custom domain name for an Employee Identity and Access Management (EIAM) instance.
        
        @param request: CreateDomainRequest
        @return: CreateDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_domain_with_options_async(request, runtime)

    def create_domain_proxy_token_with_options(
        self,
        request: eiam_20211201_models.CreateDomainProxyTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.CreateDomainProxyTokenResponse:
        """
        @summary Creates a proxy token for a domain name of an Employee Identity and Access Management (EIAM) instance.
        
        @param request: CreateDomainProxyTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDomainProxyTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDomainProxyToken',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.CreateDomainProxyTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_domain_proxy_token_with_options_async(
        self,
        request: eiam_20211201_models.CreateDomainProxyTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.CreateDomainProxyTokenResponse:
        """
        @summary Creates a proxy token for a domain name of an Employee Identity and Access Management (EIAM) instance.
        
        @param request: CreateDomainProxyTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDomainProxyTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDomainProxyToken',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.CreateDomainProxyTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_domain_proxy_token(
        self,
        request: eiam_20211201_models.CreateDomainProxyTokenRequest,
    ) -> eiam_20211201_models.CreateDomainProxyTokenResponse:
        """
        @summary Creates a proxy token for a domain name of an Employee Identity and Access Management (EIAM) instance.
        
        @param request: CreateDomainProxyTokenRequest
        @return: CreateDomainProxyTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_domain_proxy_token_with_options(request, runtime)

    async def create_domain_proxy_token_async(
        self,
        request: eiam_20211201_models.CreateDomainProxyTokenRequest,
    ) -> eiam_20211201_models.CreateDomainProxyTokenResponse:
        """
        @summary Creates a proxy token for a domain name of an Employee Identity and Access Management (EIAM) instance.
        
        @param request: CreateDomainProxyTokenRequest
        @return: CreateDomainProxyTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_domain_proxy_token_with_options_async(request, runtime)

    def create_federated_credential_provider_with_options(
        self,
        request: eiam_20211201_models.CreateFederatedCredentialProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.CreateFederatedCredentialProviderResponse:
        """
        @summary 创建联邦凭证提供方
        
        @param request: CreateFederatedCredentialProviderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFederatedCredentialProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.federated_credential_provider_name):
            query['FederatedCredentialProviderName'] = request.federated_credential_provider_name
        if not UtilClient.is_unset(request.federated_credential_provider_type):
            query['FederatedCredentialProviderType'] = request.federated_credential_provider_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_access_endpoint_id):
            query['NetworkAccessEndpointId'] = request.network_access_endpoint_id
        if not UtilClient.is_unset(request.oidc_provider_config):
            query['OidcProviderConfig'] = request.oidc_provider_config
        if not UtilClient.is_unset(request.pkcs_7provider_config):
            query['Pkcs7ProviderConfig'] = request.pkcs_7provider_config
        if not UtilClient.is_unset(request.private_ca_provider_config):
            query['PrivateCaProviderConfig'] = request.private_ca_provider_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFederatedCredentialProvider',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.CreateFederatedCredentialProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_federated_credential_provider_with_options_async(
        self,
        request: eiam_20211201_models.CreateFederatedCredentialProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.CreateFederatedCredentialProviderResponse:
        """
        @summary 创建联邦凭证提供方
        
        @param request: CreateFederatedCredentialProviderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFederatedCredentialProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.federated_credential_provider_name):
            query['FederatedCredentialProviderName'] = request.federated_credential_provider_name
        if not UtilClient.is_unset(request.federated_credential_provider_type):
            query['FederatedCredentialProviderType'] = request.federated_credential_provider_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_access_endpoint_id):
            query['NetworkAccessEndpointId'] = request.network_access_endpoint_id
        if not UtilClient.is_unset(request.oidc_provider_config):
            query['OidcProviderConfig'] = request.oidc_provider_config
        if not UtilClient.is_unset(request.pkcs_7provider_config):
            query['Pkcs7ProviderConfig'] = request.pkcs_7provider_config
        if not UtilClient.is_unset(request.private_ca_provider_config):
            query['PrivateCaProviderConfig'] = request.private_ca_provider_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFederatedCredentialProvider',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.CreateFederatedCredentialProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_federated_credential_provider(
        self,
        request: eiam_20211201_models.CreateFederatedCredentialProviderRequest,
    ) -> eiam_20211201_models.CreateFederatedCredentialProviderResponse:
        """
        @summary 创建联邦凭证提供方
        
        @param request: CreateFederatedCredentialProviderRequest
        @return: CreateFederatedCredentialProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_federated_credential_provider_with_options(request, runtime)

    async def create_federated_credential_provider_async(
        self,
        request: eiam_20211201_models.CreateFederatedCredentialProviderRequest,
    ) -> eiam_20211201_models.CreateFederatedCredentialProviderResponse:
        """
        @summary 创建联邦凭证提供方
        
        @param request: CreateFederatedCredentialProviderRequest
        @return: CreateFederatedCredentialProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_federated_credential_provider_with_options_async(request, runtime)

    def create_group_with_options(
        self,
        request: eiam_20211201_models.CreateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.CreateGroupResponse:
        """
        @summary Creates an account group in Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM).
        
        @param request: CreateGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_external_id):
            query['GroupExternalId'] = request.group_external_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGroup',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.CreateGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_group_with_options_async(
        self,
        request: eiam_20211201_models.CreateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.CreateGroupResponse:
        """
        @summary Creates an account group in Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM).
        
        @param request: CreateGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_external_id):
            query['GroupExternalId'] = request.group_external_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGroup',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.CreateGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_group(
        self,
        request: eiam_20211201_models.CreateGroupRequest,
    ) -> eiam_20211201_models.CreateGroupResponse:
        """
        @summary Creates an account group in Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM).
        
        @param request: CreateGroupRequest
        @return: CreateGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_group_with_options(request, runtime)

    async def create_group_async(
        self,
        request: eiam_20211201_models.CreateGroupRequest,
    ) -> eiam_20211201_models.CreateGroupResponse:
        """
        @summary Creates an account group in Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM).
        
        @param request: CreateGroupRequest
        @return: CreateGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_group_with_options_async(request, runtime)

    def create_identity_provider_with_options(
        self,
        request: eiam_20211201_models.CreateIdentityProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.CreateIdentityProviderResponse:
        """
        @summary Create Identity Provider
        
        @param request: CreateIdentityProviderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateIdentityProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authn_config):
            query['AuthnConfig'] = request.authn_config
        if not UtilClient.is_unset(request.auto_create_user_config):
            query['AutoCreateUserConfig'] = request.auto_create_user_config
        if not UtilClient.is_unset(request.auto_update_user_config):
            query['AutoUpdateUserConfig'] = request.auto_update_user_config
        if not UtilClient.is_unset(request.binding_config):
            query['BindingConfig'] = request.binding_config
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dingtalk_app_config):
            query['DingtalkAppConfig'] = request.dingtalk_app_config
        if not UtilClient.is_unset(request.identity_provider_name):
            query['IdentityProviderName'] = request.identity_provider_name
        if not UtilClient.is_unset(request.identity_provider_type):
            query['IdentityProviderType'] = request.identity_provider_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lark_config):
            query['LarkConfig'] = request.lark_config
        if not UtilClient.is_unset(request.ldap_config):
            query['LdapConfig'] = request.ldap_config
        if not UtilClient.is_unset(request.logo_url):
            query['LogoUrl'] = request.logo_url
        if not UtilClient.is_unset(request.network_access_endpoint_id):
            query['NetworkAccessEndpointId'] = request.network_access_endpoint_id
        if not UtilClient.is_unset(request.oidc_config):
            query['OidcConfig'] = request.oidc_config
        if not UtilClient.is_unset(request.ud_pull_config):
            query['UdPullConfig'] = request.ud_pull_config
        if not UtilClient.is_unset(request.ud_push_config):
            query['UdPushConfig'] = request.ud_push_config
        if not UtilClient.is_unset(request.we_com_config):
            query['WeComConfig'] = request.we_com_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateIdentityProvider',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.CreateIdentityProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_identity_provider_with_options_async(
        self,
        request: eiam_20211201_models.CreateIdentityProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.CreateIdentityProviderResponse:
        """
        @summary Create Identity Provider
        
        @param request: CreateIdentityProviderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateIdentityProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authn_config):
            query['AuthnConfig'] = request.authn_config
        if not UtilClient.is_unset(request.auto_create_user_config):
            query['AutoCreateUserConfig'] = request.auto_create_user_config
        if not UtilClient.is_unset(request.auto_update_user_config):
            query['AutoUpdateUserConfig'] = request.auto_update_user_config
        if not UtilClient.is_unset(request.binding_config):
            query['BindingConfig'] = request.binding_config
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dingtalk_app_config):
            query['DingtalkAppConfig'] = request.dingtalk_app_config
        if not UtilClient.is_unset(request.identity_provider_name):
            query['IdentityProviderName'] = request.identity_provider_name
        if not UtilClient.is_unset(request.identity_provider_type):
            query['IdentityProviderType'] = request.identity_provider_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lark_config):
            query['LarkConfig'] = request.lark_config
        if not UtilClient.is_unset(request.ldap_config):
            query['LdapConfig'] = request.ldap_config
        if not UtilClient.is_unset(request.logo_url):
            query['LogoUrl'] = request.logo_url
        if not UtilClient.is_unset(request.network_access_endpoint_id):
            query['NetworkAccessEndpointId'] = request.network_access_endpoint_id
        if not UtilClient.is_unset(request.oidc_config):
            query['OidcConfig'] = request.oidc_config
        if not UtilClient.is_unset(request.ud_pull_config):
            query['UdPullConfig'] = request.ud_pull_config
        if not UtilClient.is_unset(request.ud_push_config):
            query['UdPushConfig'] = request.ud_push_config
        if not UtilClient.is_unset(request.we_com_config):
            query['WeComConfig'] = request.we_com_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateIdentityProvider',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.CreateIdentityProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_identity_provider(
        self,
        request: eiam_20211201_models.CreateIdentityProviderRequest,
    ) -> eiam_20211201_models.CreateIdentityProviderResponse:
        """
        @summary Create Identity Provider
        
        @param request: CreateIdentityProviderRequest
        @return: CreateIdentityProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_identity_provider_with_options(request, runtime)

    async def create_identity_provider_async(
        self,
        request: eiam_20211201_models.CreateIdentityProviderRequest,
    ) -> eiam_20211201_models.CreateIdentityProviderResponse:
        """
        @summary Create Identity Provider
        
        @param request: CreateIdentityProviderRequest
        @return: CreateIdentityProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_identity_provider_with_options_async(request, runtime)

    def create_instance_with_options(
        self,
        request: eiam_20211201_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.CreateInstanceResponse:
        """
        @summary Creates an instance based on which all capabilities of Identity as a Service (IDaaS) Enterprise Identity and Access Management (EIAM) are provided.
        
        @param request: CreateInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        request: eiam_20211201_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.CreateInstanceResponse:
        """
        @summary Creates an instance based on which all capabilities of Identity as a Service (IDaaS) Enterprise Identity and Access Management (EIAM) are provided.
        
        @param request: CreateInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.CreateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance(
        self,
        request: eiam_20211201_models.CreateInstanceRequest,
    ) -> eiam_20211201_models.CreateInstanceResponse:
        """
        @summary Creates an instance based on which all capabilities of Identity as a Service (IDaaS) Enterprise Identity and Access Management (EIAM) are provided.
        
        @param request: CreateInstanceRequest
        @return: CreateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_instance_with_options(request, runtime)

    async def create_instance_async(
        self,
        request: eiam_20211201_models.CreateInstanceRequest,
    ) -> eiam_20211201_models.CreateInstanceResponse:
        """
        @summary Creates an instance based on which all capabilities of Identity as a Service (IDaaS) Enterprise Identity and Access Management (EIAM) are provided.
        
        @param request: CreateInstanceRequest
        @return: CreateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_instance_with_options_async(request, runtime)

    def create_network_access_endpoint_with_options(
        self,
        request: eiam_20211201_models.CreateNetworkAccessEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.CreateNetworkAccessEndpointResponse:
        """
        @summary Creates a dedicated endpoint.
        
        @param request: CreateNetworkAccessEndpointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateNetworkAccessEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_access_endpoint_name):
            query['NetworkAccessEndpointName'] = request.network_access_endpoint_name
        if not UtilClient.is_unset(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vpc_region_id):
            query['VpcRegionId'] = request.vpc_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNetworkAccessEndpoint',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.CreateNetworkAccessEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_network_access_endpoint_with_options_async(
        self,
        request: eiam_20211201_models.CreateNetworkAccessEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.CreateNetworkAccessEndpointResponse:
        """
        @summary Creates a dedicated endpoint.
        
        @param request: CreateNetworkAccessEndpointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateNetworkAccessEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_access_endpoint_name):
            query['NetworkAccessEndpointName'] = request.network_access_endpoint_name
        if not UtilClient.is_unset(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vpc_region_id):
            query['VpcRegionId'] = request.vpc_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNetworkAccessEndpoint',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.CreateNetworkAccessEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_network_access_endpoint(
        self,
        request: eiam_20211201_models.CreateNetworkAccessEndpointRequest,
    ) -> eiam_20211201_models.CreateNetworkAccessEndpointResponse:
        """
        @summary Creates a dedicated endpoint.
        
        @param request: CreateNetworkAccessEndpointRequest
        @return: CreateNetworkAccessEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_network_access_endpoint_with_options(request, runtime)

    async def create_network_access_endpoint_async(
        self,
        request: eiam_20211201_models.CreateNetworkAccessEndpointRequest,
    ) -> eiam_20211201_models.CreateNetworkAccessEndpointResponse:
        """
        @summary Creates a dedicated endpoint.
        
        @param request: CreateNetworkAccessEndpointRequest
        @return: CreateNetworkAccessEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_network_access_endpoint_with_options_async(request, runtime)

    def create_network_zone_with_options(
        self,
        request: eiam_20211201_models.CreateNetworkZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.CreateNetworkZoneResponse:
        """
        @summary 创建网络区域对象
        
        @param request: CreateNetworkZoneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateNetworkZoneResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ipv_4cidrs):
            query['Ipv4Cidrs'] = request.ipv_4cidrs
        if not UtilClient.is_unset(request.ipv_6cidrs):
            query['Ipv6Cidrs'] = request.ipv_6cidrs
        if not UtilClient.is_unset(request.network_zone_name):
            query['NetworkZoneName'] = request.network_zone_name
        if not UtilClient.is_unset(request.network_zone_type):
            query['NetworkZoneType'] = request.network_zone_type
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNetworkZone',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.CreateNetworkZoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_network_zone_with_options_async(
        self,
        request: eiam_20211201_models.CreateNetworkZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.CreateNetworkZoneResponse:
        """
        @summary 创建网络区域对象
        
        @param request: CreateNetworkZoneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateNetworkZoneResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ipv_4cidrs):
            query['Ipv4Cidrs'] = request.ipv_4cidrs
        if not UtilClient.is_unset(request.ipv_6cidrs):
            query['Ipv6Cidrs'] = request.ipv_6cidrs
        if not UtilClient.is_unset(request.network_zone_name):
            query['NetworkZoneName'] = request.network_zone_name
        if not UtilClient.is_unset(request.network_zone_type):
            query['NetworkZoneType'] = request.network_zone_type
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNetworkZone',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.CreateNetworkZoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_network_zone(
        self,
        request: eiam_20211201_models.CreateNetworkZoneRequest,
    ) -> eiam_20211201_models.CreateNetworkZoneResponse:
        """
        @summary 创建网络区域对象
        
        @param request: CreateNetworkZoneRequest
        @return: CreateNetworkZoneResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_network_zone_with_options(request, runtime)

    async def create_network_zone_async(
        self,
        request: eiam_20211201_models.CreateNetworkZoneRequest,
    ) -> eiam_20211201_models.CreateNetworkZoneResponse:
        """
        @summary 创建网络区域对象
        
        @param request: CreateNetworkZoneRequest
        @return: CreateNetworkZoneResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_network_zone_with_options_async(request, runtime)

    def create_organizational_unit_with_options(
        self,
        request: eiam_20211201_models.CreateOrganizationalUnitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.CreateOrganizationalUnitResponse:
        """
        @summary Creates an organization in Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM).
        
        @param request: CreateOrganizationalUnitRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateOrganizationalUnitResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.organizational_unit_external_id):
            query['OrganizationalUnitExternalId'] = request.organizational_unit_external_id
        if not UtilClient.is_unset(request.organizational_unit_name):
            query['OrganizationalUnitName'] = request.organizational_unit_name
        if not UtilClient.is_unset(request.parent_id):
            query['ParentId'] = request.parent_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOrganizationalUnit',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.CreateOrganizationalUnitResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_organizational_unit_with_options_async(
        self,
        request: eiam_20211201_models.CreateOrganizationalUnitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.CreateOrganizationalUnitResponse:
        """
        @summary Creates an organization in Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM).
        
        @param request: CreateOrganizationalUnitRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateOrganizationalUnitResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.organizational_unit_external_id):
            query['OrganizationalUnitExternalId'] = request.organizational_unit_external_id
        if not UtilClient.is_unset(request.organizational_unit_name):
            query['OrganizationalUnitName'] = request.organizational_unit_name
        if not UtilClient.is_unset(request.parent_id):
            query['ParentId'] = request.parent_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOrganizationalUnit',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.CreateOrganizationalUnitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_organizational_unit(
        self,
        request: eiam_20211201_models.CreateOrganizationalUnitRequest,
    ) -> eiam_20211201_models.CreateOrganizationalUnitResponse:
        """
        @summary Creates an organization in Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM).
        
        @param request: CreateOrganizationalUnitRequest
        @return: CreateOrganizationalUnitResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_organizational_unit_with_options(request, runtime)

    async def create_organizational_unit_async(
        self,
        request: eiam_20211201_models.CreateOrganizationalUnitRequest,
    ) -> eiam_20211201_models.CreateOrganizationalUnitResponse:
        """
        @summary Creates an organization in Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM).
        
        @param request: CreateOrganizationalUnitRequest
        @return: CreateOrganizationalUnitResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_organizational_unit_with_options_async(request, runtime)

    def create_user_with_options(
        self,
        request: eiam_20211201_models.CreateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.CreateUserResponse:
        """
        @summary Creates an account in an Identity as a Service (IDaaS) Enterprise Identity Access Management (EIAM) instance.
        
        @param request: CreateUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.custom_fields):
            query['CustomFields'] = request.custom_fields
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.email_verified):
            query['EmailVerified'] = request.email_verified
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.organizational_unit_ids):
            query['OrganizationalUnitIds'] = request.organizational_unit_ids
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.password_initialization_config):
            query['PasswordInitializationConfig'] = request.password_initialization_config
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.phone_number_verified):
            query['PhoneNumberVerified'] = request.phone_number_verified
        if not UtilClient.is_unset(request.phone_region):
            query['PhoneRegion'] = request.phone_region
        if not UtilClient.is_unset(request.primary_organizational_unit_id):
            query['PrimaryOrganizationalUnitId'] = request.primary_organizational_unit_id
        if not UtilClient.is_unset(request.user_external_id):
            query['UserExternalId'] = request.user_external_id
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUser',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.CreateUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_user_with_options_async(
        self,
        request: eiam_20211201_models.CreateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.CreateUserResponse:
        """
        @summary Creates an account in an Identity as a Service (IDaaS) Enterprise Identity Access Management (EIAM) instance.
        
        @param request: CreateUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.custom_fields):
            query['CustomFields'] = request.custom_fields
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.email_verified):
            query['EmailVerified'] = request.email_verified
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.organizational_unit_ids):
            query['OrganizationalUnitIds'] = request.organizational_unit_ids
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.password_initialization_config):
            query['PasswordInitializationConfig'] = request.password_initialization_config
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.phone_number_verified):
            query['PhoneNumberVerified'] = request.phone_number_verified
        if not UtilClient.is_unset(request.phone_region):
            query['PhoneRegion'] = request.phone_region
        if not UtilClient.is_unset(request.primary_organizational_unit_id):
            query['PrimaryOrganizationalUnitId'] = request.primary_organizational_unit_id
        if not UtilClient.is_unset(request.user_external_id):
            query['UserExternalId'] = request.user_external_id
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUser',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.CreateUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_user(
        self,
        request: eiam_20211201_models.CreateUserRequest,
    ) -> eiam_20211201_models.CreateUserResponse:
        """
        @summary Creates an account in an Identity as a Service (IDaaS) Enterprise Identity Access Management (EIAM) instance.
        
        @param request: CreateUserRequest
        @return: CreateUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_user_with_options(request, runtime)

    async def create_user_async(
        self,
        request: eiam_20211201_models.CreateUserRequest,
    ) -> eiam_20211201_models.CreateUserResponse:
        """
        @summary Creates an account in an Identity as a Service (IDaaS) Enterprise Identity Access Management (EIAM) instance.
        
        @param request: CreateUserRequest
        @return: CreateUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_user_with_options_async(request, runtime)

    def delete_application_with_options(
        self,
        request: eiam_20211201_models.DeleteApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DeleteApplicationResponse:
        """
        @summary Deletes an Employee Identity and Access Management (EIAM) application.
        
        @description Make sure that the EIAM application that you want to delete is not used before you delete the EIAM application. After you delete the EIAM application, all configurations are deleted and cannot be restored.
        
        @param request: DeleteApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApplication',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DeleteApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_application_with_options_async(
        self,
        request: eiam_20211201_models.DeleteApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DeleteApplicationResponse:
        """
        @summary Deletes an Employee Identity and Access Management (EIAM) application.
        
        @description Make sure that the EIAM application that you want to delete is not used before you delete the EIAM application. After you delete the EIAM application, all configurations are deleted and cannot be restored.
        
        @param request: DeleteApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApplication',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DeleteApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_application(
        self,
        request: eiam_20211201_models.DeleteApplicationRequest,
    ) -> eiam_20211201_models.DeleteApplicationResponse:
        """
        @summary Deletes an Employee Identity and Access Management (EIAM) application.
        
        @description Make sure that the EIAM application that you want to delete is not used before you delete the EIAM application. After you delete the EIAM application, all configurations are deleted and cannot be restored.
        
        @param request: DeleteApplicationRequest
        @return: DeleteApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_application_with_options(request, runtime)

    async def delete_application_async(
        self,
        request: eiam_20211201_models.DeleteApplicationRequest,
    ) -> eiam_20211201_models.DeleteApplicationResponse:
        """
        @summary Deletes an Employee Identity and Access Management (EIAM) application.
        
        @description Make sure that the EIAM application that you want to delete is not used before you delete the EIAM application. After you delete the EIAM application, all configurations are deleted and cannot be restored.
        
        @param request: DeleteApplicationRequest
        @return: DeleteApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_application_with_options_async(request, runtime)

    def delete_application_client_secret_with_options(
        self,
        request: eiam_20211201_models.DeleteApplicationClientSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DeleteApplicationClientSecretResponse:
        """
        @summary Deletes a client key for an Employee Identity and Access Management (EIAM) application.
        
        @param request: DeleteApplicationClientSecretRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteApplicationClientSecretResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.secret_id):
            query['SecretId'] = request.secret_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApplicationClientSecret',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DeleteApplicationClientSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_application_client_secret_with_options_async(
        self,
        request: eiam_20211201_models.DeleteApplicationClientSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DeleteApplicationClientSecretResponse:
        """
        @summary Deletes a client key for an Employee Identity and Access Management (EIAM) application.
        
        @param request: DeleteApplicationClientSecretRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteApplicationClientSecretResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.secret_id):
            query['SecretId'] = request.secret_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApplicationClientSecret',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DeleteApplicationClientSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_application_client_secret(
        self,
        request: eiam_20211201_models.DeleteApplicationClientSecretRequest,
    ) -> eiam_20211201_models.DeleteApplicationClientSecretResponse:
        """
        @summary Deletes a client key for an Employee Identity and Access Management (EIAM) application.
        
        @param request: DeleteApplicationClientSecretRequest
        @return: DeleteApplicationClientSecretResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_application_client_secret_with_options(request, runtime)

    async def delete_application_client_secret_async(
        self,
        request: eiam_20211201_models.DeleteApplicationClientSecretRequest,
    ) -> eiam_20211201_models.DeleteApplicationClientSecretResponse:
        """
        @summary Deletes a client key for an Employee Identity and Access Management (EIAM) application.
        
        @param request: DeleteApplicationClientSecretRequest
        @return: DeleteApplicationClientSecretResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_application_client_secret_with_options_async(request, runtime)

    def delete_application_federated_credential_with_options(
        self,
        request: eiam_20211201_models.DeleteApplicationFederatedCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DeleteApplicationFederatedCredentialResponse:
        """
        @summary 删除应用联邦凭证
        
        @param request: DeleteApplicationFederatedCredentialRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteApplicationFederatedCredentialResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_federated_credential_id):
            query['ApplicationFederatedCredentialId'] = request.application_federated_credential_id
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApplicationFederatedCredential',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DeleteApplicationFederatedCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_application_federated_credential_with_options_async(
        self,
        request: eiam_20211201_models.DeleteApplicationFederatedCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DeleteApplicationFederatedCredentialResponse:
        """
        @summary 删除应用联邦凭证
        
        @param request: DeleteApplicationFederatedCredentialRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteApplicationFederatedCredentialResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_federated_credential_id):
            query['ApplicationFederatedCredentialId'] = request.application_federated_credential_id
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApplicationFederatedCredential',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DeleteApplicationFederatedCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_application_federated_credential(
        self,
        request: eiam_20211201_models.DeleteApplicationFederatedCredentialRequest,
    ) -> eiam_20211201_models.DeleteApplicationFederatedCredentialResponse:
        """
        @summary 删除应用联邦凭证
        
        @param request: DeleteApplicationFederatedCredentialRequest
        @return: DeleteApplicationFederatedCredentialResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_application_federated_credential_with_options(request, runtime)

    async def delete_application_federated_credential_async(
        self,
        request: eiam_20211201_models.DeleteApplicationFederatedCredentialRequest,
    ) -> eiam_20211201_models.DeleteApplicationFederatedCredentialResponse:
        """
        @summary 删除应用联邦凭证
        
        @param request: DeleteApplicationFederatedCredentialRequest
        @return: DeleteApplicationFederatedCredentialResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_application_federated_credential_with_options_async(request, runtime)

    def delete_application_token_with_options(
        self,
        request: eiam_20211201_models.DeleteApplicationTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DeleteApplicationTokenResponse:
        """
        @summary 删除ApplicationToken
        
        @param request: DeleteApplicationTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteApplicationTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.application_token_id):
            query['ApplicationTokenId'] = request.application_token_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApplicationToken',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DeleteApplicationTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_application_token_with_options_async(
        self,
        request: eiam_20211201_models.DeleteApplicationTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DeleteApplicationTokenResponse:
        """
        @summary 删除ApplicationToken
        
        @param request: DeleteApplicationTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteApplicationTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.application_token_id):
            query['ApplicationTokenId'] = request.application_token_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApplicationToken',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DeleteApplicationTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_application_token(
        self,
        request: eiam_20211201_models.DeleteApplicationTokenRequest,
    ) -> eiam_20211201_models.DeleteApplicationTokenResponse:
        """
        @summary 删除ApplicationToken
        
        @param request: DeleteApplicationTokenRequest
        @return: DeleteApplicationTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_application_token_with_options(request, runtime)

    async def delete_application_token_async(
        self,
        request: eiam_20211201_models.DeleteApplicationTokenRequest,
    ) -> eiam_20211201_models.DeleteApplicationTokenResponse:
        """
        @summary 删除ApplicationToken
        
        @param request: DeleteApplicationTokenRequest
        @return: DeleteApplicationTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_application_token_with_options_async(request, runtime)

    def delete_brand_with_options(
        self,
        request: eiam_20211201_models.DeleteBrandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DeleteBrandResponse:
        """
        @summary 删除品牌
        
        @param request: DeleteBrandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteBrandResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.brand_id):
            query['BrandId'] = request.brand_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBrand',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DeleteBrandResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_brand_with_options_async(
        self,
        request: eiam_20211201_models.DeleteBrandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DeleteBrandResponse:
        """
        @summary 删除品牌
        
        @param request: DeleteBrandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteBrandResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.brand_id):
            query['BrandId'] = request.brand_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBrand',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DeleteBrandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_brand(
        self,
        request: eiam_20211201_models.DeleteBrandRequest,
    ) -> eiam_20211201_models.DeleteBrandResponse:
        """
        @summary 删除品牌
        
        @param request: DeleteBrandRequest
        @return: DeleteBrandResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_brand_with_options(request, runtime)

    async def delete_brand_async(
        self,
        request: eiam_20211201_models.DeleteBrandRequest,
    ) -> eiam_20211201_models.DeleteBrandResponse:
        """
        @summary 删除品牌
        
        @param request: DeleteBrandRequest
        @return: DeleteBrandResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_brand_with_options_async(request, runtime)

    def delete_conditional_access_policy_with_options(
        self,
        request: eiam_20211201_models.DeleteConditionalAccessPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DeleteConditionalAccessPolicyResponse:
        """
        @summary Delete Conditional Access Policy
        
        @description When deleting a specified conditional access policy, please ensure that the policy is no longer in use. After deletion, all configuration data will be removed and cannot be recovered.
        
        @param request: DeleteConditionalAccessPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteConditionalAccessPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.conditional_access_policy_id):
            query['ConditionalAccessPolicyId'] = request.conditional_access_policy_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteConditionalAccessPolicy',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DeleteConditionalAccessPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_conditional_access_policy_with_options_async(
        self,
        request: eiam_20211201_models.DeleteConditionalAccessPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DeleteConditionalAccessPolicyResponse:
        """
        @summary Delete Conditional Access Policy
        
        @description When deleting a specified conditional access policy, please ensure that the policy is no longer in use. After deletion, all configuration data will be removed and cannot be recovered.
        
        @param request: DeleteConditionalAccessPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteConditionalAccessPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.conditional_access_policy_id):
            query['ConditionalAccessPolicyId'] = request.conditional_access_policy_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteConditionalAccessPolicy',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DeleteConditionalAccessPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_conditional_access_policy(
        self,
        request: eiam_20211201_models.DeleteConditionalAccessPolicyRequest,
    ) -> eiam_20211201_models.DeleteConditionalAccessPolicyResponse:
        """
        @summary Delete Conditional Access Policy
        
        @description When deleting a specified conditional access policy, please ensure that the policy is no longer in use. After deletion, all configuration data will be removed and cannot be recovered.
        
        @param request: DeleteConditionalAccessPolicyRequest
        @return: DeleteConditionalAccessPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_conditional_access_policy_with_options(request, runtime)

    async def delete_conditional_access_policy_async(
        self,
        request: eiam_20211201_models.DeleteConditionalAccessPolicyRequest,
    ) -> eiam_20211201_models.DeleteConditionalAccessPolicyResponse:
        """
        @summary Delete Conditional Access Policy
        
        @description When deleting a specified conditional access policy, please ensure that the policy is no longer in use. After deletion, all configuration data will be removed and cannot be recovered.
        
        @param request: DeleteConditionalAccessPolicyRequest
        @return: DeleteConditionalAccessPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_conditional_access_policy_with_options_async(request, runtime)

    def delete_custom_privacy_policy_with_options(
        self,
        request: eiam_20211201_models.DeleteCustomPrivacyPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DeleteCustomPrivacyPolicyResponse:
        """
        @summary 删除自定义条款
        
        @param request: DeleteCustomPrivacyPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCustomPrivacyPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_privacy_policy_id):
            query['CustomPrivacyPolicyId'] = request.custom_privacy_policy_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCustomPrivacyPolicy',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DeleteCustomPrivacyPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_custom_privacy_policy_with_options_async(
        self,
        request: eiam_20211201_models.DeleteCustomPrivacyPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DeleteCustomPrivacyPolicyResponse:
        """
        @summary 删除自定义条款
        
        @param request: DeleteCustomPrivacyPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCustomPrivacyPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_privacy_policy_id):
            query['CustomPrivacyPolicyId'] = request.custom_privacy_policy_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCustomPrivacyPolicy',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DeleteCustomPrivacyPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_custom_privacy_policy(
        self,
        request: eiam_20211201_models.DeleteCustomPrivacyPolicyRequest,
    ) -> eiam_20211201_models.DeleteCustomPrivacyPolicyResponse:
        """
        @summary 删除自定义条款
        
        @param request: DeleteCustomPrivacyPolicyRequest
        @return: DeleteCustomPrivacyPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_custom_privacy_policy_with_options(request, runtime)

    async def delete_custom_privacy_policy_async(
        self,
        request: eiam_20211201_models.DeleteCustomPrivacyPolicyRequest,
    ) -> eiam_20211201_models.DeleteCustomPrivacyPolicyResponse:
        """
        @summary 删除自定义条款
        
        @param request: DeleteCustomPrivacyPolicyRequest
        @return: DeleteCustomPrivacyPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_custom_privacy_policy_with_options_async(request, runtime)

    def delete_domain_with_options(
        self,
        request: eiam_20211201_models.DeleteDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DeleteDomainResponse:
        """
        @summary Deletes a custom domain name of an Employee Identity and Access Management (EIAM) instance. You cannot delete the initial domain name and default domain name of the instance.
        
        @param request: DeleteDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDomain',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DeleteDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_domain_with_options_async(
        self,
        request: eiam_20211201_models.DeleteDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DeleteDomainResponse:
        """
        @summary Deletes a custom domain name of an Employee Identity and Access Management (EIAM) instance. You cannot delete the initial domain name and default domain name of the instance.
        
        @param request: DeleteDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDomain',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DeleteDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_domain(
        self,
        request: eiam_20211201_models.DeleteDomainRequest,
    ) -> eiam_20211201_models.DeleteDomainResponse:
        """
        @summary Deletes a custom domain name of an Employee Identity and Access Management (EIAM) instance. You cannot delete the initial domain name and default domain name of the instance.
        
        @param request: DeleteDomainRequest
        @return: DeleteDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_domain_with_options(request, runtime)

    async def delete_domain_async(
        self,
        request: eiam_20211201_models.DeleteDomainRequest,
    ) -> eiam_20211201_models.DeleteDomainResponse:
        """
        @summary Deletes a custom domain name of an Employee Identity and Access Management (EIAM) instance. You cannot delete the initial domain name and default domain name of the instance.
        
        @param request: DeleteDomainRequest
        @return: DeleteDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_domain_with_options_async(request, runtime)

    def delete_domain_proxy_token_with_options(
        self,
        request: eiam_20211201_models.DeleteDomainProxyTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DeleteDomainProxyTokenResponse:
        """
        @summary Deletes a proxy token for a domain name of an Employee Identity and Access Management (EIAM) instance. Only the proxy tokens in the disabled state can be deleted.
        
        @param request: DeleteDomainProxyTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDomainProxyTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.domain_proxy_token_id):
            query['DomainProxyTokenId'] = request.domain_proxy_token_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDomainProxyToken',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DeleteDomainProxyTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_domain_proxy_token_with_options_async(
        self,
        request: eiam_20211201_models.DeleteDomainProxyTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DeleteDomainProxyTokenResponse:
        """
        @summary Deletes a proxy token for a domain name of an Employee Identity and Access Management (EIAM) instance. Only the proxy tokens in the disabled state can be deleted.
        
        @param request: DeleteDomainProxyTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDomainProxyTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.domain_proxy_token_id):
            query['DomainProxyTokenId'] = request.domain_proxy_token_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDomainProxyToken',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DeleteDomainProxyTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_domain_proxy_token(
        self,
        request: eiam_20211201_models.DeleteDomainProxyTokenRequest,
    ) -> eiam_20211201_models.DeleteDomainProxyTokenResponse:
        """
        @summary Deletes a proxy token for a domain name of an Employee Identity and Access Management (EIAM) instance. Only the proxy tokens in the disabled state can be deleted.
        
        @param request: DeleteDomainProxyTokenRequest
        @return: DeleteDomainProxyTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_domain_proxy_token_with_options(request, runtime)

    async def delete_domain_proxy_token_async(
        self,
        request: eiam_20211201_models.DeleteDomainProxyTokenRequest,
    ) -> eiam_20211201_models.DeleteDomainProxyTokenResponse:
        """
        @summary Deletes a proxy token for a domain name of an Employee Identity and Access Management (EIAM) instance. Only the proxy tokens in the disabled state can be deleted.
        
        @param request: DeleteDomainProxyTokenRequest
        @return: DeleteDomainProxyTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_domain_proxy_token_with_options_async(request, runtime)

    def delete_federated_credential_provider_with_options(
        self,
        request: eiam_20211201_models.DeleteFederatedCredentialProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DeleteFederatedCredentialProviderResponse:
        """
        @summary 删除联邦凭证提供方
        
        @param request: DeleteFederatedCredentialProviderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFederatedCredentialProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.federated_credential_provider_id):
            query['FederatedCredentialProviderId'] = request.federated_credential_provider_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFederatedCredentialProvider',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DeleteFederatedCredentialProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_federated_credential_provider_with_options_async(
        self,
        request: eiam_20211201_models.DeleteFederatedCredentialProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DeleteFederatedCredentialProviderResponse:
        """
        @summary 删除联邦凭证提供方
        
        @param request: DeleteFederatedCredentialProviderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFederatedCredentialProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.federated_credential_provider_id):
            query['FederatedCredentialProviderId'] = request.federated_credential_provider_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFederatedCredentialProvider',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DeleteFederatedCredentialProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_federated_credential_provider(
        self,
        request: eiam_20211201_models.DeleteFederatedCredentialProviderRequest,
    ) -> eiam_20211201_models.DeleteFederatedCredentialProviderResponse:
        """
        @summary 删除联邦凭证提供方
        
        @param request: DeleteFederatedCredentialProviderRequest
        @return: DeleteFederatedCredentialProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_federated_credential_provider_with_options(request, runtime)

    async def delete_federated_credential_provider_async(
        self,
        request: eiam_20211201_models.DeleteFederatedCredentialProviderRequest,
    ) -> eiam_20211201_models.DeleteFederatedCredentialProviderResponse:
        """
        @summary 删除联邦凭证提供方
        
        @param request: DeleteFederatedCredentialProviderRequest
        @return: DeleteFederatedCredentialProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_federated_credential_provider_with_options_async(request, runtime)

    def delete_group_with_options(
        self,
        request: eiam_20211201_models.DeleteGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DeleteGroupResponse:
        """
        @summary Deletes the information of an account group in Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM).
        
        @param request: DeleteGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGroup',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DeleteGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_group_with_options_async(
        self,
        request: eiam_20211201_models.DeleteGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DeleteGroupResponse:
        """
        @summary Deletes the information of an account group in Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM).
        
        @param request: DeleteGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGroup',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DeleteGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_group(
        self,
        request: eiam_20211201_models.DeleteGroupRequest,
    ) -> eiam_20211201_models.DeleteGroupResponse:
        """
        @summary Deletes the information of an account group in Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM).
        
        @param request: DeleteGroupRequest
        @return: DeleteGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_group_with_options(request, runtime)

    async def delete_group_async(
        self,
        request: eiam_20211201_models.DeleteGroupRequest,
    ) -> eiam_20211201_models.DeleteGroupResponse:
        """
        @summary Deletes the information of an account group in Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM).
        
        @param request: DeleteGroupRequest
        @return: DeleteGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_group_with_options_async(request, runtime)

    def delete_identity_provider_with_options(
        self,
        request: eiam_20211201_models.DeleteIdentityProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DeleteIdentityProviderResponse:
        """
        @summary Delete identity provider
        
        @param request: DeleteIdentityProviderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteIdentityProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identity_provider_id):
            query['IdentityProviderId'] = request.identity_provider_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteIdentityProvider',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DeleteIdentityProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_identity_provider_with_options_async(
        self,
        request: eiam_20211201_models.DeleteIdentityProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DeleteIdentityProviderResponse:
        """
        @summary Delete identity provider
        
        @param request: DeleteIdentityProviderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteIdentityProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identity_provider_id):
            query['IdentityProviderId'] = request.identity_provider_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteIdentityProvider',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DeleteIdentityProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_identity_provider(
        self,
        request: eiam_20211201_models.DeleteIdentityProviderRequest,
    ) -> eiam_20211201_models.DeleteIdentityProviderResponse:
        """
        @summary Delete identity provider
        
        @param request: DeleteIdentityProviderRequest
        @return: DeleteIdentityProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_identity_provider_with_options(request, runtime)

    async def delete_identity_provider_async(
        self,
        request: eiam_20211201_models.DeleteIdentityProviderRequest,
    ) -> eiam_20211201_models.DeleteIdentityProviderResponse:
        """
        @summary Delete identity provider
        
        @param request: DeleteIdentityProviderRequest
        @return: DeleteIdentityProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_identity_provider_with_options_async(request, runtime)

    def delete_instance_with_options(
        self,
        request: eiam_20211201_models.DeleteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DeleteInstanceResponse:
        """
        @summary Deletes an Enterprise Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS) that you do not need.
        
        @description Make sure that the instance to be deleted is no longer used. If the instance is deleted, all data related to the instance will be deleted.
        
        @param request: DeleteInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInstance',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DeleteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_with_options_async(
        self,
        request: eiam_20211201_models.DeleteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DeleteInstanceResponse:
        """
        @summary Deletes an Enterprise Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS) that you do not need.
        
        @description Make sure that the instance to be deleted is no longer used. If the instance is deleted, all data related to the instance will be deleted.
        
        @param request: DeleteInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInstance',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DeleteInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance(
        self,
        request: eiam_20211201_models.DeleteInstanceRequest,
    ) -> eiam_20211201_models.DeleteInstanceResponse:
        """
        @summary Deletes an Enterprise Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS) that you do not need.
        
        @description Make sure that the instance to be deleted is no longer used. If the instance is deleted, all data related to the instance will be deleted.
        
        @param request: DeleteInstanceRequest
        @return: DeleteInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_instance_with_options(request, runtime)

    async def delete_instance_async(
        self,
        request: eiam_20211201_models.DeleteInstanceRequest,
    ) -> eiam_20211201_models.DeleteInstanceResponse:
        """
        @summary Deletes an Enterprise Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS) that you do not need.
        
        @description Make sure that the instance to be deleted is no longer used. If the instance is deleted, all data related to the instance will be deleted.
        
        @param request: DeleteInstanceRequest
        @return: DeleteInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_instance_with_options_async(request, runtime)

    def delete_network_access_endpoint_with_options(
        self,
        request: eiam_20211201_models.DeleteNetworkAccessEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DeleteNetworkAccessEndpointResponse:
        """
        @summary Delete a network endpoint of a specific type.
        
        @param request: DeleteNetworkAccessEndpointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteNetworkAccessEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_access_endpoint_id):
            query['NetworkAccessEndpointId'] = request.network_access_endpoint_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNetworkAccessEndpoint',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DeleteNetworkAccessEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_network_access_endpoint_with_options_async(
        self,
        request: eiam_20211201_models.DeleteNetworkAccessEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DeleteNetworkAccessEndpointResponse:
        """
        @summary Delete a network endpoint of a specific type.
        
        @param request: DeleteNetworkAccessEndpointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteNetworkAccessEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_access_endpoint_id):
            query['NetworkAccessEndpointId'] = request.network_access_endpoint_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNetworkAccessEndpoint',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DeleteNetworkAccessEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_network_access_endpoint(
        self,
        request: eiam_20211201_models.DeleteNetworkAccessEndpointRequest,
    ) -> eiam_20211201_models.DeleteNetworkAccessEndpointResponse:
        """
        @summary Delete a network endpoint of a specific type.
        
        @param request: DeleteNetworkAccessEndpointRequest
        @return: DeleteNetworkAccessEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_network_access_endpoint_with_options(request, runtime)

    async def delete_network_access_endpoint_async(
        self,
        request: eiam_20211201_models.DeleteNetworkAccessEndpointRequest,
    ) -> eiam_20211201_models.DeleteNetworkAccessEndpointResponse:
        """
        @summary Delete a network endpoint of a specific type.
        
        @param request: DeleteNetworkAccessEndpointRequest
        @return: DeleteNetworkAccessEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_network_access_endpoint_with_options_async(request, runtime)

    def delete_network_zone_with_options(
        self,
        request: eiam_20211201_models.DeleteNetworkZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DeleteNetworkZoneResponse:
        """
        @summary 删除网络区域对象
        
        @param request: DeleteNetworkZoneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteNetworkZoneResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_zone_id):
            query['NetworkZoneId'] = request.network_zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNetworkZone',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DeleteNetworkZoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_network_zone_with_options_async(
        self,
        request: eiam_20211201_models.DeleteNetworkZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DeleteNetworkZoneResponse:
        """
        @summary 删除网络区域对象
        
        @param request: DeleteNetworkZoneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteNetworkZoneResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_zone_id):
            query['NetworkZoneId'] = request.network_zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNetworkZone',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DeleteNetworkZoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_network_zone(
        self,
        request: eiam_20211201_models.DeleteNetworkZoneRequest,
    ) -> eiam_20211201_models.DeleteNetworkZoneResponse:
        """
        @summary 删除网络区域对象
        
        @param request: DeleteNetworkZoneRequest
        @return: DeleteNetworkZoneResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_network_zone_with_options(request, runtime)

    async def delete_network_zone_async(
        self,
        request: eiam_20211201_models.DeleteNetworkZoneRequest,
    ) -> eiam_20211201_models.DeleteNetworkZoneResponse:
        """
        @summary 删除网络区域对象
        
        @param request: DeleteNetworkZoneRequest
        @return: DeleteNetworkZoneResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_network_zone_with_options_async(request, runtime)

    def delete_organizational_unit_with_options(
        self,
        request: eiam_20211201_models.DeleteOrganizationalUnitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DeleteOrganizationalUnitResponse:
        """
        @summary Deletes an organization in Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM). If the organization has EIAM accounts or child organizations, the delete operation fails.
        
        @param request: DeleteOrganizationalUnitRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteOrganizationalUnitResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.organizational_unit_id):
            query['OrganizationalUnitId'] = request.organizational_unit_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteOrganizationalUnit',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DeleteOrganizationalUnitResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_organizational_unit_with_options_async(
        self,
        request: eiam_20211201_models.DeleteOrganizationalUnitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DeleteOrganizationalUnitResponse:
        """
        @summary Deletes an organization in Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM). If the organization has EIAM accounts or child organizations, the delete operation fails.
        
        @param request: DeleteOrganizationalUnitRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteOrganizationalUnitResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.organizational_unit_id):
            query['OrganizationalUnitId'] = request.organizational_unit_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteOrganizationalUnit',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DeleteOrganizationalUnitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_organizational_unit(
        self,
        request: eiam_20211201_models.DeleteOrganizationalUnitRequest,
    ) -> eiam_20211201_models.DeleteOrganizationalUnitResponse:
        """
        @summary Deletes an organization in Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM). If the organization has EIAM accounts or child organizations, the delete operation fails.
        
        @param request: DeleteOrganizationalUnitRequest
        @return: DeleteOrganizationalUnitResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_organizational_unit_with_options(request, runtime)

    async def delete_organizational_unit_async(
        self,
        request: eiam_20211201_models.DeleteOrganizationalUnitRequest,
    ) -> eiam_20211201_models.DeleteOrganizationalUnitResponse:
        """
        @summary Deletes an organization in Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM). If the organization has EIAM accounts or child organizations, the delete operation fails.
        
        @param request: DeleteOrganizationalUnitRequest
        @return: DeleteOrganizationalUnitResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_organizational_unit_with_options_async(request, runtime)

    def delete_organizational_unit_children_with_options(
        self,
        request: eiam_20211201_models.DeleteOrganizationalUnitChildrenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DeleteOrganizationalUnitChildrenResponse:
        """
        @summary Delete organizational unit information, forcibly deleting all accounts and sub-organizations beneath it
        
        @param request: DeleteOrganizationalUnitChildrenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteOrganizationalUnitChildrenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.organizational_unit_id):
            query['OrganizationalUnitId'] = request.organizational_unit_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteOrganizationalUnitChildren',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DeleteOrganizationalUnitChildrenResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_organizational_unit_children_with_options_async(
        self,
        request: eiam_20211201_models.DeleteOrganizationalUnitChildrenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DeleteOrganizationalUnitChildrenResponse:
        """
        @summary Delete organizational unit information, forcibly deleting all accounts and sub-organizations beneath it
        
        @param request: DeleteOrganizationalUnitChildrenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteOrganizationalUnitChildrenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.organizational_unit_id):
            query['OrganizationalUnitId'] = request.organizational_unit_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteOrganizationalUnitChildren',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DeleteOrganizationalUnitChildrenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_organizational_unit_children(
        self,
        request: eiam_20211201_models.DeleteOrganizationalUnitChildrenRequest,
    ) -> eiam_20211201_models.DeleteOrganizationalUnitChildrenResponse:
        """
        @summary Delete organizational unit information, forcibly deleting all accounts and sub-organizations beneath it
        
        @param request: DeleteOrganizationalUnitChildrenRequest
        @return: DeleteOrganizationalUnitChildrenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_organizational_unit_children_with_options(request, runtime)

    async def delete_organizational_unit_children_async(
        self,
        request: eiam_20211201_models.DeleteOrganizationalUnitChildrenRequest,
    ) -> eiam_20211201_models.DeleteOrganizationalUnitChildrenResponse:
        """
        @summary Delete organizational unit information, forcibly deleting all accounts and sub-organizations beneath it
        
        @param request: DeleteOrganizationalUnitChildrenRequest
        @return: DeleteOrganizationalUnitChildrenResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_organizational_unit_children_with_options_async(request, runtime)

    def delete_user_with_options(
        self,
        request: eiam_20211201_models.DeleteUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DeleteUserResponse:
        """
        @summary Deletes an Employee Identity and Access Management (EIAM) account of Identity as a Service (IDaaS). The information related to the account is cleared.
        
        @param request: DeleteUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUser',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DeleteUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_with_options_async(
        self,
        request: eiam_20211201_models.DeleteUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DeleteUserResponse:
        """
        @summary Deletes an Employee Identity and Access Management (EIAM) account of Identity as a Service (IDaaS). The information related to the account is cleared.
        
        @param request: DeleteUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUser',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DeleteUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user(
        self,
        request: eiam_20211201_models.DeleteUserRequest,
    ) -> eiam_20211201_models.DeleteUserResponse:
        """
        @summary Deletes an Employee Identity and Access Management (EIAM) account of Identity as a Service (IDaaS). The information related to the account is cleared.
        
        @param request: DeleteUserRequest
        @return: DeleteUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_user_with_options(request, runtime)

    async def delete_user_async(
        self,
        request: eiam_20211201_models.DeleteUserRequest,
    ) -> eiam_20211201_models.DeleteUserResponse:
        """
        @summary Deletes an Employee Identity and Access Management (EIAM) account of Identity as a Service (IDaaS). The information related to the account is cleared.
        
        @param request: DeleteUserRequest
        @return: DeleteUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_with_options_async(request, runtime)

    def disable_application_with_options(
        self,
        request: eiam_20211201_models.DisableApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DisableApplicationResponse:
        """
        @summary Disables an enabled Employee Identity and Access Management (EIAM) application. All features of the EIAM application cannot be used if you disable the EIAM application.
        
        @description All features of the EIAM application cannot be used if you disable the EIAM application, such as single sign-on (SSO) and account synchronization. Make sure that you acknowledge the risks of the delete operation.
        
        @param request: DisableApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableApplication',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DisableApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_application_with_options_async(
        self,
        request: eiam_20211201_models.DisableApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DisableApplicationResponse:
        """
        @summary Disables an enabled Employee Identity and Access Management (EIAM) application. All features of the EIAM application cannot be used if you disable the EIAM application.
        
        @description All features of the EIAM application cannot be used if you disable the EIAM application, such as single sign-on (SSO) and account synchronization. Make sure that you acknowledge the risks of the delete operation.
        
        @param request: DisableApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableApplication',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DisableApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_application(
        self,
        request: eiam_20211201_models.DisableApplicationRequest,
    ) -> eiam_20211201_models.DisableApplicationResponse:
        """
        @summary Disables an enabled Employee Identity and Access Management (EIAM) application. All features of the EIAM application cannot be used if you disable the EIAM application.
        
        @description All features of the EIAM application cannot be used if you disable the EIAM application, such as single sign-on (SSO) and account synchronization. Make sure that you acknowledge the risks of the delete operation.
        
        @param request: DisableApplicationRequest
        @return: DisableApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_application_with_options(request, runtime)

    async def disable_application_async(
        self,
        request: eiam_20211201_models.DisableApplicationRequest,
    ) -> eiam_20211201_models.DisableApplicationResponse:
        """
        @summary Disables an enabled Employee Identity and Access Management (EIAM) application. All features of the EIAM application cannot be used if you disable the EIAM application.
        
        @description All features of the EIAM application cannot be used if you disable the EIAM application, such as single sign-on (SSO) and account synchronization. Make sure that you acknowledge the risks of the delete operation.
        
        @param request: DisableApplicationRequest
        @return: DisableApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_application_with_options_async(request, runtime)

    def disable_application_api_invoke_with_options(
        self,
        request: eiam_20211201_models.DisableApplicationApiInvokeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DisableApplicationApiInvokeResponse:
        """
        @summary Disables the Developer API feature for an Employee Identity and Access Management (EIAM) application.
        
        @param request: DisableApplicationApiInvokeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableApplicationApiInvokeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableApplicationApiInvoke',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DisableApplicationApiInvokeResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_application_api_invoke_with_options_async(
        self,
        request: eiam_20211201_models.DisableApplicationApiInvokeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DisableApplicationApiInvokeResponse:
        """
        @summary Disables the Developer API feature for an Employee Identity and Access Management (EIAM) application.
        
        @param request: DisableApplicationApiInvokeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableApplicationApiInvokeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableApplicationApiInvoke',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DisableApplicationApiInvokeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_application_api_invoke(
        self,
        request: eiam_20211201_models.DisableApplicationApiInvokeRequest,
    ) -> eiam_20211201_models.DisableApplicationApiInvokeResponse:
        """
        @summary Disables the Developer API feature for an Employee Identity and Access Management (EIAM) application.
        
        @param request: DisableApplicationApiInvokeRequest
        @return: DisableApplicationApiInvokeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_application_api_invoke_with_options(request, runtime)

    async def disable_application_api_invoke_async(
        self,
        request: eiam_20211201_models.DisableApplicationApiInvokeRequest,
    ) -> eiam_20211201_models.DisableApplicationApiInvokeResponse:
        """
        @summary Disables the Developer API feature for an Employee Identity and Access Management (EIAM) application.
        
        @param request: DisableApplicationApiInvokeRequest
        @return: DisableApplicationApiInvokeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_application_api_invoke_with_options_async(request, runtime)

    def disable_application_client_secret_with_options(
        self,
        request: eiam_20211201_models.DisableApplicationClientSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DisableApplicationClientSecretResponse:
        """
        @summary Disables a client key of an Employee Identity and Access Management (EIAM) application.
        
        @param request: DisableApplicationClientSecretRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableApplicationClientSecretResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.secret_id):
            query['SecretId'] = request.secret_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableApplicationClientSecret',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DisableApplicationClientSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_application_client_secret_with_options_async(
        self,
        request: eiam_20211201_models.DisableApplicationClientSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DisableApplicationClientSecretResponse:
        """
        @summary Disables a client key of an Employee Identity and Access Management (EIAM) application.
        
        @param request: DisableApplicationClientSecretRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableApplicationClientSecretResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.secret_id):
            query['SecretId'] = request.secret_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableApplicationClientSecret',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DisableApplicationClientSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_application_client_secret(
        self,
        request: eiam_20211201_models.DisableApplicationClientSecretRequest,
    ) -> eiam_20211201_models.DisableApplicationClientSecretResponse:
        """
        @summary Disables a client key of an Employee Identity and Access Management (EIAM) application.
        
        @param request: DisableApplicationClientSecretRequest
        @return: DisableApplicationClientSecretResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_application_client_secret_with_options(request, runtime)

    async def disable_application_client_secret_async(
        self,
        request: eiam_20211201_models.DisableApplicationClientSecretRequest,
    ) -> eiam_20211201_models.DisableApplicationClientSecretResponse:
        """
        @summary Disables a client key of an Employee Identity and Access Management (EIAM) application.
        
        @param request: DisableApplicationClientSecretRequest
        @return: DisableApplicationClientSecretResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_application_client_secret_with_options_async(request, runtime)

    def disable_application_federated_credential_with_options(
        self,
        request: eiam_20211201_models.DisableApplicationFederatedCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DisableApplicationFederatedCredentialResponse:
        """
        @summary 禁用应用联邦凭证
        
        @param request: DisableApplicationFederatedCredentialRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableApplicationFederatedCredentialResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_federated_credential_id):
            query['ApplicationFederatedCredentialId'] = request.application_federated_credential_id
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableApplicationFederatedCredential',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DisableApplicationFederatedCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_application_federated_credential_with_options_async(
        self,
        request: eiam_20211201_models.DisableApplicationFederatedCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DisableApplicationFederatedCredentialResponse:
        """
        @summary 禁用应用联邦凭证
        
        @param request: DisableApplicationFederatedCredentialRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableApplicationFederatedCredentialResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_federated_credential_id):
            query['ApplicationFederatedCredentialId'] = request.application_federated_credential_id
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableApplicationFederatedCredential',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DisableApplicationFederatedCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_application_federated_credential(
        self,
        request: eiam_20211201_models.DisableApplicationFederatedCredentialRequest,
    ) -> eiam_20211201_models.DisableApplicationFederatedCredentialResponse:
        """
        @summary 禁用应用联邦凭证
        
        @param request: DisableApplicationFederatedCredentialRequest
        @return: DisableApplicationFederatedCredentialResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_application_federated_credential_with_options(request, runtime)

    async def disable_application_federated_credential_async(
        self,
        request: eiam_20211201_models.DisableApplicationFederatedCredentialRequest,
    ) -> eiam_20211201_models.DisableApplicationFederatedCredentialResponse:
        """
        @summary 禁用应用联邦凭证
        
        @param request: DisableApplicationFederatedCredentialRequest
        @return: DisableApplicationFederatedCredentialResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_application_federated_credential_with_options_async(request, runtime)

    def disable_application_provisioning_with_options(
        self,
        request: eiam_20211201_models.DisableApplicationProvisioningRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DisableApplicationProvisioningResponse:
        """
        @summary Disables the account synchronization feature for an application in Identity as a Service (IDaaS) Employee IAM (EIAM).
        
        @param request: DisableApplicationProvisioningRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableApplicationProvisioningResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableApplicationProvisioning',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DisableApplicationProvisioningResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_application_provisioning_with_options_async(
        self,
        request: eiam_20211201_models.DisableApplicationProvisioningRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DisableApplicationProvisioningResponse:
        """
        @summary Disables the account synchronization feature for an application in Identity as a Service (IDaaS) Employee IAM (EIAM).
        
        @param request: DisableApplicationProvisioningRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableApplicationProvisioningResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableApplicationProvisioning',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DisableApplicationProvisioningResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_application_provisioning(
        self,
        request: eiam_20211201_models.DisableApplicationProvisioningRequest,
    ) -> eiam_20211201_models.DisableApplicationProvisioningResponse:
        """
        @summary Disables the account synchronization feature for an application in Identity as a Service (IDaaS) Employee IAM (EIAM).
        
        @param request: DisableApplicationProvisioningRequest
        @return: DisableApplicationProvisioningResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_application_provisioning_with_options(request, runtime)

    async def disable_application_provisioning_async(
        self,
        request: eiam_20211201_models.DisableApplicationProvisioningRequest,
    ) -> eiam_20211201_models.DisableApplicationProvisioningResponse:
        """
        @summary Disables the account synchronization feature for an application in Identity as a Service (IDaaS) Employee IAM (EIAM).
        
        @param request: DisableApplicationProvisioningRequest
        @return: DisableApplicationProvisioningResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_application_provisioning_with_options_async(request, runtime)

    def disable_application_sso_with_options(
        self,
        request: eiam_20211201_models.DisableApplicationSsoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DisableApplicationSsoResponse:
        """
        @summary Disables the single sign-on (SSO) feature for an Employee Identity and Access Management (EIAM) application. This way, employees cannot log on to the application by using SSO.
        
        @param request: DisableApplicationSsoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableApplicationSsoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableApplicationSso',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DisableApplicationSsoResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_application_sso_with_options_async(
        self,
        request: eiam_20211201_models.DisableApplicationSsoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DisableApplicationSsoResponse:
        """
        @summary Disables the single sign-on (SSO) feature for an Employee Identity and Access Management (EIAM) application. This way, employees cannot log on to the application by using SSO.
        
        @param request: DisableApplicationSsoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableApplicationSsoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableApplicationSso',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DisableApplicationSsoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_application_sso(
        self,
        request: eiam_20211201_models.DisableApplicationSsoRequest,
    ) -> eiam_20211201_models.DisableApplicationSsoResponse:
        """
        @summary Disables the single sign-on (SSO) feature for an Employee Identity and Access Management (EIAM) application. This way, employees cannot log on to the application by using SSO.
        
        @param request: DisableApplicationSsoRequest
        @return: DisableApplicationSsoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_application_sso_with_options(request, runtime)

    async def disable_application_sso_async(
        self,
        request: eiam_20211201_models.DisableApplicationSsoRequest,
    ) -> eiam_20211201_models.DisableApplicationSsoResponse:
        """
        @summary Disables the single sign-on (SSO) feature for an Employee Identity and Access Management (EIAM) application. This way, employees cannot log on to the application by using SSO.
        
        @param request: DisableApplicationSsoRequest
        @return: DisableApplicationSsoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_application_sso_with_options_async(request, runtime)

    def disable_application_token_with_options(
        self,
        request: eiam_20211201_models.DisableApplicationTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DisableApplicationTokenResponse:
        """
        @summary 禁用应用Token
        
        @param request: DisableApplicationTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableApplicationTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.application_token_id):
            query['ApplicationTokenId'] = request.application_token_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableApplicationToken',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DisableApplicationTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_application_token_with_options_async(
        self,
        request: eiam_20211201_models.DisableApplicationTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DisableApplicationTokenResponse:
        """
        @summary 禁用应用Token
        
        @param request: DisableApplicationTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableApplicationTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.application_token_id):
            query['ApplicationTokenId'] = request.application_token_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableApplicationToken',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DisableApplicationTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_application_token(
        self,
        request: eiam_20211201_models.DisableApplicationTokenRequest,
    ) -> eiam_20211201_models.DisableApplicationTokenResponse:
        """
        @summary 禁用应用Token
        
        @param request: DisableApplicationTokenRequest
        @return: DisableApplicationTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_application_token_with_options(request, runtime)

    async def disable_application_token_async(
        self,
        request: eiam_20211201_models.DisableApplicationTokenRequest,
    ) -> eiam_20211201_models.DisableApplicationTokenResponse:
        """
        @summary 禁用应用Token
        
        @param request: DisableApplicationTokenRequest
        @return: DisableApplicationTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_application_token_with_options_async(request, runtime)

    def disable_brand_with_options(
        self,
        request: eiam_20211201_models.DisableBrandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DisableBrandResponse:
        """
        @summary 禁用品牌
        
        @param request: DisableBrandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableBrandResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.brand_id):
            query['BrandId'] = request.brand_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableBrand',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DisableBrandResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_brand_with_options_async(
        self,
        request: eiam_20211201_models.DisableBrandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DisableBrandResponse:
        """
        @summary 禁用品牌
        
        @param request: DisableBrandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableBrandResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.brand_id):
            query['BrandId'] = request.brand_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableBrand',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DisableBrandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_brand(
        self,
        request: eiam_20211201_models.DisableBrandRequest,
    ) -> eiam_20211201_models.DisableBrandResponse:
        """
        @summary 禁用品牌
        
        @param request: DisableBrandRequest
        @return: DisableBrandResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_brand_with_options(request, runtime)

    async def disable_brand_async(
        self,
        request: eiam_20211201_models.DisableBrandRequest,
    ) -> eiam_20211201_models.DisableBrandResponse:
        """
        @summary 禁用品牌
        
        @param request: DisableBrandRequest
        @return: DisableBrandResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_brand_with_options_async(request, runtime)

    def disable_conditional_access_policy_with_options(
        self,
        request: eiam_20211201_models.DisableConditionalAccessPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DisableConditionalAccessPolicyResponse:
        """
        @summary Disable Conditional Access Policy
        
        @description When changing a conditional access policy from an enabled state to a disabled state, the policy will no longer intercept. Please confirm that you are aware of the potential risks associated with this action.
        
        @param request: DisableConditionalAccessPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableConditionalAccessPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.conditional_access_policy_id):
            query['ConditionalAccessPolicyId'] = request.conditional_access_policy_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableConditionalAccessPolicy',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DisableConditionalAccessPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_conditional_access_policy_with_options_async(
        self,
        request: eiam_20211201_models.DisableConditionalAccessPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DisableConditionalAccessPolicyResponse:
        """
        @summary Disable Conditional Access Policy
        
        @description When changing a conditional access policy from an enabled state to a disabled state, the policy will no longer intercept. Please confirm that you are aware of the potential risks associated with this action.
        
        @param request: DisableConditionalAccessPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableConditionalAccessPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.conditional_access_policy_id):
            query['ConditionalAccessPolicyId'] = request.conditional_access_policy_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableConditionalAccessPolicy',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DisableConditionalAccessPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_conditional_access_policy(
        self,
        request: eiam_20211201_models.DisableConditionalAccessPolicyRequest,
    ) -> eiam_20211201_models.DisableConditionalAccessPolicyResponse:
        """
        @summary Disable Conditional Access Policy
        
        @description When changing a conditional access policy from an enabled state to a disabled state, the policy will no longer intercept. Please confirm that you are aware of the potential risks associated with this action.
        
        @param request: DisableConditionalAccessPolicyRequest
        @return: DisableConditionalAccessPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_conditional_access_policy_with_options(request, runtime)

    async def disable_conditional_access_policy_async(
        self,
        request: eiam_20211201_models.DisableConditionalAccessPolicyRequest,
    ) -> eiam_20211201_models.DisableConditionalAccessPolicyResponse:
        """
        @summary Disable Conditional Access Policy
        
        @description When changing a conditional access policy from an enabled state to a disabled state, the policy will no longer intercept. Please confirm that you are aware of the potential risks associated with this action.
        
        @param request: DisableConditionalAccessPolicyRequest
        @return: DisableConditionalAccessPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_conditional_access_policy_with_options_async(request, runtime)

    def disable_custom_privacy_policy_with_options(
        self,
        request: eiam_20211201_models.DisableCustomPrivacyPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DisableCustomPrivacyPolicyResponse:
        """
        @summary 禁用自定义条款
        
        @param request: DisableCustomPrivacyPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableCustomPrivacyPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_privacy_policy_id):
            query['CustomPrivacyPolicyId'] = request.custom_privacy_policy_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableCustomPrivacyPolicy',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DisableCustomPrivacyPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_custom_privacy_policy_with_options_async(
        self,
        request: eiam_20211201_models.DisableCustomPrivacyPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DisableCustomPrivacyPolicyResponse:
        """
        @summary 禁用自定义条款
        
        @param request: DisableCustomPrivacyPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableCustomPrivacyPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_privacy_policy_id):
            query['CustomPrivacyPolicyId'] = request.custom_privacy_policy_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableCustomPrivacyPolicy',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DisableCustomPrivacyPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_custom_privacy_policy(
        self,
        request: eiam_20211201_models.DisableCustomPrivacyPolicyRequest,
    ) -> eiam_20211201_models.DisableCustomPrivacyPolicyResponse:
        """
        @summary 禁用自定义条款
        
        @param request: DisableCustomPrivacyPolicyRequest
        @return: DisableCustomPrivacyPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_custom_privacy_policy_with_options(request, runtime)

    async def disable_custom_privacy_policy_async(
        self,
        request: eiam_20211201_models.DisableCustomPrivacyPolicyRequest,
    ) -> eiam_20211201_models.DisableCustomPrivacyPolicyResponse:
        """
        @summary 禁用自定义条款
        
        @param request: DisableCustomPrivacyPolicyRequest
        @return: DisableCustomPrivacyPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_custom_privacy_policy_with_options_async(request, runtime)

    def disable_domain_proxy_token_with_options(
        self,
        request: eiam_20211201_models.DisableDomainProxyTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DisableDomainProxyTokenResponse:
        """
        @summary Disables a proxy token for a domain name of an Employee Identity and Access Management (EIAM) instance. After the proxy token is disabled, the domain name may not be used as expected.
        
        @param request: DisableDomainProxyTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableDomainProxyTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.domain_proxy_token_id):
            query['DomainProxyTokenId'] = request.domain_proxy_token_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableDomainProxyToken',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DisableDomainProxyTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_domain_proxy_token_with_options_async(
        self,
        request: eiam_20211201_models.DisableDomainProxyTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DisableDomainProxyTokenResponse:
        """
        @summary Disables a proxy token for a domain name of an Employee Identity and Access Management (EIAM) instance. After the proxy token is disabled, the domain name may not be used as expected.
        
        @param request: DisableDomainProxyTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableDomainProxyTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.domain_proxy_token_id):
            query['DomainProxyTokenId'] = request.domain_proxy_token_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableDomainProxyToken',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DisableDomainProxyTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_domain_proxy_token(
        self,
        request: eiam_20211201_models.DisableDomainProxyTokenRequest,
    ) -> eiam_20211201_models.DisableDomainProxyTokenResponse:
        """
        @summary Disables a proxy token for a domain name of an Employee Identity and Access Management (EIAM) instance. After the proxy token is disabled, the domain name may not be used as expected.
        
        @param request: DisableDomainProxyTokenRequest
        @return: DisableDomainProxyTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_domain_proxy_token_with_options(request, runtime)

    async def disable_domain_proxy_token_async(
        self,
        request: eiam_20211201_models.DisableDomainProxyTokenRequest,
    ) -> eiam_20211201_models.DisableDomainProxyTokenResponse:
        """
        @summary Disables a proxy token for a domain name of an Employee Identity and Access Management (EIAM) instance. After the proxy token is disabled, the domain name may not be used as expected.
        
        @param request: DisableDomainProxyTokenRequest
        @return: DisableDomainProxyTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_domain_proxy_token_with_options_async(request, runtime)

    def disable_federated_credential_provider_with_options(
        self,
        request: eiam_20211201_models.DisableFederatedCredentialProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DisableFederatedCredentialProviderResponse:
        """
        @summary 禁用联邦凭证提供方
        
        @param request: DisableFederatedCredentialProviderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableFederatedCredentialProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.federated_credential_provider_id):
            query['FederatedCredentialProviderId'] = request.federated_credential_provider_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableFederatedCredentialProvider',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DisableFederatedCredentialProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_federated_credential_provider_with_options_async(
        self,
        request: eiam_20211201_models.DisableFederatedCredentialProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DisableFederatedCredentialProviderResponse:
        """
        @summary 禁用联邦凭证提供方
        
        @param request: DisableFederatedCredentialProviderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableFederatedCredentialProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.federated_credential_provider_id):
            query['FederatedCredentialProviderId'] = request.federated_credential_provider_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableFederatedCredentialProvider',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DisableFederatedCredentialProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_federated_credential_provider(
        self,
        request: eiam_20211201_models.DisableFederatedCredentialProviderRequest,
    ) -> eiam_20211201_models.DisableFederatedCredentialProviderResponse:
        """
        @summary 禁用联邦凭证提供方
        
        @param request: DisableFederatedCredentialProviderRequest
        @return: DisableFederatedCredentialProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_federated_credential_provider_with_options(request, runtime)

    async def disable_federated_credential_provider_async(
        self,
        request: eiam_20211201_models.DisableFederatedCredentialProviderRequest,
    ) -> eiam_20211201_models.DisableFederatedCredentialProviderResponse:
        """
        @summary 禁用联邦凭证提供方
        
        @param request: DisableFederatedCredentialProviderRequest
        @return: DisableFederatedCredentialProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_federated_credential_provider_with_options_async(request, runtime)

    def disable_identity_provider_authn_with_options(
        self,
        request: eiam_20211201_models.DisableIdentityProviderAuthnRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DisableIdentityProviderAuthnResponse:
        """
        @summary 禁用认证
        
        @param request: DisableIdentityProviderAuthnRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableIdentityProviderAuthnResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identity_provider_id):
            query['IdentityProviderId'] = request.identity_provider_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableIdentityProviderAuthn',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DisableIdentityProviderAuthnResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_identity_provider_authn_with_options_async(
        self,
        request: eiam_20211201_models.DisableIdentityProviderAuthnRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DisableIdentityProviderAuthnResponse:
        """
        @summary 禁用认证
        
        @param request: DisableIdentityProviderAuthnRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableIdentityProviderAuthnResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identity_provider_id):
            query['IdentityProviderId'] = request.identity_provider_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableIdentityProviderAuthn',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DisableIdentityProviderAuthnResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_identity_provider_authn(
        self,
        request: eiam_20211201_models.DisableIdentityProviderAuthnRequest,
    ) -> eiam_20211201_models.DisableIdentityProviderAuthnResponse:
        """
        @summary 禁用认证
        
        @param request: DisableIdentityProviderAuthnRequest
        @return: DisableIdentityProviderAuthnResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_identity_provider_authn_with_options(request, runtime)

    async def disable_identity_provider_authn_async(
        self,
        request: eiam_20211201_models.DisableIdentityProviderAuthnRequest,
    ) -> eiam_20211201_models.DisableIdentityProviderAuthnResponse:
        """
        @summary 禁用认证
        
        @param request: DisableIdentityProviderAuthnRequest
        @return: DisableIdentityProviderAuthnResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_identity_provider_authn_with_options_async(request, runtime)

    def disable_identity_provider_ud_pull_with_options(
        self,
        request: eiam_20211201_models.DisableIdentityProviderUdPullRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DisableIdentityProviderUdPullResponse:
        """
        @summary Disable identity provider synchronization
        
        @param request: DisableIdentityProviderUdPullRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableIdentityProviderUdPullResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identity_provider_id):
            query['IdentityProviderId'] = request.identity_provider_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableIdentityProviderUdPull',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DisableIdentityProviderUdPullResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_identity_provider_ud_pull_with_options_async(
        self,
        request: eiam_20211201_models.DisableIdentityProviderUdPullRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DisableIdentityProviderUdPullResponse:
        """
        @summary Disable identity provider synchronization
        
        @param request: DisableIdentityProviderUdPullRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableIdentityProviderUdPullResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identity_provider_id):
            query['IdentityProviderId'] = request.identity_provider_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableIdentityProviderUdPull',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DisableIdentityProviderUdPullResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_identity_provider_ud_pull(
        self,
        request: eiam_20211201_models.DisableIdentityProviderUdPullRequest,
    ) -> eiam_20211201_models.DisableIdentityProviderUdPullResponse:
        """
        @summary Disable identity provider synchronization
        
        @param request: DisableIdentityProviderUdPullRequest
        @return: DisableIdentityProviderUdPullResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_identity_provider_ud_pull_with_options(request, runtime)

    async def disable_identity_provider_ud_pull_async(
        self,
        request: eiam_20211201_models.DisableIdentityProviderUdPullRequest,
    ) -> eiam_20211201_models.DisableIdentityProviderUdPullResponse:
        """
        @summary Disable identity provider synchronization
        
        @param request: DisableIdentityProviderUdPullRequest
        @return: DisableIdentityProviderUdPullResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_identity_provider_ud_pull_with_options_async(request, runtime)

    def disable_init_domain_auto_redirect_with_options(
        self,
        request: eiam_20211201_models.DisableInitDomainAutoRedirectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DisableInitDomainAutoRedirectResponse:
        """
        @summary Disables the feature of automatically redirecting the initial domain name to the default domain name for an Employee Identity and Access Management (EIAM) instance. After the feature is disabled, users who visit the portal page by using the initial domain name are not redirected to the default domain name.
        
        @param request: DisableInitDomainAutoRedirectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableInitDomainAutoRedirectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableInitDomainAutoRedirect',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DisableInitDomainAutoRedirectResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_init_domain_auto_redirect_with_options_async(
        self,
        request: eiam_20211201_models.DisableInitDomainAutoRedirectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DisableInitDomainAutoRedirectResponse:
        """
        @summary Disables the feature of automatically redirecting the initial domain name to the default domain name for an Employee Identity and Access Management (EIAM) instance. After the feature is disabled, users who visit the portal page by using the initial domain name are not redirected to the default domain name.
        
        @param request: DisableInitDomainAutoRedirectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableInitDomainAutoRedirectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableInitDomainAutoRedirect',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DisableInitDomainAutoRedirectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_init_domain_auto_redirect(
        self,
        request: eiam_20211201_models.DisableInitDomainAutoRedirectRequest,
    ) -> eiam_20211201_models.DisableInitDomainAutoRedirectResponse:
        """
        @summary Disables the feature of automatically redirecting the initial domain name to the default domain name for an Employee Identity and Access Management (EIAM) instance. After the feature is disabled, users who visit the portal page by using the initial domain name are not redirected to the default domain name.
        
        @param request: DisableInitDomainAutoRedirectRequest
        @return: DisableInitDomainAutoRedirectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_init_domain_auto_redirect_with_options(request, runtime)

    async def disable_init_domain_auto_redirect_async(
        self,
        request: eiam_20211201_models.DisableInitDomainAutoRedirectRequest,
    ) -> eiam_20211201_models.DisableInitDomainAutoRedirectResponse:
        """
        @summary Disables the feature of automatically redirecting the initial domain name to the default domain name for an Employee Identity and Access Management (EIAM) instance. After the feature is disabled, users who visit the portal page by using the initial domain name are not redirected to the default domain name.
        
        @param request: DisableInitDomainAutoRedirectRequest
        @return: DisableInitDomainAutoRedirectResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_init_domain_auto_redirect_with_options_async(request, runtime)

    def disable_user_with_options(
        self,
        request: eiam_20211201_models.DisableUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DisableUserResponse:
        """
        @summary Disables an Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM) account. If the account is disabled, a success message is returned.
        
        @param request: DisableUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableUser',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DisableUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_user_with_options_async(
        self,
        request: eiam_20211201_models.DisableUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.DisableUserResponse:
        """
        @summary Disables an Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM) account. If the account is disabled, a success message is returned.
        
        @param request: DisableUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableUser',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.DisableUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_user(
        self,
        request: eiam_20211201_models.DisableUserRequest,
    ) -> eiam_20211201_models.DisableUserResponse:
        """
        @summary Disables an Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM) account. If the account is disabled, a success message is returned.
        
        @param request: DisableUserRequest
        @return: DisableUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_user_with_options(request, runtime)

    async def disable_user_async(
        self,
        request: eiam_20211201_models.DisableUserRequest,
    ) -> eiam_20211201_models.DisableUserResponse:
        """
        @summary Disables an Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM) account. If the account is disabled, a success message is returned.
        
        @param request: DisableUserRequest
        @return: DisableUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_user_with_options_async(request, runtime)

    def enable_application_with_options(
        self,
        request: eiam_20211201_models.EnableApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.EnableApplicationResponse:
        """
        @summary Enables a disabled Employee Identity and Access Management (EIAM) application.
        
        @param request: EnableApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableApplication',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.EnableApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_application_with_options_async(
        self,
        request: eiam_20211201_models.EnableApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.EnableApplicationResponse:
        """
        @summary Enables a disabled Employee Identity and Access Management (EIAM) application.
        
        @param request: EnableApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableApplication',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.EnableApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_application(
        self,
        request: eiam_20211201_models.EnableApplicationRequest,
    ) -> eiam_20211201_models.EnableApplicationResponse:
        """
        @summary Enables a disabled Employee Identity and Access Management (EIAM) application.
        
        @param request: EnableApplicationRequest
        @return: EnableApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_application_with_options(request, runtime)

    async def enable_application_async(
        self,
        request: eiam_20211201_models.EnableApplicationRequest,
    ) -> eiam_20211201_models.EnableApplicationResponse:
        """
        @summary Enables a disabled Employee Identity and Access Management (EIAM) application.
        
        @param request: EnableApplicationRequest
        @return: EnableApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_application_with_options_async(request, runtime)

    def enable_application_api_invoke_with_options(
        self,
        request: eiam_20211201_models.EnableApplicationApiInvokeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.EnableApplicationApiInvokeResponse:
        """
        @summary Enables the Developer API feature for an Employee Identity and Access Management (EIAM) application.
        
        @param request: EnableApplicationApiInvokeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableApplicationApiInvokeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableApplicationApiInvoke',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.EnableApplicationApiInvokeResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_application_api_invoke_with_options_async(
        self,
        request: eiam_20211201_models.EnableApplicationApiInvokeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.EnableApplicationApiInvokeResponse:
        """
        @summary Enables the Developer API feature for an Employee Identity and Access Management (EIAM) application.
        
        @param request: EnableApplicationApiInvokeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableApplicationApiInvokeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableApplicationApiInvoke',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.EnableApplicationApiInvokeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_application_api_invoke(
        self,
        request: eiam_20211201_models.EnableApplicationApiInvokeRequest,
    ) -> eiam_20211201_models.EnableApplicationApiInvokeResponse:
        """
        @summary Enables the Developer API feature for an Employee Identity and Access Management (EIAM) application.
        
        @param request: EnableApplicationApiInvokeRequest
        @return: EnableApplicationApiInvokeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_application_api_invoke_with_options(request, runtime)

    async def enable_application_api_invoke_async(
        self,
        request: eiam_20211201_models.EnableApplicationApiInvokeRequest,
    ) -> eiam_20211201_models.EnableApplicationApiInvokeResponse:
        """
        @summary Enables the Developer API feature for an Employee Identity and Access Management (EIAM) application.
        
        @param request: EnableApplicationApiInvokeRequest
        @return: EnableApplicationApiInvokeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_application_api_invoke_with_options_async(request, runtime)

    def enable_application_client_secret_with_options(
        self,
        request: eiam_20211201_models.EnableApplicationClientSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.EnableApplicationClientSecretResponse:
        """
        @summary Enables the client key of an application in Identity as a Service (IDaaS) Employee IAM (EIAM).
        
        @param request: EnableApplicationClientSecretRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableApplicationClientSecretResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.secret_id):
            query['SecretId'] = request.secret_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableApplicationClientSecret',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.EnableApplicationClientSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_application_client_secret_with_options_async(
        self,
        request: eiam_20211201_models.EnableApplicationClientSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.EnableApplicationClientSecretResponse:
        """
        @summary Enables the client key of an application in Identity as a Service (IDaaS) Employee IAM (EIAM).
        
        @param request: EnableApplicationClientSecretRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableApplicationClientSecretResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.secret_id):
            query['SecretId'] = request.secret_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableApplicationClientSecret',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.EnableApplicationClientSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_application_client_secret(
        self,
        request: eiam_20211201_models.EnableApplicationClientSecretRequest,
    ) -> eiam_20211201_models.EnableApplicationClientSecretResponse:
        """
        @summary Enables the client key of an application in Identity as a Service (IDaaS) Employee IAM (EIAM).
        
        @param request: EnableApplicationClientSecretRequest
        @return: EnableApplicationClientSecretResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_application_client_secret_with_options(request, runtime)

    async def enable_application_client_secret_async(
        self,
        request: eiam_20211201_models.EnableApplicationClientSecretRequest,
    ) -> eiam_20211201_models.EnableApplicationClientSecretResponse:
        """
        @summary Enables the client key of an application in Identity as a Service (IDaaS) Employee IAM (EIAM).
        
        @param request: EnableApplicationClientSecretRequest
        @return: EnableApplicationClientSecretResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_application_client_secret_with_options_async(request, runtime)

    def enable_application_federated_credential_with_options(
        self,
        request: eiam_20211201_models.EnableApplicationFederatedCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.EnableApplicationFederatedCredentialResponse:
        """
        @summary 启用应用联邦凭证
        
        @param request: EnableApplicationFederatedCredentialRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableApplicationFederatedCredentialResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_federated_credential_id):
            query['ApplicationFederatedCredentialId'] = request.application_federated_credential_id
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableApplicationFederatedCredential',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.EnableApplicationFederatedCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_application_federated_credential_with_options_async(
        self,
        request: eiam_20211201_models.EnableApplicationFederatedCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.EnableApplicationFederatedCredentialResponse:
        """
        @summary 启用应用联邦凭证
        
        @param request: EnableApplicationFederatedCredentialRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableApplicationFederatedCredentialResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_federated_credential_id):
            query['ApplicationFederatedCredentialId'] = request.application_federated_credential_id
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableApplicationFederatedCredential',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.EnableApplicationFederatedCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_application_federated_credential(
        self,
        request: eiam_20211201_models.EnableApplicationFederatedCredentialRequest,
    ) -> eiam_20211201_models.EnableApplicationFederatedCredentialResponse:
        """
        @summary 启用应用联邦凭证
        
        @param request: EnableApplicationFederatedCredentialRequest
        @return: EnableApplicationFederatedCredentialResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_application_federated_credential_with_options(request, runtime)

    async def enable_application_federated_credential_async(
        self,
        request: eiam_20211201_models.EnableApplicationFederatedCredentialRequest,
    ) -> eiam_20211201_models.EnableApplicationFederatedCredentialResponse:
        """
        @summary 启用应用联邦凭证
        
        @param request: EnableApplicationFederatedCredentialRequest
        @return: EnableApplicationFederatedCredentialResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_application_federated_credential_with_options_async(request, runtime)

    def enable_application_provisioning_with_options(
        self,
        request: eiam_20211201_models.EnableApplicationProvisioningRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.EnableApplicationProvisioningResponse:
        """
        @summary Enables the account synchronization feature for an application in Identity as a Service (IDaaS) Employee IAM (EIAM).
        
        @param request: EnableApplicationProvisioningRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableApplicationProvisioningResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableApplicationProvisioning',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.EnableApplicationProvisioningResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_application_provisioning_with_options_async(
        self,
        request: eiam_20211201_models.EnableApplicationProvisioningRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.EnableApplicationProvisioningResponse:
        """
        @summary Enables the account synchronization feature for an application in Identity as a Service (IDaaS) Employee IAM (EIAM).
        
        @param request: EnableApplicationProvisioningRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableApplicationProvisioningResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableApplicationProvisioning',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.EnableApplicationProvisioningResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_application_provisioning(
        self,
        request: eiam_20211201_models.EnableApplicationProvisioningRequest,
    ) -> eiam_20211201_models.EnableApplicationProvisioningResponse:
        """
        @summary Enables the account synchronization feature for an application in Identity as a Service (IDaaS) Employee IAM (EIAM).
        
        @param request: EnableApplicationProvisioningRequest
        @return: EnableApplicationProvisioningResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_application_provisioning_with_options(request, runtime)

    async def enable_application_provisioning_async(
        self,
        request: eiam_20211201_models.EnableApplicationProvisioningRequest,
    ) -> eiam_20211201_models.EnableApplicationProvisioningResponse:
        """
        @summary Enables the account synchronization feature for an application in Identity as a Service (IDaaS) Employee IAM (EIAM).
        
        @param request: EnableApplicationProvisioningRequest
        @return: EnableApplicationProvisioningResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_application_provisioning_with_options_async(request, runtime)

    def enable_application_sso_with_options(
        self,
        request: eiam_20211201_models.EnableApplicationSsoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.EnableApplicationSsoResponse:
        """
        @summary Enables the single sign-on (SSO) feature for an Employee Identity and Access Management (EIAM) application.
        
        @param request: EnableApplicationSsoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableApplicationSsoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableApplicationSso',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.EnableApplicationSsoResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_application_sso_with_options_async(
        self,
        request: eiam_20211201_models.EnableApplicationSsoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.EnableApplicationSsoResponse:
        """
        @summary Enables the single sign-on (SSO) feature for an Employee Identity and Access Management (EIAM) application.
        
        @param request: EnableApplicationSsoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableApplicationSsoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableApplicationSso',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.EnableApplicationSsoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_application_sso(
        self,
        request: eiam_20211201_models.EnableApplicationSsoRequest,
    ) -> eiam_20211201_models.EnableApplicationSsoResponse:
        """
        @summary Enables the single sign-on (SSO) feature for an Employee Identity and Access Management (EIAM) application.
        
        @param request: EnableApplicationSsoRequest
        @return: EnableApplicationSsoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_application_sso_with_options(request, runtime)

    async def enable_application_sso_async(
        self,
        request: eiam_20211201_models.EnableApplicationSsoRequest,
    ) -> eiam_20211201_models.EnableApplicationSsoResponse:
        """
        @summary Enables the single sign-on (SSO) feature for an Employee Identity and Access Management (EIAM) application.
        
        @param request: EnableApplicationSsoRequest
        @return: EnableApplicationSsoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_application_sso_with_options_async(request, runtime)

    def enable_application_token_with_options(
        self,
        request: eiam_20211201_models.EnableApplicationTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.EnableApplicationTokenResponse:
        """
        @summary 启用应用Token
        
        @param request: EnableApplicationTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableApplicationTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.application_token_id):
            query['ApplicationTokenId'] = request.application_token_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableApplicationToken',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.EnableApplicationTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_application_token_with_options_async(
        self,
        request: eiam_20211201_models.EnableApplicationTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.EnableApplicationTokenResponse:
        """
        @summary 启用应用Token
        
        @param request: EnableApplicationTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableApplicationTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.application_token_id):
            query['ApplicationTokenId'] = request.application_token_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableApplicationToken',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.EnableApplicationTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_application_token(
        self,
        request: eiam_20211201_models.EnableApplicationTokenRequest,
    ) -> eiam_20211201_models.EnableApplicationTokenResponse:
        """
        @summary 启用应用Token
        
        @param request: EnableApplicationTokenRequest
        @return: EnableApplicationTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_application_token_with_options(request, runtime)

    async def enable_application_token_async(
        self,
        request: eiam_20211201_models.EnableApplicationTokenRequest,
    ) -> eiam_20211201_models.EnableApplicationTokenResponse:
        """
        @summary 启用应用Token
        
        @param request: EnableApplicationTokenRequest
        @return: EnableApplicationTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_application_token_with_options_async(request, runtime)

    def enable_brand_with_options(
        self,
        request: eiam_20211201_models.EnableBrandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.EnableBrandResponse:
        """
        @summary 启用品牌
        
        @param request: EnableBrandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableBrandResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.brand_id):
            query['BrandId'] = request.brand_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableBrand',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.EnableBrandResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_brand_with_options_async(
        self,
        request: eiam_20211201_models.EnableBrandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.EnableBrandResponse:
        """
        @summary 启用品牌
        
        @param request: EnableBrandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableBrandResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.brand_id):
            query['BrandId'] = request.brand_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableBrand',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.EnableBrandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_brand(
        self,
        request: eiam_20211201_models.EnableBrandRequest,
    ) -> eiam_20211201_models.EnableBrandResponse:
        """
        @summary 启用品牌
        
        @param request: EnableBrandRequest
        @return: EnableBrandResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_brand_with_options(request, runtime)

    async def enable_brand_async(
        self,
        request: eiam_20211201_models.EnableBrandRequest,
    ) -> eiam_20211201_models.EnableBrandResponse:
        """
        @summary 启用品牌
        
        @param request: EnableBrandRequest
        @return: EnableBrandResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_brand_with_options_async(request, runtime)

    def enable_conditional_access_policy_with_options(
        self,
        request: eiam_20211201_models.EnableConditionalAccessPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.EnableConditionalAccessPolicyResponse:
        """
        @summary Enable Conditional Access Policy
        
        @description When changing the status of a conditional access policy from enabled to disabled, the policy will no longer intercept. Please confirm that you are aware of the potential risks associated with this action.
        
        @param request: EnableConditionalAccessPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableConditionalAccessPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.conditional_access_policy_id):
            query['ConditionalAccessPolicyId'] = request.conditional_access_policy_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableConditionalAccessPolicy',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.EnableConditionalAccessPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_conditional_access_policy_with_options_async(
        self,
        request: eiam_20211201_models.EnableConditionalAccessPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.EnableConditionalAccessPolicyResponse:
        """
        @summary Enable Conditional Access Policy
        
        @description When changing the status of a conditional access policy from enabled to disabled, the policy will no longer intercept. Please confirm that you are aware of the potential risks associated with this action.
        
        @param request: EnableConditionalAccessPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableConditionalAccessPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.conditional_access_policy_id):
            query['ConditionalAccessPolicyId'] = request.conditional_access_policy_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableConditionalAccessPolicy',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.EnableConditionalAccessPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_conditional_access_policy(
        self,
        request: eiam_20211201_models.EnableConditionalAccessPolicyRequest,
    ) -> eiam_20211201_models.EnableConditionalAccessPolicyResponse:
        """
        @summary Enable Conditional Access Policy
        
        @description When changing the status of a conditional access policy from enabled to disabled, the policy will no longer intercept. Please confirm that you are aware of the potential risks associated with this action.
        
        @param request: EnableConditionalAccessPolicyRequest
        @return: EnableConditionalAccessPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_conditional_access_policy_with_options(request, runtime)

    async def enable_conditional_access_policy_async(
        self,
        request: eiam_20211201_models.EnableConditionalAccessPolicyRequest,
    ) -> eiam_20211201_models.EnableConditionalAccessPolicyResponse:
        """
        @summary Enable Conditional Access Policy
        
        @description When changing the status of a conditional access policy from enabled to disabled, the policy will no longer intercept. Please confirm that you are aware of the potential risks associated with this action.
        
        @param request: EnableConditionalAccessPolicyRequest
        @return: EnableConditionalAccessPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_conditional_access_policy_with_options_async(request, runtime)

    def enable_custom_privacy_policy_with_options(
        self,
        request: eiam_20211201_models.EnableCustomPrivacyPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.EnableCustomPrivacyPolicyResponse:
        """
        @summary 启用自定义条款
        
        @param request: EnableCustomPrivacyPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableCustomPrivacyPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_privacy_policy_id):
            query['CustomPrivacyPolicyId'] = request.custom_privacy_policy_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableCustomPrivacyPolicy',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.EnableCustomPrivacyPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_custom_privacy_policy_with_options_async(
        self,
        request: eiam_20211201_models.EnableCustomPrivacyPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.EnableCustomPrivacyPolicyResponse:
        """
        @summary 启用自定义条款
        
        @param request: EnableCustomPrivacyPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableCustomPrivacyPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_privacy_policy_id):
            query['CustomPrivacyPolicyId'] = request.custom_privacy_policy_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableCustomPrivacyPolicy',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.EnableCustomPrivacyPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_custom_privacy_policy(
        self,
        request: eiam_20211201_models.EnableCustomPrivacyPolicyRequest,
    ) -> eiam_20211201_models.EnableCustomPrivacyPolicyResponse:
        """
        @summary 启用自定义条款
        
        @param request: EnableCustomPrivacyPolicyRequest
        @return: EnableCustomPrivacyPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_custom_privacy_policy_with_options(request, runtime)

    async def enable_custom_privacy_policy_async(
        self,
        request: eiam_20211201_models.EnableCustomPrivacyPolicyRequest,
    ) -> eiam_20211201_models.EnableCustomPrivacyPolicyResponse:
        """
        @summary 启用自定义条款
        
        @param request: EnableCustomPrivacyPolicyRequest
        @return: EnableCustomPrivacyPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_custom_privacy_policy_with_options_async(request, runtime)

    def enable_domain_proxy_token_with_options(
        self,
        request: eiam_20211201_models.EnableDomainProxyTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.EnableDomainProxyTokenResponse:
        """
        @summary Enables a proxy token for a domain name of an Employee Identity and Access Management (EIAM) instance. The proxy token is used to verify the security of the domain name.
        
        @param request: EnableDomainProxyTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableDomainProxyTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.domain_proxy_token_id):
            query['DomainProxyTokenId'] = request.domain_proxy_token_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableDomainProxyToken',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.EnableDomainProxyTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_domain_proxy_token_with_options_async(
        self,
        request: eiam_20211201_models.EnableDomainProxyTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.EnableDomainProxyTokenResponse:
        """
        @summary Enables a proxy token for a domain name of an Employee Identity and Access Management (EIAM) instance. The proxy token is used to verify the security of the domain name.
        
        @param request: EnableDomainProxyTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableDomainProxyTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.domain_proxy_token_id):
            query['DomainProxyTokenId'] = request.domain_proxy_token_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableDomainProxyToken',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.EnableDomainProxyTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_domain_proxy_token(
        self,
        request: eiam_20211201_models.EnableDomainProxyTokenRequest,
    ) -> eiam_20211201_models.EnableDomainProxyTokenResponse:
        """
        @summary Enables a proxy token for a domain name of an Employee Identity and Access Management (EIAM) instance. The proxy token is used to verify the security of the domain name.
        
        @param request: EnableDomainProxyTokenRequest
        @return: EnableDomainProxyTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_domain_proxy_token_with_options(request, runtime)

    async def enable_domain_proxy_token_async(
        self,
        request: eiam_20211201_models.EnableDomainProxyTokenRequest,
    ) -> eiam_20211201_models.EnableDomainProxyTokenResponse:
        """
        @summary Enables a proxy token for a domain name of an Employee Identity and Access Management (EIAM) instance. The proxy token is used to verify the security of the domain name.
        
        @param request: EnableDomainProxyTokenRequest
        @return: EnableDomainProxyTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_domain_proxy_token_with_options_async(request, runtime)

    def enable_federated_credential_provider_with_options(
        self,
        request: eiam_20211201_models.EnableFederatedCredentialProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.EnableFederatedCredentialProviderResponse:
        """
        @summary 启用联邦凭证提供方
        
        @param request: EnableFederatedCredentialProviderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableFederatedCredentialProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.federated_credential_provider_id):
            query['FederatedCredentialProviderId'] = request.federated_credential_provider_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableFederatedCredentialProvider',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.EnableFederatedCredentialProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_federated_credential_provider_with_options_async(
        self,
        request: eiam_20211201_models.EnableFederatedCredentialProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.EnableFederatedCredentialProviderResponse:
        """
        @summary 启用联邦凭证提供方
        
        @param request: EnableFederatedCredentialProviderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableFederatedCredentialProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.federated_credential_provider_id):
            query['FederatedCredentialProviderId'] = request.federated_credential_provider_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableFederatedCredentialProvider',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.EnableFederatedCredentialProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_federated_credential_provider(
        self,
        request: eiam_20211201_models.EnableFederatedCredentialProviderRequest,
    ) -> eiam_20211201_models.EnableFederatedCredentialProviderResponse:
        """
        @summary 启用联邦凭证提供方
        
        @param request: EnableFederatedCredentialProviderRequest
        @return: EnableFederatedCredentialProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_federated_credential_provider_with_options(request, runtime)

    async def enable_federated_credential_provider_async(
        self,
        request: eiam_20211201_models.EnableFederatedCredentialProviderRequest,
    ) -> eiam_20211201_models.EnableFederatedCredentialProviderResponse:
        """
        @summary 启用联邦凭证提供方
        
        @param request: EnableFederatedCredentialProviderRequest
        @return: EnableFederatedCredentialProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_federated_credential_provider_with_options_async(request, runtime)

    def enable_identity_provider_authn_with_options(
        self,
        request: eiam_20211201_models.EnableIdentityProviderAuthnRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.EnableIdentityProviderAuthnResponse:
        """
        @summary 启用认证
        
        @param request: EnableIdentityProviderAuthnRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableIdentityProviderAuthnResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identity_provider_id):
            query['IdentityProviderId'] = request.identity_provider_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableIdentityProviderAuthn',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.EnableIdentityProviderAuthnResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_identity_provider_authn_with_options_async(
        self,
        request: eiam_20211201_models.EnableIdentityProviderAuthnRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.EnableIdentityProviderAuthnResponse:
        """
        @summary 启用认证
        
        @param request: EnableIdentityProviderAuthnRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableIdentityProviderAuthnResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identity_provider_id):
            query['IdentityProviderId'] = request.identity_provider_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableIdentityProviderAuthn',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.EnableIdentityProviderAuthnResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_identity_provider_authn(
        self,
        request: eiam_20211201_models.EnableIdentityProviderAuthnRequest,
    ) -> eiam_20211201_models.EnableIdentityProviderAuthnResponse:
        """
        @summary 启用认证
        
        @param request: EnableIdentityProviderAuthnRequest
        @return: EnableIdentityProviderAuthnResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_identity_provider_authn_with_options(request, runtime)

    async def enable_identity_provider_authn_async(
        self,
        request: eiam_20211201_models.EnableIdentityProviderAuthnRequest,
    ) -> eiam_20211201_models.EnableIdentityProviderAuthnResponse:
        """
        @summary 启用认证
        
        @param request: EnableIdentityProviderAuthnRequest
        @return: EnableIdentityProviderAuthnResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_identity_provider_authn_with_options_async(request, runtime)

    def enable_identity_provider_ud_pull_with_options(
        self,
        request: eiam_20211201_models.EnableIdentityProviderUdPullRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.EnableIdentityProviderUdPullResponse:
        """
        @summary Enable identity provider synchronization.
        
        @param request: EnableIdentityProviderUdPullRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableIdentityProviderUdPullResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identity_provider_id):
            query['IdentityProviderId'] = request.identity_provider_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableIdentityProviderUdPull',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.EnableIdentityProviderUdPullResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_identity_provider_ud_pull_with_options_async(
        self,
        request: eiam_20211201_models.EnableIdentityProviderUdPullRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.EnableIdentityProviderUdPullResponse:
        """
        @summary Enable identity provider synchronization.
        
        @param request: EnableIdentityProviderUdPullRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableIdentityProviderUdPullResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identity_provider_id):
            query['IdentityProviderId'] = request.identity_provider_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableIdentityProviderUdPull',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.EnableIdentityProviderUdPullResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_identity_provider_ud_pull(
        self,
        request: eiam_20211201_models.EnableIdentityProviderUdPullRequest,
    ) -> eiam_20211201_models.EnableIdentityProviderUdPullResponse:
        """
        @summary Enable identity provider synchronization.
        
        @param request: EnableIdentityProviderUdPullRequest
        @return: EnableIdentityProviderUdPullResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_identity_provider_ud_pull_with_options(request, runtime)

    async def enable_identity_provider_ud_pull_async(
        self,
        request: eiam_20211201_models.EnableIdentityProviderUdPullRequest,
    ) -> eiam_20211201_models.EnableIdentityProviderUdPullResponse:
        """
        @summary Enable identity provider synchronization.
        
        @param request: EnableIdentityProviderUdPullRequest
        @return: EnableIdentityProviderUdPullResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_identity_provider_ud_pull_with_options_async(request, runtime)

    def enable_init_domain_auto_redirect_with_options(
        self,
        request: eiam_20211201_models.EnableInitDomainAutoRedirectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.EnableInitDomainAutoRedirectResponse:
        """
        @summary Enables the feature of automatically redirecting the initial domain name to the default domain name for an Employee Identity and Access Management (EIAM) instance.
        
        @param request: EnableInitDomainAutoRedirectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableInitDomainAutoRedirectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableInitDomainAutoRedirect',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.EnableInitDomainAutoRedirectResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_init_domain_auto_redirect_with_options_async(
        self,
        request: eiam_20211201_models.EnableInitDomainAutoRedirectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.EnableInitDomainAutoRedirectResponse:
        """
        @summary Enables the feature of automatically redirecting the initial domain name to the default domain name for an Employee Identity and Access Management (EIAM) instance.
        
        @param request: EnableInitDomainAutoRedirectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableInitDomainAutoRedirectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableInitDomainAutoRedirect',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.EnableInitDomainAutoRedirectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_init_domain_auto_redirect(
        self,
        request: eiam_20211201_models.EnableInitDomainAutoRedirectRequest,
    ) -> eiam_20211201_models.EnableInitDomainAutoRedirectResponse:
        """
        @summary Enables the feature of automatically redirecting the initial domain name to the default domain name for an Employee Identity and Access Management (EIAM) instance.
        
        @param request: EnableInitDomainAutoRedirectRequest
        @return: EnableInitDomainAutoRedirectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_init_domain_auto_redirect_with_options(request, runtime)

    async def enable_init_domain_auto_redirect_async(
        self,
        request: eiam_20211201_models.EnableInitDomainAutoRedirectRequest,
    ) -> eiam_20211201_models.EnableInitDomainAutoRedirectResponse:
        """
        @summary Enables the feature of automatically redirecting the initial domain name to the default domain name for an Employee Identity and Access Management (EIAM) instance.
        
        @param request: EnableInitDomainAutoRedirectRequest
        @return: EnableInitDomainAutoRedirectResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_init_domain_auto_redirect_with_options_async(request, runtime)

    def enable_user_with_options(
        self,
        request: eiam_20211201_models.EnableUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.EnableUserResponse:
        """
        @summary Enables an Employee Identity and Access Management (EIAM) account of Identity as a Service (IDaaS).
        
        @param request: EnableUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableUser',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.EnableUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_user_with_options_async(
        self,
        request: eiam_20211201_models.EnableUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.EnableUserResponse:
        """
        @summary Enables an Employee Identity and Access Management (EIAM) account of Identity as a Service (IDaaS).
        
        @param request: EnableUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableUser',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.EnableUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_user(
        self,
        request: eiam_20211201_models.EnableUserRequest,
    ) -> eiam_20211201_models.EnableUserResponse:
        """
        @summary Enables an Employee Identity and Access Management (EIAM) account of Identity as a Service (IDaaS).
        
        @param request: EnableUserRequest
        @return: EnableUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_user_with_options(request, runtime)

    async def enable_user_async(
        self,
        request: eiam_20211201_models.EnableUserRequest,
    ) -> eiam_20211201_models.EnableUserResponse:
        """
        @summary Enables an Employee Identity and Access Management (EIAM) account of Identity as a Service (IDaaS).
        
        @param request: EnableUserRequest
        @return: EnableUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_user_with_options_async(request, runtime)

    def get_application_with_options(
        self,
        request: eiam_20211201_models.GetApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetApplicationResponse:
        """
        @summary Queries the details of an Employee Identity and Access Management (EIAM) application.
        
        @param request: GetApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApplication',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_application_with_options_async(
        self,
        request: eiam_20211201_models.GetApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetApplicationResponse:
        """
        @summary Queries the details of an Employee Identity and Access Management (EIAM) application.
        
        @param request: GetApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApplication',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_application(
        self,
        request: eiam_20211201_models.GetApplicationRequest,
    ) -> eiam_20211201_models.GetApplicationResponse:
        """
        @summary Queries the details of an Employee Identity and Access Management (EIAM) application.
        
        @param request: GetApplicationRequest
        @return: GetApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_application_with_options(request, runtime)

    async def get_application_async(
        self,
        request: eiam_20211201_models.GetApplicationRequest,
    ) -> eiam_20211201_models.GetApplicationResponse:
        """
        @summary Queries the details of an Employee Identity and Access Management (EIAM) application.
        
        @param request: GetApplicationRequest
        @return: GetApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_application_with_options_async(request, runtime)

    def get_application_federated_credential_with_options(
        self,
        request: eiam_20211201_models.GetApplicationFederatedCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetApplicationFederatedCredentialResponse:
        """
        @summary 获取应用联邦凭证
        
        @param request: GetApplicationFederatedCredentialRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetApplicationFederatedCredentialResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_federated_credential_id):
            query['ApplicationFederatedCredentialId'] = request.application_federated_credential_id
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApplicationFederatedCredential',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetApplicationFederatedCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_application_federated_credential_with_options_async(
        self,
        request: eiam_20211201_models.GetApplicationFederatedCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetApplicationFederatedCredentialResponse:
        """
        @summary 获取应用联邦凭证
        
        @param request: GetApplicationFederatedCredentialRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetApplicationFederatedCredentialResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_federated_credential_id):
            query['ApplicationFederatedCredentialId'] = request.application_federated_credential_id
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApplicationFederatedCredential',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetApplicationFederatedCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_application_federated_credential(
        self,
        request: eiam_20211201_models.GetApplicationFederatedCredentialRequest,
    ) -> eiam_20211201_models.GetApplicationFederatedCredentialResponse:
        """
        @summary 获取应用联邦凭证
        
        @param request: GetApplicationFederatedCredentialRequest
        @return: GetApplicationFederatedCredentialResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_application_federated_credential_with_options(request, runtime)

    async def get_application_federated_credential_async(
        self,
        request: eiam_20211201_models.GetApplicationFederatedCredentialRequest,
    ) -> eiam_20211201_models.GetApplicationFederatedCredentialResponse:
        """
        @summary 获取应用联邦凭证
        
        @param request: GetApplicationFederatedCredentialRequest
        @return: GetApplicationFederatedCredentialResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_application_federated_credential_with_options_async(request, runtime)

    def get_application_grant_scope_with_options(
        self,
        request: eiam_20211201_models.GetApplicationGrantScopeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetApplicationGrantScopeResponse:
        """
        @summary Queries the permissions of the Developer API feature for an Employee Identity and Access Management (EIAM) application.
        
        @param request: GetApplicationGrantScopeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetApplicationGrantScopeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApplicationGrantScope',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetApplicationGrantScopeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_application_grant_scope_with_options_async(
        self,
        request: eiam_20211201_models.GetApplicationGrantScopeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetApplicationGrantScopeResponse:
        """
        @summary Queries the permissions of the Developer API feature for an Employee Identity and Access Management (EIAM) application.
        
        @param request: GetApplicationGrantScopeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetApplicationGrantScopeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApplicationGrantScope',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetApplicationGrantScopeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_application_grant_scope(
        self,
        request: eiam_20211201_models.GetApplicationGrantScopeRequest,
    ) -> eiam_20211201_models.GetApplicationGrantScopeResponse:
        """
        @summary Queries the permissions of the Developer API feature for an Employee Identity and Access Management (EIAM) application.
        
        @param request: GetApplicationGrantScopeRequest
        @return: GetApplicationGrantScopeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_application_grant_scope_with_options(request, runtime)

    async def get_application_grant_scope_async(
        self,
        request: eiam_20211201_models.GetApplicationGrantScopeRequest,
    ) -> eiam_20211201_models.GetApplicationGrantScopeResponse:
        """
        @summary Queries the permissions of the Developer API feature for an Employee Identity and Access Management (EIAM) application.
        
        @param request: GetApplicationGrantScopeRequest
        @return: GetApplicationGrantScopeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_application_grant_scope_with_options_async(request, runtime)

    def get_application_provisioning_config_with_options(
        self,
        request: eiam_20211201_models.GetApplicationProvisioningConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetApplicationProvisioningConfigResponse:
        """
        @summary Queries the configuration of the account synchronization feature for an application in Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM).
        
        @param request: GetApplicationProvisioningConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetApplicationProvisioningConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApplicationProvisioningConfig',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetApplicationProvisioningConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_application_provisioning_config_with_options_async(
        self,
        request: eiam_20211201_models.GetApplicationProvisioningConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetApplicationProvisioningConfigResponse:
        """
        @summary Queries the configuration of the account synchronization feature for an application in Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM).
        
        @param request: GetApplicationProvisioningConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetApplicationProvisioningConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApplicationProvisioningConfig',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetApplicationProvisioningConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_application_provisioning_config(
        self,
        request: eiam_20211201_models.GetApplicationProvisioningConfigRequest,
    ) -> eiam_20211201_models.GetApplicationProvisioningConfigResponse:
        """
        @summary Queries the configuration of the account synchronization feature for an application in Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM).
        
        @param request: GetApplicationProvisioningConfigRequest
        @return: GetApplicationProvisioningConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_application_provisioning_config_with_options(request, runtime)

    async def get_application_provisioning_config_async(
        self,
        request: eiam_20211201_models.GetApplicationProvisioningConfigRequest,
    ) -> eiam_20211201_models.GetApplicationProvisioningConfigResponse:
        """
        @summary Queries the configuration of the account synchronization feature for an application in Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM).
        
        @param request: GetApplicationProvisioningConfigRequest
        @return: GetApplicationProvisioningConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_application_provisioning_config_with_options_async(request, runtime)

    def get_application_provisioning_scope_with_options(
        self,
        request: eiam_20211201_models.GetApplicationProvisioningScopeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetApplicationProvisioningScopeResponse:
        """
        @summary Queries the account synchronization scope of applications in Identity as a Service (IDaaS) Employee IAM (EIAM). This scope is the same as the scope within which developers can call the DeveloperAPI to query and manage accounts.
        
        @param request: GetApplicationProvisioningScopeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetApplicationProvisioningScopeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApplicationProvisioningScope',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetApplicationProvisioningScopeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_application_provisioning_scope_with_options_async(
        self,
        request: eiam_20211201_models.GetApplicationProvisioningScopeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetApplicationProvisioningScopeResponse:
        """
        @summary Queries the account synchronization scope of applications in Identity as a Service (IDaaS) Employee IAM (EIAM). This scope is the same as the scope within which developers can call the DeveloperAPI to query and manage accounts.
        
        @param request: GetApplicationProvisioningScopeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetApplicationProvisioningScopeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApplicationProvisioningScope',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetApplicationProvisioningScopeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_application_provisioning_scope(
        self,
        request: eiam_20211201_models.GetApplicationProvisioningScopeRequest,
    ) -> eiam_20211201_models.GetApplicationProvisioningScopeResponse:
        """
        @summary Queries the account synchronization scope of applications in Identity as a Service (IDaaS) Employee IAM (EIAM). This scope is the same as the scope within which developers can call the DeveloperAPI to query and manage accounts.
        
        @param request: GetApplicationProvisioningScopeRequest
        @return: GetApplicationProvisioningScopeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_application_provisioning_scope_with_options(request, runtime)

    async def get_application_provisioning_scope_async(
        self,
        request: eiam_20211201_models.GetApplicationProvisioningScopeRequest,
    ) -> eiam_20211201_models.GetApplicationProvisioningScopeResponse:
        """
        @summary Queries the account synchronization scope of applications in Identity as a Service (IDaaS) Employee IAM (EIAM). This scope is the same as the scope within which developers can call the DeveloperAPI to query and manage accounts.
        
        @param request: GetApplicationProvisioningScopeRequest
        @return: GetApplicationProvisioningScopeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_application_provisioning_scope_with_options_async(request, runtime)

    def get_application_sso_config_with_options(
        self,
        request: eiam_20211201_models.GetApplicationSsoConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetApplicationSsoConfigResponse:
        """
        @summary Queries the single sign-on (SSO) configuration attributes of an application in Identity as a Service (IDaaS) Employee IAM (EIAM).
        
        @param request: GetApplicationSsoConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetApplicationSsoConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApplicationSsoConfig',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetApplicationSsoConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_application_sso_config_with_options_async(
        self,
        request: eiam_20211201_models.GetApplicationSsoConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetApplicationSsoConfigResponse:
        """
        @summary Queries the single sign-on (SSO) configuration attributes of an application in Identity as a Service (IDaaS) Employee IAM (EIAM).
        
        @param request: GetApplicationSsoConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetApplicationSsoConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApplicationSsoConfig',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetApplicationSsoConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_application_sso_config(
        self,
        request: eiam_20211201_models.GetApplicationSsoConfigRequest,
    ) -> eiam_20211201_models.GetApplicationSsoConfigResponse:
        """
        @summary Queries the single sign-on (SSO) configuration attributes of an application in Identity as a Service (IDaaS) Employee IAM (EIAM).
        
        @param request: GetApplicationSsoConfigRequest
        @return: GetApplicationSsoConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_application_sso_config_with_options(request, runtime)

    async def get_application_sso_config_async(
        self,
        request: eiam_20211201_models.GetApplicationSsoConfigRequest,
    ) -> eiam_20211201_models.GetApplicationSsoConfigResponse:
        """
        @summary Queries the single sign-on (SSO) configuration attributes of an application in Identity as a Service (IDaaS) Employee IAM (EIAM).
        
        @param request: GetApplicationSsoConfigRequest
        @return: GetApplicationSsoConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_application_sso_config_with_options_async(request, runtime)

    def get_application_template_with_options(
        self,
        request: eiam_20211201_models.GetApplicationTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetApplicationTemplateResponse:
        """
        @summary 获取应用模板信息
        
        @param request: GetApplicationTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetApplicationTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_template_id):
            query['ApplicationTemplateId'] = request.application_template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApplicationTemplate',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetApplicationTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_application_template_with_options_async(
        self,
        request: eiam_20211201_models.GetApplicationTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetApplicationTemplateResponse:
        """
        @summary 获取应用模板信息
        
        @param request: GetApplicationTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetApplicationTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_template_id):
            query['ApplicationTemplateId'] = request.application_template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApplicationTemplate',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetApplicationTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_application_template(
        self,
        request: eiam_20211201_models.GetApplicationTemplateRequest,
    ) -> eiam_20211201_models.GetApplicationTemplateResponse:
        """
        @summary 获取应用模板信息
        
        @param request: GetApplicationTemplateRequest
        @return: GetApplicationTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_application_template_with_options(request, runtime)

    async def get_application_template_async(
        self,
        request: eiam_20211201_models.GetApplicationTemplateRequest,
    ) -> eiam_20211201_models.GetApplicationTemplateResponse:
        """
        @summary 获取应用模板信息
        
        @param request: GetApplicationTemplateRequest
        @return: GetApplicationTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_application_template_with_options_async(request, runtime)

    def get_brand_with_options(
        self,
        request: eiam_20211201_models.GetBrandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetBrandResponse:
        """
        @summary 获取品牌详情
        
        @param request: GetBrandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBrandResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.brand_id):
            query['BrandId'] = request.brand_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBrand',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetBrandResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_brand_with_options_async(
        self,
        request: eiam_20211201_models.GetBrandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetBrandResponse:
        """
        @summary 获取品牌详情
        
        @param request: GetBrandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBrandResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.brand_id):
            query['BrandId'] = request.brand_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBrand',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetBrandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_brand(
        self,
        request: eiam_20211201_models.GetBrandRequest,
    ) -> eiam_20211201_models.GetBrandResponse:
        """
        @summary 获取品牌详情
        
        @param request: GetBrandRequest
        @return: GetBrandResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_brand_with_options(request, runtime)

    async def get_brand_async(
        self,
        request: eiam_20211201_models.GetBrandRequest,
    ) -> eiam_20211201_models.GetBrandResponse:
        """
        @summary 获取品牌详情
        
        @param request: GetBrandRequest
        @return: GetBrandResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_brand_with_options_async(request, runtime)

    def get_conditional_access_policy_with_options(
        self,
        request: eiam_20211201_models.GetConditionalAccessPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetConditionalAccessPolicyResponse:
        """
        @summary Get Conditional Access Policy
        
        @description Query Conditional Access Policy
        
        @param request: GetConditionalAccessPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConditionalAccessPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.conditional_access_policy_id):
            query['ConditionalAccessPolicyId'] = request.conditional_access_policy_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConditionalAccessPolicy',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetConditionalAccessPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_conditional_access_policy_with_options_async(
        self,
        request: eiam_20211201_models.GetConditionalAccessPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetConditionalAccessPolicyResponse:
        """
        @summary Get Conditional Access Policy
        
        @description Query Conditional Access Policy
        
        @param request: GetConditionalAccessPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConditionalAccessPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.conditional_access_policy_id):
            query['ConditionalAccessPolicyId'] = request.conditional_access_policy_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConditionalAccessPolicy',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetConditionalAccessPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_conditional_access_policy(
        self,
        request: eiam_20211201_models.GetConditionalAccessPolicyRequest,
    ) -> eiam_20211201_models.GetConditionalAccessPolicyResponse:
        """
        @summary Get Conditional Access Policy
        
        @description Query Conditional Access Policy
        
        @param request: GetConditionalAccessPolicyRequest
        @return: GetConditionalAccessPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_conditional_access_policy_with_options(request, runtime)

    async def get_conditional_access_policy_async(
        self,
        request: eiam_20211201_models.GetConditionalAccessPolicyRequest,
    ) -> eiam_20211201_models.GetConditionalAccessPolicyResponse:
        """
        @summary Get Conditional Access Policy
        
        @description Query Conditional Access Policy
        
        @param request: GetConditionalAccessPolicyRequest
        @return: GetConditionalAccessPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_conditional_access_policy_with_options_async(request, runtime)

    def get_custom_privacy_policy_with_options(
        self,
        request: eiam_20211201_models.GetCustomPrivacyPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetCustomPrivacyPolicyResponse:
        """
        @summary 获取自定义条款
        
        @param request: GetCustomPrivacyPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCustomPrivacyPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_privacy_policy_id):
            query['CustomPrivacyPolicyId'] = request.custom_privacy_policy_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCustomPrivacyPolicy',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetCustomPrivacyPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_custom_privacy_policy_with_options_async(
        self,
        request: eiam_20211201_models.GetCustomPrivacyPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetCustomPrivacyPolicyResponse:
        """
        @summary 获取自定义条款
        
        @param request: GetCustomPrivacyPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCustomPrivacyPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_privacy_policy_id):
            query['CustomPrivacyPolicyId'] = request.custom_privacy_policy_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCustomPrivacyPolicy',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetCustomPrivacyPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_custom_privacy_policy(
        self,
        request: eiam_20211201_models.GetCustomPrivacyPolicyRequest,
    ) -> eiam_20211201_models.GetCustomPrivacyPolicyResponse:
        """
        @summary 获取自定义条款
        
        @param request: GetCustomPrivacyPolicyRequest
        @return: GetCustomPrivacyPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_custom_privacy_policy_with_options(request, runtime)

    async def get_custom_privacy_policy_async(
        self,
        request: eiam_20211201_models.GetCustomPrivacyPolicyRequest,
    ) -> eiam_20211201_models.GetCustomPrivacyPolicyResponse:
        """
        @summary 获取自定义条款
        
        @param request: GetCustomPrivacyPolicyRequest
        @return: GetCustomPrivacyPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_custom_privacy_policy_with_options_async(request, runtime)

    def get_domain_with_options(
        self,
        request: eiam_20211201_models.GetDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetDomainResponse:
        """
        @summary Queries the information about a domain name of an Employee Identity and Access Management (EIAM) instance.
        
        @param request: GetDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDomain',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_domain_with_options_async(
        self,
        request: eiam_20211201_models.GetDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetDomainResponse:
        """
        @summary Queries the information about a domain name of an Employee Identity and Access Management (EIAM) instance.
        
        @param request: GetDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDomain',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_domain(
        self,
        request: eiam_20211201_models.GetDomainRequest,
    ) -> eiam_20211201_models.GetDomainResponse:
        """
        @summary Queries the information about a domain name of an Employee Identity and Access Management (EIAM) instance.
        
        @param request: GetDomainRequest
        @return: GetDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_domain_with_options(request, runtime)

    async def get_domain_async(
        self,
        request: eiam_20211201_models.GetDomainRequest,
    ) -> eiam_20211201_models.GetDomainResponse:
        """
        @summary Queries the information about a domain name of an Employee Identity and Access Management (EIAM) instance.
        
        @param request: GetDomainRequest
        @return: GetDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_domain_with_options_async(request, runtime)

    def get_domain_dns_challenge_with_options(
        self,
        request: eiam_20211201_models.GetDomainDnsChallengeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetDomainDnsChallengeResponse:
        """
        @summary Queries the domain name system (DNS) challenge records of a domain name of an Employee Identity and Access Management (EIAM) instance. The generated records are used to verify the ownership of the domain name.
        
        @param request: GetDomainDnsChallengeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDomainDnsChallengeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDomainDnsChallenge',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetDomainDnsChallengeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_domain_dns_challenge_with_options_async(
        self,
        request: eiam_20211201_models.GetDomainDnsChallengeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetDomainDnsChallengeResponse:
        """
        @summary Queries the domain name system (DNS) challenge records of a domain name of an Employee Identity and Access Management (EIAM) instance. The generated records are used to verify the ownership of the domain name.
        
        @param request: GetDomainDnsChallengeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDomainDnsChallengeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDomainDnsChallenge',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetDomainDnsChallengeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_domain_dns_challenge(
        self,
        request: eiam_20211201_models.GetDomainDnsChallengeRequest,
    ) -> eiam_20211201_models.GetDomainDnsChallengeResponse:
        """
        @summary Queries the domain name system (DNS) challenge records of a domain name of an Employee Identity and Access Management (EIAM) instance. The generated records are used to verify the ownership of the domain name.
        
        @param request: GetDomainDnsChallengeRequest
        @return: GetDomainDnsChallengeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_domain_dns_challenge_with_options(request, runtime)

    async def get_domain_dns_challenge_async(
        self,
        request: eiam_20211201_models.GetDomainDnsChallengeRequest,
    ) -> eiam_20211201_models.GetDomainDnsChallengeResponse:
        """
        @summary Queries the domain name system (DNS) challenge records of a domain name of an Employee Identity and Access Management (EIAM) instance. The generated records are used to verify the ownership of the domain name.
        
        @param request: GetDomainDnsChallengeRequest
        @return: GetDomainDnsChallengeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_domain_dns_challenge_with_options_async(request, runtime)

    def get_federated_credential_provider_with_options(
        self,
        request: eiam_20211201_models.GetFederatedCredentialProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetFederatedCredentialProviderResponse:
        """
        @summary 获取联邦凭证提供方
        
        @param request: GetFederatedCredentialProviderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFederatedCredentialProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.federated_credential_provider_id):
            query['FederatedCredentialProviderId'] = request.federated_credential_provider_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFederatedCredentialProvider',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetFederatedCredentialProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_federated_credential_provider_with_options_async(
        self,
        request: eiam_20211201_models.GetFederatedCredentialProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetFederatedCredentialProviderResponse:
        """
        @summary 获取联邦凭证提供方
        
        @param request: GetFederatedCredentialProviderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFederatedCredentialProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.federated_credential_provider_id):
            query['FederatedCredentialProviderId'] = request.federated_credential_provider_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFederatedCredentialProvider',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetFederatedCredentialProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_federated_credential_provider(
        self,
        request: eiam_20211201_models.GetFederatedCredentialProviderRequest,
    ) -> eiam_20211201_models.GetFederatedCredentialProviderResponse:
        """
        @summary 获取联邦凭证提供方
        
        @param request: GetFederatedCredentialProviderRequest
        @return: GetFederatedCredentialProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_federated_credential_provider_with_options(request, runtime)

    async def get_federated_credential_provider_async(
        self,
        request: eiam_20211201_models.GetFederatedCredentialProviderRequest,
    ) -> eiam_20211201_models.GetFederatedCredentialProviderResponse:
        """
        @summary 获取联邦凭证提供方
        
        @param request: GetFederatedCredentialProviderRequest
        @return: GetFederatedCredentialProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_federated_credential_provider_with_options_async(request, runtime)

    def get_forget_password_configuration_with_options(
        self,
        request: eiam_20211201_models.GetForgetPasswordConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetForgetPasswordConfigurationResponse:
        """
        @summary Queries the forgot password configurations of an Employee Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS).
        
        @param request: GetForgetPasswordConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetForgetPasswordConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetForgetPasswordConfiguration',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetForgetPasswordConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_forget_password_configuration_with_options_async(
        self,
        request: eiam_20211201_models.GetForgetPasswordConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetForgetPasswordConfigurationResponse:
        """
        @summary Queries the forgot password configurations of an Employee Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS).
        
        @param request: GetForgetPasswordConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetForgetPasswordConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetForgetPasswordConfiguration',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetForgetPasswordConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_forget_password_configuration(
        self,
        request: eiam_20211201_models.GetForgetPasswordConfigurationRequest,
    ) -> eiam_20211201_models.GetForgetPasswordConfigurationResponse:
        """
        @summary Queries the forgot password configurations of an Employee Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS).
        
        @param request: GetForgetPasswordConfigurationRequest
        @return: GetForgetPasswordConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_forget_password_configuration_with_options(request, runtime)

    async def get_forget_password_configuration_async(
        self,
        request: eiam_20211201_models.GetForgetPasswordConfigurationRequest,
    ) -> eiam_20211201_models.GetForgetPasswordConfigurationResponse:
        """
        @summary Queries the forgot password configurations of an Employee Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS).
        
        @param request: GetForgetPasswordConfigurationRequest
        @return: GetForgetPasswordConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_forget_password_configuration_with_options_async(request, runtime)

    def get_group_with_options(
        self,
        request: eiam_20211201_models.GetGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetGroupResponse:
        """
        @summary Queries the information of an account group in Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM).
        
        @param request: GetGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGroup',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_group_with_options_async(
        self,
        request: eiam_20211201_models.GetGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetGroupResponse:
        """
        @summary Queries the information of an account group in Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM).
        
        @param request: GetGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGroup',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_group(
        self,
        request: eiam_20211201_models.GetGroupRequest,
    ) -> eiam_20211201_models.GetGroupResponse:
        """
        @summary Queries the information of an account group in Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM).
        
        @param request: GetGroupRequest
        @return: GetGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_group_with_options(request, runtime)

    async def get_group_async(
        self,
        request: eiam_20211201_models.GetGroupRequest,
    ) -> eiam_20211201_models.GetGroupResponse:
        """
        @summary Queries the information of an account group in Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM).
        
        @param request: GetGroupRequest
        @return: GetGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_group_with_options_async(request, runtime)

    def get_identity_provider_with_options(
        self,
        request: eiam_20211201_models.GetIdentityProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetIdentityProviderResponse:
        """
        @summary Get identity provider
        
        @param request: GetIdentityProviderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetIdentityProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identity_provider_id):
            query['IdentityProviderId'] = request.identity_provider_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetIdentityProvider',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetIdentityProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_identity_provider_with_options_async(
        self,
        request: eiam_20211201_models.GetIdentityProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetIdentityProviderResponse:
        """
        @summary Get identity provider
        
        @param request: GetIdentityProviderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetIdentityProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identity_provider_id):
            query['IdentityProviderId'] = request.identity_provider_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetIdentityProvider',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetIdentityProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_identity_provider(
        self,
        request: eiam_20211201_models.GetIdentityProviderRequest,
    ) -> eiam_20211201_models.GetIdentityProviderResponse:
        """
        @summary Get identity provider
        
        @param request: GetIdentityProviderRequest
        @return: GetIdentityProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_identity_provider_with_options(request, runtime)

    async def get_identity_provider_async(
        self,
        request: eiam_20211201_models.GetIdentityProviderRequest,
    ) -> eiam_20211201_models.GetIdentityProviderResponse:
        """
        @summary Get identity provider
        
        @param request: GetIdentityProviderRequest
        @return: GetIdentityProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_identity_provider_with_options_async(request, runtime)

    def get_identity_provider_ud_pull_configuration_with_options(
        self,
        request: eiam_20211201_models.GetIdentityProviderUdPullConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetIdentityProviderUdPullConfigurationResponse:
        """
        @summary Get IdP Inbound Synchronization Configuration Information
        
        @param request: GetIdentityProviderUdPullConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetIdentityProviderUdPullConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identity_provider_id):
            query['IdentityProviderId'] = request.identity_provider_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetIdentityProviderUdPullConfiguration',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetIdentityProviderUdPullConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_identity_provider_ud_pull_configuration_with_options_async(
        self,
        request: eiam_20211201_models.GetIdentityProviderUdPullConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetIdentityProviderUdPullConfigurationResponse:
        """
        @summary Get IdP Inbound Synchronization Configuration Information
        
        @param request: GetIdentityProviderUdPullConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetIdentityProviderUdPullConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identity_provider_id):
            query['IdentityProviderId'] = request.identity_provider_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetIdentityProviderUdPullConfiguration',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetIdentityProviderUdPullConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_identity_provider_ud_pull_configuration(
        self,
        request: eiam_20211201_models.GetIdentityProviderUdPullConfigurationRequest,
    ) -> eiam_20211201_models.GetIdentityProviderUdPullConfigurationResponse:
        """
        @summary Get IdP Inbound Synchronization Configuration Information
        
        @param request: GetIdentityProviderUdPullConfigurationRequest
        @return: GetIdentityProviderUdPullConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_identity_provider_ud_pull_configuration_with_options(request, runtime)

    async def get_identity_provider_ud_pull_configuration_async(
        self,
        request: eiam_20211201_models.GetIdentityProviderUdPullConfigurationRequest,
    ) -> eiam_20211201_models.GetIdentityProviderUdPullConfigurationResponse:
        """
        @summary Get IdP Inbound Synchronization Configuration Information
        
        @param request: GetIdentityProviderUdPullConfigurationRequest
        @return: GetIdentityProviderUdPullConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_identity_provider_ud_pull_configuration_with_options_async(request, runtime)

    def get_instance_with_options(
        self,
        request: eiam_20211201_models.GetInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetInstanceResponse:
        """
        @summary Queries the information of an Enterprise Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS).
        
        @param request: GetInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_with_options_async(
        self,
        request: eiam_20211201_models.GetInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetInstanceResponse:
        """
        @summary Queries the information of an Enterprise Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS).
        
        @param request: GetInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance(
        self,
        request: eiam_20211201_models.GetInstanceRequest,
    ) -> eiam_20211201_models.GetInstanceResponse:
        """
        @summary Queries the information of an Enterprise Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS).
        
        @param request: GetInstanceRequest
        @return: GetInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_instance_with_options(request, runtime)

    async def get_instance_async(
        self,
        request: eiam_20211201_models.GetInstanceRequest,
    ) -> eiam_20211201_models.GetInstanceResponse:
        """
        @summary Queries the information of an Enterprise Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS).
        
        @param request: GetInstanceRequest
        @return: GetInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_with_options_async(request, runtime)

    def get_instance_license_with_options(
        self,
        request: eiam_20211201_models.GetInstanceLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetInstanceLicenseResponse:
        """
        @summary Query the currently effective License information of the instance
        
        @description Please ensure that your current instance is no longer in use. When the EIAM instance is deleted, all related data will be deleted.
        
        @param request: GetInstanceLicenseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceLicenseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstanceLicense',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetInstanceLicenseResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_license_with_options_async(
        self,
        request: eiam_20211201_models.GetInstanceLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetInstanceLicenseResponse:
        """
        @summary Query the currently effective License information of the instance
        
        @description Please ensure that your current instance is no longer in use. When the EIAM instance is deleted, all related data will be deleted.
        
        @param request: GetInstanceLicenseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceLicenseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstanceLicense',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetInstanceLicenseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_license(
        self,
        request: eiam_20211201_models.GetInstanceLicenseRequest,
    ) -> eiam_20211201_models.GetInstanceLicenseResponse:
        """
        @summary Query the currently effective License information of the instance
        
        @description Please ensure that your current instance is no longer in use. When the EIAM instance is deleted, all related data will be deleted.
        
        @param request: GetInstanceLicenseRequest
        @return: GetInstanceLicenseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_instance_license_with_options(request, runtime)

    async def get_instance_license_async(
        self,
        request: eiam_20211201_models.GetInstanceLicenseRequest,
    ) -> eiam_20211201_models.GetInstanceLicenseResponse:
        """
        @summary Query the currently effective License information of the instance
        
        @description Please ensure that your current instance is no longer in use. When the EIAM instance is deleted, all related data will be deleted.
        
        @param request: GetInstanceLicenseRequest
        @return: GetInstanceLicenseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_license_with_options_async(request, runtime)

    def get_login_redirect_application_for_brand_with_options(
        self,
        request: eiam_20211201_models.GetLoginRedirectApplicationForBrandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetLoginRedirectApplicationForBrandResponse:
        """
        @summary 获取品牌登录后跳转应用
        
        @param request: GetLoginRedirectApplicationForBrandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLoginRedirectApplicationForBrandResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.brand_id):
            query['BrandId'] = request.brand_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLoginRedirectApplicationForBrand',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetLoginRedirectApplicationForBrandResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_login_redirect_application_for_brand_with_options_async(
        self,
        request: eiam_20211201_models.GetLoginRedirectApplicationForBrandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetLoginRedirectApplicationForBrandResponse:
        """
        @summary 获取品牌登录后跳转应用
        
        @param request: GetLoginRedirectApplicationForBrandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLoginRedirectApplicationForBrandResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.brand_id):
            query['BrandId'] = request.brand_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLoginRedirectApplicationForBrand',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetLoginRedirectApplicationForBrandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_login_redirect_application_for_brand(
        self,
        request: eiam_20211201_models.GetLoginRedirectApplicationForBrandRequest,
    ) -> eiam_20211201_models.GetLoginRedirectApplicationForBrandResponse:
        """
        @summary 获取品牌登录后跳转应用
        
        @param request: GetLoginRedirectApplicationForBrandRequest
        @return: GetLoginRedirectApplicationForBrandResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_login_redirect_application_for_brand_with_options(request, runtime)

    async def get_login_redirect_application_for_brand_async(
        self,
        request: eiam_20211201_models.GetLoginRedirectApplicationForBrandRequest,
    ) -> eiam_20211201_models.GetLoginRedirectApplicationForBrandResponse:
        """
        @summary 获取品牌登录后跳转应用
        
        @param request: GetLoginRedirectApplicationForBrandRequest
        @return: GetLoginRedirectApplicationForBrandResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_login_redirect_application_for_brand_with_options_async(request, runtime)

    def get_network_access_endpoint_with_options(
        self,
        request: eiam_20211201_models.GetNetworkAccessEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetNetworkAccessEndpointResponse:
        """
        @summary Get Network Endpoint Information
        
        @param request: GetNetworkAccessEndpointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNetworkAccessEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_access_endpoint_id):
            query['NetworkAccessEndpointId'] = request.network_access_endpoint_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNetworkAccessEndpoint',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetNetworkAccessEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_network_access_endpoint_with_options_async(
        self,
        request: eiam_20211201_models.GetNetworkAccessEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetNetworkAccessEndpointResponse:
        """
        @summary Get Network Endpoint Information
        
        @param request: GetNetworkAccessEndpointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNetworkAccessEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_access_endpoint_id):
            query['NetworkAccessEndpointId'] = request.network_access_endpoint_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNetworkAccessEndpoint',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetNetworkAccessEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_network_access_endpoint(
        self,
        request: eiam_20211201_models.GetNetworkAccessEndpointRequest,
    ) -> eiam_20211201_models.GetNetworkAccessEndpointResponse:
        """
        @summary Get Network Endpoint Information
        
        @param request: GetNetworkAccessEndpointRequest
        @return: GetNetworkAccessEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_network_access_endpoint_with_options(request, runtime)

    async def get_network_access_endpoint_async(
        self,
        request: eiam_20211201_models.GetNetworkAccessEndpointRequest,
    ) -> eiam_20211201_models.GetNetworkAccessEndpointResponse:
        """
        @summary Get Network Endpoint Information
        
        @param request: GetNetworkAccessEndpointRequest
        @return: GetNetworkAccessEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_network_access_endpoint_with_options_async(request, runtime)

    def get_network_zone_with_options(
        self,
        request: eiam_20211201_models.GetNetworkZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetNetworkZoneResponse:
        """
        @summary 获取网络区域对象
        
        @param request: GetNetworkZoneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNetworkZoneResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_zone_id):
            query['NetworkZoneId'] = request.network_zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNetworkZone',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetNetworkZoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_network_zone_with_options_async(
        self,
        request: eiam_20211201_models.GetNetworkZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetNetworkZoneResponse:
        """
        @summary 获取网络区域对象
        
        @param request: GetNetworkZoneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNetworkZoneResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_zone_id):
            query['NetworkZoneId'] = request.network_zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNetworkZone',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetNetworkZoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_network_zone(
        self,
        request: eiam_20211201_models.GetNetworkZoneRequest,
    ) -> eiam_20211201_models.GetNetworkZoneResponse:
        """
        @summary 获取网络区域对象
        
        @param request: GetNetworkZoneRequest
        @return: GetNetworkZoneResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_network_zone_with_options(request, runtime)

    async def get_network_zone_async(
        self,
        request: eiam_20211201_models.GetNetworkZoneRequest,
    ) -> eiam_20211201_models.GetNetworkZoneResponse:
        """
        @summary 获取网络区域对象
        
        @param request: GetNetworkZoneRequest
        @return: GetNetworkZoneResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_network_zone_with_options_async(request, runtime)

    def get_organizational_unit_with_options(
        self,
        request: eiam_20211201_models.GetOrganizationalUnitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetOrganizationalUnitResponse:
        """
        @summary Queries the information about an organizational unit in Identity as a Service (IDaaS) Employee IAM (EIAM).
        
        @param request: GetOrganizationalUnitRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOrganizationalUnitResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.organizational_unit_id):
            query['OrganizationalUnitId'] = request.organizational_unit_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOrganizationalUnit',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetOrganizationalUnitResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_organizational_unit_with_options_async(
        self,
        request: eiam_20211201_models.GetOrganizationalUnitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetOrganizationalUnitResponse:
        """
        @summary Queries the information about an organizational unit in Identity as a Service (IDaaS) Employee IAM (EIAM).
        
        @param request: GetOrganizationalUnitRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOrganizationalUnitResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.organizational_unit_id):
            query['OrganizationalUnitId'] = request.organizational_unit_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOrganizationalUnit',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetOrganizationalUnitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_organizational_unit(
        self,
        request: eiam_20211201_models.GetOrganizationalUnitRequest,
    ) -> eiam_20211201_models.GetOrganizationalUnitResponse:
        """
        @summary Queries the information about an organizational unit in Identity as a Service (IDaaS) Employee IAM (EIAM).
        
        @param request: GetOrganizationalUnitRequest
        @return: GetOrganizationalUnitResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_organizational_unit_with_options(request, runtime)

    async def get_organizational_unit_async(
        self,
        request: eiam_20211201_models.GetOrganizationalUnitRequest,
    ) -> eiam_20211201_models.GetOrganizationalUnitResponse:
        """
        @summary Queries the information about an organizational unit in Identity as a Service (IDaaS) Employee IAM (EIAM).
        
        @param request: GetOrganizationalUnitRequest
        @return: GetOrganizationalUnitResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_organizational_unit_with_options_async(request, runtime)

    def get_password_complexity_configuration_with_options(
        self,
        request: eiam_20211201_models.GetPasswordComplexityConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetPasswordComplexityConfigurationResponse:
        """
        @summary Queries the password complexity configurations of an Employee Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS).
        
        @param request: GetPasswordComplexityConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPasswordComplexityConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPasswordComplexityConfiguration',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetPasswordComplexityConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_password_complexity_configuration_with_options_async(
        self,
        request: eiam_20211201_models.GetPasswordComplexityConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetPasswordComplexityConfigurationResponse:
        """
        @summary Queries the password complexity configurations of an Employee Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS).
        
        @param request: GetPasswordComplexityConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPasswordComplexityConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPasswordComplexityConfiguration',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetPasswordComplexityConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_password_complexity_configuration(
        self,
        request: eiam_20211201_models.GetPasswordComplexityConfigurationRequest,
    ) -> eiam_20211201_models.GetPasswordComplexityConfigurationResponse:
        """
        @summary Queries the password complexity configurations of an Employee Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS).
        
        @param request: GetPasswordComplexityConfigurationRequest
        @return: GetPasswordComplexityConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_password_complexity_configuration_with_options(request, runtime)

    async def get_password_complexity_configuration_async(
        self,
        request: eiam_20211201_models.GetPasswordComplexityConfigurationRequest,
    ) -> eiam_20211201_models.GetPasswordComplexityConfigurationResponse:
        """
        @summary Queries the password complexity configurations of an Employee Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS).
        
        @param request: GetPasswordComplexityConfigurationRequest
        @return: GetPasswordComplexityConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_password_complexity_configuration_with_options_async(request, runtime)

    def get_password_expiration_configuration_with_options(
        self,
        request: eiam_20211201_models.GetPasswordExpirationConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetPasswordExpirationConfigurationResponse:
        """
        @summary Queries the password expiration configurations of an Employee Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS).
        
        @param request: GetPasswordExpirationConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPasswordExpirationConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPasswordExpirationConfiguration',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetPasswordExpirationConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_password_expiration_configuration_with_options_async(
        self,
        request: eiam_20211201_models.GetPasswordExpirationConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetPasswordExpirationConfigurationResponse:
        """
        @summary Queries the password expiration configurations of an Employee Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS).
        
        @param request: GetPasswordExpirationConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPasswordExpirationConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPasswordExpirationConfiguration',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetPasswordExpirationConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_password_expiration_configuration(
        self,
        request: eiam_20211201_models.GetPasswordExpirationConfigurationRequest,
    ) -> eiam_20211201_models.GetPasswordExpirationConfigurationResponse:
        """
        @summary Queries the password expiration configurations of an Employee Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS).
        
        @param request: GetPasswordExpirationConfigurationRequest
        @return: GetPasswordExpirationConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_password_expiration_configuration_with_options(request, runtime)

    async def get_password_expiration_configuration_async(
        self,
        request: eiam_20211201_models.GetPasswordExpirationConfigurationRequest,
    ) -> eiam_20211201_models.GetPasswordExpirationConfigurationResponse:
        """
        @summary Queries the password expiration configurations of an Employee Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS).
        
        @param request: GetPasswordExpirationConfigurationRequest
        @return: GetPasswordExpirationConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_password_expiration_configuration_with_options_async(request, runtime)

    def get_password_history_configuration_with_options(
        self,
        request: eiam_20211201_models.GetPasswordHistoryConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetPasswordHistoryConfigurationResponse:
        """
        @summary Queries the password history configurations of an Employee Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS).
        
        @param request: GetPasswordHistoryConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPasswordHistoryConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPasswordHistoryConfiguration',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetPasswordHistoryConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_password_history_configuration_with_options_async(
        self,
        request: eiam_20211201_models.GetPasswordHistoryConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetPasswordHistoryConfigurationResponse:
        """
        @summary Queries the password history configurations of an Employee Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS).
        
        @param request: GetPasswordHistoryConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPasswordHistoryConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPasswordHistoryConfiguration',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetPasswordHistoryConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_password_history_configuration(
        self,
        request: eiam_20211201_models.GetPasswordHistoryConfigurationRequest,
    ) -> eiam_20211201_models.GetPasswordHistoryConfigurationResponse:
        """
        @summary Queries the password history configurations of an Employee Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS).
        
        @param request: GetPasswordHistoryConfigurationRequest
        @return: GetPasswordHistoryConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_password_history_configuration_with_options(request, runtime)

    async def get_password_history_configuration_async(
        self,
        request: eiam_20211201_models.GetPasswordHistoryConfigurationRequest,
    ) -> eiam_20211201_models.GetPasswordHistoryConfigurationResponse:
        """
        @summary Queries the password history configurations of an Employee Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS).
        
        @param request: GetPasswordHistoryConfigurationRequest
        @return: GetPasswordHistoryConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_password_history_configuration_with_options_async(request, runtime)

    def get_password_initialization_configuration_with_options(
        self,
        request: eiam_20211201_models.GetPasswordInitializationConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetPasswordInitializationConfigurationResponse:
        """
        @summary Queries the password initialization configurations of an Employee Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS).
        
        @param request: GetPasswordInitializationConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPasswordInitializationConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPasswordInitializationConfiguration',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetPasswordInitializationConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_password_initialization_configuration_with_options_async(
        self,
        request: eiam_20211201_models.GetPasswordInitializationConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetPasswordInitializationConfigurationResponse:
        """
        @summary Queries the password initialization configurations of an Employee Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS).
        
        @param request: GetPasswordInitializationConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPasswordInitializationConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPasswordInitializationConfiguration',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetPasswordInitializationConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_password_initialization_configuration(
        self,
        request: eiam_20211201_models.GetPasswordInitializationConfigurationRequest,
    ) -> eiam_20211201_models.GetPasswordInitializationConfigurationResponse:
        """
        @summary Queries the password initialization configurations of an Employee Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS).
        
        @param request: GetPasswordInitializationConfigurationRequest
        @return: GetPasswordInitializationConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_password_initialization_configuration_with_options(request, runtime)

    async def get_password_initialization_configuration_async(
        self,
        request: eiam_20211201_models.GetPasswordInitializationConfigurationRequest,
    ) -> eiam_20211201_models.GetPasswordInitializationConfigurationResponse:
        """
        @summary Queries the password initialization configurations of an Employee Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS).
        
        @param request: GetPasswordInitializationConfigurationRequest
        @return: GetPasswordInitializationConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_password_initialization_configuration_with_options_async(request, runtime)

    def get_root_organizational_unit_with_options(
        self,
        request: eiam_20211201_models.GetRootOrganizationalUnitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetRootOrganizationalUnitResponse:
        """
        @summary Queries the information about the root organizational unit in Identity as a Service (IDaaS) Employee IAM (EIAM).
        
        @param request: GetRootOrganizationalUnitRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRootOrganizationalUnitResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRootOrganizationalUnit',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetRootOrganizationalUnitResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_root_organizational_unit_with_options_async(
        self,
        request: eiam_20211201_models.GetRootOrganizationalUnitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetRootOrganizationalUnitResponse:
        """
        @summary Queries the information about the root organizational unit in Identity as a Service (IDaaS) Employee IAM (EIAM).
        
        @param request: GetRootOrganizationalUnitRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRootOrganizationalUnitResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRootOrganizationalUnit',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetRootOrganizationalUnitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_root_organizational_unit(
        self,
        request: eiam_20211201_models.GetRootOrganizationalUnitRequest,
    ) -> eiam_20211201_models.GetRootOrganizationalUnitResponse:
        """
        @summary Queries the information about the root organizational unit in Identity as a Service (IDaaS) Employee IAM (EIAM).
        
        @param request: GetRootOrganizationalUnitRequest
        @return: GetRootOrganizationalUnitResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_root_organizational_unit_with_options(request, runtime)

    async def get_root_organizational_unit_async(
        self,
        request: eiam_20211201_models.GetRootOrganizationalUnitRequest,
    ) -> eiam_20211201_models.GetRootOrganizationalUnitResponse:
        """
        @summary Queries the information about the root organizational unit in Identity as a Service (IDaaS) Employee IAM (EIAM).
        
        @param request: GetRootOrganizationalUnitRequest
        @return: GetRootOrganizationalUnitResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_root_organizational_unit_with_options_async(request, runtime)

    def get_synchronization_job_with_options(
        self,
        request: eiam_20211201_models.GetSynchronizationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetSynchronizationJobResponse:
        """
        @summary Obtains the information about a single synchronization job.
        
        @param request: GetSynchronizationJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSynchronizationJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSynchronizationJob',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetSynchronizationJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_synchronization_job_with_options_async(
        self,
        request: eiam_20211201_models.GetSynchronizationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetSynchronizationJobResponse:
        """
        @summary Obtains the information about a single synchronization job.
        
        @param request: GetSynchronizationJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSynchronizationJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSynchronizationJob',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetSynchronizationJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_synchronization_job(
        self,
        request: eiam_20211201_models.GetSynchronizationJobRequest,
    ) -> eiam_20211201_models.GetSynchronizationJobResponse:
        """
        @summary Obtains the information about a single synchronization job.
        
        @param request: GetSynchronizationJobRequest
        @return: GetSynchronizationJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_synchronization_job_with_options(request, runtime)

    async def get_synchronization_job_async(
        self,
        request: eiam_20211201_models.GetSynchronizationJobRequest,
    ) -> eiam_20211201_models.GetSynchronizationJobResponse:
        """
        @summary Obtains the information about a single synchronization job.
        
        @param request: GetSynchronizationJobRequest
        @return: GetSynchronizationJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_synchronization_job_with_options_async(request, runtime)

    def get_user_with_options(
        self,
        request: eiam_20211201_models.GetUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetUserResponse:
        """
        @summary Queries the details of an account in Identity as a Service (IDaaS) Employee IAM (EIAM).
        
        @param request: GetUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUser',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_with_options_async(
        self,
        request: eiam_20211201_models.GetUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.GetUserResponse:
        """
        @summary Queries the details of an account in Identity as a Service (IDaaS) Employee IAM (EIAM).
        
        @param request: GetUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUser',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.GetUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user(
        self,
        request: eiam_20211201_models.GetUserRequest,
    ) -> eiam_20211201_models.GetUserResponse:
        """
        @summary Queries the details of an account in Identity as a Service (IDaaS) Employee IAM (EIAM).
        
        @param request: GetUserRequest
        @return: GetUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_user_with_options(request, runtime)

    async def get_user_async(
        self,
        request: eiam_20211201_models.GetUserRequest,
    ) -> eiam_20211201_models.GetUserResponse:
        """
        @summary Queries the details of an account in Identity as a Service (IDaaS) Employee IAM (EIAM).
        
        @param request: GetUserRequest
        @return: GetUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_user_with_options_async(request, runtime)

    def list_application_accounts_with_options(
        self,
        request: eiam_20211201_models.ListApplicationAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListApplicationAccountsResponse:
        """
        @summary 分页查询应用下的应用账户列表
        
        @param request: ListApplicationAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApplicationAccountsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplicationAccounts',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListApplicationAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_application_accounts_with_options_async(
        self,
        request: eiam_20211201_models.ListApplicationAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListApplicationAccountsResponse:
        """
        @summary 分页查询应用下的应用账户列表
        
        @param request: ListApplicationAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApplicationAccountsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplicationAccounts',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListApplicationAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_application_accounts(
        self,
        request: eiam_20211201_models.ListApplicationAccountsRequest,
    ) -> eiam_20211201_models.ListApplicationAccountsResponse:
        """
        @summary 分页查询应用下的应用账户列表
        
        @param request: ListApplicationAccountsRequest
        @return: ListApplicationAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_application_accounts_with_options(request, runtime)

    async def list_application_accounts_async(
        self,
        request: eiam_20211201_models.ListApplicationAccountsRequest,
    ) -> eiam_20211201_models.ListApplicationAccountsResponse:
        """
        @summary 分页查询应用下的应用账户列表
        
        @param request: ListApplicationAccountsRequest
        @return: ListApplicationAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_application_accounts_with_options_async(request, runtime)

    def list_application_accounts_for_user_with_options(
        self,
        request: eiam_20211201_models.ListApplicationAccountsForUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListApplicationAccountsForUserResponse:
        """
        @summary 查询当前应用下指定用户的所有账号
        
        @param request: ListApplicationAccountsForUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApplicationAccountsForUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplicationAccountsForUser',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListApplicationAccountsForUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_application_accounts_for_user_with_options_async(
        self,
        request: eiam_20211201_models.ListApplicationAccountsForUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListApplicationAccountsForUserResponse:
        """
        @summary 查询当前应用下指定用户的所有账号
        
        @param request: ListApplicationAccountsForUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApplicationAccountsForUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplicationAccountsForUser',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListApplicationAccountsForUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_application_accounts_for_user(
        self,
        request: eiam_20211201_models.ListApplicationAccountsForUserRequest,
    ) -> eiam_20211201_models.ListApplicationAccountsForUserResponse:
        """
        @summary 查询当前应用下指定用户的所有账号
        
        @param request: ListApplicationAccountsForUserRequest
        @return: ListApplicationAccountsForUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_application_accounts_for_user_with_options(request, runtime)

    async def list_application_accounts_for_user_async(
        self,
        request: eiam_20211201_models.ListApplicationAccountsForUserRequest,
    ) -> eiam_20211201_models.ListApplicationAccountsForUserResponse:
        """
        @summary 查询当前应用下指定用户的所有账号
        
        @param request: ListApplicationAccountsForUserRequest
        @return: ListApplicationAccountsForUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_application_accounts_for_user_with_options_async(request, runtime)

    def list_application_client_secrets_with_options(
        self,
        request: eiam_20211201_models.ListApplicationClientSecretsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListApplicationClientSecretsResponse:
        """
        @summary Queries all client keys of an Employee Identity and Access Management (EIAM) application. The returned key secret is not masked. If you want to query the key secret that is masked, call the ObtainApplicationClientSecret operation.
        
        @param request: ListApplicationClientSecretsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApplicationClientSecretsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplicationClientSecrets',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListApplicationClientSecretsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_application_client_secrets_with_options_async(
        self,
        request: eiam_20211201_models.ListApplicationClientSecretsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListApplicationClientSecretsResponse:
        """
        @summary Queries all client keys of an Employee Identity and Access Management (EIAM) application. The returned key secret is not masked. If you want to query the key secret that is masked, call the ObtainApplicationClientSecret operation.
        
        @param request: ListApplicationClientSecretsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApplicationClientSecretsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplicationClientSecrets',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListApplicationClientSecretsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_application_client_secrets(
        self,
        request: eiam_20211201_models.ListApplicationClientSecretsRequest,
    ) -> eiam_20211201_models.ListApplicationClientSecretsResponse:
        """
        @summary Queries all client keys of an Employee Identity and Access Management (EIAM) application. The returned key secret is not masked. If you want to query the key secret that is masked, call the ObtainApplicationClientSecret operation.
        
        @param request: ListApplicationClientSecretsRequest
        @return: ListApplicationClientSecretsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_application_client_secrets_with_options(request, runtime)

    async def list_application_client_secrets_async(
        self,
        request: eiam_20211201_models.ListApplicationClientSecretsRequest,
    ) -> eiam_20211201_models.ListApplicationClientSecretsResponse:
        """
        @summary Queries all client keys of an Employee Identity and Access Management (EIAM) application. The returned key secret is not masked. If you want to query the key secret that is masked, call the ObtainApplicationClientSecret operation.
        
        @param request: ListApplicationClientSecretsRequest
        @return: ListApplicationClientSecretsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_application_client_secrets_with_options_async(request, runtime)

    def list_application_federated_credentials_with_options(
        self,
        request: eiam_20211201_models.ListApplicationFederatedCredentialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListApplicationFederatedCredentialsResponse:
        """
        @summary 查询应用联邦凭证列表
        
        @param request: ListApplicationFederatedCredentialsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApplicationFederatedCredentialsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_federated_credential_type):
            query['ApplicationFederatedCredentialType'] = request.application_federated_credential_type
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.previous_token):
            query['PreviousToken'] = request.previous_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplicationFederatedCredentials',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListApplicationFederatedCredentialsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_application_federated_credentials_with_options_async(
        self,
        request: eiam_20211201_models.ListApplicationFederatedCredentialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListApplicationFederatedCredentialsResponse:
        """
        @summary 查询应用联邦凭证列表
        
        @param request: ListApplicationFederatedCredentialsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApplicationFederatedCredentialsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_federated_credential_type):
            query['ApplicationFederatedCredentialType'] = request.application_federated_credential_type
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.previous_token):
            query['PreviousToken'] = request.previous_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplicationFederatedCredentials',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListApplicationFederatedCredentialsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_application_federated_credentials(
        self,
        request: eiam_20211201_models.ListApplicationFederatedCredentialsRequest,
    ) -> eiam_20211201_models.ListApplicationFederatedCredentialsResponse:
        """
        @summary 查询应用联邦凭证列表
        
        @param request: ListApplicationFederatedCredentialsRequest
        @return: ListApplicationFederatedCredentialsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_application_federated_credentials_with_options(request, runtime)

    async def list_application_federated_credentials_async(
        self,
        request: eiam_20211201_models.ListApplicationFederatedCredentialsRequest,
    ) -> eiam_20211201_models.ListApplicationFederatedCredentialsResponse:
        """
        @summary 查询应用联邦凭证列表
        
        @param request: ListApplicationFederatedCredentialsRequest
        @return: ListApplicationFederatedCredentialsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_application_federated_credentials_with_options_async(request, runtime)

    def list_application_federated_credentials_for_provider_with_options(
        self,
        request: eiam_20211201_models.ListApplicationFederatedCredentialsForProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListApplicationFederatedCredentialsForProviderResponse:
        """
        @summary 根据联邦凭证提供方查询应用联邦凭证列表
        
        @param request: ListApplicationFederatedCredentialsForProviderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApplicationFederatedCredentialsForProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.federated_credential_provider_id):
            query['FederatedCredentialProviderId'] = request.federated_credential_provider_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.previous_token):
            query['PreviousToken'] = request.previous_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplicationFederatedCredentialsForProvider',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListApplicationFederatedCredentialsForProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_application_federated_credentials_for_provider_with_options_async(
        self,
        request: eiam_20211201_models.ListApplicationFederatedCredentialsForProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListApplicationFederatedCredentialsForProviderResponse:
        """
        @summary 根据联邦凭证提供方查询应用联邦凭证列表
        
        @param request: ListApplicationFederatedCredentialsForProviderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApplicationFederatedCredentialsForProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.federated_credential_provider_id):
            query['FederatedCredentialProviderId'] = request.federated_credential_provider_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.previous_token):
            query['PreviousToken'] = request.previous_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplicationFederatedCredentialsForProvider',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListApplicationFederatedCredentialsForProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_application_federated_credentials_for_provider(
        self,
        request: eiam_20211201_models.ListApplicationFederatedCredentialsForProviderRequest,
    ) -> eiam_20211201_models.ListApplicationFederatedCredentialsForProviderResponse:
        """
        @summary 根据联邦凭证提供方查询应用联邦凭证列表
        
        @param request: ListApplicationFederatedCredentialsForProviderRequest
        @return: ListApplicationFederatedCredentialsForProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_application_federated_credentials_for_provider_with_options(request, runtime)

    async def list_application_federated_credentials_for_provider_async(
        self,
        request: eiam_20211201_models.ListApplicationFederatedCredentialsForProviderRequest,
    ) -> eiam_20211201_models.ListApplicationFederatedCredentialsForProviderResponse:
        """
        @summary 根据联邦凭证提供方查询应用联邦凭证列表
        
        @param request: ListApplicationFederatedCredentialsForProviderRequest
        @return: ListApplicationFederatedCredentialsForProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_application_federated_credentials_for_provider_with_options_async(request, runtime)

    def list_application_supported_provision_protocol_types_with_options(
        self,
        request: eiam_20211201_models.ListApplicationSupportedProvisionProtocolTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListApplicationSupportedProvisionProtocolTypesResponse:
        """
        @summary 应用支持账户同步类型列表
        
        @param request: ListApplicationSupportedProvisionProtocolTypesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApplicationSupportedProvisionProtocolTypesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplicationSupportedProvisionProtocolTypes',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListApplicationSupportedProvisionProtocolTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_application_supported_provision_protocol_types_with_options_async(
        self,
        request: eiam_20211201_models.ListApplicationSupportedProvisionProtocolTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListApplicationSupportedProvisionProtocolTypesResponse:
        """
        @summary 应用支持账户同步类型列表
        
        @param request: ListApplicationSupportedProvisionProtocolTypesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApplicationSupportedProvisionProtocolTypesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplicationSupportedProvisionProtocolTypes',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListApplicationSupportedProvisionProtocolTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_application_supported_provision_protocol_types(
        self,
        request: eiam_20211201_models.ListApplicationSupportedProvisionProtocolTypesRequest,
    ) -> eiam_20211201_models.ListApplicationSupportedProvisionProtocolTypesResponse:
        """
        @summary 应用支持账户同步类型列表
        
        @param request: ListApplicationSupportedProvisionProtocolTypesRequest
        @return: ListApplicationSupportedProvisionProtocolTypesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_application_supported_provision_protocol_types_with_options(request, runtime)

    async def list_application_supported_provision_protocol_types_async(
        self,
        request: eiam_20211201_models.ListApplicationSupportedProvisionProtocolTypesRequest,
    ) -> eiam_20211201_models.ListApplicationSupportedProvisionProtocolTypesResponse:
        """
        @summary 应用支持账户同步类型列表
        
        @param request: ListApplicationSupportedProvisionProtocolTypesRequest
        @return: ListApplicationSupportedProvisionProtocolTypesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_application_supported_provision_protocol_types_with_options_async(request, runtime)

    def list_application_tokens_with_options(
        self,
        request: eiam_20211201_models.ListApplicationTokensRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListApplicationTokensResponse:
        """
        @summary 创建应用Token
        
        @param request: ListApplicationTokensRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApplicationTokensResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.application_token_type):
            query['ApplicationTokenType'] = request.application_token_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplicationTokens',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListApplicationTokensResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_application_tokens_with_options_async(
        self,
        request: eiam_20211201_models.ListApplicationTokensRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListApplicationTokensResponse:
        """
        @summary 创建应用Token
        
        @param request: ListApplicationTokensRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApplicationTokensResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.application_token_type):
            query['ApplicationTokenType'] = request.application_token_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplicationTokens',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListApplicationTokensResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_application_tokens(
        self,
        request: eiam_20211201_models.ListApplicationTokensRequest,
    ) -> eiam_20211201_models.ListApplicationTokensResponse:
        """
        @summary 创建应用Token
        
        @param request: ListApplicationTokensRequest
        @return: ListApplicationTokensResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_application_tokens_with_options(request, runtime)

    async def list_application_tokens_async(
        self,
        request: eiam_20211201_models.ListApplicationTokensRequest,
    ) -> eiam_20211201_models.ListApplicationTokensResponse:
        """
        @summary 创建应用Token
        
        @param request: ListApplicationTokensRequest
        @return: ListApplicationTokensResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_application_tokens_with_options_async(request, runtime)

    def list_applications_with_options(
        self,
        request: eiam_20211201_models.ListApplicationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListApplicationsResponse:
        """
        @summary Queries the information about one or multiple Employee Identity and Access Management (EIAM) applications by page.
        
        @param request: ListApplicationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApplicationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_ids):
            query['ApplicationIds'] = request.application_ids
        if not UtilClient.is_unset(request.application_name):
            query['ApplicationName'] = request.application_name
        if not UtilClient.is_unset(request.authorization_type):
            query['AuthorizationType'] = request.authorization_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.m_2mclient_status):
            query['M2MClientStatus'] = request.m_2mclient_status
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_server_status):
            query['ResourceServerStatus'] = request.resource_server_status
        if not UtilClient.is_unset(request.sso_type):
            query['SsoType'] = request.sso_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplications',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_applications_with_options_async(
        self,
        request: eiam_20211201_models.ListApplicationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListApplicationsResponse:
        """
        @summary Queries the information about one or multiple Employee Identity and Access Management (EIAM) applications by page.
        
        @param request: ListApplicationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApplicationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_ids):
            query['ApplicationIds'] = request.application_ids
        if not UtilClient.is_unset(request.application_name):
            query['ApplicationName'] = request.application_name
        if not UtilClient.is_unset(request.authorization_type):
            query['AuthorizationType'] = request.authorization_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.m_2mclient_status):
            query['M2MClientStatus'] = request.m_2mclient_status
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_server_status):
            query['ResourceServerStatus'] = request.resource_server_status
        if not UtilClient.is_unset(request.sso_type):
            query['SsoType'] = request.sso_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplications',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListApplicationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_applications(
        self,
        request: eiam_20211201_models.ListApplicationsRequest,
    ) -> eiam_20211201_models.ListApplicationsResponse:
        """
        @summary Queries the information about one or multiple Employee Identity and Access Management (EIAM) applications by page.
        
        @param request: ListApplicationsRequest
        @return: ListApplicationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_applications_with_options(request, runtime)

    async def list_applications_async(
        self,
        request: eiam_20211201_models.ListApplicationsRequest,
    ) -> eiam_20211201_models.ListApplicationsResponse:
        """
        @summary Queries the information about one or multiple Employee Identity and Access Management (EIAM) applications by page.
        
        @param request: ListApplicationsRequest
        @return: ListApplicationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_applications_with_options_async(request, runtime)

    def list_applications_for_group_with_options(
        self,
        request: eiam_20211201_models.ListApplicationsForGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListApplicationsForGroupResponse:
        """
        @summary 查询一个EIAM组可访问的应用列表
        
        @param request: ListApplicationsForGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApplicationsForGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_ids):
            query['ApplicationIds'] = request.application_ids
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplicationsForGroup',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListApplicationsForGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_applications_for_group_with_options_async(
        self,
        request: eiam_20211201_models.ListApplicationsForGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListApplicationsForGroupResponse:
        """
        @summary 查询一个EIAM组可访问的应用列表
        
        @param request: ListApplicationsForGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApplicationsForGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_ids):
            query['ApplicationIds'] = request.application_ids
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplicationsForGroup',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListApplicationsForGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_applications_for_group(
        self,
        request: eiam_20211201_models.ListApplicationsForGroupRequest,
    ) -> eiam_20211201_models.ListApplicationsForGroupResponse:
        """
        @summary 查询一个EIAM组可访问的应用列表
        
        @param request: ListApplicationsForGroupRequest
        @return: ListApplicationsForGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_applications_for_group_with_options(request, runtime)

    async def list_applications_for_group_async(
        self,
        request: eiam_20211201_models.ListApplicationsForGroupRequest,
    ) -> eiam_20211201_models.ListApplicationsForGroupResponse:
        """
        @summary 查询一个EIAM组可访问的应用列表
        
        @param request: ListApplicationsForGroupRequest
        @return: ListApplicationsForGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_applications_for_group_with_options_async(request, runtime)

    def list_applications_for_network_access_endpoint_with_options(
        self,
        request: eiam_20211201_models.ListApplicationsForNetworkAccessEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListApplicationsForNetworkAccessEndpointResponse:
        """
        @summary 获取网络访问端点下的App信息。
        
        @param request: ListApplicationsForNetworkAccessEndpointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApplicationsForNetworkAccessEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.network_access_endpoint_id):
            query['NetworkAccessEndpointId'] = request.network_access_endpoint_id
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplicationsForNetworkAccessEndpoint',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListApplicationsForNetworkAccessEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_applications_for_network_access_endpoint_with_options_async(
        self,
        request: eiam_20211201_models.ListApplicationsForNetworkAccessEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListApplicationsForNetworkAccessEndpointResponse:
        """
        @summary 获取网络访问端点下的App信息。
        
        @param request: ListApplicationsForNetworkAccessEndpointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApplicationsForNetworkAccessEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.network_access_endpoint_id):
            query['NetworkAccessEndpointId'] = request.network_access_endpoint_id
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplicationsForNetworkAccessEndpoint',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListApplicationsForNetworkAccessEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_applications_for_network_access_endpoint(
        self,
        request: eiam_20211201_models.ListApplicationsForNetworkAccessEndpointRequest,
    ) -> eiam_20211201_models.ListApplicationsForNetworkAccessEndpointResponse:
        """
        @summary 获取网络访问端点下的App信息。
        
        @param request: ListApplicationsForNetworkAccessEndpointRequest
        @return: ListApplicationsForNetworkAccessEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_applications_for_network_access_endpoint_with_options(request, runtime)

    async def list_applications_for_network_access_endpoint_async(
        self,
        request: eiam_20211201_models.ListApplicationsForNetworkAccessEndpointRequest,
    ) -> eiam_20211201_models.ListApplicationsForNetworkAccessEndpointResponse:
        """
        @summary 获取网络访问端点下的App信息。
        
        @param request: ListApplicationsForNetworkAccessEndpointRequest
        @return: ListApplicationsForNetworkAccessEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_applications_for_network_access_endpoint_with_options_async(request, runtime)

    def list_applications_for_network_zone_with_options(
        self,
        request: eiam_20211201_models.ListApplicationsForNetworkZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListApplicationsForNetworkZoneResponse:
        """
        @summary 获取NetworkZone关联的应用列表
        
        @param request: ListApplicationsForNetworkZoneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApplicationsForNetworkZoneResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.network_zone_id):
            query['NetworkZoneId'] = request.network_zone_id
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.previous_token):
            query['PreviousToken'] = request.previous_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplicationsForNetworkZone',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListApplicationsForNetworkZoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_applications_for_network_zone_with_options_async(
        self,
        request: eiam_20211201_models.ListApplicationsForNetworkZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListApplicationsForNetworkZoneResponse:
        """
        @summary 获取NetworkZone关联的应用列表
        
        @param request: ListApplicationsForNetworkZoneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApplicationsForNetworkZoneResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.network_zone_id):
            query['NetworkZoneId'] = request.network_zone_id
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.previous_token):
            query['PreviousToken'] = request.previous_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplicationsForNetworkZone',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListApplicationsForNetworkZoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_applications_for_network_zone(
        self,
        request: eiam_20211201_models.ListApplicationsForNetworkZoneRequest,
    ) -> eiam_20211201_models.ListApplicationsForNetworkZoneResponse:
        """
        @summary 获取NetworkZone关联的应用列表
        
        @param request: ListApplicationsForNetworkZoneRequest
        @return: ListApplicationsForNetworkZoneResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_applications_for_network_zone_with_options(request, runtime)

    async def list_applications_for_network_zone_async(
        self,
        request: eiam_20211201_models.ListApplicationsForNetworkZoneRequest,
    ) -> eiam_20211201_models.ListApplicationsForNetworkZoneResponse:
        """
        @summary 获取NetworkZone关联的应用列表
        
        @param request: ListApplicationsForNetworkZoneRequest
        @return: ListApplicationsForNetworkZoneResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_applications_for_network_zone_with_options_async(request, runtime)

    def list_applications_for_organizational_unit_with_options(
        self,
        request: eiam_20211201_models.ListApplicationsForOrganizationalUnitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListApplicationsForOrganizationalUnitResponse:
        """
        @summary Queries the applications that an Employee Identity and Access Management (EIAM) organization can access. The return result includes the IDs of the applications. If you want to obtain the details of the applications, call the GetApplication operation.
        
        @description You can only query the permissions that are directly granted to the EIAM organization by calling the ListApplicationsForOrganizationalUnit operation. You can filter applications by configuring the *ApplicationIds** parameter when you call this operation.
        
        @param request: ListApplicationsForOrganizationalUnitRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApplicationsForOrganizationalUnitResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_ids):
            query['ApplicationIds'] = request.application_ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.organizational_unit_id):
            query['OrganizationalUnitId'] = request.organizational_unit_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplicationsForOrganizationalUnit',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListApplicationsForOrganizationalUnitResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_applications_for_organizational_unit_with_options_async(
        self,
        request: eiam_20211201_models.ListApplicationsForOrganizationalUnitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListApplicationsForOrganizationalUnitResponse:
        """
        @summary Queries the applications that an Employee Identity and Access Management (EIAM) organization can access. The return result includes the IDs of the applications. If you want to obtain the details of the applications, call the GetApplication operation.
        
        @description You can only query the permissions that are directly granted to the EIAM organization by calling the ListApplicationsForOrganizationalUnit operation. You can filter applications by configuring the *ApplicationIds** parameter when you call this operation.
        
        @param request: ListApplicationsForOrganizationalUnitRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApplicationsForOrganizationalUnitResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_ids):
            query['ApplicationIds'] = request.application_ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.organizational_unit_id):
            query['OrganizationalUnitId'] = request.organizational_unit_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplicationsForOrganizationalUnit',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListApplicationsForOrganizationalUnitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_applications_for_organizational_unit(
        self,
        request: eiam_20211201_models.ListApplicationsForOrganizationalUnitRequest,
    ) -> eiam_20211201_models.ListApplicationsForOrganizationalUnitResponse:
        """
        @summary Queries the applications that an Employee Identity and Access Management (EIAM) organization can access. The return result includes the IDs of the applications. If you want to obtain the details of the applications, call the GetApplication operation.
        
        @description You can only query the permissions that are directly granted to the EIAM organization by calling the ListApplicationsForOrganizationalUnit operation. You can filter applications by configuring the *ApplicationIds** parameter when you call this operation.
        
        @param request: ListApplicationsForOrganizationalUnitRequest
        @return: ListApplicationsForOrganizationalUnitResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_applications_for_organizational_unit_with_options(request, runtime)

    async def list_applications_for_organizational_unit_async(
        self,
        request: eiam_20211201_models.ListApplicationsForOrganizationalUnitRequest,
    ) -> eiam_20211201_models.ListApplicationsForOrganizationalUnitResponse:
        """
        @summary Queries the applications that an Employee Identity and Access Management (EIAM) organization can access. The return result includes the IDs of the applications. If you want to obtain the details of the applications, call the GetApplication operation.
        
        @description You can only query the permissions that are directly granted to the EIAM organization by calling the ListApplicationsForOrganizationalUnit operation. You can filter applications by configuring the *ApplicationIds** parameter when you call this operation.
        
        @param request: ListApplicationsForOrganizationalUnitRequest
        @return: ListApplicationsForOrganizationalUnitResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_applications_for_organizational_unit_with_options_async(request, runtime)

    def list_applications_for_user_with_options(
        self,
        request: eiam_20211201_models.ListApplicationsForUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListApplicationsForUserResponse:
        """
        @summary Queries the applications that an Employee Identity and Access Management (EIAM) account can access. The return result includes the IDs of the applications. If you want to obtain the details of the applications, call the GetApplication operation.
        
        @param request: ListApplicationsForUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApplicationsForUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_ids):
            query['ApplicationIds'] = request.application_ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_mode):
            query['QueryMode'] = request.query_mode
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplicationsForUser',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListApplicationsForUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_applications_for_user_with_options_async(
        self,
        request: eiam_20211201_models.ListApplicationsForUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListApplicationsForUserResponse:
        """
        @summary Queries the applications that an Employee Identity and Access Management (EIAM) account can access. The return result includes the IDs of the applications. If you want to obtain the details of the applications, call the GetApplication operation.
        
        @param request: ListApplicationsForUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApplicationsForUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_ids):
            query['ApplicationIds'] = request.application_ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_mode):
            query['QueryMode'] = request.query_mode
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplicationsForUser',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListApplicationsForUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_applications_for_user(
        self,
        request: eiam_20211201_models.ListApplicationsForUserRequest,
    ) -> eiam_20211201_models.ListApplicationsForUserResponse:
        """
        @summary Queries the applications that an Employee Identity and Access Management (EIAM) account can access. The return result includes the IDs of the applications. If you want to obtain the details of the applications, call the GetApplication operation.
        
        @param request: ListApplicationsForUserRequest
        @return: ListApplicationsForUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_applications_for_user_with_options(request, runtime)

    async def list_applications_for_user_async(
        self,
        request: eiam_20211201_models.ListApplicationsForUserRequest,
    ) -> eiam_20211201_models.ListApplicationsForUserResponse:
        """
        @summary Queries the applications that an Employee Identity and Access Management (EIAM) account can access. The return result includes the IDs of the applications. If you want to obtain the details of the applications, call the GetApplication operation.
        
        @param request: ListApplicationsForUserRequest
        @return: ListApplicationsForUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_applications_for_user_with_options_async(request, runtime)

    def list_brands_with_options(
        self,
        request: eiam_20211201_models.ListBrandsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListBrandsResponse:
        """
        @summary 获取品牌列表
        
        @param request: ListBrandsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBrandsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.previous_token):
            query['PreviousToken'] = request.previous_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBrands',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListBrandsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_brands_with_options_async(
        self,
        request: eiam_20211201_models.ListBrandsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListBrandsResponse:
        """
        @summary 获取品牌列表
        
        @param request: ListBrandsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBrandsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.previous_token):
            query['PreviousToken'] = request.previous_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBrands',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListBrandsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_brands(
        self,
        request: eiam_20211201_models.ListBrandsRequest,
    ) -> eiam_20211201_models.ListBrandsResponse:
        """
        @summary 获取品牌列表
        
        @param request: ListBrandsRequest
        @return: ListBrandsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_brands_with_options(request, runtime)

    async def list_brands_async(
        self,
        request: eiam_20211201_models.ListBrandsRequest,
    ) -> eiam_20211201_models.ListBrandsResponse:
        """
        @summary 获取品牌列表
        
        @param request: ListBrandsRequest
        @return: ListBrandsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_brands_with_options_async(request, runtime)

    def list_conditional_access_policies_with_options(
        self,
        request: eiam_20211201_models.ListConditionalAccessPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListConditionalAccessPoliciesResponse:
        """
        @summary List of Conditional Access Policies
        
        @description Paginated query for the list of conditional access policies
        
        @param request: ListConditionalAccessPoliciesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConditionalAccessPoliciesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.previous_token):
            query['PreviousToken'] = request.previous_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConditionalAccessPolicies',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListConditionalAccessPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_conditional_access_policies_with_options_async(
        self,
        request: eiam_20211201_models.ListConditionalAccessPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListConditionalAccessPoliciesResponse:
        """
        @summary List of Conditional Access Policies
        
        @description Paginated query for the list of conditional access policies
        
        @param request: ListConditionalAccessPoliciesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConditionalAccessPoliciesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.previous_token):
            query['PreviousToken'] = request.previous_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConditionalAccessPolicies',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListConditionalAccessPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_conditional_access_policies(
        self,
        request: eiam_20211201_models.ListConditionalAccessPoliciesRequest,
    ) -> eiam_20211201_models.ListConditionalAccessPoliciesResponse:
        """
        @summary List of Conditional Access Policies
        
        @description Paginated query for the list of conditional access policies
        
        @param request: ListConditionalAccessPoliciesRequest
        @return: ListConditionalAccessPoliciesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_conditional_access_policies_with_options(request, runtime)

    async def list_conditional_access_policies_async(
        self,
        request: eiam_20211201_models.ListConditionalAccessPoliciesRequest,
    ) -> eiam_20211201_models.ListConditionalAccessPoliciesResponse:
        """
        @summary List of Conditional Access Policies
        
        @description Paginated query for the list of conditional access policies
        
        @param request: ListConditionalAccessPoliciesRequest
        @return: ListConditionalAccessPoliciesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_conditional_access_policies_with_options_async(request, runtime)

    def list_conditional_access_policies_for_application_with_options(
        self,
        request: eiam_20211201_models.ListConditionalAccessPoliciesForApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListConditionalAccessPoliciesForApplicationResponse:
        """
        @summary 获取应用关联的条件访问策略列表
        
        @param request: ListConditionalAccessPoliciesForApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConditionalAccessPoliciesForApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConditionalAccessPoliciesForApplication',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListConditionalAccessPoliciesForApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_conditional_access_policies_for_application_with_options_async(
        self,
        request: eiam_20211201_models.ListConditionalAccessPoliciesForApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListConditionalAccessPoliciesForApplicationResponse:
        """
        @summary 获取应用关联的条件访问策略列表
        
        @param request: ListConditionalAccessPoliciesForApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConditionalAccessPoliciesForApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConditionalAccessPoliciesForApplication',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListConditionalAccessPoliciesForApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_conditional_access_policies_for_application(
        self,
        request: eiam_20211201_models.ListConditionalAccessPoliciesForApplicationRequest,
    ) -> eiam_20211201_models.ListConditionalAccessPoliciesForApplicationResponse:
        """
        @summary 获取应用关联的条件访问策略列表
        
        @param request: ListConditionalAccessPoliciesForApplicationRequest
        @return: ListConditionalAccessPoliciesForApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_conditional_access_policies_for_application_with_options(request, runtime)

    async def list_conditional_access_policies_for_application_async(
        self,
        request: eiam_20211201_models.ListConditionalAccessPoliciesForApplicationRequest,
    ) -> eiam_20211201_models.ListConditionalAccessPoliciesForApplicationResponse:
        """
        @summary 获取应用关联的条件访问策略列表
        
        @param request: ListConditionalAccessPoliciesForApplicationRequest
        @return: ListConditionalAccessPoliciesForApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_conditional_access_policies_for_application_with_options_async(request, runtime)

    def list_conditional_access_policies_for_network_zone_with_options(
        self,
        request: eiam_20211201_models.ListConditionalAccessPoliciesForNetworkZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListConditionalAccessPoliciesForNetworkZoneResponse:
        """
        @summary List Conditional Access Policies Associated with Network Areas
        
        @description List Conditional Access Policies Associated with Network Zones
        
        @param request: ListConditionalAccessPoliciesForNetworkZoneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConditionalAccessPoliciesForNetworkZoneResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_zone_id):
            query['NetworkZoneId'] = request.network_zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConditionalAccessPoliciesForNetworkZone',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListConditionalAccessPoliciesForNetworkZoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_conditional_access_policies_for_network_zone_with_options_async(
        self,
        request: eiam_20211201_models.ListConditionalAccessPoliciesForNetworkZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListConditionalAccessPoliciesForNetworkZoneResponse:
        """
        @summary List Conditional Access Policies Associated with Network Areas
        
        @description List Conditional Access Policies Associated with Network Zones
        
        @param request: ListConditionalAccessPoliciesForNetworkZoneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConditionalAccessPoliciesForNetworkZoneResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_zone_id):
            query['NetworkZoneId'] = request.network_zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConditionalAccessPoliciesForNetworkZone',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListConditionalAccessPoliciesForNetworkZoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_conditional_access_policies_for_network_zone(
        self,
        request: eiam_20211201_models.ListConditionalAccessPoliciesForNetworkZoneRequest,
    ) -> eiam_20211201_models.ListConditionalAccessPoliciesForNetworkZoneResponse:
        """
        @summary List Conditional Access Policies Associated with Network Areas
        
        @description List Conditional Access Policies Associated with Network Zones
        
        @param request: ListConditionalAccessPoliciesForNetworkZoneRequest
        @return: ListConditionalAccessPoliciesForNetworkZoneResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_conditional_access_policies_for_network_zone_with_options(request, runtime)

    async def list_conditional_access_policies_for_network_zone_async(
        self,
        request: eiam_20211201_models.ListConditionalAccessPoliciesForNetworkZoneRequest,
    ) -> eiam_20211201_models.ListConditionalAccessPoliciesForNetworkZoneResponse:
        """
        @summary List Conditional Access Policies Associated with Network Areas
        
        @description List Conditional Access Policies Associated with Network Zones
        
        @param request: ListConditionalAccessPoliciesForNetworkZoneRequest
        @return: ListConditionalAccessPoliciesForNetworkZoneResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_conditional_access_policies_for_network_zone_with_options_async(request, runtime)

    def list_conditional_access_policies_for_user_with_options(
        self,
        request: eiam_20211201_models.ListConditionalAccessPoliciesForUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListConditionalAccessPoliciesForUserResponse:
        """
        @summary 获取用户关联的条件访问策略列表
        
        @param request: ListConditionalAccessPoliciesForUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConditionalAccessPoliciesForUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConditionalAccessPoliciesForUser',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListConditionalAccessPoliciesForUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_conditional_access_policies_for_user_with_options_async(
        self,
        request: eiam_20211201_models.ListConditionalAccessPoliciesForUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListConditionalAccessPoliciesForUserResponse:
        """
        @summary 获取用户关联的条件访问策略列表
        
        @param request: ListConditionalAccessPoliciesForUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConditionalAccessPoliciesForUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConditionalAccessPoliciesForUser',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListConditionalAccessPoliciesForUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_conditional_access_policies_for_user(
        self,
        request: eiam_20211201_models.ListConditionalAccessPoliciesForUserRequest,
    ) -> eiam_20211201_models.ListConditionalAccessPoliciesForUserResponse:
        """
        @summary 获取用户关联的条件访问策略列表
        
        @param request: ListConditionalAccessPoliciesForUserRequest
        @return: ListConditionalAccessPoliciesForUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_conditional_access_policies_for_user_with_options(request, runtime)

    async def list_conditional_access_policies_for_user_async(
        self,
        request: eiam_20211201_models.ListConditionalAccessPoliciesForUserRequest,
    ) -> eiam_20211201_models.ListConditionalAccessPoliciesForUserResponse:
        """
        @summary 获取用户关联的条件访问策略列表
        
        @param request: ListConditionalAccessPoliciesForUserRequest
        @return: ListConditionalAccessPoliciesForUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_conditional_access_policies_for_user_with_options_async(request, runtime)

    def list_custom_privacy_policies_with_options(
        self,
        request: eiam_20211201_models.ListCustomPrivacyPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListCustomPrivacyPoliciesResponse:
        """
        @summary 自定义条款列表查询。
        
        @param request: ListCustomPrivacyPoliciesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCustomPrivacyPoliciesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_privacy_policy_name_starts_with):
            query['CustomPrivacyPolicyNameStartsWith'] = request.custom_privacy_policy_name_starts_with
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.previous_token):
            query['PreviousToken'] = request.previous_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCustomPrivacyPolicies',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListCustomPrivacyPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_custom_privacy_policies_with_options_async(
        self,
        request: eiam_20211201_models.ListCustomPrivacyPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListCustomPrivacyPoliciesResponse:
        """
        @summary 自定义条款列表查询。
        
        @param request: ListCustomPrivacyPoliciesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCustomPrivacyPoliciesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_privacy_policy_name_starts_with):
            query['CustomPrivacyPolicyNameStartsWith'] = request.custom_privacy_policy_name_starts_with
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.previous_token):
            query['PreviousToken'] = request.previous_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCustomPrivacyPolicies',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListCustomPrivacyPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_custom_privacy_policies(
        self,
        request: eiam_20211201_models.ListCustomPrivacyPoliciesRequest,
    ) -> eiam_20211201_models.ListCustomPrivacyPoliciesResponse:
        """
        @summary 自定义条款列表查询。
        
        @param request: ListCustomPrivacyPoliciesRequest
        @return: ListCustomPrivacyPoliciesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_custom_privacy_policies_with_options(request, runtime)

    async def list_custom_privacy_policies_async(
        self,
        request: eiam_20211201_models.ListCustomPrivacyPoliciesRequest,
    ) -> eiam_20211201_models.ListCustomPrivacyPoliciesResponse:
        """
        @summary 自定义条款列表查询。
        
        @param request: ListCustomPrivacyPoliciesRequest
        @return: ListCustomPrivacyPoliciesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_custom_privacy_policies_with_options_async(request, runtime)

    def list_custom_privacy_policies_for_brand_with_options(
        self,
        request: eiam_20211201_models.ListCustomPrivacyPoliciesForBrandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListCustomPrivacyPoliciesForBrandResponse:
        """
        @summary 获取品牌关联资源的资源
        
        @param request: ListCustomPrivacyPoliciesForBrandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCustomPrivacyPoliciesForBrandResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.brand_id):
            query['BrandId'] = request.brand_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.previous_token):
            query['PreviousToken'] = request.previous_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCustomPrivacyPoliciesForBrand',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListCustomPrivacyPoliciesForBrandResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_custom_privacy_policies_for_brand_with_options_async(
        self,
        request: eiam_20211201_models.ListCustomPrivacyPoliciesForBrandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListCustomPrivacyPoliciesForBrandResponse:
        """
        @summary 获取品牌关联资源的资源
        
        @param request: ListCustomPrivacyPoliciesForBrandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCustomPrivacyPoliciesForBrandResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.brand_id):
            query['BrandId'] = request.brand_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.previous_token):
            query['PreviousToken'] = request.previous_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCustomPrivacyPoliciesForBrand',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListCustomPrivacyPoliciesForBrandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_custom_privacy_policies_for_brand(
        self,
        request: eiam_20211201_models.ListCustomPrivacyPoliciesForBrandRequest,
    ) -> eiam_20211201_models.ListCustomPrivacyPoliciesForBrandResponse:
        """
        @summary 获取品牌关联资源的资源
        
        @param request: ListCustomPrivacyPoliciesForBrandRequest
        @return: ListCustomPrivacyPoliciesForBrandResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_custom_privacy_policies_for_brand_with_options(request, runtime)

    async def list_custom_privacy_policies_for_brand_async(
        self,
        request: eiam_20211201_models.ListCustomPrivacyPoliciesForBrandRequest,
    ) -> eiam_20211201_models.ListCustomPrivacyPoliciesForBrandResponse:
        """
        @summary 获取品牌关联资源的资源
        
        @param request: ListCustomPrivacyPoliciesForBrandRequest
        @return: ListCustomPrivacyPoliciesForBrandResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_custom_privacy_policies_for_brand_with_options_async(request, runtime)

    def list_domain_proxy_tokens_with_options(
        self,
        request: eiam_20211201_models.ListDomainProxyTokensRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListDomainProxyTokensResponse:
        """
        @summary Queries the proxy tokens of a domain name of an Employee Identity and Access Management (EIAM) instance.
        
        @param request: ListDomainProxyTokensRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDomainProxyTokensResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDomainProxyTokens',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListDomainProxyTokensResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_domain_proxy_tokens_with_options_async(
        self,
        request: eiam_20211201_models.ListDomainProxyTokensRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListDomainProxyTokensResponse:
        """
        @summary Queries the proxy tokens of a domain name of an Employee Identity and Access Management (EIAM) instance.
        
        @param request: ListDomainProxyTokensRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDomainProxyTokensResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDomainProxyTokens',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListDomainProxyTokensResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_domain_proxy_tokens(
        self,
        request: eiam_20211201_models.ListDomainProxyTokensRequest,
    ) -> eiam_20211201_models.ListDomainProxyTokensResponse:
        """
        @summary Queries the proxy tokens of a domain name of an Employee Identity and Access Management (EIAM) instance.
        
        @param request: ListDomainProxyTokensRequest
        @return: ListDomainProxyTokensResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_domain_proxy_tokens_with_options(request, runtime)

    async def list_domain_proxy_tokens_async(
        self,
        request: eiam_20211201_models.ListDomainProxyTokensRequest,
    ) -> eiam_20211201_models.ListDomainProxyTokensResponse:
        """
        @summary Queries the proxy tokens of a domain name of an Employee Identity and Access Management (EIAM) instance.
        
        @param request: ListDomainProxyTokensRequest
        @return: ListDomainProxyTokensResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_domain_proxy_tokens_with_options_async(request, runtime)

    def list_domains_with_options(
        self,
        request: eiam_20211201_models.ListDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListDomainsResponse:
        """
        @summary Queries a list of domain names of an Employee Identity and Access Management (EIAM) instance. The list contains the initial domain name and custom domain names.
        
        @param request: ListDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDomainsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.brand_id):
            query['BrandId'] = request.brand_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDomains',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_domains_with_options_async(
        self,
        request: eiam_20211201_models.ListDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListDomainsResponse:
        """
        @summary Queries a list of domain names of an Employee Identity and Access Management (EIAM) instance. The list contains the initial domain name and custom domain names.
        
        @param request: ListDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDomainsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.brand_id):
            query['BrandId'] = request.brand_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDomains',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_domains(
        self,
        request: eiam_20211201_models.ListDomainsRequest,
    ) -> eiam_20211201_models.ListDomainsResponse:
        """
        @summary Queries a list of domain names of an Employee Identity and Access Management (EIAM) instance. The list contains the initial domain name and custom domain names.
        
        @param request: ListDomainsRequest
        @return: ListDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_domains_with_options(request, runtime)

    async def list_domains_async(
        self,
        request: eiam_20211201_models.ListDomainsRequest,
    ) -> eiam_20211201_models.ListDomainsResponse:
        """
        @summary Queries a list of domain names of an Employee Identity and Access Management (EIAM) instance. The list contains the initial domain name and custom domain names.
        
        @param request: ListDomainsRequest
        @return: ListDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_domains_with_options_async(request, runtime)

    def list_eiam_instances_with_options(
        self,
        request: eiam_20211201_models.ListEiamInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListEiamInstancesResponse:
        """
        @summary Queries the information about Employee Identity and Access Management (EIAM) V1.0 instances or EIAM V2.0 instances.
        
        @param request: ListEiamInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEiamInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.instance_region_id):
            query['InstanceRegionId'] = request.instance_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEiamInstances',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListEiamInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_eiam_instances_with_options_async(
        self,
        request: eiam_20211201_models.ListEiamInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListEiamInstancesResponse:
        """
        @summary Queries the information about Employee Identity and Access Management (EIAM) V1.0 instances or EIAM V2.0 instances.
        
        @param request: ListEiamInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEiamInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.instance_region_id):
            query['InstanceRegionId'] = request.instance_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEiamInstances',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListEiamInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_eiam_instances(
        self,
        request: eiam_20211201_models.ListEiamInstancesRequest,
    ) -> eiam_20211201_models.ListEiamInstancesResponse:
        """
        @summary Queries the information about Employee Identity and Access Management (EIAM) V1.0 instances or EIAM V2.0 instances.
        
        @param request: ListEiamInstancesRequest
        @return: ListEiamInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_eiam_instances_with_options(request, runtime)

    async def list_eiam_instances_async(
        self,
        request: eiam_20211201_models.ListEiamInstancesRequest,
    ) -> eiam_20211201_models.ListEiamInstancesResponse:
        """
        @summary Queries the information about Employee Identity and Access Management (EIAM) V1.0 instances or EIAM V2.0 instances.
        
        @param request: ListEiamInstancesRequest
        @return: ListEiamInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_eiam_instances_with_options_async(request, runtime)

    def list_eiam_regions_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListEiamRegionsResponse:
        """
        @summary Queries the regions in which Employee Identity and Access Management (EIAM) V1.0 instances or EIAM V2.0 instances reside.
        
        @param request: ListEiamRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEiamRegionsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListEiamRegions',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListEiamRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_eiam_regions_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListEiamRegionsResponse:
        """
        @summary Queries the regions in which Employee Identity and Access Management (EIAM) V1.0 instances or EIAM V2.0 instances reside.
        
        @param request: ListEiamRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEiamRegionsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListEiamRegions',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListEiamRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_eiam_regions(self) -> eiam_20211201_models.ListEiamRegionsResponse:
        """
        @summary Queries the regions in which Employee Identity and Access Management (EIAM) V1.0 instances or EIAM V2.0 instances reside.
        
        @return: ListEiamRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_eiam_regions_with_options(runtime)

    async def list_eiam_regions_async(self) -> eiam_20211201_models.ListEiamRegionsResponse:
        """
        @summary Queries the regions in which Employee Identity and Access Management (EIAM) V1.0 instances or EIAM V2.0 instances reside.
        
        @return: ListEiamRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_eiam_regions_with_options_async(runtime)

    def list_federated_credential_providers_with_options(
        self,
        request: eiam_20211201_models.ListFederatedCredentialProvidersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListFederatedCredentialProvidersResponse:
        """
        @summary 查询联邦凭证提供方列表
        
        @param request: ListFederatedCredentialProvidersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFederatedCredentialProvidersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.federated_credential_provider_name):
            query['FederatedCredentialProviderName'] = request.federated_credential_provider_name
        if not UtilClient.is_unset(request.federated_credential_provider_type):
            query['FederatedCredentialProviderType'] = request.federated_credential_provider_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.previous_token):
            query['PreviousToken'] = request.previous_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFederatedCredentialProviders',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListFederatedCredentialProvidersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_federated_credential_providers_with_options_async(
        self,
        request: eiam_20211201_models.ListFederatedCredentialProvidersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListFederatedCredentialProvidersResponse:
        """
        @summary 查询联邦凭证提供方列表
        
        @param request: ListFederatedCredentialProvidersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFederatedCredentialProvidersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.federated_credential_provider_name):
            query['FederatedCredentialProviderName'] = request.federated_credential_provider_name
        if not UtilClient.is_unset(request.federated_credential_provider_type):
            query['FederatedCredentialProviderType'] = request.federated_credential_provider_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.previous_token):
            query['PreviousToken'] = request.previous_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFederatedCredentialProviders',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListFederatedCredentialProvidersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_federated_credential_providers(
        self,
        request: eiam_20211201_models.ListFederatedCredentialProvidersRequest,
    ) -> eiam_20211201_models.ListFederatedCredentialProvidersResponse:
        """
        @summary 查询联邦凭证提供方列表
        
        @param request: ListFederatedCredentialProvidersRequest
        @return: ListFederatedCredentialProvidersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_federated_credential_providers_with_options(request, runtime)

    async def list_federated_credential_providers_async(
        self,
        request: eiam_20211201_models.ListFederatedCredentialProvidersRequest,
    ) -> eiam_20211201_models.ListFederatedCredentialProvidersResponse:
        """
        @summary 查询联邦凭证提供方列表
        
        @param request: ListFederatedCredentialProvidersRequest
        @return: ListFederatedCredentialProvidersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_federated_credential_providers_with_options_async(request, runtime)

    def list_groups_with_options(
        self,
        request: eiam_20211201_models.ListGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListGroupsResponse:
        """
        @summary Queries a list of account groups in Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM).
        
        @param request: ListGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_external_id):
            query['GroupExternalId'] = request.group_external_id
        if not UtilClient.is_unset(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.group_name_starts_with):
            query['GroupNameStartsWith'] = request.group_name_starts_with
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroups',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_groups_with_options_async(
        self,
        request: eiam_20211201_models.ListGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListGroupsResponse:
        """
        @summary Queries a list of account groups in Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM).
        
        @param request: ListGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_external_id):
            query['GroupExternalId'] = request.group_external_id
        if not UtilClient.is_unset(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.group_name_starts_with):
            query['GroupNameStartsWith'] = request.group_name_starts_with
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroups',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_groups(
        self,
        request: eiam_20211201_models.ListGroupsRequest,
    ) -> eiam_20211201_models.ListGroupsResponse:
        """
        @summary Queries a list of account groups in Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM).
        
        @param request: ListGroupsRequest
        @return: ListGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_groups_with_options(request, runtime)

    async def list_groups_async(
        self,
        request: eiam_20211201_models.ListGroupsRequest,
    ) -> eiam_20211201_models.ListGroupsResponse:
        """
        @summary Queries a list of account groups in Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM).
        
        @param request: ListGroupsRequest
        @return: ListGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_groups_with_options_async(request, runtime)

    def list_groups_for_application_with_options(
        self,
        request: eiam_20211201_models.ListGroupsForApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListGroupsForApplicationResponse:
        """
        @summary Queries a list of account groups to which the permissions to access an application are granted. The returned results contain the group IDs. You can call the GetGroup operation to query the information about an account group based on the group ID.
        
        @param request: ListGroupsForApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGroupsForApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroupsForApplication',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListGroupsForApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_groups_for_application_with_options_async(
        self,
        request: eiam_20211201_models.ListGroupsForApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListGroupsForApplicationResponse:
        """
        @summary Queries a list of account groups to which the permissions to access an application are granted. The returned results contain the group IDs. You can call the GetGroup operation to query the information about an account group based on the group ID.
        
        @param request: ListGroupsForApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGroupsForApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroupsForApplication',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListGroupsForApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_groups_for_application(
        self,
        request: eiam_20211201_models.ListGroupsForApplicationRequest,
    ) -> eiam_20211201_models.ListGroupsForApplicationResponse:
        """
        @summary Queries a list of account groups to which the permissions to access an application are granted. The returned results contain the group IDs. You can call the GetGroup operation to query the information about an account group based on the group ID.
        
        @param request: ListGroupsForApplicationRequest
        @return: ListGroupsForApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_groups_for_application_with_options(request, runtime)

    async def list_groups_for_application_async(
        self,
        request: eiam_20211201_models.ListGroupsForApplicationRequest,
    ) -> eiam_20211201_models.ListGroupsForApplicationResponse:
        """
        @summary Queries a list of account groups to which the permissions to access an application are granted. The returned results contain the group IDs. You can call the GetGroup operation to query the information about an account group based on the group ID.
        
        @param request: ListGroupsForApplicationRequest
        @return: ListGroupsForApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_groups_for_application_with_options_async(request, runtime)

    def list_groups_for_user_with_options(
        self,
        request: eiam_20211201_models.ListGroupsForUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListGroupsForUserResponse:
        """
        @summary Queries a list of account groups to which an Employee Identity and Access Management (EIAM) account of Identity as a Service (IDaaS) belongs.
        
        @param request: ListGroupsForUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGroupsForUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroupsForUser',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListGroupsForUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_groups_for_user_with_options_async(
        self,
        request: eiam_20211201_models.ListGroupsForUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListGroupsForUserResponse:
        """
        @summary Queries a list of account groups to which an Employee Identity and Access Management (EIAM) account of Identity as a Service (IDaaS) belongs.
        
        @param request: ListGroupsForUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGroupsForUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroupsForUser',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListGroupsForUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_groups_for_user(
        self,
        request: eiam_20211201_models.ListGroupsForUserRequest,
    ) -> eiam_20211201_models.ListGroupsForUserResponse:
        """
        @summary Queries a list of account groups to which an Employee Identity and Access Management (EIAM) account of Identity as a Service (IDaaS) belongs.
        
        @param request: ListGroupsForUserRequest
        @return: ListGroupsForUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_groups_for_user_with_options(request, runtime)

    async def list_groups_for_user_async(
        self,
        request: eiam_20211201_models.ListGroupsForUserRequest,
    ) -> eiam_20211201_models.ListGroupsForUserResponse:
        """
        @summary Queries a list of account groups to which an Employee Identity and Access Management (EIAM) account of Identity as a Service (IDaaS) belongs.
        
        @param request: ListGroupsForUserRequest
        @return: ListGroupsForUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_groups_for_user_with_options_async(request, runtime)

    def list_identity_providers_with_options(
        self,
        request: eiam_20211201_models.ListIdentityProvidersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListIdentityProvidersResponse:
        """
        @summary Query the list of identity providers.
        
        @param request: ListIdentityProvidersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIdentityProvidersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIdentityProviders',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListIdentityProvidersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_identity_providers_with_options_async(
        self,
        request: eiam_20211201_models.ListIdentityProvidersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListIdentityProvidersResponse:
        """
        @summary Query the list of identity providers.
        
        @param request: ListIdentityProvidersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIdentityProvidersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIdentityProviders',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListIdentityProvidersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_identity_providers(
        self,
        request: eiam_20211201_models.ListIdentityProvidersRequest,
    ) -> eiam_20211201_models.ListIdentityProvidersResponse:
        """
        @summary Query the list of identity providers.
        
        @param request: ListIdentityProvidersRequest
        @return: ListIdentityProvidersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_identity_providers_with_options(request, runtime)

    async def list_identity_providers_async(
        self,
        request: eiam_20211201_models.ListIdentityProvidersRequest,
    ) -> eiam_20211201_models.ListIdentityProvidersResponse:
        """
        @summary Query the list of identity providers.
        
        @param request: ListIdentityProvidersRequest
        @return: ListIdentityProvidersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_identity_providers_with_options_async(request, runtime)

    def list_identity_providers_for_network_access_endpoint_with_options(
        self,
        request: eiam_20211201_models.ListIdentityProvidersForNetworkAccessEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListIdentityProvidersForNetworkAccessEndpointResponse:
        """
        @summary 获取网络端点下的IdP信息。
        
        @param request: ListIdentityProvidersForNetworkAccessEndpointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIdentityProvidersForNetworkAccessEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.network_access_endpoint_id):
            query['NetworkAccessEndpointId'] = request.network_access_endpoint_id
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIdentityProvidersForNetworkAccessEndpoint',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListIdentityProvidersForNetworkAccessEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_identity_providers_for_network_access_endpoint_with_options_async(
        self,
        request: eiam_20211201_models.ListIdentityProvidersForNetworkAccessEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListIdentityProvidersForNetworkAccessEndpointResponse:
        """
        @summary 获取网络端点下的IdP信息。
        
        @param request: ListIdentityProvidersForNetworkAccessEndpointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIdentityProvidersForNetworkAccessEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.network_access_endpoint_id):
            query['NetworkAccessEndpointId'] = request.network_access_endpoint_id
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIdentityProvidersForNetworkAccessEndpoint',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListIdentityProvidersForNetworkAccessEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_identity_providers_for_network_access_endpoint(
        self,
        request: eiam_20211201_models.ListIdentityProvidersForNetworkAccessEndpointRequest,
    ) -> eiam_20211201_models.ListIdentityProvidersForNetworkAccessEndpointResponse:
        """
        @summary 获取网络端点下的IdP信息。
        
        @param request: ListIdentityProvidersForNetworkAccessEndpointRequest
        @return: ListIdentityProvidersForNetworkAccessEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_identity_providers_for_network_access_endpoint_with_options(request, runtime)

    async def list_identity_providers_for_network_access_endpoint_async(
        self,
        request: eiam_20211201_models.ListIdentityProvidersForNetworkAccessEndpointRequest,
    ) -> eiam_20211201_models.ListIdentityProvidersForNetworkAccessEndpointResponse:
        """
        @summary 获取网络端点下的IdP信息。
        
        @param request: ListIdentityProvidersForNetworkAccessEndpointRequest
        @return: ListIdentityProvidersForNetworkAccessEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_identity_providers_for_network_access_endpoint_with_options_async(request, runtime)

    def list_instances_with_options(
        self,
        request: eiam_20211201_models.ListInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListInstancesResponse:
        """
        @summary Queries the information of one or more Enterprise Identity and Access Management (EIAM) instances of Identity as a Service (IDaaS).
        
        @param request: ListInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        request: eiam_20211201_models.ListInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListInstancesResponse:
        """
        @summary Queries the information of one or more Enterprise Identity and Access Management (EIAM) instances of Identity as a Service (IDaaS).
        
        @param request: ListInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instances(
        self,
        request: eiam_20211201_models.ListInstancesRequest,
    ) -> eiam_20211201_models.ListInstancesResponse:
        """
        @summary Queries the information of one or more Enterprise Identity and Access Management (EIAM) instances of Identity as a Service (IDaaS).
        
        @param request: ListInstancesRequest
        @return: ListInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_instances_with_options(request, runtime)

    async def list_instances_async(
        self,
        request: eiam_20211201_models.ListInstancesRequest,
    ) -> eiam_20211201_models.ListInstancesResponse:
        """
        @summary Queries the information of one or more Enterprise Identity and Access Management (EIAM) instances of Identity as a Service (IDaaS).
        
        @param request: ListInstancesRequest
        @return: ListInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_instances_with_options_async(request, runtime)

    def list_network_access_endpoint_available_regions_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListNetworkAccessEndpointAvailableRegionsResponse:
        """
        @summary Get a list of regions that support network access endpoints.
        
        @param request: ListNetworkAccessEndpointAvailableRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNetworkAccessEndpointAvailableRegionsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListNetworkAccessEndpointAvailableRegions',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListNetworkAccessEndpointAvailableRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_network_access_endpoint_available_regions_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListNetworkAccessEndpointAvailableRegionsResponse:
        """
        @summary Get a list of regions that support network access endpoints.
        
        @param request: ListNetworkAccessEndpointAvailableRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNetworkAccessEndpointAvailableRegionsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListNetworkAccessEndpointAvailableRegions',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListNetworkAccessEndpointAvailableRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_network_access_endpoint_available_regions(self) -> eiam_20211201_models.ListNetworkAccessEndpointAvailableRegionsResponse:
        """
        @summary Get a list of regions that support network access endpoints.
        
        @return: ListNetworkAccessEndpointAvailableRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_network_access_endpoint_available_regions_with_options(runtime)

    async def list_network_access_endpoint_available_regions_async(self) -> eiam_20211201_models.ListNetworkAccessEndpointAvailableRegionsResponse:
        """
        @summary Get a list of regions that support network access endpoints.
        
        @return: ListNetworkAccessEndpointAvailableRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_network_access_endpoint_available_regions_with_options_async(runtime)

    def list_network_access_endpoint_available_zones_with_options(
        self,
        request: eiam_20211201_models.ListNetworkAccessEndpointAvailableZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListNetworkAccessEndpointAvailableZonesResponse:
        """
        @summary 获取支持NAE的可用区列表
        
        @param request: ListNetworkAccessEndpointAvailableZonesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNetworkAccessEndpointAvailableZonesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.nae_region_id):
            query['NaeRegionId'] = request.nae_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNetworkAccessEndpointAvailableZones',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListNetworkAccessEndpointAvailableZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_network_access_endpoint_available_zones_with_options_async(
        self,
        request: eiam_20211201_models.ListNetworkAccessEndpointAvailableZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListNetworkAccessEndpointAvailableZonesResponse:
        """
        @summary 获取支持NAE的可用区列表
        
        @param request: ListNetworkAccessEndpointAvailableZonesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNetworkAccessEndpointAvailableZonesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.nae_region_id):
            query['NaeRegionId'] = request.nae_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNetworkAccessEndpointAvailableZones',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListNetworkAccessEndpointAvailableZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_network_access_endpoint_available_zones(
        self,
        request: eiam_20211201_models.ListNetworkAccessEndpointAvailableZonesRequest,
    ) -> eiam_20211201_models.ListNetworkAccessEndpointAvailableZonesResponse:
        """
        @summary 获取支持NAE的可用区列表
        
        @param request: ListNetworkAccessEndpointAvailableZonesRequest
        @return: ListNetworkAccessEndpointAvailableZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_network_access_endpoint_available_zones_with_options(request, runtime)

    async def list_network_access_endpoint_available_zones_async(
        self,
        request: eiam_20211201_models.ListNetworkAccessEndpointAvailableZonesRequest,
    ) -> eiam_20211201_models.ListNetworkAccessEndpointAvailableZonesResponse:
        """
        @summary 获取支持NAE的可用区列表
        
        @param request: ListNetworkAccessEndpointAvailableZonesRequest
        @return: ListNetworkAccessEndpointAvailableZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_network_access_endpoint_available_zones_with_options_async(request, runtime)

    def list_network_access_endpoints_with_options(
        self,
        request: eiam_20211201_models.ListNetworkAccessEndpointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListNetworkAccessEndpointsResponse:
        """
        @summary 列表查询专属网络端点。
        
        @param request: ListNetworkAccessEndpointsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNetworkAccessEndpointsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.network_access_endpoint_status):
            query['NetworkAccessEndpointStatus'] = request.network_access_endpoint_status
        if not UtilClient.is_unset(request.network_access_endpoint_type):
            query['NetworkAccessEndpointType'] = request.network_access_endpoint_type
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vpc_region_id):
            query['VpcRegionId'] = request.vpc_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNetworkAccessEndpoints',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListNetworkAccessEndpointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_network_access_endpoints_with_options_async(
        self,
        request: eiam_20211201_models.ListNetworkAccessEndpointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListNetworkAccessEndpointsResponse:
        """
        @summary 列表查询专属网络端点。
        
        @param request: ListNetworkAccessEndpointsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNetworkAccessEndpointsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.network_access_endpoint_status):
            query['NetworkAccessEndpointStatus'] = request.network_access_endpoint_status
        if not UtilClient.is_unset(request.network_access_endpoint_type):
            query['NetworkAccessEndpointType'] = request.network_access_endpoint_type
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vpc_region_id):
            query['VpcRegionId'] = request.vpc_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNetworkAccessEndpoints',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListNetworkAccessEndpointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_network_access_endpoints(
        self,
        request: eiam_20211201_models.ListNetworkAccessEndpointsRequest,
    ) -> eiam_20211201_models.ListNetworkAccessEndpointsResponse:
        """
        @summary 列表查询专属网络端点。
        
        @param request: ListNetworkAccessEndpointsRequest
        @return: ListNetworkAccessEndpointsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_network_access_endpoints_with_options(request, runtime)

    async def list_network_access_endpoints_async(
        self,
        request: eiam_20211201_models.ListNetworkAccessEndpointsRequest,
    ) -> eiam_20211201_models.ListNetworkAccessEndpointsResponse:
        """
        @summary 列表查询专属网络端点。
        
        @param request: ListNetworkAccessEndpointsRequest
        @return: ListNetworkAccessEndpointsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_network_access_endpoints_with_options_async(request, runtime)

    def list_network_access_paths_with_options(
        self,
        request: eiam_20211201_models.ListNetworkAccessPathsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListNetworkAccessPathsResponse:
        """
        @summary List the access paths under a certain network access endpoint.
        
        @param request: ListNetworkAccessPathsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNetworkAccessPathsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_access_endpoint_id):
            query['NetworkAccessEndpointId'] = request.network_access_endpoint_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNetworkAccessPaths',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListNetworkAccessPathsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_network_access_paths_with_options_async(
        self,
        request: eiam_20211201_models.ListNetworkAccessPathsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListNetworkAccessPathsResponse:
        """
        @summary List the access paths under a certain network access endpoint.
        
        @param request: ListNetworkAccessPathsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNetworkAccessPathsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_access_endpoint_id):
            query['NetworkAccessEndpointId'] = request.network_access_endpoint_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNetworkAccessPaths',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListNetworkAccessPathsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_network_access_paths(
        self,
        request: eiam_20211201_models.ListNetworkAccessPathsRequest,
    ) -> eiam_20211201_models.ListNetworkAccessPathsResponse:
        """
        @summary List the access paths under a certain network access endpoint.
        
        @param request: ListNetworkAccessPathsRequest
        @return: ListNetworkAccessPathsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_network_access_paths_with_options(request, runtime)

    async def list_network_access_paths_async(
        self,
        request: eiam_20211201_models.ListNetworkAccessPathsRequest,
    ) -> eiam_20211201_models.ListNetworkAccessPathsResponse:
        """
        @summary List the access paths under a certain network access endpoint.
        
        @param request: ListNetworkAccessPathsRequest
        @return: ListNetworkAccessPathsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_network_access_paths_with_options_async(request, runtime)

    def list_network_zones_with_options(
        self,
        request: eiam_20211201_models.ListNetworkZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListNetworkZonesResponse:
        """
        @summary 网络区域对象列表
        
        @param request: ListNetworkZonesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNetworkZonesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.network_zone_ids):
            query['NetworkZoneIds'] = request.network_zone_ids
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.previous_token):
            query['PreviousToken'] = request.previous_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNetworkZones',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListNetworkZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_network_zones_with_options_async(
        self,
        request: eiam_20211201_models.ListNetworkZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListNetworkZonesResponse:
        """
        @summary 网络区域对象列表
        
        @param request: ListNetworkZonesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNetworkZonesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.network_zone_ids):
            query['NetworkZoneIds'] = request.network_zone_ids
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.previous_token):
            query['PreviousToken'] = request.previous_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNetworkZones',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListNetworkZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_network_zones(
        self,
        request: eiam_20211201_models.ListNetworkZonesRequest,
    ) -> eiam_20211201_models.ListNetworkZonesResponse:
        """
        @summary 网络区域对象列表
        
        @param request: ListNetworkZonesRequest
        @return: ListNetworkZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_network_zones_with_options(request, runtime)

    async def list_network_zones_async(
        self,
        request: eiam_20211201_models.ListNetworkZonesRequest,
    ) -> eiam_20211201_models.ListNetworkZonesResponse:
        """
        @summary 网络区域对象列表
        
        @param request: ListNetworkZonesRequest
        @return: ListNetworkZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_network_zones_with_options_async(request, runtime)

    def list_organizational_unit_parents_with_options(
        self,
        request: eiam_20211201_models.ListOrganizationalUnitParentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListOrganizationalUnitParentsResponse:
        """
        @summary Queries all parent organizations of an Employee Identity and Access Management (EIAM) organization.
        
        @param request: ListOrganizationalUnitParentsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOrganizationalUnitParentsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.organizational_unit_id):
            query['OrganizationalUnitId'] = request.organizational_unit_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOrganizationalUnitParents',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListOrganizationalUnitParentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_organizational_unit_parents_with_options_async(
        self,
        request: eiam_20211201_models.ListOrganizationalUnitParentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListOrganizationalUnitParentsResponse:
        """
        @summary Queries all parent organizations of an Employee Identity and Access Management (EIAM) organization.
        
        @param request: ListOrganizationalUnitParentsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOrganizationalUnitParentsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.organizational_unit_id):
            query['OrganizationalUnitId'] = request.organizational_unit_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOrganizationalUnitParents',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListOrganizationalUnitParentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_organizational_unit_parents(
        self,
        request: eiam_20211201_models.ListOrganizationalUnitParentsRequest,
    ) -> eiam_20211201_models.ListOrganizationalUnitParentsResponse:
        """
        @summary Queries all parent organizations of an Employee Identity and Access Management (EIAM) organization.
        
        @param request: ListOrganizationalUnitParentsRequest
        @return: ListOrganizationalUnitParentsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_organizational_unit_parents_with_options(request, runtime)

    async def list_organizational_unit_parents_async(
        self,
        request: eiam_20211201_models.ListOrganizationalUnitParentsRequest,
    ) -> eiam_20211201_models.ListOrganizationalUnitParentsResponse:
        """
        @summary Queries all parent organizations of an Employee Identity and Access Management (EIAM) organization.
        
        @param request: ListOrganizationalUnitParentsRequest
        @return: ListOrganizationalUnitParentsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_organizational_unit_parents_with_options_async(request, runtime)

    def list_organizational_units_with_options(
        self,
        request: eiam_20211201_models.ListOrganizationalUnitsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListOrganizationalUnitsResponse:
        """
        @summary Queries the information about organizational units in Identity as a Service (IDaaS) Employee IAM (EIAM) by page.
        
        @param request: ListOrganizationalUnitsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOrganizationalUnitsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.organizational_unit_ids):
            query['OrganizationalUnitIds'] = request.organizational_unit_ids
        if not UtilClient.is_unset(request.organizational_unit_name):
            query['OrganizationalUnitName'] = request.organizational_unit_name
        if not UtilClient.is_unset(request.organizational_unit_name_starts_with):
            query['OrganizationalUnitNameStartsWith'] = request.organizational_unit_name_starts_with
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_id):
            query['ParentId'] = request.parent_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOrganizationalUnits',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListOrganizationalUnitsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_organizational_units_with_options_async(
        self,
        request: eiam_20211201_models.ListOrganizationalUnitsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListOrganizationalUnitsResponse:
        """
        @summary Queries the information about organizational units in Identity as a Service (IDaaS) Employee IAM (EIAM) by page.
        
        @param request: ListOrganizationalUnitsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOrganizationalUnitsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.organizational_unit_ids):
            query['OrganizationalUnitIds'] = request.organizational_unit_ids
        if not UtilClient.is_unset(request.organizational_unit_name):
            query['OrganizationalUnitName'] = request.organizational_unit_name
        if not UtilClient.is_unset(request.organizational_unit_name_starts_with):
            query['OrganizationalUnitNameStartsWith'] = request.organizational_unit_name_starts_with
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_id):
            query['ParentId'] = request.parent_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOrganizationalUnits',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListOrganizationalUnitsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_organizational_units(
        self,
        request: eiam_20211201_models.ListOrganizationalUnitsRequest,
    ) -> eiam_20211201_models.ListOrganizationalUnitsResponse:
        """
        @summary Queries the information about organizational units in Identity as a Service (IDaaS) Employee IAM (EIAM) by page.
        
        @param request: ListOrganizationalUnitsRequest
        @return: ListOrganizationalUnitsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_organizational_units_with_options(request, runtime)

    async def list_organizational_units_async(
        self,
        request: eiam_20211201_models.ListOrganizationalUnitsRequest,
    ) -> eiam_20211201_models.ListOrganizationalUnitsResponse:
        """
        @summary Queries the information about organizational units in Identity as a Service (IDaaS) Employee IAM (EIAM) by page.
        
        @param request: ListOrganizationalUnitsRequest
        @return: ListOrganizationalUnitsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_organizational_units_with_options_async(request, runtime)

    def list_organizational_units_for_application_with_options(
        self,
        request: eiam_20211201_models.ListOrganizationalUnitsForApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListOrganizationalUnitsForApplicationResponse:
        """
        @summary Queries the organizations that are allowed to access an Employee Identity and Access Management (EIAM) application by page. The return result includes the IDs of the organizations. If you want to obtain the details of the organizations, call the GetOrganizationalUnit operation.
        
        @param request: ListOrganizationalUnitsForApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOrganizationalUnitsForApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.organizational_unit_ids):
            query['OrganizationalUnitIds'] = request.organizational_unit_ids
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOrganizationalUnitsForApplication',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListOrganizationalUnitsForApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_organizational_units_for_application_with_options_async(
        self,
        request: eiam_20211201_models.ListOrganizationalUnitsForApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListOrganizationalUnitsForApplicationResponse:
        """
        @summary Queries the organizations that are allowed to access an Employee Identity and Access Management (EIAM) application by page. The return result includes the IDs of the organizations. If you want to obtain the details of the organizations, call the GetOrganizationalUnit operation.
        
        @param request: ListOrganizationalUnitsForApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOrganizationalUnitsForApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.organizational_unit_ids):
            query['OrganizationalUnitIds'] = request.organizational_unit_ids
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOrganizationalUnitsForApplication',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListOrganizationalUnitsForApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_organizational_units_for_application(
        self,
        request: eiam_20211201_models.ListOrganizationalUnitsForApplicationRequest,
    ) -> eiam_20211201_models.ListOrganizationalUnitsForApplicationResponse:
        """
        @summary Queries the organizations that are allowed to access an Employee Identity and Access Management (EIAM) application by page. The return result includes the IDs of the organizations. If you want to obtain the details of the organizations, call the GetOrganizationalUnit operation.
        
        @param request: ListOrganizationalUnitsForApplicationRequest
        @return: ListOrganizationalUnitsForApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_organizational_units_for_application_with_options(request, runtime)

    async def list_organizational_units_for_application_async(
        self,
        request: eiam_20211201_models.ListOrganizationalUnitsForApplicationRequest,
    ) -> eiam_20211201_models.ListOrganizationalUnitsForApplicationResponse:
        """
        @summary Queries the organizations that are allowed to access an Employee Identity and Access Management (EIAM) application by page. The return result includes the IDs of the organizations. If you want to obtain the details of the organizations, call the GetOrganizationalUnit operation.
        
        @param request: ListOrganizationalUnitsForApplicationRequest
        @return: ListOrganizationalUnitsForApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_organizational_units_for_application_with_options_async(request, runtime)

    def list_regions_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListRegionsResponse:
        """
        @summary Queries the supported Alibaba Cloud regions.
        
        @param request: ListRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRegionsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListRegions',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_regions_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListRegionsResponse:
        """
        @summary Queries the supported Alibaba Cloud regions.
        
        @param request: ListRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRegionsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListRegions',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_regions(self) -> eiam_20211201_models.ListRegionsResponse:
        """
        @summary Queries the supported Alibaba Cloud regions.
        
        @return: ListRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_regions_with_options(runtime)

    async def list_regions_async(self) -> eiam_20211201_models.ListRegionsResponse:
        """
        @summary Queries the supported Alibaba Cloud regions.
        
        @return: ListRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_regions_with_options_async(runtime)

    def list_synchronization_jobs_with_options(
        self,
        request: eiam_20211201_models.ListSynchronizationJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListSynchronizationJobsResponse:
        """
        @summary 查询同步任务
        
        @param request: ListSynchronizationJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSynchronizationJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.target_ids):
            query['TargetIds'] = request.target_ids
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSynchronizationJobs',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListSynchronizationJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_synchronization_jobs_with_options_async(
        self,
        request: eiam_20211201_models.ListSynchronizationJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListSynchronizationJobsResponse:
        """
        @summary 查询同步任务
        
        @param request: ListSynchronizationJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSynchronizationJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.target_ids):
            query['TargetIds'] = request.target_ids
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSynchronizationJobs',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListSynchronizationJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_synchronization_jobs(
        self,
        request: eiam_20211201_models.ListSynchronizationJobsRequest,
    ) -> eiam_20211201_models.ListSynchronizationJobsResponse:
        """
        @summary 查询同步任务
        
        @param request: ListSynchronizationJobsRequest
        @return: ListSynchronizationJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_synchronization_jobs_with_options(request, runtime)

    async def list_synchronization_jobs_async(
        self,
        request: eiam_20211201_models.ListSynchronizationJobsRequest,
    ) -> eiam_20211201_models.ListSynchronizationJobsResponse:
        """
        @summary 查询同步任务
        
        @param request: ListSynchronizationJobsRequest
        @return: ListSynchronizationJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_synchronization_jobs_with_options_async(request, runtime)

    def list_user_authn_source_mappings_with_options(
        self,
        request: eiam_20211201_models.ListUserAuthnSourceMappingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListUserAuthnSourceMappingsResponse:
        """
        @summary 查询三方登录账户绑定关系
        
        @param request: ListUserAuthnSourceMappingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserAuthnSourceMappingsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identity_provider_id):
            query['IdentityProviderId'] = request.identity_provider_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.previous_token):
            query['PreviousToken'] = request.previous_token
        if not UtilClient.is_unset(request.user_external_id):
            query['UserExternalId'] = request.user_external_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserAuthnSourceMappings',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListUserAuthnSourceMappingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_authn_source_mappings_with_options_async(
        self,
        request: eiam_20211201_models.ListUserAuthnSourceMappingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListUserAuthnSourceMappingsResponse:
        """
        @summary 查询三方登录账户绑定关系
        
        @param request: ListUserAuthnSourceMappingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserAuthnSourceMappingsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identity_provider_id):
            query['IdentityProviderId'] = request.identity_provider_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.previous_token):
            query['PreviousToken'] = request.previous_token
        if not UtilClient.is_unset(request.user_external_id):
            query['UserExternalId'] = request.user_external_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserAuthnSourceMappings',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListUserAuthnSourceMappingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_authn_source_mappings(
        self,
        request: eiam_20211201_models.ListUserAuthnSourceMappingsRequest,
    ) -> eiam_20211201_models.ListUserAuthnSourceMappingsResponse:
        """
        @summary 查询三方登录账户绑定关系
        
        @param request: ListUserAuthnSourceMappingsRequest
        @return: ListUserAuthnSourceMappingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_user_authn_source_mappings_with_options(request, runtime)

    async def list_user_authn_source_mappings_async(
        self,
        request: eiam_20211201_models.ListUserAuthnSourceMappingsRequest,
    ) -> eiam_20211201_models.ListUserAuthnSourceMappingsResponse:
        """
        @summary 查询三方登录账户绑定关系
        
        @param request: ListUserAuthnSourceMappingsRequest
        @return: ListUserAuthnSourceMappingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_user_authn_source_mappings_with_options_async(request, runtime)

    def list_users_with_options(
        self,
        request: eiam_20211201_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListUsersResponse:
        """
        @summary Queries the details of accounts in Identity as a Service (IDaaS) Employee IAM (EIAM) by page.
        
        @param request: ListUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.display_name_starts_with):
            query['DisplayNameStartsWith'] = request.display_name_starts_with
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.organizational_unit_id):
            query['OrganizationalUnitId'] = request.organizational_unit_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.phone_region):
            query['PhoneRegion'] = request.phone_region
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.user_external_id):
            query['UserExternalId'] = request.user_external_id
        if not UtilClient.is_unset(request.user_ids):
            query['UserIds'] = request.user_ids
        if not UtilClient.is_unset(request.user_source_id):
            query['UserSourceId'] = request.user_source_id
        if not UtilClient.is_unset(request.user_source_type):
            query['UserSourceType'] = request.user_source_type
        if not UtilClient.is_unset(request.username_starts_with):
            query['UsernameStartsWith'] = request.username_starts_with
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsers',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_users_with_options_async(
        self,
        request: eiam_20211201_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListUsersResponse:
        """
        @summary Queries the details of accounts in Identity as a Service (IDaaS) Employee IAM (EIAM) by page.
        
        @param request: ListUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.display_name_starts_with):
            query['DisplayNameStartsWith'] = request.display_name_starts_with
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.organizational_unit_id):
            query['OrganizationalUnitId'] = request.organizational_unit_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.phone_region):
            query['PhoneRegion'] = request.phone_region
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.user_external_id):
            query['UserExternalId'] = request.user_external_id
        if not UtilClient.is_unset(request.user_ids):
            query['UserIds'] = request.user_ids
        if not UtilClient.is_unset(request.user_source_id):
            query['UserSourceId'] = request.user_source_id
        if not UtilClient.is_unset(request.user_source_type):
            query['UserSourceType'] = request.user_source_type
        if not UtilClient.is_unset(request.username_starts_with):
            query['UsernameStartsWith'] = request.username_starts_with
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsers',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_users(
        self,
        request: eiam_20211201_models.ListUsersRequest,
    ) -> eiam_20211201_models.ListUsersResponse:
        """
        @summary Queries the details of accounts in Identity as a Service (IDaaS) Employee IAM (EIAM) by page.
        
        @param request: ListUsersRequest
        @return: ListUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_users_with_options(request, runtime)

    async def list_users_async(
        self,
        request: eiam_20211201_models.ListUsersRequest,
    ) -> eiam_20211201_models.ListUsersResponse:
        """
        @summary Queries the details of accounts in Identity as a Service (IDaaS) Employee IAM (EIAM) by page.
        
        @param request: ListUsersRequest
        @return: ListUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_users_with_options_async(request, runtime)

    def list_users_for_application_with_options(
        self,
        request: eiam_20211201_models.ListUsersForApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListUsersForApplicationResponse:
        """
        @summary Queries the accounts that are allowed to access an Employee Identity and Access Management (EIAM) application. The return results include the IDs of the accounts. If you need to obtain the details of the accounts, call the GetUser operation.
        
        @param request: ListUsersForApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUsersForApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsersForApplication',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListUsersForApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_users_for_application_with_options_async(
        self,
        request: eiam_20211201_models.ListUsersForApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListUsersForApplicationResponse:
        """
        @summary Queries the accounts that are allowed to access an Employee Identity and Access Management (EIAM) application. The return results include the IDs of the accounts. If you need to obtain the details of the accounts, call the GetUser operation.
        
        @param request: ListUsersForApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUsersForApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsersForApplication',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListUsersForApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_users_for_application(
        self,
        request: eiam_20211201_models.ListUsersForApplicationRequest,
    ) -> eiam_20211201_models.ListUsersForApplicationResponse:
        """
        @summary Queries the accounts that are allowed to access an Employee Identity and Access Management (EIAM) application. The return results include the IDs of the accounts. If you need to obtain the details of the accounts, call the GetUser operation.
        
        @param request: ListUsersForApplicationRequest
        @return: ListUsersForApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_users_for_application_with_options(request, runtime)

    async def list_users_for_application_async(
        self,
        request: eiam_20211201_models.ListUsersForApplicationRequest,
    ) -> eiam_20211201_models.ListUsersForApplicationResponse:
        """
        @summary Queries the accounts that are allowed to access an Employee Identity and Access Management (EIAM) application. The return results include the IDs of the accounts. If you need to obtain the details of the accounts, call the GetUser operation.
        
        @param request: ListUsersForApplicationRequest
        @return: ListUsersForApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_users_for_application_with_options_async(request, runtime)

    def list_users_for_group_with_options(
        self,
        request: eiam_20211201_models.ListUsersForGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListUsersForGroupResponse:
        """
        @summary Queries the information of accounts in an Employee Identity and Access Management (EIAM) group of Identity as a Service (IDaaS).
        
        @param request: ListUsersForGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUsersForGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsersForGroup',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListUsersForGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_users_for_group_with_options_async(
        self,
        request: eiam_20211201_models.ListUsersForGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ListUsersForGroupResponse:
        """
        @summary Queries the information of accounts in an Employee Identity and Access Management (EIAM) group of Identity as a Service (IDaaS).
        
        @param request: ListUsersForGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUsersForGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsersForGroup',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ListUsersForGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_users_for_group(
        self,
        request: eiam_20211201_models.ListUsersForGroupRequest,
    ) -> eiam_20211201_models.ListUsersForGroupResponse:
        """
        @summary Queries the information of accounts in an Employee Identity and Access Management (EIAM) group of Identity as a Service (IDaaS).
        
        @param request: ListUsersForGroupRequest
        @return: ListUsersForGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_users_for_group_with_options(request, runtime)

    async def list_users_for_group_async(
        self,
        request: eiam_20211201_models.ListUsersForGroupRequest,
    ) -> eiam_20211201_models.ListUsersForGroupResponse:
        """
        @summary Queries the information of accounts in an Employee Identity and Access Management (EIAM) group of Identity as a Service (IDaaS).
        
        @param request: ListUsersForGroupRequest
        @return: ListUsersForGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_users_for_group_with_options_async(request, runtime)

    def obtain_application_client_secret_with_options(
        self,
        request: eiam_20211201_models.ObtainApplicationClientSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ObtainApplicationClientSecretResponse:
        """
        @summary Queries a client key of an Employee Identity and Access Management (EIAM) application. The returned key secret is masked. If you want to query the key secret that is not masked, call the ListApplicationClientSecrets operation.
        
        @param request: ObtainApplicationClientSecretRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ObtainApplicationClientSecretResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.secret_id):
            query['SecretId'] = request.secret_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ObtainApplicationClientSecret',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ObtainApplicationClientSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def obtain_application_client_secret_with_options_async(
        self,
        request: eiam_20211201_models.ObtainApplicationClientSecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ObtainApplicationClientSecretResponse:
        """
        @summary Queries a client key of an Employee Identity and Access Management (EIAM) application. The returned key secret is masked. If you want to query the key secret that is not masked, call the ListApplicationClientSecrets operation.
        
        @param request: ObtainApplicationClientSecretRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ObtainApplicationClientSecretResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.secret_id):
            query['SecretId'] = request.secret_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ObtainApplicationClientSecret',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ObtainApplicationClientSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def obtain_application_client_secret(
        self,
        request: eiam_20211201_models.ObtainApplicationClientSecretRequest,
    ) -> eiam_20211201_models.ObtainApplicationClientSecretResponse:
        """
        @summary Queries a client key of an Employee Identity and Access Management (EIAM) application. The returned key secret is masked. If you want to query the key secret that is not masked, call the ListApplicationClientSecrets operation.
        
        @param request: ObtainApplicationClientSecretRequest
        @return: ObtainApplicationClientSecretResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.obtain_application_client_secret_with_options(request, runtime)

    async def obtain_application_client_secret_async(
        self,
        request: eiam_20211201_models.ObtainApplicationClientSecretRequest,
    ) -> eiam_20211201_models.ObtainApplicationClientSecretResponse:
        """
        @summary Queries a client key of an Employee Identity and Access Management (EIAM) application. The returned key secret is masked. If you want to query the key secret that is not masked, call the ListApplicationClientSecrets operation.
        
        @param request: ObtainApplicationClientSecretRequest
        @return: ObtainApplicationClientSecretResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.obtain_application_client_secret_with_options_async(request, runtime)

    def obtain_application_token_with_options(
        self,
        request: eiam_20211201_models.ObtainApplicationTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ObtainApplicationTokenResponse:
        """
        @summary 查询指定应用Token
        
        @param request: ObtainApplicationTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ObtainApplicationTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.application_token_id):
            query['ApplicationTokenId'] = request.application_token_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ObtainApplicationToken',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ObtainApplicationTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def obtain_application_token_with_options_async(
        self,
        request: eiam_20211201_models.ObtainApplicationTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ObtainApplicationTokenResponse:
        """
        @summary 查询指定应用Token
        
        @param request: ObtainApplicationTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ObtainApplicationTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.application_token_id):
            query['ApplicationTokenId'] = request.application_token_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ObtainApplicationToken',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ObtainApplicationTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def obtain_application_token(
        self,
        request: eiam_20211201_models.ObtainApplicationTokenRequest,
    ) -> eiam_20211201_models.ObtainApplicationTokenResponse:
        """
        @summary 查询指定应用Token
        
        @param request: ObtainApplicationTokenRequest
        @return: ObtainApplicationTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.obtain_application_token_with_options(request, runtime)

    async def obtain_application_token_async(
        self,
        request: eiam_20211201_models.ObtainApplicationTokenRequest,
    ) -> eiam_20211201_models.ObtainApplicationTokenResponse:
        """
        @summary 查询指定应用Token
        
        @param request: ObtainApplicationTokenRequest
        @return: ObtainApplicationTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.obtain_application_token_with_options_async(request, runtime)

    def obtain_domain_proxy_token_with_options(
        self,
        request: eiam_20211201_models.ObtainDomainProxyTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ObtainDomainProxyTokenResponse:
        """
        @summary Queries the information about a proxy token of a domain name of an Employee Identity and Access Management (EIAM) instance.
        
        @param request: ObtainDomainProxyTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ObtainDomainProxyTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.domain_proxy_token_id):
            query['DomainProxyTokenId'] = request.domain_proxy_token_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ObtainDomainProxyToken',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ObtainDomainProxyTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def obtain_domain_proxy_token_with_options_async(
        self,
        request: eiam_20211201_models.ObtainDomainProxyTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.ObtainDomainProxyTokenResponse:
        """
        @summary Queries the information about a proxy token of a domain name of an Employee Identity and Access Management (EIAM) instance.
        
        @param request: ObtainDomainProxyTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ObtainDomainProxyTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.domain_proxy_token_id):
            query['DomainProxyTokenId'] = request.domain_proxy_token_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ObtainDomainProxyToken',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.ObtainDomainProxyTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def obtain_domain_proxy_token(
        self,
        request: eiam_20211201_models.ObtainDomainProxyTokenRequest,
    ) -> eiam_20211201_models.ObtainDomainProxyTokenResponse:
        """
        @summary Queries the information about a proxy token of a domain name of an Employee Identity and Access Management (EIAM) instance.
        
        @param request: ObtainDomainProxyTokenRequest
        @return: ObtainDomainProxyTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.obtain_domain_proxy_token_with_options(request, runtime)

    async def obtain_domain_proxy_token_async(
        self,
        request: eiam_20211201_models.ObtainDomainProxyTokenRequest,
    ) -> eiam_20211201_models.ObtainDomainProxyTokenResponse:
        """
        @summary Queries the information about a proxy token of a domain name of an Employee Identity and Access Management (EIAM) instance.
        
        @param request: ObtainDomainProxyTokenRequest
        @return: ObtainDomainProxyTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.obtain_domain_proxy_token_with_options_async(request, runtime)

    def remove_application_account_from_user_with_options(
        self,
        request: eiam_20211201_models.RemoveApplicationAccountFromUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.RemoveApplicationAccountFromUserResponse:
        """
        @summary 删除一个当前应用下的指定员工的应用账号
        
        @param request: RemoveApplicationAccountFromUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveApplicationAccountFromUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_account_id):
            query['ApplicationAccountId'] = request.application_account_id
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveApplicationAccountFromUser',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.RemoveApplicationAccountFromUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_application_account_from_user_with_options_async(
        self,
        request: eiam_20211201_models.RemoveApplicationAccountFromUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.RemoveApplicationAccountFromUserResponse:
        """
        @summary 删除一个当前应用下的指定员工的应用账号
        
        @param request: RemoveApplicationAccountFromUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveApplicationAccountFromUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_account_id):
            query['ApplicationAccountId'] = request.application_account_id
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveApplicationAccountFromUser',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.RemoveApplicationAccountFromUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_application_account_from_user(
        self,
        request: eiam_20211201_models.RemoveApplicationAccountFromUserRequest,
    ) -> eiam_20211201_models.RemoveApplicationAccountFromUserResponse:
        """
        @summary 删除一个当前应用下的指定员工的应用账号
        
        @param request: RemoveApplicationAccountFromUserRequest
        @return: RemoveApplicationAccountFromUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_application_account_from_user_with_options(request, runtime)

    async def remove_application_account_from_user_async(
        self,
        request: eiam_20211201_models.RemoveApplicationAccountFromUserRequest,
    ) -> eiam_20211201_models.RemoveApplicationAccountFromUserResponse:
        """
        @summary 删除一个当前应用下的指定员工的应用账号
        
        @param request: RemoveApplicationAccountFromUserRequest
        @return: RemoveApplicationAccountFromUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_application_account_from_user_with_options_async(request, runtime)

    def remove_custom_privacy_policies_from_brand_with_options(
        self,
        request: eiam_20211201_models.RemoveCustomPrivacyPoliciesFromBrandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.RemoveCustomPrivacyPoliciesFromBrandResponse:
        """
        @summary 移除品牌关联条款
        
        @param request: RemoveCustomPrivacyPoliciesFromBrandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveCustomPrivacyPoliciesFromBrandResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.brand_id):
            query['BrandId'] = request.brand_id
        if not UtilClient.is_unset(request.custom_privacy_policy_ids):
            query['CustomPrivacyPolicyIds'] = request.custom_privacy_policy_ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveCustomPrivacyPoliciesFromBrand',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.RemoveCustomPrivacyPoliciesFromBrandResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_custom_privacy_policies_from_brand_with_options_async(
        self,
        request: eiam_20211201_models.RemoveCustomPrivacyPoliciesFromBrandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.RemoveCustomPrivacyPoliciesFromBrandResponse:
        """
        @summary 移除品牌关联条款
        
        @param request: RemoveCustomPrivacyPoliciesFromBrandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveCustomPrivacyPoliciesFromBrandResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.brand_id):
            query['BrandId'] = request.brand_id
        if not UtilClient.is_unset(request.custom_privacy_policy_ids):
            query['CustomPrivacyPolicyIds'] = request.custom_privacy_policy_ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveCustomPrivacyPoliciesFromBrand',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.RemoveCustomPrivacyPoliciesFromBrandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_custom_privacy_policies_from_brand(
        self,
        request: eiam_20211201_models.RemoveCustomPrivacyPoliciesFromBrandRequest,
    ) -> eiam_20211201_models.RemoveCustomPrivacyPoliciesFromBrandResponse:
        """
        @summary 移除品牌关联条款
        
        @param request: RemoveCustomPrivacyPoliciesFromBrandRequest
        @return: RemoveCustomPrivacyPoliciesFromBrandResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_custom_privacy_policies_from_brand_with_options(request, runtime)

    async def remove_custom_privacy_policies_from_brand_async(
        self,
        request: eiam_20211201_models.RemoveCustomPrivacyPoliciesFromBrandRequest,
    ) -> eiam_20211201_models.RemoveCustomPrivacyPoliciesFromBrandResponse:
        """
        @summary 移除品牌关联条款
        
        @param request: RemoveCustomPrivacyPoliciesFromBrandRequest
        @return: RemoveCustomPrivacyPoliciesFromBrandResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_custom_privacy_policies_from_brand_with_options_async(request, runtime)

    def remove_user_from_organizational_units_with_options(
        self,
        request: eiam_20211201_models.RemoveUserFromOrganizationalUnitsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.RemoveUserFromOrganizationalUnitsResponse:
        """
        @summary Removes an Employee Identity and Access Management (EIAM) account from multiple EIAM organizations of Identity as a Service (IDaaS). You cannot remove an account from a primary organization.
        
        @param request: RemoveUserFromOrganizationalUnitsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveUserFromOrganizationalUnitsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.organizational_unit_ids):
            query['OrganizationalUnitIds'] = request.organizational_unit_ids
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveUserFromOrganizationalUnits',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.RemoveUserFromOrganizationalUnitsResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_user_from_organizational_units_with_options_async(
        self,
        request: eiam_20211201_models.RemoveUserFromOrganizationalUnitsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.RemoveUserFromOrganizationalUnitsResponse:
        """
        @summary Removes an Employee Identity and Access Management (EIAM) account from multiple EIAM organizations of Identity as a Service (IDaaS). You cannot remove an account from a primary organization.
        
        @param request: RemoveUserFromOrganizationalUnitsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveUserFromOrganizationalUnitsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.organizational_unit_ids):
            query['OrganizationalUnitIds'] = request.organizational_unit_ids
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveUserFromOrganizationalUnits',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.RemoveUserFromOrganizationalUnitsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_user_from_organizational_units(
        self,
        request: eiam_20211201_models.RemoveUserFromOrganizationalUnitsRequest,
    ) -> eiam_20211201_models.RemoveUserFromOrganizationalUnitsResponse:
        """
        @summary Removes an Employee Identity and Access Management (EIAM) account from multiple EIAM organizations of Identity as a Service (IDaaS). You cannot remove an account from a primary organization.
        
        @param request: RemoveUserFromOrganizationalUnitsRequest
        @return: RemoveUserFromOrganizationalUnitsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_user_from_organizational_units_with_options(request, runtime)

    async def remove_user_from_organizational_units_async(
        self,
        request: eiam_20211201_models.RemoveUserFromOrganizationalUnitsRequest,
    ) -> eiam_20211201_models.RemoveUserFromOrganizationalUnitsResponse:
        """
        @summary Removes an Employee Identity and Access Management (EIAM) account from multiple EIAM organizations of Identity as a Service (IDaaS). You cannot remove an account from a primary organization.
        
        @param request: RemoveUserFromOrganizationalUnitsRequest
        @return: RemoveUserFromOrganizationalUnitsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_user_from_organizational_units_with_options_async(request, runtime)

    def remove_users_from_group_with_options(
        self,
        request: eiam_20211201_models.RemoveUsersFromGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.RemoveUsersFromGroupResponse:
        """
        @summary Removes Employee Identity and Access Management (EIAM) accounts from an EIAM group of Identity as a Service (IDaaS).
        
        @param request: RemoveUsersFromGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveUsersFromGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveUsersFromGroup',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.RemoveUsersFromGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_users_from_group_with_options_async(
        self,
        request: eiam_20211201_models.RemoveUsersFromGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.RemoveUsersFromGroupResponse:
        """
        @summary Removes Employee Identity and Access Management (EIAM) accounts from an EIAM group of Identity as a Service (IDaaS).
        
        @param request: RemoveUsersFromGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveUsersFromGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveUsersFromGroup',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.RemoveUsersFromGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_users_from_group(
        self,
        request: eiam_20211201_models.RemoveUsersFromGroupRequest,
    ) -> eiam_20211201_models.RemoveUsersFromGroupResponse:
        """
        @summary Removes Employee Identity and Access Management (EIAM) accounts from an EIAM group of Identity as a Service (IDaaS).
        
        @param request: RemoveUsersFromGroupRequest
        @return: RemoveUsersFromGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_users_from_group_with_options(request, runtime)

    async def remove_users_from_group_async(
        self,
        request: eiam_20211201_models.RemoveUsersFromGroupRequest,
    ) -> eiam_20211201_models.RemoveUsersFromGroupResponse:
        """
        @summary Removes Employee Identity and Access Management (EIAM) accounts from an EIAM group of Identity as a Service (IDaaS).
        
        @param request: RemoveUsersFromGroupRequest
        @return: RemoveUsersFromGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_users_from_group_with_options_async(request, runtime)

    def revoke_application_from_groups_with_options(
        self,
        request: eiam_20211201_models.RevokeApplicationFromGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.RevokeApplicationFromGroupsResponse:
        """
        @summary Revokes the permissions to access an application from multiple account groups at a time in Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM).
        
        @param request: RevokeApplicationFromGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RevokeApplicationFromGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevokeApplicationFromGroups',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.RevokeApplicationFromGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_application_from_groups_with_options_async(
        self,
        request: eiam_20211201_models.RevokeApplicationFromGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.RevokeApplicationFromGroupsResponse:
        """
        @summary Revokes the permissions to access an application from multiple account groups at a time in Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM).
        
        @param request: RevokeApplicationFromGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RevokeApplicationFromGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevokeApplicationFromGroups',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.RevokeApplicationFromGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_application_from_groups(
        self,
        request: eiam_20211201_models.RevokeApplicationFromGroupsRequest,
    ) -> eiam_20211201_models.RevokeApplicationFromGroupsResponse:
        """
        @summary Revokes the permissions to access an application from multiple account groups at a time in Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM).
        
        @param request: RevokeApplicationFromGroupsRequest
        @return: RevokeApplicationFromGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.revoke_application_from_groups_with_options(request, runtime)

    async def revoke_application_from_groups_async(
        self,
        request: eiam_20211201_models.RevokeApplicationFromGroupsRequest,
    ) -> eiam_20211201_models.RevokeApplicationFromGroupsResponse:
        """
        @summary Revokes the permissions to access an application from multiple account groups at a time in Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM).
        
        @param request: RevokeApplicationFromGroupsRequest
        @return: RevokeApplicationFromGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.revoke_application_from_groups_with_options_async(request, runtime)

    def revoke_application_from_organizational_units_with_options(
        self,
        request: eiam_20211201_models.RevokeApplicationFromOrganizationalUnitsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.RevokeApplicationFromOrganizationalUnitsResponse:
        """
        @summary Revokes the permissions to access an application from multiple Employee Identity and Access Management (EIAM) organizations at a time.
        
        @param request: RevokeApplicationFromOrganizationalUnitsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RevokeApplicationFromOrganizationalUnitsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.organizational_unit_ids):
            query['OrganizationalUnitIds'] = request.organizational_unit_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevokeApplicationFromOrganizationalUnits',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.RevokeApplicationFromOrganizationalUnitsResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_application_from_organizational_units_with_options_async(
        self,
        request: eiam_20211201_models.RevokeApplicationFromOrganizationalUnitsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.RevokeApplicationFromOrganizationalUnitsResponse:
        """
        @summary Revokes the permissions to access an application from multiple Employee Identity and Access Management (EIAM) organizations at a time.
        
        @param request: RevokeApplicationFromOrganizationalUnitsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RevokeApplicationFromOrganizationalUnitsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.organizational_unit_ids):
            query['OrganizationalUnitIds'] = request.organizational_unit_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevokeApplicationFromOrganizationalUnits',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.RevokeApplicationFromOrganizationalUnitsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_application_from_organizational_units(
        self,
        request: eiam_20211201_models.RevokeApplicationFromOrganizationalUnitsRequest,
    ) -> eiam_20211201_models.RevokeApplicationFromOrganizationalUnitsResponse:
        """
        @summary Revokes the permissions to access an application from multiple Employee Identity and Access Management (EIAM) organizations at a time.
        
        @param request: RevokeApplicationFromOrganizationalUnitsRequest
        @return: RevokeApplicationFromOrganizationalUnitsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.revoke_application_from_organizational_units_with_options(request, runtime)

    async def revoke_application_from_organizational_units_async(
        self,
        request: eiam_20211201_models.RevokeApplicationFromOrganizationalUnitsRequest,
    ) -> eiam_20211201_models.RevokeApplicationFromOrganizationalUnitsResponse:
        """
        @summary Revokes the permissions to access an application from multiple Employee Identity and Access Management (EIAM) organizations at a time.
        
        @param request: RevokeApplicationFromOrganizationalUnitsRequest
        @return: RevokeApplicationFromOrganizationalUnitsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.revoke_application_from_organizational_units_with_options_async(request, runtime)

    def revoke_application_from_users_with_options(
        self,
        request: eiam_20211201_models.RevokeApplicationFromUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.RevokeApplicationFromUsersResponse:
        """
        @summary Revokes the permissions to access an application from multiple Employee Identity and Access Management (EIAM) accounts at a time.
        
        @param request: RevokeApplicationFromUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RevokeApplicationFromUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevokeApplicationFromUsers',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.RevokeApplicationFromUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_application_from_users_with_options_async(
        self,
        request: eiam_20211201_models.RevokeApplicationFromUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.RevokeApplicationFromUsersResponse:
        """
        @summary Revokes the permissions to access an application from multiple Employee Identity and Access Management (EIAM) accounts at a time.
        
        @param request: RevokeApplicationFromUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RevokeApplicationFromUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevokeApplicationFromUsers',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.RevokeApplicationFromUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_application_from_users(
        self,
        request: eiam_20211201_models.RevokeApplicationFromUsersRequest,
    ) -> eiam_20211201_models.RevokeApplicationFromUsersResponse:
        """
        @summary Revokes the permissions to access an application from multiple Employee Identity and Access Management (EIAM) accounts at a time.
        
        @param request: RevokeApplicationFromUsersRequest
        @return: RevokeApplicationFromUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.revoke_application_from_users_with_options(request, runtime)

    async def revoke_application_from_users_async(
        self,
        request: eiam_20211201_models.RevokeApplicationFromUsersRequest,
    ) -> eiam_20211201_models.RevokeApplicationFromUsersResponse:
        """
        @summary Revokes the permissions to access an application from multiple Employee Identity and Access Management (EIAM) accounts at a time.
        
        @param request: RevokeApplicationFromUsersRequest
        @return: RevokeApplicationFromUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.revoke_application_from_users_with_options_async(request, runtime)

    def run_synchronization_job_with_options(
        self,
        request: eiam_20211201_models.RunSynchronizationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.RunSynchronizationJobResponse:
        """
        @summary Creates a synchronization job and immediately runs the job.
        
        @param request: RunSynchronizationJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunSynchronizationJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.password_initialization):
            query['PasswordInitialization'] = request.password_initialization
        if not UtilClient.is_unset(request.synchronization_scope_config):
            query['SynchronizationScopeConfig'] = request.synchronization_scope_config
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        if not UtilClient.is_unset(request.user_identity_types):
            query['UserIdentityTypes'] = request.user_identity_types
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunSynchronizationJob',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.RunSynchronizationJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_synchronization_job_with_options_async(
        self,
        request: eiam_20211201_models.RunSynchronizationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.RunSynchronizationJobResponse:
        """
        @summary Creates a synchronization job and immediately runs the job.
        
        @param request: RunSynchronizationJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunSynchronizationJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.password_initialization):
            query['PasswordInitialization'] = request.password_initialization
        if not UtilClient.is_unset(request.synchronization_scope_config):
            query['SynchronizationScopeConfig'] = request.synchronization_scope_config
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        if not UtilClient.is_unset(request.user_identity_types):
            query['UserIdentityTypes'] = request.user_identity_types
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunSynchronizationJob',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.RunSynchronizationJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_synchronization_job(
        self,
        request: eiam_20211201_models.RunSynchronizationJobRequest,
    ) -> eiam_20211201_models.RunSynchronizationJobResponse:
        """
        @summary Creates a synchronization job and immediately runs the job.
        
        @param request: RunSynchronizationJobRequest
        @return: RunSynchronizationJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_synchronization_job_with_options(request, runtime)

    async def run_synchronization_job_async(
        self,
        request: eiam_20211201_models.RunSynchronizationJobRequest,
    ) -> eiam_20211201_models.RunSynchronizationJobResponse:
        """
        @summary Creates a synchronization job and immediately runs the job.
        
        @param request: RunSynchronizationJobRequest
        @return: RunSynchronizationJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_synchronization_job_with_options_async(request, runtime)

    def set_application_grant_scope_with_options(
        self,
        request: eiam_20211201_models.SetApplicationGrantScopeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.SetApplicationGrantScopeResponse:
        """
        @summary Configures the permissions of the Developer API feature of an Employee Identity and Access Management (EIAM) application.
        
        @param request: SetApplicationGrantScopeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetApplicationGrantScopeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.grant_scopes):
            query['GrantScopes'] = request.grant_scopes
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetApplicationGrantScope',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.SetApplicationGrantScopeResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_application_grant_scope_with_options_async(
        self,
        request: eiam_20211201_models.SetApplicationGrantScopeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.SetApplicationGrantScopeResponse:
        """
        @summary Configures the permissions of the Developer API feature of an Employee Identity and Access Management (EIAM) application.
        
        @param request: SetApplicationGrantScopeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetApplicationGrantScopeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.grant_scopes):
            query['GrantScopes'] = request.grant_scopes
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetApplicationGrantScope',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.SetApplicationGrantScopeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_application_grant_scope(
        self,
        request: eiam_20211201_models.SetApplicationGrantScopeRequest,
    ) -> eiam_20211201_models.SetApplicationGrantScopeResponse:
        """
        @summary Configures the permissions of the Developer API feature of an Employee Identity and Access Management (EIAM) application.
        
        @param request: SetApplicationGrantScopeRequest
        @return: SetApplicationGrantScopeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_application_grant_scope_with_options(request, runtime)

    async def set_application_grant_scope_async(
        self,
        request: eiam_20211201_models.SetApplicationGrantScopeRequest,
    ) -> eiam_20211201_models.SetApplicationGrantScopeResponse:
        """
        @summary Configures the permissions of the Developer API feature of an Employee Identity and Access Management (EIAM) application.
        
        @param request: SetApplicationGrantScopeRequest
        @return: SetApplicationGrantScopeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_application_grant_scope_with_options_async(request, runtime)

    def set_application_provisioning_config_with_options(
        self,
        request: eiam_20211201_models.SetApplicationProvisioningConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.SetApplicationProvisioningConfigResponse:
        """
        @summary Configures the account synchronization feature for an application in Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM).
        
        @param request: SetApplicationProvisioningConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetApplicationProvisioningConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.callback_provisioning_config):
            query['CallbackProvisioningConfig'] = request.callback_provisioning_config
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_access_endpoint_id):
            query['NetworkAccessEndpointId'] = request.network_access_endpoint_id
        if not UtilClient.is_unset(request.provision_password):
            query['ProvisionPassword'] = request.provision_password
        if not UtilClient.is_unset(request.provision_protocol_type):
            query['ProvisionProtocolType'] = request.provision_protocol_type
        if not UtilClient.is_unset(request.scim_provisioning_config):
            query['ScimProvisioningConfig'] = request.scim_provisioning_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetApplicationProvisioningConfig',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.SetApplicationProvisioningConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_application_provisioning_config_with_options_async(
        self,
        request: eiam_20211201_models.SetApplicationProvisioningConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.SetApplicationProvisioningConfigResponse:
        """
        @summary Configures the account synchronization feature for an application in Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM).
        
        @param request: SetApplicationProvisioningConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetApplicationProvisioningConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.callback_provisioning_config):
            query['CallbackProvisioningConfig'] = request.callback_provisioning_config
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_access_endpoint_id):
            query['NetworkAccessEndpointId'] = request.network_access_endpoint_id
        if not UtilClient.is_unset(request.provision_password):
            query['ProvisionPassword'] = request.provision_password
        if not UtilClient.is_unset(request.provision_protocol_type):
            query['ProvisionProtocolType'] = request.provision_protocol_type
        if not UtilClient.is_unset(request.scim_provisioning_config):
            query['ScimProvisioningConfig'] = request.scim_provisioning_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetApplicationProvisioningConfig',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.SetApplicationProvisioningConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_application_provisioning_config(
        self,
        request: eiam_20211201_models.SetApplicationProvisioningConfigRequest,
    ) -> eiam_20211201_models.SetApplicationProvisioningConfigResponse:
        """
        @summary Configures the account synchronization feature for an application in Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM).
        
        @param request: SetApplicationProvisioningConfigRequest
        @return: SetApplicationProvisioningConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_application_provisioning_config_with_options(request, runtime)

    async def set_application_provisioning_config_async(
        self,
        request: eiam_20211201_models.SetApplicationProvisioningConfigRequest,
    ) -> eiam_20211201_models.SetApplicationProvisioningConfigResponse:
        """
        @summary Configures the account synchronization feature for an application in Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM).
        
        @param request: SetApplicationProvisioningConfigRequest
        @return: SetApplicationProvisioningConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_application_provisioning_config_with_options_async(request, runtime)

    def set_application_provisioning_scope_with_options(
        self,
        request: eiam_20211201_models.SetApplicationProvisioningScopeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.SetApplicationProvisioningScopeResponse:
        """
        @summary Sets the account synchronization scope of applications in Identity as a Service (IDaaS) Employee IAM (EIAM). This scope is the same as the scope within which developers can call the DeveloperAPI to query and manage accounts.
        
        @param request: SetApplicationProvisioningScopeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetApplicationProvisioningScopeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.organizational_unit_ids):
            query['OrganizationalUnitIds'] = request.organizational_unit_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetApplicationProvisioningScope',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.SetApplicationProvisioningScopeResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_application_provisioning_scope_with_options_async(
        self,
        request: eiam_20211201_models.SetApplicationProvisioningScopeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.SetApplicationProvisioningScopeResponse:
        """
        @summary Sets the account synchronization scope of applications in Identity as a Service (IDaaS) Employee IAM (EIAM). This scope is the same as the scope within which developers can call the DeveloperAPI to query and manage accounts.
        
        @param request: SetApplicationProvisioningScopeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetApplicationProvisioningScopeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.organizational_unit_ids):
            query['OrganizationalUnitIds'] = request.organizational_unit_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetApplicationProvisioningScope',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.SetApplicationProvisioningScopeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_application_provisioning_scope(
        self,
        request: eiam_20211201_models.SetApplicationProvisioningScopeRequest,
    ) -> eiam_20211201_models.SetApplicationProvisioningScopeResponse:
        """
        @summary Sets the account synchronization scope of applications in Identity as a Service (IDaaS) Employee IAM (EIAM). This scope is the same as the scope within which developers can call the DeveloperAPI to query and manage accounts.
        
        @param request: SetApplicationProvisioningScopeRequest
        @return: SetApplicationProvisioningScopeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_application_provisioning_scope_with_options(request, runtime)

    async def set_application_provisioning_scope_async(
        self,
        request: eiam_20211201_models.SetApplicationProvisioningScopeRequest,
    ) -> eiam_20211201_models.SetApplicationProvisioningScopeResponse:
        """
        @summary Sets the account synchronization scope of applications in Identity as a Service (IDaaS) Employee IAM (EIAM). This scope is the same as the scope within which developers can call the DeveloperAPI to query and manage accounts.
        
        @param request: SetApplicationProvisioningScopeRequest
        @return: SetApplicationProvisioningScopeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_application_provisioning_scope_with_options_async(request, runtime)

    def set_application_sso_config_with_options(
        self,
        request: eiam_20211201_models.SetApplicationSsoConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.SetApplicationSsoConfigResponse:
        """
        @summary Specifies the single sign-on (SSO) configuration attributes of an application in Identity as a Service (IDaaS) Employee IAM (EIAM).
        
        @description In IDaaS EIAM, the application management feature supports multiple SSO protocols for applications, including SAML 2.0 and OIDC protocols. Each application supports only one protocol, and the protocol cannot be changed after the application is created. You can specify the SSO configuration attributes of an application based on the supported SSO protocol.
        
        @param request: SetApplicationSsoConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetApplicationSsoConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.init_login_type):
            query['InitLoginType'] = request.init_login_type
        if not UtilClient.is_unset(request.init_login_url):
            query['InitLoginUrl'] = request.init_login_url
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.oidc_sso_config):
            query['OidcSsoConfig'] = request.oidc_sso_config
        if not UtilClient.is_unset(request.saml_sso_config):
            query['SamlSsoConfig'] = request.saml_sso_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetApplicationSsoConfig',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.SetApplicationSsoConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_application_sso_config_with_options_async(
        self,
        request: eiam_20211201_models.SetApplicationSsoConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.SetApplicationSsoConfigResponse:
        """
        @summary Specifies the single sign-on (SSO) configuration attributes of an application in Identity as a Service (IDaaS) Employee IAM (EIAM).
        
        @description In IDaaS EIAM, the application management feature supports multiple SSO protocols for applications, including SAML 2.0 and OIDC protocols. Each application supports only one protocol, and the protocol cannot be changed after the application is created. You can specify the SSO configuration attributes of an application based on the supported SSO protocol.
        
        @param request: SetApplicationSsoConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetApplicationSsoConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.init_login_type):
            query['InitLoginType'] = request.init_login_type
        if not UtilClient.is_unset(request.init_login_url):
            query['InitLoginUrl'] = request.init_login_url
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.oidc_sso_config):
            query['OidcSsoConfig'] = request.oidc_sso_config
        if not UtilClient.is_unset(request.saml_sso_config):
            query['SamlSsoConfig'] = request.saml_sso_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetApplicationSsoConfig',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.SetApplicationSsoConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_application_sso_config(
        self,
        request: eiam_20211201_models.SetApplicationSsoConfigRequest,
    ) -> eiam_20211201_models.SetApplicationSsoConfigResponse:
        """
        @summary Specifies the single sign-on (SSO) configuration attributes of an application in Identity as a Service (IDaaS) Employee IAM (EIAM).
        
        @description In IDaaS EIAM, the application management feature supports multiple SSO protocols for applications, including SAML 2.0 and OIDC protocols. Each application supports only one protocol, and the protocol cannot be changed after the application is created. You can specify the SSO configuration attributes of an application based on the supported SSO protocol.
        
        @param request: SetApplicationSsoConfigRequest
        @return: SetApplicationSsoConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_application_sso_config_with_options(request, runtime)

    async def set_application_sso_config_async(
        self,
        request: eiam_20211201_models.SetApplicationSsoConfigRequest,
    ) -> eiam_20211201_models.SetApplicationSsoConfigResponse:
        """
        @summary Specifies the single sign-on (SSO) configuration attributes of an application in Identity as a Service (IDaaS) Employee IAM (EIAM).
        
        @description In IDaaS EIAM, the application management feature supports multiple SSO protocols for applications, including SAML 2.0 and OIDC protocols. Each application supports only one protocol, and the protocol cannot be changed after the application is created. You can specify the SSO configuration attributes of an application based on the supported SSO protocol.
        
        @param request: SetApplicationSsoConfigRequest
        @return: SetApplicationSsoConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_application_sso_config_with_options_async(request, runtime)

    def set_default_domain_with_options(
        self,
        request: eiam_20211201_models.SetDefaultDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.SetDefaultDomainResponse:
        """
        @summary Sets a domain name of an Employee Identity and Access Management (EIAM) instance as the default domain name.
        
        @param request: SetDefaultDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetDefaultDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDefaultDomain',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.SetDefaultDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_default_domain_with_options_async(
        self,
        request: eiam_20211201_models.SetDefaultDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.SetDefaultDomainResponse:
        """
        @summary Sets a domain name of an Employee Identity and Access Management (EIAM) instance as the default domain name.
        
        @param request: SetDefaultDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetDefaultDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDefaultDomain',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.SetDefaultDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_default_domain(
        self,
        request: eiam_20211201_models.SetDefaultDomainRequest,
    ) -> eiam_20211201_models.SetDefaultDomainResponse:
        """
        @summary Sets a domain name of an Employee Identity and Access Management (EIAM) instance as the default domain name.
        
        @param request: SetDefaultDomainRequest
        @return: SetDefaultDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_default_domain_with_options(request, runtime)

    async def set_default_domain_async(
        self,
        request: eiam_20211201_models.SetDefaultDomainRequest,
    ) -> eiam_20211201_models.SetDefaultDomainResponse:
        """
        @summary Sets a domain name of an Employee Identity and Access Management (EIAM) instance as the default domain name.
        
        @param request: SetDefaultDomainRequest
        @return: SetDefaultDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_default_domain_with_options_async(request, runtime)

    def set_forget_password_configuration_with_options(
        self,
        request: eiam_20211201_models.SetForgetPasswordConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.SetForgetPasswordConfigurationResponse:
        """
        @summary Configures a forgot password policy for an Employee Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS).
        
        @param request: SetForgetPasswordConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetForgetPasswordConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authentication_channels):
            query['AuthenticationChannels'] = request.authentication_channels
        if not UtilClient.is_unset(request.forget_password_status):
            query['ForgetPasswordStatus'] = request.forget_password_status
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetForgetPasswordConfiguration',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.SetForgetPasswordConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_forget_password_configuration_with_options_async(
        self,
        request: eiam_20211201_models.SetForgetPasswordConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.SetForgetPasswordConfigurationResponse:
        """
        @summary Configures a forgot password policy for an Employee Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS).
        
        @param request: SetForgetPasswordConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetForgetPasswordConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authentication_channels):
            query['AuthenticationChannels'] = request.authentication_channels
        if not UtilClient.is_unset(request.forget_password_status):
            query['ForgetPasswordStatus'] = request.forget_password_status
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetForgetPasswordConfiguration',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.SetForgetPasswordConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_forget_password_configuration(
        self,
        request: eiam_20211201_models.SetForgetPasswordConfigurationRequest,
    ) -> eiam_20211201_models.SetForgetPasswordConfigurationResponse:
        """
        @summary Configures a forgot password policy for an Employee Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS).
        
        @param request: SetForgetPasswordConfigurationRequest
        @return: SetForgetPasswordConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_forget_password_configuration_with_options(request, runtime)

    async def set_forget_password_configuration_async(
        self,
        request: eiam_20211201_models.SetForgetPasswordConfigurationRequest,
    ) -> eiam_20211201_models.SetForgetPasswordConfigurationResponse:
        """
        @summary Configures a forgot password policy for an Employee Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS).
        
        @param request: SetForgetPasswordConfigurationRequest
        @return: SetForgetPasswordConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_forget_password_configuration_with_options_async(request, runtime)

    def set_identity_provider_ud_pull_configuration_with_options(
        self,
        request: eiam_20211201_models.SetIdentityProviderUdPullConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.SetIdentityProviderUdPullConfigurationResponse:
        """
        @summary Update IdP synchronization configuration.
        
        @param request: SetIdentityProviderUdPullConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetIdentityProviderUdPullConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_sync_status):
            query['GroupSyncStatus'] = request.group_sync_status
        if not UtilClient.is_unset(request.identity_provider_id):
            query['IdentityProviderId'] = request.identity_provider_id
        if not UtilClient.is_unset(request.incremental_callback_status):
            query['IncrementalCallbackStatus'] = request.incremental_callback_status
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ldap_ud_pull_config):
            query['LdapUdPullConfig'] = request.ldap_ud_pull_config
        if not UtilClient.is_unset(request.periodic_sync_config):
            query['PeriodicSyncConfig'] = request.periodic_sync_config
        if not UtilClient.is_unset(request.periodic_sync_status):
            query['PeriodicSyncStatus'] = request.periodic_sync_status
        if not UtilClient.is_unset(request.pull_protected_rule):
            query['PullProtectedRule'] = request.pull_protected_rule
        if not UtilClient.is_unset(request.ud_sync_scope_config):
            query['UdSyncScopeConfig'] = request.ud_sync_scope_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetIdentityProviderUdPullConfiguration',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.SetIdentityProviderUdPullConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_identity_provider_ud_pull_configuration_with_options_async(
        self,
        request: eiam_20211201_models.SetIdentityProviderUdPullConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.SetIdentityProviderUdPullConfigurationResponse:
        """
        @summary Update IdP synchronization configuration.
        
        @param request: SetIdentityProviderUdPullConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetIdentityProviderUdPullConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_sync_status):
            query['GroupSyncStatus'] = request.group_sync_status
        if not UtilClient.is_unset(request.identity_provider_id):
            query['IdentityProviderId'] = request.identity_provider_id
        if not UtilClient.is_unset(request.incremental_callback_status):
            query['IncrementalCallbackStatus'] = request.incremental_callback_status
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ldap_ud_pull_config):
            query['LdapUdPullConfig'] = request.ldap_ud_pull_config
        if not UtilClient.is_unset(request.periodic_sync_config):
            query['PeriodicSyncConfig'] = request.periodic_sync_config
        if not UtilClient.is_unset(request.periodic_sync_status):
            query['PeriodicSyncStatus'] = request.periodic_sync_status
        if not UtilClient.is_unset(request.pull_protected_rule):
            query['PullProtectedRule'] = request.pull_protected_rule
        if not UtilClient.is_unset(request.ud_sync_scope_config):
            query['UdSyncScopeConfig'] = request.ud_sync_scope_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetIdentityProviderUdPullConfiguration',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.SetIdentityProviderUdPullConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_identity_provider_ud_pull_configuration(
        self,
        request: eiam_20211201_models.SetIdentityProviderUdPullConfigurationRequest,
    ) -> eiam_20211201_models.SetIdentityProviderUdPullConfigurationResponse:
        """
        @summary Update IdP synchronization configuration.
        
        @param request: SetIdentityProviderUdPullConfigurationRequest
        @return: SetIdentityProviderUdPullConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_identity_provider_ud_pull_configuration_with_options(request, runtime)

    async def set_identity_provider_ud_pull_configuration_async(
        self,
        request: eiam_20211201_models.SetIdentityProviderUdPullConfigurationRequest,
    ) -> eiam_20211201_models.SetIdentityProviderUdPullConfigurationResponse:
        """
        @summary Update IdP synchronization configuration.
        
        @param request: SetIdentityProviderUdPullConfigurationRequest
        @return: SetIdentityProviderUdPullConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_identity_provider_ud_pull_configuration_with_options_async(request, runtime)

    def set_login_redirect_application_for_brand_with_options(
        self,
        request: eiam_20211201_models.SetLoginRedirectApplicationForBrandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.SetLoginRedirectApplicationForBrandResponse:
        """
        @summary 为品牌设置登录后跳转应用
        
        @param request: SetLoginRedirectApplicationForBrandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetLoginRedirectApplicationForBrandResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.brand_id):
            query['BrandId'] = request.brand_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetLoginRedirectApplicationForBrand',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.SetLoginRedirectApplicationForBrandResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_login_redirect_application_for_brand_with_options_async(
        self,
        request: eiam_20211201_models.SetLoginRedirectApplicationForBrandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.SetLoginRedirectApplicationForBrandResponse:
        """
        @summary 为品牌设置登录后跳转应用
        
        @param request: SetLoginRedirectApplicationForBrandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetLoginRedirectApplicationForBrandResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.brand_id):
            query['BrandId'] = request.brand_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetLoginRedirectApplicationForBrand',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.SetLoginRedirectApplicationForBrandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_login_redirect_application_for_brand(
        self,
        request: eiam_20211201_models.SetLoginRedirectApplicationForBrandRequest,
    ) -> eiam_20211201_models.SetLoginRedirectApplicationForBrandResponse:
        """
        @summary 为品牌设置登录后跳转应用
        
        @param request: SetLoginRedirectApplicationForBrandRequest
        @return: SetLoginRedirectApplicationForBrandResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_login_redirect_application_for_brand_with_options(request, runtime)

    async def set_login_redirect_application_for_brand_async(
        self,
        request: eiam_20211201_models.SetLoginRedirectApplicationForBrandRequest,
    ) -> eiam_20211201_models.SetLoginRedirectApplicationForBrandResponse:
        """
        @summary 为品牌设置登录后跳转应用
        
        @param request: SetLoginRedirectApplicationForBrandRequest
        @return: SetLoginRedirectApplicationForBrandResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_login_redirect_application_for_brand_with_options_async(request, runtime)

    def set_password_complexity_configuration_with_options(
        self,
        request: eiam_20211201_models.SetPasswordComplexityConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.SetPasswordComplexityConfigurationResponse:
        """
        @summary Configures a password complexity policy for an Employee Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS).
        
        @param request: SetPasswordComplexityConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetPasswordComplexityConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.password_complexity_rules):
            query['PasswordComplexityRules'] = request.password_complexity_rules
        if not UtilClient.is_unset(request.password_min_length):
            query['PasswordMinLength'] = request.password_min_length
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetPasswordComplexityConfiguration',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.SetPasswordComplexityConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_password_complexity_configuration_with_options_async(
        self,
        request: eiam_20211201_models.SetPasswordComplexityConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.SetPasswordComplexityConfigurationResponse:
        """
        @summary Configures a password complexity policy for an Employee Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS).
        
        @param request: SetPasswordComplexityConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetPasswordComplexityConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.password_complexity_rules):
            query['PasswordComplexityRules'] = request.password_complexity_rules
        if not UtilClient.is_unset(request.password_min_length):
            query['PasswordMinLength'] = request.password_min_length
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetPasswordComplexityConfiguration',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.SetPasswordComplexityConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_password_complexity_configuration(
        self,
        request: eiam_20211201_models.SetPasswordComplexityConfigurationRequest,
    ) -> eiam_20211201_models.SetPasswordComplexityConfigurationResponse:
        """
        @summary Configures a password complexity policy for an Employee Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS).
        
        @param request: SetPasswordComplexityConfigurationRequest
        @return: SetPasswordComplexityConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_password_complexity_configuration_with_options(request, runtime)

    async def set_password_complexity_configuration_async(
        self,
        request: eiam_20211201_models.SetPasswordComplexityConfigurationRequest,
    ) -> eiam_20211201_models.SetPasswordComplexityConfigurationResponse:
        """
        @summary Configures a password complexity policy for an Employee Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS).
        
        @param request: SetPasswordComplexityConfigurationRequest
        @return: SetPasswordComplexityConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_password_complexity_configuration_with_options_async(request, runtime)

    def set_password_expiration_configuration_with_options(
        self,
        request: eiam_20211201_models.SetPasswordExpirationConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.SetPasswordExpirationConfigurationResponse:
        """
        @summary Configures a password expiration policy for an Employee Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS).
        
        @param request: SetPasswordExpirationConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetPasswordExpirationConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.effective_authentication_source_ids):
            query['EffectiveAuthenticationSourceIds'] = request.effective_authentication_source_ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.password_expiration_action):
            query['PasswordExpirationAction'] = request.password_expiration_action
        if not UtilClient.is_unset(request.password_expiration_notification_channels):
            query['PasswordExpirationNotificationChannels'] = request.password_expiration_notification_channels
        if not UtilClient.is_unset(request.password_expiration_notification_duration):
            query['PasswordExpirationNotificationDuration'] = request.password_expiration_notification_duration
        if not UtilClient.is_unset(request.password_expiration_notification_status):
            query['PasswordExpirationNotificationStatus'] = request.password_expiration_notification_status
        if not UtilClient.is_unset(request.password_expiration_status):
            query['PasswordExpirationStatus'] = request.password_expiration_status
        if not UtilClient.is_unset(request.password_forced_update_duration):
            query['PasswordForcedUpdateDuration'] = request.password_forced_update_duration
        if not UtilClient.is_unset(request.password_valid_max_day):
            query['PasswordValidMaxDay'] = request.password_valid_max_day
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetPasswordExpirationConfiguration',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.SetPasswordExpirationConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_password_expiration_configuration_with_options_async(
        self,
        request: eiam_20211201_models.SetPasswordExpirationConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.SetPasswordExpirationConfigurationResponse:
        """
        @summary Configures a password expiration policy for an Employee Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS).
        
        @param request: SetPasswordExpirationConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetPasswordExpirationConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.effective_authentication_source_ids):
            query['EffectiveAuthenticationSourceIds'] = request.effective_authentication_source_ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.password_expiration_action):
            query['PasswordExpirationAction'] = request.password_expiration_action
        if not UtilClient.is_unset(request.password_expiration_notification_channels):
            query['PasswordExpirationNotificationChannels'] = request.password_expiration_notification_channels
        if not UtilClient.is_unset(request.password_expiration_notification_duration):
            query['PasswordExpirationNotificationDuration'] = request.password_expiration_notification_duration
        if not UtilClient.is_unset(request.password_expiration_notification_status):
            query['PasswordExpirationNotificationStatus'] = request.password_expiration_notification_status
        if not UtilClient.is_unset(request.password_expiration_status):
            query['PasswordExpirationStatus'] = request.password_expiration_status
        if not UtilClient.is_unset(request.password_forced_update_duration):
            query['PasswordForcedUpdateDuration'] = request.password_forced_update_duration
        if not UtilClient.is_unset(request.password_valid_max_day):
            query['PasswordValidMaxDay'] = request.password_valid_max_day
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetPasswordExpirationConfiguration',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.SetPasswordExpirationConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_password_expiration_configuration(
        self,
        request: eiam_20211201_models.SetPasswordExpirationConfigurationRequest,
    ) -> eiam_20211201_models.SetPasswordExpirationConfigurationResponse:
        """
        @summary Configures a password expiration policy for an Employee Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS).
        
        @param request: SetPasswordExpirationConfigurationRequest
        @return: SetPasswordExpirationConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_password_expiration_configuration_with_options(request, runtime)

    async def set_password_expiration_configuration_async(
        self,
        request: eiam_20211201_models.SetPasswordExpirationConfigurationRequest,
    ) -> eiam_20211201_models.SetPasswordExpirationConfigurationResponse:
        """
        @summary Configures a password expiration policy for an Employee Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS).
        
        @param request: SetPasswordExpirationConfigurationRequest
        @return: SetPasswordExpirationConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_password_expiration_configuration_with_options_async(request, runtime)

    def set_password_history_configuration_with_options(
        self,
        request: eiam_20211201_models.SetPasswordHistoryConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.SetPasswordHistoryConfigurationResponse:
        """
        @summary Configures a password history policy for an Employee Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS).
        
        @param request: SetPasswordHistoryConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetPasswordHistoryConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.password_history_max_retention):
            query['PasswordHistoryMaxRetention'] = request.password_history_max_retention
        if not UtilClient.is_unset(request.password_history_status):
            query['PasswordHistoryStatus'] = request.password_history_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetPasswordHistoryConfiguration',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.SetPasswordHistoryConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_password_history_configuration_with_options_async(
        self,
        request: eiam_20211201_models.SetPasswordHistoryConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.SetPasswordHistoryConfigurationResponse:
        """
        @summary Configures a password history policy for an Employee Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS).
        
        @param request: SetPasswordHistoryConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetPasswordHistoryConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.password_history_max_retention):
            query['PasswordHistoryMaxRetention'] = request.password_history_max_retention
        if not UtilClient.is_unset(request.password_history_status):
            query['PasswordHistoryStatus'] = request.password_history_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetPasswordHistoryConfiguration',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.SetPasswordHistoryConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_password_history_configuration(
        self,
        request: eiam_20211201_models.SetPasswordHistoryConfigurationRequest,
    ) -> eiam_20211201_models.SetPasswordHistoryConfigurationResponse:
        """
        @summary Configures a password history policy for an Employee Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS).
        
        @param request: SetPasswordHistoryConfigurationRequest
        @return: SetPasswordHistoryConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_password_history_configuration_with_options(request, runtime)

    async def set_password_history_configuration_async(
        self,
        request: eiam_20211201_models.SetPasswordHistoryConfigurationRequest,
    ) -> eiam_20211201_models.SetPasswordHistoryConfigurationResponse:
        """
        @summary Configures a password history policy for an Employee Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS).
        
        @param request: SetPasswordHistoryConfigurationRequest
        @return: SetPasswordHistoryConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_password_history_configuration_with_options_async(request, runtime)

    def set_password_initialization_configuration_with_options(
        self,
        request: eiam_20211201_models.SetPasswordInitializationConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.SetPasswordInitializationConfigurationResponse:
        """
        @summary Sets the password initialization configurations for an Employee Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS).
        
        @param request: SetPasswordInitializationConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetPasswordInitializationConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.password_forced_update_status):
            query['PasswordForcedUpdateStatus'] = request.password_forced_update_status
        if not UtilClient.is_unset(request.password_initialization_notification_channels):
            query['PasswordInitializationNotificationChannels'] = request.password_initialization_notification_channels
        if not UtilClient.is_unset(request.password_initialization_status):
            query['PasswordInitializationStatus'] = request.password_initialization_status
        if not UtilClient.is_unset(request.password_initialization_type):
            query['PasswordInitializationType'] = request.password_initialization_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetPasswordInitializationConfiguration',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.SetPasswordInitializationConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_password_initialization_configuration_with_options_async(
        self,
        request: eiam_20211201_models.SetPasswordInitializationConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.SetPasswordInitializationConfigurationResponse:
        """
        @summary Sets the password initialization configurations for an Employee Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS).
        
        @param request: SetPasswordInitializationConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetPasswordInitializationConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.password_forced_update_status):
            query['PasswordForcedUpdateStatus'] = request.password_forced_update_status
        if not UtilClient.is_unset(request.password_initialization_notification_channels):
            query['PasswordInitializationNotificationChannels'] = request.password_initialization_notification_channels
        if not UtilClient.is_unset(request.password_initialization_status):
            query['PasswordInitializationStatus'] = request.password_initialization_status
        if not UtilClient.is_unset(request.password_initialization_type):
            query['PasswordInitializationType'] = request.password_initialization_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetPasswordInitializationConfiguration',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.SetPasswordInitializationConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_password_initialization_configuration(
        self,
        request: eiam_20211201_models.SetPasswordInitializationConfigurationRequest,
    ) -> eiam_20211201_models.SetPasswordInitializationConfigurationResponse:
        """
        @summary Sets the password initialization configurations for an Employee Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS).
        
        @param request: SetPasswordInitializationConfigurationRequest
        @return: SetPasswordInitializationConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_password_initialization_configuration_with_options(request, runtime)

    async def set_password_initialization_configuration_async(
        self,
        request: eiam_20211201_models.SetPasswordInitializationConfigurationRequest,
    ) -> eiam_20211201_models.SetPasswordInitializationConfigurationResponse:
        """
        @summary Sets the password initialization configurations for an Employee Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS).
        
        @param request: SetPasswordInitializationConfigurationRequest
        @return: SetPasswordInitializationConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_password_initialization_configuration_with_options_async(request, runtime)

    def set_user_primary_organizational_unit_with_options(
        self,
        request: eiam_20211201_models.SetUserPrimaryOrganizationalUnitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.SetUserPrimaryOrganizationalUnitResponse:
        """
        @summary Updates the primary organizational unit to which an Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM) account belongs. This account will be removed from the previous primary organizational unit and added to the new primary organization.
        
        @param request: SetUserPrimaryOrganizationalUnitRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetUserPrimaryOrganizationalUnitResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.organizational_unit_id):
            query['OrganizationalUnitId'] = request.organizational_unit_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetUserPrimaryOrganizationalUnit',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.SetUserPrimaryOrganizationalUnitResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_user_primary_organizational_unit_with_options_async(
        self,
        request: eiam_20211201_models.SetUserPrimaryOrganizationalUnitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.SetUserPrimaryOrganizationalUnitResponse:
        """
        @summary Updates the primary organizational unit to which an Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM) account belongs. This account will be removed from the previous primary organizational unit and added to the new primary organization.
        
        @param request: SetUserPrimaryOrganizationalUnitRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetUserPrimaryOrganizationalUnitResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.organizational_unit_id):
            query['OrganizationalUnitId'] = request.organizational_unit_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetUserPrimaryOrganizationalUnit',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.SetUserPrimaryOrganizationalUnitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_user_primary_organizational_unit(
        self,
        request: eiam_20211201_models.SetUserPrimaryOrganizationalUnitRequest,
    ) -> eiam_20211201_models.SetUserPrimaryOrganizationalUnitResponse:
        """
        @summary Updates the primary organizational unit to which an Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM) account belongs. This account will be removed from the previous primary organizational unit and added to the new primary organization.
        
        @param request: SetUserPrimaryOrganizationalUnitRequest
        @return: SetUserPrimaryOrganizationalUnitResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_user_primary_organizational_unit_with_options(request, runtime)

    async def set_user_primary_organizational_unit_async(
        self,
        request: eiam_20211201_models.SetUserPrimaryOrganizationalUnitRequest,
    ) -> eiam_20211201_models.SetUserPrimaryOrganizationalUnitResponse:
        """
        @summary Updates the primary organizational unit to which an Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM) account belongs. This account will be removed from the previous primary organizational unit and added to the new primary organization.
        
        @param request: SetUserPrimaryOrganizationalUnitRequest
        @return: SetUserPrimaryOrganizationalUnitResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_user_primary_organizational_unit_with_options_async(request, runtime)

    def unbind_user_authn_source_mapping_with_options(
        self,
        request: eiam_20211201_models.UnbindUserAuthnSourceMappingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UnbindUserAuthnSourceMappingResponse:
        """
        @summary 解绑三方登录账户
        
        @param request: UnbindUserAuthnSourceMappingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindUserAuthnSourceMappingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identity_provider_id):
            query['IdentityProviderId'] = request.identity_provider_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_external_id):
            query['UserExternalId'] = request.user_external_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindUserAuthnSourceMapping',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UnbindUserAuthnSourceMappingResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_user_authn_source_mapping_with_options_async(
        self,
        request: eiam_20211201_models.UnbindUserAuthnSourceMappingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UnbindUserAuthnSourceMappingResponse:
        """
        @summary 解绑三方登录账户
        
        @param request: UnbindUserAuthnSourceMappingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindUserAuthnSourceMappingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identity_provider_id):
            query['IdentityProviderId'] = request.identity_provider_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_external_id):
            query['UserExternalId'] = request.user_external_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindUserAuthnSourceMapping',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UnbindUserAuthnSourceMappingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_user_authn_source_mapping(
        self,
        request: eiam_20211201_models.UnbindUserAuthnSourceMappingRequest,
    ) -> eiam_20211201_models.UnbindUserAuthnSourceMappingResponse:
        """
        @summary 解绑三方登录账户
        
        @param request: UnbindUserAuthnSourceMappingRequest
        @return: UnbindUserAuthnSourceMappingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.unbind_user_authn_source_mapping_with_options(request, runtime)

    async def unbind_user_authn_source_mapping_async(
        self,
        request: eiam_20211201_models.UnbindUserAuthnSourceMappingRequest,
    ) -> eiam_20211201_models.UnbindUserAuthnSourceMappingResponse:
        """
        @summary 解绑三方登录账户
        
        @param request: UnbindUserAuthnSourceMappingRequest
        @return: UnbindUserAuthnSourceMappingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.unbind_user_authn_source_mapping_with_options_async(request, runtime)

    def unlock_user_with_options(
        self,
        request: eiam_20211201_models.UnlockUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UnlockUserResponse:
        """
        @summary Unlocks an Employee Identity and Access Management (EIAM) account of Identity as a Service (IDaaS) that is locked.
        
        @param request: UnlockUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnlockUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnlockUser',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UnlockUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def unlock_user_with_options_async(
        self,
        request: eiam_20211201_models.UnlockUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UnlockUserResponse:
        """
        @summary Unlocks an Employee Identity and Access Management (EIAM) account of Identity as a Service (IDaaS) that is locked.
        
        @param request: UnlockUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnlockUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnlockUser',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UnlockUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unlock_user(
        self,
        request: eiam_20211201_models.UnlockUserRequest,
    ) -> eiam_20211201_models.UnlockUserResponse:
        """
        @summary Unlocks an Employee Identity and Access Management (EIAM) account of Identity as a Service (IDaaS) that is locked.
        
        @param request: UnlockUserRequest
        @return: UnlockUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.unlock_user_with_options(request, runtime)

    async def unlock_user_async(
        self,
        request: eiam_20211201_models.UnlockUserRequest,
    ) -> eiam_20211201_models.UnlockUserResponse:
        """
        @summary Unlocks an Employee Identity and Access Management (EIAM) account of Identity as a Service (IDaaS) that is locked.
        
        @param request: UnlockUserRequest
        @return: UnlockUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.unlock_user_with_options_async(request, runtime)

    def update_application_authorization_type_with_options(
        self,
        request: eiam_20211201_models.UpdateApplicationAuthorizationTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UpdateApplicationAuthorizationTypeResponse:
        """
        @summary Modifies the authorization type of an Employee Identity and Access Management (EIAM) application.
        
        @param request: UpdateApplicationAuthorizationTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateApplicationAuthorizationTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.authorization_type):
            query['AuthorizationType'] = request.authorization_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApplicationAuthorizationType',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateApplicationAuthorizationTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_application_authorization_type_with_options_async(
        self,
        request: eiam_20211201_models.UpdateApplicationAuthorizationTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UpdateApplicationAuthorizationTypeResponse:
        """
        @summary Modifies the authorization type of an Employee Identity and Access Management (EIAM) application.
        
        @param request: UpdateApplicationAuthorizationTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateApplicationAuthorizationTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.authorization_type):
            query['AuthorizationType'] = request.authorization_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApplicationAuthorizationType',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateApplicationAuthorizationTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_application_authorization_type(
        self,
        request: eiam_20211201_models.UpdateApplicationAuthorizationTypeRequest,
    ) -> eiam_20211201_models.UpdateApplicationAuthorizationTypeResponse:
        """
        @summary Modifies the authorization type of an Employee Identity and Access Management (EIAM) application.
        
        @param request: UpdateApplicationAuthorizationTypeRequest
        @return: UpdateApplicationAuthorizationTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_application_authorization_type_with_options(request, runtime)

    async def update_application_authorization_type_async(
        self,
        request: eiam_20211201_models.UpdateApplicationAuthorizationTypeRequest,
    ) -> eiam_20211201_models.UpdateApplicationAuthorizationTypeResponse:
        """
        @summary Modifies the authorization type of an Employee Identity and Access Management (EIAM) application.
        
        @param request: UpdateApplicationAuthorizationTypeRequest
        @return: UpdateApplicationAuthorizationTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_application_authorization_type_with_options_async(request, runtime)

    def update_application_client_secret_expiration_time_with_options(
        self,
        request: eiam_20211201_models.UpdateApplicationClientSecretExpirationTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UpdateApplicationClientSecretExpirationTimeResponse:
        """
        @summary 更新应用的指定ClientSecret的到期时间
        
        @param request: UpdateApplicationClientSecretExpirationTimeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateApplicationClientSecretExpirationTimeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.expiration_time):
            query['ExpirationTime'] = request.expiration_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.secret_id):
            query['SecretId'] = request.secret_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApplicationClientSecretExpirationTime',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateApplicationClientSecretExpirationTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_application_client_secret_expiration_time_with_options_async(
        self,
        request: eiam_20211201_models.UpdateApplicationClientSecretExpirationTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UpdateApplicationClientSecretExpirationTimeResponse:
        """
        @summary 更新应用的指定ClientSecret的到期时间
        
        @param request: UpdateApplicationClientSecretExpirationTimeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateApplicationClientSecretExpirationTimeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.expiration_time):
            query['ExpirationTime'] = request.expiration_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.secret_id):
            query['SecretId'] = request.secret_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApplicationClientSecretExpirationTime',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateApplicationClientSecretExpirationTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_application_client_secret_expiration_time(
        self,
        request: eiam_20211201_models.UpdateApplicationClientSecretExpirationTimeRequest,
    ) -> eiam_20211201_models.UpdateApplicationClientSecretExpirationTimeResponse:
        """
        @summary 更新应用的指定ClientSecret的到期时间
        
        @param request: UpdateApplicationClientSecretExpirationTimeRequest
        @return: UpdateApplicationClientSecretExpirationTimeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_application_client_secret_expiration_time_with_options(request, runtime)

    async def update_application_client_secret_expiration_time_async(
        self,
        request: eiam_20211201_models.UpdateApplicationClientSecretExpirationTimeRequest,
    ) -> eiam_20211201_models.UpdateApplicationClientSecretExpirationTimeResponse:
        """
        @summary 更新应用的指定ClientSecret的到期时间
        
        @param request: UpdateApplicationClientSecretExpirationTimeRequest
        @return: UpdateApplicationClientSecretExpirationTimeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_application_client_secret_expiration_time_with_options_async(request, runtime)

    def update_application_description_with_options(
        self,
        request: eiam_20211201_models.UpdateApplicationDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UpdateApplicationDescriptionResponse:
        """
        @summary Modifies the description of an Employee Identity and Access Management (EIAM) application.
        
        @param request: UpdateApplicationDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateApplicationDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApplicationDescription',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateApplicationDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_application_description_with_options_async(
        self,
        request: eiam_20211201_models.UpdateApplicationDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UpdateApplicationDescriptionResponse:
        """
        @summary Modifies the description of an Employee Identity and Access Management (EIAM) application.
        
        @param request: UpdateApplicationDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateApplicationDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApplicationDescription',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateApplicationDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_application_description(
        self,
        request: eiam_20211201_models.UpdateApplicationDescriptionRequest,
    ) -> eiam_20211201_models.UpdateApplicationDescriptionResponse:
        """
        @summary Modifies the description of an Employee Identity and Access Management (EIAM) application.
        
        @param request: UpdateApplicationDescriptionRequest
        @return: UpdateApplicationDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_application_description_with_options(request, runtime)

    async def update_application_description_async(
        self,
        request: eiam_20211201_models.UpdateApplicationDescriptionRequest,
    ) -> eiam_20211201_models.UpdateApplicationDescriptionResponse:
        """
        @summary Modifies the description of an Employee Identity and Access Management (EIAM) application.
        
        @param request: UpdateApplicationDescriptionRequest
        @return: UpdateApplicationDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_application_description_with_options_async(request, runtime)

    def update_application_federated_credential_with_options(
        self,
        request: eiam_20211201_models.UpdateApplicationFederatedCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UpdateApplicationFederatedCredentialResponse:
        """
        @summary 更新应用联邦凭证
        
        @param request: UpdateApplicationFederatedCredentialRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateApplicationFederatedCredentialResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_federated_credential_id):
            query['ApplicationFederatedCredentialId'] = request.application_federated_credential_id
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.attribute_mappings):
            query['AttributeMappings'] = request.attribute_mappings
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.verification_condition):
            query['VerificationCondition'] = request.verification_condition
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApplicationFederatedCredential',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateApplicationFederatedCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_application_federated_credential_with_options_async(
        self,
        request: eiam_20211201_models.UpdateApplicationFederatedCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UpdateApplicationFederatedCredentialResponse:
        """
        @summary 更新应用联邦凭证
        
        @param request: UpdateApplicationFederatedCredentialRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateApplicationFederatedCredentialResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_federated_credential_id):
            query['ApplicationFederatedCredentialId'] = request.application_federated_credential_id
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.attribute_mappings):
            query['AttributeMappings'] = request.attribute_mappings
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.verification_condition):
            query['VerificationCondition'] = request.verification_condition
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApplicationFederatedCredential',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateApplicationFederatedCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_application_federated_credential(
        self,
        request: eiam_20211201_models.UpdateApplicationFederatedCredentialRequest,
    ) -> eiam_20211201_models.UpdateApplicationFederatedCredentialResponse:
        """
        @summary 更新应用联邦凭证
        
        @param request: UpdateApplicationFederatedCredentialRequest
        @return: UpdateApplicationFederatedCredentialResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_application_federated_credential_with_options(request, runtime)

    async def update_application_federated_credential_async(
        self,
        request: eiam_20211201_models.UpdateApplicationFederatedCredentialRequest,
    ) -> eiam_20211201_models.UpdateApplicationFederatedCredentialResponse:
        """
        @summary 更新应用联邦凭证
        
        @param request: UpdateApplicationFederatedCredentialRequest
        @return: UpdateApplicationFederatedCredentialResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_application_federated_credential_with_options_async(request, runtime)

    def update_application_federated_credential_description_with_options(
        self,
        request: eiam_20211201_models.UpdateApplicationFederatedCredentialDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UpdateApplicationFederatedCredentialDescriptionResponse:
        """
        @summary 更新应用联邦凭证描述
        
        @param request: UpdateApplicationFederatedCredentialDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateApplicationFederatedCredentialDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_federated_credential_id):
            query['ApplicationFederatedCredentialId'] = request.application_federated_credential_id
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApplicationFederatedCredentialDescription',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateApplicationFederatedCredentialDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_application_federated_credential_description_with_options_async(
        self,
        request: eiam_20211201_models.UpdateApplicationFederatedCredentialDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UpdateApplicationFederatedCredentialDescriptionResponse:
        """
        @summary 更新应用联邦凭证描述
        
        @param request: UpdateApplicationFederatedCredentialDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateApplicationFederatedCredentialDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_federated_credential_id):
            query['ApplicationFederatedCredentialId'] = request.application_federated_credential_id
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApplicationFederatedCredentialDescription',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateApplicationFederatedCredentialDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_application_federated_credential_description(
        self,
        request: eiam_20211201_models.UpdateApplicationFederatedCredentialDescriptionRequest,
    ) -> eiam_20211201_models.UpdateApplicationFederatedCredentialDescriptionResponse:
        """
        @summary 更新应用联邦凭证描述
        
        @param request: UpdateApplicationFederatedCredentialDescriptionRequest
        @return: UpdateApplicationFederatedCredentialDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_application_federated_credential_description_with_options(request, runtime)

    async def update_application_federated_credential_description_async(
        self,
        request: eiam_20211201_models.UpdateApplicationFederatedCredentialDescriptionRequest,
    ) -> eiam_20211201_models.UpdateApplicationFederatedCredentialDescriptionResponse:
        """
        @summary 更新应用联邦凭证描述
        
        @param request: UpdateApplicationFederatedCredentialDescriptionRequest
        @return: UpdateApplicationFederatedCredentialDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_application_federated_credential_description_with_options_async(request, runtime)

    def update_application_info_with_options(
        self,
        request: eiam_20211201_models.UpdateApplicationInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UpdateApplicationInfoResponse:
        """
        @summary 更新应用基本信息
        
        @param request: UpdateApplicationInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateApplicationInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.application_name):
            query['ApplicationName'] = request.application_name
        if not UtilClient.is_unset(request.application_visibility):
            query['ApplicationVisibility'] = request.application_visibility
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.logo_url):
            query['LogoUrl'] = request.logo_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApplicationInfo',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateApplicationInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_application_info_with_options_async(
        self,
        request: eiam_20211201_models.UpdateApplicationInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UpdateApplicationInfoResponse:
        """
        @summary 更新应用基本信息
        
        @param request: UpdateApplicationInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateApplicationInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.application_name):
            query['ApplicationName'] = request.application_name
        if not UtilClient.is_unset(request.application_visibility):
            query['ApplicationVisibility'] = request.application_visibility
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.logo_url):
            query['LogoUrl'] = request.logo_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApplicationInfo',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateApplicationInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_application_info(
        self,
        request: eiam_20211201_models.UpdateApplicationInfoRequest,
    ) -> eiam_20211201_models.UpdateApplicationInfoResponse:
        """
        @summary 更新应用基本信息
        
        @param request: UpdateApplicationInfoRequest
        @return: UpdateApplicationInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_application_info_with_options(request, runtime)

    async def update_application_info_async(
        self,
        request: eiam_20211201_models.UpdateApplicationInfoRequest,
    ) -> eiam_20211201_models.UpdateApplicationInfoResponse:
        """
        @summary 更新应用基本信息
        
        @param request: UpdateApplicationInfoRequest
        @return: UpdateApplicationInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_application_info_with_options_async(request, runtime)

    def update_application_token_expiration_time_with_options(
        self,
        request: eiam_20211201_models.UpdateApplicationTokenExpirationTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UpdateApplicationTokenExpirationTimeResponse:
        """
        @summary 更新ApplicationToken过期时间
        
        @param request: UpdateApplicationTokenExpirationTimeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateApplicationTokenExpirationTimeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.application_token_id):
            query['ApplicationTokenId'] = request.application_token_id
        if not UtilClient.is_unset(request.expiration_time):
            query['ExpirationTime'] = request.expiration_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApplicationTokenExpirationTime',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateApplicationTokenExpirationTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_application_token_expiration_time_with_options_async(
        self,
        request: eiam_20211201_models.UpdateApplicationTokenExpirationTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UpdateApplicationTokenExpirationTimeResponse:
        """
        @summary 更新ApplicationToken过期时间
        
        @param request: UpdateApplicationTokenExpirationTimeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateApplicationTokenExpirationTimeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.application_token_id):
            query['ApplicationTokenId'] = request.application_token_id
        if not UtilClient.is_unset(request.expiration_time):
            query['ExpirationTime'] = request.expiration_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApplicationTokenExpirationTime',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateApplicationTokenExpirationTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_application_token_expiration_time(
        self,
        request: eiam_20211201_models.UpdateApplicationTokenExpirationTimeRequest,
    ) -> eiam_20211201_models.UpdateApplicationTokenExpirationTimeResponse:
        """
        @summary 更新ApplicationToken过期时间
        
        @param request: UpdateApplicationTokenExpirationTimeRequest
        @return: UpdateApplicationTokenExpirationTimeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_application_token_expiration_time_with_options(request, runtime)

    async def update_application_token_expiration_time_async(
        self,
        request: eiam_20211201_models.UpdateApplicationTokenExpirationTimeRequest,
    ) -> eiam_20211201_models.UpdateApplicationTokenExpirationTimeResponse:
        """
        @summary 更新ApplicationToken过期时间
        
        @param request: UpdateApplicationTokenExpirationTimeRequest
        @return: UpdateApplicationTokenExpirationTimeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_application_token_expiration_time_with_options_async(request, runtime)

    def update_brand_with_options(
        self,
        request: eiam_20211201_models.UpdateBrandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UpdateBrandResponse:
        """
        @summary 修改品牌
        
        @param request: UpdateBrandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateBrandResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.brand_id):
            query['BrandId'] = request.brand_id
        if not UtilClient.is_unset(request.brand_name):
            query['BrandName'] = request.brand_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateBrand',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateBrandResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_brand_with_options_async(
        self,
        request: eiam_20211201_models.UpdateBrandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UpdateBrandResponse:
        """
        @summary 修改品牌
        
        @param request: UpdateBrandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateBrandResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.brand_id):
            query['BrandId'] = request.brand_id
        if not UtilClient.is_unset(request.brand_name):
            query['BrandName'] = request.brand_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateBrand',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateBrandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_brand(
        self,
        request: eiam_20211201_models.UpdateBrandRequest,
    ) -> eiam_20211201_models.UpdateBrandResponse:
        """
        @summary 修改品牌
        
        @param request: UpdateBrandRequest
        @return: UpdateBrandResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_brand_with_options(request, runtime)

    async def update_brand_async(
        self,
        request: eiam_20211201_models.UpdateBrandRequest,
    ) -> eiam_20211201_models.UpdateBrandResponse:
        """
        @summary 修改品牌
        
        @param request: UpdateBrandRequest
        @return: UpdateBrandResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_brand_with_options_async(request, runtime)

    def update_conditional_access_policy_with_options(
        self,
        request: eiam_20211201_models.UpdateConditionalAccessPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UpdateConditionalAccessPolicyResponse:
        """
        @summary Update Conditional Access Policy
        
        @description Update Conditional Access Policy
        
        @param request: UpdateConditionalAccessPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateConditionalAccessPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.conditional_access_policy_id):
            query['ConditionalAccessPolicyId'] = request.conditional_access_policy_id
        if not UtilClient.is_unset(request.conditional_access_policy_name):
            query['ConditionalAccessPolicyName'] = request.conditional_access_policy_name
        if not UtilClient.is_unset(request.conditions_config):
            query['ConditionsConfig'] = request.conditions_config
        if not UtilClient.is_unset(request.decision_config):
            query['DecisionConfig'] = request.decision_config
        if not UtilClient.is_unset(request.decision_type):
            query['DecisionType'] = request.decision_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateConditionalAccessPolicy',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateConditionalAccessPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_conditional_access_policy_with_options_async(
        self,
        request: eiam_20211201_models.UpdateConditionalAccessPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UpdateConditionalAccessPolicyResponse:
        """
        @summary Update Conditional Access Policy
        
        @description Update Conditional Access Policy
        
        @param request: UpdateConditionalAccessPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateConditionalAccessPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.conditional_access_policy_id):
            query['ConditionalAccessPolicyId'] = request.conditional_access_policy_id
        if not UtilClient.is_unset(request.conditional_access_policy_name):
            query['ConditionalAccessPolicyName'] = request.conditional_access_policy_name
        if not UtilClient.is_unset(request.conditions_config):
            query['ConditionsConfig'] = request.conditions_config
        if not UtilClient.is_unset(request.decision_config):
            query['DecisionConfig'] = request.decision_config
        if not UtilClient.is_unset(request.decision_type):
            query['DecisionType'] = request.decision_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateConditionalAccessPolicy',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateConditionalAccessPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_conditional_access_policy(
        self,
        request: eiam_20211201_models.UpdateConditionalAccessPolicyRequest,
    ) -> eiam_20211201_models.UpdateConditionalAccessPolicyResponse:
        """
        @summary Update Conditional Access Policy
        
        @description Update Conditional Access Policy
        
        @param request: UpdateConditionalAccessPolicyRequest
        @return: UpdateConditionalAccessPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_conditional_access_policy_with_options(request, runtime)

    async def update_conditional_access_policy_async(
        self,
        request: eiam_20211201_models.UpdateConditionalAccessPolicyRequest,
    ) -> eiam_20211201_models.UpdateConditionalAccessPolicyResponse:
        """
        @summary Update Conditional Access Policy
        
        @description Update Conditional Access Policy
        
        @param request: UpdateConditionalAccessPolicyRequest
        @return: UpdateConditionalAccessPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_conditional_access_policy_with_options_async(request, runtime)

    def update_conditional_access_policy_description_with_options(
        self,
        request: eiam_20211201_models.UpdateConditionalAccessPolicyDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UpdateConditionalAccessPolicyDescriptionResponse:
        """
        @summary Update Conditional Access Policy Description
        
        @description Update Conditional Access Policy Description
        
        @param request: UpdateConditionalAccessPolicyDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateConditionalAccessPolicyDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.conditional_access_policy_id):
            query['ConditionalAccessPolicyId'] = request.conditional_access_policy_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateConditionalAccessPolicyDescription',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateConditionalAccessPolicyDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_conditional_access_policy_description_with_options_async(
        self,
        request: eiam_20211201_models.UpdateConditionalAccessPolicyDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UpdateConditionalAccessPolicyDescriptionResponse:
        """
        @summary Update Conditional Access Policy Description
        
        @description Update Conditional Access Policy Description
        
        @param request: UpdateConditionalAccessPolicyDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateConditionalAccessPolicyDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.conditional_access_policy_id):
            query['ConditionalAccessPolicyId'] = request.conditional_access_policy_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateConditionalAccessPolicyDescription',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateConditionalAccessPolicyDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_conditional_access_policy_description(
        self,
        request: eiam_20211201_models.UpdateConditionalAccessPolicyDescriptionRequest,
    ) -> eiam_20211201_models.UpdateConditionalAccessPolicyDescriptionResponse:
        """
        @summary Update Conditional Access Policy Description
        
        @description Update Conditional Access Policy Description
        
        @param request: UpdateConditionalAccessPolicyDescriptionRequest
        @return: UpdateConditionalAccessPolicyDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_conditional_access_policy_description_with_options(request, runtime)

    async def update_conditional_access_policy_description_async(
        self,
        request: eiam_20211201_models.UpdateConditionalAccessPolicyDescriptionRequest,
    ) -> eiam_20211201_models.UpdateConditionalAccessPolicyDescriptionResponse:
        """
        @summary Update Conditional Access Policy Description
        
        @description Update Conditional Access Policy Description
        
        @param request: UpdateConditionalAccessPolicyDescriptionRequest
        @return: UpdateConditionalAccessPolicyDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_conditional_access_policy_description_with_options_async(request, runtime)

    def update_custom_privacy_policy_with_options(
        self,
        request: eiam_20211201_models.UpdateCustomPrivacyPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UpdateCustomPrivacyPolicyResponse:
        """
        @summary 更新自定义条款
        
        @param request: UpdateCustomPrivacyPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCustomPrivacyPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_privacy_policy_contents):
            query['CustomPrivacyPolicyContents'] = request.custom_privacy_policy_contents
        if not UtilClient.is_unset(request.custom_privacy_policy_id):
            query['CustomPrivacyPolicyId'] = request.custom_privacy_policy_id
        if not UtilClient.is_unset(request.custom_privacy_policy_name):
            query['CustomPrivacyPolicyName'] = request.custom_privacy_policy_name
        if not UtilClient.is_unset(request.default_language_code):
            query['DefaultLanguageCode'] = request.default_language_code
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_consent_type):
            query['UserConsentType'] = request.user_consent_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCustomPrivacyPolicy',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateCustomPrivacyPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_custom_privacy_policy_with_options_async(
        self,
        request: eiam_20211201_models.UpdateCustomPrivacyPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UpdateCustomPrivacyPolicyResponse:
        """
        @summary 更新自定义条款
        
        @param request: UpdateCustomPrivacyPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCustomPrivacyPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_privacy_policy_contents):
            query['CustomPrivacyPolicyContents'] = request.custom_privacy_policy_contents
        if not UtilClient.is_unset(request.custom_privacy_policy_id):
            query['CustomPrivacyPolicyId'] = request.custom_privacy_policy_id
        if not UtilClient.is_unset(request.custom_privacy_policy_name):
            query['CustomPrivacyPolicyName'] = request.custom_privacy_policy_name
        if not UtilClient.is_unset(request.default_language_code):
            query['DefaultLanguageCode'] = request.default_language_code
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_consent_type):
            query['UserConsentType'] = request.user_consent_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCustomPrivacyPolicy',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateCustomPrivacyPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_custom_privacy_policy(
        self,
        request: eiam_20211201_models.UpdateCustomPrivacyPolicyRequest,
    ) -> eiam_20211201_models.UpdateCustomPrivacyPolicyResponse:
        """
        @summary 更新自定义条款
        
        @param request: UpdateCustomPrivacyPolicyRequest
        @return: UpdateCustomPrivacyPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_custom_privacy_policy_with_options(request, runtime)

    async def update_custom_privacy_policy_async(
        self,
        request: eiam_20211201_models.UpdateCustomPrivacyPolicyRequest,
    ) -> eiam_20211201_models.UpdateCustomPrivacyPolicyResponse:
        """
        @summary 更新自定义条款
        
        @param request: UpdateCustomPrivacyPolicyRequest
        @return: UpdateCustomPrivacyPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_custom_privacy_policy_with_options_async(request, runtime)

    def update_domain_brand_with_options(
        self,
        request: eiam_20211201_models.UpdateDomainBrandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UpdateDomainBrandResponse:
        """
        @summary 修改域名关联的品牌。
        
        @param request: UpdateDomainBrandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDomainBrandResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.brand_id):
            query['BrandId'] = request.brand_id
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDomainBrand',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateDomainBrandResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_domain_brand_with_options_async(
        self,
        request: eiam_20211201_models.UpdateDomainBrandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UpdateDomainBrandResponse:
        """
        @summary 修改域名关联的品牌。
        
        @param request: UpdateDomainBrandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDomainBrandResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.brand_id):
            query['BrandId'] = request.brand_id
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDomainBrand',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateDomainBrandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_domain_brand(
        self,
        request: eiam_20211201_models.UpdateDomainBrandRequest,
    ) -> eiam_20211201_models.UpdateDomainBrandResponse:
        """
        @summary 修改域名关联的品牌。
        
        @param request: UpdateDomainBrandRequest
        @return: UpdateDomainBrandResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_domain_brand_with_options(request, runtime)

    async def update_domain_brand_async(
        self,
        request: eiam_20211201_models.UpdateDomainBrandRequest,
    ) -> eiam_20211201_models.UpdateDomainBrandResponse:
        """
        @summary 修改域名关联的品牌。
        
        @param request: UpdateDomainBrandRequest
        @return: UpdateDomainBrandResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_domain_brand_with_options_async(request, runtime)

    def update_domain_icp_number_with_options(
        self,
        request: eiam_20211201_models.UpdateDomainIcpNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UpdateDomainIcpNumberResponse:
        """
        @summary 更新域名备案号。
        
        @param request: UpdateDomainIcpNumberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDomainIcpNumberResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.icp_number):
            query['IcpNumber'] = request.icp_number
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDomainIcpNumber',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateDomainIcpNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_domain_icp_number_with_options_async(
        self,
        request: eiam_20211201_models.UpdateDomainIcpNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UpdateDomainIcpNumberResponse:
        """
        @summary 更新域名备案号。
        
        @param request: UpdateDomainIcpNumberRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDomainIcpNumberResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.icp_number):
            query['IcpNumber'] = request.icp_number
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDomainIcpNumber',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateDomainIcpNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_domain_icp_number(
        self,
        request: eiam_20211201_models.UpdateDomainIcpNumberRequest,
    ) -> eiam_20211201_models.UpdateDomainIcpNumberResponse:
        """
        @summary 更新域名备案号。
        
        @param request: UpdateDomainIcpNumberRequest
        @return: UpdateDomainIcpNumberResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_domain_icp_number_with_options(request, runtime)

    async def update_domain_icp_number_async(
        self,
        request: eiam_20211201_models.UpdateDomainIcpNumberRequest,
    ) -> eiam_20211201_models.UpdateDomainIcpNumberResponse:
        """
        @summary 更新域名备案号。
        
        @param request: UpdateDomainIcpNumberRequest
        @return: UpdateDomainIcpNumberResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_domain_icp_number_with_options_async(request, runtime)

    def update_federated_credential_provider_with_options(
        self,
        request: eiam_20211201_models.UpdateFederatedCredentialProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UpdateFederatedCredentialProviderResponse:
        """
        @summary 更新联邦凭证提供方
        
        @param request: UpdateFederatedCredentialProviderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFederatedCredentialProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.federated_credential_provider_id):
            query['FederatedCredentialProviderId'] = request.federated_credential_provider_id
        if not UtilClient.is_unset(request.federated_credential_provider_name):
            query['FederatedCredentialProviderName'] = request.federated_credential_provider_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_access_endpoint_id):
            query['NetworkAccessEndpointId'] = request.network_access_endpoint_id
        if not UtilClient.is_unset(request.oidc_provider_config):
            query['OidcProviderConfig'] = request.oidc_provider_config
        if not UtilClient.is_unset(request.pkcs_7provider_config):
            query['Pkcs7ProviderConfig'] = request.pkcs_7provider_config
        if not UtilClient.is_unset(request.private_ca_provider_config):
            query['PrivateCaProviderConfig'] = request.private_ca_provider_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFederatedCredentialProvider',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateFederatedCredentialProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_federated_credential_provider_with_options_async(
        self,
        request: eiam_20211201_models.UpdateFederatedCredentialProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UpdateFederatedCredentialProviderResponse:
        """
        @summary 更新联邦凭证提供方
        
        @param request: UpdateFederatedCredentialProviderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFederatedCredentialProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.federated_credential_provider_id):
            query['FederatedCredentialProviderId'] = request.federated_credential_provider_id
        if not UtilClient.is_unset(request.federated_credential_provider_name):
            query['FederatedCredentialProviderName'] = request.federated_credential_provider_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_access_endpoint_id):
            query['NetworkAccessEndpointId'] = request.network_access_endpoint_id
        if not UtilClient.is_unset(request.oidc_provider_config):
            query['OidcProviderConfig'] = request.oidc_provider_config
        if not UtilClient.is_unset(request.pkcs_7provider_config):
            query['Pkcs7ProviderConfig'] = request.pkcs_7provider_config
        if not UtilClient.is_unset(request.private_ca_provider_config):
            query['PrivateCaProviderConfig'] = request.private_ca_provider_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFederatedCredentialProvider',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateFederatedCredentialProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_federated_credential_provider(
        self,
        request: eiam_20211201_models.UpdateFederatedCredentialProviderRequest,
    ) -> eiam_20211201_models.UpdateFederatedCredentialProviderResponse:
        """
        @summary 更新联邦凭证提供方
        
        @param request: UpdateFederatedCredentialProviderRequest
        @return: UpdateFederatedCredentialProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_federated_credential_provider_with_options(request, runtime)

    async def update_federated_credential_provider_async(
        self,
        request: eiam_20211201_models.UpdateFederatedCredentialProviderRequest,
    ) -> eiam_20211201_models.UpdateFederatedCredentialProviderResponse:
        """
        @summary 更新联邦凭证提供方
        
        @param request: UpdateFederatedCredentialProviderRequest
        @return: UpdateFederatedCredentialProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_federated_credential_provider_with_options_async(request, runtime)

    def update_federated_credential_provider_description_with_options(
        self,
        request: eiam_20211201_models.UpdateFederatedCredentialProviderDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UpdateFederatedCredentialProviderDescriptionResponse:
        """
        @summary 更新联邦凭证提供方描述
        
        @param request: UpdateFederatedCredentialProviderDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFederatedCredentialProviderDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.federated_credential_provider_id):
            query['FederatedCredentialProviderId'] = request.federated_credential_provider_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFederatedCredentialProviderDescription',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateFederatedCredentialProviderDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_federated_credential_provider_description_with_options_async(
        self,
        request: eiam_20211201_models.UpdateFederatedCredentialProviderDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UpdateFederatedCredentialProviderDescriptionResponse:
        """
        @summary 更新联邦凭证提供方描述
        
        @param request: UpdateFederatedCredentialProviderDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFederatedCredentialProviderDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.federated_credential_provider_id):
            query['FederatedCredentialProviderId'] = request.federated_credential_provider_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFederatedCredentialProviderDescription',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateFederatedCredentialProviderDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_federated_credential_provider_description(
        self,
        request: eiam_20211201_models.UpdateFederatedCredentialProviderDescriptionRequest,
    ) -> eiam_20211201_models.UpdateFederatedCredentialProviderDescriptionResponse:
        """
        @summary 更新联邦凭证提供方描述
        
        @param request: UpdateFederatedCredentialProviderDescriptionRequest
        @return: UpdateFederatedCredentialProviderDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_federated_credential_provider_description_with_options(request, runtime)

    async def update_federated_credential_provider_description_async(
        self,
        request: eiam_20211201_models.UpdateFederatedCredentialProviderDescriptionRequest,
    ) -> eiam_20211201_models.UpdateFederatedCredentialProviderDescriptionResponse:
        """
        @summary 更新联邦凭证提供方描述
        
        @param request: UpdateFederatedCredentialProviderDescriptionRequest
        @return: UpdateFederatedCredentialProviderDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_federated_credential_provider_description_with_options_async(request, runtime)

    def update_group_with_options(
        self,
        request: eiam_20211201_models.UpdateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UpdateGroupResponse:
        """
        @summary Updates the information about an account group in Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM). If the information is empty, the information is not updated by default.
        
        @param request: UpdateGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_external_id):
            query['GroupExternalId'] = request.group_external_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGroup',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_group_with_options_async(
        self,
        request: eiam_20211201_models.UpdateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UpdateGroupResponse:
        """
        @summary Updates the information about an account group in Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM). If the information is empty, the information is not updated by default.
        
        @param request: UpdateGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_external_id):
            query['GroupExternalId'] = request.group_external_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGroup',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_group(
        self,
        request: eiam_20211201_models.UpdateGroupRequest,
    ) -> eiam_20211201_models.UpdateGroupResponse:
        """
        @summary Updates the information about an account group in Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM). If the information is empty, the information is not updated by default.
        
        @param request: UpdateGroupRequest
        @return: UpdateGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_group_with_options(request, runtime)

    async def update_group_async(
        self,
        request: eiam_20211201_models.UpdateGroupRequest,
    ) -> eiam_20211201_models.UpdateGroupResponse:
        """
        @summary Updates the information about an account group in Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM). If the information is empty, the information is not updated by default.
        
        @param request: UpdateGroupRequest
        @return: UpdateGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_group_with_options_async(request, runtime)

    def update_group_description_with_options(
        self,
        request: eiam_20211201_models.UpdateGroupDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UpdateGroupDescriptionResponse:
        """
        @summary Updates the description of an Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM) account group.
        
        @param request: UpdateGroupDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateGroupDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGroupDescription',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateGroupDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_group_description_with_options_async(
        self,
        request: eiam_20211201_models.UpdateGroupDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UpdateGroupDescriptionResponse:
        """
        @summary Updates the description of an Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM) account group.
        
        @param request: UpdateGroupDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateGroupDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGroupDescription',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateGroupDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_group_description(
        self,
        request: eiam_20211201_models.UpdateGroupDescriptionRequest,
    ) -> eiam_20211201_models.UpdateGroupDescriptionResponse:
        """
        @summary Updates the description of an Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM) account group.
        
        @param request: UpdateGroupDescriptionRequest
        @return: UpdateGroupDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_group_description_with_options(request, runtime)

    async def update_group_description_async(
        self,
        request: eiam_20211201_models.UpdateGroupDescriptionRequest,
    ) -> eiam_20211201_models.UpdateGroupDescriptionResponse:
        """
        @summary Updates the description of an Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM) account group.
        
        @param request: UpdateGroupDescriptionRequest
        @return: UpdateGroupDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_group_description_with_options_async(request, runtime)

    def update_identity_provider_with_options(
        self,
        request: eiam_20211201_models.UpdateIdentityProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UpdateIdentityProviderResponse:
        """
        @summary 更新idp基础配置
        
        @param request: UpdateIdentityProviderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateIdentityProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dingtalk_app_config):
            query['DingtalkAppConfig'] = request.dingtalk_app_config
        if not UtilClient.is_unset(request.identity_provider_id):
            query['IdentityProviderId'] = request.identity_provider_id
        if not UtilClient.is_unset(request.identity_provider_name):
            query['IdentityProviderName'] = request.identity_provider_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lark_config):
            query['LarkConfig'] = request.lark_config
        if not UtilClient.is_unset(request.ldap_config):
            query['LdapConfig'] = request.ldap_config
        if not UtilClient.is_unset(request.logo_url):
            query['LogoUrl'] = request.logo_url
        if not UtilClient.is_unset(request.network_access_endpoint_id):
            query['NetworkAccessEndpointId'] = request.network_access_endpoint_id
        if not UtilClient.is_unset(request.oidc_config):
            query['OidcConfig'] = request.oidc_config
        if not UtilClient.is_unset(request.we_com_config):
            query['WeComConfig'] = request.we_com_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateIdentityProvider',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateIdentityProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_identity_provider_with_options_async(
        self,
        request: eiam_20211201_models.UpdateIdentityProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UpdateIdentityProviderResponse:
        """
        @summary 更新idp基础配置
        
        @param request: UpdateIdentityProviderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateIdentityProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dingtalk_app_config):
            query['DingtalkAppConfig'] = request.dingtalk_app_config
        if not UtilClient.is_unset(request.identity_provider_id):
            query['IdentityProviderId'] = request.identity_provider_id
        if not UtilClient.is_unset(request.identity_provider_name):
            query['IdentityProviderName'] = request.identity_provider_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lark_config):
            query['LarkConfig'] = request.lark_config
        if not UtilClient.is_unset(request.ldap_config):
            query['LdapConfig'] = request.ldap_config
        if not UtilClient.is_unset(request.logo_url):
            query['LogoUrl'] = request.logo_url
        if not UtilClient.is_unset(request.network_access_endpoint_id):
            query['NetworkAccessEndpointId'] = request.network_access_endpoint_id
        if not UtilClient.is_unset(request.oidc_config):
            query['OidcConfig'] = request.oidc_config
        if not UtilClient.is_unset(request.we_com_config):
            query['WeComConfig'] = request.we_com_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateIdentityProvider',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateIdentityProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_identity_provider(
        self,
        request: eiam_20211201_models.UpdateIdentityProviderRequest,
    ) -> eiam_20211201_models.UpdateIdentityProviderResponse:
        """
        @summary 更新idp基础配置
        
        @param request: UpdateIdentityProviderRequest
        @return: UpdateIdentityProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_identity_provider_with_options(request, runtime)

    async def update_identity_provider_async(
        self,
        request: eiam_20211201_models.UpdateIdentityProviderRequest,
    ) -> eiam_20211201_models.UpdateIdentityProviderResponse:
        """
        @summary 更新idp基础配置
        
        @param request: UpdateIdentityProviderRequest
        @return: UpdateIdentityProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_identity_provider_with_options_async(request, runtime)

    def update_instance_description_with_options(
        self,
        request: eiam_20211201_models.UpdateInstanceDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UpdateInstanceDescriptionResponse:
        """
        @summary Modifies the description of an Enterprise Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS).
        
        @param request: UpdateInstanceDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInstanceDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInstanceDescription',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateInstanceDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_description_with_options_async(
        self,
        request: eiam_20211201_models.UpdateInstanceDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UpdateInstanceDescriptionResponse:
        """
        @summary Modifies the description of an Enterprise Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS).
        
        @param request: UpdateInstanceDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInstanceDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInstanceDescription',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateInstanceDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance_description(
        self,
        request: eiam_20211201_models.UpdateInstanceDescriptionRequest,
    ) -> eiam_20211201_models.UpdateInstanceDescriptionResponse:
        """
        @summary Modifies the description of an Enterprise Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS).
        
        @param request: UpdateInstanceDescriptionRequest
        @return: UpdateInstanceDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_instance_description_with_options(request, runtime)

    async def update_instance_description_async(
        self,
        request: eiam_20211201_models.UpdateInstanceDescriptionRequest,
    ) -> eiam_20211201_models.UpdateInstanceDescriptionResponse:
        """
        @summary Modifies the description of an Enterprise Identity and Access Management (EIAM) instance of Identity as a Service (IDaaS).
        
        @param request: UpdateInstanceDescriptionRequest
        @return: UpdateInstanceDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_instance_description_with_options_async(request, runtime)

    def update_network_access_endpoint_name_with_options(
        self,
        request: eiam_20211201_models.UpdateNetworkAccessEndpointNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UpdateNetworkAccessEndpointNameResponse:
        """
        @summary 更新一个专属网络端点的名称。
        
        @param request: UpdateNetworkAccessEndpointNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateNetworkAccessEndpointNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_access_endpoint_id):
            query['NetworkAccessEndpointId'] = request.network_access_endpoint_id
        if not UtilClient.is_unset(request.network_access_endpoint_name):
            query['NetworkAccessEndpointName'] = request.network_access_endpoint_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateNetworkAccessEndpointName',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateNetworkAccessEndpointNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_network_access_endpoint_name_with_options_async(
        self,
        request: eiam_20211201_models.UpdateNetworkAccessEndpointNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UpdateNetworkAccessEndpointNameResponse:
        """
        @summary 更新一个专属网络端点的名称。
        
        @param request: UpdateNetworkAccessEndpointNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateNetworkAccessEndpointNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_access_endpoint_id):
            query['NetworkAccessEndpointId'] = request.network_access_endpoint_id
        if not UtilClient.is_unset(request.network_access_endpoint_name):
            query['NetworkAccessEndpointName'] = request.network_access_endpoint_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateNetworkAccessEndpointName',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateNetworkAccessEndpointNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_network_access_endpoint_name(
        self,
        request: eiam_20211201_models.UpdateNetworkAccessEndpointNameRequest,
    ) -> eiam_20211201_models.UpdateNetworkAccessEndpointNameResponse:
        """
        @summary 更新一个专属网络端点的名称。
        
        @param request: UpdateNetworkAccessEndpointNameRequest
        @return: UpdateNetworkAccessEndpointNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_network_access_endpoint_name_with_options(request, runtime)

    async def update_network_access_endpoint_name_async(
        self,
        request: eiam_20211201_models.UpdateNetworkAccessEndpointNameRequest,
    ) -> eiam_20211201_models.UpdateNetworkAccessEndpointNameResponse:
        """
        @summary 更新一个专属网络端点的名称。
        
        @param request: UpdateNetworkAccessEndpointNameRequest
        @return: UpdateNetworkAccessEndpointNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_network_access_endpoint_name_with_options_async(request, runtime)

    def update_network_zone_with_options(
        self,
        request: eiam_20211201_models.UpdateNetworkZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UpdateNetworkZoneResponse:
        """
        @summary 更新网络区域对象
        
        @param request: UpdateNetworkZoneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateNetworkZoneResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ipv_4cidrs):
            query['Ipv4Cidrs'] = request.ipv_4cidrs
        if not UtilClient.is_unset(request.ipv_6cidrs):
            query['Ipv6Cidrs'] = request.ipv_6cidrs
        if not UtilClient.is_unset(request.network_zone_id):
            query['NetworkZoneId'] = request.network_zone_id
        if not UtilClient.is_unset(request.network_zone_name):
            query['NetworkZoneName'] = request.network_zone_name
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateNetworkZone',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateNetworkZoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_network_zone_with_options_async(
        self,
        request: eiam_20211201_models.UpdateNetworkZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UpdateNetworkZoneResponse:
        """
        @summary 更新网络区域对象
        
        @param request: UpdateNetworkZoneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateNetworkZoneResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ipv_4cidrs):
            query['Ipv4Cidrs'] = request.ipv_4cidrs
        if not UtilClient.is_unset(request.ipv_6cidrs):
            query['Ipv6Cidrs'] = request.ipv_6cidrs
        if not UtilClient.is_unset(request.network_zone_id):
            query['NetworkZoneId'] = request.network_zone_id
        if not UtilClient.is_unset(request.network_zone_name):
            query['NetworkZoneName'] = request.network_zone_name
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateNetworkZone',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateNetworkZoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_network_zone(
        self,
        request: eiam_20211201_models.UpdateNetworkZoneRequest,
    ) -> eiam_20211201_models.UpdateNetworkZoneResponse:
        """
        @summary 更新网络区域对象
        
        @param request: UpdateNetworkZoneRequest
        @return: UpdateNetworkZoneResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_network_zone_with_options(request, runtime)

    async def update_network_zone_async(
        self,
        request: eiam_20211201_models.UpdateNetworkZoneRequest,
    ) -> eiam_20211201_models.UpdateNetworkZoneResponse:
        """
        @summary 更新网络区域对象
        
        @param request: UpdateNetworkZoneRequest
        @return: UpdateNetworkZoneResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_network_zone_with_options_async(request, runtime)

    def update_network_zone_description_with_options(
        self,
        request: eiam_20211201_models.UpdateNetworkZoneDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UpdateNetworkZoneDescriptionResponse:
        """
        @summary 更新网络区域对象描述
        
        @param request: UpdateNetworkZoneDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateNetworkZoneDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_zone_id):
            query['NetworkZoneId'] = request.network_zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateNetworkZoneDescription',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateNetworkZoneDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_network_zone_description_with_options_async(
        self,
        request: eiam_20211201_models.UpdateNetworkZoneDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UpdateNetworkZoneDescriptionResponse:
        """
        @summary 更新网络区域对象描述
        
        @param request: UpdateNetworkZoneDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateNetworkZoneDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.network_zone_id):
            query['NetworkZoneId'] = request.network_zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateNetworkZoneDescription',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateNetworkZoneDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_network_zone_description(
        self,
        request: eiam_20211201_models.UpdateNetworkZoneDescriptionRequest,
    ) -> eiam_20211201_models.UpdateNetworkZoneDescriptionResponse:
        """
        @summary 更新网络区域对象描述
        
        @param request: UpdateNetworkZoneDescriptionRequest
        @return: UpdateNetworkZoneDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_network_zone_description_with_options(request, runtime)

    async def update_network_zone_description_async(
        self,
        request: eiam_20211201_models.UpdateNetworkZoneDescriptionRequest,
    ) -> eiam_20211201_models.UpdateNetworkZoneDescriptionResponse:
        """
        @summary 更新网络区域对象描述
        
        @param request: UpdateNetworkZoneDescriptionRequest
        @return: UpdateNetworkZoneDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_network_zone_description_with_options_async(request, runtime)

    def update_organizational_unit_with_options(
        self,
        request: eiam_20211201_models.UpdateOrganizationalUnitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UpdateOrganizationalUnitResponse:
        """
        @summary Updates the basic information about an Employee Identity and Access Management (EIAM) organization. The basic information about the organization is not updated by default if no parameter is specified.
        
        @param request: UpdateOrganizationalUnitRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateOrganizationalUnitResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.organizational_unit_id):
            query['OrganizationalUnitId'] = request.organizational_unit_id
        if not UtilClient.is_unset(request.organizational_unit_name):
            query['OrganizationalUnitName'] = request.organizational_unit_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateOrganizationalUnit',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateOrganizationalUnitResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_organizational_unit_with_options_async(
        self,
        request: eiam_20211201_models.UpdateOrganizationalUnitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UpdateOrganizationalUnitResponse:
        """
        @summary Updates the basic information about an Employee Identity and Access Management (EIAM) organization. The basic information about the organization is not updated by default if no parameter is specified.
        
        @param request: UpdateOrganizationalUnitRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateOrganizationalUnitResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.organizational_unit_id):
            query['OrganizationalUnitId'] = request.organizational_unit_id
        if not UtilClient.is_unset(request.organizational_unit_name):
            query['OrganizationalUnitName'] = request.organizational_unit_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateOrganizationalUnit',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateOrganizationalUnitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_organizational_unit(
        self,
        request: eiam_20211201_models.UpdateOrganizationalUnitRequest,
    ) -> eiam_20211201_models.UpdateOrganizationalUnitResponse:
        """
        @summary Updates the basic information about an Employee Identity and Access Management (EIAM) organization. The basic information about the organization is not updated by default if no parameter is specified.
        
        @param request: UpdateOrganizationalUnitRequest
        @return: UpdateOrganizationalUnitResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_organizational_unit_with_options(request, runtime)

    async def update_organizational_unit_async(
        self,
        request: eiam_20211201_models.UpdateOrganizationalUnitRequest,
    ) -> eiam_20211201_models.UpdateOrganizationalUnitResponse:
        """
        @summary Updates the basic information about an Employee Identity and Access Management (EIAM) organization. The basic information about the organization is not updated by default if no parameter is specified.
        
        @param request: UpdateOrganizationalUnitRequest
        @return: UpdateOrganizationalUnitResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_organizational_unit_with_options_async(request, runtime)

    def update_organizational_unit_description_with_options(
        self,
        request: eiam_20211201_models.UpdateOrganizationalUnitDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UpdateOrganizationalUnitDescriptionResponse:
        """
        @summary Modifies the description of an Employee Identity and Access Management (EIAM) organization.
        
        @param request: UpdateOrganizationalUnitDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateOrganizationalUnitDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.organizational_unit_id):
            query['OrganizationalUnitId'] = request.organizational_unit_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateOrganizationalUnitDescription',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateOrganizationalUnitDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_organizational_unit_description_with_options_async(
        self,
        request: eiam_20211201_models.UpdateOrganizationalUnitDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UpdateOrganizationalUnitDescriptionResponse:
        """
        @summary Modifies the description of an Employee Identity and Access Management (EIAM) organization.
        
        @param request: UpdateOrganizationalUnitDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateOrganizationalUnitDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.organizational_unit_id):
            query['OrganizationalUnitId'] = request.organizational_unit_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateOrganizationalUnitDescription',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateOrganizationalUnitDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_organizational_unit_description(
        self,
        request: eiam_20211201_models.UpdateOrganizationalUnitDescriptionRequest,
    ) -> eiam_20211201_models.UpdateOrganizationalUnitDescriptionResponse:
        """
        @summary Modifies the description of an Employee Identity and Access Management (EIAM) organization.
        
        @param request: UpdateOrganizationalUnitDescriptionRequest
        @return: UpdateOrganizationalUnitDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_organizational_unit_description_with_options(request, runtime)

    async def update_organizational_unit_description_async(
        self,
        request: eiam_20211201_models.UpdateOrganizationalUnitDescriptionRequest,
    ) -> eiam_20211201_models.UpdateOrganizationalUnitDescriptionResponse:
        """
        @summary Modifies the description of an Employee Identity and Access Management (EIAM) organization.
        
        @param request: UpdateOrganizationalUnitDescriptionRequest
        @return: UpdateOrganizationalUnitDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_organizational_unit_description_with_options_async(request, runtime)

    def update_organizational_unit_parent_id_with_options(
        self,
        request: eiam_20211201_models.UpdateOrganizationalUnitParentIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UpdateOrganizationalUnitParentIdResponse:
        """
        @summary Updates the parent organization ID of an organization in Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM). In this case, the organization is moved from a parent node to a new node.
        
        @param request: UpdateOrganizationalUnitParentIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateOrganizationalUnitParentIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.organizational_unit_id):
            query['OrganizationalUnitId'] = request.organizational_unit_id
        if not UtilClient.is_unset(request.parent_id):
            query['ParentId'] = request.parent_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateOrganizationalUnitParentId',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateOrganizationalUnitParentIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_organizational_unit_parent_id_with_options_async(
        self,
        request: eiam_20211201_models.UpdateOrganizationalUnitParentIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UpdateOrganizationalUnitParentIdResponse:
        """
        @summary Updates the parent organization ID of an organization in Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM). In this case, the organization is moved from a parent node to a new node.
        
        @param request: UpdateOrganizationalUnitParentIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateOrganizationalUnitParentIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.organizational_unit_id):
            query['OrganizationalUnitId'] = request.organizational_unit_id
        if not UtilClient.is_unset(request.parent_id):
            query['ParentId'] = request.parent_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateOrganizationalUnitParentId',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateOrganizationalUnitParentIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_organizational_unit_parent_id(
        self,
        request: eiam_20211201_models.UpdateOrganizationalUnitParentIdRequest,
    ) -> eiam_20211201_models.UpdateOrganizationalUnitParentIdResponse:
        """
        @summary Updates the parent organization ID of an organization in Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM). In this case, the organization is moved from a parent node to a new node.
        
        @param request: UpdateOrganizationalUnitParentIdRequest
        @return: UpdateOrganizationalUnitParentIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_organizational_unit_parent_id_with_options(request, runtime)

    async def update_organizational_unit_parent_id_async(
        self,
        request: eiam_20211201_models.UpdateOrganizationalUnitParentIdRequest,
    ) -> eiam_20211201_models.UpdateOrganizationalUnitParentIdResponse:
        """
        @summary Updates the parent organization ID of an organization in Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM). In this case, the organization is moved from a parent node to a new node.
        
        @param request: UpdateOrganizationalUnitParentIdRequest
        @return: UpdateOrganizationalUnitParentIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_organizational_unit_parent_id_with_options_async(request, runtime)

    def update_user_with_options(
        self,
        request: eiam_20211201_models.UpdateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UpdateUserResponse:
        """
        @summary Updates the basic information about an Employee Identity and Access Management (EIAM) account of Identity as a Service (IDaaS).
        
        @param request: UpdateUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_fields):
            query['CustomFields'] = request.custom_fields
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.email_verified):
            query['EmailVerified'] = request.email_verified
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.phone_number_verified):
            query['PhoneNumberVerified'] = request.phone_number_verified
        if not UtilClient.is_unset(request.phone_region):
            query['PhoneRegion'] = request.phone_region
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUser',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_with_options_async(
        self,
        request: eiam_20211201_models.UpdateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UpdateUserResponse:
        """
        @summary Updates the basic information about an Employee Identity and Access Management (EIAM) account of Identity as a Service (IDaaS).
        
        @param request: UpdateUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_fields):
            query['CustomFields'] = request.custom_fields
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.email_verified):
            query['EmailVerified'] = request.email_verified
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.phone_number_verified):
            query['PhoneNumberVerified'] = request.phone_number_verified
        if not UtilClient.is_unset(request.phone_region):
            query['PhoneRegion'] = request.phone_region
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUser',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user(
        self,
        request: eiam_20211201_models.UpdateUserRequest,
    ) -> eiam_20211201_models.UpdateUserResponse:
        """
        @summary Updates the basic information about an Employee Identity and Access Management (EIAM) account of Identity as a Service (IDaaS).
        
        @param request: UpdateUserRequest
        @return: UpdateUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_user_with_options(request, runtime)

    async def update_user_async(
        self,
        request: eiam_20211201_models.UpdateUserRequest,
    ) -> eiam_20211201_models.UpdateUserResponse:
        """
        @summary Updates the basic information about an Employee Identity and Access Management (EIAM) account of Identity as a Service (IDaaS).
        
        @param request: UpdateUserRequest
        @return: UpdateUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_user_with_options_async(request, runtime)

    def update_user_description_with_options(
        self,
        request: eiam_20211201_models.UpdateUserDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UpdateUserDescriptionResponse:
        """
        @summary Modifies the description of an Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM) account.
        
        @param request: UpdateUserDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUserDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUserDescription',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateUserDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_description_with_options_async(
        self,
        request: eiam_20211201_models.UpdateUserDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UpdateUserDescriptionResponse:
        """
        @summary Modifies the description of an Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM) account.
        
        @param request: UpdateUserDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUserDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUserDescription',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateUserDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user_description(
        self,
        request: eiam_20211201_models.UpdateUserDescriptionRequest,
    ) -> eiam_20211201_models.UpdateUserDescriptionResponse:
        """
        @summary Modifies the description of an Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM) account.
        
        @param request: UpdateUserDescriptionRequest
        @return: UpdateUserDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_user_description_with_options(request, runtime)

    async def update_user_description_async(
        self,
        request: eiam_20211201_models.UpdateUserDescriptionRequest,
    ) -> eiam_20211201_models.UpdateUserDescriptionResponse:
        """
        @summary Modifies the description of an Identity as a Service (IDaaS) Employee Identity and Access Management (EIAM) account.
        
        @param request: UpdateUserDescriptionRequest
        @return: UpdateUserDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_user_description_with_options_async(request, runtime)

    def update_user_password_with_options(
        self,
        request: eiam_20211201_models.UpdateUserPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UpdateUserPasswordResponse:
        """
        @summary Updates the password information of an Employee Identity and Access Management (EIAM) account of Identity as a Service (IDaaS). The password must meet the requirements of the password policies that are configured in the IDaaS console.
        
        @param request: UpdateUserPasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUserPasswordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.password_forced_update_status):
            query['PasswordForcedUpdateStatus'] = request.password_forced_update_status
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_notification_channels):
            query['UserNotificationChannels'] = request.user_notification_channels
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUserPassword',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateUserPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_password_with_options_async(
        self,
        request: eiam_20211201_models.UpdateUserPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eiam_20211201_models.UpdateUserPasswordResponse:
        """
        @summary Updates the password information of an Employee Identity and Access Management (EIAM) account of Identity as a Service (IDaaS). The password must meet the requirements of the password policies that are configured in the IDaaS console.
        
        @param request: UpdateUserPasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUserPasswordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.password_forced_update_status):
            query['PasswordForcedUpdateStatus'] = request.password_forced_update_status
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_notification_channels):
            query['UserNotificationChannels'] = request.user_notification_channels
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUserPassword',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eiam_20211201_models.UpdateUserPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user_password(
        self,
        request: eiam_20211201_models.UpdateUserPasswordRequest,
    ) -> eiam_20211201_models.UpdateUserPasswordResponse:
        """
        @summary Updates the password information of an Employee Identity and Access Management (EIAM) account of Identity as a Service (IDaaS). The password must meet the requirements of the password policies that are configured in the IDaaS console.
        
        @param request: UpdateUserPasswordRequest
        @return: UpdateUserPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_user_password_with_options(request, runtime)

    async def update_user_password_async(
        self,
        request: eiam_20211201_models.UpdateUserPasswordRequest,
    ) -> eiam_20211201_models.UpdateUserPasswordResponse:
        """
        @summary Updates the password information of an Employee Identity and Access Management (EIAM) account of Identity as a Service (IDaaS). The password must meet the requirements of the password policies that are configured in the IDaaS console.
        
        @param request: UpdateUserPasswordRequest
        @return: UpdateUserPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_user_password_with_options_async(request, runtime)
