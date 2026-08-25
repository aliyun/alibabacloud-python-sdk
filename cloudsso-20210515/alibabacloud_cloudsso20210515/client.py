# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_cloudsso20210515 import models as main_models
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
        self._endpoint_map = {
            'cn-shanghai': 'cloudsso.cn-shanghai.aliyuncs.com',
            'cn-hongkong': 'cloudsso.cn-hongkong.aliyuncs.com',
            'ap-northeast-2': 'cloudsso.ap-northeast-2.aliyuncs.com',
            'ap-southeast-1': 'cloudsso.ap-southeast-1.aliyuncs.com',
            'us-west-1': 'cloudsso.us-west-1.aliyuncs.com',
            'eu-central-1': 'cloudsso.eu-central-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('cloudsso', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_external_samlid_pcertificate_with_options(
        self,
        request: main_models.AddExternalSAMLIdPCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddExternalSAMLIdPCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.x_509certificate):
            query['X509Certificate'] = request.x_509certificate
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddExternalSAMLIdPCertificate',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddExternalSAMLIdPCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_external_samlid_pcertificate_with_options_async(
        self,
        request: main_models.AddExternalSAMLIdPCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddExternalSAMLIdPCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.x_509certificate):
            query['X509Certificate'] = request.x_509certificate
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddExternalSAMLIdPCertificate',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddExternalSAMLIdPCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_external_samlid_pcertificate(
        self,
        request: main_models.AddExternalSAMLIdPCertificateRequest,
    ) -> main_models.AddExternalSAMLIdPCertificateResponse:
        runtime = RuntimeOptions()
        return self.add_external_samlid_pcertificate_with_options(request, runtime)

    async def add_external_samlid_pcertificate_async(
        self,
        request: main_models.AddExternalSAMLIdPCertificateRequest,
    ) -> main_models.AddExternalSAMLIdPCertificateResponse:
        runtime = RuntimeOptions()
        return await self.add_external_samlid_pcertificate_with_options_async(request, runtime)

    def add_permission_policy_to_access_configuration_with_options(
        self,
        request: main_models.AddPermissionPolicyToAccessConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddPermissionPolicyToAccessConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.inline_policy_document):
            query['InlinePolicyDocument'] = request.inline_policy_document
        if not DaraCore.is_null(request.permission_policy_name):
            query['PermissionPolicyName'] = request.permission_policy_name
        if not DaraCore.is_null(request.permission_policy_type):
            query['PermissionPolicyType'] = request.permission_policy_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddPermissionPolicyToAccessConfiguration',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddPermissionPolicyToAccessConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_permission_policy_to_access_configuration_with_options_async(
        self,
        request: main_models.AddPermissionPolicyToAccessConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddPermissionPolicyToAccessConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.inline_policy_document):
            query['InlinePolicyDocument'] = request.inline_policy_document
        if not DaraCore.is_null(request.permission_policy_name):
            query['PermissionPolicyName'] = request.permission_policy_name
        if not DaraCore.is_null(request.permission_policy_type):
            query['PermissionPolicyType'] = request.permission_policy_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddPermissionPolicyToAccessConfiguration',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddPermissionPolicyToAccessConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_permission_policy_to_access_configuration(
        self,
        request: main_models.AddPermissionPolicyToAccessConfigurationRequest,
    ) -> main_models.AddPermissionPolicyToAccessConfigurationResponse:
        runtime = RuntimeOptions()
        return self.add_permission_policy_to_access_configuration_with_options(request, runtime)

    async def add_permission_policy_to_access_configuration_async(
        self,
        request: main_models.AddPermissionPolicyToAccessConfigurationRequest,
    ) -> main_models.AddPermissionPolicyToAccessConfigurationResponse:
        runtime = RuntimeOptions()
        return await self.add_permission_policy_to_access_configuration_with_options_async(request, runtime)

    def add_user_to_group_with_options(
        self,
        request: main_models.AddUserToGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddUserToGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddUserToGroup',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddUserToGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_user_to_group_with_options_async(
        self,
        request: main_models.AddUserToGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddUserToGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddUserToGroup',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddUserToGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_user_to_group(
        self,
        request: main_models.AddUserToGroupRequest,
    ) -> main_models.AddUserToGroupResponse:
        runtime = RuntimeOptions()
        return self.add_user_to_group_with_options(request, runtime)

    async def add_user_to_group_async(
        self,
        request: main_models.AddUserToGroupRequest,
    ) -> main_models.AddUserToGroupResponse:
        runtime = RuntimeOptions()
        return await self.add_user_to_group_with_options_async(request, runtime)

    def clear_external_samlidentity_provider_with_options(
        self,
        request: main_models.ClearExternalSAMLIdentityProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ClearExternalSAMLIdentityProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ClearExternalSAMLIdentityProvider',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ClearExternalSAMLIdentityProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def clear_external_samlidentity_provider_with_options_async(
        self,
        request: main_models.ClearExternalSAMLIdentityProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ClearExternalSAMLIdentityProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ClearExternalSAMLIdentityProvider',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ClearExternalSAMLIdentityProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clear_external_samlidentity_provider(
        self,
        request: main_models.ClearExternalSAMLIdentityProviderRequest,
    ) -> main_models.ClearExternalSAMLIdentityProviderResponse:
        runtime = RuntimeOptions()
        return self.clear_external_samlidentity_provider_with_options(request, runtime)

    async def clear_external_samlidentity_provider_async(
        self,
        request: main_models.ClearExternalSAMLIdentityProviderRequest,
    ) -> main_models.ClearExternalSAMLIdentityProviderResponse:
        runtime = RuntimeOptions()
        return await self.clear_external_samlidentity_provider_with_options_async(request, runtime)

    def create_access_assignment_with_options(
        self,
        request: main_models.CreateAccessAssignmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAccessAssignmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.origin_target_id):
            query['OriginTargetId'] = request.origin_target_id
        if not DaraCore.is_null(request.principal_id):
            query['PrincipalId'] = request.principal_id
        if not DaraCore.is_null(request.principal_type):
            query['PrincipalType'] = request.principal_type
        if not DaraCore.is_null(request.target_id):
            query['TargetId'] = request.target_id
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAccessAssignment',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAccessAssignmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_access_assignment_with_options_async(
        self,
        request: main_models.CreateAccessAssignmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAccessAssignmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.origin_target_id):
            query['OriginTargetId'] = request.origin_target_id
        if not DaraCore.is_null(request.principal_id):
            query['PrincipalId'] = request.principal_id
        if not DaraCore.is_null(request.principal_type):
            query['PrincipalType'] = request.principal_type
        if not DaraCore.is_null(request.target_id):
            query['TargetId'] = request.target_id
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAccessAssignment',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAccessAssignmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_access_assignment(
        self,
        request: main_models.CreateAccessAssignmentRequest,
    ) -> main_models.CreateAccessAssignmentResponse:
        runtime = RuntimeOptions()
        return self.create_access_assignment_with_options(request, runtime)

    async def create_access_assignment_async(
        self,
        request: main_models.CreateAccessAssignmentRequest,
    ) -> main_models.CreateAccessAssignmentResponse:
        runtime = RuntimeOptions()
        return await self.create_access_assignment_with_options_async(request, runtime)

    def create_access_configuration_with_options(
        self,
        request: main_models.CreateAccessConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAccessConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_configuration_name):
            query['AccessConfigurationName'] = request.access_configuration_name
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.relay_state):
            query['RelayState'] = request.relay_state
        if not DaraCore.is_null(request.session_duration):
            query['SessionDuration'] = request.session_duration
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAccessConfiguration',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAccessConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_access_configuration_with_options_async(
        self,
        request: main_models.CreateAccessConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAccessConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_configuration_name):
            query['AccessConfigurationName'] = request.access_configuration_name
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.relay_state):
            query['RelayState'] = request.relay_state
        if not DaraCore.is_null(request.session_duration):
            query['SessionDuration'] = request.session_duration
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAccessConfiguration',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAccessConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_access_configuration(
        self,
        request: main_models.CreateAccessConfigurationRequest,
    ) -> main_models.CreateAccessConfigurationResponse:
        runtime = RuntimeOptions()
        return self.create_access_configuration_with_options(request, runtime)

    async def create_access_configuration_async(
        self,
        request: main_models.CreateAccessConfigurationRequest,
    ) -> main_models.CreateAccessConfigurationResponse:
        runtime = RuntimeOptions()
        return await self.create_access_configuration_with_options_async(request, runtime)

    def create_directory_with_options(
        self,
        request: main_models.CreateDirectoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDirectoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_name):
            query['DirectoryName'] = request.directory_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDirectory',
            version = '2021-05-15',
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
        request: main_models.CreateDirectoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDirectoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_name):
            query['DirectoryName'] = request.directory_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDirectory',
            version = '2021-05-15',
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

    def create_group_with_options(
        self,
        request: main_models.CreateGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateGroup',
            version = '2021-05-15',
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
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateGroup',
            version = '2021-05-15',
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

    def create_scimserver_credential_with_options(
        self,
        request: main_models.CreateSCIMServerCredentialRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSCIMServerCredentialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSCIMServerCredential',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSCIMServerCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_scimserver_credential_with_options_async(
        self,
        request: main_models.CreateSCIMServerCredentialRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSCIMServerCredentialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSCIMServerCredential',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSCIMServerCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_scimserver_credential(
        self,
        request: main_models.CreateSCIMServerCredentialRequest,
    ) -> main_models.CreateSCIMServerCredentialResponse:
        runtime = RuntimeOptions()
        return self.create_scimserver_credential_with_options(request, runtime)

    async def create_scimserver_credential_async(
        self,
        request: main_models.CreateSCIMServerCredentialRequest,
    ) -> main_models.CreateSCIMServerCredentialResponse:
        runtime = RuntimeOptions()
        return await self.create_scimserver_credential_with_options_async(request, runtime)

    def create_user_with_options(
        self,
        request: main_models.CreateUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.display_name):
            query['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.first_name):
            query['FirstName'] = request.first_name
        if not DaraCore.is_null(request.last_name):
            query['LastName'] = request.last_name
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateUser',
            version = '2021-05-15',
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
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.display_name):
            query['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.first_name):
            query['FirstName'] = request.first_name
        if not DaraCore.is_null(request.last_name):
            query['LastName'] = request.last_name
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateUser',
            version = '2021-05-15',
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

    def create_user_provisioning_with_options(
        self,
        request: main_models.CreateUserProvisioningRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUserProvisioningResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.deletion_strategy):
            query['DeletionStrategy'] = request.deletion_strategy
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.duplication_strategy):
            query['DuplicationStrategy'] = request.duplication_strategy
        if not DaraCore.is_null(request.principal_id):
            query['PrincipalId'] = request.principal_id
        if not DaraCore.is_null(request.principal_type):
            query['PrincipalType'] = request.principal_type
        if not DaraCore.is_null(request.target_id):
            query['TargetId'] = request.target_id
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateUserProvisioning',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUserProvisioningResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_user_provisioning_with_options_async(
        self,
        request: main_models.CreateUserProvisioningRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUserProvisioningResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.deletion_strategy):
            query['DeletionStrategy'] = request.deletion_strategy
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.duplication_strategy):
            query['DuplicationStrategy'] = request.duplication_strategy
        if not DaraCore.is_null(request.principal_id):
            query['PrincipalId'] = request.principal_id
        if not DaraCore.is_null(request.principal_type):
            query['PrincipalType'] = request.principal_type
        if not DaraCore.is_null(request.target_id):
            query['TargetId'] = request.target_id
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateUserProvisioning',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUserProvisioningResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_user_provisioning(
        self,
        request: main_models.CreateUserProvisioningRequest,
    ) -> main_models.CreateUserProvisioningResponse:
        runtime = RuntimeOptions()
        return self.create_user_provisioning_with_options(request, runtime)

    async def create_user_provisioning_async(
        self,
        request: main_models.CreateUserProvisioningRequest,
    ) -> main_models.CreateUserProvisioningResponse:
        runtime = RuntimeOptions()
        return await self.create_user_provisioning_with_options_async(request, runtime)

    def delete_access_assignment_with_options(
        self,
        request: main_models.DeleteAccessAssignmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAccessAssignmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not DaraCore.is_null(request.deprovision_strategy):
            query['DeprovisionStrategy'] = request.deprovision_strategy
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.origin_target_id):
            query['OriginTargetId'] = request.origin_target_id
        if not DaraCore.is_null(request.principal_id):
            query['PrincipalId'] = request.principal_id
        if not DaraCore.is_null(request.principal_type):
            query['PrincipalType'] = request.principal_type
        if not DaraCore.is_null(request.target_id):
            query['TargetId'] = request.target_id
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAccessAssignment',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAccessAssignmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_access_assignment_with_options_async(
        self,
        request: main_models.DeleteAccessAssignmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAccessAssignmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not DaraCore.is_null(request.deprovision_strategy):
            query['DeprovisionStrategy'] = request.deprovision_strategy
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.origin_target_id):
            query['OriginTargetId'] = request.origin_target_id
        if not DaraCore.is_null(request.principal_id):
            query['PrincipalId'] = request.principal_id
        if not DaraCore.is_null(request.principal_type):
            query['PrincipalType'] = request.principal_type
        if not DaraCore.is_null(request.target_id):
            query['TargetId'] = request.target_id
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAccessAssignment',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAccessAssignmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_access_assignment(
        self,
        request: main_models.DeleteAccessAssignmentRequest,
    ) -> main_models.DeleteAccessAssignmentResponse:
        runtime = RuntimeOptions()
        return self.delete_access_assignment_with_options(request, runtime)

    async def delete_access_assignment_async(
        self,
        request: main_models.DeleteAccessAssignmentRequest,
    ) -> main_models.DeleteAccessAssignmentResponse:
        runtime = RuntimeOptions()
        return await self.delete_access_assignment_with_options_async(request, runtime)

    def delete_access_configuration_with_options(
        self,
        request: main_models.DeleteAccessConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAccessConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.force_remove_permission_policies):
            query['ForceRemovePermissionPolicies'] = request.force_remove_permission_policies
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAccessConfiguration',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAccessConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_access_configuration_with_options_async(
        self,
        request: main_models.DeleteAccessConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAccessConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.force_remove_permission_policies):
            query['ForceRemovePermissionPolicies'] = request.force_remove_permission_policies
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAccessConfiguration',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAccessConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_access_configuration(
        self,
        request: main_models.DeleteAccessConfigurationRequest,
    ) -> main_models.DeleteAccessConfigurationResponse:
        runtime = RuntimeOptions()
        return self.delete_access_configuration_with_options(request, runtime)

    async def delete_access_configuration_async(
        self,
        request: main_models.DeleteAccessConfigurationRequest,
    ) -> main_models.DeleteAccessConfigurationResponse:
        runtime = RuntimeOptions()
        return await self.delete_access_configuration_with_options_async(request, runtime)

    def delete_directory_with_options(
        self,
        request: main_models.DeleteDirectoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDirectoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDirectory',
            version = '2021-05-15',
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
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDirectory',
            version = '2021-05-15',
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

    def delete_group_with_options(
        self,
        request: main_models.DeleteGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGroup',
            version = '2021-05-15',
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
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGroup',
            version = '2021-05-15',
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

    def delete_mfadevice_for_user_with_options(
        self,
        request: main_models.DeleteMFADeviceForUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMFADeviceForUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.mfadevice_id):
            query['MFADeviceId'] = request.mfadevice_id
        if not DaraCore.is_null(request.mfa_type):
            query['MfaType'] = request.mfa_type
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMFADeviceForUser',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMFADeviceForUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_mfadevice_for_user_with_options_async(
        self,
        request: main_models.DeleteMFADeviceForUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMFADeviceForUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.mfadevice_id):
            query['MFADeviceId'] = request.mfadevice_id
        if not DaraCore.is_null(request.mfa_type):
            query['MfaType'] = request.mfa_type
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMFADeviceForUser',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMFADeviceForUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_mfadevice_for_user(
        self,
        request: main_models.DeleteMFADeviceForUserRequest,
    ) -> main_models.DeleteMFADeviceForUserResponse:
        runtime = RuntimeOptions()
        return self.delete_mfadevice_for_user_with_options(request, runtime)

    async def delete_mfadevice_for_user_async(
        self,
        request: main_models.DeleteMFADeviceForUserRequest,
    ) -> main_models.DeleteMFADeviceForUserResponse:
        runtime = RuntimeOptions()
        return await self.delete_mfadevice_for_user_with_options_async(request, runtime)

    def delete_scimserver_credential_with_options(
        self,
        request: main_models.DeleteSCIMServerCredentialRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSCIMServerCredentialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.credential_id):
            query['CredentialId'] = request.credential_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSCIMServerCredential',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSCIMServerCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_scimserver_credential_with_options_async(
        self,
        request: main_models.DeleteSCIMServerCredentialRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSCIMServerCredentialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.credential_id):
            query['CredentialId'] = request.credential_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSCIMServerCredential',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSCIMServerCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_scimserver_credential(
        self,
        request: main_models.DeleteSCIMServerCredentialRequest,
    ) -> main_models.DeleteSCIMServerCredentialResponse:
        runtime = RuntimeOptions()
        return self.delete_scimserver_credential_with_options(request, runtime)

    async def delete_scimserver_credential_async(
        self,
        request: main_models.DeleteSCIMServerCredentialRequest,
    ) -> main_models.DeleteSCIMServerCredentialResponse:
        runtime = RuntimeOptions()
        return await self.delete_scimserver_credential_with_options_async(request, runtime)

    def delete_user_with_options(
        self,
        request: main_models.DeleteUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUser',
            version = '2021-05-15',
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
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUser',
            version = '2021-05-15',
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

    def delete_user_provisioning_with_options(
        self,
        request: main_models.DeleteUserProvisioningRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserProvisioningResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.deletion_strategy):
            query['DeletionStrategy'] = request.deletion_strategy
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.user_provisioning_id):
            query['UserProvisioningId'] = request.user_provisioning_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUserProvisioning',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUserProvisioningResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_provisioning_with_options_async(
        self,
        request: main_models.DeleteUserProvisioningRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserProvisioningResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.deletion_strategy):
            query['DeletionStrategy'] = request.deletion_strategy
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.user_provisioning_id):
            query['UserProvisioningId'] = request.user_provisioning_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUserProvisioning',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUserProvisioningResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user_provisioning(
        self,
        request: main_models.DeleteUserProvisioningRequest,
    ) -> main_models.DeleteUserProvisioningResponse:
        runtime = RuntimeOptions()
        return self.delete_user_provisioning_with_options(request, runtime)

    async def delete_user_provisioning_async(
        self,
        request: main_models.DeleteUserProvisioningRequest,
    ) -> main_models.DeleteUserProvisioningResponse:
        runtime = RuntimeOptions()
        return await self.delete_user_provisioning_with_options_async(request, runtime)

    def delete_user_provisioning_event_with_options(
        self,
        request: main_models.DeleteUserProvisioningEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserProvisioningEventResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.event_id):
            query['EventId'] = request.event_id
        if not DaraCore.is_null(request.user_provisioning_id):
            query['UserProvisioningId'] = request.user_provisioning_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUserProvisioningEvent',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUserProvisioningEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_provisioning_event_with_options_async(
        self,
        request: main_models.DeleteUserProvisioningEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserProvisioningEventResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.event_id):
            query['EventId'] = request.event_id
        if not DaraCore.is_null(request.user_provisioning_id):
            query['UserProvisioningId'] = request.user_provisioning_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUserProvisioningEvent',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUserProvisioningEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user_provisioning_event(
        self,
        request: main_models.DeleteUserProvisioningEventRequest,
    ) -> main_models.DeleteUserProvisioningEventResponse:
        runtime = RuntimeOptions()
        return self.delete_user_provisioning_event_with_options(request, runtime)

    async def delete_user_provisioning_event_async(
        self,
        request: main_models.DeleteUserProvisioningEventRequest,
    ) -> main_models.DeleteUserProvisioningEventResponse:
        runtime = RuntimeOptions()
        return await self.delete_user_provisioning_event_with_options_async(request, runtime)

    def deprovision_access_configuration_with_options(
        self,
        request: main_models.DeprovisionAccessConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeprovisionAccessConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.origin_target_id):
            query['OriginTargetId'] = request.origin_target_id
        if not DaraCore.is_null(request.target_id):
            query['TargetId'] = request.target_id
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeprovisionAccessConfiguration',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeprovisionAccessConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def deprovision_access_configuration_with_options_async(
        self,
        request: main_models.DeprovisionAccessConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeprovisionAccessConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.origin_target_id):
            query['OriginTargetId'] = request.origin_target_id
        if not DaraCore.is_null(request.target_id):
            query['TargetId'] = request.target_id
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeprovisionAccessConfiguration',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeprovisionAccessConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deprovision_access_configuration(
        self,
        request: main_models.DeprovisionAccessConfigurationRequest,
    ) -> main_models.DeprovisionAccessConfigurationResponse:
        runtime = RuntimeOptions()
        return self.deprovision_access_configuration_with_options(request, runtime)

    async def deprovision_access_configuration_async(
        self,
        request: main_models.DeprovisionAccessConfigurationRequest,
    ) -> main_models.DeprovisionAccessConfigurationResponse:
        runtime = RuntimeOptions()
        return await self.deprovision_access_configuration_with_options_async(request, runtime)

    def disable_delegate_account_with_options(
        self,
        request: main_models.DisableDelegateAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableDelegateAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableDelegateAccount',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableDelegateAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_delegate_account_with_options_async(
        self,
        request: main_models.DisableDelegateAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableDelegateAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableDelegateAccount',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableDelegateAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_delegate_account(
        self,
        request: main_models.DisableDelegateAccountRequest,
    ) -> main_models.DisableDelegateAccountResponse:
        runtime = RuntimeOptions()
        return self.disable_delegate_account_with_options(request, runtime)

    async def disable_delegate_account_async(
        self,
        request: main_models.DisableDelegateAccountRequest,
    ) -> main_models.DisableDelegateAccountResponse:
        runtime = RuntimeOptions()
        return await self.disable_delegate_account_with_options_async(request, runtime)

    def disable_service_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DisableServiceResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DisableService',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_service_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DisableServiceResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DisableService',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_service(self) -> main_models.DisableServiceResponse:
        runtime = RuntimeOptions()
        return self.disable_service_with_options(runtime)

    async def disable_service_async(self) -> main_models.DisableServiceResponse:
        runtime = RuntimeOptions()
        return await self.disable_service_with_options_async(runtime)

    def enable_delegate_account_with_options(
        self,
        request: main_models.EnableDelegateAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableDelegateAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableDelegateAccount',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableDelegateAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_delegate_account_with_options_async(
        self,
        request: main_models.EnableDelegateAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableDelegateAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableDelegateAccount',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableDelegateAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_delegate_account(
        self,
        request: main_models.EnableDelegateAccountRequest,
    ) -> main_models.EnableDelegateAccountResponse:
        runtime = RuntimeOptions()
        return self.enable_delegate_account_with_options(request, runtime)

    async def enable_delegate_account_async(
        self,
        request: main_models.EnableDelegateAccountRequest,
    ) -> main_models.EnableDelegateAccountResponse:
        runtime = RuntimeOptions()
        return await self.enable_delegate_account_with_options_async(request, runtime)

    def enable_service_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.EnableServiceResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'EnableService',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_service_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.EnableServiceResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'EnableService',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_service(self) -> main_models.EnableServiceResponse:
        runtime = RuntimeOptions()
        return self.enable_service_with_options(runtime)

    async def enable_service_async(self) -> main_models.EnableServiceResponse:
        runtime = RuntimeOptions()
        return await self.enable_service_with_options_async(runtime)

    def get_access_configuration_with_options(
        self,
        request: main_models.GetAccessConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAccessConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAccessConfiguration',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAccessConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_access_configuration_with_options_async(
        self,
        request: main_models.GetAccessConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAccessConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAccessConfiguration',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAccessConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_access_configuration(
        self,
        request: main_models.GetAccessConfigurationRequest,
    ) -> main_models.GetAccessConfigurationResponse:
        runtime = RuntimeOptions()
        return self.get_access_configuration_with_options(request, runtime)

    async def get_access_configuration_async(
        self,
        request: main_models.GetAccessConfigurationRequest,
    ) -> main_models.GetAccessConfigurationResponse:
        runtime = RuntimeOptions()
        return await self.get_access_configuration_with_options_async(request, runtime)

    def get_directory_with_options(
        self,
        request: main_models.GetDirectoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDirectoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDirectory',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_directory_with_options_async(
        self,
        request: main_models.GetDirectoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDirectoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDirectory',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_directory(
        self,
        request: main_models.GetDirectoryRequest,
    ) -> main_models.GetDirectoryResponse:
        runtime = RuntimeOptions()
        return self.get_directory_with_options(request, runtime)

    async def get_directory_async(
        self,
        request: main_models.GetDirectoryRequest,
    ) -> main_models.GetDirectoryResponse:
        runtime = RuntimeOptions()
        return await self.get_directory_with_options_async(request, runtime)

    def get_directory_samlservice_provider_info_with_options(
        self,
        request: main_models.GetDirectorySAMLServiceProviderInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDirectorySAMLServiceProviderInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDirectorySAMLServiceProviderInfo',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDirectorySAMLServiceProviderInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_directory_samlservice_provider_info_with_options_async(
        self,
        request: main_models.GetDirectorySAMLServiceProviderInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDirectorySAMLServiceProviderInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDirectorySAMLServiceProviderInfo',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDirectorySAMLServiceProviderInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_directory_samlservice_provider_info(
        self,
        request: main_models.GetDirectorySAMLServiceProviderInfoRequest,
    ) -> main_models.GetDirectorySAMLServiceProviderInfoResponse:
        runtime = RuntimeOptions()
        return self.get_directory_samlservice_provider_info_with_options(request, runtime)

    async def get_directory_samlservice_provider_info_async(
        self,
        request: main_models.GetDirectorySAMLServiceProviderInfoRequest,
    ) -> main_models.GetDirectorySAMLServiceProviderInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_directory_samlservice_provider_info_with_options_async(request, runtime)

    def get_directory_statistics_with_options(
        self,
        request: main_models.GetDirectoryStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDirectoryStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDirectoryStatistics',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDirectoryStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_directory_statistics_with_options_async(
        self,
        request: main_models.GetDirectoryStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDirectoryStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDirectoryStatistics',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDirectoryStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_directory_statistics(
        self,
        request: main_models.GetDirectoryStatisticsRequest,
    ) -> main_models.GetDirectoryStatisticsResponse:
        runtime = RuntimeOptions()
        return self.get_directory_statistics_with_options(request, runtime)

    async def get_directory_statistics_async(
        self,
        request: main_models.GetDirectoryStatisticsRequest,
    ) -> main_models.GetDirectoryStatisticsResponse:
        runtime = RuntimeOptions()
        return await self.get_directory_statistics_with_options_async(request, runtime)

    def get_external_samlidentity_provider_with_options(
        self,
        request: main_models.GetExternalSAMLIdentityProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetExternalSAMLIdentityProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetExternalSAMLIdentityProvider',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetExternalSAMLIdentityProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_external_samlidentity_provider_with_options_async(
        self,
        request: main_models.GetExternalSAMLIdentityProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetExternalSAMLIdentityProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetExternalSAMLIdentityProvider',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetExternalSAMLIdentityProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_external_samlidentity_provider(
        self,
        request: main_models.GetExternalSAMLIdentityProviderRequest,
    ) -> main_models.GetExternalSAMLIdentityProviderResponse:
        runtime = RuntimeOptions()
        return self.get_external_samlidentity_provider_with_options(request, runtime)

    async def get_external_samlidentity_provider_async(
        self,
        request: main_models.GetExternalSAMLIdentityProviderRequest,
    ) -> main_models.GetExternalSAMLIdentityProviderResponse:
        runtime = RuntimeOptions()
        return await self.get_external_samlidentity_provider_with_options_async(request, runtime)

    def get_group_with_options(
        self,
        request: main_models.GetGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetGroup',
            version = '2021-05-15',
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
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetGroup',
            version = '2021-05-15',
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

    def get_login_preference_with_options(
        self,
        request: main_models.GetLoginPreferenceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLoginPreferenceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLoginPreference',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLoginPreferenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_login_preference_with_options_async(
        self,
        request: main_models.GetLoginPreferenceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLoginPreferenceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLoginPreference',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLoginPreferenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_login_preference(
        self,
        request: main_models.GetLoginPreferenceRequest,
    ) -> main_models.GetLoginPreferenceResponse:
        runtime = RuntimeOptions()
        return self.get_login_preference_with_options(request, runtime)

    async def get_login_preference_async(
        self,
        request: main_models.GetLoginPreferenceRequest,
    ) -> main_models.GetLoginPreferenceResponse:
        runtime = RuntimeOptions()
        return await self.get_login_preference_with_options_async(request, runtime)

    def get_mfaauthentication_setting_info_with_options(
        self,
        request: main_models.GetMFAAuthenticationSettingInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMFAAuthenticationSettingInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMFAAuthenticationSettingInfo',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMFAAuthenticationSettingInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mfaauthentication_setting_info_with_options_async(
        self,
        request: main_models.GetMFAAuthenticationSettingInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMFAAuthenticationSettingInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMFAAuthenticationSettingInfo',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMFAAuthenticationSettingInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mfaauthentication_setting_info(
        self,
        request: main_models.GetMFAAuthenticationSettingInfoRequest,
    ) -> main_models.GetMFAAuthenticationSettingInfoResponse:
        runtime = RuntimeOptions()
        return self.get_mfaauthentication_setting_info_with_options(request, runtime)

    async def get_mfaauthentication_setting_info_async(
        self,
        request: main_models.GetMFAAuthenticationSettingInfoRequest,
    ) -> main_models.GetMFAAuthenticationSettingInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_mfaauthentication_setting_info_with_options_async(request, runtime)

    def get_mfaauthentication_settings_with_options(
        self,
        request: main_models.GetMFAAuthenticationSettingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMFAAuthenticationSettingsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMFAAuthenticationSettings',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMFAAuthenticationSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mfaauthentication_settings_with_options_async(
        self,
        request: main_models.GetMFAAuthenticationSettingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMFAAuthenticationSettingsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMFAAuthenticationSettings',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMFAAuthenticationSettingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mfaauthentication_settings(
        self,
        request: main_models.GetMFAAuthenticationSettingsRequest,
    ) -> main_models.GetMFAAuthenticationSettingsResponse:
        runtime = RuntimeOptions()
        return self.get_mfaauthentication_settings_with_options(request, runtime)

    async def get_mfaauthentication_settings_async(
        self,
        request: main_models.GetMFAAuthenticationSettingsRequest,
    ) -> main_models.GetMFAAuthenticationSettingsResponse:
        runtime = RuntimeOptions()
        return await self.get_mfaauthentication_settings_with_options_async(request, runtime)

    def get_mfaauthentication_status_with_options(
        self,
        request: main_models.GetMFAAuthenticationStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMFAAuthenticationStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMFAAuthenticationStatus',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMFAAuthenticationStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mfaauthentication_status_with_options_async(
        self,
        request: main_models.GetMFAAuthenticationStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMFAAuthenticationStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMFAAuthenticationStatus',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMFAAuthenticationStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mfaauthentication_status(
        self,
        request: main_models.GetMFAAuthenticationStatusRequest,
    ) -> main_models.GetMFAAuthenticationStatusResponse:
        runtime = RuntimeOptions()
        return self.get_mfaauthentication_status_with_options(request, runtime)

    async def get_mfaauthentication_status_async(
        self,
        request: main_models.GetMFAAuthenticationStatusRequest,
    ) -> main_models.GetMFAAuthenticationStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_mfaauthentication_status_with_options_async(request, runtime)

    def get_password_policy_with_options(
        self,
        request: main_models.GetPasswordPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPasswordPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPasswordPolicy',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPasswordPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_password_policy_with_options_async(
        self,
        request: main_models.GetPasswordPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPasswordPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPasswordPolicy',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPasswordPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_password_policy(
        self,
        request: main_models.GetPasswordPolicyRequest,
    ) -> main_models.GetPasswordPolicyResponse:
        runtime = RuntimeOptions()
        return self.get_password_policy_with_options(request, runtime)

    async def get_password_policy_async(
        self,
        request: main_models.GetPasswordPolicyRequest,
    ) -> main_models.GetPasswordPolicyResponse:
        runtime = RuntimeOptions()
        return await self.get_password_policy_with_options_async(request, runtime)

    def get_scimsynchronization_status_with_options(
        self,
        request: main_models.GetSCIMSynchronizationStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSCIMSynchronizationStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSCIMSynchronizationStatus',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSCIMSynchronizationStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_scimsynchronization_status_with_options_async(
        self,
        request: main_models.GetSCIMSynchronizationStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSCIMSynchronizationStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSCIMSynchronizationStatus',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSCIMSynchronizationStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_scimsynchronization_status(
        self,
        request: main_models.GetSCIMSynchronizationStatusRequest,
    ) -> main_models.GetSCIMSynchronizationStatusResponse:
        runtime = RuntimeOptions()
        return self.get_scimsynchronization_status_with_options(request, runtime)

    async def get_scimsynchronization_status_async(
        self,
        request: main_models.GetSCIMSynchronizationStatusRequest,
    ) -> main_models.GetSCIMSynchronizationStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_scimsynchronization_status_with_options_async(request, runtime)

    def get_service_status_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceStatusResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetServiceStatus',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_status_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceStatusResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetServiceStatus',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_status(self) -> main_models.GetServiceStatusResponse:
        runtime = RuntimeOptions()
        return self.get_service_status_with_options(runtime)

    async def get_service_status_async(self) -> main_models.GetServiceStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_service_status_with_options_async(runtime)

    def get_task_with_options(
        self,
        request: main_models.GetTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTask',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_with_options_async(
        self,
        request: main_models.GetTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTask',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task(
        self,
        request: main_models.GetTaskRequest,
    ) -> main_models.GetTaskResponse:
        runtime = RuntimeOptions()
        return self.get_task_with_options(request, runtime)

    async def get_task_async(
        self,
        request: main_models.GetTaskRequest,
    ) -> main_models.GetTaskResponse:
        runtime = RuntimeOptions()
        return await self.get_task_with_options_async(request, runtime)

    def get_task_status_with_options(
        self,
        request: main_models.GetTaskStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTaskStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTaskStatus',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_status_with_options_async(
        self,
        request: main_models.GetTaskStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTaskStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTaskStatus',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTaskStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task_status(
        self,
        request: main_models.GetTaskStatusRequest,
    ) -> main_models.GetTaskStatusResponse:
        runtime = RuntimeOptions()
        return self.get_task_status_with_options(request, runtime)

    async def get_task_status_async(
        self,
        request: main_models.GetTaskStatusRequest,
    ) -> main_models.GetTaskStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_task_status_with_options_async(request, runtime)

    def get_user_with_options(
        self,
        request: main_models.GetUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUser',
            version = '2021-05-15',
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
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUser',
            version = '2021-05-15',
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

    def get_user_id_with_options(
        self,
        tmp_req: main_models.GetUserIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserIdResponse:
        tmp_req.validate()
        request = main_models.GetUserIdShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.external_id):
            request.external_id_shrink = Utils.array_to_string_with_specified_style(tmp_req.external_id, 'ExternalId', 'json')
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.external_id_shrink):
            query['ExternalId'] = request.external_id_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserId',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_id_with_options_async(
        self,
        tmp_req: main_models.GetUserIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserIdResponse:
        tmp_req.validate()
        request = main_models.GetUserIdShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.external_id):
            request.external_id_shrink = Utils.array_to_string_with_specified_style(tmp_req.external_id, 'ExternalId', 'json')
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.external_id_shrink):
            query['ExternalId'] = request.external_id_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserId',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_id(
        self,
        request: main_models.GetUserIdRequest,
    ) -> main_models.GetUserIdResponse:
        runtime = RuntimeOptions()
        return self.get_user_id_with_options(request, runtime)

    async def get_user_id_async(
        self,
        request: main_models.GetUserIdRequest,
    ) -> main_models.GetUserIdResponse:
        runtime = RuntimeOptions()
        return await self.get_user_id_with_options_async(request, runtime)

    def get_user_mfaauthentication_settings_with_options(
        self,
        request: main_models.GetUserMFAAuthenticationSettingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserMFAAuthenticationSettingsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserMFAAuthenticationSettings',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserMFAAuthenticationSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_mfaauthentication_settings_with_options_async(
        self,
        request: main_models.GetUserMFAAuthenticationSettingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserMFAAuthenticationSettingsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserMFAAuthenticationSettings',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserMFAAuthenticationSettingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_mfaauthentication_settings(
        self,
        request: main_models.GetUserMFAAuthenticationSettingsRequest,
    ) -> main_models.GetUserMFAAuthenticationSettingsResponse:
        runtime = RuntimeOptions()
        return self.get_user_mfaauthentication_settings_with_options(request, runtime)

    async def get_user_mfaauthentication_settings_async(
        self,
        request: main_models.GetUserMFAAuthenticationSettingsRequest,
    ) -> main_models.GetUserMFAAuthenticationSettingsResponse:
        runtime = RuntimeOptions()
        return await self.get_user_mfaauthentication_settings_with_options_async(request, runtime)

    def get_user_provisioning_with_options(
        self,
        request: main_models.GetUserProvisioningRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserProvisioningResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.user_provisioning_id):
            query['UserProvisioningId'] = request.user_provisioning_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserProvisioning',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserProvisioningResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_provisioning_with_options_async(
        self,
        request: main_models.GetUserProvisioningRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserProvisioningResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.user_provisioning_id):
            query['UserProvisioningId'] = request.user_provisioning_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserProvisioning',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserProvisioningResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_provisioning(
        self,
        request: main_models.GetUserProvisioningRequest,
    ) -> main_models.GetUserProvisioningResponse:
        runtime = RuntimeOptions()
        return self.get_user_provisioning_with_options(request, runtime)

    async def get_user_provisioning_async(
        self,
        request: main_models.GetUserProvisioningRequest,
    ) -> main_models.GetUserProvisioningResponse:
        runtime = RuntimeOptions()
        return await self.get_user_provisioning_with_options_async(request, runtime)

    def get_user_provisioning_configuration_with_options(
        self,
        request: main_models.GetUserProvisioningConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserProvisioningConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserProvisioningConfiguration',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserProvisioningConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_provisioning_configuration_with_options_async(
        self,
        request: main_models.GetUserProvisioningConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserProvisioningConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserProvisioningConfiguration',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserProvisioningConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_provisioning_configuration(
        self,
        request: main_models.GetUserProvisioningConfigurationRequest,
    ) -> main_models.GetUserProvisioningConfigurationResponse:
        runtime = RuntimeOptions()
        return self.get_user_provisioning_configuration_with_options(request, runtime)

    async def get_user_provisioning_configuration_async(
        self,
        request: main_models.GetUserProvisioningConfigurationRequest,
    ) -> main_models.GetUserProvisioningConfigurationResponse:
        runtime = RuntimeOptions()
        return await self.get_user_provisioning_configuration_with_options_async(request, runtime)

    def get_user_provisioning_event_with_options(
        self,
        request: main_models.GetUserProvisioningEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserProvisioningEventResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.event_id):
            query['EventId'] = request.event_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserProvisioningEvent',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserProvisioningEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_provisioning_event_with_options_async(
        self,
        request: main_models.GetUserProvisioningEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserProvisioningEventResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.event_id):
            query['EventId'] = request.event_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserProvisioningEvent',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserProvisioningEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_provisioning_event(
        self,
        request: main_models.GetUserProvisioningEventRequest,
    ) -> main_models.GetUserProvisioningEventResponse:
        runtime = RuntimeOptions()
        return self.get_user_provisioning_event_with_options(request, runtime)

    async def get_user_provisioning_event_async(
        self,
        request: main_models.GetUserProvisioningEventRequest,
    ) -> main_models.GetUserProvisioningEventResponse:
        runtime = RuntimeOptions()
        return await self.get_user_provisioning_event_with_options_async(request, runtime)

    def get_user_provisioning_rd_account_statistics_with_options(
        self,
        request: main_models.GetUserProvisioningRdAccountStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserProvisioningRdAccountStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.rd_member_id):
            query['RdMemberId'] = request.rd_member_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserProvisioningRdAccountStatistics',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserProvisioningRdAccountStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_provisioning_rd_account_statistics_with_options_async(
        self,
        request: main_models.GetUserProvisioningRdAccountStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserProvisioningRdAccountStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.rd_member_id):
            query['RdMemberId'] = request.rd_member_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserProvisioningRdAccountStatistics',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserProvisioningRdAccountStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_provisioning_rd_account_statistics(
        self,
        request: main_models.GetUserProvisioningRdAccountStatisticsRequest,
    ) -> main_models.GetUserProvisioningRdAccountStatisticsResponse:
        runtime = RuntimeOptions()
        return self.get_user_provisioning_rd_account_statistics_with_options(request, runtime)

    async def get_user_provisioning_rd_account_statistics_async(
        self,
        request: main_models.GetUserProvisioningRdAccountStatisticsRequest,
    ) -> main_models.GetUserProvisioningRdAccountStatisticsResponse:
        runtime = RuntimeOptions()
        return await self.get_user_provisioning_rd_account_statistics_with_options_async(request, runtime)

    def get_user_provisioning_statistics_with_options(
        self,
        request: main_models.GetUserProvisioningStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserProvisioningStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.user_provisioning_id):
            query['UserProvisioningId'] = request.user_provisioning_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserProvisioningStatistics',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserProvisioningStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_provisioning_statistics_with_options_async(
        self,
        request: main_models.GetUserProvisioningStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserProvisioningStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.user_provisioning_id):
            query['UserProvisioningId'] = request.user_provisioning_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserProvisioningStatistics',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserProvisioningStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_provisioning_statistics(
        self,
        request: main_models.GetUserProvisioningStatisticsRequest,
    ) -> main_models.GetUserProvisioningStatisticsResponse:
        runtime = RuntimeOptions()
        return self.get_user_provisioning_statistics_with_options(request, runtime)

    async def get_user_provisioning_statistics_async(
        self,
        request: main_models.GetUserProvisioningStatisticsRequest,
    ) -> main_models.GetUserProvisioningStatisticsResponse:
        runtime = RuntimeOptions()
        return await self.get_user_provisioning_statistics_with_options_async(request, runtime)

    def list_access_assignments_with_options(
        self,
        request: main_models.ListAccessAssignmentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAccessAssignmentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.origin_target_id):
            query['OriginTargetId'] = request.origin_target_id
        if not DaraCore.is_null(request.principal_id):
            query['PrincipalId'] = request.principal_id
        if not DaraCore.is_null(request.principal_type):
            query['PrincipalType'] = request.principal_type
        if not DaraCore.is_null(request.target_id):
            query['TargetId'] = request.target_id
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAccessAssignments',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAccessAssignmentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_access_assignments_with_options_async(
        self,
        request: main_models.ListAccessAssignmentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAccessAssignmentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.origin_target_id):
            query['OriginTargetId'] = request.origin_target_id
        if not DaraCore.is_null(request.principal_id):
            query['PrincipalId'] = request.principal_id
        if not DaraCore.is_null(request.principal_type):
            query['PrincipalType'] = request.principal_type
        if not DaraCore.is_null(request.target_id):
            query['TargetId'] = request.target_id
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAccessAssignments',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAccessAssignmentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_access_assignments(
        self,
        request: main_models.ListAccessAssignmentsRequest,
    ) -> main_models.ListAccessAssignmentsResponse:
        runtime = RuntimeOptions()
        return self.list_access_assignments_with_options(request, runtime)

    async def list_access_assignments_async(
        self,
        request: main_models.ListAccessAssignmentsRequest,
    ) -> main_models.ListAccessAssignmentsResponse:
        runtime = RuntimeOptions()
        return await self.list_access_assignments_with_options_async(request, runtime)

    def list_access_configuration_provisionings_with_options(
        self,
        request: main_models.ListAccessConfigurationProvisioningsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAccessConfigurationProvisioningsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.origin_target_id):
            query['OriginTargetId'] = request.origin_target_id
        if not DaraCore.is_null(request.provisioning_status):
            query['ProvisioningStatus'] = request.provisioning_status
        if not DaraCore.is_null(request.target_id):
            query['TargetId'] = request.target_id
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAccessConfigurationProvisionings',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAccessConfigurationProvisioningsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_access_configuration_provisionings_with_options_async(
        self,
        request: main_models.ListAccessConfigurationProvisioningsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAccessConfigurationProvisioningsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.origin_target_id):
            query['OriginTargetId'] = request.origin_target_id
        if not DaraCore.is_null(request.provisioning_status):
            query['ProvisioningStatus'] = request.provisioning_status
        if not DaraCore.is_null(request.target_id):
            query['TargetId'] = request.target_id
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAccessConfigurationProvisionings',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAccessConfigurationProvisioningsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_access_configuration_provisionings(
        self,
        request: main_models.ListAccessConfigurationProvisioningsRequest,
    ) -> main_models.ListAccessConfigurationProvisioningsResponse:
        runtime = RuntimeOptions()
        return self.list_access_configuration_provisionings_with_options(request, runtime)

    async def list_access_configuration_provisionings_async(
        self,
        request: main_models.ListAccessConfigurationProvisioningsRequest,
    ) -> main_models.ListAccessConfigurationProvisioningsResponse:
        runtime = RuntimeOptions()
        return await self.list_access_configuration_provisionings_with_options_async(request, runtime)

    def list_access_configurations_with_options(
        self,
        request: main_models.ListAccessConfigurationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAccessConfigurationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.status_notifications):
            query['StatusNotifications'] = request.status_notifications
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAccessConfigurations',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAccessConfigurationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_access_configurations_with_options_async(
        self,
        request: main_models.ListAccessConfigurationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAccessConfigurationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.status_notifications):
            query['StatusNotifications'] = request.status_notifications
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAccessConfigurations',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAccessConfigurationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_access_configurations(
        self,
        request: main_models.ListAccessConfigurationsRequest,
    ) -> main_models.ListAccessConfigurationsResponse:
        runtime = RuntimeOptions()
        return self.list_access_configurations_with_options(request, runtime)

    async def list_access_configurations_async(
        self,
        request: main_models.ListAccessConfigurationsRequest,
    ) -> main_models.ListAccessConfigurationsResponse:
        runtime = RuntimeOptions()
        return await self.list_access_configurations_with_options_async(request, runtime)

    def list_directories_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListDirectoriesResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListDirectories',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDirectoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_directories_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListDirectoriesResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListDirectories',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDirectoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_directories(self) -> main_models.ListDirectoriesResponse:
        runtime = RuntimeOptions()
        return self.list_directories_with_options(runtime)

    async def list_directories_async(self) -> main_models.ListDirectoriesResponse:
        runtime = RuntimeOptions()
        return await self.list_directories_with_options_async(runtime)

    def list_external_samlid_pcertificates_with_options(
        self,
        request: main_models.ListExternalSAMLIdPCertificatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListExternalSAMLIdPCertificatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExternalSAMLIdPCertificates',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExternalSAMLIdPCertificatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_external_samlid_pcertificates_with_options_async(
        self,
        request: main_models.ListExternalSAMLIdPCertificatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListExternalSAMLIdPCertificatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExternalSAMLIdPCertificates',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExternalSAMLIdPCertificatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_external_samlid_pcertificates(
        self,
        request: main_models.ListExternalSAMLIdPCertificatesRequest,
    ) -> main_models.ListExternalSAMLIdPCertificatesResponse:
        runtime = RuntimeOptions()
        return self.list_external_samlid_pcertificates_with_options(request, runtime)

    async def list_external_samlid_pcertificates_async(
        self,
        request: main_models.ListExternalSAMLIdPCertificatesRequest,
    ) -> main_models.ListExternalSAMLIdPCertificatesResponse:
        runtime = RuntimeOptions()
        return await self.list_external_samlid_pcertificates_with_options_async(request, runtime)

    def list_group_members_with_options(
        self,
        request: main_models.ListGroupMembersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGroupMembersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGroupMembers',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGroupMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_group_members_with_options_async(
        self,
        request: main_models.ListGroupMembersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGroupMembersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGroupMembers',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGroupMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_group_members(
        self,
        request: main_models.ListGroupMembersRequest,
    ) -> main_models.ListGroupMembersResponse:
        runtime = RuntimeOptions()
        return self.list_group_members_with_options(request, runtime)

    async def list_group_members_async(
        self,
        request: main_models.ListGroupMembersRequest,
    ) -> main_models.ListGroupMembersResponse:
        runtime = RuntimeOptions()
        return await self.list_group_members_with_options_async(request, runtime)

    def list_groups_with_options(
        self,
        request: main_models.ListGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.provision_type):
            query['ProvisionType'] = request.provision_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGroups',
            version = '2021-05-15',
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
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.provision_type):
            query['ProvisionType'] = request.provision_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGroups',
            version = '2021-05-15',
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

    def list_joined_groups_for_user_with_options(
        self,
        request: main_models.ListJoinedGroupsForUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListJoinedGroupsForUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
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
            action = 'ListJoinedGroupsForUser',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListJoinedGroupsForUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_joined_groups_for_user_with_options_async(
        self,
        request: main_models.ListJoinedGroupsForUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListJoinedGroupsForUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
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
            action = 'ListJoinedGroupsForUser',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListJoinedGroupsForUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_joined_groups_for_user(
        self,
        request: main_models.ListJoinedGroupsForUserRequest,
    ) -> main_models.ListJoinedGroupsForUserResponse:
        runtime = RuntimeOptions()
        return self.list_joined_groups_for_user_with_options(request, runtime)

    async def list_joined_groups_for_user_async(
        self,
        request: main_models.ListJoinedGroupsForUserRequest,
    ) -> main_models.ListJoinedGroupsForUserResponse:
        runtime = RuntimeOptions()
        return await self.list_joined_groups_for_user_with_options_async(request, runtime)

    def list_mfadevices_for_user_with_options(
        self,
        request: main_models.ListMFADevicesForUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMFADevicesForUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMFADevicesForUser',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMFADevicesForUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mfadevices_for_user_with_options_async(
        self,
        request: main_models.ListMFADevicesForUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMFADevicesForUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMFADevicesForUser',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMFADevicesForUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mfadevices_for_user(
        self,
        request: main_models.ListMFADevicesForUserRequest,
    ) -> main_models.ListMFADevicesForUserResponse:
        runtime = RuntimeOptions()
        return self.list_mfadevices_for_user_with_options(request, runtime)

    async def list_mfadevices_for_user_async(
        self,
        request: main_models.ListMFADevicesForUserRequest,
    ) -> main_models.ListMFADevicesForUserResponse:
        runtime = RuntimeOptions()
        return await self.list_mfadevices_for_user_with_options_async(request, runtime)

    def list_permission_policies_in_access_configuration_with_options(
        self,
        request: main_models.ListPermissionPoliciesInAccessConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPermissionPoliciesInAccessConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.permission_policy_type):
            query['PermissionPolicyType'] = request.permission_policy_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPermissionPoliciesInAccessConfiguration',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPermissionPoliciesInAccessConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_permission_policies_in_access_configuration_with_options_async(
        self,
        request: main_models.ListPermissionPoliciesInAccessConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPermissionPoliciesInAccessConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.permission_policy_type):
            query['PermissionPolicyType'] = request.permission_policy_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPermissionPoliciesInAccessConfiguration',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPermissionPoliciesInAccessConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_permission_policies_in_access_configuration(
        self,
        request: main_models.ListPermissionPoliciesInAccessConfigurationRequest,
    ) -> main_models.ListPermissionPoliciesInAccessConfigurationResponse:
        runtime = RuntimeOptions()
        return self.list_permission_policies_in_access_configuration_with_options(request, runtime)

    async def list_permission_policies_in_access_configuration_async(
        self,
        request: main_models.ListPermissionPoliciesInAccessConfigurationRequest,
    ) -> main_models.ListPermissionPoliciesInAccessConfigurationResponse:
        runtime = RuntimeOptions()
        return await self.list_permission_policies_in_access_configuration_with_options_async(request, runtime)

    def list_scimserver_credentials_with_options(
        self,
        request: main_models.ListSCIMServerCredentialsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSCIMServerCredentialsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSCIMServerCredentials',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSCIMServerCredentialsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_scimserver_credentials_with_options_async(
        self,
        request: main_models.ListSCIMServerCredentialsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSCIMServerCredentialsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSCIMServerCredentials',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSCIMServerCredentialsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_scimserver_credentials(
        self,
        request: main_models.ListSCIMServerCredentialsRequest,
    ) -> main_models.ListSCIMServerCredentialsResponse:
        runtime = RuntimeOptions()
        return self.list_scimserver_credentials_with_options(request, runtime)

    async def list_scimserver_credentials_async(
        self,
        request: main_models.ListSCIMServerCredentialsRequest,
    ) -> main_models.ListSCIMServerCredentialsResponse:
        runtime = RuntimeOptions()
        return await self.list_scimserver_credentials_with_options_async(request, runtime)

    def list_tasks_with_options(
        self,
        request: main_models.ListTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.principal_id):
            query['PrincipalId'] = request.principal_id
        if not DaraCore.is_null(request.principal_type):
            query['PrincipalType'] = request.principal_type
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.target_id):
            query['TargetId'] = request.target_id
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTasks',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tasks_with_options_async(
        self,
        request: main_models.ListTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.principal_id):
            query['PrincipalId'] = request.principal_id
        if not DaraCore.is_null(request.principal_type):
            query['PrincipalType'] = request.principal_type
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.target_id):
            query['TargetId'] = request.target_id
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTasks',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tasks(
        self,
        request: main_models.ListTasksRequest,
    ) -> main_models.ListTasksResponse:
        runtime = RuntimeOptions()
        return self.list_tasks_with_options(request, runtime)

    async def list_tasks_async(
        self,
        request: main_models.ListTasksRequest,
    ) -> main_models.ListTasksResponse:
        runtime = RuntimeOptions()
        return await self.list_tasks_with_options_async(request, runtime)

    def list_user_provisioning_events_with_options(
        self,
        request: main_models.ListUserProvisioningEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserProvisioningEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.user_provisioning_id):
            query['UserProvisioningId'] = request.user_provisioning_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserProvisioningEvents',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserProvisioningEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_provisioning_events_with_options_async(
        self,
        request: main_models.ListUserProvisioningEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserProvisioningEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.user_provisioning_id):
            query['UserProvisioningId'] = request.user_provisioning_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserProvisioningEvents',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserProvisioningEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_provisioning_events(
        self,
        request: main_models.ListUserProvisioningEventsRequest,
    ) -> main_models.ListUserProvisioningEventsResponse:
        runtime = RuntimeOptions()
        return self.list_user_provisioning_events_with_options(request, runtime)

    async def list_user_provisioning_events_async(
        self,
        request: main_models.ListUserProvisioningEventsRequest,
    ) -> main_models.ListUserProvisioningEventsResponse:
        runtime = RuntimeOptions()
        return await self.list_user_provisioning_events_with_options_async(request, runtime)

    def list_user_provisionings_with_options(
        self,
        request: main_models.ListUserProvisioningsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserProvisioningsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.principal_id):
            query['PrincipalId'] = request.principal_id
        if not DaraCore.is_null(request.principal_type):
            query['PrincipalType'] = request.principal_type
        if not DaraCore.is_null(request.target_id):
            query['TargetId'] = request.target_id
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserProvisionings',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserProvisioningsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_provisionings_with_options_async(
        self,
        request: main_models.ListUserProvisioningsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserProvisioningsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.principal_id):
            query['PrincipalId'] = request.principal_id
        if not DaraCore.is_null(request.principal_type):
            query['PrincipalType'] = request.principal_type
        if not DaraCore.is_null(request.target_id):
            query['TargetId'] = request.target_id
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserProvisionings',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserProvisioningsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_provisionings(
        self,
        request: main_models.ListUserProvisioningsRequest,
    ) -> main_models.ListUserProvisioningsResponse:
        runtime = RuntimeOptions()
        return self.list_user_provisionings_with_options(request, runtime)

    async def list_user_provisionings_async(
        self,
        request: main_models.ListUserProvisioningsRequest,
    ) -> main_models.ListUserProvisioningsResponse:
        runtime = RuntimeOptions()
        return await self.list_user_provisionings_with_options_async(request, runtime)

    def list_users_with_options(
        self,
        request: main_models.ListUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.provision_type):
            query['ProvisionType'] = request.provision_type
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUsers',
            version = '2021-05-15',
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
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.provision_type):
            query['ProvisionType'] = request.provision_type
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUsers',
            version = '2021-05-15',
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

    def provision_access_configuration_with_options(
        self,
        request: main_models.ProvisionAccessConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ProvisionAccessConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.origin_target_id):
            query['OriginTargetId'] = request.origin_target_id
        if not DaraCore.is_null(request.target_id):
            query['TargetId'] = request.target_id
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ProvisionAccessConfiguration',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ProvisionAccessConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def provision_access_configuration_with_options_async(
        self,
        request: main_models.ProvisionAccessConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ProvisionAccessConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.origin_target_id):
            query['OriginTargetId'] = request.origin_target_id
        if not DaraCore.is_null(request.target_id):
            query['TargetId'] = request.target_id
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ProvisionAccessConfiguration',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ProvisionAccessConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def provision_access_configuration(
        self,
        request: main_models.ProvisionAccessConfigurationRequest,
    ) -> main_models.ProvisionAccessConfigurationResponse:
        runtime = RuntimeOptions()
        return self.provision_access_configuration_with_options(request, runtime)

    async def provision_access_configuration_async(
        self,
        request: main_models.ProvisionAccessConfigurationRequest,
    ) -> main_models.ProvisionAccessConfigurationResponse:
        runtime = RuntimeOptions()
        return await self.provision_access_configuration_with_options_async(request, runtime)

    def remove_external_samlid_pcertificate_with_options(
        self,
        request: main_models.RemoveExternalSAMLIdPCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveExternalSAMLIdPCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.certificate_id):
            query['CertificateId'] = request.certificate_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveExternalSAMLIdPCertificate',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveExternalSAMLIdPCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_external_samlid_pcertificate_with_options_async(
        self,
        request: main_models.RemoveExternalSAMLIdPCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveExternalSAMLIdPCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.certificate_id):
            query['CertificateId'] = request.certificate_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveExternalSAMLIdPCertificate',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveExternalSAMLIdPCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_external_samlid_pcertificate(
        self,
        request: main_models.RemoveExternalSAMLIdPCertificateRequest,
    ) -> main_models.RemoveExternalSAMLIdPCertificateResponse:
        runtime = RuntimeOptions()
        return self.remove_external_samlid_pcertificate_with_options(request, runtime)

    async def remove_external_samlid_pcertificate_async(
        self,
        request: main_models.RemoveExternalSAMLIdPCertificateRequest,
    ) -> main_models.RemoveExternalSAMLIdPCertificateResponse:
        runtime = RuntimeOptions()
        return await self.remove_external_samlid_pcertificate_with_options_async(request, runtime)

    def remove_permission_policy_from_access_configuration_with_options(
        self,
        request: main_models.RemovePermissionPolicyFromAccessConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemovePermissionPolicyFromAccessConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.permission_policy_name):
            query['PermissionPolicyName'] = request.permission_policy_name
        if not DaraCore.is_null(request.permission_policy_type):
            query['PermissionPolicyType'] = request.permission_policy_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemovePermissionPolicyFromAccessConfiguration',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemovePermissionPolicyFromAccessConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_permission_policy_from_access_configuration_with_options_async(
        self,
        request: main_models.RemovePermissionPolicyFromAccessConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemovePermissionPolicyFromAccessConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.permission_policy_name):
            query['PermissionPolicyName'] = request.permission_policy_name
        if not DaraCore.is_null(request.permission_policy_type):
            query['PermissionPolicyType'] = request.permission_policy_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemovePermissionPolicyFromAccessConfiguration',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemovePermissionPolicyFromAccessConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_permission_policy_from_access_configuration(
        self,
        request: main_models.RemovePermissionPolicyFromAccessConfigurationRequest,
    ) -> main_models.RemovePermissionPolicyFromAccessConfigurationResponse:
        runtime = RuntimeOptions()
        return self.remove_permission_policy_from_access_configuration_with_options(request, runtime)

    async def remove_permission_policy_from_access_configuration_async(
        self,
        request: main_models.RemovePermissionPolicyFromAccessConfigurationRequest,
    ) -> main_models.RemovePermissionPolicyFromAccessConfigurationResponse:
        runtime = RuntimeOptions()
        return await self.remove_permission_policy_from_access_configuration_with_options_async(request, runtime)

    def remove_user_from_group_with_options(
        self,
        request: main_models.RemoveUserFromGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveUserFromGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveUserFromGroup',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveUserFromGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_user_from_group_with_options_async(
        self,
        request: main_models.RemoveUserFromGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveUserFromGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveUserFromGroup',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveUserFromGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_user_from_group(
        self,
        request: main_models.RemoveUserFromGroupRequest,
    ) -> main_models.RemoveUserFromGroupResponse:
        runtime = RuntimeOptions()
        return self.remove_user_from_group_with_options(request, runtime)

    async def remove_user_from_group_async(
        self,
        request: main_models.RemoveUserFromGroupRequest,
    ) -> main_models.RemoveUserFromGroupResponse:
        runtime = RuntimeOptions()
        return await self.remove_user_from_group_with_options_async(request, runtime)

    def reset_user_password_with_options(
        self,
        request: main_models.ResetUserPasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetUserPasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.generate_random_password):
            query['GenerateRandomPassword'] = request.generate_random_password
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.require_password_reset_for_next_login):
            query['RequirePasswordResetForNextLogin'] = request.require_password_reset_for_next_login
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetUserPassword',
            version = '2021-05-15',
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
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.generate_random_password):
            query['GenerateRandomPassword'] = request.generate_random_password
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.require_password_reset_for_next_login):
            query['RequirePasswordResetForNextLogin'] = request.require_password_reset_for_next_login
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetUserPassword',
            version = '2021-05-15',
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

    def retry_user_provisioning_event_with_options(
        self,
        request: main_models.RetryUserProvisioningEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RetryUserProvisioningEventResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.duplication_strategy):
            query['DuplicationStrategy'] = request.duplication_strategy
        if not DaraCore.is_null(request.event_id):
            query['EventId'] = request.event_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RetryUserProvisioningEvent',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RetryUserProvisioningEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def retry_user_provisioning_event_with_options_async(
        self,
        request: main_models.RetryUserProvisioningEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RetryUserProvisioningEventResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.duplication_strategy):
            query['DuplicationStrategy'] = request.duplication_strategy
        if not DaraCore.is_null(request.event_id):
            query['EventId'] = request.event_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RetryUserProvisioningEvent',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RetryUserProvisioningEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def retry_user_provisioning_event(
        self,
        request: main_models.RetryUserProvisioningEventRequest,
    ) -> main_models.RetryUserProvisioningEventResponse:
        runtime = RuntimeOptions()
        return self.retry_user_provisioning_event_with_options(request, runtime)

    async def retry_user_provisioning_event_async(
        self,
        request: main_models.RetryUserProvisioningEventRequest,
    ) -> main_models.RetryUserProvisioningEventResponse:
        runtime = RuntimeOptions()
        return await self.retry_user_provisioning_event_with_options_async(request, runtime)

    def set_external_samlidentity_provider_with_options(
        self,
        request: main_models.SetExternalSAMLIdentityProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetExternalSAMLIdentityProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.binding_type):
            query['BindingType'] = request.binding_type
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.encoded_metadata_document):
            query['EncodedMetadataDocument'] = request.encoded_metadata_document
        if not DaraCore.is_null(request.entity_id):
            query['EntityId'] = request.entity_id
        if not DaraCore.is_null(request.login_url):
            query['LoginUrl'] = request.login_url
        if not DaraCore.is_null(request.ssostatus):
            query['SSOStatus'] = request.ssostatus
        if not DaraCore.is_null(request.want_request_signed):
            query['WantRequestSigned'] = request.want_request_signed
        if not DaraCore.is_null(request.x_509certificate):
            query['X509Certificate'] = request.x_509certificate
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetExternalSAMLIdentityProvider',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetExternalSAMLIdentityProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_external_samlidentity_provider_with_options_async(
        self,
        request: main_models.SetExternalSAMLIdentityProviderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetExternalSAMLIdentityProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.binding_type):
            query['BindingType'] = request.binding_type
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.encoded_metadata_document):
            query['EncodedMetadataDocument'] = request.encoded_metadata_document
        if not DaraCore.is_null(request.entity_id):
            query['EntityId'] = request.entity_id
        if not DaraCore.is_null(request.login_url):
            query['LoginUrl'] = request.login_url
        if not DaraCore.is_null(request.ssostatus):
            query['SSOStatus'] = request.ssostatus
        if not DaraCore.is_null(request.want_request_signed):
            query['WantRequestSigned'] = request.want_request_signed
        if not DaraCore.is_null(request.x_509certificate):
            query['X509Certificate'] = request.x_509certificate
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetExternalSAMLIdentityProvider',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetExternalSAMLIdentityProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_external_samlidentity_provider(
        self,
        request: main_models.SetExternalSAMLIdentityProviderRequest,
    ) -> main_models.SetExternalSAMLIdentityProviderResponse:
        runtime = RuntimeOptions()
        return self.set_external_samlidentity_provider_with_options(request, runtime)

    async def set_external_samlidentity_provider_async(
        self,
        request: main_models.SetExternalSAMLIdentityProviderRequest,
    ) -> main_models.SetExternalSAMLIdentityProviderResponse:
        runtime = RuntimeOptions()
        return await self.set_external_samlidentity_provider_with_options_async(request, runtime)

    def set_login_preference_with_options(
        self,
        request: main_models.SetLoginPreferenceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetLoginPreferenceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.allow_user_to_get_credentials):
            query['AllowUserToGetCredentials'] = request.allow_user_to_get_credentials
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.login_network_masks):
            query['LoginNetworkMasks'] = request.login_network_masks
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetLoginPreference',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetLoginPreferenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_login_preference_with_options_async(
        self,
        request: main_models.SetLoginPreferenceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetLoginPreferenceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.allow_user_to_get_credentials):
            query['AllowUserToGetCredentials'] = request.allow_user_to_get_credentials
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.login_network_masks):
            query['LoginNetworkMasks'] = request.login_network_masks
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetLoginPreference',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetLoginPreferenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_login_preference(
        self,
        request: main_models.SetLoginPreferenceRequest,
    ) -> main_models.SetLoginPreferenceResponse:
        runtime = RuntimeOptions()
        return self.set_login_preference_with_options(request, runtime)

    async def set_login_preference_async(
        self,
        request: main_models.SetLoginPreferenceRequest,
    ) -> main_models.SetLoginPreferenceResponse:
        runtime = RuntimeOptions()
        return await self.set_login_preference_with_options_async(request, runtime)

    def set_mfaauthentication_status_with_options(
        self,
        request: main_models.SetMFAAuthenticationStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetMFAAuthenticationStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.mfaauthentication_status):
            query['MFAAuthenticationStatus'] = request.mfaauthentication_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetMFAAuthenticationStatus',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetMFAAuthenticationStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_mfaauthentication_status_with_options_async(
        self,
        request: main_models.SetMFAAuthenticationStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetMFAAuthenticationStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.mfaauthentication_status):
            query['MFAAuthenticationStatus'] = request.mfaauthentication_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetMFAAuthenticationStatus',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetMFAAuthenticationStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_mfaauthentication_status(
        self,
        request: main_models.SetMFAAuthenticationStatusRequest,
    ) -> main_models.SetMFAAuthenticationStatusResponse:
        runtime = RuntimeOptions()
        return self.set_mfaauthentication_status_with_options(request, runtime)

    async def set_mfaauthentication_status_async(
        self,
        request: main_models.SetMFAAuthenticationStatusRequest,
    ) -> main_models.SetMFAAuthenticationStatusResponse:
        runtime = RuntimeOptions()
        return await self.set_mfaauthentication_status_with_options_async(request, runtime)

    def set_password_policy_with_options(
        self,
        request: main_models.SetPasswordPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetPasswordPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.max_login_attempts):
            query['MaxLoginAttempts'] = request.max_login_attempts
        if not DaraCore.is_null(request.max_password_age):
            query['MaxPasswordAge'] = request.max_password_age
        if not DaraCore.is_null(request.min_password_different_chars):
            query['MinPasswordDifferentChars'] = request.min_password_different_chars
        if not DaraCore.is_null(request.min_password_length):
            query['MinPasswordLength'] = request.min_password_length
        if not DaraCore.is_null(request.password_not_contain_username):
            query['PasswordNotContainUsername'] = request.password_not_contain_username
        if not DaraCore.is_null(request.password_reuse_prevention):
            query['PasswordReusePrevention'] = request.password_reuse_prevention
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetPasswordPolicy',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetPasswordPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_password_policy_with_options_async(
        self,
        request: main_models.SetPasswordPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetPasswordPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.max_login_attempts):
            query['MaxLoginAttempts'] = request.max_login_attempts
        if not DaraCore.is_null(request.max_password_age):
            query['MaxPasswordAge'] = request.max_password_age
        if not DaraCore.is_null(request.min_password_different_chars):
            query['MinPasswordDifferentChars'] = request.min_password_different_chars
        if not DaraCore.is_null(request.min_password_length):
            query['MinPasswordLength'] = request.min_password_length
        if not DaraCore.is_null(request.password_not_contain_username):
            query['PasswordNotContainUsername'] = request.password_not_contain_username
        if not DaraCore.is_null(request.password_reuse_prevention):
            query['PasswordReusePrevention'] = request.password_reuse_prevention
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetPasswordPolicy',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetPasswordPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_password_policy(
        self,
        request: main_models.SetPasswordPolicyRequest,
    ) -> main_models.SetPasswordPolicyResponse:
        runtime = RuntimeOptions()
        return self.set_password_policy_with_options(request, runtime)

    async def set_password_policy_async(
        self,
        request: main_models.SetPasswordPolicyRequest,
    ) -> main_models.SetPasswordPolicyResponse:
        runtime = RuntimeOptions()
        return await self.set_password_policy_with_options_async(request, runtime)

    def set_scimsynchronization_status_with_options(
        self,
        request: main_models.SetSCIMSynchronizationStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetSCIMSynchronizationStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.scimsynchronization_status):
            query['SCIMSynchronizationStatus'] = request.scimsynchronization_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetSCIMSynchronizationStatus',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetSCIMSynchronizationStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_scimsynchronization_status_with_options_async(
        self,
        request: main_models.SetSCIMSynchronizationStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetSCIMSynchronizationStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.scimsynchronization_status):
            query['SCIMSynchronizationStatus'] = request.scimsynchronization_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetSCIMSynchronizationStatus',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetSCIMSynchronizationStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_scimsynchronization_status(
        self,
        request: main_models.SetSCIMSynchronizationStatusRequest,
    ) -> main_models.SetSCIMSynchronizationStatusResponse:
        runtime = RuntimeOptions()
        return self.set_scimsynchronization_status_with_options(request, runtime)

    async def set_scimsynchronization_status_async(
        self,
        request: main_models.SetSCIMSynchronizationStatusRequest,
    ) -> main_models.SetSCIMSynchronizationStatusResponse:
        runtime = RuntimeOptions()
        return await self.set_scimsynchronization_status_with_options_async(request, runtime)

    def update_access_configuration_with_options(
        self,
        request: main_models.UpdateAccessConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAccessConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.new_description):
            query['NewDescription'] = request.new_description
        if not DaraCore.is_null(request.new_relay_state):
            query['NewRelayState'] = request.new_relay_state
        if not DaraCore.is_null(request.new_session_duration):
            query['NewSessionDuration'] = request.new_session_duration
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAccessConfiguration',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAccessConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_access_configuration_with_options_async(
        self,
        request: main_models.UpdateAccessConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAccessConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.new_description):
            query['NewDescription'] = request.new_description
        if not DaraCore.is_null(request.new_relay_state):
            query['NewRelayState'] = request.new_relay_state
        if not DaraCore.is_null(request.new_session_duration):
            query['NewSessionDuration'] = request.new_session_duration
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAccessConfiguration',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAccessConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_access_configuration(
        self,
        request: main_models.UpdateAccessConfigurationRequest,
    ) -> main_models.UpdateAccessConfigurationResponse:
        runtime = RuntimeOptions()
        return self.update_access_configuration_with_options(request, runtime)

    async def update_access_configuration_async(
        self,
        request: main_models.UpdateAccessConfigurationRequest,
    ) -> main_models.UpdateAccessConfigurationResponse:
        runtime = RuntimeOptions()
        return await self.update_access_configuration_with_options_async(request, runtime)

    def update_directory_with_options(
        self,
        request: main_models.UpdateDirectoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDirectoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.new_directory_name):
            query['NewDirectoryName'] = request.new_directory_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDirectory',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_directory_with_options_async(
        self,
        request: main_models.UpdateDirectoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDirectoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.new_directory_name):
            query['NewDirectoryName'] = request.new_directory_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDirectory',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_directory(
        self,
        request: main_models.UpdateDirectoryRequest,
    ) -> main_models.UpdateDirectoryResponse:
        runtime = RuntimeOptions()
        return self.update_directory_with_options(request, runtime)

    async def update_directory_async(
        self,
        request: main_models.UpdateDirectoryRequest,
    ) -> main_models.UpdateDirectoryResponse:
        runtime = RuntimeOptions()
        return await self.update_directory_with_options_async(request, runtime)

    def update_group_with_options(
        self,
        request: main_models.UpdateGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.new_description):
            query['NewDescription'] = request.new_description
        if not DaraCore.is_null(request.new_group_name):
            query['NewGroupName'] = request.new_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGroup',
            version = '2021-05-15',
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
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.new_description):
            query['NewDescription'] = request.new_description
        if not DaraCore.is_null(request.new_group_name):
            query['NewGroupName'] = request.new_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGroup',
            version = '2021-05-15',
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

    def update_inline_policy_for_access_configuration_with_options(
        self,
        request: main_models.UpdateInlinePolicyForAccessConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInlinePolicyForAccessConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.inline_policy_name):
            query['InlinePolicyName'] = request.inline_policy_name
        if not DaraCore.is_null(request.new_inline_policy_document):
            query['NewInlinePolicyDocument'] = request.new_inline_policy_document
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInlinePolicyForAccessConfiguration',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInlinePolicyForAccessConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_inline_policy_for_access_configuration_with_options_async(
        self,
        request: main_models.UpdateInlinePolicyForAccessConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInlinePolicyForAccessConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.inline_policy_name):
            query['InlinePolicyName'] = request.inline_policy_name
        if not DaraCore.is_null(request.new_inline_policy_document):
            query['NewInlinePolicyDocument'] = request.new_inline_policy_document
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInlinePolicyForAccessConfiguration',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInlinePolicyForAccessConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_inline_policy_for_access_configuration(
        self,
        request: main_models.UpdateInlinePolicyForAccessConfigurationRequest,
    ) -> main_models.UpdateInlinePolicyForAccessConfigurationResponse:
        runtime = RuntimeOptions()
        return self.update_inline_policy_for_access_configuration_with_options(request, runtime)

    async def update_inline_policy_for_access_configuration_async(
        self,
        request: main_models.UpdateInlinePolicyForAccessConfigurationRequest,
    ) -> main_models.UpdateInlinePolicyForAccessConfigurationResponse:
        runtime = RuntimeOptions()
        return await self.update_inline_policy_for_access_configuration_with_options_async(request, runtime)

    def update_mfaauthentication_settings_with_options(
        self,
        tmp_req: main_models.UpdateMFAAuthenticationSettingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMFAAuthenticationSettingsResponse:
        tmp_req.validate()
        request = main_models.UpdateMFAAuthenticationSettingsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.allowed_verification_types):
            request.allowed_verification_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.allowed_verification_types, 'AllowedVerificationTypes', 'json')
        query = {}
        if not DaraCore.is_null(request.allowed_verification_types_shrink):
            query['AllowedVerificationTypes'] = request.allowed_verification_types_shrink
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.mfaauthentication_settings):
            query['MFAAuthenticationSettings'] = request.mfaauthentication_settings
        if not DaraCore.is_null(request.operation_for_risk_login):
            query['OperationForRiskLogin'] = request.operation_for_risk_login
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMFAAuthenticationSettings',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMFAAuthenticationSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_mfaauthentication_settings_with_options_async(
        self,
        tmp_req: main_models.UpdateMFAAuthenticationSettingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMFAAuthenticationSettingsResponse:
        tmp_req.validate()
        request = main_models.UpdateMFAAuthenticationSettingsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.allowed_verification_types):
            request.allowed_verification_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.allowed_verification_types, 'AllowedVerificationTypes', 'json')
        query = {}
        if not DaraCore.is_null(request.allowed_verification_types_shrink):
            query['AllowedVerificationTypes'] = request.allowed_verification_types_shrink
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.mfaauthentication_settings):
            query['MFAAuthenticationSettings'] = request.mfaauthentication_settings
        if not DaraCore.is_null(request.operation_for_risk_login):
            query['OperationForRiskLogin'] = request.operation_for_risk_login
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMFAAuthenticationSettings',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMFAAuthenticationSettingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_mfaauthentication_settings(
        self,
        request: main_models.UpdateMFAAuthenticationSettingsRequest,
    ) -> main_models.UpdateMFAAuthenticationSettingsResponse:
        runtime = RuntimeOptions()
        return self.update_mfaauthentication_settings_with_options(request, runtime)

    async def update_mfaauthentication_settings_async(
        self,
        request: main_models.UpdateMFAAuthenticationSettingsRequest,
    ) -> main_models.UpdateMFAAuthenticationSettingsResponse:
        runtime = RuntimeOptions()
        return await self.update_mfaauthentication_settings_with_options_async(request, runtime)

    def update_scimserver_credential_status_with_options(
        self,
        request: main_models.UpdateSCIMServerCredentialStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSCIMServerCredentialStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.credential_id):
            query['CredentialId'] = request.credential_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.new_status):
            query['NewStatus'] = request.new_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSCIMServerCredentialStatus',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSCIMServerCredentialStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_scimserver_credential_status_with_options_async(
        self,
        request: main_models.UpdateSCIMServerCredentialStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSCIMServerCredentialStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.credential_id):
            query['CredentialId'] = request.credential_id
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.new_status):
            query['NewStatus'] = request.new_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSCIMServerCredentialStatus',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSCIMServerCredentialStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_scimserver_credential_status(
        self,
        request: main_models.UpdateSCIMServerCredentialStatusRequest,
    ) -> main_models.UpdateSCIMServerCredentialStatusResponse:
        runtime = RuntimeOptions()
        return self.update_scimserver_credential_status_with_options(request, runtime)

    async def update_scimserver_credential_status_async(
        self,
        request: main_models.UpdateSCIMServerCredentialStatusRequest,
    ) -> main_models.UpdateSCIMServerCredentialStatusResponse:
        runtime = RuntimeOptions()
        return await self.update_scimserver_credential_status_with_options_async(request, runtime)

    def update_user_with_options(
        self,
        request: main_models.UpdateUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.new_description):
            query['NewDescription'] = request.new_description
        if not DaraCore.is_null(request.new_display_name):
            query['NewDisplayName'] = request.new_display_name
        if not DaraCore.is_null(request.new_email):
            query['NewEmail'] = request.new_email
        if not DaraCore.is_null(request.new_first_name):
            query['NewFirstName'] = request.new_first_name
        if not DaraCore.is_null(request.new_last_name):
            query['NewLastName'] = request.new_last_name
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUser',
            version = '2021-05-15',
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
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.new_description):
            query['NewDescription'] = request.new_description
        if not DaraCore.is_null(request.new_display_name):
            query['NewDisplayName'] = request.new_display_name
        if not DaraCore.is_null(request.new_email):
            query['NewEmail'] = request.new_email
        if not DaraCore.is_null(request.new_first_name):
            query['NewFirstName'] = request.new_first_name
        if not DaraCore.is_null(request.new_last_name):
            query['NewLastName'] = request.new_last_name
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUser',
            version = '2021-05-15',
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

    def update_user_mfaauthentication_settings_with_options(
        self,
        request: main_models.UpdateUserMFAAuthenticationSettingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserMFAAuthenticationSettingsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.user_mfaauthentication_settings):
            query['UserMFAAuthenticationSettings'] = request.user_mfaauthentication_settings
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUserMFAAuthenticationSettings',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUserMFAAuthenticationSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_mfaauthentication_settings_with_options_async(
        self,
        request: main_models.UpdateUserMFAAuthenticationSettingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserMFAAuthenticationSettingsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.user_mfaauthentication_settings):
            query['UserMFAAuthenticationSettings'] = request.user_mfaauthentication_settings
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUserMFAAuthenticationSettings',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUserMFAAuthenticationSettingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user_mfaauthentication_settings(
        self,
        request: main_models.UpdateUserMFAAuthenticationSettingsRequest,
    ) -> main_models.UpdateUserMFAAuthenticationSettingsResponse:
        runtime = RuntimeOptions()
        return self.update_user_mfaauthentication_settings_with_options(request, runtime)

    async def update_user_mfaauthentication_settings_async(
        self,
        request: main_models.UpdateUserMFAAuthenticationSettingsRequest,
    ) -> main_models.UpdateUserMFAAuthenticationSettingsResponse:
        runtime = RuntimeOptions()
        return await self.update_user_mfaauthentication_settings_with_options_async(request, runtime)

    def update_user_provisioning_with_options(
        self,
        request: main_models.UpdateUserProvisioningRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserProvisioningResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.new_deletion_strategy):
            query['NewDeletionStrategy'] = request.new_deletion_strategy
        if not DaraCore.is_null(request.new_description):
            query['NewDescription'] = request.new_description
        if not DaraCore.is_null(request.new_duplication_strategy):
            query['NewDuplicationStrategy'] = request.new_duplication_strategy
        if not DaraCore.is_null(request.user_provisioning_id):
            query['UserProvisioningId'] = request.user_provisioning_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUserProvisioning',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUserProvisioningResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_provisioning_with_options_async(
        self,
        request: main_models.UpdateUserProvisioningRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserProvisioningResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.new_deletion_strategy):
            query['NewDeletionStrategy'] = request.new_deletion_strategy
        if not DaraCore.is_null(request.new_description):
            query['NewDescription'] = request.new_description
        if not DaraCore.is_null(request.new_duplication_strategy):
            query['NewDuplicationStrategy'] = request.new_duplication_strategy
        if not DaraCore.is_null(request.user_provisioning_id):
            query['UserProvisioningId'] = request.user_provisioning_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUserProvisioning',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUserProvisioningResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user_provisioning(
        self,
        request: main_models.UpdateUserProvisioningRequest,
    ) -> main_models.UpdateUserProvisioningResponse:
        runtime = RuntimeOptions()
        return self.update_user_provisioning_with_options(request, runtime)

    async def update_user_provisioning_async(
        self,
        request: main_models.UpdateUserProvisioningRequest,
    ) -> main_models.UpdateUserProvisioningResponse:
        runtime = RuntimeOptions()
        return await self.update_user_provisioning_with_options_async(request, runtime)

    def update_user_provisioning_configuration_with_options(
        self,
        request: main_models.UpdateUserProvisioningConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserProvisioningConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.new_default_landing_page):
            query['NewDefaultLandingPage'] = request.new_default_landing_page
        if not DaraCore.is_null(request.new_session_duration):
            query['NewSessionDuration'] = request.new_session_duration
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUserProvisioningConfiguration',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUserProvisioningConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_provisioning_configuration_with_options_async(
        self,
        request: main_models.UpdateUserProvisioningConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserProvisioningConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.new_default_landing_page):
            query['NewDefaultLandingPage'] = request.new_default_landing_page
        if not DaraCore.is_null(request.new_session_duration):
            query['NewSessionDuration'] = request.new_session_duration
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUserProvisioningConfiguration',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUserProvisioningConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user_provisioning_configuration(
        self,
        request: main_models.UpdateUserProvisioningConfigurationRequest,
    ) -> main_models.UpdateUserProvisioningConfigurationResponse:
        runtime = RuntimeOptions()
        return self.update_user_provisioning_configuration_with_options(request, runtime)

    async def update_user_provisioning_configuration_async(
        self,
        request: main_models.UpdateUserProvisioningConfigurationRequest,
    ) -> main_models.UpdateUserProvisioningConfigurationResponse:
        runtime = RuntimeOptions()
        return await self.update_user_provisioning_configuration_with_options_async(request, runtime)

    def update_user_status_with_options(
        self,
        request: main_models.UpdateUserStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.new_status):
            query['NewStatus'] = request.new_status
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUserStatus',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUserStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_status_with_options_async(
        self,
        request: main_models.UpdateUserStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not DaraCore.is_null(request.new_status):
            query['NewStatus'] = request.new_status
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUserStatus',
            version = '2021-05-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUserStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user_status(
        self,
        request: main_models.UpdateUserStatusRequest,
    ) -> main_models.UpdateUserStatusResponse:
        runtime = RuntimeOptions()
        return self.update_user_status_with_options(request, runtime)

    async def update_user_status_async(
        self,
        request: main_models.UpdateUserStatusRequest,
    ) -> main_models.UpdateUserStatusResponse:
        runtime = RuntimeOptions()
        return await self.update_user_status_with_options_async(request, runtime)
