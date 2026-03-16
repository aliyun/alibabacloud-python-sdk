# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_eds_user20210308 import models as main_models
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
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('eds-user', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def batch_set_desktop_manager_with_options(
        self,
        request: main_models.BatchSetDesktopManagerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchSetDesktopManagerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.business_channel):
            body['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.is_desktop_manager):
            body['IsDesktopManager'] = request.is_desktop_manager
        if not DaraCore.is_null(request.users):
            body['Users'] = request.users
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchSetDesktopManager',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchSetDesktopManagerResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_set_desktop_manager_with_options_async(
        self,
        request: main_models.BatchSetDesktopManagerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchSetDesktopManagerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.business_channel):
            body['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.is_desktop_manager):
            body['IsDesktopManager'] = request.is_desktop_manager
        if not DaraCore.is_null(request.users):
            body['Users'] = request.users
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchSetDesktopManager',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchSetDesktopManagerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_set_desktop_manager(
        self,
        request: main_models.BatchSetDesktopManagerRequest,
    ) -> main_models.BatchSetDesktopManagerResponse:
        runtime = RuntimeOptions()
        return self.batch_set_desktop_manager_with_options(request, runtime)

    async def batch_set_desktop_manager_async(
        self,
        request: main_models.BatchSetDesktopManagerRequest,
    ) -> main_models.BatchSetDesktopManagerResponse:
        runtime = RuntimeOptions()
        return await self.batch_set_desktop_manager_with_options_async(request, runtime)

    def change_user_password_with_options(
        self,
        request: main_models.ChangeUserPasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeUserPasswordResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.business_channel):
            body['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not DaraCore.is_null(request.new_password):
            body['NewPassword'] = request.new_password
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ChangeUserPassword',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeUserPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_user_password_with_options_async(
        self,
        request: main_models.ChangeUserPasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeUserPasswordResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.business_channel):
            body['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not DaraCore.is_null(request.new_password):
            body['NewPassword'] = request.new_password
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ChangeUserPassword',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeUserPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_user_password(
        self,
        request: main_models.ChangeUserPasswordRequest,
    ) -> main_models.ChangeUserPasswordResponse:
        runtime = RuntimeOptions()
        return self.change_user_password_with_options(request, runtime)

    async def change_user_password_async(
        self,
        request: main_models.ChangeUserPasswordRequest,
    ) -> main_models.ChangeUserPasswordResponse:
        runtime = RuntimeOptions()
        return await self.change_user_password_with_options_async(request, runtime)

    def check_used_property_with_options(
        self,
        request: main_models.CheckUsedPropertyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckUsedPropertyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_channel):
            query['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.property_id):
            query['PropertyId'] = request.property_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckUsedProperty',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckUsedPropertyResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_used_property_with_options_async(
        self,
        request: main_models.CheckUsedPropertyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckUsedPropertyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_channel):
            query['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.property_id):
            query['PropertyId'] = request.property_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckUsedProperty',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckUsedPropertyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_used_property(
        self,
        request: main_models.CheckUsedPropertyRequest,
    ) -> main_models.CheckUsedPropertyResponse:
        runtime = RuntimeOptions()
        return self.check_used_property_with_options(request, runtime)

    async def check_used_property_async(
        self,
        request: main_models.CheckUsedPropertyRequest,
    ) -> main_models.CheckUsedPropertyResponse:
        runtime = RuntimeOptions()
        return await self.check_used_property_with_options_async(request, runtime)

    def check_used_property_value_with_options(
        self,
        request: main_models.CheckUsedPropertyValueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckUsedPropertyValueResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_channel):
            query['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.property_id):
            query['PropertyId'] = request.property_id
        if not DaraCore.is_null(request.property_value_id):
            query['PropertyValueId'] = request.property_value_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckUsedPropertyValue',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckUsedPropertyValueResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_used_property_value_with_options_async(
        self,
        request: main_models.CheckUsedPropertyValueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckUsedPropertyValueResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_channel):
            query['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.property_id):
            query['PropertyId'] = request.property_id
        if not DaraCore.is_null(request.property_value_id):
            query['PropertyValueId'] = request.property_value_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckUsedPropertyValue',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckUsedPropertyValueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_used_property_value(
        self,
        request: main_models.CheckUsedPropertyValueRequest,
    ) -> main_models.CheckUsedPropertyValueResponse:
        runtime = RuntimeOptions()
        return self.check_used_property_value_with_options(request, runtime)

    async def check_used_property_value_async(
        self,
        request: main_models.CheckUsedPropertyValueRequest,
    ) -> main_models.CheckUsedPropertyValueResponse:
        runtime = RuntimeOptions()
        return await self.check_used_property_value_with_options_async(request, runtime)

    def create_group_with_options(
        self,
        request: main_models.CreateGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.business_channel):
            query['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.parent_group_id):
            query['ParentGroupId'] = request.parent_group_id
        if not DaraCore.is_null(request.solution_id):
            query['SolutionId'] = request.solution_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateGroup',
            version = '2021-03-08',
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
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.business_channel):
            query['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.parent_group_id):
            query['ParentGroupId'] = request.parent_group_id
        if not DaraCore.is_null(request.solution_id):
            query['SolutionId'] = request.solution_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateGroup',
            version = '2021-03-08',
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

    def create_org_with_options(
        self,
        request: main_models.CreateOrgRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOrgResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_channel):
            query['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.org_name):
            query['OrgName'] = request.org_name
        if not DaraCore.is_null(request.parent_org_id):
            query['ParentOrgId'] = request.parent_org_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateOrg',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOrgResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_org_with_options_async(
        self,
        request: main_models.CreateOrgRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOrgResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_channel):
            query['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.org_name):
            query['OrgName'] = request.org_name
        if not DaraCore.is_null(request.parent_org_id):
            query['ParentOrgId'] = request.parent_org_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateOrg',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOrgResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_org(
        self,
        request: main_models.CreateOrgRequest,
    ) -> main_models.CreateOrgResponse:
        runtime = RuntimeOptions()
        return self.create_org_with_options(request, runtime)

    async def create_org_async(
        self,
        request: main_models.CreateOrgRequest,
    ) -> main_models.CreateOrgResponse:
        runtime = RuntimeOptions()
        return await self.create_org_with_options_async(request, runtime)

    def create_property_with_options(
        self,
        request: main_models.CreatePropertyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePropertyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.business_channel):
            body['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.property_key):
            body['PropertyKey'] = request.property_key
        if not DaraCore.is_null(request.property_values):
            body['PropertyValues'] = request.property_values
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateProperty',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePropertyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_property_with_options_async(
        self,
        request: main_models.CreatePropertyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePropertyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.business_channel):
            body['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.property_key):
            body['PropertyKey'] = request.property_key
        if not DaraCore.is_null(request.property_values):
            body['PropertyValues'] = request.property_values
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateProperty',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePropertyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_property(
        self,
        request: main_models.CreatePropertyRequest,
    ) -> main_models.CreatePropertyResponse:
        runtime = RuntimeOptions()
        return self.create_property_with_options(request, runtime)

    async def create_property_async(
        self,
        request: main_models.CreatePropertyRequest,
    ) -> main_models.CreatePropertyResponse:
        runtime = RuntimeOptions()
        return await self.create_property_with_options_async(request, runtime)

    def create_resource_group_with_options(
        self,
        request: main_models.CreateResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_channel):
            query['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.is_resource_group_with_office_site):
            query['IsResourceGroupWithOfficeSite'] = request.is_resource_group_with_office_site
        if not DaraCore.is_null(request.platform):
            query['Platform'] = request.platform
        if not DaraCore.is_null(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateResourceGroup',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_resource_group_with_options_async(
        self,
        request: main_models.CreateResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_channel):
            query['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.is_resource_group_with_office_site):
            query['IsResourceGroupWithOfficeSite'] = request.is_resource_group_with_office_site
        if not DaraCore.is_null(request.platform):
            query['Platform'] = request.platform
        if not DaraCore.is_null(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateResourceGroup',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_resource_group(
        self,
        request: main_models.CreateResourceGroupRequest,
    ) -> main_models.CreateResourceGroupResponse:
        runtime = RuntimeOptions()
        return self.create_resource_group_with_options(request, runtime)

    async def create_resource_group_async(
        self,
        request: main_models.CreateResourceGroupRequest,
    ) -> main_models.CreateResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.create_resource_group_with_options_async(request, runtime)

    def create_users_with_options(
        self,
        request: main_models.CreateUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_lock_time):
            query['AutoLockTime'] = request.auto_lock_time
        if not DaraCore.is_null(request.business_channel):
            query['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.is_local_admin):
            query['IsLocalAdmin'] = request.is_local_admin
        if not DaraCore.is_null(request.password_expire_days):
            query['PasswordExpireDays'] = request.password_expire_days
        body = {}
        if not DaraCore.is_null(request.password):
            body['Password'] = request.password
        if not DaraCore.is_null(request.users):
            body['Users'] = request.users
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateUsers',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_users_with_options_async(
        self,
        request: main_models.CreateUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_lock_time):
            query['AutoLockTime'] = request.auto_lock_time
        if not DaraCore.is_null(request.business_channel):
            query['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.is_local_admin):
            query['IsLocalAdmin'] = request.is_local_admin
        if not DaraCore.is_null(request.password_expire_days):
            query['PasswordExpireDays'] = request.password_expire_days
        body = {}
        if not DaraCore.is_null(request.password):
            body['Password'] = request.password
        if not DaraCore.is_null(request.users):
            body['Users'] = request.users
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateUsers',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_users(
        self,
        request: main_models.CreateUsersRequest,
    ) -> main_models.CreateUsersResponse:
        runtime = RuntimeOptions()
        return self.create_users_with_options(request, runtime)

    async def create_users_async(
        self,
        request: main_models.CreateUsersRequest,
    ) -> main_models.CreateUsersResponse:
        runtime = RuntimeOptions()
        return await self.create_users_with_options_async(request, runtime)

    def delete_resource_group_with_options(
        self,
        request: main_models.DeleteResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_channel):
            query['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_group_ids):
            query['ResourceGroupIds'] = request.resource_group_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteResourceGroup',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_resource_group_with_options_async(
        self,
        request: main_models.DeleteResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_channel):
            query['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_group_ids):
            query['ResourceGroupIds'] = request.resource_group_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteResourceGroup',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_resource_group(
        self,
        request: main_models.DeleteResourceGroupRequest,
    ) -> main_models.DeleteResourceGroupResponse:
        runtime = RuntimeOptions()
        return self.delete_resource_group_with_options(request, runtime)

    async def delete_resource_group_async(
        self,
        request: main_models.DeleteResourceGroupRequest,
    ) -> main_models.DeleteResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.delete_resource_group_with_options_async(request, runtime)

    def delete_user_property_value_with_options(
        self,
        request: main_models.DeleteUserPropertyValueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserPropertyValueResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.business_channel):
            body['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.property_id):
            body['PropertyId'] = request.property_id
        if not DaraCore.is_null(request.property_value_id):
            body['PropertyValueId'] = request.property_value_id
        if not DaraCore.is_null(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUserPropertyValue',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUserPropertyValueResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_property_value_with_options_async(
        self,
        request: main_models.DeleteUserPropertyValueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserPropertyValueResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.business_channel):
            body['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.property_id):
            body['PropertyId'] = request.property_id
        if not DaraCore.is_null(request.property_value_id):
            body['PropertyValueId'] = request.property_value_id
        if not DaraCore.is_null(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUserPropertyValue',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUserPropertyValueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user_property_value(
        self,
        request: main_models.DeleteUserPropertyValueRequest,
    ) -> main_models.DeleteUserPropertyValueResponse:
        runtime = RuntimeOptions()
        return self.delete_user_property_value_with_options(request, runtime)

    async def delete_user_property_value_async(
        self,
        request: main_models.DeleteUserPropertyValueRequest,
    ) -> main_models.DeleteUserPropertyValueResponse:
        runtime = RuntimeOptions()
        return await self.delete_user_property_value_with_options_async(request, runtime)

    def describe_group_user_with_options(
        self,
        request: main_models.DescribeGroupUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGroupUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.business_channel):
            query['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.solution_id):
            query['SolutionId'] = request.solution_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGroupUser',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGroupUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_group_user_with_options_async(
        self,
        request: main_models.DescribeGroupUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGroupUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.business_channel):
            query['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.solution_id):
            query['SolutionId'] = request.solution_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGroupUser',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGroupUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_group_user(
        self,
        request: main_models.DescribeGroupUserRequest,
    ) -> main_models.DescribeGroupUserResponse:
        runtime = RuntimeOptions()
        return self.describe_group_user_with_options(request, runtime)

    async def describe_group_user_async(
        self,
        request: main_models.DescribeGroupUserRequest,
    ) -> main_models.DescribeGroupUserResponse:
        runtime = RuntimeOptions()
        return await self.describe_group_user_with_options_async(request, runtime)

    def describe_groups_with_options(
        self,
        request: main_models.DescribeGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.business_channel):
            query['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.exclude_attached_login_policy_groups):
            query['ExcludeAttachedLoginPolicyGroups'] = request.exclude_attached_login_policy_groups
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.idp_id):
            query['IdpId'] = request.idp_id
        if not DaraCore.is_null(request.login_policy_id):
            query['LoginPolicyId'] = request.login_policy_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.solution_id):
            query['SolutionId'] = request.solution_id
        if not DaraCore.is_null(request.transfer_file_need_approval):
            query['TransferFileNeedApproval'] = request.transfer_file_need_approval
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGroups',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_groups_with_options_async(
        self,
        request: main_models.DescribeGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_type):
            query['BizType'] = request.biz_type
        if not DaraCore.is_null(request.business_channel):
            query['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.exclude_attached_login_policy_groups):
            query['ExcludeAttachedLoginPolicyGroups'] = request.exclude_attached_login_policy_groups
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.idp_id):
            query['IdpId'] = request.idp_id
        if not DaraCore.is_null(request.login_policy_id):
            query['LoginPolicyId'] = request.login_policy_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.solution_id):
            query['SolutionId'] = request.solution_id
        if not DaraCore.is_null(request.transfer_file_need_approval):
            query['TransferFileNeedApproval'] = request.transfer_file_need_approval
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGroups',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_groups(
        self,
        request: main_models.DescribeGroupsRequest,
    ) -> main_models.DescribeGroupsResponse:
        runtime = RuntimeOptions()
        return self.describe_groups_with_options(request, runtime)

    async def describe_groups_async(
        self,
        request: main_models.DescribeGroupsRequest,
    ) -> main_models.DescribeGroupsResponse:
        runtime = RuntimeOptions()
        return await self.describe_groups_with_options_async(request, runtime)

    def describe_mfa_devices_with_options(
        self,
        request: main_models.DescribeMfaDevicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMfaDevicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ad_domain):
            query['AdDomain'] = request.ad_domain
        if not DaraCore.is_null(request.business_channel):
            query['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.end_user_ids):
            query['EndUserIds'] = request.end_user_ids
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.serial_numbers):
            query['SerialNumbers'] = request.serial_numbers
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMfaDevices',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMfaDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_mfa_devices_with_options_async(
        self,
        request: main_models.DescribeMfaDevicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMfaDevicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ad_domain):
            query['AdDomain'] = request.ad_domain
        if not DaraCore.is_null(request.business_channel):
            query['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.end_user_ids):
            query['EndUserIds'] = request.end_user_ids
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.serial_numbers):
            query['SerialNumbers'] = request.serial_numbers
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMfaDevices',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMfaDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_mfa_devices(
        self,
        request: main_models.DescribeMfaDevicesRequest,
    ) -> main_models.DescribeMfaDevicesResponse:
        runtime = RuntimeOptions()
        return self.describe_mfa_devices_with_options(request, runtime)

    async def describe_mfa_devices_async(
        self,
        request: main_models.DescribeMfaDevicesRequest,
    ) -> main_models.DescribeMfaDevicesResponse:
        runtime = RuntimeOptions()
        return await self.describe_mfa_devices_with_options_async(request, runtime)

    def describe_org_by_layer_with_options(
        self,
        request: main_models.DescribeOrgByLayerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOrgByLayerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.business_channel):
            body['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.org_name):
            body['OrgName'] = request.org_name
        if not DaraCore.is_null(request.parent_org_id):
            body['ParentOrgId'] = request.parent_org_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOrgByLayer',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOrgByLayerResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_org_by_layer_with_options_async(
        self,
        request: main_models.DescribeOrgByLayerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOrgByLayerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.business_channel):
            body['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.org_name):
            body['OrgName'] = request.org_name
        if not DaraCore.is_null(request.parent_org_id):
            body['ParentOrgId'] = request.parent_org_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOrgByLayer',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOrgByLayerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_org_by_layer(
        self,
        request: main_models.DescribeOrgByLayerRequest,
    ) -> main_models.DescribeOrgByLayerResponse:
        runtime = RuntimeOptions()
        return self.describe_org_by_layer_with_options(request, runtime)

    async def describe_org_by_layer_async(
        self,
        request: main_models.DescribeOrgByLayerRequest,
    ) -> main_models.DescribeOrgByLayerResponse:
        runtime = RuntimeOptions()
        return await self.describe_org_by_layer_with_options_async(request, runtime)

    def describe_orgs_with_options(
        self,
        tmp_req: main_models.DescribeOrgsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOrgsResponse:
        tmp_req.validate()
        request = main_models.DescribeOrgsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.show_extras):
            request.show_extras_shrink = Utils.array_to_string_with_specified_style(tmp_req.show_extras, 'ShowExtras', 'json')
        query = {}
        if not DaraCore.is_null(request.business_channel):
            query['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.org_name):
            query['OrgName'] = request.org_name
        if not DaraCore.is_null(request.parent_org_id):
            query['ParentOrgId'] = request.parent_org_id
        if not DaraCore.is_null(request.show_extras_shrink):
            query['ShowExtras'] = request.show_extras_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOrgs',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOrgsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_orgs_with_options_async(
        self,
        tmp_req: main_models.DescribeOrgsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOrgsResponse:
        tmp_req.validate()
        request = main_models.DescribeOrgsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.show_extras):
            request.show_extras_shrink = Utils.array_to_string_with_specified_style(tmp_req.show_extras, 'ShowExtras', 'json')
        query = {}
        if not DaraCore.is_null(request.business_channel):
            query['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.org_name):
            query['OrgName'] = request.org_name
        if not DaraCore.is_null(request.parent_org_id):
            query['ParentOrgId'] = request.parent_org_id
        if not DaraCore.is_null(request.show_extras_shrink):
            query['ShowExtras'] = request.show_extras_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOrgs',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOrgsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_orgs(
        self,
        request: main_models.DescribeOrgsRequest,
    ) -> main_models.DescribeOrgsResponse:
        runtime = RuntimeOptions()
        return self.describe_orgs_with_options(request, runtime)

    async def describe_orgs_async(
        self,
        request: main_models.DescribeOrgsRequest,
    ) -> main_models.DescribeOrgsResponse:
        runtime = RuntimeOptions()
        return await self.describe_orgs_with_options_async(request, runtime)

    def describe_resource_groups_with_options(
        self,
        request: main_models.DescribeResourceGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResourceGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_resource_group_ids):
            query['AliyunResourceGroupIds'] = request.aliyun_resource_group_ids
        if not DaraCore.is_null(request.business_channel):
            query['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.need_contain_resource_group_with_office_site):
            query['NeedContainResourceGroupWithOfficeSite'] = request.need_contain_resource_group_with_office_site
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.platform):
            query['Platform'] = request.platform
        if not DaraCore.is_null(request.resource_group_ids):
            query['ResourceGroupIds'] = request.resource_group_ids
        if not DaraCore.is_null(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeResourceGroups',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResourceGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resource_groups_with_options_async(
        self,
        request: main_models.DescribeResourceGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResourceGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_resource_group_ids):
            query['AliyunResourceGroupIds'] = request.aliyun_resource_group_ids
        if not DaraCore.is_null(request.business_channel):
            query['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.need_contain_resource_group_with_office_site):
            query['NeedContainResourceGroupWithOfficeSite'] = request.need_contain_resource_group_with_office_site
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.platform):
            query['Platform'] = request.platform
        if not DaraCore.is_null(request.resource_group_ids):
            query['ResourceGroupIds'] = request.resource_group_ids
        if not DaraCore.is_null(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeResourceGroups',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResourceGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resource_groups(
        self,
        request: main_models.DescribeResourceGroupsRequest,
    ) -> main_models.DescribeResourceGroupsResponse:
        runtime = RuntimeOptions()
        return self.describe_resource_groups_with_options(request, runtime)

    async def describe_resource_groups_async(
        self,
        request: main_models.DescribeResourceGroupsRequest,
    ) -> main_models.DescribeResourceGroupsResponse:
        runtime = RuntimeOptions()
        return await self.describe_resource_groups_with_options_async(request, runtime)

    def describe_users_with_options(
        self,
        tmp_req: main_models.DescribeUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUsersResponse:
        tmp_req.validate()
        request = main_models.DescribeUsersShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter_map):
            request.filter_map_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter_map, 'FilterMap', 'json')
        if not DaraCore.is_null(tmp_req.filter_with_assigned_resource):
            request.filter_with_assigned_resource_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter_with_assigned_resource, 'FilterWithAssignedResource', 'json')
        if not DaraCore.is_null(tmp_req.filter_with_assigned_resources):
            request.filter_with_assigned_resources_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter_with_assigned_resources, 'FilterWithAssignedResources', 'json')
        if not DaraCore.is_null(tmp_req.show_extras):
            request.show_extras_shrink = Utils.array_to_string_with_specified_style(tmp_req.show_extras, 'ShowExtras', 'json')
        query = {}
        if not DaraCore.is_null(request.business_channel):
            query['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.filter_map_shrink):
            query['FilterMap'] = request.filter_map_shrink
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        body = {}
        if not DaraCore.is_null(request.biz_type):
            body['BizType'] = request.biz_type
        if not DaraCore.is_null(request.end_user_ids):
            body['EndUserIds'] = request.end_user_ids
        if not DaraCore.is_null(request.exclude_end_user_ids):
            body['ExcludeEndUserIds'] = request.exclude_end_user_ids
        if not DaraCore.is_null(request.exclude_group_id):
            body['ExcludeGroupId'] = request.exclude_group_id
        if not DaraCore.is_null(request.filter_with_assigned_resource_shrink):
            body['FilterWithAssignedResource'] = request.filter_with_assigned_resource_shrink
        if not DaraCore.is_null(request.filter_with_assigned_resources_shrink):
            body['FilterWithAssignedResources'] = request.filter_with_assigned_resources_shrink
        if not DaraCore.is_null(request.group_id):
            body['GroupId'] = request.group_id
        if not DaraCore.is_null(request.is_query_all_sub_orgs):
            body['IsQueryAllSubOrgs'] = request.is_query_all_sub_orgs
        if not DaraCore.is_null(request.org_id):
            body['OrgId'] = request.org_id
        if not DaraCore.is_null(request.show_extras_shrink):
            body['ShowExtras'] = request.show_extras_shrink
        if not DaraCore.is_null(request.solution_id):
            body['SolutionId'] = request.solution_id
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUsers',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_users_with_options_async(
        self,
        tmp_req: main_models.DescribeUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUsersResponse:
        tmp_req.validate()
        request = main_models.DescribeUsersShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter_map):
            request.filter_map_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter_map, 'FilterMap', 'json')
        if not DaraCore.is_null(tmp_req.filter_with_assigned_resource):
            request.filter_with_assigned_resource_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter_with_assigned_resource, 'FilterWithAssignedResource', 'json')
        if not DaraCore.is_null(tmp_req.filter_with_assigned_resources):
            request.filter_with_assigned_resources_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter_with_assigned_resources, 'FilterWithAssignedResources', 'json')
        if not DaraCore.is_null(tmp_req.show_extras):
            request.show_extras_shrink = Utils.array_to_string_with_specified_style(tmp_req.show_extras, 'ShowExtras', 'json')
        query = {}
        if not DaraCore.is_null(request.business_channel):
            query['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.filter_map_shrink):
            query['FilterMap'] = request.filter_map_shrink
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        body = {}
        if not DaraCore.is_null(request.biz_type):
            body['BizType'] = request.biz_type
        if not DaraCore.is_null(request.end_user_ids):
            body['EndUserIds'] = request.end_user_ids
        if not DaraCore.is_null(request.exclude_end_user_ids):
            body['ExcludeEndUserIds'] = request.exclude_end_user_ids
        if not DaraCore.is_null(request.exclude_group_id):
            body['ExcludeGroupId'] = request.exclude_group_id
        if not DaraCore.is_null(request.filter_with_assigned_resource_shrink):
            body['FilterWithAssignedResource'] = request.filter_with_assigned_resource_shrink
        if not DaraCore.is_null(request.filter_with_assigned_resources_shrink):
            body['FilterWithAssignedResources'] = request.filter_with_assigned_resources_shrink
        if not DaraCore.is_null(request.group_id):
            body['GroupId'] = request.group_id
        if not DaraCore.is_null(request.is_query_all_sub_orgs):
            body['IsQueryAllSubOrgs'] = request.is_query_all_sub_orgs
        if not DaraCore.is_null(request.org_id):
            body['OrgId'] = request.org_id
        if not DaraCore.is_null(request.show_extras_shrink):
            body['ShowExtras'] = request.show_extras_shrink
        if not DaraCore.is_null(request.solution_id):
            body['SolutionId'] = request.solution_id
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUsers',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_users(
        self,
        request: main_models.DescribeUsersRequest,
    ) -> main_models.DescribeUsersResponse:
        runtime = RuntimeOptions()
        return self.describe_users_with_options(request, runtime)

    async def describe_users_async(
        self,
        request: main_models.DescribeUsersRequest,
    ) -> main_models.DescribeUsersResponse:
        runtime = RuntimeOptions()
        return await self.describe_users_with_options_async(request, runtime)

    def filter_users_with_options(
        self,
        tmp_req: main_models.FilterUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FilterUsersResponse:
        tmp_req.validate()
        request = main_models.FilterUsersShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter_map):
            request.filter_map_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter_map, 'FilterMap', 'json')
        if not DaraCore.is_null(tmp_req.order_param):
            request.order_param_shrink = Utils.array_to_string_with_specified_style(tmp_req.order_param, 'OrderParam', 'json')
        query = {}
        if not DaraCore.is_null(request.business_channel):
            query['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.exclude_end_user_ids):
            query['ExcludeEndUserIds'] = request.exclude_end_user_ids
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.filter_map_shrink):
            query['FilterMap'] = request.filter_map_shrink
        if not DaraCore.is_null(request.include_desktop_count):
            query['IncludeDesktopCount'] = request.include_desktop_count
        if not DaraCore.is_null(request.include_desktop_group_count):
            query['IncludeDesktopGroupCount'] = request.include_desktop_group_count
        if not DaraCore.is_null(request.include_end_user_ids):
            query['IncludeEndUserIds'] = request.include_end_user_ids
        if not DaraCore.is_null(request.include_org_info):
            query['IncludeOrgInfo'] = request.include_org_info
        if not DaraCore.is_null(request.include_support_idps):
            query['IncludeSupportIdps'] = request.include_support_idps
        if not DaraCore.is_null(request.is_query_all_sub_orgs):
            query['IsQueryAllSubOrgs'] = request.is_query_all_sub_orgs
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_param_shrink):
            query['OrderParam'] = request.order_param_shrink
        if not DaraCore.is_null(request.org_id):
            query['OrgId'] = request.org_id
        if not DaraCore.is_null(request.owner_type):
            query['OwnerType'] = request.owner_type
        if not DaraCore.is_null(request.property_filter_param):
            query['PropertyFilterParam'] = request.property_filter_param
        if not DaraCore.is_null(request.property_key_value_filter_param):
            query['PropertyKeyValueFilterParam'] = request.property_key_value_filter_param
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FilterUsers',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FilterUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def filter_users_with_options_async(
        self,
        tmp_req: main_models.FilterUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FilterUsersResponse:
        tmp_req.validate()
        request = main_models.FilterUsersShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter_map):
            request.filter_map_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter_map, 'FilterMap', 'json')
        if not DaraCore.is_null(tmp_req.order_param):
            request.order_param_shrink = Utils.array_to_string_with_specified_style(tmp_req.order_param, 'OrderParam', 'json')
        query = {}
        if not DaraCore.is_null(request.business_channel):
            query['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.exclude_end_user_ids):
            query['ExcludeEndUserIds'] = request.exclude_end_user_ids
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.filter_map_shrink):
            query['FilterMap'] = request.filter_map_shrink
        if not DaraCore.is_null(request.include_desktop_count):
            query['IncludeDesktopCount'] = request.include_desktop_count
        if not DaraCore.is_null(request.include_desktop_group_count):
            query['IncludeDesktopGroupCount'] = request.include_desktop_group_count
        if not DaraCore.is_null(request.include_end_user_ids):
            query['IncludeEndUserIds'] = request.include_end_user_ids
        if not DaraCore.is_null(request.include_org_info):
            query['IncludeOrgInfo'] = request.include_org_info
        if not DaraCore.is_null(request.include_support_idps):
            query['IncludeSupportIdps'] = request.include_support_idps
        if not DaraCore.is_null(request.is_query_all_sub_orgs):
            query['IsQueryAllSubOrgs'] = request.is_query_all_sub_orgs
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_param_shrink):
            query['OrderParam'] = request.order_param_shrink
        if not DaraCore.is_null(request.org_id):
            query['OrgId'] = request.org_id
        if not DaraCore.is_null(request.owner_type):
            query['OwnerType'] = request.owner_type
        if not DaraCore.is_null(request.property_filter_param):
            query['PropertyFilterParam'] = request.property_filter_param
        if not DaraCore.is_null(request.property_key_value_filter_param):
            query['PropertyKeyValueFilterParam'] = request.property_key_value_filter_param
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FilterUsers',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FilterUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def filter_users(
        self,
        request: main_models.FilterUsersRequest,
    ) -> main_models.FilterUsersResponse:
        runtime = RuntimeOptions()
        return self.filter_users_with_options(request, runtime)

    async def filter_users_async(
        self,
        request: main_models.FilterUsersRequest,
    ) -> main_models.FilterUsersResponse:
        runtime = RuntimeOptions()
        return await self.filter_users_with_options_async(request, runtime)

    def get_manager_info_by_auth_code_with_options(
        self,
        request: main_models.GetManagerInfoByAuthCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetManagerInfoByAuthCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetManagerInfoByAuthCode',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetManagerInfoByAuthCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_manager_info_by_auth_code_with_options_async(
        self,
        request: main_models.GetManagerInfoByAuthCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetManagerInfoByAuthCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_code):
            query['AuthCode'] = request.auth_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetManagerInfoByAuthCode',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetManagerInfoByAuthCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_manager_info_by_auth_code(
        self,
        request: main_models.GetManagerInfoByAuthCodeRequest,
    ) -> main_models.GetManagerInfoByAuthCodeResponse:
        runtime = RuntimeOptions()
        return self.get_manager_info_by_auth_code_with_options(request, runtime)

    async def get_manager_info_by_auth_code_async(
        self,
        request: main_models.GetManagerInfoByAuthCodeRequest,
    ) -> main_models.GetManagerInfoByAuthCodeResponse:
        runtime = RuntimeOptions()
        return await self.get_manager_info_by_auth_code_with_options_async(request, runtime)

    def init_tenant_alias_with_options(
        self,
        request: main_models.InitTenantAliasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InitTenantAliasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_channel):
            query['BusinessChannel'] = request.business_channel
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InitTenantAlias',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InitTenantAliasResponse(),
            self.call_api(params, req, runtime)
        )

    async def init_tenant_alias_with_options_async(
        self,
        request: main_models.InitTenantAliasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InitTenantAliasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_channel):
            query['BusinessChannel'] = request.business_channel
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InitTenantAlias',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InitTenantAliasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def init_tenant_alias(
        self,
        request: main_models.InitTenantAliasRequest,
    ) -> main_models.InitTenantAliasResponse:
        runtime = RuntimeOptions()
        return self.init_tenant_alias_with_options(request, runtime)

    async def init_tenant_alias_async(
        self,
        request: main_models.InitTenantAliasRequest,
    ) -> main_models.InitTenantAliasResponse:
        runtime = RuntimeOptions()
        return await self.init_tenant_alias_with_options_async(request, runtime)

    def list_property_with_options(
        self,
        request: main_models.ListPropertyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPropertyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_channel):
            query['BusinessChannel'] = request.business_channel
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProperty',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPropertyResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_property_with_options_async(
        self,
        request: main_models.ListPropertyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPropertyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_channel):
            query['BusinessChannel'] = request.business_channel
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProperty',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPropertyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_property(
        self,
        request: main_models.ListPropertyRequest,
    ) -> main_models.ListPropertyResponse:
        runtime = RuntimeOptions()
        return self.list_property_with_options(request, runtime)

    async def list_property_async(
        self,
        request: main_models.ListPropertyRequest,
    ) -> main_models.ListPropertyResponse:
        runtime = RuntimeOptions()
        return await self.list_property_with_options_async(request, runtime)

    def list_property_value_with_options(
        self,
        request: main_models.ListPropertyValueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPropertyValueResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_channel):
            query['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.property_id):
            query['PropertyId'] = request.property_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPropertyValue',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPropertyValueResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_property_value_with_options_async(
        self,
        request: main_models.ListPropertyValueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPropertyValueResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_channel):
            query['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.property_id):
            query['PropertyId'] = request.property_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPropertyValue',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPropertyValueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_property_value(
        self,
        request: main_models.ListPropertyValueRequest,
    ) -> main_models.ListPropertyValueResponse:
        runtime = RuntimeOptions()
        return self.list_property_value_with_options(request, runtime)

    async def list_property_value_async(
        self,
        request: main_models.ListPropertyValueRequest,
    ) -> main_models.ListPropertyValueResponse:
        runtime = RuntimeOptions()
        return await self.list_property_value_with_options_async(request, runtime)

    def lock_mfa_device_with_options(
        self,
        request: main_models.LockMfaDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LockMfaDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ad_domain):
            query['AdDomain'] = request.ad_domain
        if not DaraCore.is_null(request.business_channel):
            query['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.serial_number):
            query['SerialNumber'] = request.serial_number
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'LockMfaDevice',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LockMfaDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def lock_mfa_device_with_options_async(
        self,
        request: main_models.LockMfaDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LockMfaDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ad_domain):
            query['AdDomain'] = request.ad_domain
        if not DaraCore.is_null(request.business_channel):
            query['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.serial_number):
            query['SerialNumber'] = request.serial_number
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'LockMfaDevice',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LockMfaDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def lock_mfa_device(
        self,
        request: main_models.LockMfaDeviceRequest,
    ) -> main_models.LockMfaDeviceResponse:
        runtime = RuntimeOptions()
        return self.lock_mfa_device_with_options(request, runtime)

    async def lock_mfa_device_async(
        self,
        request: main_models.LockMfaDeviceRequest,
    ) -> main_models.LockMfaDeviceResponse:
        runtime = RuntimeOptions()
        return await self.lock_mfa_device_with_options_async(request, runtime)

    def lock_users_with_options(
        self,
        request: main_models.LockUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LockUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_channel):
            query['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.logout_session):
            query['LogoutSession'] = request.logout_session
        body = {}
        if not DaraCore.is_null(request.users):
            body['Users'] = request.users
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'LockUsers',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LockUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def lock_users_with_options_async(
        self,
        request: main_models.LockUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LockUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_channel):
            query['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.logout_session):
            query['LogoutSession'] = request.logout_session
        body = {}
        if not DaraCore.is_null(request.users):
            body['Users'] = request.users
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'LockUsers',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LockUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def lock_users(
        self,
        request: main_models.LockUsersRequest,
    ) -> main_models.LockUsersResponse:
        runtime = RuntimeOptions()
        return self.lock_users_with_options(request, runtime)

    async def lock_users_async(
        self,
        request: main_models.LockUsersRequest,
    ) -> main_models.LockUsersResponse:
        runtime = RuntimeOptions()
        return await self.lock_users_with_options_async(request, runtime)

    def modify_group_with_options(
        self,
        request: main_models.ModifyGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_channel):
            query['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.new_group_name):
            query['NewGroupName'] = request.new_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyGroup',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_group_with_options_async(
        self,
        request: main_models.ModifyGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_channel):
            query['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.new_group_name):
            query['NewGroupName'] = request.new_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyGroup',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_group(
        self,
        request: main_models.ModifyGroupRequest,
    ) -> main_models.ModifyGroupResponse:
        runtime = RuntimeOptions()
        return self.modify_group_with_options(request, runtime)

    async def modify_group_async(
        self,
        request: main_models.ModifyGroupRequest,
    ) -> main_models.ModifyGroupResponse:
        runtime = RuntimeOptions()
        return await self.modify_group_with_options_async(request, runtime)

    def modify_org_with_options(
        self,
        request: main_models.ModifyOrgRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyOrgResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_channel):
            query['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.org_id):
            query['OrgId'] = request.org_id
        if not DaraCore.is_null(request.org_name):
            query['OrgName'] = request.org_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyOrg',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyOrgResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_org_with_options_async(
        self,
        request: main_models.ModifyOrgRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyOrgResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_channel):
            query['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.org_id):
            query['OrgId'] = request.org_id
        if not DaraCore.is_null(request.org_name):
            query['OrgName'] = request.org_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyOrg',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyOrgResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_org(
        self,
        request: main_models.ModifyOrgRequest,
    ) -> main_models.ModifyOrgResponse:
        runtime = RuntimeOptions()
        return self.modify_org_with_options(request, runtime)

    async def modify_org_async(
        self,
        request: main_models.ModifyOrgRequest,
    ) -> main_models.ModifyOrgResponse:
        runtime = RuntimeOptions()
        return await self.modify_org_with_options_async(request, runtime)

    def modify_user_with_options(
        self,
        request: main_models.ModifyUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_channel):
            query['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not DaraCore.is_null(request.phone):
            query['Phone'] = request.phone
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyUser',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_user_with_options_async(
        self,
        request: main_models.ModifyUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_channel):
            query['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not DaraCore.is_null(request.phone):
            query['Phone'] = request.phone
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyUser',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_user(
        self,
        request: main_models.ModifyUserRequest,
    ) -> main_models.ModifyUserResponse:
        runtime = RuntimeOptions()
        return self.modify_user_with_options(request, runtime)

    async def modify_user_async(
        self,
        request: main_models.ModifyUserRequest,
    ) -> main_models.ModifyUserResponse:
        runtime = RuntimeOptions()
        return await self.modify_user_with_options_async(request, runtime)

    def move_org_with_options(
        self,
        request: main_models.MoveOrgRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MoveOrgResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.business_channel):
            body['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.new_parent_org_id):
            body['NewParentOrgId'] = request.new_parent_org_id
        if not DaraCore.is_null(request.org_id):
            body['OrgId'] = request.org_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'MoveOrg',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveOrgResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_org_with_options_async(
        self,
        request: main_models.MoveOrgRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MoveOrgResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.business_channel):
            body['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.new_parent_org_id):
            body['NewParentOrgId'] = request.new_parent_org_id
        if not DaraCore.is_null(request.org_id):
            body['OrgId'] = request.org_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'MoveOrg',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveOrgResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def move_org(
        self,
        request: main_models.MoveOrgRequest,
    ) -> main_models.MoveOrgResponse:
        runtime = RuntimeOptions()
        return self.move_org_with_options(request, runtime)

    async def move_org_async(
        self,
        request: main_models.MoveOrgRequest,
    ) -> main_models.MoveOrgResponse:
        runtime = RuntimeOptions()
        return await self.move_org_with_options_async(request, runtime)

    def move_user_org_with_options(
        self,
        request: main_models.MoveUserOrgRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MoveUserOrgResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.business_channel):
            body['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.end_user_ids):
            body['EndUserIds'] = request.end_user_ids
        if not DaraCore.is_null(request.org_id):
            body['OrgId'] = request.org_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'MoveUserOrg',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveUserOrgResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_user_org_with_options_async(
        self,
        request: main_models.MoveUserOrgRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MoveUserOrgResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.business_channel):
            body['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.end_user_ids):
            body['EndUserIds'] = request.end_user_ids
        if not DaraCore.is_null(request.org_id):
            body['OrgId'] = request.org_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'MoveUserOrg',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveUserOrgResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def move_user_org(
        self,
        request: main_models.MoveUserOrgRequest,
    ) -> main_models.MoveUserOrgResponse:
        runtime = RuntimeOptions()
        return self.move_user_org_with_options(request, runtime)

    async def move_user_org_async(
        self,
        request: main_models.MoveUserOrgRequest,
    ) -> main_models.MoveUserOrgResponse:
        runtime = RuntimeOptions()
        return await self.move_user_org_with_options_async(request, runtime)

    def query_sync_status_by_ali_uid_with_options(
        self,
        request: main_models.QuerySyncStatusByAliUidRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySyncStatusByAliUidResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_channel):
            query['BusinessChannel'] = request.business_channel
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySyncStatusByAliUid',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySyncStatusByAliUidResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sync_status_by_ali_uid_with_options_async(
        self,
        request: main_models.QuerySyncStatusByAliUidRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySyncStatusByAliUidResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_channel):
            query['BusinessChannel'] = request.business_channel
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySyncStatusByAliUid',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySyncStatusByAliUidResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sync_status_by_ali_uid(
        self,
        request: main_models.QuerySyncStatusByAliUidRequest,
    ) -> main_models.QuerySyncStatusByAliUidResponse:
        runtime = RuntimeOptions()
        return self.query_sync_status_by_ali_uid_with_options(request, runtime)

    async def query_sync_status_by_ali_uid_async(
        self,
        request: main_models.QuerySyncStatusByAliUidRequest,
    ) -> main_models.QuerySyncStatusByAliUidResponse:
        runtime = RuntimeOptions()
        return await self.query_sync_status_by_ali_uid_with_options_async(request, runtime)

    def remove_group_with_options(
        self,
        request: main_models.RemoveGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_channel):
            query['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.group_ids):
            query['GroupIds'] = request.group_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveGroup',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_group_with_options_async(
        self,
        request: main_models.RemoveGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_channel):
            query['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.group_ids):
            query['GroupIds'] = request.group_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveGroup',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_group(
        self,
        request: main_models.RemoveGroupRequest,
    ) -> main_models.RemoveGroupResponse:
        runtime = RuntimeOptions()
        return self.remove_group_with_options(request, runtime)

    async def remove_group_async(
        self,
        request: main_models.RemoveGroupRequest,
    ) -> main_models.RemoveGroupResponse:
        runtime = RuntimeOptions()
        return await self.remove_group_with_options_async(request, runtime)

    def remove_mfa_device_with_options(
        self,
        request: main_models.RemoveMfaDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveMfaDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ad_domain):
            query['AdDomain'] = request.ad_domain
        if not DaraCore.is_null(request.business_channel):
            query['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.serial_number):
            query['SerialNumber'] = request.serial_number
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveMfaDevice',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveMfaDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_mfa_device_with_options_async(
        self,
        request: main_models.RemoveMfaDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveMfaDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ad_domain):
            query['AdDomain'] = request.ad_domain
        if not DaraCore.is_null(request.business_channel):
            query['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.serial_number):
            query['SerialNumber'] = request.serial_number
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveMfaDevice',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveMfaDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_mfa_device(
        self,
        request: main_models.RemoveMfaDeviceRequest,
    ) -> main_models.RemoveMfaDeviceResponse:
        runtime = RuntimeOptions()
        return self.remove_mfa_device_with_options(request, runtime)

    async def remove_mfa_device_async(
        self,
        request: main_models.RemoveMfaDeviceRequest,
    ) -> main_models.RemoveMfaDeviceResponse:
        runtime = RuntimeOptions()
        return await self.remove_mfa_device_with_options_async(request, runtime)

    def remove_org_with_options(
        self,
        request: main_models.RemoveOrgRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveOrgResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.business_channel):
            body['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.org_id):
            body['OrgId'] = request.org_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RemoveOrg',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveOrgResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_org_with_options_async(
        self,
        request: main_models.RemoveOrgRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveOrgResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.business_channel):
            body['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.org_id):
            body['OrgId'] = request.org_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RemoveOrg',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveOrgResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_org(
        self,
        request: main_models.RemoveOrgRequest,
    ) -> main_models.RemoveOrgResponse:
        runtime = RuntimeOptions()
        return self.remove_org_with_options(request, runtime)

    async def remove_org_async(
        self,
        request: main_models.RemoveOrgRequest,
    ) -> main_models.RemoveOrgResponse:
        runtime = RuntimeOptions()
        return await self.remove_org_with_options_async(request, runtime)

    def remove_property_with_options(
        self,
        request: main_models.RemovePropertyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemovePropertyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_channel):
            query['BusinessChannel'] = request.business_channel
        body = {}
        if not DaraCore.is_null(request.property_id):
            body['PropertyId'] = request.property_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RemoveProperty',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemovePropertyResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_property_with_options_async(
        self,
        request: main_models.RemovePropertyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemovePropertyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_channel):
            query['BusinessChannel'] = request.business_channel
        body = {}
        if not DaraCore.is_null(request.property_id):
            body['PropertyId'] = request.property_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RemoveProperty',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemovePropertyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_property(
        self,
        request: main_models.RemovePropertyRequest,
    ) -> main_models.RemovePropertyResponse:
        runtime = RuntimeOptions()
        return self.remove_property_with_options(request, runtime)

    async def remove_property_async(
        self,
        request: main_models.RemovePropertyRequest,
    ) -> main_models.RemovePropertyResponse:
        runtime = RuntimeOptions()
        return await self.remove_property_with_options_async(request, runtime)

    def remove_users_with_options(
        self,
        request: main_models.RemoveUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveUsersResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.business_channel):
            body['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.users):
            body['Users'] = request.users
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RemoveUsers',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_users_with_options_async(
        self,
        request: main_models.RemoveUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveUsersResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.business_channel):
            body['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.users):
            body['Users'] = request.users
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RemoveUsers',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_users(
        self,
        request: main_models.RemoveUsersRequest,
    ) -> main_models.RemoveUsersResponse:
        runtime = RuntimeOptions()
        return self.remove_users_with_options(request, runtime)

    async def remove_users_async(
        self,
        request: main_models.RemoveUsersRequest,
    ) -> main_models.RemoveUsersResponse:
        runtime = RuntimeOptions()
        return await self.remove_users_with_options_async(request, runtime)

    def reset_user_password_with_options(
        self,
        request: main_models.ResetUserPasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetUserPasswordResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.business_channel):
            body['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.notify_type):
            body['NotifyType'] = request.notify_type
        if not DaraCore.is_null(request.users):
            body['Users'] = request.users
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ResetUserPassword',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetUserPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_user_password_with_options_async(
        self,
        request: main_models.ResetUserPasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetUserPasswordResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.business_channel):
            body['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.notify_type):
            body['NotifyType'] = request.notify_type
        if not DaraCore.is_null(request.users):
            body['Users'] = request.users
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ResetUserPassword',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetUserPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_user_password(
        self,
        request: main_models.ResetUserPasswordRequest,
    ) -> main_models.ResetUserPasswordResponse:
        runtime = RuntimeOptions()
        return self.reset_user_password_with_options(request, runtime)

    async def reset_user_password_async(
        self,
        request: main_models.ResetUserPasswordRequest,
    ) -> main_models.ResetUserPasswordResponse:
        runtime = RuntimeOptions()
        return await self.reset_user_password_with_options_async(request, runtime)

    def set_user_property_value_with_options(
        self,
        request: main_models.SetUserPropertyValueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetUserPropertyValueResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.business_channel):
            body['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.property_id):
            body['PropertyId'] = request.property_id
        if not DaraCore.is_null(request.property_value_id):
            body['PropertyValueId'] = request.property_value_id
        if not DaraCore.is_null(request.user_id):
            body['UserId'] = request.user_id
        if not DaraCore.is_null(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SetUserPropertyValue',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetUserPropertyValueResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_user_property_value_with_options_async(
        self,
        request: main_models.SetUserPropertyValueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetUserPropertyValueResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.business_channel):
            body['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.property_id):
            body['PropertyId'] = request.property_id
        if not DaraCore.is_null(request.property_value_id):
            body['PropertyValueId'] = request.property_value_id
        if not DaraCore.is_null(request.user_id):
            body['UserId'] = request.user_id
        if not DaraCore.is_null(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SetUserPropertyValue',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetUserPropertyValueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_user_property_value(
        self,
        request: main_models.SetUserPropertyValueRequest,
    ) -> main_models.SetUserPropertyValueResponse:
        runtime = RuntimeOptions()
        return self.set_user_property_value_with_options(request, runtime)

    async def set_user_property_value_async(
        self,
        request: main_models.SetUserPropertyValueRequest,
    ) -> main_models.SetUserPropertyValueResponse:
        runtime = RuntimeOptions()
        return await self.set_user_property_value_with_options_async(request, runtime)

    def sync_all_edu_info_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.SyncAllEduInfoResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'SyncAllEduInfo',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SyncAllEduInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def sync_all_edu_info_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.SyncAllEduInfoResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'SyncAllEduInfo',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SyncAllEduInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sync_all_edu_info(self) -> main_models.SyncAllEduInfoResponse:
        runtime = RuntimeOptions()
        return self.sync_all_edu_info_with_options(runtime)

    async def sync_all_edu_info_async(self) -> main_models.SyncAllEduInfoResponse:
        runtime = RuntimeOptions()
        return await self.sync_all_edu_info_with_options_async(runtime)

    def unlock_mfa_device_with_options(
        self,
        request: main_models.UnlockMfaDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnlockMfaDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ad_domain):
            query['AdDomain'] = request.ad_domain
        if not DaraCore.is_null(request.business_channel):
            query['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.serial_number):
            query['SerialNumber'] = request.serial_number
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnlockMfaDevice',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnlockMfaDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def unlock_mfa_device_with_options_async(
        self,
        request: main_models.UnlockMfaDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnlockMfaDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ad_domain):
            query['AdDomain'] = request.ad_domain
        if not DaraCore.is_null(request.business_channel):
            query['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.serial_number):
            query['SerialNumber'] = request.serial_number
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnlockMfaDevice',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnlockMfaDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unlock_mfa_device(
        self,
        request: main_models.UnlockMfaDeviceRequest,
    ) -> main_models.UnlockMfaDeviceResponse:
        runtime = RuntimeOptions()
        return self.unlock_mfa_device_with_options(request, runtime)

    async def unlock_mfa_device_async(
        self,
        request: main_models.UnlockMfaDeviceRequest,
    ) -> main_models.UnlockMfaDeviceResponse:
        runtime = RuntimeOptions()
        return await self.unlock_mfa_device_with_options_async(request, runtime)

    def unlock_users_with_options(
        self,
        request: main_models.UnlockUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnlockUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_lock_time):
            query['AutoLockTime'] = request.auto_lock_time
        if not DaraCore.is_null(request.business_channel):
            query['BusinessChannel'] = request.business_channel
        body = {}
        if not DaraCore.is_null(request.users):
            body['Users'] = request.users
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UnlockUsers',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnlockUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def unlock_users_with_options_async(
        self,
        request: main_models.UnlockUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnlockUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_lock_time):
            query['AutoLockTime'] = request.auto_lock_time
        if not DaraCore.is_null(request.business_channel):
            query['BusinessChannel'] = request.business_channel
        body = {}
        if not DaraCore.is_null(request.users):
            body['Users'] = request.users
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UnlockUsers',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnlockUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unlock_users(
        self,
        request: main_models.UnlockUsersRequest,
    ) -> main_models.UnlockUsersResponse:
        runtime = RuntimeOptions()
        return self.unlock_users_with_options(request, runtime)

    async def unlock_users_async(
        self,
        request: main_models.UnlockUsersRequest,
    ) -> main_models.UnlockUsersResponse:
        runtime = RuntimeOptions()
        return await self.unlock_users_with_options_async(request, runtime)

    def update_property_with_options(
        self,
        request: main_models.UpdatePropertyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePropertyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_channel):
            query['BusinessChannel'] = request.business_channel
        body = {}
        if not DaraCore.is_null(request.property_id):
            body['PropertyId'] = request.property_id
        if not DaraCore.is_null(request.property_key):
            body['PropertyKey'] = request.property_key
        if not DaraCore.is_null(request.property_values):
            body['PropertyValues'] = request.property_values
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateProperty',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePropertyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_property_with_options_async(
        self,
        request: main_models.UpdatePropertyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePropertyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_channel):
            query['BusinessChannel'] = request.business_channel
        body = {}
        if not DaraCore.is_null(request.property_id):
            body['PropertyId'] = request.property_id
        if not DaraCore.is_null(request.property_key):
            body['PropertyKey'] = request.property_key
        if not DaraCore.is_null(request.property_values):
            body['PropertyValues'] = request.property_values
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateProperty',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePropertyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_property(
        self,
        request: main_models.UpdatePropertyRequest,
    ) -> main_models.UpdatePropertyResponse:
        runtime = RuntimeOptions()
        return self.update_property_with_options(request, runtime)

    async def update_property_async(
        self,
        request: main_models.UpdatePropertyRequest,
    ) -> main_models.UpdatePropertyResponse:
        runtime = RuntimeOptions()
        return await self.update_property_with_options_async(request, runtime)

    def user_batch_join_group_with_options(
        self,
        request: main_models.UserBatchJoinGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UserBatchJoinGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.business_channel):
            body['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.end_user_ids):
            body['EndUserIds'] = request.end_user_ids
        if not DaraCore.is_null(request.group_id):
            body['GroupId'] = request.group_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UserBatchJoinGroup',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UserBatchJoinGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def user_batch_join_group_with_options_async(
        self,
        request: main_models.UserBatchJoinGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UserBatchJoinGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.business_channel):
            body['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.end_user_ids):
            body['EndUserIds'] = request.end_user_ids
        if not DaraCore.is_null(request.group_id):
            body['GroupId'] = request.group_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UserBatchJoinGroup',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UserBatchJoinGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def user_batch_join_group(
        self,
        request: main_models.UserBatchJoinGroupRequest,
    ) -> main_models.UserBatchJoinGroupResponse:
        runtime = RuntimeOptions()
        return self.user_batch_join_group_with_options(request, runtime)

    async def user_batch_join_group_async(
        self,
        request: main_models.UserBatchJoinGroupRequest,
    ) -> main_models.UserBatchJoinGroupResponse:
        runtime = RuntimeOptions()
        return await self.user_batch_join_group_with_options_async(request, runtime)

    def user_batch_quit_group_with_options(
        self,
        request: main_models.UserBatchQuitGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UserBatchQuitGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.business_channel):
            body['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.end_user_ids):
            body['EndUserIds'] = request.end_user_ids
        if not DaraCore.is_null(request.group_id):
            body['GroupId'] = request.group_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UserBatchQuitGroup',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UserBatchQuitGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def user_batch_quit_group_with_options_async(
        self,
        request: main_models.UserBatchQuitGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UserBatchQuitGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.business_channel):
            body['BusinessChannel'] = request.business_channel
        if not DaraCore.is_null(request.end_user_ids):
            body['EndUserIds'] = request.end_user_ids
        if not DaraCore.is_null(request.group_id):
            body['GroupId'] = request.group_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UserBatchQuitGroup',
            version = '2021-03-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UserBatchQuitGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def user_batch_quit_group(
        self,
        request: main_models.UserBatchQuitGroupRequest,
    ) -> main_models.UserBatchQuitGroupResponse:
        runtime = RuntimeOptions()
        return self.user_batch_quit_group_with_options(request, runtime)

    async def user_batch_quit_group_async(
        self,
        request: main_models.UserBatchQuitGroupRequest,
    ) -> main_models.UserBatchQuitGroupResponse:
        runtime = RuntimeOptions()
        return await self.user_batch_quit_group_with_options_async(request, runtime)
