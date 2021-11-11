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
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.CreateAuthenticatorRegistrationResponse(),
            self.do_rpcrequest('CreateAuthenticatorRegistration', '2021-05-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_authenticator_registration_with_options_async(
        self,
        request: idaas_doraemon_20210520_models.CreateAuthenticatorRegistrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.CreateAuthenticatorRegistrationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.CreateAuthenticatorRegistrationResponse(),
            await self.do_rpcrequest_async('CreateAuthenticatorRegistration', '2021-05-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_authenticator_registration(
        self,
        request: idaas_doraemon_20210520_models.CreateAuthenticatorRegistrationRequest,
    ) -> idaas_doraemon_20210520_models.CreateAuthenticatorRegistrationResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_authenticator_registration_with_options(request, runtime)

    async def create_authenticator_registration_async(
        self,
        request: idaas_doraemon_20210520_models.CreateAuthenticatorRegistrationRequest,
    ) -> idaas_doraemon_20210520_models.CreateAuthenticatorRegistrationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_authenticator_registration_with_options_async(request, runtime)

    def create_user_authenticate_options_with_options(
        self,
        request: idaas_doraemon_20210520_models.CreateUserAuthenticateOptionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.CreateUserAuthenticateOptionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.CreateUserAuthenticateOptionsResponse(),
            self.do_rpcrequest('CreateUserAuthenticateOptions', '2021-05-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_user_authenticate_options_with_options_async(
        self,
        request: idaas_doraemon_20210520_models.CreateUserAuthenticateOptionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.CreateUserAuthenticateOptionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.CreateUserAuthenticateOptionsResponse(),
            await self.do_rpcrequest_async('CreateUserAuthenticateOptions', '2021-05-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_user_authenticate_options(
        self,
        request: idaas_doraemon_20210520_models.CreateUserAuthenticateOptionsRequest,
    ) -> idaas_doraemon_20210520_models.CreateUserAuthenticateOptionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_user_authenticate_options_with_options(request, runtime)

    async def create_user_authenticate_options_async(
        self,
        request: idaas_doraemon_20210520_models.CreateUserAuthenticateOptionsRequest,
    ) -> idaas_doraemon_20210520_models.CreateUserAuthenticateOptionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_user_authenticate_options_with_options_async(request, runtime)

    def deregister_authenticator_with_options(
        self,
        request: idaas_doraemon_20210520_models.DeregisterAuthenticatorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.DeregisterAuthenticatorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.DeregisterAuthenticatorResponse(),
            self.do_rpcrequest('DeregisterAuthenticator', '2021-05-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def deregister_authenticator_with_options_async(
        self,
        request: idaas_doraemon_20210520_models.DeregisterAuthenticatorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.DeregisterAuthenticatorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.DeregisterAuthenticatorResponse(),
            await self.do_rpcrequest_async('DeregisterAuthenticator', '2021-05-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def deregister_authenticator(
        self,
        request: idaas_doraemon_20210520_models.DeregisterAuthenticatorRequest,
    ) -> idaas_doraemon_20210520_models.DeregisterAuthenticatorResponse:
        runtime = util_models.RuntimeOptions()
        return self.deregister_authenticator_with_options(request, runtime)

    async def deregister_authenticator_async(
        self,
        request: idaas_doraemon_20210520_models.DeregisterAuthenticatorRequest,
    ) -> idaas_doraemon_20210520_models.DeregisterAuthenticatorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.deregister_authenticator_with_options_async(request, runtime)

    def fetch_access_token_with_options(
        self,
        request: idaas_doraemon_20210520_models.FetchAccessTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.FetchAccessTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.FetchAccessTokenResponse(),
            self.do_rpcrequest('FetchAccessToken', '2021-05-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def fetch_access_token_with_options_async(
        self,
        request: idaas_doraemon_20210520_models.FetchAccessTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.FetchAccessTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.FetchAccessTokenResponse(),
            await self.do_rpcrequest_async('FetchAccessToken', '2021-05-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def fetch_access_token(
        self,
        request: idaas_doraemon_20210520_models.FetchAccessTokenRequest,
    ) -> idaas_doraemon_20210520_models.FetchAccessTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.fetch_access_token_with_options(request, runtime)

    async def fetch_access_token_async(
        self,
        request: idaas_doraemon_20210520_models.FetchAccessTokenRequest,
    ) -> idaas_doraemon_20210520_models.FetchAccessTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.fetch_access_token_with_options_async(request, runtime)

    def get_authenticator_with_options(
        self,
        request: idaas_doraemon_20210520_models.GetAuthenticatorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.GetAuthenticatorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.GetAuthenticatorResponse(),
            self.do_rpcrequest('GetAuthenticator', '2021-05-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_authenticator_with_options_async(
        self,
        request: idaas_doraemon_20210520_models.GetAuthenticatorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.GetAuthenticatorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.GetAuthenticatorResponse(),
            await self.do_rpcrequest_async('GetAuthenticator', '2021-05-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_authenticator(
        self,
        request: idaas_doraemon_20210520_models.GetAuthenticatorRequest,
    ) -> idaas_doraemon_20210520_models.GetAuthenticatorResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_authenticator_with_options(request, runtime)

    async def get_authenticator_async(
        self,
        request: idaas_doraemon_20210520_models.GetAuthenticatorRequest,
    ) -> idaas_doraemon_20210520_models.GetAuthenticatorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_authenticator_with_options_async(request, runtime)

    def list_authentication_logs_with_options(
        self,
        request: idaas_doraemon_20210520_models.ListAuthenticationLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.ListAuthenticationLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.ListAuthenticationLogsResponse(),
            self.do_rpcrequest('ListAuthenticationLogs', '2021-05-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_authentication_logs_with_options_async(
        self,
        request: idaas_doraemon_20210520_models.ListAuthenticationLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.ListAuthenticationLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.ListAuthenticationLogsResponse(),
            await self.do_rpcrequest_async('ListAuthenticationLogs', '2021-05-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_authentication_logs(
        self,
        request: idaas_doraemon_20210520_models.ListAuthenticationLogsRequest,
    ) -> idaas_doraemon_20210520_models.ListAuthenticationLogsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_authentication_logs_with_options(request, runtime)

    async def list_authentication_logs_async(
        self,
        request: idaas_doraemon_20210520_models.ListAuthenticationLogsRequest,
    ) -> idaas_doraemon_20210520_models.ListAuthenticationLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_authentication_logs_with_options_async(request, runtime)

    def list_authenticator_ops_logs_with_options(
        self,
        request: idaas_doraemon_20210520_models.ListAuthenticatorOpsLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.ListAuthenticatorOpsLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.ListAuthenticatorOpsLogsResponse(),
            self.do_rpcrequest('ListAuthenticatorOpsLogs', '2021-05-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_authenticator_ops_logs_with_options_async(
        self,
        request: idaas_doraemon_20210520_models.ListAuthenticatorOpsLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.ListAuthenticatorOpsLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.ListAuthenticatorOpsLogsResponse(),
            await self.do_rpcrequest_async('ListAuthenticatorOpsLogs', '2021-05-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_authenticator_ops_logs(
        self,
        request: idaas_doraemon_20210520_models.ListAuthenticatorOpsLogsRequest,
    ) -> idaas_doraemon_20210520_models.ListAuthenticatorOpsLogsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_authenticator_ops_logs_with_options(request, runtime)

    async def list_authenticator_ops_logs_async(
        self,
        request: idaas_doraemon_20210520_models.ListAuthenticatorOpsLogsRequest,
    ) -> idaas_doraemon_20210520_models.ListAuthenticatorOpsLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_authenticator_ops_logs_with_options_async(request, runtime)

    def list_authenticators_with_options(
        self,
        request: idaas_doraemon_20210520_models.ListAuthenticatorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.ListAuthenticatorsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.ListAuthenticatorsResponse(),
            self.do_rpcrequest('ListAuthenticators', '2021-05-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_authenticators_with_options_async(
        self,
        request: idaas_doraemon_20210520_models.ListAuthenticatorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.ListAuthenticatorsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.ListAuthenticatorsResponse(),
            await self.do_rpcrequest_async('ListAuthenticators', '2021-05-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_authenticators(
        self,
        request: idaas_doraemon_20210520_models.ListAuthenticatorsRequest,
    ) -> idaas_doraemon_20210520_models.ListAuthenticatorsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_authenticators_with_options(request, runtime)

    async def list_authenticators_async(
        self,
        request: idaas_doraemon_20210520_models.ListAuthenticatorsRequest,
    ) -> idaas_doraemon_20210520_models.ListAuthenticatorsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_authenticators_with_options_async(request, runtime)

    def list_pwned_passwords_with_options(
        self,
        request: idaas_doraemon_20210520_models.ListPwnedPasswordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.ListPwnedPasswordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.ListPwnedPasswordsResponse(),
            self.do_rpcrequest('ListPwnedPasswords', '2021-05-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_pwned_passwords_with_options_async(
        self,
        request: idaas_doraemon_20210520_models.ListPwnedPasswordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.ListPwnedPasswordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.ListPwnedPasswordsResponse(),
            await self.do_rpcrequest_async('ListPwnedPasswords', '2021-05-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_pwned_passwords(
        self,
        request: idaas_doraemon_20210520_models.ListPwnedPasswordsRequest,
    ) -> idaas_doraemon_20210520_models.ListPwnedPasswordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_pwned_passwords_with_options(request, runtime)

    async def list_pwned_passwords_async(
        self,
        request: idaas_doraemon_20210520_models.ListPwnedPasswordsRequest,
    ) -> idaas_doraemon_20210520_models.ListPwnedPasswordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_pwned_passwords_with_options_async(request, runtime)

    def list_users_with_options(
        self,
        request: idaas_doraemon_20210520_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.ListUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.ListUsersResponse(),
            self.do_rpcrequest('ListUsers', '2021-05-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_users_with_options_async(
        self,
        request: idaas_doraemon_20210520_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.ListUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.ListUsersResponse(),
            await self.do_rpcrequest_async('ListUsers', '2021-05-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_users(
        self,
        request: idaas_doraemon_20210520_models.ListUsersRequest,
    ) -> idaas_doraemon_20210520_models.ListUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_users_with_options(request, runtime)

    async def list_users_async(
        self,
        request: idaas_doraemon_20210520_models.ListUsersRequest,
    ) -> idaas_doraemon_20210520_models.ListUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_users_with_options_async(request, runtime)

    def register_authenticator_with_options(
        self,
        request: idaas_doraemon_20210520_models.RegisterAuthenticatorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.RegisterAuthenticatorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.RegisterAuthenticatorResponse(),
            self.do_rpcrequest('RegisterAuthenticator', '2021-05-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def register_authenticator_with_options_async(
        self,
        request: idaas_doraemon_20210520_models.RegisterAuthenticatorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.RegisterAuthenticatorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.RegisterAuthenticatorResponse(),
            await self.do_rpcrequest_async('RegisterAuthenticator', '2021-05-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def register_authenticator(
        self,
        request: idaas_doraemon_20210520_models.RegisterAuthenticatorRequest,
    ) -> idaas_doraemon_20210520_models.RegisterAuthenticatorResponse:
        runtime = util_models.RuntimeOptions()
        return self.register_authenticator_with_options(request, runtime)

    async def register_authenticator_async(
        self,
        request: idaas_doraemon_20210520_models.RegisterAuthenticatorRequest,
    ) -> idaas_doraemon_20210520_models.RegisterAuthenticatorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.register_authenticator_with_options_async(request, runtime)

    def service_invoke_with_options(
        self,
        request: idaas_doraemon_20210520_models.ServiceInvokeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.ServiceInvokeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.ServiceInvokeResponse(),
            self.do_rpcrequest('ServiceInvoke', '2021-05-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def service_invoke_with_options_async(
        self,
        request: idaas_doraemon_20210520_models.ServiceInvokeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.ServiceInvokeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.ServiceInvokeResponse(),
            await self.do_rpcrequest_async('ServiceInvoke', '2021-05-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def service_invoke(
        self,
        request: idaas_doraemon_20210520_models.ServiceInvokeRequest,
    ) -> idaas_doraemon_20210520_models.ServiceInvokeResponse:
        runtime = util_models.RuntimeOptions()
        return self.service_invoke_with_options(request, runtime)

    async def service_invoke_async(
        self,
        request: idaas_doraemon_20210520_models.ServiceInvokeRequest,
    ) -> idaas_doraemon_20210520_models.ServiceInvokeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.service_invoke_with_options_async(request, runtime)

    def update_authenticator_attribute_with_options(
        self,
        request: idaas_doraemon_20210520_models.UpdateAuthenticatorAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.UpdateAuthenticatorAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.UpdateAuthenticatorAttributeResponse(),
            self.do_rpcrequest('UpdateAuthenticatorAttribute', '2021-05-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_authenticator_attribute_with_options_async(
        self,
        request: idaas_doraemon_20210520_models.UpdateAuthenticatorAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.UpdateAuthenticatorAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.UpdateAuthenticatorAttributeResponse(),
            await self.do_rpcrequest_async('UpdateAuthenticatorAttribute', '2021-05-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_authenticator_attribute(
        self,
        request: idaas_doraemon_20210520_models.UpdateAuthenticatorAttributeRequest,
    ) -> idaas_doraemon_20210520_models.UpdateAuthenticatorAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_authenticator_attribute_with_options(request, runtime)

    async def update_authenticator_attribute_async(
        self,
        request: idaas_doraemon_20210520_models.UpdateAuthenticatorAttributeRequest,
    ) -> idaas_doraemon_20210520_models.UpdateAuthenticatorAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_authenticator_attribute_with_options_async(request, runtime)

    def verify_user_authentication_with_options(
        self,
        request: idaas_doraemon_20210520_models.VerifyUserAuthenticationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.VerifyUserAuthenticationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.VerifyUserAuthenticationResponse(),
            self.do_rpcrequest('VerifyUserAuthentication', '2021-05-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def verify_user_authentication_with_options_async(
        self,
        request: idaas_doraemon_20210520_models.VerifyUserAuthenticationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> idaas_doraemon_20210520_models.VerifyUserAuthenticationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            idaas_doraemon_20210520_models.VerifyUserAuthenticationResponse(),
            await self.do_rpcrequest_async('VerifyUserAuthentication', '2021-05-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def verify_user_authentication(
        self,
        request: idaas_doraemon_20210520_models.VerifyUserAuthenticationRequest,
    ) -> idaas_doraemon_20210520_models.VerifyUserAuthenticationResponse:
        runtime = util_models.RuntimeOptions()
        return self.verify_user_authentication_with_options(request, runtime)

    async def verify_user_authentication_async(
        self,
        request: idaas_doraemon_20210520_models.VerifyUserAuthenticationRequest,
    ) -> idaas_doraemon_20210520_models.VerifyUserAuthenticationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.verify_user_authentication_with_options_async(request, runtime)
