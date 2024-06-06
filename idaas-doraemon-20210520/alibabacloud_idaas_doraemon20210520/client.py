# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_idaas_doraemon20210520 import models as idaas_doraemon_20210520_models
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
        self._endpoint_rule = 'central'
        self._endpoint_map = {
            'cn-hangzhou': 'idaas-doraemon.cn-hangzhou.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('idaas-doraemon', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_authenticator_registration_with_options(
        self,
        request: idaas_doraemon_20210520_models.CreateAuthenticatorRegistrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.CreateAuthenticatorRegistrationResponse:
        """
        @summary 创建认证器请求
        
        @param request: CreateAuthenticatorRegistrationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAuthenticatorRegistrationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_external_id):
            query['ApplicationExternalId'] = request.application_external_id
        if not UtilClient.is_unset(request.authenticator_type):
            query['AuthenticatorType'] = request.authenticator_type
        if not UtilClient.is_unset(request.client_extend_params_json):
            query['ClientExtendParamsJson'] = request.client_extend_params_json
        if not UtilClient.is_unset(request.client_extend_params_json_sign):
            query['ClientExtendParamsJsonSign'] = request.client_extend_params_json_sign
        if not UtilClient.is_unset(request.registration_context):
            query['RegistrationContext'] = request.registration_context
        if not UtilClient.is_unset(request.server_extend_params_json):
            query['ServerExtendParamsJson'] = request.server_extend_params_json
        if not UtilClient.is_unset(request.user_display_name):
            query['UserDisplayName'] = request.user_display_name
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAuthenticatorRegistration',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.CreateAuthenticatorRegistrationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_authenticator_registration_with_options_async(
        self,
        request: idaas_doraemon_20210520_models.CreateAuthenticatorRegistrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.CreateAuthenticatorRegistrationResponse:
        """
        @summary 创建认证器请求
        
        @param request: CreateAuthenticatorRegistrationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAuthenticatorRegistrationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_external_id):
            query['ApplicationExternalId'] = request.application_external_id
        if not UtilClient.is_unset(request.authenticator_type):
            query['AuthenticatorType'] = request.authenticator_type
        if not UtilClient.is_unset(request.client_extend_params_json):
            query['ClientExtendParamsJson'] = request.client_extend_params_json
        if not UtilClient.is_unset(request.client_extend_params_json_sign):
            query['ClientExtendParamsJsonSign'] = request.client_extend_params_json_sign
        if not UtilClient.is_unset(request.registration_context):
            query['RegistrationContext'] = request.registration_context
        if not UtilClient.is_unset(request.server_extend_params_json):
            query['ServerExtendParamsJson'] = request.server_extend_params_json
        if not UtilClient.is_unset(request.user_display_name):
            query['UserDisplayName'] = request.user_display_name
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAuthenticatorRegistration',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.CreateAuthenticatorRegistrationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_authenticator_registration(
        self,
        request: idaas_doraemon_20210520_models.CreateAuthenticatorRegistrationRequest,
    ) -> idaas_doraemon_20210520_models.CreateAuthenticatorRegistrationResponse:
        """
        @summary 创建认证器请求
        
        @param request: CreateAuthenticatorRegistrationRequest
        @return: CreateAuthenticatorRegistrationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_authenticator_registration_with_options(request, runtime)

    async def create_authenticator_registration_async(
        self,
        request: idaas_doraemon_20210520_models.CreateAuthenticatorRegistrationRequest,
    ) -> idaas_doraemon_20210520_models.CreateAuthenticatorRegistrationResponse:
        """
        @summary 创建认证器请求
        
        @param request: CreateAuthenticatorRegistrationRequest
        @return: CreateAuthenticatorRegistrationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_authenticator_registration_with_options_async(request, runtime)

    def create_user_authenticate_options_with_options(
        self,
        request: idaas_doraemon_20210520_models.CreateUserAuthenticateOptionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.CreateUserAuthenticateOptionsResponse:
        """
        @summary 创建用户认证请求
        
        @param request: CreateUserAuthenticateOptionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateUserAuthenticateOptionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_external_id):
            query['ApplicationExternalId'] = request.application_external_id
        if not UtilClient.is_unset(request.authenticator_type):
            query['AuthenticatorType'] = request.authenticator_type
        if not UtilClient.is_unset(request.bind_hash_base_64):
            query['BindHashBase64'] = request.bind_hash_base_64
        if not UtilClient.is_unset(request.client_extend_params_json):
            query['ClientExtendParamsJson'] = request.client_extend_params_json
        if not UtilClient.is_unset(request.client_extend_params_json_sign):
            query['ClientExtendParamsJsonSign'] = request.client_extend_params_json_sign
        if not UtilClient.is_unset(request.server_extend_params_json):
            query['ServerExtendParamsJson'] = request.server_extend_params_json
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUserAuthenticateOptions',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.CreateUserAuthenticateOptionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_user_authenticate_options_with_options_async(
        self,
        request: idaas_doraemon_20210520_models.CreateUserAuthenticateOptionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.CreateUserAuthenticateOptionsResponse:
        """
        @summary 创建用户认证请求
        
        @param request: CreateUserAuthenticateOptionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateUserAuthenticateOptionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_external_id):
            query['ApplicationExternalId'] = request.application_external_id
        if not UtilClient.is_unset(request.authenticator_type):
            query['AuthenticatorType'] = request.authenticator_type
        if not UtilClient.is_unset(request.bind_hash_base_64):
            query['BindHashBase64'] = request.bind_hash_base_64
        if not UtilClient.is_unset(request.client_extend_params_json):
            query['ClientExtendParamsJson'] = request.client_extend_params_json
        if not UtilClient.is_unset(request.client_extend_params_json_sign):
            query['ClientExtendParamsJsonSign'] = request.client_extend_params_json_sign
        if not UtilClient.is_unset(request.server_extend_params_json):
            query['ServerExtendParamsJson'] = request.server_extend_params_json
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUserAuthenticateOptions',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.CreateUserAuthenticateOptionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_user_authenticate_options(
        self,
        request: idaas_doraemon_20210520_models.CreateUserAuthenticateOptionsRequest,
    ) -> idaas_doraemon_20210520_models.CreateUserAuthenticateOptionsResponse:
        """
        @summary 创建用户认证请求
        
        @param request: CreateUserAuthenticateOptionsRequest
        @return: CreateUserAuthenticateOptionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_user_authenticate_options_with_options(request, runtime)

    async def create_user_authenticate_options_async(
        self,
        request: idaas_doraemon_20210520_models.CreateUserAuthenticateOptionsRequest,
    ) -> idaas_doraemon_20210520_models.CreateUserAuthenticateOptionsResponse:
        """
        @summary 创建用户认证请求
        
        @param request: CreateUserAuthenticateOptionsRequest
        @return: CreateUserAuthenticateOptionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_user_authenticate_options_with_options_async(request, runtime)

    def deregister_authenticator_with_options(
        self,
        request: idaas_doraemon_20210520_models.DeregisterAuthenticatorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.DeregisterAuthenticatorResponse:
        """
        @summary 删除认证器
        
        @param request: DeregisterAuthenticatorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeregisterAuthenticatorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_external_id):
            query['ApplicationExternalId'] = request.application_external_id
        if not UtilClient.is_unset(request.authenticator_uuid):
            query['AuthenticatorUuid'] = request.authenticator_uuid
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeregisterAuthenticator',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.DeregisterAuthenticatorResponse(),
            self.call_api(params, req, runtime)
        )

    async def deregister_authenticator_with_options_async(
        self,
        request: idaas_doraemon_20210520_models.DeregisterAuthenticatorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.DeregisterAuthenticatorResponse:
        """
        @summary 删除认证器
        
        @param request: DeregisterAuthenticatorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeregisterAuthenticatorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_external_id):
            query['ApplicationExternalId'] = request.application_external_id
        if not UtilClient.is_unset(request.authenticator_uuid):
            query['AuthenticatorUuid'] = request.authenticator_uuid
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeregisterAuthenticator',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.DeregisterAuthenticatorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deregister_authenticator(
        self,
        request: idaas_doraemon_20210520_models.DeregisterAuthenticatorRequest,
    ) -> idaas_doraemon_20210520_models.DeregisterAuthenticatorResponse:
        """
        @summary 删除认证器
        
        @param request: DeregisterAuthenticatorRequest
        @return: DeregisterAuthenticatorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.deregister_authenticator_with_options(request, runtime)

    async def deregister_authenticator_async(
        self,
        request: idaas_doraemon_20210520_models.DeregisterAuthenticatorRequest,
    ) -> idaas_doraemon_20210520_models.DeregisterAuthenticatorResponse:
        """
        @summary 删除认证器
        
        @param request: DeregisterAuthenticatorRequest
        @return: DeregisterAuthenticatorResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.deregister_authenticator_with_options_async(request, runtime)

    def fetch_access_token_with_options(
        self,
        request: idaas_doraemon_20210520_models.FetchAccessTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.FetchAccessTokenResponse:
        """
        @summary 获取access_token
        
        @param request: FetchAccessTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FetchAccessTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_external_id):
            query['ApplicationExternalId'] = request.application_external_id
        if not UtilClient.is_unset(request.mobile_extend_params_json):
            query['MobileExtendParamsJson'] = request.mobile_extend_params_json
        if not UtilClient.is_unset(request.mobile_extend_params_json_sign):
            query['MobileExtendParamsJsonSign'] = request.mobile_extend_params_json_sign
        if not UtilClient.is_unset(request.server_extend_params_json):
            query['ServerExtendParamsJson'] = request.server_extend_params_json
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.xclient_ip):
            query['XClientIp'] = request.xclient_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FetchAccessToken',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.FetchAccessTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def fetch_access_token_with_options_async(
        self,
        request: idaas_doraemon_20210520_models.FetchAccessTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.FetchAccessTokenResponse:
        """
        @summary 获取access_token
        
        @param request: FetchAccessTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FetchAccessTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_external_id):
            query['ApplicationExternalId'] = request.application_external_id
        if not UtilClient.is_unset(request.mobile_extend_params_json):
            query['MobileExtendParamsJson'] = request.mobile_extend_params_json
        if not UtilClient.is_unset(request.mobile_extend_params_json_sign):
            query['MobileExtendParamsJsonSign'] = request.mobile_extend_params_json_sign
        if not UtilClient.is_unset(request.server_extend_params_json):
            query['ServerExtendParamsJson'] = request.server_extend_params_json
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.xclient_ip):
            query['XClientIp'] = request.xclient_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FetchAccessToken',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.FetchAccessTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def fetch_access_token(
        self,
        request: idaas_doraemon_20210520_models.FetchAccessTokenRequest,
    ) -> idaas_doraemon_20210520_models.FetchAccessTokenResponse:
        """
        @summary 获取access_token
        
        @param request: FetchAccessTokenRequest
        @return: FetchAccessTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.fetch_access_token_with_options(request, runtime)

    async def fetch_access_token_async(
        self,
        request: idaas_doraemon_20210520_models.FetchAccessTokenRequest,
    ) -> idaas_doraemon_20210520_models.FetchAccessTokenResponse:
        """
        @summary 获取access_token
        
        @param request: FetchAccessTokenRequest
        @return: FetchAccessTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.fetch_access_token_with_options_async(request, runtime)

    def get_authenticator_with_options(
        self,
        request: idaas_doraemon_20210520_models.GetAuthenticatorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.GetAuthenticatorResponse:
        """
        @summary 查询单个认证器
        
        @param request: GetAuthenticatorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAuthenticatorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_external_id):
            query['ApplicationExternalId'] = request.application_external_id
        if not UtilClient.is_unset(request.authenticator_uuid):
            query['AuthenticatorUuid'] = request.authenticator_uuid
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAuthenticator',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.GetAuthenticatorResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_authenticator_with_options_async(
        self,
        request: idaas_doraemon_20210520_models.GetAuthenticatorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.GetAuthenticatorResponse:
        """
        @summary 查询单个认证器
        
        @param request: GetAuthenticatorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAuthenticatorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_external_id):
            query['ApplicationExternalId'] = request.application_external_id
        if not UtilClient.is_unset(request.authenticator_uuid):
            query['AuthenticatorUuid'] = request.authenticator_uuid
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAuthenticator',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.GetAuthenticatorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_authenticator(
        self,
        request: idaas_doraemon_20210520_models.GetAuthenticatorRequest,
    ) -> idaas_doraemon_20210520_models.GetAuthenticatorResponse:
        """
        @summary 查询单个认证器
        
        @param request: GetAuthenticatorRequest
        @return: GetAuthenticatorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_authenticator_with_options(request, runtime)

    async def get_authenticator_async(
        self,
        request: idaas_doraemon_20210520_models.GetAuthenticatorRequest,
    ) -> idaas_doraemon_20210520_models.GetAuthenticatorResponse:
        """
        @summary 查询单个认证器
        
        @param request: GetAuthenticatorRequest
        @return: GetAuthenticatorResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_authenticator_with_options_async(request, runtime)

    def list_authentication_logs_with_options(
        self,
        request: idaas_doraemon_20210520_models.ListAuthenticationLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.ListAuthenticationLogsResponse:
        """
        @summary 列表查询认证事件日志
        
        @param request: ListAuthenticationLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAuthenticationLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_external_id):
            query['ApplicationExternalId'] = request.application_external_id
        if not UtilClient.is_unset(request.authenticator_type):
            query['AuthenticatorType'] = request.authenticator_type
        if not UtilClient.is_unset(request.authenticator_uuid):
            query['AuthenticatorUuid'] = request.authenticator_uuid
        if not UtilClient.is_unset(request.credential_id):
            query['CredentialId'] = request.credential_id
        if not UtilClient.is_unset(request.from_time):
            query['FromTime'] = request.from_time
        if not UtilClient.is_unset(request.log_tag):
            query['LogTag'] = request.log_tag
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.to_time):
            query['ToTime'] = request.to_time
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAuthenticationLogs',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.ListAuthenticationLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_authentication_logs_with_options_async(
        self,
        request: idaas_doraemon_20210520_models.ListAuthenticationLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.ListAuthenticationLogsResponse:
        """
        @summary 列表查询认证事件日志
        
        @param request: ListAuthenticationLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAuthenticationLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_external_id):
            query['ApplicationExternalId'] = request.application_external_id
        if not UtilClient.is_unset(request.authenticator_type):
            query['AuthenticatorType'] = request.authenticator_type
        if not UtilClient.is_unset(request.authenticator_uuid):
            query['AuthenticatorUuid'] = request.authenticator_uuid
        if not UtilClient.is_unset(request.credential_id):
            query['CredentialId'] = request.credential_id
        if not UtilClient.is_unset(request.from_time):
            query['FromTime'] = request.from_time
        if not UtilClient.is_unset(request.log_tag):
            query['LogTag'] = request.log_tag
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.to_time):
            query['ToTime'] = request.to_time
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAuthenticationLogs',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.ListAuthenticationLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_authentication_logs(
        self,
        request: idaas_doraemon_20210520_models.ListAuthenticationLogsRequest,
    ) -> idaas_doraemon_20210520_models.ListAuthenticationLogsResponse:
        """
        @summary 列表查询认证事件日志
        
        @param request: ListAuthenticationLogsRequest
        @return: ListAuthenticationLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_authentication_logs_with_options(request, runtime)

    async def list_authentication_logs_async(
        self,
        request: idaas_doraemon_20210520_models.ListAuthenticationLogsRequest,
    ) -> idaas_doraemon_20210520_models.ListAuthenticationLogsResponse:
        """
        @summary 列表查询认证事件日志
        
        @param request: ListAuthenticationLogsRequest
        @return: ListAuthenticationLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_authentication_logs_with_options_async(request, runtime)

    def list_authenticator_ops_logs_with_options(
        self,
        request: idaas_doraemon_20210520_models.ListAuthenticatorOpsLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.ListAuthenticatorOpsLogsResponse:
        """
        @summary 列表查询认证器操作日志
        
        @param request: ListAuthenticatorOpsLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAuthenticatorOpsLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_external_id):
            query['ApplicationExternalId'] = request.application_external_id
        if not UtilClient.is_unset(request.authenticator_type):
            query['AuthenticatorType'] = request.authenticator_type
        if not UtilClient.is_unset(request.authenticator_uuid):
            query['AuthenticatorUuid'] = request.authenticator_uuid
        if not UtilClient.is_unset(request.from_time):
            query['FromTime'] = request.from_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.to_time):
            query['ToTime'] = request.to_time
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAuthenticatorOpsLogs',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.ListAuthenticatorOpsLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_authenticator_ops_logs_with_options_async(
        self,
        request: idaas_doraemon_20210520_models.ListAuthenticatorOpsLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.ListAuthenticatorOpsLogsResponse:
        """
        @summary 列表查询认证器操作日志
        
        @param request: ListAuthenticatorOpsLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAuthenticatorOpsLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_external_id):
            query['ApplicationExternalId'] = request.application_external_id
        if not UtilClient.is_unset(request.authenticator_type):
            query['AuthenticatorType'] = request.authenticator_type
        if not UtilClient.is_unset(request.authenticator_uuid):
            query['AuthenticatorUuid'] = request.authenticator_uuid
        if not UtilClient.is_unset(request.from_time):
            query['FromTime'] = request.from_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.to_time):
            query['ToTime'] = request.to_time
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAuthenticatorOpsLogs',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.ListAuthenticatorOpsLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_authenticator_ops_logs(
        self,
        request: idaas_doraemon_20210520_models.ListAuthenticatorOpsLogsRequest,
    ) -> idaas_doraemon_20210520_models.ListAuthenticatorOpsLogsResponse:
        """
        @summary 列表查询认证器操作日志
        
        @param request: ListAuthenticatorOpsLogsRequest
        @return: ListAuthenticatorOpsLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_authenticator_ops_logs_with_options(request, runtime)

    async def list_authenticator_ops_logs_async(
        self,
        request: idaas_doraemon_20210520_models.ListAuthenticatorOpsLogsRequest,
    ) -> idaas_doraemon_20210520_models.ListAuthenticatorOpsLogsResponse:
        """
        @summary 列表查询认证器操作日志
        
        @param request: ListAuthenticatorOpsLogsRequest
        @return: ListAuthenticatorOpsLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_authenticator_ops_logs_with_options_async(request, runtime)

    def list_authenticators_with_options(
        self,
        request: idaas_doraemon_20210520_models.ListAuthenticatorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.ListAuthenticatorsResponse:
        """
        @summary 列表查询认证器
        
        @param request: ListAuthenticatorsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAuthenticatorsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_external_id):
            query['ApplicationExternalId'] = request.application_external_id
        if not UtilClient.is_unset(request.authenticator_type):
            query['AuthenticatorType'] = request.authenticator_type
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
            action='ListAuthenticators',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.ListAuthenticatorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_authenticators_with_options_async(
        self,
        request: idaas_doraemon_20210520_models.ListAuthenticatorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.ListAuthenticatorsResponse:
        """
        @summary 列表查询认证器
        
        @param request: ListAuthenticatorsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAuthenticatorsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_external_id):
            query['ApplicationExternalId'] = request.application_external_id
        if not UtilClient.is_unset(request.authenticator_type):
            query['AuthenticatorType'] = request.authenticator_type
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
            action='ListAuthenticators',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.ListAuthenticatorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_authenticators(
        self,
        request: idaas_doraemon_20210520_models.ListAuthenticatorsRequest,
    ) -> idaas_doraemon_20210520_models.ListAuthenticatorsResponse:
        """
        @summary 列表查询认证器
        
        @param request: ListAuthenticatorsRequest
        @return: ListAuthenticatorsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_authenticators_with_options(request, runtime)

    async def list_authenticators_async(
        self,
        request: idaas_doraemon_20210520_models.ListAuthenticatorsRequest,
    ) -> idaas_doraemon_20210520_models.ListAuthenticatorsResponse:
        """
        @summary 列表查询认证器
        
        @param request: ListAuthenticatorsRequest
        @return: ListAuthenticatorsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_authenticators_with_options_async(request, runtime)

    def list_cost_unit_orders_with_options(
        self,
        request: idaas_doraemon_20210520_models.ListCostUnitOrdersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.ListCostUnitOrdersResponse:
        """
        @summary 查询按量计费订单列表
        
        @param request: ListCostUnitOrdersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCostUnitOrdersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_date):
            query['BeginDate'] = request.begin_date
        if not UtilClient.is_unset(request.final_date):
            query['FinalDate'] = request.final_date
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCostUnitOrders',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.ListCostUnitOrdersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cost_unit_orders_with_options_async(
        self,
        request: idaas_doraemon_20210520_models.ListCostUnitOrdersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.ListCostUnitOrdersResponse:
        """
        @summary 查询按量计费订单列表
        
        @param request: ListCostUnitOrdersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCostUnitOrdersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_date):
            query['BeginDate'] = request.begin_date
        if not UtilClient.is_unset(request.final_date):
            query['FinalDate'] = request.final_date
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCostUnitOrders',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.ListCostUnitOrdersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cost_unit_orders(
        self,
        request: idaas_doraemon_20210520_models.ListCostUnitOrdersRequest,
    ) -> idaas_doraemon_20210520_models.ListCostUnitOrdersResponse:
        """
        @summary 查询按量计费订单列表
        
        @param request: ListCostUnitOrdersRequest
        @return: ListCostUnitOrdersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_cost_unit_orders_with_options(request, runtime)

    async def list_cost_unit_orders_async(
        self,
        request: idaas_doraemon_20210520_models.ListCostUnitOrdersRequest,
    ) -> idaas_doraemon_20210520_models.ListCostUnitOrdersResponse:
        """
        @summary 查询按量计费订单列表
        
        @param request: ListCostUnitOrdersRequest
        @return: ListCostUnitOrdersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_cost_unit_orders_with_options_async(request, runtime)

    def list_order_consume_statistic_records_with_options(
        self,
        request: idaas_doraemon_20210520_models.ListOrderConsumeStatisticRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.ListOrderConsumeStatisticRecordsResponse:
        """
        @summary 查询用量消费统计记录列表
        
        @param request: ListOrderConsumeStatisticRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOrderConsumeStatisticRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_order_code):
            query['AliOrderCode'] = request.ali_order_code
        if not UtilClient.is_unset(request.application_external_id):
            query['ApplicationExternalId'] = request.application_external_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.service_code):
            query['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.statistic_time_max):
            query['StatisticTimeMax'] = request.statistic_time_max
        if not UtilClient.is_unset(request.statistic_time_min):
            query['StatisticTimeMin'] = request.statistic_time_min
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOrderConsumeStatisticRecords',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.ListOrderConsumeStatisticRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_order_consume_statistic_records_with_options_async(
        self,
        request: idaas_doraemon_20210520_models.ListOrderConsumeStatisticRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.ListOrderConsumeStatisticRecordsResponse:
        """
        @summary 查询用量消费统计记录列表
        
        @param request: ListOrderConsumeStatisticRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOrderConsumeStatisticRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_order_code):
            query['AliOrderCode'] = request.ali_order_code
        if not UtilClient.is_unset(request.application_external_id):
            query['ApplicationExternalId'] = request.application_external_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.service_code):
            query['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.statistic_time_max):
            query['StatisticTimeMax'] = request.statistic_time_max
        if not UtilClient.is_unset(request.statistic_time_min):
            query['StatisticTimeMin'] = request.statistic_time_min
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOrderConsumeStatisticRecords',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.ListOrderConsumeStatisticRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_order_consume_statistic_records(
        self,
        request: idaas_doraemon_20210520_models.ListOrderConsumeStatisticRecordsRequest,
    ) -> idaas_doraemon_20210520_models.ListOrderConsumeStatisticRecordsResponse:
        """
        @summary 查询用量消费统计记录列表
        
        @param request: ListOrderConsumeStatisticRecordsRequest
        @return: ListOrderConsumeStatisticRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_order_consume_statistic_records_with_options(request, runtime)

    async def list_order_consume_statistic_records_async(
        self,
        request: idaas_doraemon_20210520_models.ListOrderConsumeStatisticRecordsRequest,
    ) -> idaas_doraemon_20210520_models.ListOrderConsumeStatisticRecordsResponse:
        """
        @summary 查询用量消费统计记录列表
        
        @param request: ListOrderConsumeStatisticRecordsRequest
        @return: ListOrderConsumeStatisticRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_order_consume_statistic_records_with_options_async(request, runtime)

    def list_pwned_passwords_with_options(
        self,
        request: idaas_doraemon_20210520_models.ListPwnedPasswordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.ListPwnedPasswordsResponse:
        """
        @summary 弱密码检测
        
        @param request: ListPwnedPasswordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPwnedPasswordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.prefix_hex_password_sha_1hash):
            query['PrefixHexPasswordSha1Hash'] = request.prefix_hex_password_sha_1hash
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPwnedPasswords',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.ListPwnedPasswordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pwned_passwords_with_options_async(
        self,
        request: idaas_doraemon_20210520_models.ListPwnedPasswordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.ListPwnedPasswordsResponse:
        """
        @summary 弱密码检测
        
        @param request: ListPwnedPasswordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPwnedPasswordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.prefix_hex_password_sha_1hash):
            query['PrefixHexPasswordSha1Hash'] = request.prefix_hex_password_sha_1hash
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPwnedPasswords',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.ListPwnedPasswordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pwned_passwords(
        self,
        request: idaas_doraemon_20210520_models.ListPwnedPasswordsRequest,
    ) -> idaas_doraemon_20210520_models.ListPwnedPasswordsResponse:
        """
        @summary 弱密码检测
        
        @param request: ListPwnedPasswordsRequest
        @return: ListPwnedPasswordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_pwned_passwords_with_options(request, runtime)

    async def list_pwned_passwords_async(
        self,
        request: idaas_doraemon_20210520_models.ListPwnedPasswordsRequest,
    ) -> idaas_doraemon_20210520_models.ListPwnedPasswordsResponse:
        """
        @summary 弱密码检测
        
        @param request: ListPwnedPasswordsRequest
        @return: ListPwnedPasswordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_pwned_passwords_with_options_async(request, runtime)

    def list_users_with_options(
        self,
        request: idaas_doraemon_20210520_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.ListUsersResponse:
        """
        @summary 查询应用用户
        
        @param request: ListUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_external_id):
            query['ApplicationExternalId'] = request.application_external_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsers',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.ListUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_users_with_options_async(
        self,
        request: idaas_doraemon_20210520_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.ListUsersResponse:
        """
        @summary 查询应用用户
        
        @param request: ListUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_external_id):
            query['ApplicationExternalId'] = request.application_external_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsers',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.ListUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_users(
        self,
        request: idaas_doraemon_20210520_models.ListUsersRequest,
    ) -> idaas_doraemon_20210520_models.ListUsersResponse:
        """
        @summary 查询应用用户
        
        @param request: ListUsersRequest
        @return: ListUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_users_with_options(request, runtime)

    async def list_users_async(
        self,
        request: idaas_doraemon_20210520_models.ListUsersRequest,
    ) -> idaas_doraemon_20210520_models.ListUsersResponse:
        """
        @summary 查询应用用户
        
        @param request: ListUsersRequest
        @return: ListUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_users_with_options_async(request, runtime)

    def query_sms_reports_with_options(
        self,
        request: idaas_doraemon_20210520_models.QuerySmsReportsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.QuerySmsReportsResponse:
        """
        @summary 短信回执查询
        
        @param request: QuerySmsReportsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsReportsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsReports',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.QuerySmsReportsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_reports_with_options_async(
        self,
        request: idaas_doraemon_20210520_models.QuerySmsReportsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.QuerySmsReportsResponse:
        """
        @summary 短信回执查询
        
        @param request: QuerySmsReportsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsReportsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmsReports',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.QuerySmsReportsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_reports(
        self,
        request: idaas_doraemon_20210520_models.QuerySmsReportsRequest,
    ) -> idaas_doraemon_20210520_models.QuerySmsReportsResponse:
        """
        @summary 短信回执查询
        
        @param request: QuerySmsReportsRequest
        @return: QuerySmsReportsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_sms_reports_with_options(request, runtime)

    async def query_sms_reports_async(
        self,
        request: idaas_doraemon_20210520_models.QuerySmsReportsRequest,
    ) -> idaas_doraemon_20210520_models.QuerySmsReportsResponse:
        """
        @summary 短信回执查询
        
        @param request: QuerySmsReportsRequest
        @return: QuerySmsReportsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_sms_reports_with_options_async(request, runtime)

    def query_sms_ups_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.QuerySmsUpsResponse:
        """
        @summary 短信上行查询
        
        @param request: QuerySmsUpsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsUpsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='QuerySmsUps',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.QuerySmsUpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sms_ups_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.QuerySmsUpsResponse:
        """
        @summary 短信上行查询
        
        @param request: QuerySmsUpsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySmsUpsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='QuerySmsUps',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.QuerySmsUpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sms_ups(self) -> idaas_doraemon_20210520_models.QuerySmsUpsResponse:
        """
        @summary 短信上行查询
        
        @return: QuerySmsUpsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_sms_ups_with_options(runtime)

    async def query_sms_ups_async(self) -> idaas_doraemon_20210520_models.QuerySmsUpsResponse:
        """
        @summary 短信上行查询
        
        @return: QuerySmsUpsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_sms_ups_with_options_async(runtime)

    def register_authenticator_with_options(
        self,
        request: idaas_doraemon_20210520_models.RegisterAuthenticatorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.RegisterAuthenticatorResponse:
        """
        @summary 注册认证器
        
        @param request: RegisterAuthenticatorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RegisterAuthenticatorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_external_id):
            query['ApplicationExternalId'] = request.application_external_id
        if not UtilClient.is_unset(request.authenticator_name):
            query['AuthenticatorName'] = request.authenticator_name
        if not UtilClient.is_unset(request.authenticator_type):
            query['AuthenticatorType'] = request.authenticator_type
        if not UtilClient.is_unset(request.client_extend_params_json):
            query['ClientExtendParamsJson'] = request.client_extend_params_json
        if not UtilClient.is_unset(request.client_extend_params_json_sign):
            query['ClientExtendParamsJsonSign'] = request.client_extend_params_json_sign
        if not UtilClient.is_unset(request.log_params):
            query['LogParams'] = request.log_params
        if not UtilClient.is_unset(request.registration_context):
            query['RegistrationContext'] = request.registration_context
        if not UtilClient.is_unset(request.require_challenge_base_64):
            query['RequireChallengeBase64'] = request.require_challenge_base_64
        if not UtilClient.is_unset(request.server_extend_params_json):
            query['ServerExtendParamsJson'] = request.server_extend_params_json
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_source_ip):
            query['UserSourceIp'] = request.user_source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegisterAuthenticator',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.RegisterAuthenticatorResponse(),
            self.call_api(params, req, runtime)
        )

    async def register_authenticator_with_options_async(
        self,
        request: idaas_doraemon_20210520_models.RegisterAuthenticatorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.RegisterAuthenticatorResponse:
        """
        @summary 注册认证器
        
        @param request: RegisterAuthenticatorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RegisterAuthenticatorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_external_id):
            query['ApplicationExternalId'] = request.application_external_id
        if not UtilClient.is_unset(request.authenticator_name):
            query['AuthenticatorName'] = request.authenticator_name
        if not UtilClient.is_unset(request.authenticator_type):
            query['AuthenticatorType'] = request.authenticator_type
        if not UtilClient.is_unset(request.client_extend_params_json):
            query['ClientExtendParamsJson'] = request.client_extend_params_json
        if not UtilClient.is_unset(request.client_extend_params_json_sign):
            query['ClientExtendParamsJsonSign'] = request.client_extend_params_json_sign
        if not UtilClient.is_unset(request.log_params):
            query['LogParams'] = request.log_params
        if not UtilClient.is_unset(request.registration_context):
            query['RegistrationContext'] = request.registration_context
        if not UtilClient.is_unset(request.require_challenge_base_64):
            query['RequireChallengeBase64'] = request.require_challenge_base_64
        if not UtilClient.is_unset(request.server_extend_params_json):
            query['ServerExtendParamsJson'] = request.server_extend_params_json
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_source_ip):
            query['UserSourceIp'] = request.user_source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegisterAuthenticator',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.RegisterAuthenticatorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def register_authenticator(
        self,
        request: idaas_doraemon_20210520_models.RegisterAuthenticatorRequest,
    ) -> idaas_doraemon_20210520_models.RegisterAuthenticatorResponse:
        """
        @summary 注册认证器
        
        @param request: RegisterAuthenticatorRequest
        @return: RegisterAuthenticatorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.register_authenticator_with_options(request, runtime)

    async def register_authenticator_async(
        self,
        request: idaas_doraemon_20210520_models.RegisterAuthenticatorRequest,
    ) -> idaas_doraemon_20210520_models.RegisterAuthenticatorResponse:
        """
        @summary 注册认证器
        
        @param request: RegisterAuthenticatorRequest
        @return: RegisterAuthenticatorResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.register_authenticator_with_options_async(request, runtime)

    def service_invoke_with_options(
        self,
        request: idaas_doraemon_20210520_models.ServiceInvokeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.ServiceInvokeResponse:
        """
        @summary 认证接口
        
        @param request: ServiceInvokeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ServiceInvokeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_external_id):
            query['ApplicationExternalId'] = request.application_external_id
        if not UtilClient.is_unset(request.doraemon_action):
            query['DoraemonAction'] = request.doraemon_action
        if not UtilClient.is_unset(request.mobile_extend_params_json):
            query['MobileExtendParamsJson'] = request.mobile_extend_params_json
        if not UtilClient.is_unset(request.mobile_extend_params_json_sign):
            query['MobileExtendParamsJsonSign'] = request.mobile_extend_params_json_sign
        if not UtilClient.is_unset(request.server_extend_params_json):
            query['ServerExtendParamsJson'] = request.server_extend_params_json
        if not UtilClient.is_unset(request.service_code):
            query['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.test_model):
            query['TestModel'] = request.test_model
        if not UtilClient.is_unset(request.xclient_ip):
            query['XClientIp'] = request.xclient_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ServiceInvoke',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.ServiceInvokeResponse(),
            self.call_api(params, req, runtime)
        )

    async def service_invoke_with_options_async(
        self,
        request: idaas_doraemon_20210520_models.ServiceInvokeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.ServiceInvokeResponse:
        """
        @summary 认证接口
        
        @param request: ServiceInvokeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ServiceInvokeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_external_id):
            query['ApplicationExternalId'] = request.application_external_id
        if not UtilClient.is_unset(request.doraemon_action):
            query['DoraemonAction'] = request.doraemon_action
        if not UtilClient.is_unset(request.mobile_extend_params_json):
            query['MobileExtendParamsJson'] = request.mobile_extend_params_json
        if not UtilClient.is_unset(request.mobile_extend_params_json_sign):
            query['MobileExtendParamsJsonSign'] = request.mobile_extend_params_json_sign
        if not UtilClient.is_unset(request.server_extend_params_json):
            query['ServerExtendParamsJson'] = request.server_extend_params_json
        if not UtilClient.is_unset(request.service_code):
            query['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.test_model):
            query['TestModel'] = request.test_model
        if not UtilClient.is_unset(request.xclient_ip):
            query['XClientIp'] = request.xclient_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ServiceInvoke',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.ServiceInvokeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def service_invoke(
        self,
        request: idaas_doraemon_20210520_models.ServiceInvokeRequest,
    ) -> idaas_doraemon_20210520_models.ServiceInvokeResponse:
        """
        @summary 认证接口
        
        @param request: ServiceInvokeRequest
        @return: ServiceInvokeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.service_invoke_with_options(request, runtime)

    async def service_invoke_async(
        self,
        request: idaas_doraemon_20210520_models.ServiceInvokeRequest,
    ) -> idaas_doraemon_20210520_models.ServiceInvokeResponse:
        """
        @summary 认证接口
        
        @param request: ServiceInvokeRequest
        @return: ServiceInvokeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.service_invoke_with_options_async(request, runtime)

    def update_authenticator_attribute_with_options(
        self,
        request: idaas_doraemon_20210520_models.UpdateAuthenticatorAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.UpdateAuthenticatorAttributeResponse:
        """
        @summary 更新认证器名字
        
        @param request: UpdateAuthenticatorAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAuthenticatorAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_external_id):
            query['ApplicationExternalId'] = request.application_external_id
        if not UtilClient.is_unset(request.authenticator_name):
            query['AuthenticatorName'] = request.authenticator_name
        if not UtilClient.is_unset(request.authenticator_uuid):
            query['AuthenticatorUuid'] = request.authenticator_uuid
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAuthenticatorAttribute',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.UpdateAuthenticatorAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_authenticator_attribute_with_options_async(
        self,
        request: idaas_doraemon_20210520_models.UpdateAuthenticatorAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.UpdateAuthenticatorAttributeResponse:
        """
        @summary 更新认证器名字
        
        @param request: UpdateAuthenticatorAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAuthenticatorAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_external_id):
            query['ApplicationExternalId'] = request.application_external_id
        if not UtilClient.is_unset(request.authenticator_name):
            query['AuthenticatorName'] = request.authenticator_name
        if not UtilClient.is_unset(request.authenticator_uuid):
            query['AuthenticatorUuid'] = request.authenticator_uuid
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAuthenticatorAttribute',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.UpdateAuthenticatorAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_authenticator_attribute(
        self,
        request: idaas_doraemon_20210520_models.UpdateAuthenticatorAttributeRequest,
    ) -> idaas_doraemon_20210520_models.UpdateAuthenticatorAttributeResponse:
        """
        @summary 更新认证器名字
        
        @param request: UpdateAuthenticatorAttributeRequest
        @return: UpdateAuthenticatorAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_authenticator_attribute_with_options(request, runtime)

    async def update_authenticator_attribute_async(
        self,
        request: idaas_doraemon_20210520_models.UpdateAuthenticatorAttributeRequest,
    ) -> idaas_doraemon_20210520_models.UpdateAuthenticatorAttributeResponse:
        """
        @summary 更新认证器名字
        
        @param request: UpdateAuthenticatorAttributeRequest
        @return: UpdateAuthenticatorAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_authenticator_attribute_with_options_async(request, runtime)

    def verify_id_token_with_options(
        self,
        request: idaas_doraemon_20210520_models.VerifyIdTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.VerifyIdTokenResponse:
        """
        @summary 验证id_token
        
        @param request: VerifyIdTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifyIdTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_external_id):
            query['ApplicationExternalId'] = request.application_external_id
        if not UtilClient.is_unset(request.jwt_id_token):
            query['JwtIdToken'] = request.jwt_id_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyIdToken',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.VerifyIdTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_id_token_with_options_async(
        self,
        request: idaas_doraemon_20210520_models.VerifyIdTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.VerifyIdTokenResponse:
        """
        @summary 验证id_token
        
        @param request: VerifyIdTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifyIdTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_external_id):
            query['ApplicationExternalId'] = request.application_external_id
        if not UtilClient.is_unset(request.jwt_id_token):
            query['JwtIdToken'] = request.jwt_id_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyIdToken',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.VerifyIdTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_id_token(
        self,
        request: idaas_doraemon_20210520_models.VerifyIdTokenRequest,
    ) -> idaas_doraemon_20210520_models.VerifyIdTokenResponse:
        """
        @summary 验证id_token
        
        @param request: VerifyIdTokenRequest
        @return: VerifyIdTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.verify_id_token_with_options(request, runtime)

    async def verify_id_token_async(
        self,
        request: idaas_doraemon_20210520_models.VerifyIdTokenRequest,
    ) -> idaas_doraemon_20210520_models.VerifyIdTokenResponse:
        """
        @summary 验证id_token
        
        @param request: VerifyIdTokenRequest
        @return: VerifyIdTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.verify_id_token_with_options_async(request, runtime)

    def verify_user_authentication_with_options(
        self,
        request: idaas_doraemon_20210520_models.VerifyUserAuthenticationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.VerifyUserAuthenticationResponse:
        """
        @summary 认证用户
        
        @param request: VerifyUserAuthenticationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifyUserAuthenticationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_external_id):
            query['ApplicationExternalId'] = request.application_external_id
        if not UtilClient.is_unset(request.authentication_context):
            query['AuthenticationContext'] = request.authentication_context
        if not UtilClient.is_unset(request.authenticator_type):
            query['AuthenticatorType'] = request.authenticator_type
        if not UtilClient.is_unset(request.client_extend_params_json):
            query['ClientExtendParamsJson'] = request.client_extend_params_json
        if not UtilClient.is_unset(request.client_extend_params_json_sign):
            query['ClientExtendParamsJsonSign'] = request.client_extend_params_json_sign
        if not UtilClient.is_unset(request.log_params):
            query['LogParams'] = request.log_params
        if not UtilClient.is_unset(request.log_tag):
            query['LogTag'] = request.log_tag
        if not UtilClient.is_unset(request.require_bind_hash_base_64):
            query['RequireBindHashBase64'] = request.require_bind_hash_base_64
        if not UtilClient.is_unset(request.require_challenge_base_64):
            query['RequireChallengeBase64'] = request.require_challenge_base_64
        if not UtilClient.is_unset(request.server_extend_params_json):
            query['ServerExtendParamsJson'] = request.server_extend_params_json
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_source_ip):
            query['UserSourceIp'] = request.user_source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyUserAuthentication',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.VerifyUserAuthenticationResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_user_authentication_with_options_async(
        self,
        request: idaas_doraemon_20210520_models.VerifyUserAuthenticationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.VerifyUserAuthenticationResponse:
        """
        @summary 认证用户
        
        @param request: VerifyUserAuthenticationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifyUserAuthenticationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_external_id):
            query['ApplicationExternalId'] = request.application_external_id
        if not UtilClient.is_unset(request.authentication_context):
            query['AuthenticationContext'] = request.authentication_context
        if not UtilClient.is_unset(request.authenticator_type):
            query['AuthenticatorType'] = request.authenticator_type
        if not UtilClient.is_unset(request.client_extend_params_json):
            query['ClientExtendParamsJson'] = request.client_extend_params_json
        if not UtilClient.is_unset(request.client_extend_params_json_sign):
            query['ClientExtendParamsJsonSign'] = request.client_extend_params_json_sign
        if not UtilClient.is_unset(request.log_params):
            query['LogParams'] = request.log_params
        if not UtilClient.is_unset(request.log_tag):
            query['LogTag'] = request.log_tag
        if not UtilClient.is_unset(request.require_bind_hash_base_64):
            query['RequireBindHashBase64'] = request.require_bind_hash_base_64
        if not UtilClient.is_unset(request.require_challenge_base_64):
            query['RequireChallengeBase64'] = request.require_challenge_base_64
        if not UtilClient.is_unset(request.server_extend_params_json):
            query['ServerExtendParamsJson'] = request.server_extend_params_json
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_source_ip):
            query['UserSourceIp'] = request.user_source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyUserAuthentication',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.VerifyUserAuthenticationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_user_authentication(
        self,
        request: idaas_doraemon_20210520_models.VerifyUserAuthenticationRequest,
    ) -> idaas_doraemon_20210520_models.VerifyUserAuthenticationResponse:
        """
        @summary 认证用户
        
        @param request: VerifyUserAuthenticationRequest
        @return: VerifyUserAuthenticationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.verify_user_authentication_with_options(request, runtime)

    async def verify_user_authentication_async(
        self,
        request: idaas_doraemon_20210520_models.VerifyUserAuthenticationRequest,
    ) -> idaas_doraemon_20210520_models.VerifyUserAuthenticationResponse:
        """
        @summary 认证用户
        
        @param request: VerifyUserAuthenticationRequest
        @return: VerifyUserAuthenticationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.verify_user_authentication_with_options_async(request, runtime)
