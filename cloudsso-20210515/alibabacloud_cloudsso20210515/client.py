# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cloudsso20210515 import models as cloudsso_20210515_models
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
        self._endpoint_rule = 'regional'
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_external_samlid_pcertificate_with_options(
        self,
        request: cloudsso_20210515_models.AddExternalSAMLIdPCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.AddExternalSAMLIdPCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        query['X509Certificate'] = request.x_509certificate
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddExternalSAMLIdPCertificate',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.AddExternalSAMLIdPCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_external_samlid_pcertificate_with_options_async(
        self,
        request: cloudsso_20210515_models.AddExternalSAMLIdPCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.AddExternalSAMLIdPCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        query['X509Certificate'] = request.x_509certificate
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddExternalSAMLIdPCertificate',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.AddExternalSAMLIdPCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_external_samlid_pcertificate(
        self,
        request: cloudsso_20210515_models.AddExternalSAMLIdPCertificateRequest,
    ) -> cloudsso_20210515_models.AddExternalSAMLIdPCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_external_samlid_pcertificate_with_options(request, runtime)

    async def add_external_samlid_pcertificate_async(
        self,
        request: cloudsso_20210515_models.AddExternalSAMLIdPCertificateRequest,
    ) -> cloudsso_20210515_models.AddExternalSAMLIdPCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_external_samlid_pcertificate_with_options_async(request, runtime)

    def add_permission_policy_to_access_configuration_with_options(
        self,
        request: cloudsso_20210515_models.AddPermissionPolicyToAccessConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.AddPermissionPolicyToAccessConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccessConfigurationId'] = request.access_configuration_id
        query['DirectoryId'] = request.directory_id
        query['InlinePolicyDocument'] = request.inline_policy_document
        query['PermissionPolicyName'] = request.permission_policy_name
        query['PermissionPolicyType'] = request.permission_policy_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddPermissionPolicyToAccessConfiguration',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.AddPermissionPolicyToAccessConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_permission_policy_to_access_configuration_with_options_async(
        self,
        request: cloudsso_20210515_models.AddPermissionPolicyToAccessConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.AddPermissionPolicyToAccessConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccessConfigurationId'] = request.access_configuration_id
        query['DirectoryId'] = request.directory_id
        query['InlinePolicyDocument'] = request.inline_policy_document
        query['PermissionPolicyName'] = request.permission_policy_name
        query['PermissionPolicyType'] = request.permission_policy_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddPermissionPolicyToAccessConfiguration',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.AddPermissionPolicyToAccessConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_permission_policy_to_access_configuration(
        self,
        request: cloudsso_20210515_models.AddPermissionPolicyToAccessConfigurationRequest,
    ) -> cloudsso_20210515_models.AddPermissionPolicyToAccessConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_permission_policy_to_access_configuration_with_options(request, runtime)

    async def add_permission_policy_to_access_configuration_async(
        self,
        request: cloudsso_20210515_models.AddPermissionPolicyToAccessConfigurationRequest,
    ) -> cloudsso_20210515_models.AddPermissionPolicyToAccessConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_permission_policy_to_access_configuration_with_options_async(request, runtime)

    def add_user_to_group_with_options(
        self,
        request: cloudsso_20210515_models.AddUserToGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.AddUserToGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        query['GroupId'] = request.group_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddUserToGroup',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.AddUserToGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_user_to_group_with_options_async(
        self,
        request: cloudsso_20210515_models.AddUserToGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.AddUserToGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        query['GroupId'] = request.group_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddUserToGroup',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.AddUserToGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_user_to_group(
        self,
        request: cloudsso_20210515_models.AddUserToGroupRequest,
    ) -> cloudsso_20210515_models.AddUserToGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_user_to_group_with_options(request, runtime)

    async def add_user_to_group_async(
        self,
        request: cloudsso_20210515_models.AddUserToGroupRequest,
    ) -> cloudsso_20210515_models.AddUserToGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_user_to_group_with_options_async(request, runtime)

    def clear_external_samlidentity_provider_with_options(
        self,
        request: cloudsso_20210515_models.ClearExternalSAMLIdentityProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.ClearExternalSAMLIdentityProviderResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ClearExternalSAMLIdentityProvider',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.ClearExternalSAMLIdentityProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def clear_external_samlidentity_provider_with_options_async(
        self,
        request: cloudsso_20210515_models.ClearExternalSAMLIdentityProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.ClearExternalSAMLIdentityProviderResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ClearExternalSAMLIdentityProvider',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.ClearExternalSAMLIdentityProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clear_external_samlidentity_provider(
        self,
        request: cloudsso_20210515_models.ClearExternalSAMLIdentityProviderRequest,
    ) -> cloudsso_20210515_models.ClearExternalSAMLIdentityProviderResponse:
        runtime = util_models.RuntimeOptions()
        return self.clear_external_samlidentity_provider_with_options(request, runtime)

    async def clear_external_samlidentity_provider_async(
        self,
        request: cloudsso_20210515_models.ClearExternalSAMLIdentityProviderRequest,
    ) -> cloudsso_20210515_models.ClearExternalSAMLIdentityProviderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.clear_external_samlidentity_provider_with_options_async(request, runtime)

    def create_access_assignment_with_options(
        self,
        request: cloudsso_20210515_models.CreateAccessAssignmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.CreateAccessAssignmentResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccessConfigurationId'] = request.access_configuration_id
        query['DirectoryId'] = request.directory_id
        query['PrincipalId'] = request.principal_id
        query['PrincipalType'] = request.principal_type
        query['TargetId'] = request.target_id
        query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateAccessAssignment',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.CreateAccessAssignmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_access_assignment_with_options_async(
        self,
        request: cloudsso_20210515_models.CreateAccessAssignmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.CreateAccessAssignmentResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccessConfigurationId'] = request.access_configuration_id
        query['DirectoryId'] = request.directory_id
        query['PrincipalId'] = request.principal_id
        query['PrincipalType'] = request.principal_type
        query['TargetId'] = request.target_id
        query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateAccessAssignment',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.CreateAccessAssignmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_access_assignment(
        self,
        request: cloudsso_20210515_models.CreateAccessAssignmentRequest,
    ) -> cloudsso_20210515_models.CreateAccessAssignmentResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_access_assignment_with_options(request, runtime)

    async def create_access_assignment_async(
        self,
        request: cloudsso_20210515_models.CreateAccessAssignmentRequest,
    ) -> cloudsso_20210515_models.CreateAccessAssignmentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_access_assignment_with_options_async(request, runtime)

    def create_access_configuration_with_options(
        self,
        request: cloudsso_20210515_models.CreateAccessConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.CreateAccessConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccessConfigurationName'] = request.access_configuration_name
        query['Description'] = request.description
        query['DirectoryId'] = request.directory_id
        query['RelayState'] = request.relay_state
        query['SessionDuration'] = request.session_duration
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateAccessConfiguration',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.CreateAccessConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_access_configuration_with_options_async(
        self,
        request: cloudsso_20210515_models.CreateAccessConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.CreateAccessConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccessConfigurationName'] = request.access_configuration_name
        query['Description'] = request.description
        query['DirectoryId'] = request.directory_id
        query['RelayState'] = request.relay_state
        query['SessionDuration'] = request.session_duration
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateAccessConfiguration',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.CreateAccessConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_access_configuration(
        self,
        request: cloudsso_20210515_models.CreateAccessConfigurationRequest,
    ) -> cloudsso_20210515_models.CreateAccessConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_access_configuration_with_options(request, runtime)

    async def create_access_configuration_async(
        self,
        request: cloudsso_20210515_models.CreateAccessConfigurationRequest,
    ) -> cloudsso_20210515_models.CreateAccessConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_access_configuration_with_options_async(request, runtime)

    def create_directory_with_options(
        self,
        request: cloudsso_20210515_models.CreateDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.CreateDirectoryResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryName'] = request.directory_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDirectory',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.CreateDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_directory_with_options_async(
        self,
        request: cloudsso_20210515_models.CreateDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.CreateDirectoryResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryName'] = request.directory_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDirectory',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.CreateDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_directory(
        self,
        request: cloudsso_20210515_models.CreateDirectoryRequest,
    ) -> cloudsso_20210515_models.CreateDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_directory_with_options(request, runtime)

    async def create_directory_async(
        self,
        request: cloudsso_20210515_models.CreateDirectoryRequest,
    ) -> cloudsso_20210515_models.CreateDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_directory_with_options_async(request, runtime)

    def create_group_with_options(
        self,
        request: cloudsso_20210515_models.CreateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.CreateGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Description'] = request.description
        query['DirectoryId'] = request.directory_id
        query['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateGroup',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.CreateGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_group_with_options_async(
        self,
        request: cloudsso_20210515_models.CreateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.CreateGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Description'] = request.description
        query['DirectoryId'] = request.directory_id
        query['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateGroup',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.CreateGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_group(
        self,
        request: cloudsso_20210515_models.CreateGroupRequest,
    ) -> cloudsso_20210515_models.CreateGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_group_with_options(request, runtime)

    async def create_group_async(
        self,
        request: cloudsso_20210515_models.CreateGroupRequest,
    ) -> cloudsso_20210515_models.CreateGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_group_with_options_async(request, runtime)

    def create_scimserver_credential_with_options(
        self,
        request: cloudsso_20210515_models.CreateSCIMServerCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.CreateSCIMServerCredentialResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateSCIMServerCredential',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.CreateSCIMServerCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_scimserver_credential_with_options_async(
        self,
        request: cloudsso_20210515_models.CreateSCIMServerCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.CreateSCIMServerCredentialResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateSCIMServerCredential',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.CreateSCIMServerCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_scimserver_credential(
        self,
        request: cloudsso_20210515_models.CreateSCIMServerCredentialRequest,
    ) -> cloudsso_20210515_models.CreateSCIMServerCredentialResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_scimserver_credential_with_options(request, runtime)

    async def create_scimserver_credential_async(
        self,
        request: cloudsso_20210515_models.CreateSCIMServerCredentialRequest,
    ) -> cloudsso_20210515_models.CreateSCIMServerCredentialResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_scimserver_credential_with_options_async(request, runtime)

    def create_user_with_options(
        self,
        request: cloudsso_20210515_models.CreateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.CreateUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Description'] = request.description
        query['DirectoryId'] = request.directory_id
        query['DisplayName'] = request.display_name
        query['Email'] = request.email
        query['FirstName'] = request.first_name
        query['LastName'] = request.last_name
        query['Status'] = request.status
        query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateUser',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.CreateUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_user_with_options_async(
        self,
        request: cloudsso_20210515_models.CreateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.CreateUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Description'] = request.description
        query['DirectoryId'] = request.directory_id
        query['DisplayName'] = request.display_name
        query['Email'] = request.email
        query['FirstName'] = request.first_name
        query['LastName'] = request.last_name
        query['Status'] = request.status
        query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateUser',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.CreateUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_user(
        self,
        request: cloudsso_20210515_models.CreateUserRequest,
    ) -> cloudsso_20210515_models.CreateUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_user_with_options(request, runtime)

    async def create_user_async(
        self,
        request: cloudsso_20210515_models.CreateUserRequest,
    ) -> cloudsso_20210515_models.CreateUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_user_with_options_async(request, runtime)

    def delete_access_assignment_with_options(
        self,
        request: cloudsso_20210515_models.DeleteAccessAssignmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.DeleteAccessAssignmentResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccessConfigurationId'] = request.access_configuration_id
        query['DeprovisionStrategy'] = request.deprovision_strategy
        query['DirectoryId'] = request.directory_id
        query['PrincipalId'] = request.principal_id
        query['PrincipalType'] = request.principal_type
        query['TargetId'] = request.target_id
        query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteAccessAssignment',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.DeleteAccessAssignmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_access_assignment_with_options_async(
        self,
        request: cloudsso_20210515_models.DeleteAccessAssignmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.DeleteAccessAssignmentResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccessConfigurationId'] = request.access_configuration_id
        query['DeprovisionStrategy'] = request.deprovision_strategy
        query['DirectoryId'] = request.directory_id
        query['PrincipalId'] = request.principal_id
        query['PrincipalType'] = request.principal_type
        query['TargetId'] = request.target_id
        query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteAccessAssignment',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.DeleteAccessAssignmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_access_assignment(
        self,
        request: cloudsso_20210515_models.DeleteAccessAssignmentRequest,
    ) -> cloudsso_20210515_models.DeleteAccessAssignmentResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_access_assignment_with_options(request, runtime)

    async def delete_access_assignment_async(
        self,
        request: cloudsso_20210515_models.DeleteAccessAssignmentRequest,
    ) -> cloudsso_20210515_models.DeleteAccessAssignmentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_access_assignment_with_options_async(request, runtime)

    def delete_access_configuration_with_options(
        self,
        request: cloudsso_20210515_models.DeleteAccessConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.DeleteAccessConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccessConfigurationId'] = request.access_configuration_id
        query['DirectoryId'] = request.directory_id
        query['ForceRemovePermissionPolicies'] = request.force_remove_permission_policies
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteAccessConfiguration',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.DeleteAccessConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_access_configuration_with_options_async(
        self,
        request: cloudsso_20210515_models.DeleteAccessConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.DeleteAccessConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccessConfigurationId'] = request.access_configuration_id
        query['DirectoryId'] = request.directory_id
        query['ForceRemovePermissionPolicies'] = request.force_remove_permission_policies
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteAccessConfiguration',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.DeleteAccessConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_access_configuration(
        self,
        request: cloudsso_20210515_models.DeleteAccessConfigurationRequest,
    ) -> cloudsso_20210515_models.DeleteAccessConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_access_configuration_with_options(request, runtime)

    async def delete_access_configuration_async(
        self,
        request: cloudsso_20210515_models.DeleteAccessConfigurationRequest,
    ) -> cloudsso_20210515_models.DeleteAccessConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_access_configuration_with_options_async(request, runtime)

    def delete_directory_with_options(
        self,
        request: cloudsso_20210515_models.DeleteDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.DeleteDirectoryResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteDirectory',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.DeleteDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_directory_with_options_async(
        self,
        request: cloudsso_20210515_models.DeleteDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.DeleteDirectoryResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteDirectory',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.DeleteDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_directory(
        self,
        request: cloudsso_20210515_models.DeleteDirectoryRequest,
    ) -> cloudsso_20210515_models.DeleteDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_directory_with_options(request, runtime)

    async def delete_directory_async(
        self,
        request: cloudsso_20210515_models.DeleteDirectoryRequest,
    ) -> cloudsso_20210515_models.DeleteDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_directory_with_options_async(request, runtime)

    def delete_group_with_options(
        self,
        request: cloudsso_20210515_models.DeleteGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.DeleteGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteGroup',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.DeleteGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_group_with_options_async(
        self,
        request: cloudsso_20210515_models.DeleteGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.DeleteGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteGroup',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.DeleteGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_group(
        self,
        request: cloudsso_20210515_models.DeleteGroupRequest,
    ) -> cloudsso_20210515_models.DeleteGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_group_with_options(request, runtime)

    async def delete_group_async(
        self,
        request: cloudsso_20210515_models.DeleteGroupRequest,
    ) -> cloudsso_20210515_models.DeleteGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_group_with_options_async(request, runtime)

    def delete_mfadevice_for_user_with_options(
        self,
        request: cloudsso_20210515_models.DeleteMFADeviceForUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.DeleteMFADeviceForUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        query['MFADeviceId'] = request.mfadevice_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteMFADeviceForUser',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.DeleteMFADeviceForUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_mfadevice_for_user_with_options_async(
        self,
        request: cloudsso_20210515_models.DeleteMFADeviceForUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.DeleteMFADeviceForUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        query['MFADeviceId'] = request.mfadevice_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteMFADeviceForUser',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.DeleteMFADeviceForUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_mfadevice_for_user(
        self,
        request: cloudsso_20210515_models.DeleteMFADeviceForUserRequest,
    ) -> cloudsso_20210515_models.DeleteMFADeviceForUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_mfadevice_for_user_with_options(request, runtime)

    async def delete_mfadevice_for_user_async(
        self,
        request: cloudsso_20210515_models.DeleteMFADeviceForUserRequest,
    ) -> cloudsso_20210515_models.DeleteMFADeviceForUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_mfadevice_for_user_with_options_async(request, runtime)

    def delete_scimserver_credential_with_options(
        self,
        request: cloudsso_20210515_models.DeleteSCIMServerCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.DeleteSCIMServerCredentialResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CredentialId'] = request.credential_id
        query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteSCIMServerCredential',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.DeleteSCIMServerCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_scimserver_credential_with_options_async(
        self,
        request: cloudsso_20210515_models.DeleteSCIMServerCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.DeleteSCIMServerCredentialResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CredentialId'] = request.credential_id
        query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteSCIMServerCredential',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.DeleteSCIMServerCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_scimserver_credential(
        self,
        request: cloudsso_20210515_models.DeleteSCIMServerCredentialRequest,
    ) -> cloudsso_20210515_models.DeleteSCIMServerCredentialResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_scimserver_credential_with_options(request, runtime)

    async def delete_scimserver_credential_async(
        self,
        request: cloudsso_20210515_models.DeleteSCIMServerCredentialRequest,
    ) -> cloudsso_20210515_models.DeleteSCIMServerCredentialResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_scimserver_credential_with_options_async(request, runtime)

    def delete_user_with_options(
        self,
        request: cloudsso_20210515_models.DeleteUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.DeleteUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteUser',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.DeleteUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_with_options_async(
        self,
        request: cloudsso_20210515_models.DeleteUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.DeleteUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteUser',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.DeleteUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user(
        self,
        request: cloudsso_20210515_models.DeleteUserRequest,
    ) -> cloudsso_20210515_models.DeleteUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_user_with_options(request, runtime)

    async def delete_user_async(
        self,
        request: cloudsso_20210515_models.DeleteUserRequest,
    ) -> cloudsso_20210515_models.DeleteUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_with_options_async(request, runtime)

    def deprovision_access_configuration_with_options(
        self,
        request: cloudsso_20210515_models.DeprovisionAccessConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.DeprovisionAccessConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccessConfigurationId'] = request.access_configuration_id
        query['DirectoryId'] = request.directory_id
        query['TargetId'] = request.target_id
        query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeprovisionAccessConfiguration',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.DeprovisionAccessConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def deprovision_access_configuration_with_options_async(
        self,
        request: cloudsso_20210515_models.DeprovisionAccessConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.DeprovisionAccessConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccessConfigurationId'] = request.access_configuration_id
        query['DirectoryId'] = request.directory_id
        query['TargetId'] = request.target_id
        query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeprovisionAccessConfiguration',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.DeprovisionAccessConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deprovision_access_configuration(
        self,
        request: cloudsso_20210515_models.DeprovisionAccessConfigurationRequest,
    ) -> cloudsso_20210515_models.DeprovisionAccessConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return self.deprovision_access_configuration_with_options(request, runtime)

    async def deprovision_access_configuration_async(
        self,
        request: cloudsso_20210515_models.DeprovisionAccessConfigurationRequest,
    ) -> cloudsso_20210515_models.DeprovisionAccessConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.deprovision_access_configuration_with_options_async(request, runtime)

    def disable_service_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.DisableServiceResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DisableService',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.DisableServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_service_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.DisableServiceResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DisableService',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.DisableServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_service(self) -> cloudsso_20210515_models.DisableServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_service_with_options(runtime)

    async def disable_service_async(self) -> cloudsso_20210515_models.DisableServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_service_with_options_async(runtime)

    def enable_service_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.EnableServiceResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='EnableService',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.EnableServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_service_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.EnableServiceResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='EnableService',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.EnableServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_service(self) -> cloudsso_20210515_models.EnableServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_service_with_options(runtime)

    async def enable_service_async(self) -> cloudsso_20210515_models.EnableServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_service_with_options_async(runtime)

    def get_access_configuration_with_options(
        self,
        request: cloudsso_20210515_models.GetAccessConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.GetAccessConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccessConfigurationId'] = request.access_configuration_id
        query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetAccessConfiguration',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.GetAccessConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_access_configuration_with_options_async(
        self,
        request: cloudsso_20210515_models.GetAccessConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.GetAccessConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccessConfigurationId'] = request.access_configuration_id
        query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetAccessConfiguration',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.GetAccessConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_access_configuration(
        self,
        request: cloudsso_20210515_models.GetAccessConfigurationRequest,
    ) -> cloudsso_20210515_models.GetAccessConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_access_configuration_with_options(request, runtime)

    async def get_access_configuration_async(
        self,
        request: cloudsso_20210515_models.GetAccessConfigurationRequest,
    ) -> cloudsso_20210515_models.GetAccessConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_access_configuration_with_options_async(request, runtime)

    def get_directory_with_options(
        self,
        request: cloudsso_20210515_models.GetDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.GetDirectoryResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetDirectory',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.GetDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_directory_with_options_async(
        self,
        request: cloudsso_20210515_models.GetDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.GetDirectoryResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetDirectory',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.GetDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_directory(
        self,
        request: cloudsso_20210515_models.GetDirectoryRequest,
    ) -> cloudsso_20210515_models.GetDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_directory_with_options(request, runtime)

    async def get_directory_async(
        self,
        request: cloudsso_20210515_models.GetDirectoryRequest,
    ) -> cloudsso_20210515_models.GetDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_directory_with_options_async(request, runtime)

    def get_directory_samlservice_provider_info_with_options(
        self,
        request: cloudsso_20210515_models.GetDirectorySAMLServiceProviderInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.GetDirectorySAMLServiceProviderInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetDirectorySAMLServiceProviderInfo',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.GetDirectorySAMLServiceProviderInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_directory_samlservice_provider_info_with_options_async(
        self,
        request: cloudsso_20210515_models.GetDirectorySAMLServiceProviderInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.GetDirectorySAMLServiceProviderInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetDirectorySAMLServiceProviderInfo',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.GetDirectorySAMLServiceProviderInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_directory_samlservice_provider_info(
        self,
        request: cloudsso_20210515_models.GetDirectorySAMLServiceProviderInfoRequest,
    ) -> cloudsso_20210515_models.GetDirectorySAMLServiceProviderInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_directory_samlservice_provider_info_with_options(request, runtime)

    async def get_directory_samlservice_provider_info_async(
        self,
        request: cloudsso_20210515_models.GetDirectorySAMLServiceProviderInfoRequest,
    ) -> cloudsso_20210515_models.GetDirectorySAMLServiceProviderInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_directory_samlservice_provider_info_with_options_async(request, runtime)

    def get_directory_statistics_with_options(
        self,
        request: cloudsso_20210515_models.GetDirectoryStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.GetDirectoryStatisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetDirectoryStatistics',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.GetDirectoryStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_directory_statistics_with_options_async(
        self,
        request: cloudsso_20210515_models.GetDirectoryStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.GetDirectoryStatisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetDirectoryStatistics',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.GetDirectoryStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_directory_statistics(
        self,
        request: cloudsso_20210515_models.GetDirectoryStatisticsRequest,
    ) -> cloudsso_20210515_models.GetDirectoryStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_directory_statistics_with_options(request, runtime)

    async def get_directory_statistics_async(
        self,
        request: cloudsso_20210515_models.GetDirectoryStatisticsRequest,
    ) -> cloudsso_20210515_models.GetDirectoryStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_directory_statistics_with_options_async(request, runtime)

    def get_external_samlidentity_provider_with_options(
        self,
        request: cloudsso_20210515_models.GetExternalSAMLIdentityProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.GetExternalSAMLIdentityProviderResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetExternalSAMLIdentityProvider',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.GetExternalSAMLIdentityProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_external_samlidentity_provider_with_options_async(
        self,
        request: cloudsso_20210515_models.GetExternalSAMLIdentityProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.GetExternalSAMLIdentityProviderResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetExternalSAMLIdentityProvider',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.GetExternalSAMLIdentityProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_external_samlidentity_provider(
        self,
        request: cloudsso_20210515_models.GetExternalSAMLIdentityProviderRequest,
    ) -> cloudsso_20210515_models.GetExternalSAMLIdentityProviderResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_external_samlidentity_provider_with_options(request, runtime)

    async def get_external_samlidentity_provider_async(
        self,
        request: cloudsso_20210515_models.GetExternalSAMLIdentityProviderRequest,
    ) -> cloudsso_20210515_models.GetExternalSAMLIdentityProviderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_external_samlidentity_provider_with_options_async(request, runtime)

    def get_group_with_options(
        self,
        request: cloudsso_20210515_models.GetGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.GetGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetGroup',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.GetGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_group_with_options_async(
        self,
        request: cloudsso_20210515_models.GetGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.GetGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetGroup',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.GetGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_group(
        self,
        request: cloudsso_20210515_models.GetGroupRequest,
    ) -> cloudsso_20210515_models.GetGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_group_with_options(request, runtime)

    async def get_group_async(
        self,
        request: cloudsso_20210515_models.GetGroupRequest,
    ) -> cloudsso_20210515_models.GetGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_group_with_options_async(request, runtime)

    def get_mfaauthentication_status_with_options(
        self,
        request: cloudsso_20210515_models.GetMFAAuthenticationStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.GetMFAAuthenticationStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetMFAAuthenticationStatus',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.GetMFAAuthenticationStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mfaauthentication_status_with_options_async(
        self,
        request: cloudsso_20210515_models.GetMFAAuthenticationStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.GetMFAAuthenticationStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetMFAAuthenticationStatus',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.GetMFAAuthenticationStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mfaauthentication_status(
        self,
        request: cloudsso_20210515_models.GetMFAAuthenticationStatusRequest,
    ) -> cloudsso_20210515_models.GetMFAAuthenticationStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_mfaauthentication_status_with_options(request, runtime)

    async def get_mfaauthentication_status_async(
        self,
        request: cloudsso_20210515_models.GetMFAAuthenticationStatusRequest,
    ) -> cloudsso_20210515_models.GetMFAAuthenticationStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_mfaauthentication_status_with_options_async(request, runtime)

    def get_scimsynchronization_status_with_options(
        self,
        request: cloudsso_20210515_models.GetSCIMSynchronizationStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.GetSCIMSynchronizationStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetSCIMSynchronizationStatus',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.GetSCIMSynchronizationStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_scimsynchronization_status_with_options_async(
        self,
        request: cloudsso_20210515_models.GetSCIMSynchronizationStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.GetSCIMSynchronizationStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetSCIMSynchronizationStatus',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.GetSCIMSynchronizationStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_scimsynchronization_status(
        self,
        request: cloudsso_20210515_models.GetSCIMSynchronizationStatusRequest,
    ) -> cloudsso_20210515_models.GetSCIMSynchronizationStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_scimsynchronization_status_with_options(request, runtime)

    async def get_scimsynchronization_status_async(
        self,
        request: cloudsso_20210515_models.GetSCIMSynchronizationStatusRequest,
    ) -> cloudsso_20210515_models.GetSCIMSynchronizationStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_scimsynchronization_status_with_options_async(request, runtime)

    def get_service_status_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.GetServiceStatusResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetServiceStatus',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.GetServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_status_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.GetServiceStatusResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetServiceStatus',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.GetServiceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_status(self) -> cloudsso_20210515_models.GetServiceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_service_status_with_options(runtime)

    async def get_service_status_async(self) -> cloudsso_20210515_models.GetServiceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_service_status_with_options_async(runtime)

    def get_task_with_options(
        self,
        request: cloudsso_20210515_models.GetTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.GetTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetTask',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.GetTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_with_options_async(
        self,
        request: cloudsso_20210515_models.GetTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.GetTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetTask',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.GetTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task(
        self,
        request: cloudsso_20210515_models.GetTaskRequest,
    ) -> cloudsso_20210515_models.GetTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_task_with_options(request, runtime)

    async def get_task_async(
        self,
        request: cloudsso_20210515_models.GetTaskRequest,
    ) -> cloudsso_20210515_models.GetTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_task_with_options_async(request, runtime)

    def get_task_status_with_options(
        self,
        request: cloudsso_20210515_models.GetTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.GetTaskStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetTaskStatus',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.GetTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_status_with_options_async(
        self,
        request: cloudsso_20210515_models.GetTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.GetTaskStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetTaskStatus',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.GetTaskStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task_status(
        self,
        request: cloudsso_20210515_models.GetTaskStatusRequest,
    ) -> cloudsso_20210515_models.GetTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_task_status_with_options(request, runtime)

    async def get_task_status_async(
        self,
        request: cloudsso_20210515_models.GetTaskStatusRequest,
    ) -> cloudsso_20210515_models.GetTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_task_status_with_options_async(request, runtime)

    def get_user_with_options(
        self,
        request: cloudsso_20210515_models.GetUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.GetUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetUser',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.GetUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_with_options_async(
        self,
        request: cloudsso_20210515_models.GetUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.GetUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetUser',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.GetUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user(
        self,
        request: cloudsso_20210515_models.GetUserRequest,
    ) -> cloudsso_20210515_models.GetUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_user_with_options(request, runtime)

    async def get_user_async(
        self,
        request: cloudsso_20210515_models.GetUserRequest,
    ) -> cloudsso_20210515_models.GetUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_user_with_options_async(request, runtime)

    def list_access_assignments_with_options(
        self,
        request: cloudsso_20210515_models.ListAccessAssignmentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.ListAccessAssignmentsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccessConfigurationId'] = request.access_configuration_id
        query['DirectoryId'] = request.directory_id
        query['MaxResults'] = request.max_results
        query['NextToken'] = request.next_token
        query['PrincipalId'] = request.principal_id
        query['PrincipalType'] = request.principal_type
        query['TargetId'] = request.target_id
        query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListAccessAssignments',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.ListAccessAssignmentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_access_assignments_with_options_async(
        self,
        request: cloudsso_20210515_models.ListAccessAssignmentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.ListAccessAssignmentsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccessConfigurationId'] = request.access_configuration_id
        query['DirectoryId'] = request.directory_id
        query['MaxResults'] = request.max_results
        query['NextToken'] = request.next_token
        query['PrincipalId'] = request.principal_id
        query['PrincipalType'] = request.principal_type
        query['TargetId'] = request.target_id
        query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListAccessAssignments',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.ListAccessAssignmentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_access_assignments(
        self,
        request: cloudsso_20210515_models.ListAccessAssignmentsRequest,
    ) -> cloudsso_20210515_models.ListAccessAssignmentsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_access_assignments_with_options(request, runtime)

    async def list_access_assignments_async(
        self,
        request: cloudsso_20210515_models.ListAccessAssignmentsRequest,
    ) -> cloudsso_20210515_models.ListAccessAssignmentsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_access_assignments_with_options_async(request, runtime)

    def list_access_configuration_provisionings_with_options(
        self,
        request: cloudsso_20210515_models.ListAccessConfigurationProvisioningsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.ListAccessConfigurationProvisioningsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccessConfigurationId'] = request.access_configuration_id
        query['DirectoryId'] = request.directory_id
        query['MaxResults'] = request.max_results
        query['NextToken'] = request.next_token
        query['ProvisioningStatus'] = request.provisioning_status
        query['TargetId'] = request.target_id
        query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListAccessConfigurationProvisionings',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.ListAccessConfigurationProvisioningsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_access_configuration_provisionings_with_options_async(
        self,
        request: cloudsso_20210515_models.ListAccessConfigurationProvisioningsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.ListAccessConfigurationProvisioningsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccessConfigurationId'] = request.access_configuration_id
        query['DirectoryId'] = request.directory_id
        query['MaxResults'] = request.max_results
        query['NextToken'] = request.next_token
        query['ProvisioningStatus'] = request.provisioning_status
        query['TargetId'] = request.target_id
        query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListAccessConfigurationProvisionings',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.ListAccessConfigurationProvisioningsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_access_configuration_provisionings(
        self,
        request: cloudsso_20210515_models.ListAccessConfigurationProvisioningsRequest,
    ) -> cloudsso_20210515_models.ListAccessConfigurationProvisioningsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_access_configuration_provisionings_with_options(request, runtime)

    async def list_access_configuration_provisionings_async(
        self,
        request: cloudsso_20210515_models.ListAccessConfigurationProvisioningsRequest,
    ) -> cloudsso_20210515_models.ListAccessConfigurationProvisioningsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_access_configuration_provisionings_with_options_async(request, runtime)

    def list_access_configurations_with_options(
        self,
        request: cloudsso_20210515_models.ListAccessConfigurationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.ListAccessConfigurationsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        query['Filter'] = request.filter
        query['MaxResults'] = request.max_results
        query['NextToken'] = request.next_token
        query['StatusNotifications'] = request.status_notifications
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListAccessConfigurations',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.ListAccessConfigurationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_access_configurations_with_options_async(
        self,
        request: cloudsso_20210515_models.ListAccessConfigurationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.ListAccessConfigurationsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        query['Filter'] = request.filter
        query['MaxResults'] = request.max_results
        query['NextToken'] = request.next_token
        query['StatusNotifications'] = request.status_notifications
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListAccessConfigurations',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.ListAccessConfigurationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_access_configurations(
        self,
        request: cloudsso_20210515_models.ListAccessConfigurationsRequest,
    ) -> cloudsso_20210515_models.ListAccessConfigurationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_access_configurations_with_options(request, runtime)

    async def list_access_configurations_async(
        self,
        request: cloudsso_20210515_models.ListAccessConfigurationsRequest,
    ) -> cloudsso_20210515_models.ListAccessConfigurationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_access_configurations_with_options_async(request, runtime)

    def list_directories_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.ListDirectoriesResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListDirectories',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.ListDirectoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_directories_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.ListDirectoriesResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListDirectories',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.ListDirectoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_directories(self) -> cloudsso_20210515_models.ListDirectoriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_directories_with_options(runtime)

    async def list_directories_async(self) -> cloudsso_20210515_models.ListDirectoriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_directories_with_options_async(runtime)

    def list_external_samlid_pcertificates_with_options(
        self,
        request: cloudsso_20210515_models.ListExternalSAMLIdPCertificatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.ListExternalSAMLIdPCertificatesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListExternalSAMLIdPCertificates',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.ListExternalSAMLIdPCertificatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_external_samlid_pcertificates_with_options_async(
        self,
        request: cloudsso_20210515_models.ListExternalSAMLIdPCertificatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.ListExternalSAMLIdPCertificatesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListExternalSAMLIdPCertificates',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.ListExternalSAMLIdPCertificatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_external_samlid_pcertificates(
        self,
        request: cloudsso_20210515_models.ListExternalSAMLIdPCertificatesRequest,
    ) -> cloudsso_20210515_models.ListExternalSAMLIdPCertificatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_external_samlid_pcertificates_with_options(request, runtime)

    async def list_external_samlid_pcertificates_async(
        self,
        request: cloudsso_20210515_models.ListExternalSAMLIdPCertificatesRequest,
    ) -> cloudsso_20210515_models.ListExternalSAMLIdPCertificatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_external_samlid_pcertificates_with_options_async(request, runtime)

    def list_group_members_with_options(
        self,
        request: cloudsso_20210515_models.ListGroupMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.ListGroupMembersResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        query['GroupId'] = request.group_id
        query['MaxResults'] = request.max_results
        query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListGroupMembers',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.ListGroupMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_group_members_with_options_async(
        self,
        request: cloudsso_20210515_models.ListGroupMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.ListGroupMembersResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        query['GroupId'] = request.group_id
        query['MaxResults'] = request.max_results
        query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListGroupMembers',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.ListGroupMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_group_members(
        self,
        request: cloudsso_20210515_models.ListGroupMembersRequest,
    ) -> cloudsso_20210515_models.ListGroupMembersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_group_members_with_options(request, runtime)

    async def list_group_members_async(
        self,
        request: cloudsso_20210515_models.ListGroupMembersRequest,
    ) -> cloudsso_20210515_models.ListGroupMembersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_group_members_with_options_async(request, runtime)

    def list_groups_with_options(
        self,
        request: cloudsso_20210515_models.ListGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.ListGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        query['Filter'] = request.filter
        query['MaxResults'] = request.max_results
        query['NextToken'] = request.next_token
        query['ProvisionType'] = request.provision_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListGroups',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.ListGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_groups_with_options_async(
        self,
        request: cloudsso_20210515_models.ListGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.ListGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        query['Filter'] = request.filter
        query['MaxResults'] = request.max_results
        query['NextToken'] = request.next_token
        query['ProvisionType'] = request.provision_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListGroups',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.ListGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_groups(
        self,
        request: cloudsso_20210515_models.ListGroupsRequest,
    ) -> cloudsso_20210515_models.ListGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_groups_with_options(request, runtime)

    async def list_groups_async(
        self,
        request: cloudsso_20210515_models.ListGroupsRequest,
    ) -> cloudsso_20210515_models.ListGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_groups_with_options_async(request, runtime)

    def list_joined_groups_for_user_with_options(
        self,
        request: cloudsso_20210515_models.ListJoinedGroupsForUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.ListJoinedGroupsForUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        query['MaxResults'] = request.max_results
        query['NextToken'] = request.next_token
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListJoinedGroupsForUser',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.ListJoinedGroupsForUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_joined_groups_for_user_with_options_async(
        self,
        request: cloudsso_20210515_models.ListJoinedGroupsForUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.ListJoinedGroupsForUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        query['MaxResults'] = request.max_results
        query['NextToken'] = request.next_token
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListJoinedGroupsForUser',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.ListJoinedGroupsForUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_joined_groups_for_user(
        self,
        request: cloudsso_20210515_models.ListJoinedGroupsForUserRequest,
    ) -> cloudsso_20210515_models.ListJoinedGroupsForUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_joined_groups_for_user_with_options(request, runtime)

    async def list_joined_groups_for_user_async(
        self,
        request: cloudsso_20210515_models.ListJoinedGroupsForUserRequest,
    ) -> cloudsso_20210515_models.ListJoinedGroupsForUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_joined_groups_for_user_with_options_async(request, runtime)

    def list_mfadevices_for_user_with_options(
        self,
        request: cloudsso_20210515_models.ListMFADevicesForUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.ListMFADevicesForUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListMFADevicesForUser',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.ListMFADevicesForUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mfadevices_for_user_with_options_async(
        self,
        request: cloudsso_20210515_models.ListMFADevicesForUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.ListMFADevicesForUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListMFADevicesForUser',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.ListMFADevicesForUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mfadevices_for_user(
        self,
        request: cloudsso_20210515_models.ListMFADevicesForUserRequest,
    ) -> cloudsso_20210515_models.ListMFADevicesForUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_mfadevices_for_user_with_options(request, runtime)

    async def list_mfadevices_for_user_async(
        self,
        request: cloudsso_20210515_models.ListMFADevicesForUserRequest,
    ) -> cloudsso_20210515_models.ListMFADevicesForUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_mfadevices_for_user_with_options_async(request, runtime)

    def list_permission_policies_in_access_configuration_with_options(
        self,
        request: cloudsso_20210515_models.ListPermissionPoliciesInAccessConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.ListPermissionPoliciesInAccessConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccessConfigurationId'] = request.access_configuration_id
        query['DirectoryId'] = request.directory_id
        query['PermissionPolicyType'] = request.permission_policy_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListPermissionPoliciesInAccessConfiguration',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.ListPermissionPoliciesInAccessConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_permission_policies_in_access_configuration_with_options_async(
        self,
        request: cloudsso_20210515_models.ListPermissionPoliciesInAccessConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.ListPermissionPoliciesInAccessConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccessConfigurationId'] = request.access_configuration_id
        query['DirectoryId'] = request.directory_id
        query['PermissionPolicyType'] = request.permission_policy_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListPermissionPoliciesInAccessConfiguration',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.ListPermissionPoliciesInAccessConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_permission_policies_in_access_configuration(
        self,
        request: cloudsso_20210515_models.ListPermissionPoliciesInAccessConfigurationRequest,
    ) -> cloudsso_20210515_models.ListPermissionPoliciesInAccessConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_permission_policies_in_access_configuration_with_options(request, runtime)

    async def list_permission_policies_in_access_configuration_async(
        self,
        request: cloudsso_20210515_models.ListPermissionPoliciesInAccessConfigurationRequest,
    ) -> cloudsso_20210515_models.ListPermissionPoliciesInAccessConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_permission_policies_in_access_configuration_with_options_async(request, runtime)

    def list_scimserver_credentials_with_options(
        self,
        request: cloudsso_20210515_models.ListSCIMServerCredentialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.ListSCIMServerCredentialsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListSCIMServerCredentials',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.ListSCIMServerCredentialsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_scimserver_credentials_with_options_async(
        self,
        request: cloudsso_20210515_models.ListSCIMServerCredentialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.ListSCIMServerCredentialsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListSCIMServerCredentials',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.ListSCIMServerCredentialsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_scimserver_credentials(
        self,
        request: cloudsso_20210515_models.ListSCIMServerCredentialsRequest,
    ) -> cloudsso_20210515_models.ListSCIMServerCredentialsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_scimserver_credentials_with_options(request, runtime)

    async def list_scimserver_credentials_async(
        self,
        request: cloudsso_20210515_models.ListSCIMServerCredentialsRequest,
    ) -> cloudsso_20210515_models.ListSCIMServerCredentialsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_scimserver_credentials_with_options_async(request, runtime)

    def list_tasks_with_options(
        self,
        request: cloudsso_20210515_models.ListTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.ListTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccessConfigurationId'] = request.access_configuration_id
        query['DirectoryId'] = request.directory_id
        query['Filter'] = request.filter
        query['MaxResults'] = request.max_results
        query['NextToken'] = request.next_token
        query['PrincipalId'] = request.principal_id
        query['PrincipalType'] = request.principal_type
        query['Status'] = request.status
        query['TargetId'] = request.target_id
        query['TargetType'] = request.target_type
        query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListTasks',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.ListTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tasks_with_options_async(
        self,
        request: cloudsso_20210515_models.ListTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.ListTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccessConfigurationId'] = request.access_configuration_id
        query['DirectoryId'] = request.directory_id
        query['Filter'] = request.filter
        query['MaxResults'] = request.max_results
        query['NextToken'] = request.next_token
        query['PrincipalId'] = request.principal_id
        query['PrincipalType'] = request.principal_type
        query['Status'] = request.status
        query['TargetId'] = request.target_id
        query['TargetType'] = request.target_type
        query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListTasks',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.ListTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tasks(
        self,
        request: cloudsso_20210515_models.ListTasksRequest,
    ) -> cloudsso_20210515_models.ListTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tasks_with_options(request, runtime)

    async def list_tasks_async(
        self,
        request: cloudsso_20210515_models.ListTasksRequest,
    ) -> cloudsso_20210515_models.ListTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tasks_with_options_async(request, runtime)

    def list_users_with_options(
        self,
        request: cloudsso_20210515_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.ListUsersResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        query['Filter'] = request.filter
        query['MaxResults'] = request.max_results
        query['NextToken'] = request.next_token
        query['ProvisionType'] = request.provision_type
        query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListUsers',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.ListUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_users_with_options_async(
        self,
        request: cloudsso_20210515_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.ListUsersResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        query['Filter'] = request.filter
        query['MaxResults'] = request.max_results
        query['NextToken'] = request.next_token
        query['ProvisionType'] = request.provision_type
        query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListUsers',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.ListUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_users(
        self,
        request: cloudsso_20210515_models.ListUsersRequest,
    ) -> cloudsso_20210515_models.ListUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_users_with_options(request, runtime)

    async def list_users_async(
        self,
        request: cloudsso_20210515_models.ListUsersRequest,
    ) -> cloudsso_20210515_models.ListUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_users_with_options_async(request, runtime)

    def provision_access_configuration_with_options(
        self,
        request: cloudsso_20210515_models.ProvisionAccessConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.ProvisionAccessConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccessConfigurationId'] = request.access_configuration_id
        query['DirectoryId'] = request.directory_id
        query['TargetId'] = request.target_id
        query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ProvisionAccessConfiguration',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.ProvisionAccessConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def provision_access_configuration_with_options_async(
        self,
        request: cloudsso_20210515_models.ProvisionAccessConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.ProvisionAccessConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccessConfigurationId'] = request.access_configuration_id
        query['DirectoryId'] = request.directory_id
        query['TargetId'] = request.target_id
        query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ProvisionAccessConfiguration',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.ProvisionAccessConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def provision_access_configuration(
        self,
        request: cloudsso_20210515_models.ProvisionAccessConfigurationRequest,
    ) -> cloudsso_20210515_models.ProvisionAccessConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return self.provision_access_configuration_with_options(request, runtime)

    async def provision_access_configuration_async(
        self,
        request: cloudsso_20210515_models.ProvisionAccessConfigurationRequest,
    ) -> cloudsso_20210515_models.ProvisionAccessConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.provision_access_configuration_with_options_async(request, runtime)

    def remove_external_samlid_pcertificate_with_options(
        self,
        request: cloudsso_20210515_models.RemoveExternalSAMLIdPCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.RemoveExternalSAMLIdPCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CertificateId'] = request.certificate_id
        query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveExternalSAMLIdPCertificate',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.RemoveExternalSAMLIdPCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_external_samlid_pcertificate_with_options_async(
        self,
        request: cloudsso_20210515_models.RemoveExternalSAMLIdPCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.RemoveExternalSAMLIdPCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CertificateId'] = request.certificate_id
        query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveExternalSAMLIdPCertificate',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.RemoveExternalSAMLIdPCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_external_samlid_pcertificate(
        self,
        request: cloudsso_20210515_models.RemoveExternalSAMLIdPCertificateRequest,
    ) -> cloudsso_20210515_models.RemoveExternalSAMLIdPCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_external_samlid_pcertificate_with_options(request, runtime)

    async def remove_external_samlid_pcertificate_async(
        self,
        request: cloudsso_20210515_models.RemoveExternalSAMLIdPCertificateRequest,
    ) -> cloudsso_20210515_models.RemoveExternalSAMLIdPCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_external_samlid_pcertificate_with_options_async(request, runtime)

    def remove_permission_policy_from_access_configuration_with_options(
        self,
        request: cloudsso_20210515_models.RemovePermissionPolicyFromAccessConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.RemovePermissionPolicyFromAccessConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccessConfigurationId'] = request.access_configuration_id
        query['DirectoryId'] = request.directory_id
        query['PermissionPolicyName'] = request.permission_policy_name
        query['PermissionPolicyType'] = request.permission_policy_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemovePermissionPolicyFromAccessConfiguration',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.RemovePermissionPolicyFromAccessConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_permission_policy_from_access_configuration_with_options_async(
        self,
        request: cloudsso_20210515_models.RemovePermissionPolicyFromAccessConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.RemovePermissionPolicyFromAccessConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccessConfigurationId'] = request.access_configuration_id
        query['DirectoryId'] = request.directory_id
        query['PermissionPolicyName'] = request.permission_policy_name
        query['PermissionPolicyType'] = request.permission_policy_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemovePermissionPolicyFromAccessConfiguration',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.RemovePermissionPolicyFromAccessConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_permission_policy_from_access_configuration(
        self,
        request: cloudsso_20210515_models.RemovePermissionPolicyFromAccessConfigurationRequest,
    ) -> cloudsso_20210515_models.RemovePermissionPolicyFromAccessConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_permission_policy_from_access_configuration_with_options(request, runtime)

    async def remove_permission_policy_from_access_configuration_async(
        self,
        request: cloudsso_20210515_models.RemovePermissionPolicyFromAccessConfigurationRequest,
    ) -> cloudsso_20210515_models.RemovePermissionPolicyFromAccessConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_permission_policy_from_access_configuration_with_options_async(request, runtime)

    def remove_user_from_group_with_options(
        self,
        request: cloudsso_20210515_models.RemoveUserFromGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.RemoveUserFromGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        query['GroupId'] = request.group_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveUserFromGroup',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.RemoveUserFromGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_user_from_group_with_options_async(
        self,
        request: cloudsso_20210515_models.RemoveUserFromGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.RemoveUserFromGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        query['GroupId'] = request.group_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveUserFromGroup',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.RemoveUserFromGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_user_from_group(
        self,
        request: cloudsso_20210515_models.RemoveUserFromGroupRequest,
    ) -> cloudsso_20210515_models.RemoveUserFromGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_user_from_group_with_options(request, runtime)

    async def remove_user_from_group_async(
        self,
        request: cloudsso_20210515_models.RemoveUserFromGroupRequest,
    ) -> cloudsso_20210515_models.RemoveUserFromGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_user_from_group_with_options_async(request, runtime)

    def reset_user_password_with_options(
        self,
        request: cloudsso_20210515_models.ResetUserPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.ResetUserPasswordResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        query['GenerateRandomPassword'] = request.generate_random_password
        query['Password'] = request.password
        query['RequirePasswordResetForNextLogin'] = request.require_password_reset_for_next_login
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ResetUserPassword',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.ResetUserPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_user_password_with_options_async(
        self,
        request: cloudsso_20210515_models.ResetUserPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.ResetUserPasswordResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        query['GenerateRandomPassword'] = request.generate_random_password
        query['Password'] = request.password
        query['RequirePasswordResetForNextLogin'] = request.require_password_reset_for_next_login
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ResetUserPassword',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.ResetUserPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_user_password(
        self,
        request: cloudsso_20210515_models.ResetUserPasswordRequest,
    ) -> cloudsso_20210515_models.ResetUserPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_user_password_with_options(request, runtime)

    async def reset_user_password_async(
        self,
        request: cloudsso_20210515_models.ResetUserPasswordRequest,
    ) -> cloudsso_20210515_models.ResetUserPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_user_password_with_options_async(request, runtime)

    def set_external_samlidentity_provider_with_options(
        self,
        request: cloudsso_20210515_models.SetExternalSAMLIdentityProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.SetExternalSAMLIdentityProviderResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        query['EncodedMetadataDocument'] = request.encoded_metadata_document
        query['EntityId'] = request.entity_id
        query['LoginUrl'] = request.login_url
        query['SSOStatus'] = request.ssostatus
        query['WantRequestSigned'] = request.want_request_signed
        query['X509Certificate'] = request.x_509certificate
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetExternalSAMLIdentityProvider',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.SetExternalSAMLIdentityProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_external_samlidentity_provider_with_options_async(
        self,
        request: cloudsso_20210515_models.SetExternalSAMLIdentityProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.SetExternalSAMLIdentityProviderResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        query['EncodedMetadataDocument'] = request.encoded_metadata_document
        query['EntityId'] = request.entity_id
        query['LoginUrl'] = request.login_url
        query['SSOStatus'] = request.ssostatus
        query['WantRequestSigned'] = request.want_request_signed
        query['X509Certificate'] = request.x_509certificate
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetExternalSAMLIdentityProvider',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.SetExternalSAMLIdentityProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_external_samlidentity_provider(
        self,
        request: cloudsso_20210515_models.SetExternalSAMLIdentityProviderRequest,
    ) -> cloudsso_20210515_models.SetExternalSAMLIdentityProviderResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_external_samlidentity_provider_with_options(request, runtime)

    async def set_external_samlidentity_provider_async(
        self,
        request: cloudsso_20210515_models.SetExternalSAMLIdentityProviderRequest,
    ) -> cloudsso_20210515_models.SetExternalSAMLIdentityProviderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_external_samlidentity_provider_with_options_async(request, runtime)

    def set_mfaauthentication_status_with_options(
        self,
        request: cloudsso_20210515_models.SetMFAAuthenticationStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.SetMFAAuthenticationStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        query['MFAAuthenticationStatus'] = request.mfaauthentication_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetMFAAuthenticationStatus',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.SetMFAAuthenticationStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_mfaauthentication_status_with_options_async(
        self,
        request: cloudsso_20210515_models.SetMFAAuthenticationStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.SetMFAAuthenticationStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        query['MFAAuthenticationStatus'] = request.mfaauthentication_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetMFAAuthenticationStatus',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.SetMFAAuthenticationStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_mfaauthentication_status(
        self,
        request: cloudsso_20210515_models.SetMFAAuthenticationStatusRequest,
    ) -> cloudsso_20210515_models.SetMFAAuthenticationStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_mfaauthentication_status_with_options(request, runtime)

    async def set_mfaauthentication_status_async(
        self,
        request: cloudsso_20210515_models.SetMFAAuthenticationStatusRequest,
    ) -> cloudsso_20210515_models.SetMFAAuthenticationStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_mfaauthentication_status_with_options_async(request, runtime)

    def set_scimsynchronization_status_with_options(
        self,
        request: cloudsso_20210515_models.SetSCIMSynchronizationStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.SetSCIMSynchronizationStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        query['SCIMSynchronizationStatus'] = request.scimsynchronization_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetSCIMSynchronizationStatus',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.SetSCIMSynchronizationStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_scimsynchronization_status_with_options_async(
        self,
        request: cloudsso_20210515_models.SetSCIMSynchronizationStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.SetSCIMSynchronizationStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        query['SCIMSynchronizationStatus'] = request.scimsynchronization_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetSCIMSynchronizationStatus',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.SetSCIMSynchronizationStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_scimsynchronization_status(
        self,
        request: cloudsso_20210515_models.SetSCIMSynchronizationStatusRequest,
    ) -> cloudsso_20210515_models.SetSCIMSynchronizationStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_scimsynchronization_status_with_options(request, runtime)

    async def set_scimsynchronization_status_async(
        self,
        request: cloudsso_20210515_models.SetSCIMSynchronizationStatusRequest,
    ) -> cloudsso_20210515_models.SetSCIMSynchronizationStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_scimsynchronization_status_with_options_async(request, runtime)

    def update_access_configuration_with_options(
        self,
        request: cloudsso_20210515_models.UpdateAccessConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.UpdateAccessConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccessConfigurationId'] = request.access_configuration_id
        query['DirectoryId'] = request.directory_id
        query['NewDescription'] = request.new_description
        query['NewRelayState'] = request.new_relay_state
        query['NewSessionDuration'] = request.new_session_duration
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateAccessConfiguration',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.UpdateAccessConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_access_configuration_with_options_async(
        self,
        request: cloudsso_20210515_models.UpdateAccessConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.UpdateAccessConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccessConfigurationId'] = request.access_configuration_id
        query['DirectoryId'] = request.directory_id
        query['NewDescription'] = request.new_description
        query['NewRelayState'] = request.new_relay_state
        query['NewSessionDuration'] = request.new_session_duration
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateAccessConfiguration',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.UpdateAccessConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_access_configuration(
        self,
        request: cloudsso_20210515_models.UpdateAccessConfigurationRequest,
    ) -> cloudsso_20210515_models.UpdateAccessConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_access_configuration_with_options(request, runtime)

    async def update_access_configuration_async(
        self,
        request: cloudsso_20210515_models.UpdateAccessConfigurationRequest,
    ) -> cloudsso_20210515_models.UpdateAccessConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_access_configuration_with_options_async(request, runtime)

    def update_directory_with_options(
        self,
        request: cloudsso_20210515_models.UpdateDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.UpdateDirectoryResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        query['NewDirectoryName'] = request.new_directory_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateDirectory',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.UpdateDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_directory_with_options_async(
        self,
        request: cloudsso_20210515_models.UpdateDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.UpdateDirectoryResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        query['NewDirectoryName'] = request.new_directory_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateDirectory',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.UpdateDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_directory(
        self,
        request: cloudsso_20210515_models.UpdateDirectoryRequest,
    ) -> cloudsso_20210515_models.UpdateDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_directory_with_options(request, runtime)

    async def update_directory_async(
        self,
        request: cloudsso_20210515_models.UpdateDirectoryRequest,
    ) -> cloudsso_20210515_models.UpdateDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_directory_with_options_async(request, runtime)

    def update_group_with_options(
        self,
        request: cloudsso_20210515_models.UpdateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.UpdateGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        query['GroupId'] = request.group_id
        query['NewDescription'] = request.new_description
        query['NewGroupName'] = request.new_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateGroup',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.UpdateGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_group_with_options_async(
        self,
        request: cloudsso_20210515_models.UpdateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.UpdateGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        query['GroupId'] = request.group_id
        query['NewDescription'] = request.new_description
        query['NewGroupName'] = request.new_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateGroup',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.UpdateGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_group(
        self,
        request: cloudsso_20210515_models.UpdateGroupRequest,
    ) -> cloudsso_20210515_models.UpdateGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_group_with_options(request, runtime)

    async def update_group_async(
        self,
        request: cloudsso_20210515_models.UpdateGroupRequest,
    ) -> cloudsso_20210515_models.UpdateGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_group_with_options_async(request, runtime)

    def update_inline_policy_for_access_configuration_with_options(
        self,
        request: cloudsso_20210515_models.UpdateInlinePolicyForAccessConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.UpdateInlinePolicyForAccessConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccessConfigurationId'] = request.access_configuration_id
        query['DirectoryId'] = request.directory_id
        query['InlinePolicyName'] = request.inline_policy_name
        query['NewInlinePolicyDocument'] = request.new_inline_policy_document
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateInlinePolicyForAccessConfiguration',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.UpdateInlinePolicyForAccessConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_inline_policy_for_access_configuration_with_options_async(
        self,
        request: cloudsso_20210515_models.UpdateInlinePolicyForAccessConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.UpdateInlinePolicyForAccessConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccessConfigurationId'] = request.access_configuration_id
        query['DirectoryId'] = request.directory_id
        query['InlinePolicyName'] = request.inline_policy_name
        query['NewInlinePolicyDocument'] = request.new_inline_policy_document
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateInlinePolicyForAccessConfiguration',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.UpdateInlinePolicyForAccessConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_inline_policy_for_access_configuration(
        self,
        request: cloudsso_20210515_models.UpdateInlinePolicyForAccessConfigurationRequest,
    ) -> cloudsso_20210515_models.UpdateInlinePolicyForAccessConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_inline_policy_for_access_configuration_with_options(request, runtime)

    async def update_inline_policy_for_access_configuration_async(
        self,
        request: cloudsso_20210515_models.UpdateInlinePolicyForAccessConfigurationRequest,
    ) -> cloudsso_20210515_models.UpdateInlinePolicyForAccessConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_inline_policy_for_access_configuration_with_options_async(request, runtime)

    def update_scimserver_credential_status_with_options(
        self,
        request: cloudsso_20210515_models.UpdateSCIMServerCredentialStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.UpdateSCIMServerCredentialStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CredentialId'] = request.credential_id
        query['DirectoryId'] = request.directory_id
        query['NewStatus'] = request.new_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateSCIMServerCredentialStatus',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.UpdateSCIMServerCredentialStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_scimserver_credential_status_with_options_async(
        self,
        request: cloudsso_20210515_models.UpdateSCIMServerCredentialStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.UpdateSCIMServerCredentialStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CredentialId'] = request.credential_id
        query['DirectoryId'] = request.directory_id
        query['NewStatus'] = request.new_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateSCIMServerCredentialStatus',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.UpdateSCIMServerCredentialStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_scimserver_credential_status(
        self,
        request: cloudsso_20210515_models.UpdateSCIMServerCredentialStatusRequest,
    ) -> cloudsso_20210515_models.UpdateSCIMServerCredentialStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_scimserver_credential_status_with_options(request, runtime)

    async def update_scimserver_credential_status_async(
        self,
        request: cloudsso_20210515_models.UpdateSCIMServerCredentialStatusRequest,
    ) -> cloudsso_20210515_models.UpdateSCIMServerCredentialStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_scimserver_credential_status_with_options_async(request, runtime)

    def update_user_with_options(
        self,
        request: cloudsso_20210515_models.UpdateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.UpdateUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        query['NewDescription'] = request.new_description
        query['NewDisplayName'] = request.new_display_name
        query['NewEmail'] = request.new_email
        query['NewFirstName'] = request.new_first_name
        query['NewLastName'] = request.new_last_name
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateUser',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.UpdateUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_with_options_async(
        self,
        request: cloudsso_20210515_models.UpdateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.UpdateUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        query['NewDescription'] = request.new_description
        query['NewDisplayName'] = request.new_display_name
        query['NewEmail'] = request.new_email
        query['NewFirstName'] = request.new_first_name
        query['NewLastName'] = request.new_last_name
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateUser',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.UpdateUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user(
        self,
        request: cloudsso_20210515_models.UpdateUserRequest,
    ) -> cloudsso_20210515_models.UpdateUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_user_with_options(request, runtime)

    async def update_user_async(
        self,
        request: cloudsso_20210515_models.UpdateUserRequest,
    ) -> cloudsso_20210515_models.UpdateUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_user_with_options_async(request, runtime)

    def update_user_status_with_options(
        self,
        request: cloudsso_20210515_models.UpdateUserStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.UpdateUserStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        query['NewStatus'] = request.new_status
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateUserStatus',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.UpdateUserStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_status_with_options_async(
        self,
        request: cloudsso_20210515_models.UpdateUserStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.UpdateUserStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DirectoryId'] = request.directory_id
        query['NewStatus'] = request.new_status
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateUserStatus',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.UpdateUserStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user_status(
        self,
        request: cloudsso_20210515_models.UpdateUserStatusRequest,
    ) -> cloudsso_20210515_models.UpdateUserStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_user_status_with_options(request, runtime)

    async def update_user_status_async(
        self,
        request: cloudsso_20210515_models.UpdateUserStatusRequest,
    ) -> cloudsso_20210515_models.UpdateUserStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_user_status_with_options_async(request, runtime)
