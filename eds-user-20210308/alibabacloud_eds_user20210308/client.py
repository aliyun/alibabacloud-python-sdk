# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_eds_user20210308 import models as eds_user_20210308_models
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
        self._signature_algorithm = 'v2'
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def batch_set_desktop_manager_with_options(
        self,
        request: eds_user_20210308_models.BatchSetDesktopManagerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_user_20210308_models.BatchSetDesktopManagerResponse:
        """
        @summary 批量设置桌面管理员
        
        @param request: BatchSetDesktopManagerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchSetDesktopManagerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.is_desktop_manager):
            body['IsDesktopManager'] = request.is_desktop_manager
        if not UtilClient.is_unset(request.users):
            body['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchSetDesktopManager',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.BatchSetDesktopManagerResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_set_desktop_manager_with_options_async(
        self,
        request: eds_user_20210308_models.BatchSetDesktopManagerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_user_20210308_models.BatchSetDesktopManagerResponse:
        """
        @summary 批量设置桌面管理员
        
        @param request: BatchSetDesktopManagerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchSetDesktopManagerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.is_desktop_manager):
            body['IsDesktopManager'] = request.is_desktop_manager
        if not UtilClient.is_unset(request.users):
            body['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchSetDesktopManager',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.BatchSetDesktopManagerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_set_desktop_manager(
        self,
        request: eds_user_20210308_models.BatchSetDesktopManagerRequest,
    ) -> eds_user_20210308_models.BatchSetDesktopManagerResponse:
        """
        @summary 批量设置桌面管理员
        
        @param request: BatchSetDesktopManagerRequest
        @return: BatchSetDesktopManagerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_set_desktop_manager_with_options(request, runtime)

    async def batch_set_desktop_manager_async(
        self,
        request: eds_user_20210308_models.BatchSetDesktopManagerRequest,
    ) -> eds_user_20210308_models.BatchSetDesktopManagerResponse:
        """
        @summary 批量设置桌面管理员
        
        @param request: BatchSetDesktopManagerRequest
        @return: BatchSetDesktopManagerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_set_desktop_manager_with_options_async(request, runtime)

    def change_user_password_with_options(
        self,
        request: eds_user_20210308_models.ChangeUserPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_user_20210308_models.ChangeUserPasswordResponse:
        """
        @summary 管理员修改用户密码
        
        @param request: ChangeUserPasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeUserPasswordResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.new_password):
            body['NewPassword'] = request.new_password
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChangeUserPassword',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.ChangeUserPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_user_password_with_options_async(
        self,
        request: eds_user_20210308_models.ChangeUserPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_user_20210308_models.ChangeUserPasswordResponse:
        """
        @summary 管理员修改用户密码
        
        @param request: ChangeUserPasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeUserPasswordResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.new_password):
            body['NewPassword'] = request.new_password
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChangeUserPassword',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.ChangeUserPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_user_password(
        self,
        request: eds_user_20210308_models.ChangeUserPasswordRequest,
    ) -> eds_user_20210308_models.ChangeUserPasswordResponse:
        """
        @summary 管理员修改用户密码
        
        @param request: ChangeUserPasswordRequest
        @return: ChangeUserPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.change_user_password_with_options(request, runtime)

    async def change_user_password_async(
        self,
        request: eds_user_20210308_models.ChangeUserPasswordRequest,
    ) -> eds_user_20210308_models.ChangeUserPasswordResponse:
        """
        @summary 管理员修改用户密码
        
        @param request: ChangeUserPasswordRequest
        @return: ChangeUserPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.change_user_password_with_options_async(request, runtime)

    def check_used_property_with_options(
        self,
        request: eds_user_20210308_models.CheckUsedPropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_user_20210308_models.CheckUsedPropertyResponse:
        """
        @summary Queries whether a property is associated with one or more convenience users.
        
        @param request: CheckUsedPropertyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckUsedPropertyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.property_id):
            query['PropertyId'] = request.property_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckUsedProperty',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.CheckUsedPropertyResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_used_property_with_options_async(
        self,
        request: eds_user_20210308_models.CheckUsedPropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_user_20210308_models.CheckUsedPropertyResponse:
        """
        @summary Queries whether a property is associated with one or more convenience users.
        
        @param request: CheckUsedPropertyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckUsedPropertyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.property_id):
            query['PropertyId'] = request.property_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckUsedProperty',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.CheckUsedPropertyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_used_property(
        self,
        request: eds_user_20210308_models.CheckUsedPropertyRequest,
    ) -> eds_user_20210308_models.CheckUsedPropertyResponse:
        """
        @summary Queries whether a property is associated with one or more convenience users.
        
        @param request: CheckUsedPropertyRequest
        @return: CheckUsedPropertyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_used_property_with_options(request, runtime)

    async def check_used_property_async(
        self,
        request: eds_user_20210308_models.CheckUsedPropertyRequest,
    ) -> eds_user_20210308_models.CheckUsedPropertyResponse:
        """
        @summary Queries whether a property is associated with one or more convenience users.
        
        @param request: CheckUsedPropertyRequest
        @return: CheckUsedPropertyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_used_property_with_options_async(request, runtime)

    def check_used_property_value_with_options(
        self,
        request: eds_user_20210308_models.CheckUsedPropertyValueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_user_20210308_models.CheckUsedPropertyValueResponse:
        """
        @summary Checks whether a property value is associated with a user.
        
        @description Before you call the operation, you can call the [ListProperty](https://help.aliyun.com/document_detail/410890.html) operation to query the existing user properties and their IDs (PropertyId) and values (PropertyValueId).
        
        @param request: CheckUsedPropertyValueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckUsedPropertyValueResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.property_id):
            query['PropertyId'] = request.property_id
        if not UtilClient.is_unset(request.property_value_id):
            query['PropertyValueId'] = request.property_value_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckUsedPropertyValue',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.CheckUsedPropertyValueResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_used_property_value_with_options_async(
        self,
        request: eds_user_20210308_models.CheckUsedPropertyValueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_user_20210308_models.CheckUsedPropertyValueResponse:
        """
        @summary Checks whether a property value is associated with a user.
        
        @description Before you call the operation, you can call the [ListProperty](https://help.aliyun.com/document_detail/410890.html) operation to query the existing user properties and their IDs (PropertyId) and values (PropertyValueId).
        
        @param request: CheckUsedPropertyValueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckUsedPropertyValueResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.property_id):
            query['PropertyId'] = request.property_id
        if not UtilClient.is_unset(request.property_value_id):
            query['PropertyValueId'] = request.property_value_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckUsedPropertyValue',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.CheckUsedPropertyValueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_used_property_value(
        self,
        request: eds_user_20210308_models.CheckUsedPropertyValueRequest,
    ) -> eds_user_20210308_models.CheckUsedPropertyValueResponse:
        """
        @summary Checks whether a property value is associated with a user.
        
        @description Before you call the operation, you can call the [ListProperty](https://help.aliyun.com/document_detail/410890.html) operation to query the existing user properties and their IDs (PropertyId) and values (PropertyValueId).
        
        @param request: CheckUsedPropertyValueRequest
        @return: CheckUsedPropertyValueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_used_property_value_with_options(request, runtime)

    async def check_used_property_value_async(
        self,
        request: eds_user_20210308_models.CheckUsedPropertyValueRequest,
    ) -> eds_user_20210308_models.CheckUsedPropertyValueResponse:
        """
        @summary Checks whether a property value is associated with a user.
        
        @description Before you call the operation, you can call the [ListProperty](https://help.aliyun.com/document_detail/410890.html) operation to query the existing user properties and their IDs (PropertyId) and values (PropertyValueId).
        
        @param request: CheckUsedPropertyValueRequest
        @return: CheckUsedPropertyValueResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_used_property_value_with_options_async(request, runtime)

    def create_property_with_options(
        self,
        request: eds_user_20210308_models.CreatePropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_user_20210308_models.CreatePropertyResponse:
        """
        @summary Creates a user property.
        
        @param request: CreatePropertyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePropertyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.property_key):
            body['PropertyKey'] = request.property_key
        if not UtilClient.is_unset(request.property_values):
            body['PropertyValues'] = request.property_values
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProperty',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.CreatePropertyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_property_with_options_async(
        self,
        request: eds_user_20210308_models.CreatePropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_user_20210308_models.CreatePropertyResponse:
        """
        @summary Creates a user property.
        
        @param request: CreatePropertyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePropertyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.property_key):
            body['PropertyKey'] = request.property_key
        if not UtilClient.is_unset(request.property_values):
            body['PropertyValues'] = request.property_values
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProperty',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.CreatePropertyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_property(
        self,
        request: eds_user_20210308_models.CreatePropertyRequest,
    ) -> eds_user_20210308_models.CreatePropertyResponse:
        """
        @summary Creates a user property.
        
        @param request: CreatePropertyRequest
        @return: CreatePropertyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_property_with_options(request, runtime)

    async def create_property_async(
        self,
        request: eds_user_20210308_models.CreatePropertyRequest,
    ) -> eds_user_20210308_models.CreatePropertyResponse:
        """
        @summary Creates a user property.
        
        @param request: CreatePropertyRequest
        @return: CreatePropertyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_property_with_options_async(request, runtime)

    def create_users_with_options(
        self,
        request: eds_user_20210308_models.CreateUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_user_20210308_models.CreateUsersResponse:
        """
        @summary Creates a convenience user.
        
        @description Convenience users are dedicated Elastic Desktop Service (EDS) user accounts and are suitable for scenarios in which you do not need to connect to enterprise Active Directory (AD) systems. The information about a convenience user includes the username, email address, and mobile number. You must specify the username or email address.
        
        @param request: CreateUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_lock_time):
            query['AutoLockTime'] = request.auto_lock_time
        if not UtilClient.is_unset(request.is_local_admin):
            query['IsLocalAdmin'] = request.is_local_admin
        if not UtilClient.is_unset(request.password_expire_days):
            query['PasswordExpireDays'] = request.password_expire_days
        body = {}
        if not UtilClient.is_unset(request.password):
            body['Password'] = request.password
        if not UtilClient.is_unset(request.users):
            body['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateUsers',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.CreateUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_users_with_options_async(
        self,
        request: eds_user_20210308_models.CreateUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_user_20210308_models.CreateUsersResponse:
        """
        @summary Creates a convenience user.
        
        @description Convenience users are dedicated Elastic Desktop Service (EDS) user accounts and are suitable for scenarios in which you do not need to connect to enterprise Active Directory (AD) systems. The information about a convenience user includes the username, email address, and mobile number. You must specify the username or email address.
        
        @param request: CreateUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_lock_time):
            query['AutoLockTime'] = request.auto_lock_time
        if not UtilClient.is_unset(request.is_local_admin):
            query['IsLocalAdmin'] = request.is_local_admin
        if not UtilClient.is_unset(request.password_expire_days):
            query['PasswordExpireDays'] = request.password_expire_days
        body = {}
        if not UtilClient.is_unset(request.password):
            body['Password'] = request.password
        if not UtilClient.is_unset(request.users):
            body['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateUsers',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.CreateUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_users(
        self,
        request: eds_user_20210308_models.CreateUsersRequest,
    ) -> eds_user_20210308_models.CreateUsersResponse:
        """
        @summary Creates a convenience user.
        
        @description Convenience users are dedicated Elastic Desktop Service (EDS) user accounts and are suitable for scenarios in which you do not need to connect to enterprise Active Directory (AD) systems. The information about a convenience user includes the username, email address, and mobile number. You must specify the username or email address.
        
        @param request: CreateUsersRequest
        @return: CreateUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_users_with_options(request, runtime)

    async def create_users_async(
        self,
        request: eds_user_20210308_models.CreateUsersRequest,
    ) -> eds_user_20210308_models.CreateUsersResponse:
        """
        @summary Creates a convenience user.
        
        @description Convenience users are dedicated Elastic Desktop Service (EDS) user accounts and are suitable for scenarios in which you do not need to connect to enterprise Active Directory (AD) systems. The information about a convenience user includes the username, email address, and mobile number. You must specify the username or email address.
        
        @param request: CreateUsersRequest
        @return: CreateUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_users_with_options_async(request, runtime)

    def delete_user_property_value_with_options(
        self,
        request: eds_user_20210308_models.DeleteUserPropertyValueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_user_20210308_models.DeleteUserPropertyValueResponse:
        """
        @summary Dissociates a user property from a user.
        
        @description Before you call this operation, you can call the FilterUsers operation to query the users that are associated with user properties.
        
        @param request: DeleteUserPropertyValueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUserPropertyValueResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.property_id):
            body['PropertyId'] = request.property_id
        if not UtilClient.is_unset(request.property_value_id):
            body['PropertyValueId'] = request.property_value_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteUserPropertyValue',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.DeleteUserPropertyValueResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_property_value_with_options_async(
        self,
        request: eds_user_20210308_models.DeleteUserPropertyValueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_user_20210308_models.DeleteUserPropertyValueResponse:
        """
        @summary Dissociates a user property from a user.
        
        @description Before you call this operation, you can call the FilterUsers operation to query the users that are associated with user properties.
        
        @param request: DeleteUserPropertyValueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUserPropertyValueResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.property_id):
            body['PropertyId'] = request.property_id
        if not UtilClient.is_unset(request.property_value_id):
            body['PropertyValueId'] = request.property_value_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteUserPropertyValue',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.DeleteUserPropertyValueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user_property_value(
        self,
        request: eds_user_20210308_models.DeleteUserPropertyValueRequest,
    ) -> eds_user_20210308_models.DeleteUserPropertyValueResponse:
        """
        @summary Dissociates a user property from a user.
        
        @description Before you call this operation, you can call the FilterUsers operation to query the users that are associated with user properties.
        
        @param request: DeleteUserPropertyValueRequest
        @return: DeleteUserPropertyValueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_user_property_value_with_options(request, runtime)

    async def delete_user_property_value_async(
        self,
        request: eds_user_20210308_models.DeleteUserPropertyValueRequest,
    ) -> eds_user_20210308_models.DeleteUserPropertyValueResponse:
        """
        @summary Dissociates a user property from a user.
        
        @description Before you call this operation, you can call the FilterUsers operation to query the users that are associated with user properties.
        
        @param request: DeleteUserPropertyValueRequest
        @return: DeleteUserPropertyValueResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_property_value_with_options_async(request, runtime)

    def describe_mfa_devices_with_options(
        self,
        request: eds_user_20210308_models.DescribeMfaDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_user_20210308_models.DescribeMfaDevicesResponse:
        """
        @summary Queries the information about virtual multi-factor authentication (MFA) devices that are bound to convenience users.
        
        @param request: DescribeMfaDevicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMfaDevicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ad_domain):
            query['AdDomain'] = request.ad_domain
        if not UtilClient.is_unset(request.end_user_ids):
            query['EndUserIds'] = request.end_user_ids
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.serial_numbers):
            query['SerialNumbers'] = request.serial_numbers
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMfaDevices',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.DescribeMfaDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_mfa_devices_with_options_async(
        self,
        request: eds_user_20210308_models.DescribeMfaDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_user_20210308_models.DescribeMfaDevicesResponse:
        """
        @summary Queries the information about virtual multi-factor authentication (MFA) devices that are bound to convenience users.
        
        @param request: DescribeMfaDevicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMfaDevicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ad_domain):
            query['AdDomain'] = request.ad_domain
        if not UtilClient.is_unset(request.end_user_ids):
            query['EndUserIds'] = request.end_user_ids
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.serial_numbers):
            query['SerialNumbers'] = request.serial_numbers
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMfaDevices',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.DescribeMfaDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_mfa_devices(
        self,
        request: eds_user_20210308_models.DescribeMfaDevicesRequest,
    ) -> eds_user_20210308_models.DescribeMfaDevicesResponse:
        """
        @summary Queries the information about virtual multi-factor authentication (MFA) devices that are bound to convenience users.
        
        @param request: DescribeMfaDevicesRequest
        @return: DescribeMfaDevicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_mfa_devices_with_options(request, runtime)

    async def describe_mfa_devices_async(
        self,
        request: eds_user_20210308_models.DescribeMfaDevicesRequest,
    ) -> eds_user_20210308_models.DescribeMfaDevicesResponse:
        """
        @summary Queries the information about virtual multi-factor authentication (MFA) devices that are bound to convenience users.
        
        @param request: DescribeMfaDevicesRequest
        @return: DescribeMfaDevicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_mfa_devices_with_options_async(request, runtime)

    def describe_orgs_with_options(
        self,
        request: eds_user_20210308_models.DescribeOrgsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_user_20210308_models.DescribeOrgsResponse:
        """
        @summary Queries organizations.
        
        @description An organization is in a tree structure. The root organization ID is in the following format: org-aliyun-wy-org-id.
        
        @param request: DescribeOrgsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOrgsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.org_name):
            query['OrgName'] = request.org_name
        if not UtilClient.is_unset(request.parent_org_id):
            query['ParentOrgId'] = request.parent_org_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOrgs',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.DescribeOrgsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_orgs_with_options_async(
        self,
        request: eds_user_20210308_models.DescribeOrgsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_user_20210308_models.DescribeOrgsResponse:
        """
        @summary Queries organizations.
        
        @description An organization is in a tree structure. The root organization ID is in the following format: org-aliyun-wy-org-id.
        
        @param request: DescribeOrgsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeOrgsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.org_name):
            query['OrgName'] = request.org_name
        if not UtilClient.is_unset(request.parent_org_id):
            query['ParentOrgId'] = request.parent_org_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOrgs',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.DescribeOrgsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_orgs(
        self,
        request: eds_user_20210308_models.DescribeOrgsRequest,
    ) -> eds_user_20210308_models.DescribeOrgsResponse:
        """
        @summary Queries organizations.
        
        @description An organization is in a tree structure. The root organization ID is in the following format: org-aliyun-wy-org-id.
        
        @param request: DescribeOrgsRequest
        @return: DescribeOrgsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_orgs_with_options(request, runtime)

    async def describe_orgs_async(
        self,
        request: eds_user_20210308_models.DescribeOrgsRequest,
    ) -> eds_user_20210308_models.DescribeOrgsResponse:
        """
        @summary Queries organizations.
        
        @description An organization is in a tree structure. The root organization ID is in the following format: org-aliyun-wy-org-id.
        
        @param request: DescribeOrgsRequest
        @return: DescribeOrgsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_orgs_with_options_async(request, runtime)

    def describe_users_with_options(
        self,
        tmp_req: eds_user_20210308_models.DescribeUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_user_20210308_models.DescribeUsersResponse:
        """
        @summary Queries the information about convenience users. The information of a convenience user includes a username, an email address, and a description.
        
        @param tmp_req: DescribeUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUsersResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eds_user_20210308_models.DescribeUsersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter_with_assigned_resources):
            request.filter_with_assigned_resources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter_with_assigned_resources, 'FilterWithAssignedResources', 'json')
        if not UtilClient.is_unset(tmp_req.show_extras):
            request.show_extras_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.show_extras, 'ShowExtras', 'json')
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        body = {}
        if not UtilClient.is_unset(request.biz_type):
            body['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.end_user_ids):
            body['EndUserIds'] = request.end_user_ids
        if not UtilClient.is_unset(request.exclude_end_user_ids):
            body['ExcludeEndUserIds'] = request.exclude_end_user_ids
        if not UtilClient.is_unset(request.filter_with_assigned_resources_shrink):
            body['FilterWithAssignedResources'] = request.filter_with_assigned_resources_shrink
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.org_id):
            body['OrgId'] = request.org_id
        if not UtilClient.is_unset(request.show_extras_shrink):
            body['ShowExtras'] = request.show_extras_shrink
        if not UtilClient.is_unset(request.solution_id):
            body['SolutionId'] = request.solution_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeUsers',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.DescribeUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_users_with_options_async(
        self,
        tmp_req: eds_user_20210308_models.DescribeUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_user_20210308_models.DescribeUsersResponse:
        """
        @summary Queries the information about convenience users. The information of a convenience user includes a username, an email address, and a description.
        
        @param tmp_req: DescribeUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUsersResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eds_user_20210308_models.DescribeUsersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter_with_assigned_resources):
            request.filter_with_assigned_resources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter_with_assigned_resources, 'FilterWithAssignedResources', 'json')
        if not UtilClient.is_unset(tmp_req.show_extras):
            request.show_extras_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.show_extras, 'ShowExtras', 'json')
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        body = {}
        if not UtilClient.is_unset(request.biz_type):
            body['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.end_user_ids):
            body['EndUserIds'] = request.end_user_ids
        if not UtilClient.is_unset(request.exclude_end_user_ids):
            body['ExcludeEndUserIds'] = request.exclude_end_user_ids
        if not UtilClient.is_unset(request.filter_with_assigned_resources_shrink):
            body['FilterWithAssignedResources'] = request.filter_with_assigned_resources_shrink
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.org_id):
            body['OrgId'] = request.org_id
        if not UtilClient.is_unset(request.show_extras_shrink):
            body['ShowExtras'] = request.show_extras_shrink
        if not UtilClient.is_unset(request.solution_id):
            body['SolutionId'] = request.solution_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeUsers',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.DescribeUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_users(
        self,
        request: eds_user_20210308_models.DescribeUsersRequest,
    ) -> eds_user_20210308_models.DescribeUsersResponse:
        """
        @summary Queries the information about convenience users. The information of a convenience user includes a username, an email address, and a description.
        
        @param request: DescribeUsersRequest
        @return: DescribeUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_users_with_options(request, runtime)

    async def describe_users_async(
        self,
        request: eds_user_20210308_models.DescribeUsersRequest,
    ) -> eds_user_20210308_models.DescribeUsersResponse:
        """
        @summary Queries the information about convenience users. The information of a convenience user includes a username, an email address, and a description.
        
        @param request: DescribeUsersRequest
        @return: DescribeUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_users_with_options_async(request, runtime)

    def filter_users_with_options(
        self,
        tmp_req: eds_user_20210308_models.FilterUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_user_20210308_models.FilterUsersResponse:
        """
        @summary Filters convenience users by property.
        
        @param tmp_req: FilterUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FilterUsersResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eds_user_20210308_models.FilterUsersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.order_param):
            request.order_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.order_param, 'OrderParam', 'json')
        query = {}
        if not UtilClient.is_unset(request.exclude_end_user_ids):
            query['ExcludeEndUserIds'] = request.exclude_end_user_ids
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.include_desktop_count):
            query['IncludeDesktopCount'] = request.include_desktop_count
        if not UtilClient.is_unset(request.include_desktop_group_count):
            query['IncludeDesktopGroupCount'] = request.include_desktop_group_count
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_param_shrink):
            query['OrderParam'] = request.order_param_shrink
        if not UtilClient.is_unset(request.org_id):
            query['OrgId'] = request.org_id
        if not UtilClient.is_unset(request.owner_type):
            query['OwnerType'] = request.owner_type
        if not UtilClient.is_unset(request.property_filter_param):
            query['PropertyFilterParam'] = request.property_filter_param
        if not UtilClient.is_unset(request.property_key_value_filter_param):
            query['PropertyKeyValueFilterParam'] = request.property_key_value_filter_param
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FilterUsers',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.FilterUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def filter_users_with_options_async(
        self,
        tmp_req: eds_user_20210308_models.FilterUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_user_20210308_models.FilterUsersResponse:
        """
        @summary Filters convenience users by property.
        
        @param tmp_req: FilterUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FilterUsersResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eds_user_20210308_models.FilterUsersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.order_param):
            request.order_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.order_param, 'OrderParam', 'json')
        query = {}
        if not UtilClient.is_unset(request.exclude_end_user_ids):
            query['ExcludeEndUserIds'] = request.exclude_end_user_ids
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.include_desktop_count):
            query['IncludeDesktopCount'] = request.include_desktop_count
        if not UtilClient.is_unset(request.include_desktop_group_count):
            query['IncludeDesktopGroupCount'] = request.include_desktop_group_count
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_param_shrink):
            query['OrderParam'] = request.order_param_shrink
        if not UtilClient.is_unset(request.org_id):
            query['OrgId'] = request.org_id
        if not UtilClient.is_unset(request.owner_type):
            query['OwnerType'] = request.owner_type
        if not UtilClient.is_unset(request.property_filter_param):
            query['PropertyFilterParam'] = request.property_filter_param
        if not UtilClient.is_unset(request.property_key_value_filter_param):
            query['PropertyKeyValueFilterParam'] = request.property_key_value_filter_param
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FilterUsers',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.FilterUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def filter_users(
        self,
        request: eds_user_20210308_models.FilterUsersRequest,
    ) -> eds_user_20210308_models.FilterUsersResponse:
        """
        @summary Filters convenience users by property.
        
        @param request: FilterUsersRequest
        @return: FilterUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.filter_users_with_options(request, runtime)

    async def filter_users_async(
        self,
        request: eds_user_20210308_models.FilterUsersRequest,
    ) -> eds_user_20210308_models.FilterUsersResponse:
        """
        @summary Filters convenience users by property.
        
        @param request: FilterUsersRequest
        @return: FilterUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.filter_users_with_options_async(request, runtime)

    def get_manager_info_by_auth_code_with_options(
        self,
        request: eds_user_20210308_models.GetManagerInfoByAuthCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_user_20210308_models.GetManagerInfoByAuthCodeResponse:
        """
        @summary Obtains the information about the current logon administrator based on the authorization code.
        
        @param request: GetManagerInfoByAuthCodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetManagerInfoByAuthCodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_code):
            query['AuthCode'] = request.auth_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetManagerInfoByAuthCode',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.GetManagerInfoByAuthCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_manager_info_by_auth_code_with_options_async(
        self,
        request: eds_user_20210308_models.GetManagerInfoByAuthCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_user_20210308_models.GetManagerInfoByAuthCodeResponse:
        """
        @summary Obtains the information about the current logon administrator based on the authorization code.
        
        @param request: GetManagerInfoByAuthCodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetManagerInfoByAuthCodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_code):
            query['AuthCode'] = request.auth_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetManagerInfoByAuthCode',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.GetManagerInfoByAuthCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_manager_info_by_auth_code(
        self,
        request: eds_user_20210308_models.GetManagerInfoByAuthCodeRequest,
    ) -> eds_user_20210308_models.GetManagerInfoByAuthCodeResponse:
        """
        @summary Obtains the information about the current logon administrator based on the authorization code.
        
        @param request: GetManagerInfoByAuthCodeRequest
        @return: GetManagerInfoByAuthCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_manager_info_by_auth_code_with_options(request, runtime)

    async def get_manager_info_by_auth_code_async(
        self,
        request: eds_user_20210308_models.GetManagerInfoByAuthCodeRequest,
    ) -> eds_user_20210308_models.GetManagerInfoByAuthCodeResponse:
        """
        @summary Obtains the information about the current logon administrator based on the authorization code.
        
        @param request: GetManagerInfoByAuthCodeRequest
        @return: GetManagerInfoByAuthCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_manager_info_by_auth_code_with_options_async(request, runtime)

    def list_property_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> eds_user_20210308_models.ListPropertyResponse:
        """
        @summary Queries all user properties within an Alibaba Cloud account.
        
        @param request: ListPropertyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPropertyResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListProperty',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.ListPropertyResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_property_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> eds_user_20210308_models.ListPropertyResponse:
        """
        @summary Queries all user properties within an Alibaba Cloud account.
        
        @param request: ListPropertyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPropertyResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListProperty',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.ListPropertyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_property(self) -> eds_user_20210308_models.ListPropertyResponse:
        """
        @summary Queries all user properties within an Alibaba Cloud account.
        
        @return: ListPropertyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_property_with_options(runtime)

    async def list_property_async(self) -> eds_user_20210308_models.ListPropertyResponse:
        """
        @summary Queries all user properties within an Alibaba Cloud account.
        
        @return: ListPropertyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_property_with_options_async(runtime)

    def list_property_value_with_options(
        self,
        request: eds_user_20210308_models.ListPropertyValueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_user_20210308_models.ListPropertyValueResponse:
        """
        @summary Queries property values of a user property.
        
        @param request: ListPropertyValueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPropertyValueResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.property_id):
            query['PropertyId'] = request.property_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPropertyValue',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.ListPropertyValueResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_property_value_with_options_async(
        self,
        request: eds_user_20210308_models.ListPropertyValueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_user_20210308_models.ListPropertyValueResponse:
        """
        @summary Queries property values of a user property.
        
        @param request: ListPropertyValueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPropertyValueResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.property_id):
            query['PropertyId'] = request.property_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPropertyValue',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.ListPropertyValueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_property_value(
        self,
        request: eds_user_20210308_models.ListPropertyValueRequest,
    ) -> eds_user_20210308_models.ListPropertyValueResponse:
        """
        @summary Queries property values of a user property.
        
        @param request: ListPropertyValueRequest
        @return: ListPropertyValueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_property_value_with_options(request, runtime)

    async def list_property_value_async(
        self,
        request: eds_user_20210308_models.ListPropertyValueRequest,
    ) -> eds_user_20210308_models.ListPropertyValueResponse:
        """
        @summary Queries property values of a user property.
        
        @param request: ListPropertyValueRequest
        @return: ListPropertyValueResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_property_value_with_options_async(request, runtime)

    def lock_mfa_device_with_options(
        self,
        request: eds_user_20210308_models.LockMfaDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_user_20210308_models.LockMfaDeviceResponse:
        """
        @summary Locks a virtual multi-factor authentication (MFA) device that is bound to a convenience user.
        
        @description After a virtual MFA device is locked, the status of the virtual MFA device changes to LOCKED. The convenience user to which the MFA device is bound cannot log on to the cloud desktop that resides in the workspace with the MFA feature enabled because the identity of the convenience user cannot be verified based on the virtual MFA device. You can call the [UnlockMfaDevice](https://help.aliyun.com/document_detail/286534.html) operation to unlock the virtual MFA device.
        
        @param request: LockMfaDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: LockMfaDeviceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ad_domain):
            query['AdDomain'] = request.ad_domain
        if not UtilClient.is_unset(request.serial_number):
            query['SerialNumber'] = request.serial_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LockMfaDevice',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.LockMfaDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def lock_mfa_device_with_options_async(
        self,
        request: eds_user_20210308_models.LockMfaDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_user_20210308_models.LockMfaDeviceResponse:
        """
        @summary Locks a virtual multi-factor authentication (MFA) device that is bound to a convenience user.
        
        @description After a virtual MFA device is locked, the status of the virtual MFA device changes to LOCKED. The convenience user to which the MFA device is bound cannot log on to the cloud desktop that resides in the workspace with the MFA feature enabled because the identity of the convenience user cannot be verified based on the virtual MFA device. You can call the [UnlockMfaDevice](https://help.aliyun.com/document_detail/286534.html) operation to unlock the virtual MFA device.
        
        @param request: LockMfaDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: LockMfaDeviceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ad_domain):
            query['AdDomain'] = request.ad_domain
        if not UtilClient.is_unset(request.serial_number):
            query['SerialNumber'] = request.serial_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LockMfaDevice',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.LockMfaDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def lock_mfa_device(
        self,
        request: eds_user_20210308_models.LockMfaDeviceRequest,
    ) -> eds_user_20210308_models.LockMfaDeviceResponse:
        """
        @summary Locks a virtual multi-factor authentication (MFA) device that is bound to a convenience user.
        
        @description After a virtual MFA device is locked, the status of the virtual MFA device changes to LOCKED. The convenience user to which the MFA device is bound cannot log on to the cloud desktop that resides in the workspace with the MFA feature enabled because the identity of the convenience user cannot be verified based on the virtual MFA device. You can call the [UnlockMfaDevice](https://help.aliyun.com/document_detail/286534.html) operation to unlock the virtual MFA device.
        
        @param request: LockMfaDeviceRequest
        @return: LockMfaDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.lock_mfa_device_with_options(request, runtime)

    async def lock_mfa_device_async(
        self,
        request: eds_user_20210308_models.LockMfaDeviceRequest,
    ) -> eds_user_20210308_models.LockMfaDeviceResponse:
        """
        @summary Locks a virtual multi-factor authentication (MFA) device that is bound to a convenience user.
        
        @description After a virtual MFA device is locked, the status of the virtual MFA device changes to LOCKED. The convenience user to which the MFA device is bound cannot log on to the cloud desktop that resides in the workspace with the MFA feature enabled because the identity of the convenience user cannot be verified based on the virtual MFA device. You can call the [UnlockMfaDevice](https://help.aliyun.com/document_detail/286534.html) operation to unlock the virtual MFA device.
        
        @param request: LockMfaDeviceRequest
        @return: LockMfaDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.lock_mfa_device_with_options_async(request, runtime)

    def lock_users_with_options(
        self,
        request: eds_user_20210308_models.LockUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_user_20210308_models.LockUsersResponse:
        """
        @summary Locks one or more convenience users.
        
        @param request: LockUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: LockUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.logout_session):
            query['LogoutSession'] = request.logout_session
        body = {}
        if not UtilClient.is_unset(request.users):
            body['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='LockUsers',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.LockUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def lock_users_with_options_async(
        self,
        request: eds_user_20210308_models.LockUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_user_20210308_models.LockUsersResponse:
        """
        @summary Locks one or more convenience users.
        
        @param request: LockUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: LockUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.logout_session):
            query['LogoutSession'] = request.logout_session
        body = {}
        if not UtilClient.is_unset(request.users):
            body['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='LockUsers',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.LockUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def lock_users(
        self,
        request: eds_user_20210308_models.LockUsersRequest,
    ) -> eds_user_20210308_models.LockUsersResponse:
        """
        @summary Locks one or more convenience users.
        
        @param request: LockUsersRequest
        @return: LockUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.lock_users_with_options(request, runtime)

    async def lock_users_async(
        self,
        request: eds_user_20210308_models.LockUsersRequest,
    ) -> eds_user_20210308_models.LockUsersResponse:
        """
        @summary Locks one or more convenience users.
        
        @param request: LockUsersRequest
        @return: LockUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.lock_users_with_options_async(request, runtime)

    def modify_user_with_options(
        self,
        request: eds_user_20210308_models.ModifyUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_user_20210308_models.ModifyUserResponse:
        """
        @summary Modifies user information.
        
        @param request: ModifyUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.phone):
            query['Phone'] = request.phone
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyUser',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.ModifyUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_user_with_options_async(
        self,
        request: eds_user_20210308_models.ModifyUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_user_20210308_models.ModifyUserResponse:
        """
        @summary Modifies user information.
        
        @param request: ModifyUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.phone):
            query['Phone'] = request.phone
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyUser',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.ModifyUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_user(
        self,
        request: eds_user_20210308_models.ModifyUserRequest,
    ) -> eds_user_20210308_models.ModifyUserResponse:
        """
        @summary Modifies user information.
        
        @param request: ModifyUserRequest
        @return: ModifyUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_user_with_options(request, runtime)

    async def modify_user_async(
        self,
        request: eds_user_20210308_models.ModifyUserRequest,
    ) -> eds_user_20210308_models.ModifyUserResponse:
        """
        @summary Modifies user information.
        
        @param request: ModifyUserRequest
        @return: ModifyUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_user_with_options_async(request, runtime)

    def query_sync_status_by_ali_uid_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> eds_user_20210308_models.QuerySyncStatusByAliUidResponse:
        """
        @summary 查询edu同步信息
        
        @param request: QuerySyncStatusByAliUidRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySyncStatusByAliUidResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='QuerySyncStatusByAliUid',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.QuerySyncStatusByAliUidResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sync_status_by_ali_uid_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> eds_user_20210308_models.QuerySyncStatusByAliUidResponse:
        """
        @summary 查询edu同步信息
        
        @param request: QuerySyncStatusByAliUidRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySyncStatusByAliUidResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='QuerySyncStatusByAliUid',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.QuerySyncStatusByAliUidResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sync_status_by_ali_uid(self) -> eds_user_20210308_models.QuerySyncStatusByAliUidResponse:
        """
        @summary 查询edu同步信息
        
        @return: QuerySyncStatusByAliUidResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_sync_status_by_ali_uid_with_options(runtime)

    async def query_sync_status_by_ali_uid_async(self) -> eds_user_20210308_models.QuerySyncStatusByAliUidResponse:
        """
        @summary 查询edu同步信息
        
        @return: QuerySyncStatusByAliUidResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_sync_status_by_ali_uid_with_options_async(runtime)

    def remove_mfa_device_with_options(
        self,
        request: eds_user_20210308_models.RemoveMfaDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_user_20210308_models.RemoveMfaDeviceResponse:
        """
        @summary Removes a virtual multi-factor authentication (MFA) device that is bound to a convenience user.
        
        @description If you remove a virtual MFA device that is bound to a convenience user, the convenience user can no longer use the virtual MFA device to log on to cloud desktops. Before the convenience user can log on to cloud desktops again, a new virtual MFA device must be bound to the convenience user.
        
        @param request: RemoveMfaDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveMfaDeviceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ad_domain):
            query['AdDomain'] = request.ad_domain
        if not UtilClient.is_unset(request.serial_number):
            query['SerialNumber'] = request.serial_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveMfaDevice',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.RemoveMfaDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_mfa_device_with_options_async(
        self,
        request: eds_user_20210308_models.RemoveMfaDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_user_20210308_models.RemoveMfaDeviceResponse:
        """
        @summary Removes a virtual multi-factor authentication (MFA) device that is bound to a convenience user.
        
        @description If you remove a virtual MFA device that is bound to a convenience user, the convenience user can no longer use the virtual MFA device to log on to cloud desktops. Before the convenience user can log on to cloud desktops again, a new virtual MFA device must be bound to the convenience user.
        
        @param request: RemoveMfaDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveMfaDeviceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ad_domain):
            query['AdDomain'] = request.ad_domain
        if not UtilClient.is_unset(request.serial_number):
            query['SerialNumber'] = request.serial_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveMfaDevice',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.RemoveMfaDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_mfa_device(
        self,
        request: eds_user_20210308_models.RemoveMfaDeviceRequest,
    ) -> eds_user_20210308_models.RemoveMfaDeviceResponse:
        """
        @summary Removes a virtual multi-factor authentication (MFA) device that is bound to a convenience user.
        
        @description If you remove a virtual MFA device that is bound to a convenience user, the convenience user can no longer use the virtual MFA device to log on to cloud desktops. Before the convenience user can log on to cloud desktops again, a new virtual MFA device must be bound to the convenience user.
        
        @param request: RemoveMfaDeviceRequest
        @return: RemoveMfaDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_mfa_device_with_options(request, runtime)

    async def remove_mfa_device_async(
        self,
        request: eds_user_20210308_models.RemoveMfaDeviceRequest,
    ) -> eds_user_20210308_models.RemoveMfaDeviceResponse:
        """
        @summary Removes a virtual multi-factor authentication (MFA) device that is bound to a convenience user.
        
        @description If you remove a virtual MFA device that is bound to a convenience user, the convenience user can no longer use the virtual MFA device to log on to cloud desktops. Before the convenience user can log on to cloud desktops again, a new virtual MFA device must be bound to the convenience user.
        
        @param request: RemoveMfaDeviceRequest
        @return: RemoveMfaDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_mfa_device_with_options_async(request, runtime)

    def remove_property_with_options(
        self,
        request: eds_user_20210308_models.RemovePropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_user_20210308_models.RemovePropertyResponse:
        """
        @summary Deletes a user property.
        
        @param request: RemovePropertyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemovePropertyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.property_id):
            body['PropertyId'] = request.property_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveProperty',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.RemovePropertyResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_property_with_options_async(
        self,
        request: eds_user_20210308_models.RemovePropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_user_20210308_models.RemovePropertyResponse:
        """
        @summary Deletes a user property.
        
        @param request: RemovePropertyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemovePropertyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.property_id):
            body['PropertyId'] = request.property_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveProperty',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.RemovePropertyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_property(
        self,
        request: eds_user_20210308_models.RemovePropertyRequest,
    ) -> eds_user_20210308_models.RemovePropertyResponse:
        """
        @summary Deletes a user property.
        
        @param request: RemovePropertyRequest
        @return: RemovePropertyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_property_with_options(request, runtime)

    async def remove_property_async(
        self,
        request: eds_user_20210308_models.RemovePropertyRequest,
    ) -> eds_user_20210308_models.RemovePropertyResponse:
        """
        @summary Deletes a user property.
        
        @param request: RemovePropertyRequest
        @return: RemovePropertyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_property_with_options_async(request, runtime)

    def remove_users_with_options(
        self,
        request: eds_user_20210308_models.RemoveUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_user_20210308_models.RemoveUsersResponse:
        """
        @summary Removes one or more convenience users.
        
        @param request: RemoveUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveUsersResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.users):
            body['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveUsers',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.RemoveUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_users_with_options_async(
        self,
        request: eds_user_20210308_models.RemoveUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_user_20210308_models.RemoveUsersResponse:
        """
        @summary Removes one or more convenience users.
        
        @param request: RemoveUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveUsersResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.users):
            body['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveUsers',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.RemoveUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_users(
        self,
        request: eds_user_20210308_models.RemoveUsersRequest,
    ) -> eds_user_20210308_models.RemoveUsersResponse:
        """
        @summary Removes one or more convenience users.
        
        @param request: RemoveUsersRequest
        @return: RemoveUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_users_with_options(request, runtime)

    async def remove_users_async(
        self,
        request: eds_user_20210308_models.RemoveUsersRequest,
    ) -> eds_user_20210308_models.RemoveUsersResponse:
        """
        @summary Removes one or more convenience users.
        
        @param request: RemoveUsersRequest
        @return: RemoveUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_users_with_options_async(request, runtime)

    def reset_user_password_with_options(
        self,
        request: eds_user_20210308_models.ResetUserPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_user_20210308_models.ResetUserPasswordResponse:
        """
        @summary Resets the password for a convenience user. If you call this operation, a token that is used to reset the password is generated, and the system sends a password reset email that includes the token to the email address of the convenience user.
        
        @param request: ResetUserPasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetUserPasswordResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.notify_type):
            body['NotifyType'] = request.notify_type
        if not UtilClient.is_unset(request.users):
            body['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResetUserPassword',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.ResetUserPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_user_password_with_options_async(
        self,
        request: eds_user_20210308_models.ResetUserPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_user_20210308_models.ResetUserPasswordResponse:
        """
        @summary Resets the password for a convenience user. If you call this operation, a token that is used to reset the password is generated, and the system sends a password reset email that includes the token to the email address of the convenience user.
        
        @param request: ResetUserPasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetUserPasswordResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.notify_type):
            body['NotifyType'] = request.notify_type
        if not UtilClient.is_unset(request.users):
            body['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResetUserPassword',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.ResetUserPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_user_password(
        self,
        request: eds_user_20210308_models.ResetUserPasswordRequest,
    ) -> eds_user_20210308_models.ResetUserPasswordResponse:
        """
        @summary Resets the password for a convenience user. If you call this operation, a token that is used to reset the password is generated, and the system sends a password reset email that includes the token to the email address of the convenience user.
        
        @param request: ResetUserPasswordRequest
        @return: ResetUserPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reset_user_password_with_options(request, runtime)

    async def reset_user_password_async(
        self,
        request: eds_user_20210308_models.ResetUserPasswordRequest,
    ) -> eds_user_20210308_models.ResetUserPasswordResponse:
        """
        @summary Resets the password for a convenience user. If you call this operation, a token that is used to reset the password is generated, and the system sends a password reset email that includes the token to the email address of the convenience user.
        
        @param request: ResetUserPasswordRequest
        @return: ResetUserPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reset_user_password_with_options_async(request, runtime)

    def set_user_property_value_with_options(
        self,
        request: eds_user_20210308_models.SetUserPropertyValueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_user_20210308_models.SetUserPropertyValueResponse:
        """
        @summary Associates a user property with a convenience user.
        
        @param request: SetUserPropertyValueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetUserPropertyValueResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.property_id):
            body['PropertyId'] = request.property_id
        if not UtilClient.is_unset(request.property_value_id):
            body['PropertyValueId'] = request.property_value_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetUserPropertyValue',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.SetUserPropertyValueResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_user_property_value_with_options_async(
        self,
        request: eds_user_20210308_models.SetUserPropertyValueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_user_20210308_models.SetUserPropertyValueResponse:
        """
        @summary Associates a user property with a convenience user.
        
        @param request: SetUserPropertyValueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetUserPropertyValueResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.property_id):
            body['PropertyId'] = request.property_id
        if not UtilClient.is_unset(request.property_value_id):
            body['PropertyValueId'] = request.property_value_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetUserPropertyValue',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.SetUserPropertyValueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_user_property_value(
        self,
        request: eds_user_20210308_models.SetUserPropertyValueRequest,
    ) -> eds_user_20210308_models.SetUserPropertyValueResponse:
        """
        @summary Associates a user property with a convenience user.
        
        @param request: SetUserPropertyValueRequest
        @return: SetUserPropertyValueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_user_property_value_with_options(request, runtime)

    async def set_user_property_value_async(
        self,
        request: eds_user_20210308_models.SetUserPropertyValueRequest,
    ) -> eds_user_20210308_models.SetUserPropertyValueResponse:
        """
        @summary Associates a user property with a convenience user.
        
        @param request: SetUserPropertyValueRequest
        @return: SetUserPropertyValueResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_user_property_value_with_options_async(request, runtime)

    def sync_all_edu_info_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> eds_user_20210308_models.SyncAllEduInfoResponse:
        """
        @summary 从钉钉手动同步老师学生信息
        
        @param request: SyncAllEduInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SyncAllEduInfoResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='SyncAllEduInfo',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.SyncAllEduInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def sync_all_edu_info_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> eds_user_20210308_models.SyncAllEduInfoResponse:
        """
        @summary 从钉钉手动同步老师学生信息
        
        @param request: SyncAllEduInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SyncAllEduInfoResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='SyncAllEduInfo',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.SyncAllEduInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sync_all_edu_info(self) -> eds_user_20210308_models.SyncAllEduInfoResponse:
        """
        @summary 从钉钉手动同步老师学生信息
        
        @return: SyncAllEduInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.sync_all_edu_info_with_options(runtime)

    async def sync_all_edu_info_async(self) -> eds_user_20210308_models.SyncAllEduInfoResponse:
        """
        @summary 从钉钉手动同步老师学生信息
        
        @return: SyncAllEduInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.sync_all_edu_info_with_options_async(runtime)

    def unlock_mfa_device_with_options(
        self,
        request: eds_user_20210308_models.UnlockMfaDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_user_20210308_models.UnlockMfaDeviceResponse:
        """
        @summary Unlocks a virtual multi-factor authentication (MFA) device that is bound to a convenience user.
        
        @param request: UnlockMfaDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnlockMfaDeviceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ad_domain):
            query['AdDomain'] = request.ad_domain
        if not UtilClient.is_unset(request.serial_number):
            query['SerialNumber'] = request.serial_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnlockMfaDevice',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.UnlockMfaDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def unlock_mfa_device_with_options_async(
        self,
        request: eds_user_20210308_models.UnlockMfaDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_user_20210308_models.UnlockMfaDeviceResponse:
        """
        @summary Unlocks a virtual multi-factor authentication (MFA) device that is bound to a convenience user.
        
        @param request: UnlockMfaDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnlockMfaDeviceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ad_domain):
            query['AdDomain'] = request.ad_domain
        if not UtilClient.is_unset(request.serial_number):
            query['SerialNumber'] = request.serial_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnlockMfaDevice',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.UnlockMfaDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unlock_mfa_device(
        self,
        request: eds_user_20210308_models.UnlockMfaDeviceRequest,
    ) -> eds_user_20210308_models.UnlockMfaDeviceResponse:
        """
        @summary Unlocks a virtual multi-factor authentication (MFA) device that is bound to a convenience user.
        
        @param request: UnlockMfaDeviceRequest
        @return: UnlockMfaDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.unlock_mfa_device_with_options(request, runtime)

    async def unlock_mfa_device_async(
        self,
        request: eds_user_20210308_models.UnlockMfaDeviceRequest,
    ) -> eds_user_20210308_models.UnlockMfaDeviceResponse:
        """
        @summary Unlocks a virtual multi-factor authentication (MFA) device that is bound to a convenience user.
        
        @param request: UnlockMfaDeviceRequest
        @return: UnlockMfaDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.unlock_mfa_device_with_options_async(request, runtime)

    def unlock_users_with_options(
        self,
        request: eds_user_20210308_models.UnlockUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_user_20210308_models.UnlockUsersResponse:
        """
        @summary Unlocks one or more convenience users.
        
        @param request: UnlockUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnlockUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_lock_time):
            query['AutoLockTime'] = request.auto_lock_time
        body = {}
        if not UtilClient.is_unset(request.users):
            body['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UnlockUsers',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.UnlockUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def unlock_users_with_options_async(
        self,
        request: eds_user_20210308_models.UnlockUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_user_20210308_models.UnlockUsersResponse:
        """
        @summary Unlocks one or more convenience users.
        
        @param request: UnlockUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnlockUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_lock_time):
            query['AutoLockTime'] = request.auto_lock_time
        body = {}
        if not UtilClient.is_unset(request.users):
            body['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UnlockUsers',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.UnlockUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unlock_users(
        self,
        request: eds_user_20210308_models.UnlockUsersRequest,
    ) -> eds_user_20210308_models.UnlockUsersResponse:
        """
        @summary Unlocks one or more convenience users.
        
        @param request: UnlockUsersRequest
        @return: UnlockUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.unlock_users_with_options(request, runtime)

    async def unlock_users_async(
        self,
        request: eds_user_20210308_models.UnlockUsersRequest,
    ) -> eds_user_20210308_models.UnlockUsersResponse:
        """
        @summary Unlocks one or more convenience users.
        
        @param request: UnlockUsersRequest
        @return: UnlockUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.unlock_users_with_options_async(request, runtime)

    def update_property_with_options(
        self,
        request: eds_user_20210308_models.UpdatePropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_user_20210308_models.UpdatePropertyResponse:
        """
        @summary Modifies a user property.
        
        @param request: UpdatePropertyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePropertyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.property_id):
            body['PropertyId'] = request.property_id
        if not UtilClient.is_unset(request.property_key):
            body['PropertyKey'] = request.property_key
        if not UtilClient.is_unset(request.property_values):
            body['PropertyValues'] = request.property_values
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProperty',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.UpdatePropertyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_property_with_options_async(
        self,
        request: eds_user_20210308_models.UpdatePropertyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eds_user_20210308_models.UpdatePropertyResponse:
        """
        @summary Modifies a user property.
        
        @param request: UpdatePropertyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePropertyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.property_id):
            body['PropertyId'] = request.property_id
        if not UtilClient.is_unset(request.property_key):
            body['PropertyKey'] = request.property_key
        if not UtilClient.is_unset(request.property_values):
            body['PropertyValues'] = request.property_values
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProperty',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.UpdatePropertyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_property(
        self,
        request: eds_user_20210308_models.UpdatePropertyRequest,
    ) -> eds_user_20210308_models.UpdatePropertyResponse:
        """
        @summary Modifies a user property.
        
        @param request: UpdatePropertyRequest
        @return: UpdatePropertyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_property_with_options(request, runtime)

    async def update_property_async(
        self,
        request: eds_user_20210308_models.UpdatePropertyRequest,
    ) -> eds_user_20210308_models.UpdatePropertyResponse:
        """
        @summary Modifies a user property.
        
        @param request: UpdatePropertyRequest
        @return: UpdatePropertyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_property_with_options_async(request, runtime)
