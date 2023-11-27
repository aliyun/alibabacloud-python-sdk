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
        """
        You can add up to two SAML signing certificates.
        This topic provides an example on how to add a SAML signing certificate to the directory `d-00fc2p61****`.
        
        @param request: AddExternalSAMLIdPCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddExternalSAMLIdPCertificateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.x_509certificate):
            query['X509Certificate'] = request.x_509certificate
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddExternalSAMLIdPCertificate',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        You can add up to two SAML signing certificates.
        This topic provides an example on how to add a SAML signing certificate to the directory `d-00fc2p61****`.
        
        @param request: AddExternalSAMLIdPCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddExternalSAMLIdPCertificateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.x_509certificate):
            query['X509Certificate'] = request.x_509certificate
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddExternalSAMLIdPCertificate',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        You can add up to two SAML signing certificates.
        This topic provides an example on how to add a SAML signing certificate to the directory `d-00fc2p61****`.
        
        @param request: AddExternalSAMLIdPCertificateRequest
        @return: AddExternalSAMLIdPCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_external_samlid_pcertificate_with_options(request, runtime)

    async def add_external_samlid_pcertificate_async(
        self,
        request: cloudsso_20210515_models.AddExternalSAMLIdPCertificateRequest,
    ) -> cloudsso_20210515_models.AddExternalSAMLIdPCertificateResponse:
        """
        You can add up to two SAML signing certificates.
        This topic provides an example on how to add a SAML signing certificate to the directory `d-00fc2p61****`.
        
        @param request: AddExternalSAMLIdPCertificateRequest
        @return: AddExternalSAMLIdPCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_external_samlid_pcertificate_with_options_async(request, runtime)

    def add_permission_policy_to_access_configuration_with_options(
        self,
        request: cloudsso_20210515_models.AddPermissionPolicyToAccessConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.AddPermissionPolicyToAccessConfigurationResponse:
        """
        This topic provides an example on how to add the system policy `AliyunECSFullAccess` to the access configuration `ac-00jhtfl8thteu6uj***`.
        
        @param request: AddPermissionPolicyToAccessConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddPermissionPolicyToAccessConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.inline_policy_document):
            query['InlinePolicyDocument'] = request.inline_policy_document
        if not UtilClient.is_unset(request.permission_policy_name):
            query['PermissionPolicyName'] = request.permission_policy_name
        if not UtilClient.is_unset(request.permission_policy_type):
            query['PermissionPolicyType'] = request.permission_policy_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddPermissionPolicyToAccessConfiguration',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to add the system policy `AliyunECSFullAccess` to the access configuration `ac-00jhtfl8thteu6uj***`.
        
        @param request: AddPermissionPolicyToAccessConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddPermissionPolicyToAccessConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.inline_policy_document):
            query['InlinePolicyDocument'] = request.inline_policy_document
        if not UtilClient.is_unset(request.permission_policy_name):
            query['PermissionPolicyName'] = request.permission_policy_name
        if not UtilClient.is_unset(request.permission_policy_type):
            query['PermissionPolicyType'] = request.permission_policy_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddPermissionPolicyToAccessConfiguration',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to add the system policy `AliyunECSFullAccess` to the access configuration `ac-00jhtfl8thteu6uj***`.
        
        @param request: AddPermissionPolicyToAccessConfigurationRequest
        @return: AddPermissionPolicyToAccessConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_permission_policy_to_access_configuration_with_options(request, runtime)

    async def add_permission_policy_to_access_configuration_async(
        self,
        request: cloudsso_20210515_models.AddPermissionPolicyToAccessConfigurationRequest,
    ) -> cloudsso_20210515_models.AddPermissionPolicyToAccessConfigurationResponse:
        """
        This topic provides an example on how to add the system policy `AliyunECSFullAccess` to the access configuration `ac-00jhtfl8thteu6uj***`.
        
        @param request: AddPermissionPolicyToAccessConfigurationRequest
        @return: AddPermissionPolicyToAccessConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_permission_policy_to_access_configuration_with_options_async(request, runtime)

    def add_user_to_group_with_options(
        self,
        request: cloudsso_20210515_models.AddUserToGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.AddUserToGroupResponse:
        """
        If System for Cross-domain Identity Management (SCIM) synchronization is enabled, you cannot add a user to a group that is synchronized by using SCIM.
        This topic provides an example of how to add the user `u-00q8wbq42wiltcrk****` to the group `g-00jqzghi2n3o5hkh****`.
        
        @param request: AddUserToGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddUserToGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddUserToGroup',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        If System for Cross-domain Identity Management (SCIM) synchronization is enabled, you cannot add a user to a group that is synchronized by using SCIM.
        This topic provides an example of how to add the user `u-00q8wbq42wiltcrk****` to the group `g-00jqzghi2n3o5hkh****`.
        
        @param request: AddUserToGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddUserToGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddUserToGroup',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        If System for Cross-domain Identity Management (SCIM) synchronization is enabled, you cannot add a user to a group that is synchronized by using SCIM.
        This topic provides an example of how to add the user `u-00q8wbq42wiltcrk****` to the group `g-00jqzghi2n3o5hkh****`.
        
        @param request: AddUserToGroupRequest
        @return: AddUserToGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_user_to_group_with_options(request, runtime)

    async def add_user_to_group_async(
        self,
        request: cloudsso_20210515_models.AddUserToGroupRequest,
    ) -> cloudsso_20210515_models.AddUserToGroupResponse:
        """
        If System for Cross-domain Identity Management (SCIM) synchronization is enabled, you cannot add a user to a group that is synchronized by using SCIM.
        This topic provides an example of how to add the user `u-00q8wbq42wiltcrk****` to the group `g-00jqzghi2n3o5hkh****`.
        
        @param request: AddUserToGroupRequest
        @return: AddUserToGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_user_to_group_with_options_async(request, runtime)

    def clear_external_samlidentity_provider_with_options(
        self,
        request: cloudsso_20210515_models.ClearExternalSAMLIdentityProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.ClearExternalSAMLIdentityProviderResponse:
        """
        If single sign-on (SSO) logon is disabled, you can clear the configurations of a SAML IdP. If SSO logon is enabled, you cannot clear the configurations.
        This topic provides an example on how to clear the configurations of the SAML IdP within the directory `d-00fc2p61****`.
        
        @param request: ClearExternalSAMLIdentityProviderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ClearExternalSAMLIdentityProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ClearExternalSAMLIdentityProvider',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        If single sign-on (SSO) logon is disabled, you can clear the configurations of a SAML IdP. If SSO logon is enabled, you cannot clear the configurations.
        This topic provides an example on how to clear the configurations of the SAML IdP within the directory `d-00fc2p61****`.
        
        @param request: ClearExternalSAMLIdentityProviderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ClearExternalSAMLIdentityProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ClearExternalSAMLIdentityProvider',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        If single sign-on (SSO) logon is disabled, you can clear the configurations of a SAML IdP. If SSO logon is enabled, you cannot clear the configurations.
        This topic provides an example on how to clear the configurations of the SAML IdP within the directory `d-00fc2p61****`.
        
        @param request: ClearExternalSAMLIdentityProviderRequest
        @return: ClearExternalSAMLIdentityProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.clear_external_samlidentity_provider_with_options(request, runtime)

    async def clear_external_samlidentity_provider_async(
        self,
        request: cloudsso_20210515_models.ClearExternalSAMLIdentityProviderRequest,
    ) -> cloudsso_20210515_models.ClearExternalSAMLIdentityProviderResponse:
        """
        If single sign-on (SSO) logon is disabled, you can clear the configurations of a SAML IdP. If SSO logon is enabled, you cannot clear the configurations.
        This topic provides an example on how to clear the configurations of the SAML IdP within the directory `d-00fc2p61****`.
        
        @param request: ClearExternalSAMLIdentityProviderRequest
        @return: ClearExternalSAMLIdentityProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.clear_external_samlidentity_provider_with_options_async(request, runtime)

    def create_access_assignment_with_options(
        self,
        request: cloudsso_20210515_models.CreateAccessAssignmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.CreateAccessAssignmentResponse:
        """
        When you call this operation, an asynchronous task is created. You can call the [GetTask](~~340670~~) operation to query the progress of task execution by using the value of the `TaskId` response parameter.
        For more information about how to assign permissions on an account in your resource directory, see [Overview of multi-account authorization](~~266726~~).
        This topic provides an example on how to assign access permissions on the account `114240524784****` in your resource directory to the CloudSSO user `u-00q8wbq42wiltcrk****` by using the access configuration `ac-00jhtfl8thteu6uj****`. After the call is successful, the CloudSSO user can access resources within the account in the resource directory.
        
        @param request: CreateAccessAssignmentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAccessAssignmentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.principal_id):
            query['PrincipalId'] = request.principal_id
        if not UtilClient.is_unset(request.principal_type):
            query['PrincipalType'] = request.principal_type
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccessAssignment',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        When you call this operation, an asynchronous task is created. You can call the [GetTask](~~340670~~) operation to query the progress of task execution by using the value of the `TaskId` response parameter.
        For more information about how to assign permissions on an account in your resource directory, see [Overview of multi-account authorization](~~266726~~).
        This topic provides an example on how to assign access permissions on the account `114240524784****` in your resource directory to the CloudSSO user `u-00q8wbq42wiltcrk****` by using the access configuration `ac-00jhtfl8thteu6uj****`. After the call is successful, the CloudSSO user can access resources within the account in the resource directory.
        
        @param request: CreateAccessAssignmentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAccessAssignmentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.principal_id):
            query['PrincipalId'] = request.principal_id
        if not UtilClient.is_unset(request.principal_type):
            query['PrincipalType'] = request.principal_type
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccessAssignment',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        When you call this operation, an asynchronous task is created. You can call the [GetTask](~~340670~~) operation to query the progress of task execution by using the value of the `TaskId` response parameter.
        For more information about how to assign permissions on an account in your resource directory, see [Overview of multi-account authorization](~~266726~~).
        This topic provides an example on how to assign access permissions on the account `114240524784****` in your resource directory to the CloudSSO user `u-00q8wbq42wiltcrk****` by using the access configuration `ac-00jhtfl8thteu6uj****`. After the call is successful, the CloudSSO user can access resources within the account in the resource directory.
        
        @param request: CreateAccessAssignmentRequest
        @return: CreateAccessAssignmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_access_assignment_with_options(request, runtime)

    async def create_access_assignment_async(
        self,
        request: cloudsso_20210515_models.CreateAccessAssignmentRequest,
    ) -> cloudsso_20210515_models.CreateAccessAssignmentResponse:
        """
        When you call this operation, an asynchronous task is created. You can call the [GetTask](~~340670~~) operation to query the progress of task execution by using the value of the `TaskId` response parameter.
        For more information about how to assign permissions on an account in your resource directory, see [Overview of multi-account authorization](~~266726~~).
        This topic provides an example on how to assign access permissions on the account `114240524784****` in your resource directory to the CloudSSO user `u-00q8wbq42wiltcrk****` by using the access configuration `ac-00jhtfl8thteu6uj****`. After the call is successful, the CloudSSO user can access resources within the account in the resource directory.
        
        @param request: CreateAccessAssignmentRequest
        @return: CreateAccessAssignmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_access_assignment_with_options_async(request, runtime)

    def create_access_configuration_with_options(
        self,
        request: cloudsso_20210515_models.CreateAccessConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.CreateAccessConfigurationResponse:
        """
        For more information about access configurations, see [Overview of access configurations](~~266737~~).
        This topic provides an example on how to create an access configuration named `ECS-Admin`.
        
        @param request: CreateAccessConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAccessConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_configuration_name):
            query['AccessConfigurationName'] = request.access_configuration_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.relay_state):
            query['RelayState'] = request.relay_state
        if not UtilClient.is_unset(request.session_duration):
            query['SessionDuration'] = request.session_duration
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccessConfiguration',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        For more information about access configurations, see [Overview of access configurations](~~266737~~).
        This topic provides an example on how to create an access configuration named `ECS-Admin`.
        
        @param request: CreateAccessConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAccessConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_configuration_name):
            query['AccessConfigurationName'] = request.access_configuration_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.relay_state):
            query['RelayState'] = request.relay_state
        if not UtilClient.is_unset(request.session_duration):
            query['SessionDuration'] = request.session_duration
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccessConfiguration',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        For more information about access configurations, see [Overview of access configurations](~~266737~~).
        This topic provides an example on how to create an access configuration named `ECS-Admin`.
        
        @param request: CreateAccessConfigurationRequest
        @return: CreateAccessConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_access_configuration_with_options(request, runtime)

    async def create_access_configuration_async(
        self,
        request: cloudsso_20210515_models.CreateAccessConfigurationRequest,
    ) -> cloudsso_20210515_models.CreateAccessConfigurationResponse:
        """
        For more information about access configurations, see [Overview of access configurations](~~266737~~).
        This topic provides an example on how to create an access configuration named `ECS-Admin`.
        
        @param request: CreateAccessConfigurationRequest
        @return: CreateAccessConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_access_configuration_with_options_async(request, runtime)

    def create_directory_with_options(
        self,
        request: cloudsso_20210515_models.CreateDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.CreateDirectoryResponse:
        """
        A directory is a CloudSSO instance. Before you can use CloudSSO, you must create a directory. The directory is used to manage all CloudSSO resources.
        To create a directory, you must select a region. Alibaba Cloud stores data in the directory only in the region that you select. However, you can deploy Alibaba Cloud resources including Elastic Compute Service (ECS) instances and ApsaraDB RDS instances in other regions. You can also use your cloud account for logons and access the Alibaba Cloud resources in other regions. You can select a region to create a directory based on your security compliance requirements and the geographic location of specific users. If you do not have strict security compliance requirements, we recommend that you select a region that is the closest to the geographical location of the specific users. This way, access to cloud resources is accelerated. You can create the CloudSSO directory in the China (Shanghai), China (Hong Kong), US (Silicon Valley), or Germany (Frankfurt) region.
        This topic provides an example on how to create a directory named `example` in the China (Shanghai) region.
        ## Limits
        - You can create only one directory for a management account.
        - If you want to change the region of a directory, you must delete the directory and then create a directory in a different region.
        
        @param request: CreateDirectoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDirectoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_name):
            query['DirectoryName'] = request.directory_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDirectory',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        A directory is a CloudSSO instance. Before you can use CloudSSO, you must create a directory. The directory is used to manage all CloudSSO resources.
        To create a directory, you must select a region. Alibaba Cloud stores data in the directory only in the region that you select. However, you can deploy Alibaba Cloud resources including Elastic Compute Service (ECS) instances and ApsaraDB RDS instances in other regions. You can also use your cloud account for logons and access the Alibaba Cloud resources in other regions. You can select a region to create a directory based on your security compliance requirements and the geographic location of specific users. If you do not have strict security compliance requirements, we recommend that you select a region that is the closest to the geographical location of the specific users. This way, access to cloud resources is accelerated. You can create the CloudSSO directory in the China (Shanghai), China (Hong Kong), US (Silicon Valley), or Germany (Frankfurt) region.
        This topic provides an example on how to create a directory named `example` in the China (Shanghai) region.
        ## Limits
        - You can create only one directory for a management account.
        - If you want to change the region of a directory, you must delete the directory and then create a directory in a different region.
        
        @param request: CreateDirectoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDirectoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_name):
            query['DirectoryName'] = request.directory_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDirectory',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        A directory is a CloudSSO instance. Before you can use CloudSSO, you must create a directory. The directory is used to manage all CloudSSO resources.
        To create a directory, you must select a region. Alibaba Cloud stores data in the directory only in the region that you select. However, you can deploy Alibaba Cloud resources including Elastic Compute Service (ECS) instances and ApsaraDB RDS instances in other regions. You can also use your cloud account for logons and access the Alibaba Cloud resources in other regions. You can select a region to create a directory based on your security compliance requirements and the geographic location of specific users. If you do not have strict security compliance requirements, we recommend that you select a region that is the closest to the geographical location of the specific users. This way, access to cloud resources is accelerated. You can create the CloudSSO directory in the China (Shanghai), China (Hong Kong), US (Silicon Valley), or Germany (Frankfurt) region.
        This topic provides an example on how to create a directory named `example` in the China (Shanghai) region.
        ## Limits
        - You can create only one directory for a management account.
        - If you want to change the region of a directory, you must delete the directory and then create a directory in a different region.
        
        @param request: CreateDirectoryRequest
        @return: CreateDirectoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_directory_with_options(request, runtime)

    async def create_directory_async(
        self,
        request: cloudsso_20210515_models.CreateDirectoryRequest,
    ) -> cloudsso_20210515_models.CreateDirectoryResponse:
        """
        A directory is a CloudSSO instance. Before you can use CloudSSO, you must create a directory. The directory is used to manage all CloudSSO resources.
        To create a directory, you must select a region. Alibaba Cloud stores data in the directory only in the region that you select. However, you can deploy Alibaba Cloud resources including Elastic Compute Service (ECS) instances and ApsaraDB RDS instances in other regions. You can also use your cloud account for logons and access the Alibaba Cloud resources in other regions. You can select a region to create a directory based on your security compliance requirements and the geographic location of specific users. If you do not have strict security compliance requirements, we recommend that you select a region that is the closest to the geographical location of the specific users. This way, access to cloud resources is accelerated. You can create the CloudSSO directory in the China (Shanghai), China (Hong Kong), US (Silicon Valley), or Germany (Frankfurt) region.
        This topic provides an example on how to create a directory named `example` in the China (Shanghai) region.
        ## Limits
        - You can create only one directory for a management account.
        - If you want to change the region of a directory, you must delete the directory and then create a directory in a different region.
        
        @param request: CreateDirectoryRequest
        @return: CreateDirectoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_directory_with_options_async(request, runtime)

    def create_group_with_options(
        self,
        request: cloudsso_20210515_models.CreateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.CreateGroupResponse:
        """
        This topic provides an example on how to create a group named `TestGroup`.
        
        @param request: CreateGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGroup',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to create a group named `TestGroup`.
        
        @param request: CreateGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGroup',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to create a group named `TestGroup`.
        
        @param request: CreateGroupRequest
        @return: CreateGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_group_with_options(request, runtime)

    async def create_group_async(
        self,
        request: cloudsso_20210515_models.CreateGroupRequest,
    ) -> cloudsso_20210515_models.CreateGroupResponse:
        """
        This topic provides an example on how to create a group named `TestGroup`.
        
        @param request: CreateGroupRequest
        @return: CreateGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_group_with_options_async(request, runtime)

    def create_scimserver_credential_with_options(
        self,
        request: cloudsso_20210515_models.CreateSCIMServerCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.CreateSCIMServerCredentialResponse:
        """
        SCIM credentials are required for SCIM synchronization. You can create up to two SCIM credentials.
        This topic provides an example on how to create a SCIM credential within the directory `d-00fc2p61****`.
        
        @param request: CreateSCIMServerCredentialRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSCIMServerCredentialResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSCIMServerCredential',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        SCIM credentials are required for SCIM synchronization. You can create up to two SCIM credentials.
        This topic provides an example on how to create a SCIM credential within the directory `d-00fc2p61****`.
        
        @param request: CreateSCIMServerCredentialRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSCIMServerCredentialResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSCIMServerCredential',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        SCIM credentials are required for SCIM synchronization. You can create up to two SCIM credentials.
        This topic provides an example on how to create a SCIM credential within the directory `d-00fc2p61****`.
        
        @param request: CreateSCIMServerCredentialRequest
        @return: CreateSCIMServerCredentialResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_scimserver_credential_with_options(request, runtime)

    async def create_scimserver_credential_async(
        self,
        request: cloudsso_20210515_models.CreateSCIMServerCredentialRequest,
    ) -> cloudsso_20210515_models.CreateSCIMServerCredentialResponse:
        """
        SCIM credentials are required for SCIM synchronization. You can create up to two SCIM credentials.
        This topic provides an example on how to create a SCIM credential within the directory `d-00fc2p61****`.
        
        @param request: CreateSCIMServerCredentialRequest
        @return: CreateSCIMServerCredentialResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_scimserver_credential_with_options_async(request, runtime)

    def create_user_with_options(
        self,
        request: cloudsso_20210515_models.CreateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.CreateUserResponse:
        """
        This topic provides an example on how to create a user named `Alice`.
        
        @param request: CreateUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.first_name):
            query['FirstName'] = request.first_name
        if not UtilClient.is_unset(request.last_name):
            query['LastName'] = request.last_name
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUser',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to create a user named `Alice`.
        
        @param request: CreateUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.first_name):
            query['FirstName'] = request.first_name
        if not UtilClient.is_unset(request.last_name):
            query['LastName'] = request.last_name
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUser',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to create a user named `Alice`.
        
        @param request: CreateUserRequest
        @return: CreateUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_user_with_options(request, runtime)

    async def create_user_async(
        self,
        request: cloudsso_20210515_models.CreateUserRequest,
    ) -> cloudsso_20210515_models.CreateUserResponse:
        """
        This topic provides an example on how to create a user named `Alice`.
        
        @param request: CreateUserRequest
        @return: CreateUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_user_with_options_async(request, runtime)

    def create_user_provisioning_with_options(
        self,
        request: cloudsso_20210515_models.CreateUserProvisioningRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.CreateUserProvisioningResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deletion_strategy):
            query['DeletionStrategy'] = request.deletion_strategy
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.duplication_strategy):
            query['DuplicationStrategy'] = request.duplication_strategy
        if not UtilClient.is_unset(request.principal_id):
            query['PrincipalId'] = request.principal_id
        if not UtilClient.is_unset(request.principal_type):
            query['PrincipalType'] = request.principal_type
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUserProvisioning',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.CreateUserProvisioningResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_user_provisioning_with_options_async(
        self,
        request: cloudsso_20210515_models.CreateUserProvisioningRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.CreateUserProvisioningResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deletion_strategy):
            query['DeletionStrategy'] = request.deletion_strategy
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.duplication_strategy):
            query['DuplicationStrategy'] = request.duplication_strategy
        if not UtilClient.is_unset(request.principal_id):
            query['PrincipalId'] = request.principal_id
        if not UtilClient.is_unset(request.principal_type):
            query['PrincipalType'] = request.principal_type
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUserProvisioning',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.CreateUserProvisioningResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_user_provisioning(
        self,
        request: cloudsso_20210515_models.CreateUserProvisioningRequest,
    ) -> cloudsso_20210515_models.CreateUserProvisioningResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_user_provisioning_with_options(request, runtime)

    async def create_user_provisioning_async(
        self,
        request: cloudsso_20210515_models.CreateUserProvisioningRequest,
    ) -> cloudsso_20210515_models.CreateUserProvisioningResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_user_provisioning_with_options_async(request, runtime)

    def delete_access_assignment_with_options(
        self,
        request: cloudsso_20210515_models.DeleteAccessAssignmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.DeleteAccessAssignmentResponse:
        """
        When you call this operation, an asynchronous task is created. You can call the [GetTask](~~340670~~) operation to query the progress of the task based on the value of the `TaskId` response parameter.
        This topic provides an example on how to remove the access permissions on the account `114240524784****` in the resource directory from the CloudSSO user `u-00q8wbq42wiltcrk****`. The access permissions are assigned by using the access configuration `ac-00jhtfl8thteu6uj****`.
        
        @param request: DeleteAccessAssignmentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAccessAssignmentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not UtilClient.is_unset(request.deprovision_strategy):
            query['DeprovisionStrategy'] = request.deprovision_strategy
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.principal_id):
            query['PrincipalId'] = request.principal_id
        if not UtilClient.is_unset(request.principal_type):
            query['PrincipalType'] = request.principal_type
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccessAssignment',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        When you call this operation, an asynchronous task is created. You can call the [GetTask](~~340670~~) operation to query the progress of the task based on the value of the `TaskId` response parameter.
        This topic provides an example on how to remove the access permissions on the account `114240524784****` in the resource directory from the CloudSSO user `u-00q8wbq42wiltcrk****`. The access permissions are assigned by using the access configuration `ac-00jhtfl8thteu6uj****`.
        
        @param request: DeleteAccessAssignmentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAccessAssignmentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not UtilClient.is_unset(request.deprovision_strategy):
            query['DeprovisionStrategy'] = request.deprovision_strategy
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.principal_id):
            query['PrincipalId'] = request.principal_id
        if not UtilClient.is_unset(request.principal_type):
            query['PrincipalType'] = request.principal_type
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccessAssignment',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        When you call this operation, an asynchronous task is created. You can call the [GetTask](~~340670~~) operation to query the progress of the task based on the value of the `TaskId` response parameter.
        This topic provides an example on how to remove the access permissions on the account `114240524784****` in the resource directory from the CloudSSO user `u-00q8wbq42wiltcrk****`. The access permissions are assigned by using the access configuration `ac-00jhtfl8thteu6uj****`.
        
        @param request: DeleteAccessAssignmentRequest
        @return: DeleteAccessAssignmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_access_assignment_with_options(request, runtime)

    async def delete_access_assignment_async(
        self,
        request: cloudsso_20210515_models.DeleteAccessAssignmentRequest,
    ) -> cloudsso_20210515_models.DeleteAccessAssignmentResponse:
        """
        When you call this operation, an asynchronous task is created. You can call the [GetTask](~~340670~~) operation to query the progress of the task based on the value of the `TaskId` response parameter.
        This topic provides an example on how to remove the access permissions on the account `114240524784****` in the resource directory from the CloudSSO user `u-00q8wbq42wiltcrk****`. The access permissions are assigned by using the access configuration `ac-00jhtfl8thteu6uj****`.
        
        @param request: DeleteAccessAssignmentRequest
        @return: DeleteAccessAssignmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_access_assignment_with_options_async(request, runtime)

    def delete_access_configuration_with_options(
        self,
        request: cloudsso_20210515_models.DeleteAccessConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.DeleteAccessConfigurationResponse:
        """
        This topic provides an example on how to delete the access configuration whose ID is `ac-001j9mcm3k7335bc***`.
        ## Prerequisites
        The access configuration that you want to delete is de-provisioned from the accounts in your resource directory. For more information, see [DeprovisionAccessConfiguration](~~338352~~).
        
        @param request: DeleteAccessConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAccessConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.force_remove_permission_policies):
            query['ForceRemovePermissionPolicies'] = request.force_remove_permission_policies
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccessConfiguration',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to delete the access configuration whose ID is `ac-001j9mcm3k7335bc***`.
        ## Prerequisites
        The access configuration that you want to delete is de-provisioned from the accounts in your resource directory. For more information, see [DeprovisionAccessConfiguration](~~338352~~).
        
        @param request: DeleteAccessConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAccessConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.force_remove_permission_policies):
            query['ForceRemovePermissionPolicies'] = request.force_remove_permission_policies
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccessConfiguration',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to delete the access configuration whose ID is `ac-001j9mcm3k7335bc***`.
        ## Prerequisites
        The access configuration that you want to delete is de-provisioned from the accounts in your resource directory. For more information, see [DeprovisionAccessConfiguration](~~338352~~).
        
        @param request: DeleteAccessConfigurationRequest
        @return: DeleteAccessConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_access_configuration_with_options(request, runtime)

    async def delete_access_configuration_async(
        self,
        request: cloudsso_20210515_models.DeleteAccessConfigurationRequest,
    ) -> cloudsso_20210515_models.DeleteAccessConfigurationResponse:
        """
        This topic provides an example on how to delete the access configuration whose ID is `ac-001j9mcm3k7335bc***`.
        ## Prerequisites
        The access configuration that you want to delete is de-provisioned from the accounts in your resource directory. For more information, see [DeprovisionAccessConfiguration](~~338352~~).
        
        @param request: DeleteAccessConfigurationRequest
        @return: DeleteAccessConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_access_configuration_with_options_async(request, runtime)

    def delete_directory_with_options(
        self,
        request: cloudsso_20210515_models.DeleteDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.DeleteDirectoryResponse:
        """
        This topic provides an example on how to delete a directory whose ID is `d-00fc2p61***`.
        ## Prerequisites
        No resources are contained in the directory that you want to delete.
        *   Access permissions on the accounts in your resource directory are removed from all users and groups. For more information, see [DeleteAccessAssignment](~~338350~~).
        *   Users are deleted. For more information, see [DeleteUser](~~341671~~).
        *   Groups are deleted. For more information, see [DeleteGroup](~~341821~~).
        *   Access configurations are deleted. For more information, see [DeleteAccessConfiguration](~~336907~~).
        *   System for Cross-domain Identity Management (SCIM) credentials are deleted. For more information, see [DeleteSCIMServerCredential](~~341842~~).
        *   SSO logon configurations are deleted. For more information, see [ClearExternalSAMLIdentityProvider](~~341573~~).
        
        @param request: DeleteDirectoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDirectoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDirectory',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to delete a directory whose ID is `d-00fc2p61***`.
        ## Prerequisites
        No resources are contained in the directory that you want to delete.
        *   Access permissions on the accounts in your resource directory are removed from all users and groups. For more information, see [DeleteAccessAssignment](~~338350~~).
        *   Users are deleted. For more information, see [DeleteUser](~~341671~~).
        *   Groups are deleted. For more information, see [DeleteGroup](~~341821~~).
        *   Access configurations are deleted. For more information, see [DeleteAccessConfiguration](~~336907~~).
        *   System for Cross-domain Identity Management (SCIM) credentials are deleted. For more information, see [DeleteSCIMServerCredential](~~341842~~).
        *   SSO logon configurations are deleted. For more information, see [ClearExternalSAMLIdentityProvider](~~341573~~).
        
        @param request: DeleteDirectoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDirectoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDirectory',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to delete a directory whose ID is `d-00fc2p61***`.
        ## Prerequisites
        No resources are contained in the directory that you want to delete.
        *   Access permissions on the accounts in your resource directory are removed from all users and groups. For more information, see [DeleteAccessAssignment](~~338350~~).
        *   Users are deleted. For more information, see [DeleteUser](~~341671~~).
        *   Groups are deleted. For more information, see [DeleteGroup](~~341821~~).
        *   Access configurations are deleted. For more information, see [DeleteAccessConfiguration](~~336907~~).
        *   System for Cross-domain Identity Management (SCIM) credentials are deleted. For more information, see [DeleteSCIMServerCredential](~~341842~~).
        *   SSO logon configurations are deleted. For more information, see [ClearExternalSAMLIdentityProvider](~~341573~~).
        
        @param request: DeleteDirectoryRequest
        @return: DeleteDirectoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_directory_with_options(request, runtime)

    async def delete_directory_async(
        self,
        request: cloudsso_20210515_models.DeleteDirectoryRequest,
    ) -> cloudsso_20210515_models.DeleteDirectoryResponse:
        """
        This topic provides an example on how to delete a directory whose ID is `d-00fc2p61***`.
        ## Prerequisites
        No resources are contained in the directory that you want to delete.
        *   Access permissions on the accounts in your resource directory are removed from all users and groups. For more information, see [DeleteAccessAssignment](~~338350~~).
        *   Users are deleted. For more information, see [DeleteUser](~~341671~~).
        *   Groups are deleted. For more information, see [DeleteGroup](~~341821~~).
        *   Access configurations are deleted. For more information, see [DeleteAccessConfiguration](~~336907~~).
        *   System for Cross-domain Identity Management (SCIM) credentials are deleted. For more information, see [DeleteSCIMServerCredential](~~341842~~).
        *   SSO logon configurations are deleted. For more information, see [ClearExternalSAMLIdentityProvider](~~341573~~).
        
        @param request: DeleteDirectoryRequest
        @return: DeleteDirectoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_directory_with_options_async(request, runtime)

    def delete_group_with_options(
        self,
        request: cloudsso_20210515_models.DeleteGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.DeleteGroupResponse:
        """
        If System for Cross-domain Identity Management (SCIM) synchronization is enabled, you cannot delete a group that is synchronized by using SCIM.
        ## Prerequisites
        The group that you want to delete is not associated with the following resources. If the group is associated with the resources, the deletion fails.
        *   Users: You must remove users from the group. For more information, see [RemoveUserFromGroup](~~335116~~).
        *   Access permissions: You must remove the access permissions on the accounts in your resource directory from the group. For more information, see [DeleteAccessAssignment](~~338350~~).
        
        @param request: DeleteGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGroup',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        If System for Cross-domain Identity Management (SCIM) synchronization is enabled, you cannot delete a group that is synchronized by using SCIM.
        ## Prerequisites
        The group that you want to delete is not associated with the following resources. If the group is associated with the resources, the deletion fails.
        *   Users: You must remove users from the group. For more information, see [RemoveUserFromGroup](~~335116~~).
        *   Access permissions: You must remove the access permissions on the accounts in your resource directory from the group. For more information, see [DeleteAccessAssignment](~~338350~~).
        
        @param request: DeleteGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGroup',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        If System for Cross-domain Identity Management (SCIM) synchronization is enabled, you cannot delete a group that is synchronized by using SCIM.
        ## Prerequisites
        The group that you want to delete is not associated with the following resources. If the group is associated with the resources, the deletion fails.
        *   Users: You must remove users from the group. For more information, see [RemoveUserFromGroup](~~335116~~).
        *   Access permissions: You must remove the access permissions on the accounts in your resource directory from the group. For more information, see [DeleteAccessAssignment](~~338350~~).
        
        @param request: DeleteGroupRequest
        @return: DeleteGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_group_with_options(request, runtime)

    async def delete_group_async(
        self,
        request: cloudsso_20210515_models.DeleteGroupRequest,
    ) -> cloudsso_20210515_models.DeleteGroupResponse:
        """
        If System for Cross-domain Identity Management (SCIM) synchronization is enabled, you cannot delete a group that is synchronized by using SCIM.
        ## Prerequisites
        The group that you want to delete is not associated with the following resources. If the group is associated with the resources, the deletion fails.
        *   Users: You must remove users from the group. For more information, see [RemoveUserFromGroup](~~335116~~).
        *   Access permissions: You must remove the access permissions on the accounts in your resource directory from the group. For more information, see [DeleteAccessAssignment](~~338350~~).
        
        @param request: DeleteGroupRequest
        @return: DeleteGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_group_with_options_async(request, runtime)

    def delete_mfadevice_for_user_with_options(
        self,
        request: cloudsso_20210515_models.DeleteMFADeviceForUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.DeleteMFADeviceForUserResponse:
        """
        This topic provides an example on how to unbind the MFA device `mfa-00ujhet8pycljj7j***` from the user `u-00q8wbq42wiltcrk****`.
        
        @param request: DeleteMFADeviceForUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMFADeviceForUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.mfadevice_id):
            query['MFADeviceId'] = request.mfadevice_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMFADeviceForUser',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to unbind the MFA device `mfa-00ujhet8pycljj7j***` from the user `u-00q8wbq42wiltcrk****`.
        
        @param request: DeleteMFADeviceForUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMFADeviceForUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.mfadevice_id):
            query['MFADeviceId'] = request.mfadevice_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMFADeviceForUser',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to unbind the MFA device `mfa-00ujhet8pycljj7j***` from the user `u-00q8wbq42wiltcrk****`.
        
        @param request: DeleteMFADeviceForUserRequest
        @return: DeleteMFADeviceForUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_mfadevice_for_user_with_options(request, runtime)

    async def delete_mfadevice_for_user_async(
        self,
        request: cloudsso_20210515_models.DeleteMFADeviceForUserRequest,
    ) -> cloudsso_20210515_models.DeleteMFADeviceForUserResponse:
        """
        This topic provides an example on how to unbind the MFA device `mfa-00ujhet8pycljj7j***` from the user `u-00q8wbq42wiltcrk****`.
        
        @param request: DeleteMFADeviceForUserRequest
        @return: DeleteMFADeviceForUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_mfadevice_for_user_with_options_async(request, runtime)

    def delete_scimserver_credential_with_options(
        self,
        request: cloudsso_20210515_models.DeleteSCIMServerCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.DeleteSCIMServerCredentialResponse:
        """
        After a SCIM credential is deleted, the synchronization task that uses the SCIM credential fails.
        This topic provides an example on how to delete the SCIM credential whose ID is `scimcred-004whl0kvfwcypbi****`.
        
        @param request: DeleteSCIMServerCredentialRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSCIMServerCredentialResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.credential_id):
            query['CredentialId'] = request.credential_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSCIMServerCredential',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        After a SCIM credential is deleted, the synchronization task that uses the SCIM credential fails.
        This topic provides an example on how to delete the SCIM credential whose ID is `scimcred-004whl0kvfwcypbi****`.
        
        @param request: DeleteSCIMServerCredentialRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSCIMServerCredentialResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.credential_id):
            query['CredentialId'] = request.credential_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSCIMServerCredential',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        After a SCIM credential is deleted, the synchronization task that uses the SCIM credential fails.
        This topic provides an example on how to delete the SCIM credential whose ID is `scimcred-004whl0kvfwcypbi****`.
        
        @param request: DeleteSCIMServerCredentialRequest
        @return: DeleteSCIMServerCredentialResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_scimserver_credential_with_options(request, runtime)

    async def delete_scimserver_credential_async(
        self,
        request: cloudsso_20210515_models.DeleteSCIMServerCredentialRequest,
    ) -> cloudsso_20210515_models.DeleteSCIMServerCredentialResponse:
        """
        After a SCIM credential is deleted, the synchronization task that uses the SCIM credential fails.
        This topic provides an example on how to delete the SCIM credential whose ID is `scimcred-004whl0kvfwcypbi****`.
        
        @param request: DeleteSCIMServerCredentialRequest
        @return: DeleteSCIMServerCredentialResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_scimserver_credential_with_options_async(request, runtime)

    def delete_user_with_options(
        self,
        request: cloudsso_20210515_models.DeleteUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.DeleteUserResponse:
        """
        If System for Cross-domain Identity Management (SCIM) synchronization is enabled, you cannot delete a user that is synchronized by using SCIM.
        ## Prerequisites
        The user that you want to delete is not associated with the following resources. If the user is associated with the resources, the deletion fails.
        *   Multi-factor authentication (MFA) devices: You must unbind the MFA devices from the user. For more information, see [DeleteMFADeviceForUser](~~341675~~).
        *   Access permissions: You must remove the access permissions on the accounts in your resource directory from the user. For more information, see [DeleteAccessAssignment](~~338350~~).
        *   Groups: You must remove the user from groups. For more information, see [RemoveUserFromGroup](~~335116~~).
        
        @param request: DeleteUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUser',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        If System for Cross-domain Identity Management (SCIM) synchronization is enabled, you cannot delete a user that is synchronized by using SCIM.
        ## Prerequisites
        The user that you want to delete is not associated with the following resources. If the user is associated with the resources, the deletion fails.
        *   Multi-factor authentication (MFA) devices: You must unbind the MFA devices from the user. For more information, see [DeleteMFADeviceForUser](~~341675~~).
        *   Access permissions: You must remove the access permissions on the accounts in your resource directory from the user. For more information, see [DeleteAccessAssignment](~~338350~~).
        *   Groups: You must remove the user from groups. For more information, see [RemoveUserFromGroup](~~335116~~).
        
        @param request: DeleteUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUser',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        If System for Cross-domain Identity Management (SCIM) synchronization is enabled, you cannot delete a user that is synchronized by using SCIM.
        ## Prerequisites
        The user that you want to delete is not associated with the following resources. If the user is associated with the resources, the deletion fails.
        *   Multi-factor authentication (MFA) devices: You must unbind the MFA devices from the user. For more information, see [DeleteMFADeviceForUser](~~341675~~).
        *   Access permissions: You must remove the access permissions on the accounts in your resource directory from the user. For more information, see [DeleteAccessAssignment](~~338350~~).
        *   Groups: You must remove the user from groups. For more information, see [RemoveUserFromGroup](~~335116~~).
        
        @param request: DeleteUserRequest
        @return: DeleteUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_user_with_options(request, runtime)

    async def delete_user_async(
        self,
        request: cloudsso_20210515_models.DeleteUserRequest,
    ) -> cloudsso_20210515_models.DeleteUserResponse:
        """
        If System for Cross-domain Identity Management (SCIM) synchronization is enabled, you cannot delete a user that is synchronized by using SCIM.
        ## Prerequisites
        The user that you want to delete is not associated with the following resources. If the user is associated with the resources, the deletion fails.
        *   Multi-factor authentication (MFA) devices: You must unbind the MFA devices from the user. For more information, see [DeleteMFADeviceForUser](~~341675~~).
        *   Access permissions: You must remove the access permissions on the accounts in your resource directory from the user. For more information, see [DeleteAccessAssignment](~~338350~~).
        *   Groups: You must remove the user from groups. For more information, see [RemoveUserFromGroup](~~335116~~).
        
        @param request: DeleteUserRequest
        @return: DeleteUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_with_options_async(request, runtime)

    def delete_user_provisioning_with_options(
        self,
        request: cloudsso_20210515_models.DeleteUserProvisioningRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.DeleteUserProvisioningResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deletion_strategy):
            query['DeletionStrategy'] = request.deletion_strategy
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.user_provisioning_id):
            query['UserProvisioningId'] = request.user_provisioning_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUserProvisioning',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.DeleteUserProvisioningResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_provisioning_with_options_async(
        self,
        request: cloudsso_20210515_models.DeleteUserProvisioningRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.DeleteUserProvisioningResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deletion_strategy):
            query['DeletionStrategy'] = request.deletion_strategy
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.user_provisioning_id):
            query['UserProvisioningId'] = request.user_provisioning_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUserProvisioning',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.DeleteUserProvisioningResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user_provisioning(
        self,
        request: cloudsso_20210515_models.DeleteUserProvisioningRequest,
    ) -> cloudsso_20210515_models.DeleteUserProvisioningResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_user_provisioning_with_options(request, runtime)

    async def delete_user_provisioning_async(
        self,
        request: cloudsso_20210515_models.DeleteUserProvisioningRequest,
    ) -> cloudsso_20210515_models.DeleteUserProvisioningResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_provisioning_with_options_async(request, runtime)

    def delete_user_provisioning_event_with_options(
        self,
        request: cloudsso_20210515_models.DeleteUserProvisioningEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.DeleteUserProvisioningEventResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.user_provisioning_id):
            query['UserProvisioningId'] = request.user_provisioning_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUserProvisioningEvent',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.DeleteUserProvisioningEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_provisioning_event_with_options_async(
        self,
        request: cloudsso_20210515_models.DeleteUserProvisioningEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.DeleteUserProvisioningEventResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        if not UtilClient.is_unset(request.user_provisioning_id):
            query['UserProvisioningId'] = request.user_provisioning_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUserProvisioningEvent',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.DeleteUserProvisioningEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user_provisioning_event(
        self,
        request: cloudsso_20210515_models.DeleteUserProvisioningEventRequest,
    ) -> cloudsso_20210515_models.DeleteUserProvisioningEventResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_user_provisioning_event_with_options(request, runtime)

    async def delete_user_provisioning_event_async(
        self,
        request: cloudsso_20210515_models.DeleteUserProvisioningEventRequest,
    ) -> cloudsso_20210515_models.DeleteUserProvisioningEventResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_provisioning_event_with_options_async(request, runtime)

    def deprovision_access_configuration_with_options(
        self,
        request: cloudsso_20210515_models.DeprovisionAccessConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.DeprovisionAccessConfigurationResponse:
        """
        When you call this operation, an asynchronous task is automatically created. You can call the [GetTask](~~340670~~) operation to query the progress of the task based on the value of the `TaskId` response parameter.
        This topic provides an example on how to de-provision the access configuration `ac-00jhtfl8thteu6uj****` from the account `114240524784****` in your resource directory.
        
        @param request: DeprovisionAccessConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeprovisionAccessConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeprovisionAccessConfiguration',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        When you call this operation, an asynchronous task is automatically created. You can call the [GetTask](~~340670~~) operation to query the progress of the task based on the value of the `TaskId` response parameter.
        This topic provides an example on how to de-provision the access configuration `ac-00jhtfl8thteu6uj****` from the account `114240524784****` in your resource directory.
        
        @param request: DeprovisionAccessConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeprovisionAccessConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeprovisionAccessConfiguration',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        When you call this operation, an asynchronous task is automatically created. You can call the [GetTask](~~340670~~) operation to query the progress of the task based on the value of the `TaskId` response parameter.
        This topic provides an example on how to de-provision the access configuration `ac-00jhtfl8thteu6uj****` from the account `114240524784****` in your resource directory.
        
        @param request: DeprovisionAccessConfigurationRequest
        @return: DeprovisionAccessConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.deprovision_access_configuration_with_options(request, runtime)

    async def deprovision_access_configuration_async(
        self,
        request: cloudsso_20210515_models.DeprovisionAccessConfigurationRequest,
    ) -> cloudsso_20210515_models.DeprovisionAccessConfigurationResponse:
        """
        When you call this operation, an asynchronous task is automatically created. You can call the [GetTask](~~340670~~) operation to query the progress of the task based on the value of the `TaskId` response parameter.
        This topic provides an example on how to de-provision the access configuration `ac-00jhtfl8thteu6uj****` from the account `114240524784****` in your resource directory.
        
        @param request: DeprovisionAccessConfigurationRequest
        @return: DeprovisionAccessConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.deprovision_access_configuration_with_options_async(request, runtime)

    def disable_service_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.DisableServiceResponse:
        """
        If your CloudSSO has no directory, you can disable CloudSSO based on your business requirements. After you disable CloudSSO, you can enable it at any time.
        
        @param request: DisableServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableServiceResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DisableService',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        If your CloudSSO has no directory, you can disable CloudSSO based on your business requirements. After you disable CloudSSO, you can enable it at any time.
        
        @param request: DisableServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableServiceResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DisableService',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.DisableServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_service(self) -> cloudsso_20210515_models.DisableServiceResponse:
        """
        If your CloudSSO has no directory, you can disable CloudSSO based on your business requirements. After you disable CloudSSO, you can enable it at any time.
        
        @return: DisableServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_service_with_options(runtime)

    async def disable_service_async(self) -> cloudsso_20210515_models.DisableServiceResponse:
        """
        If your CloudSSO has no directory, you can disable CloudSSO based on your business requirements. After you disable CloudSSO, you can enable it at any time.
        
        @return: DisableServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_service_with_options_async(runtime)

    def enable_service_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.EnableServiceResponse:
        """
        You can call this operation only if your account belongs to the management account that is used to enable a resource directory and has permissions to enable CloudSSO. For more information, see [Enable CloudSSO](~~262819~~).
        If you call this operation, you agree to the [Alibaba Cloud International Website Product Terms of Service](https://www.alibabacloud.com/help/doc-detail/42416.htm).
        
        @param request: EnableServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableServiceResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='EnableService',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        You can call this operation only if your account belongs to the management account that is used to enable a resource directory and has permissions to enable CloudSSO. For more information, see [Enable CloudSSO](~~262819~~).
        If you call this operation, you agree to the [Alibaba Cloud International Website Product Terms of Service](https://www.alibabacloud.com/help/doc-detail/42416.htm).
        
        @param request: EnableServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableServiceResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='EnableService',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.EnableServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_service(self) -> cloudsso_20210515_models.EnableServiceResponse:
        """
        You can call this operation only if your account belongs to the management account that is used to enable a resource directory and has permissions to enable CloudSSO. For more information, see [Enable CloudSSO](~~262819~~).
        If you call this operation, you agree to the [Alibaba Cloud International Website Product Terms of Service](https://www.alibabacloud.com/help/doc-detail/42416.htm).
        
        @return: EnableServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_service_with_options(runtime)

    async def enable_service_async(self) -> cloudsso_20210515_models.EnableServiceResponse:
        """
        You can call this operation only if your account belongs to the management account that is used to enable a resource directory and has permissions to enable CloudSSO. For more information, see [Enable CloudSSO](~~262819~~).
        If you call this operation, you agree to the [Alibaba Cloud International Website Product Terms of Service](https://www.alibabacloud.com/help/doc-detail/42416.htm).
        
        @return: EnableServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_service_with_options_async(runtime)

    def get_access_configuration_with_options(
        self,
        request: cloudsso_20210515_models.GetAccessConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.GetAccessConfigurationResponse:
        """
        This topic provides an example on how to query the information about the access configuration whose ID is `ac-00ccule7tadaijxc***`.
        
        @param request: GetAccessConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAccessConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccessConfiguration',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to query the information about the access configuration whose ID is `ac-00ccule7tadaijxc***`.
        
        @param request: GetAccessConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAccessConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccessConfiguration',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to query the information about the access configuration whose ID is `ac-00ccule7tadaijxc***`.
        
        @param request: GetAccessConfigurationRequest
        @return: GetAccessConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_access_configuration_with_options(request, runtime)

    async def get_access_configuration_async(
        self,
        request: cloudsso_20210515_models.GetAccessConfigurationRequest,
    ) -> cloudsso_20210515_models.GetAccessConfigurationResponse:
        """
        This topic provides an example on how to query the information about the access configuration whose ID is `ac-00ccule7tadaijxc***`.
        
        @param request: GetAccessConfigurationRequest
        @return: GetAccessConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_access_configuration_with_options_async(request, runtime)

    def get_directory_with_options(
        self,
        request: cloudsso_20210515_models.GetDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.GetDirectoryResponse:
        """
        This topic provides an example on how to query information about the directory whose ID is `d-00fc2p61***`.
        
        @param request: GetDirectoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDirectoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDirectory',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to query information about the directory whose ID is `d-00fc2p61***`.
        
        @param request: GetDirectoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDirectoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDirectory',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to query information about the directory whose ID is `d-00fc2p61***`.
        
        @param request: GetDirectoryRequest
        @return: GetDirectoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_directory_with_options(request, runtime)

    async def get_directory_async(
        self,
        request: cloudsso_20210515_models.GetDirectoryRequest,
    ) -> cloudsso_20210515_models.GetDirectoryResponse:
        """
        This topic provides an example on how to query information about the directory whose ID is `d-00fc2p61***`.
        
        @param request: GetDirectoryRequest
        @return: GetDirectoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_directory_with_options_async(request, runtime)

    def get_directory_samlservice_provider_info_with_options(
        self,
        request: cloudsso_20210515_models.GetDirectorySAMLServiceProviderInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.GetDirectorySAMLServiceProviderInfoResponse:
        """
        During SAML 2.0-based single sign-on (SSO) logon, CloudSSO is an SP, and the identity management system of an enterprise is an identity provider (IdP).
        This topic provides an example on how to query the information about the SP within the directory `d-00fc2p61****`.
        
        @param request: GetDirectorySAMLServiceProviderInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDirectorySAMLServiceProviderInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDirectorySAMLServiceProviderInfo',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        During SAML 2.0-based single sign-on (SSO) logon, CloudSSO is an SP, and the identity management system of an enterprise is an identity provider (IdP).
        This topic provides an example on how to query the information about the SP within the directory `d-00fc2p61****`.
        
        @param request: GetDirectorySAMLServiceProviderInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDirectorySAMLServiceProviderInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDirectorySAMLServiceProviderInfo',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        During SAML 2.0-based single sign-on (SSO) logon, CloudSSO is an SP, and the identity management system of an enterprise is an identity provider (IdP).
        This topic provides an example on how to query the information about the SP within the directory `d-00fc2p61****`.
        
        @param request: GetDirectorySAMLServiceProviderInfoRequest
        @return: GetDirectorySAMLServiceProviderInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_directory_samlservice_provider_info_with_options(request, runtime)

    async def get_directory_samlservice_provider_info_async(
        self,
        request: cloudsso_20210515_models.GetDirectorySAMLServiceProviderInfoRequest,
    ) -> cloudsso_20210515_models.GetDirectorySAMLServiceProviderInfoResponse:
        """
        During SAML 2.0-based single sign-on (SSO) logon, CloudSSO is an SP, and the identity management system of an enterprise is an identity provider (IdP).
        This topic provides an example on how to query the information about the SP within the directory `d-00fc2p61****`.
        
        @param request: GetDirectorySAMLServiceProviderInfoRequest
        @return: GetDirectorySAMLServiceProviderInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_directory_samlservice_provider_info_with_options_async(request, runtime)

    def get_directory_statistics_with_options(
        self,
        request: cloudsso_20210515_models.GetDirectoryStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.GetDirectoryStatisticsResponse:
        """
        ### [](#)
        This topic provides an example on how to query the statistics of a directory whose ID is `d-00fc2p61****`. The statistics include the number of users, quota for users, number of groups, quota for groups, number of access configurations, quota for access configurations, quota for system policies that can be configured for an access configuration, number of access permissions that are assigned, number of System for Cross-domain Identity Management (SCIM) credentials, number of asynchronous tasks, status of single sign-on (SSO), and status of SCIM synchronization.
        ### [](#qps)Limit
        You can call this operation up to 100 times per second per account. This operation is globally limited to 100 times per second across all accounts. If the number of the calls per second exceeds a limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limits when you call this operation.
        
        @param request: GetDirectoryStatisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDirectoryStatisticsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDirectoryStatistics',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        ### [](#)
        This topic provides an example on how to query the statistics of a directory whose ID is `d-00fc2p61****`. The statistics include the number of users, quota for users, number of groups, quota for groups, number of access configurations, quota for access configurations, quota for system policies that can be configured for an access configuration, number of access permissions that are assigned, number of System for Cross-domain Identity Management (SCIM) credentials, number of asynchronous tasks, status of single sign-on (SSO), and status of SCIM synchronization.
        ### [](#qps)Limit
        You can call this operation up to 100 times per second per account. This operation is globally limited to 100 times per second across all accounts. If the number of the calls per second exceeds a limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limits when you call this operation.
        
        @param request: GetDirectoryStatisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDirectoryStatisticsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDirectoryStatistics',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        ### [](#)
        This topic provides an example on how to query the statistics of a directory whose ID is `d-00fc2p61****`. The statistics include the number of users, quota for users, number of groups, quota for groups, number of access configurations, quota for access configurations, quota for system policies that can be configured for an access configuration, number of access permissions that are assigned, number of System for Cross-domain Identity Management (SCIM) credentials, number of asynchronous tasks, status of single sign-on (SSO), and status of SCIM synchronization.
        ### [](#qps)Limit
        You can call this operation up to 100 times per second per account. This operation is globally limited to 100 times per second across all accounts. If the number of the calls per second exceeds a limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limits when you call this operation.
        
        @param request: GetDirectoryStatisticsRequest
        @return: GetDirectoryStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_directory_statistics_with_options(request, runtime)

    async def get_directory_statistics_async(
        self,
        request: cloudsso_20210515_models.GetDirectoryStatisticsRequest,
    ) -> cloudsso_20210515_models.GetDirectoryStatisticsResponse:
        """
        ### [](#)
        This topic provides an example on how to query the statistics of a directory whose ID is `d-00fc2p61****`. The statistics include the number of users, quota for users, number of groups, quota for groups, number of access configurations, quota for access configurations, quota for system policies that can be configured for an access configuration, number of access permissions that are assigned, number of System for Cross-domain Identity Management (SCIM) credentials, number of asynchronous tasks, status of single sign-on (SSO), and status of SCIM synchronization.
        ### [](#qps)Limit
        You can call this operation up to 100 times per second per account. This operation is globally limited to 100 times per second across all accounts. If the number of the calls per second exceeds a limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limits when you call this operation.
        
        @param request: GetDirectoryStatisticsRequest
        @return: GetDirectoryStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_directory_statistics_with_options_async(request, runtime)

    def get_external_samlidentity_provider_with_options(
        self,
        request: cloudsso_20210515_models.GetExternalSAMLIdentityProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.GetExternalSAMLIdentityProviderResponse:
        """
        This topic provides an example on how to query the configurations of the SAML IdP within the directory `d-00fc2p61***`.
        
        @param request: GetExternalSAMLIdentityProviderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetExternalSAMLIdentityProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetExternalSAMLIdentityProvider',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to query the configurations of the SAML IdP within the directory `d-00fc2p61***`.
        
        @param request: GetExternalSAMLIdentityProviderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetExternalSAMLIdentityProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetExternalSAMLIdentityProvider',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to query the configurations of the SAML IdP within the directory `d-00fc2p61***`.
        
        @param request: GetExternalSAMLIdentityProviderRequest
        @return: GetExternalSAMLIdentityProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_external_samlidentity_provider_with_options(request, runtime)

    async def get_external_samlidentity_provider_async(
        self,
        request: cloudsso_20210515_models.GetExternalSAMLIdentityProviderRequest,
    ) -> cloudsso_20210515_models.GetExternalSAMLIdentityProviderResponse:
        """
        This topic provides an example on how to query the configurations of the SAML IdP within the directory `d-00fc2p61***`.
        
        @param request: GetExternalSAMLIdentityProviderRequest
        @return: GetExternalSAMLIdentityProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_external_samlidentity_provider_with_options_async(request, runtime)

    def get_group_with_options(
        self,
        request: cloudsso_20210515_models.GetGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.GetGroupResponse:
        """
        This topic provides an example on how to query the information about the group `g-00jqzghi2n3o5hkh***` in the directory `d-00fc2p61****`.
        
        @param request: GetGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGroup',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to query the information about the group `g-00jqzghi2n3o5hkh***` in the directory `d-00fc2p61****`.
        
        @param request: GetGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGroup',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to query the information about the group `g-00jqzghi2n3o5hkh***` in the directory `d-00fc2p61****`.
        
        @param request: GetGroupRequest
        @return: GetGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_group_with_options(request, runtime)

    async def get_group_async(
        self,
        request: cloudsso_20210515_models.GetGroupRequest,
    ) -> cloudsso_20210515_models.GetGroupResponse:
        """
        This topic provides an example on how to query the information about the group `g-00jqzghi2n3o5hkh***` in the directory `d-00fc2p61****`.
        
        @param request: GetGroupRequest
        @return: GetGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_group_with_options_async(request, runtime)

    def get_mfaauthentication_setting_info_with_options(
        self,
        request: cloudsso_20210515_models.GetMFAAuthenticationSettingInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.GetMFAAuthenticationSettingInfoResponse:
        """
        If you enable username-password logon for CloudSSO users, you can also configure MFA for the users.
        This topic provides an example on how to query the MFA setting of all CloudSSO users that belong to the directory named `00q8wbq42wiltcrk****`.
        
        @param request: GetMFAAuthenticationSettingInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMFAAuthenticationSettingInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMFAAuthenticationSettingInfo',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.GetMFAAuthenticationSettingInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mfaauthentication_setting_info_with_options_async(
        self,
        request: cloudsso_20210515_models.GetMFAAuthenticationSettingInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.GetMFAAuthenticationSettingInfoResponse:
        """
        If you enable username-password logon for CloudSSO users, you can also configure MFA for the users.
        This topic provides an example on how to query the MFA setting of all CloudSSO users that belong to the directory named `00q8wbq42wiltcrk****`.
        
        @param request: GetMFAAuthenticationSettingInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMFAAuthenticationSettingInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMFAAuthenticationSettingInfo',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.GetMFAAuthenticationSettingInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mfaauthentication_setting_info(
        self,
        request: cloudsso_20210515_models.GetMFAAuthenticationSettingInfoRequest,
    ) -> cloudsso_20210515_models.GetMFAAuthenticationSettingInfoResponse:
        """
        If you enable username-password logon for CloudSSO users, you can also configure MFA for the users.
        This topic provides an example on how to query the MFA setting of all CloudSSO users that belong to the directory named `00q8wbq42wiltcrk****`.
        
        @param request: GetMFAAuthenticationSettingInfoRequest
        @return: GetMFAAuthenticationSettingInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_mfaauthentication_setting_info_with_options(request, runtime)

    async def get_mfaauthentication_setting_info_async(
        self,
        request: cloudsso_20210515_models.GetMFAAuthenticationSettingInfoRequest,
    ) -> cloudsso_20210515_models.GetMFAAuthenticationSettingInfoResponse:
        """
        If you enable username-password logon for CloudSSO users, you can also configure MFA for the users.
        This topic provides an example on how to query the MFA setting of all CloudSSO users that belong to the directory named `00q8wbq42wiltcrk****`.
        
        @param request: GetMFAAuthenticationSettingInfoRequest
        @return: GetMFAAuthenticationSettingInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_mfaauthentication_setting_info_with_options_async(request, runtime)

    def get_mfaauthentication_settings_with_options(
        self,
        request: cloudsso_20210515_models.GetMFAAuthenticationSettingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.GetMFAAuthenticationSettingsResponse:
        """
        > This operation is no longer maintained and updated. You can call the [GetMFAAuthenticationSettingInfo](~~611286~~) operation to query more detailed information.
        This topic provides an example on how to query the MFA setting of the users that belong to the directory named `d-00fc2p61****`. The returned result shows that MFA is enabled for all the users.
        
        @param request: GetMFAAuthenticationSettingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMFAAuthenticationSettingsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMFAAuthenticationSettings',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.GetMFAAuthenticationSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mfaauthentication_settings_with_options_async(
        self,
        request: cloudsso_20210515_models.GetMFAAuthenticationSettingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.GetMFAAuthenticationSettingsResponse:
        """
        > This operation is no longer maintained and updated. You can call the [GetMFAAuthenticationSettingInfo](~~611286~~) operation to query more detailed information.
        This topic provides an example on how to query the MFA setting of the users that belong to the directory named `d-00fc2p61****`. The returned result shows that MFA is enabled for all the users.
        
        @param request: GetMFAAuthenticationSettingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMFAAuthenticationSettingsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMFAAuthenticationSettings',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.GetMFAAuthenticationSettingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mfaauthentication_settings(
        self,
        request: cloudsso_20210515_models.GetMFAAuthenticationSettingsRequest,
    ) -> cloudsso_20210515_models.GetMFAAuthenticationSettingsResponse:
        """
        > This operation is no longer maintained and updated. You can call the [GetMFAAuthenticationSettingInfo](~~611286~~) operation to query more detailed information.
        This topic provides an example on how to query the MFA setting of the users that belong to the directory named `d-00fc2p61****`. The returned result shows that MFA is enabled for all the users.
        
        @param request: GetMFAAuthenticationSettingsRequest
        @return: GetMFAAuthenticationSettingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_mfaauthentication_settings_with_options(request, runtime)

    async def get_mfaauthentication_settings_async(
        self,
        request: cloudsso_20210515_models.GetMFAAuthenticationSettingsRequest,
    ) -> cloudsso_20210515_models.GetMFAAuthenticationSettingsResponse:
        """
        > This operation is no longer maintained and updated. You can call the [GetMFAAuthenticationSettingInfo](~~611286~~) operation to query more detailed information.
        This topic provides an example on how to query the MFA setting of the users that belong to the directory named `d-00fc2p61****`. The returned result shows that MFA is enabled for all the users.
        
        @param request: GetMFAAuthenticationSettingsRequest
        @return: GetMFAAuthenticationSettingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_mfaauthentication_settings_with_options_async(request, runtime)

    def get_mfaauthentication_status_with_options(
        self,
        request: cloudsso_20210515_models.GetMFAAuthenticationStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.GetMFAAuthenticationStatusResponse:
        """
        This topic provides an example on how to check whether MFA is enabled for users in the directory whose ID is `00fc2p61***`. The returned result shows that MFA is in the Enabled state.
        
        @param request: GetMFAAuthenticationStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMFAAuthenticationStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMFAAuthenticationStatus',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to check whether MFA is enabled for users in the directory whose ID is `00fc2p61***`. The returned result shows that MFA is in the Enabled state.
        
        @param request: GetMFAAuthenticationStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMFAAuthenticationStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMFAAuthenticationStatus',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to check whether MFA is enabled for users in the directory whose ID is `00fc2p61***`. The returned result shows that MFA is in the Enabled state.
        
        @param request: GetMFAAuthenticationStatusRequest
        @return: GetMFAAuthenticationStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_mfaauthentication_status_with_options(request, runtime)

    async def get_mfaauthentication_status_async(
        self,
        request: cloudsso_20210515_models.GetMFAAuthenticationStatusRequest,
    ) -> cloudsso_20210515_models.GetMFAAuthenticationStatusResponse:
        """
        This topic provides an example on how to check whether MFA is enabled for users in the directory whose ID is `00fc2p61***`. The returned result shows that MFA is in the Enabled state.
        
        @param request: GetMFAAuthenticationStatusRequest
        @return: GetMFAAuthenticationStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_mfaauthentication_status_with_options_async(request, runtime)

    def get_scimsynchronization_status_with_options(
        self,
        request: cloudsso_20210515_models.GetSCIMSynchronizationStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.GetSCIMSynchronizationStatusResponse:
        """
        This topic provides an example on how to query the status of SCIM synchronization within the directory `d-00fc2p61***`. The returned result shows that SCIM synchronization is in the Enabled state.
        
        @param request: GetSCIMSynchronizationStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSCIMSynchronizationStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSCIMSynchronizationStatus',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to query the status of SCIM synchronization within the directory `d-00fc2p61***`. The returned result shows that SCIM synchronization is in the Enabled state.
        
        @param request: GetSCIMSynchronizationStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSCIMSynchronizationStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSCIMSynchronizationStatus',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to query the status of SCIM synchronization within the directory `d-00fc2p61***`. The returned result shows that SCIM synchronization is in the Enabled state.
        
        @param request: GetSCIMSynchronizationStatusRequest
        @return: GetSCIMSynchronizationStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_scimsynchronization_status_with_options(request, runtime)

    async def get_scimsynchronization_status_async(
        self,
        request: cloudsso_20210515_models.GetSCIMSynchronizationStatusRequest,
    ) -> cloudsso_20210515_models.GetSCIMSynchronizationStatusResponse:
        """
        This topic provides an example on how to query the status of SCIM synchronization within the directory `d-00fc2p61***`. The returned result shows that SCIM synchronization is in the Enabled state.
        
        @param request: GetSCIMSynchronizationStatusRequest
        @return: GetSCIMSynchronizationStatusResponse
        """
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
            req_body_type='formData',
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
            req_body_type='formData',
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
        """
        This topic provides an example on how to query the information about the task whose ID is `t-shfqw1u1edszvxw5***`.
        
        @param request: GetTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTask',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to query the information about the task whose ID is `t-shfqw1u1edszvxw5***`.
        
        @param request: GetTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTask',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to query the information about the task whose ID is `t-shfqw1u1edszvxw5***`.
        
        @param request: GetTaskRequest
        @return: GetTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_task_with_options(request, runtime)

    async def get_task_async(
        self,
        request: cloudsso_20210515_models.GetTaskRequest,
    ) -> cloudsso_20210515_models.GetTaskResponse:
        """
        This topic provides an example on how to query the information about the task whose ID is `t-shfqw1u1edszvxw5***`.
        
        @param request: GetTaskRequest
        @return: GetTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_task_with_options_async(request, runtime)

    def get_task_status_with_options(
        self,
        request: cloudsso_20210515_models.GetTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.GetTaskStatusResponse:
        """
        You can call the GetTaskStatus operation to query the status of an asynchronous task. If you want to query more information about an asynchronous task, you can call the [GetTask](~~340670~~) operation.
        This topic provides an example on how to query the information about the task whose ID is `t-shfqw1u1edszvxw5****`.
        
        @param request: GetTaskStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTaskStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTaskStatus',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        You can call the GetTaskStatus operation to query the status of an asynchronous task. If you want to query more information about an asynchronous task, you can call the [GetTask](~~340670~~) operation.
        This topic provides an example on how to query the information about the task whose ID is `t-shfqw1u1edszvxw5****`.
        
        @param request: GetTaskStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTaskStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTaskStatus',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        You can call the GetTaskStatus operation to query the status of an asynchronous task. If you want to query more information about an asynchronous task, you can call the [GetTask](~~340670~~) operation.
        This topic provides an example on how to query the information about the task whose ID is `t-shfqw1u1edszvxw5****`.
        
        @param request: GetTaskStatusRequest
        @return: GetTaskStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_task_status_with_options(request, runtime)

    async def get_task_status_async(
        self,
        request: cloudsso_20210515_models.GetTaskStatusRequest,
    ) -> cloudsso_20210515_models.GetTaskStatusResponse:
        """
        You can call the GetTaskStatus operation to query the status of an asynchronous task. If you want to query more information about an asynchronous task, you can call the [GetTask](~~340670~~) operation.
        This topic provides an example on how to query the information about the task whose ID is `t-shfqw1u1edszvxw5****`.
        
        @param request: GetTaskStatusRequest
        @return: GetTaskStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_task_status_with_options_async(request, runtime)

    def get_user_with_options(
        self,
        request: cloudsso_20210515_models.GetUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.GetUserResponse:
        """
        This topic provides an example on how to query information about the user whose ID is `u-00q8wbq42wiltcrk***` in the `d-00fc2p61****` directory.
        
        @param request: GetUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUser',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to query information about the user whose ID is `u-00q8wbq42wiltcrk***` in the `d-00fc2p61****` directory.
        
        @param request: GetUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUser',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to query information about the user whose ID is `u-00q8wbq42wiltcrk***` in the `d-00fc2p61****` directory.
        
        @param request: GetUserRequest
        @return: GetUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_user_with_options(request, runtime)

    async def get_user_async(
        self,
        request: cloudsso_20210515_models.GetUserRequest,
    ) -> cloudsso_20210515_models.GetUserResponse:
        """
        This topic provides an example on how to query information about the user whose ID is `u-00q8wbq42wiltcrk***` in the `d-00fc2p61****` directory.
        
        @param request: GetUserRequest
        @return: GetUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_user_with_options_async(request, runtime)

    def get_user_mfaauthentication_settings_with_options(
        self,
        request: cloudsso_20210515_models.GetUserMFAAuthenticationSettingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.GetUserMFAAuthenticationSettingsResponse:
        """
        This topic provides an example on how to query the MFA setting of the user named `u-00q8wbq42wiltcrk***`. The returned result shows that MFA is enabled for the user.
        
        @param request: GetUserMFAAuthenticationSettingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserMFAAuthenticationSettingsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserMFAAuthenticationSettings',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.GetUserMFAAuthenticationSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_mfaauthentication_settings_with_options_async(
        self,
        request: cloudsso_20210515_models.GetUserMFAAuthenticationSettingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.GetUserMFAAuthenticationSettingsResponse:
        """
        This topic provides an example on how to query the MFA setting of the user named `u-00q8wbq42wiltcrk***`. The returned result shows that MFA is enabled for the user.
        
        @param request: GetUserMFAAuthenticationSettingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserMFAAuthenticationSettingsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserMFAAuthenticationSettings',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.GetUserMFAAuthenticationSettingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_mfaauthentication_settings(
        self,
        request: cloudsso_20210515_models.GetUserMFAAuthenticationSettingsRequest,
    ) -> cloudsso_20210515_models.GetUserMFAAuthenticationSettingsResponse:
        """
        This topic provides an example on how to query the MFA setting of the user named `u-00q8wbq42wiltcrk***`. The returned result shows that MFA is enabled for the user.
        
        @param request: GetUserMFAAuthenticationSettingsRequest
        @return: GetUserMFAAuthenticationSettingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_user_mfaauthentication_settings_with_options(request, runtime)

    async def get_user_mfaauthentication_settings_async(
        self,
        request: cloudsso_20210515_models.GetUserMFAAuthenticationSettingsRequest,
    ) -> cloudsso_20210515_models.GetUserMFAAuthenticationSettingsResponse:
        """
        This topic provides an example on how to query the MFA setting of the user named `u-00q8wbq42wiltcrk***`. The returned result shows that MFA is enabled for the user.
        
        @param request: GetUserMFAAuthenticationSettingsRequest
        @return: GetUserMFAAuthenticationSettingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_user_mfaauthentication_settings_with_options_async(request, runtime)

    def get_user_provisioning_with_options(
        self,
        request: cloudsso_20210515_models.GetUserProvisioningRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.GetUserProvisioningResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.user_provisioning_id):
            query['UserProvisioningId'] = request.user_provisioning_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserProvisioning',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.GetUserProvisioningResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_provisioning_with_options_async(
        self,
        request: cloudsso_20210515_models.GetUserProvisioningRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.GetUserProvisioningResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.user_provisioning_id):
            query['UserProvisioningId'] = request.user_provisioning_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserProvisioning',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.GetUserProvisioningResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_provisioning(
        self,
        request: cloudsso_20210515_models.GetUserProvisioningRequest,
    ) -> cloudsso_20210515_models.GetUserProvisioningResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_user_provisioning_with_options(request, runtime)

    async def get_user_provisioning_async(
        self,
        request: cloudsso_20210515_models.GetUserProvisioningRequest,
    ) -> cloudsso_20210515_models.GetUserProvisioningResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_user_provisioning_with_options_async(request, runtime)

    def get_user_provisioning_configuration_with_options(
        self,
        request: cloudsso_20210515_models.GetUserProvisioningConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.GetUserProvisioningConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserProvisioningConfiguration',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.GetUserProvisioningConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_provisioning_configuration_with_options_async(
        self,
        request: cloudsso_20210515_models.GetUserProvisioningConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.GetUserProvisioningConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserProvisioningConfiguration',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.GetUserProvisioningConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_provisioning_configuration(
        self,
        request: cloudsso_20210515_models.GetUserProvisioningConfigurationRequest,
    ) -> cloudsso_20210515_models.GetUserProvisioningConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_user_provisioning_configuration_with_options(request, runtime)

    async def get_user_provisioning_configuration_async(
        self,
        request: cloudsso_20210515_models.GetUserProvisioningConfigurationRequest,
    ) -> cloudsso_20210515_models.GetUserProvisioningConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_user_provisioning_configuration_with_options_async(request, runtime)

    def get_user_provisioning_event_with_options(
        self,
        request: cloudsso_20210515_models.GetUserProvisioningEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.GetUserProvisioningEventResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserProvisioningEvent',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.GetUserProvisioningEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_provisioning_event_with_options_async(
        self,
        request: cloudsso_20210515_models.GetUserProvisioningEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.GetUserProvisioningEventResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserProvisioningEvent',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.GetUserProvisioningEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_provisioning_event(
        self,
        request: cloudsso_20210515_models.GetUserProvisioningEventRequest,
    ) -> cloudsso_20210515_models.GetUserProvisioningEventResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_user_provisioning_event_with_options(request, runtime)

    async def get_user_provisioning_event_async(
        self,
        request: cloudsso_20210515_models.GetUserProvisioningEventRequest,
    ) -> cloudsso_20210515_models.GetUserProvisioningEventResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_user_provisioning_event_with_options_async(request, runtime)

    def get_user_provisioning_rd_account_statistics_with_options(
        self,
        request: cloudsso_20210515_models.GetUserProvisioningRdAccountStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.GetUserProvisioningRdAccountStatisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.rd_member_id):
            query['RdMemberId'] = request.rd_member_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserProvisioningRdAccountStatistics',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.GetUserProvisioningRdAccountStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_provisioning_rd_account_statistics_with_options_async(
        self,
        request: cloudsso_20210515_models.GetUserProvisioningRdAccountStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.GetUserProvisioningRdAccountStatisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.rd_member_id):
            query['RdMemberId'] = request.rd_member_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserProvisioningRdAccountStatistics',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.GetUserProvisioningRdAccountStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_provisioning_rd_account_statistics(
        self,
        request: cloudsso_20210515_models.GetUserProvisioningRdAccountStatisticsRequest,
    ) -> cloudsso_20210515_models.GetUserProvisioningRdAccountStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_user_provisioning_rd_account_statistics_with_options(request, runtime)

    async def get_user_provisioning_rd_account_statistics_async(
        self,
        request: cloudsso_20210515_models.GetUserProvisioningRdAccountStatisticsRequest,
    ) -> cloudsso_20210515_models.GetUserProvisioningRdAccountStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_user_provisioning_rd_account_statistics_with_options_async(request, runtime)

    def get_user_provisioning_statistics_with_options(
        self,
        request: cloudsso_20210515_models.GetUserProvisioningStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.GetUserProvisioningStatisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.user_provisioning_id):
            query['UserProvisioningId'] = request.user_provisioning_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserProvisioningStatistics',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.GetUserProvisioningStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_provisioning_statistics_with_options_async(
        self,
        request: cloudsso_20210515_models.GetUserProvisioningStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.GetUserProvisioningStatisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.user_provisioning_id):
            query['UserProvisioningId'] = request.user_provisioning_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserProvisioningStatistics',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.GetUserProvisioningStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_provisioning_statistics(
        self,
        request: cloudsso_20210515_models.GetUserProvisioningStatisticsRequest,
    ) -> cloudsso_20210515_models.GetUserProvisioningStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_user_provisioning_statistics_with_options(request, runtime)

    async def get_user_provisioning_statistics_async(
        self,
        request: cloudsso_20210515_models.GetUserProvisioningStatisticsRequest,
    ) -> cloudsso_20210515_models.GetUserProvisioningStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_user_provisioning_statistics_with_options_async(request, runtime)

    def list_access_assignments_with_options(
        self,
        request: cloudsso_20210515_models.ListAccessAssignmentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.ListAccessAssignmentsResponse:
        """
        This topic provides an example on how to query the assigned access permissions on the account `114240524784***` in your resource directory. The returned result shows that access permissions on the account in your resource directory are assigned to one user.
        
        @param request: ListAccessAssignmentsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAccessAssignmentsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.principal_id):
            query['PrincipalId'] = request.principal_id
        if not UtilClient.is_unset(request.principal_type):
            query['PrincipalType'] = request.principal_type
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccessAssignments',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to query the assigned access permissions on the account `114240524784***` in your resource directory. The returned result shows that access permissions on the account in your resource directory are assigned to one user.
        
        @param request: ListAccessAssignmentsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAccessAssignmentsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.principal_id):
            query['PrincipalId'] = request.principal_id
        if not UtilClient.is_unset(request.principal_type):
            query['PrincipalType'] = request.principal_type
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccessAssignments',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to query the assigned access permissions on the account `114240524784***` in your resource directory. The returned result shows that access permissions on the account in your resource directory are assigned to one user.
        
        @param request: ListAccessAssignmentsRequest
        @return: ListAccessAssignmentsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_access_assignments_with_options(request, runtime)

    async def list_access_assignments_async(
        self,
        request: cloudsso_20210515_models.ListAccessAssignmentsRequest,
    ) -> cloudsso_20210515_models.ListAccessAssignmentsResponse:
        """
        This topic provides an example on how to query the assigned access permissions on the account `114240524784***` in your resource directory. The returned result shows that access permissions on the account in your resource directory are assigned to one user.
        
        @param request: ListAccessAssignmentsRequest
        @return: ListAccessAssignmentsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_access_assignments_with_options_async(request, runtime)

    def list_access_configuration_provisionings_with_options(
        self,
        request: cloudsso_20210515_models.ListAccessConfigurationProvisioningsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.ListAccessConfigurationProvisioningsResponse:
        """
        This topic provides an example on how to query the accounts for which the access permission `ac-00ccule7tadaijxc***` is provisioned. The returned result shows that the access configuration is provisioned for two accounts in your resource directory.
        
        @param request: ListAccessConfigurationProvisioningsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAccessConfigurationProvisioningsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.provisioning_status):
            query['ProvisioningStatus'] = request.provisioning_status
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccessConfigurationProvisionings',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to query the accounts for which the access permission `ac-00ccule7tadaijxc***` is provisioned. The returned result shows that the access configuration is provisioned for two accounts in your resource directory.
        
        @param request: ListAccessConfigurationProvisioningsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAccessConfigurationProvisioningsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.provisioning_status):
            query['ProvisioningStatus'] = request.provisioning_status
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccessConfigurationProvisionings',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to query the accounts for which the access permission `ac-00ccule7tadaijxc***` is provisioned. The returned result shows that the access configuration is provisioned for two accounts in your resource directory.
        
        @param request: ListAccessConfigurationProvisioningsRequest
        @return: ListAccessConfigurationProvisioningsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_access_configuration_provisionings_with_options(request, runtime)

    async def list_access_configuration_provisionings_async(
        self,
        request: cloudsso_20210515_models.ListAccessConfigurationProvisioningsRequest,
    ) -> cloudsso_20210515_models.ListAccessConfigurationProvisioningsResponse:
        """
        This topic provides an example on how to query the accounts for which the access permission `ac-00ccule7tadaijxc***` is provisioned. The returned result shows that the access configuration is provisioned for two accounts in your resource directory.
        
        @param request: ListAccessConfigurationProvisioningsRequest
        @return: ListAccessConfigurationProvisioningsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_access_configuration_provisionings_with_options_async(request, runtime)

    def list_access_configurations_with_options(
        self,
        request: cloudsso_20210515_models.ListAccessConfigurationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.ListAccessConfigurationsResponse:
        """
        This topic provides an example on how to query the access configurations within the directory `d-00fc2p61***`. The returned result shows that the directory contains the `VPC-Admin` and `ECS-Admin` access configurations.
        
        @param request: ListAccessConfigurationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAccessConfigurationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.status_notifications):
            query['StatusNotifications'] = request.status_notifications
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccessConfigurations',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to query the access configurations within the directory `d-00fc2p61***`. The returned result shows that the directory contains the `VPC-Admin` and `ECS-Admin` access configurations.
        
        @param request: ListAccessConfigurationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAccessConfigurationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.status_notifications):
            query['StatusNotifications'] = request.status_notifications
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccessConfigurations',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to query the access configurations within the directory `d-00fc2p61***`. The returned result shows that the directory contains the `VPC-Admin` and `ECS-Admin` access configurations.
        
        @param request: ListAccessConfigurationsRequest
        @return: ListAccessConfigurationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_access_configurations_with_options(request, runtime)

    async def list_access_configurations_async(
        self,
        request: cloudsso_20210515_models.ListAccessConfigurationsRequest,
    ) -> cloudsso_20210515_models.ListAccessConfigurationsResponse:
        """
        This topic provides an example on how to query the access configurations within the directory `d-00fc2p61***`. The returned result shows that the directory contains the `VPC-Admin` and `ECS-Admin` access configurations.
        
        @param request: ListAccessConfigurationsRequest
        @return: ListAccessConfigurationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_access_configurations_with_options_async(request, runtime)

    def list_directories_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.ListDirectoriesResponse:
        """
        This topic provides an example on how to query the directories within your Alibaba Cloud account. The returned result shows that only one directory with the ID `d-00fc2p61***` is created within your Alibaba Cloud account.
        
        @param request: ListDirectoriesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDirectoriesResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListDirectories',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to query the directories within your Alibaba Cloud account. The returned result shows that only one directory with the ID `d-00fc2p61***` is created within your Alibaba Cloud account.
        
        @param request: ListDirectoriesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDirectoriesResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListDirectories',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.ListDirectoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_directories(self) -> cloudsso_20210515_models.ListDirectoriesResponse:
        """
        This topic provides an example on how to query the directories within your Alibaba Cloud account. The returned result shows that only one directory with the ID `d-00fc2p61***` is created within your Alibaba Cloud account.
        
        @return: ListDirectoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_directories_with_options(runtime)

    async def list_directories_async(self) -> cloudsso_20210515_models.ListDirectoriesResponse:
        """
        This topic provides an example on how to query the directories within your Alibaba Cloud account. The returned result shows that only one directory with the ID `d-00fc2p61***` is created within your Alibaba Cloud account.
        
        @return: ListDirectoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_directories_with_options_async(runtime)

    def list_external_samlid_pcertificates_with_options(
        self,
        request: cloudsso_20210515_models.ListExternalSAMLIdPCertificatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.ListExternalSAMLIdPCertificatesResponse:
        """
        This topic provides an example on how to query the SAML signing certificates within the directory `d-00fc2p61***`. The returned result shows that the directory contains one SAML signing certificate.
        
        @param request: ListExternalSAMLIdPCertificatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExternalSAMLIdPCertificatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExternalSAMLIdPCertificates',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to query the SAML signing certificates within the directory `d-00fc2p61***`. The returned result shows that the directory contains one SAML signing certificate.
        
        @param request: ListExternalSAMLIdPCertificatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExternalSAMLIdPCertificatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExternalSAMLIdPCertificates',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to query the SAML signing certificates within the directory `d-00fc2p61***`. The returned result shows that the directory contains one SAML signing certificate.
        
        @param request: ListExternalSAMLIdPCertificatesRequest
        @return: ListExternalSAMLIdPCertificatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_external_samlid_pcertificates_with_options(request, runtime)

    async def list_external_samlid_pcertificates_async(
        self,
        request: cloudsso_20210515_models.ListExternalSAMLIdPCertificatesRequest,
    ) -> cloudsso_20210515_models.ListExternalSAMLIdPCertificatesResponse:
        """
        This topic provides an example on how to query the SAML signing certificates within the directory `d-00fc2p61***`. The returned result shows that the directory contains one SAML signing certificate.
        
        @param request: ListExternalSAMLIdPCertificatesRequest
        @return: ListExternalSAMLIdPCertificatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_external_samlid_pcertificates_with_options_async(request, runtime)

    def list_group_members_with_options(
        self,
        request: cloudsso_20210515_models.ListGroupMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.ListGroupMembersResponse:
        """
        This topic provides an example on how to query the users in the group `g-00jqzghi2n3o5hkh***`. The returned result shows that the group contains the user `Alice` and the user `user1`.
        
        @param request: ListGroupMembersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGroupMembersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroupMembers',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to query the users in the group `g-00jqzghi2n3o5hkh***`. The returned result shows that the group contains the user `Alice` and the user `user1`.
        
        @param request: ListGroupMembersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGroupMembersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroupMembers',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to query the users in the group `g-00jqzghi2n3o5hkh***`. The returned result shows that the group contains the user `Alice` and the user `user1`.
        
        @param request: ListGroupMembersRequest
        @return: ListGroupMembersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_group_members_with_options(request, runtime)

    async def list_group_members_async(
        self,
        request: cloudsso_20210515_models.ListGroupMembersRequest,
    ) -> cloudsso_20210515_models.ListGroupMembersResponse:
        """
        This topic provides an example on how to query the users in the group `g-00jqzghi2n3o5hkh***`. The returned result shows that the group contains the user `Alice` and the user `user1`.
        
        @param request: ListGroupMembersRequest
        @return: ListGroupMembersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_group_members_with_options_async(request, runtime)

    def list_groups_with_options(
        self,
        request: cloudsso_20210515_models.ListGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.ListGroupsResponse:
        """
        This topic provides an example on how to query the groups in the directory `d-00fc2p61***`. The returned result shows that the directory contains three groups. The groups `group1` and `group2` are synchronized from an external identity provider (IdP). The group `TestGroup` is manually created in CloudSSO.
        
        @param request: ListGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.provision_type):
            query['ProvisionType'] = request.provision_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroups',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to query the groups in the directory `d-00fc2p61***`. The returned result shows that the directory contains three groups. The groups `group1` and `group2` are synchronized from an external identity provider (IdP). The group `TestGroup` is manually created in CloudSSO.
        
        @param request: ListGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.provision_type):
            query['ProvisionType'] = request.provision_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroups',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to query the groups in the directory `d-00fc2p61***`. The returned result shows that the directory contains three groups. The groups `group1` and `group2` are synchronized from an external identity provider (IdP). The group `TestGroup` is manually created in CloudSSO.
        
        @param request: ListGroupsRequest
        @return: ListGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_groups_with_options(request, runtime)

    async def list_groups_async(
        self,
        request: cloudsso_20210515_models.ListGroupsRequest,
    ) -> cloudsso_20210515_models.ListGroupsResponse:
        """
        This topic provides an example on how to query the groups in the directory `d-00fc2p61***`. The returned result shows that the directory contains three groups. The groups `group1` and `group2` are synchronized from an external identity provider (IdP). The group `TestGroup` is manually created in CloudSSO.
        
        @param request: ListGroupsRequest
        @return: ListGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_groups_with_options_async(request, runtime)

    def list_joined_groups_for_user_with_options(
        self,
        request: cloudsso_20210515_models.ListJoinedGroupsForUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.ListJoinedGroupsForUserResponse:
        """
        This topic provides an example on how to query the groups to which the user `u-00q8wbq42wiltcrk***` is added. The returned result shows that the user is added to both the `TestGroup` and the `group1` groups.
        
        @param request: ListJoinedGroupsForUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJoinedGroupsForUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJoinedGroupsForUser',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to query the groups to which the user `u-00q8wbq42wiltcrk***` is added. The returned result shows that the user is added to both the `TestGroup` and the `group1` groups.
        
        @param request: ListJoinedGroupsForUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJoinedGroupsForUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJoinedGroupsForUser',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to query the groups to which the user `u-00q8wbq42wiltcrk***` is added. The returned result shows that the user is added to both the `TestGroup` and the `group1` groups.
        
        @param request: ListJoinedGroupsForUserRequest
        @return: ListJoinedGroupsForUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_joined_groups_for_user_with_options(request, runtime)

    async def list_joined_groups_for_user_async(
        self,
        request: cloudsso_20210515_models.ListJoinedGroupsForUserRequest,
    ) -> cloudsso_20210515_models.ListJoinedGroupsForUserResponse:
        """
        This topic provides an example on how to query the groups to which the user `u-00q8wbq42wiltcrk***` is added. The returned result shows that the user is added to both the `TestGroup` and the `group1` groups.
        
        @param request: ListJoinedGroupsForUserRequest
        @return: ListJoinedGroupsForUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_joined_groups_for_user_with_options_async(request, runtime)

    def list_mfadevices_for_user_with_options(
        self,
        request: cloudsso_20210515_models.ListMFADevicesForUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.ListMFADevicesForUserResponse:
        """
        This topic provides an example on how to query the MFA devices that are bound to the user `u-00q8wbq42wiltcrk***`. The returned result shows that the MFA device named `Alice-MFA1` is bound to the user.
        
        @param request: ListMFADevicesForUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMFADevicesForUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMFADevicesForUser',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to query the MFA devices that are bound to the user `u-00q8wbq42wiltcrk***`. The returned result shows that the MFA device named `Alice-MFA1` is bound to the user.
        
        @param request: ListMFADevicesForUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMFADevicesForUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMFADevicesForUser',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to query the MFA devices that are bound to the user `u-00q8wbq42wiltcrk***`. The returned result shows that the MFA device named `Alice-MFA1` is bound to the user.
        
        @param request: ListMFADevicesForUserRequest
        @return: ListMFADevicesForUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_mfadevices_for_user_with_options(request, runtime)

    async def list_mfadevices_for_user_async(
        self,
        request: cloudsso_20210515_models.ListMFADevicesForUserRequest,
    ) -> cloudsso_20210515_models.ListMFADevicesForUserResponse:
        """
        This topic provides an example on how to query the MFA devices that are bound to the user `u-00q8wbq42wiltcrk***`. The returned result shows that the MFA device named `Alice-MFA1` is bound to the user.
        
        @param request: ListMFADevicesForUserRequest
        @return: ListMFADevicesForUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_mfadevices_for_user_with_options_async(request, runtime)

    def list_permission_policies_in_access_configuration_with_options(
        self,
        request: cloudsso_20210515_models.ListPermissionPoliciesInAccessConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.ListPermissionPoliciesInAccessConfigurationResponse:
        """
        This topic provides an example on how to query the policies that are created for the access configuration `ac-00jhtfl8thteu6uj***`. The returned result shows that the access configuration contains one system policy and one inline policy.
        
        @param request: ListPermissionPoliciesInAccessConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPermissionPoliciesInAccessConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.permission_policy_type):
            query['PermissionPolicyType'] = request.permission_policy_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPermissionPoliciesInAccessConfiguration',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to query the policies that are created for the access configuration `ac-00jhtfl8thteu6uj***`. The returned result shows that the access configuration contains one system policy and one inline policy.
        
        @param request: ListPermissionPoliciesInAccessConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPermissionPoliciesInAccessConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.permission_policy_type):
            query['PermissionPolicyType'] = request.permission_policy_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPermissionPoliciesInAccessConfiguration',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to query the policies that are created for the access configuration `ac-00jhtfl8thteu6uj***`. The returned result shows that the access configuration contains one system policy and one inline policy.
        
        @param request: ListPermissionPoliciesInAccessConfigurationRequest
        @return: ListPermissionPoliciesInAccessConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_permission_policies_in_access_configuration_with_options(request, runtime)

    async def list_permission_policies_in_access_configuration_async(
        self,
        request: cloudsso_20210515_models.ListPermissionPoliciesInAccessConfigurationRequest,
    ) -> cloudsso_20210515_models.ListPermissionPoliciesInAccessConfigurationResponse:
        """
        This topic provides an example on how to query the policies that are created for the access configuration `ac-00jhtfl8thteu6uj***`. The returned result shows that the access configuration contains one system policy and one inline policy.
        
        @param request: ListPermissionPoliciesInAccessConfigurationRequest
        @return: ListPermissionPoliciesInAccessConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_permission_policies_in_access_configuration_with_options_async(request, runtime)

    def list_scimserver_credentials_with_options(
        self,
        request: cloudsso_20210515_models.ListSCIMServerCredentialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.ListSCIMServerCredentialsResponse:
        """
        This topic provides an example on how to query the SCIM credentials within the `d-00fc2p61***` directory.
        
        @param request: ListSCIMServerCredentialsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSCIMServerCredentialsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSCIMServerCredentials',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to query the SCIM credentials within the `d-00fc2p61***` directory.
        
        @param request: ListSCIMServerCredentialsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSCIMServerCredentialsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSCIMServerCredentials',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to query the SCIM credentials within the `d-00fc2p61***` directory.
        
        @param request: ListSCIMServerCredentialsRequest
        @return: ListSCIMServerCredentialsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_scimserver_credentials_with_options(request, runtime)

    async def list_scimserver_credentials_async(
        self,
        request: cloudsso_20210515_models.ListSCIMServerCredentialsRequest,
    ) -> cloudsso_20210515_models.ListSCIMServerCredentialsResponse:
        """
        This topic provides an example on how to query the SCIM credentials within the `d-00fc2p61***` directory.
        
        @param request: ListSCIMServerCredentialsRequest
        @return: ListSCIMServerCredentialsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_scimserver_credentials_with_options_async(request, runtime)

    def list_tasks_with_options(
        self,
        request: cloudsso_20210515_models.ListTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.ListTasksResponse:
        """
        By default, this operation queries the tasks within the previous 24 hours. This operation allows you to query the tasks within a maximum of 7 days. You can specify the start time of the query by using `Filter`.
        This topic provides an example on how to query the tasks within the previous 24 hours.
        
        @param request: ListTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.principal_id):
            query['PrincipalId'] = request.principal_id
        if not UtilClient.is_unset(request.principal_type):
            query['PrincipalType'] = request.principal_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTasks',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        By default, this operation queries the tasks within the previous 24 hours. This operation allows you to query the tasks within a maximum of 7 days. You can specify the start time of the query by using `Filter`.
        This topic provides an example on how to query the tasks within the previous 24 hours.
        
        @param request: ListTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.principal_id):
            query['PrincipalId'] = request.principal_id
        if not UtilClient.is_unset(request.principal_type):
            query['PrincipalType'] = request.principal_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTasks',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        By default, this operation queries the tasks within the previous 24 hours. This operation allows you to query the tasks within a maximum of 7 days. You can specify the start time of the query by using `Filter`.
        This topic provides an example on how to query the tasks within the previous 24 hours.
        
        @param request: ListTasksRequest
        @return: ListTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tasks_with_options(request, runtime)

    async def list_tasks_async(
        self,
        request: cloudsso_20210515_models.ListTasksRequest,
    ) -> cloudsso_20210515_models.ListTasksResponse:
        """
        By default, this operation queries the tasks within the previous 24 hours. This operation allows you to query the tasks within a maximum of 7 days. You can specify the start time of the query by using `Filter`.
        This topic provides an example on how to query the tasks within the previous 24 hours.
        
        @param request: ListTasksRequest
        @return: ListTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tasks_with_options_async(request, runtime)

    def list_user_provisioning_events_with_options(
        self,
        request: cloudsso_20210515_models.ListUserProvisioningEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.ListUserProvisioningEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.user_provisioning_id):
            query['UserProvisioningId'] = request.user_provisioning_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserProvisioningEvents',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.ListUserProvisioningEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_provisioning_events_with_options_async(
        self,
        request: cloudsso_20210515_models.ListUserProvisioningEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.ListUserProvisioningEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.user_provisioning_id):
            query['UserProvisioningId'] = request.user_provisioning_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserProvisioningEvents',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.ListUserProvisioningEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_provisioning_events(
        self,
        request: cloudsso_20210515_models.ListUserProvisioningEventsRequest,
    ) -> cloudsso_20210515_models.ListUserProvisioningEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_user_provisioning_events_with_options(request, runtime)

    async def list_user_provisioning_events_async(
        self,
        request: cloudsso_20210515_models.ListUserProvisioningEventsRequest,
    ) -> cloudsso_20210515_models.ListUserProvisioningEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_user_provisioning_events_with_options_async(request, runtime)

    def list_user_provisionings_with_options(
        self,
        request: cloudsso_20210515_models.ListUserProvisioningsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.ListUserProvisioningsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.principal_id):
            query['PrincipalId'] = request.principal_id
        if not UtilClient.is_unset(request.principal_type):
            query['PrincipalType'] = request.principal_type
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserProvisionings',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.ListUserProvisioningsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_provisionings_with_options_async(
        self,
        request: cloudsso_20210515_models.ListUserProvisioningsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.ListUserProvisioningsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.principal_id):
            query['PrincipalId'] = request.principal_id
        if not UtilClient.is_unset(request.principal_type):
            query['PrincipalType'] = request.principal_type
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserProvisionings',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.ListUserProvisioningsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_provisionings(
        self,
        request: cloudsso_20210515_models.ListUserProvisioningsRequest,
    ) -> cloudsso_20210515_models.ListUserProvisioningsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_user_provisionings_with_options(request, runtime)

    async def list_user_provisionings_async(
        self,
        request: cloudsso_20210515_models.ListUserProvisioningsRequest,
    ) -> cloudsso_20210515_models.ListUserProvisioningsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_user_provisionings_with_options_async(request, runtime)

    def list_users_with_options(
        self,
        request: cloudsso_20210515_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.ListUsersResponse:
        """
        This topic provides an example on how to query users in the `d-00fc2p61***` directory. The returned result shows that the directory contains two users. The user `AliceLee` is synchronized from an external identity provider (IdP). The user `user1` is manually created within CloudSSO.
        
        @param request: ListUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.provision_type):
            query['ProvisionType'] = request.provision_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsers',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to query users in the `d-00fc2p61***` directory. The returned result shows that the directory contains two users. The user `AliceLee` is synchronized from an external identity provider (IdP). The user `user1` is manually created within CloudSSO.
        
        @param request: ListUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.provision_type):
            query['ProvisionType'] = request.provision_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsers',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to query users in the `d-00fc2p61***` directory. The returned result shows that the directory contains two users. The user `AliceLee` is synchronized from an external identity provider (IdP). The user `user1` is manually created within CloudSSO.
        
        @param request: ListUsersRequest
        @return: ListUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_users_with_options(request, runtime)

    async def list_users_async(
        self,
        request: cloudsso_20210515_models.ListUsersRequest,
    ) -> cloudsso_20210515_models.ListUsersResponse:
        """
        This topic provides an example on how to query users in the `d-00fc2p61***` directory. The returned result shows that the directory contains two users. The user `AliceLee` is synchronized from an external identity provider (IdP). The user `user1` is manually created within CloudSSO.
        
        @param request: ListUsersRequest
        @return: ListUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_users_with_options_async(request, runtime)

    def provision_access_configuration_with_options(
        self,
        request: cloudsso_20210515_models.ProvisionAccessConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.ProvisionAccessConfigurationResponse:
        """
        When you call this operation, an asynchronous task is automatically created. You can call the [GetTask](~~340670~~) operation to query the progress of the task based on the value of the `TaskId` response parameter.
        This topic provides an example on how to provision the access configuration `ac-00jhtfl8thteu6uj****` for the account `114240524784****` in your resource directory.
        
        @param request: ProvisionAccessConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ProvisionAccessConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ProvisionAccessConfiguration',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        When you call this operation, an asynchronous task is automatically created. You can call the [GetTask](~~340670~~) operation to query the progress of the task based on the value of the `TaskId` response parameter.
        This topic provides an example on how to provision the access configuration `ac-00jhtfl8thteu6uj****` for the account `114240524784****` in your resource directory.
        
        @param request: ProvisionAccessConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ProvisionAccessConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ProvisionAccessConfiguration',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        When you call this operation, an asynchronous task is automatically created. You can call the [GetTask](~~340670~~) operation to query the progress of the task based on the value of the `TaskId` response parameter.
        This topic provides an example on how to provision the access configuration `ac-00jhtfl8thteu6uj****` for the account `114240524784****` in your resource directory.
        
        @param request: ProvisionAccessConfigurationRequest
        @return: ProvisionAccessConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.provision_access_configuration_with_options(request, runtime)

    async def provision_access_configuration_async(
        self,
        request: cloudsso_20210515_models.ProvisionAccessConfigurationRequest,
    ) -> cloudsso_20210515_models.ProvisionAccessConfigurationResponse:
        """
        When you call this operation, an asynchronous task is automatically created. You can call the [GetTask](~~340670~~) operation to query the progress of the task based on the value of the `TaskId` response parameter.
        This topic provides an example on how to provision the access configuration `ac-00jhtfl8thteu6uj****` for the account `114240524784****` in your resource directory.
        
        @param request: ProvisionAccessConfigurationRequest
        @return: ProvisionAccessConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.provision_access_configuration_with_options_async(request, runtime)

    def remove_external_samlid_pcertificate_with_options(
        self,
        request: cloudsso_20210515_models.RemoveExternalSAMLIdPCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.RemoveExternalSAMLIdPCertificateResponse:
        """
        This topic provides an example on how to remove the SAML signing certificate whose ID is `idp-c-00dt9gnl7fmjaw9c***`.
        
        @param request: RemoveExternalSAMLIdPCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveExternalSAMLIdPCertificateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certificate_id):
            query['CertificateId'] = request.certificate_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveExternalSAMLIdPCertificate',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to remove the SAML signing certificate whose ID is `idp-c-00dt9gnl7fmjaw9c***`.
        
        @param request: RemoveExternalSAMLIdPCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveExternalSAMLIdPCertificateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certificate_id):
            query['CertificateId'] = request.certificate_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveExternalSAMLIdPCertificate',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to remove the SAML signing certificate whose ID is `idp-c-00dt9gnl7fmjaw9c***`.
        
        @param request: RemoveExternalSAMLIdPCertificateRequest
        @return: RemoveExternalSAMLIdPCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_external_samlid_pcertificate_with_options(request, runtime)

    async def remove_external_samlid_pcertificate_async(
        self,
        request: cloudsso_20210515_models.RemoveExternalSAMLIdPCertificateRequest,
    ) -> cloudsso_20210515_models.RemoveExternalSAMLIdPCertificateResponse:
        """
        This topic provides an example on how to remove the SAML signing certificate whose ID is `idp-c-00dt9gnl7fmjaw9c***`.
        
        @param request: RemoveExternalSAMLIdPCertificateRequest
        @return: RemoveExternalSAMLIdPCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_external_samlid_pcertificate_with_options_async(request, runtime)

    def remove_permission_policy_from_access_configuration_with_options(
        self,
        request: cloudsso_20210515_models.RemovePermissionPolicyFromAccessConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.RemovePermissionPolicyFromAccessConfigurationResponse:
        """
        After you remove an inline policy from an access configuration, the policy cannot be restored.
        This topic provides an example on how to remove the system policy `AliyunECSFullAccess` from the access configuration `ac-00jhtfl8thteu6uj****`.
        
        @param request: RemovePermissionPolicyFromAccessConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemovePermissionPolicyFromAccessConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.permission_policy_name):
            query['PermissionPolicyName'] = request.permission_policy_name
        if not UtilClient.is_unset(request.permission_policy_type):
            query['PermissionPolicyType'] = request.permission_policy_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemovePermissionPolicyFromAccessConfiguration',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        After you remove an inline policy from an access configuration, the policy cannot be restored.
        This topic provides an example on how to remove the system policy `AliyunECSFullAccess` from the access configuration `ac-00jhtfl8thteu6uj****`.
        
        @param request: RemovePermissionPolicyFromAccessConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemovePermissionPolicyFromAccessConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.permission_policy_name):
            query['PermissionPolicyName'] = request.permission_policy_name
        if not UtilClient.is_unset(request.permission_policy_type):
            query['PermissionPolicyType'] = request.permission_policy_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemovePermissionPolicyFromAccessConfiguration',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        After you remove an inline policy from an access configuration, the policy cannot be restored.
        This topic provides an example on how to remove the system policy `AliyunECSFullAccess` from the access configuration `ac-00jhtfl8thteu6uj****`.
        
        @param request: RemovePermissionPolicyFromAccessConfigurationRequest
        @return: RemovePermissionPolicyFromAccessConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_permission_policy_from_access_configuration_with_options(request, runtime)

    async def remove_permission_policy_from_access_configuration_async(
        self,
        request: cloudsso_20210515_models.RemovePermissionPolicyFromAccessConfigurationRequest,
    ) -> cloudsso_20210515_models.RemovePermissionPolicyFromAccessConfigurationResponse:
        """
        After you remove an inline policy from an access configuration, the policy cannot be restored.
        This topic provides an example on how to remove the system policy `AliyunECSFullAccess` from the access configuration `ac-00jhtfl8thteu6uj****`.
        
        @param request: RemovePermissionPolicyFromAccessConfigurationRequest
        @return: RemovePermissionPolicyFromAccessConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_permission_policy_from_access_configuration_with_options_async(request, runtime)

    def remove_user_from_group_with_options(
        self,
        request: cloudsso_20210515_models.RemoveUserFromGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.RemoveUserFromGroupResponse:
        """
        If System for Cross-domain Identity Management (SCIM) synchronization is enabled, you cannot remove a user from a group that is synchronized by using SCIM.
        This topic provides an example on how to remove the user `u-00q8wbq42wiltcrk****` from the group `g-00jqzghi2n3o5hkh****`.
        
        @param request: RemoveUserFromGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveUserFromGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveUserFromGroup',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        If System for Cross-domain Identity Management (SCIM) synchronization is enabled, you cannot remove a user from a group that is synchronized by using SCIM.
        This topic provides an example on how to remove the user `u-00q8wbq42wiltcrk****` from the group `g-00jqzghi2n3o5hkh****`.
        
        @param request: RemoveUserFromGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveUserFromGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveUserFromGroup',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        If System for Cross-domain Identity Management (SCIM) synchronization is enabled, you cannot remove a user from a group that is synchronized by using SCIM.
        This topic provides an example on how to remove the user `u-00q8wbq42wiltcrk****` from the group `g-00jqzghi2n3o5hkh****`.
        
        @param request: RemoveUserFromGroupRequest
        @return: RemoveUserFromGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_user_from_group_with_options(request, runtime)

    async def remove_user_from_group_async(
        self,
        request: cloudsso_20210515_models.RemoveUserFromGroupRequest,
    ) -> cloudsso_20210515_models.RemoveUserFromGroupResponse:
        """
        If System for Cross-domain Identity Management (SCIM) synchronization is enabled, you cannot remove a user from a group that is synchronized by using SCIM.
        This topic provides an example on how to remove the user `u-00q8wbq42wiltcrk****` from the group `g-00jqzghi2n3o5hkh****`.
        
        @param request: RemoveUserFromGroupRequest
        @return: RemoveUserFromGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_user_from_group_with_options_async(request, runtime)

    def reset_user_password_with_options(
        self,
        request: cloudsso_20210515_models.ResetUserPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.ResetUserPasswordResponse:
        """
        If you forget your password or your password expires or is at risk, you must contact a CloudSSO administrator to reset your password.
        >  After you enable SSO logon, your password cannot be reset.
        This topic provides an example on how to reset the password of the user `u-00q8wbq42wiltcrk****`. The new password is automatically generated by the system.
        
        @param request: ResetUserPasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetUserPasswordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.generate_random_password):
            query['GenerateRandomPassword'] = request.generate_random_password
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.require_password_reset_for_next_login):
            query['RequirePasswordResetForNextLogin'] = request.require_password_reset_for_next_login
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetUserPassword',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        If you forget your password or your password expires or is at risk, you must contact a CloudSSO administrator to reset your password.
        >  After you enable SSO logon, your password cannot be reset.
        This topic provides an example on how to reset the password of the user `u-00q8wbq42wiltcrk****`. The new password is automatically generated by the system.
        
        @param request: ResetUserPasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetUserPasswordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.generate_random_password):
            query['GenerateRandomPassword'] = request.generate_random_password
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.require_password_reset_for_next_login):
            query['RequirePasswordResetForNextLogin'] = request.require_password_reset_for_next_login
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetUserPassword',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        If you forget your password or your password expires or is at risk, you must contact a CloudSSO administrator to reset your password.
        >  After you enable SSO logon, your password cannot be reset.
        This topic provides an example on how to reset the password of the user `u-00q8wbq42wiltcrk****`. The new password is automatically generated by the system.
        
        @param request: ResetUserPasswordRequest
        @return: ResetUserPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reset_user_password_with_options(request, runtime)

    async def reset_user_password_async(
        self,
        request: cloudsso_20210515_models.ResetUserPasswordRequest,
    ) -> cloudsso_20210515_models.ResetUserPasswordResponse:
        """
        If you forget your password or your password expires or is at risk, you must contact a CloudSSO administrator to reset your password.
        >  After you enable SSO logon, your password cannot be reset.
        This topic provides an example on how to reset the password of the user `u-00q8wbq42wiltcrk****`. The new password is automatically generated by the system.
        
        @param request: ResetUserPasswordRequest
        @return: ResetUserPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reset_user_password_with_options_async(request, runtime)

    def retry_user_provisioning_event_with_options(
        self,
        request: cloudsso_20210515_models.RetryUserProvisioningEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.RetryUserProvisioningEventResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.duplication_strategy):
            query['DuplicationStrategy'] = request.duplication_strategy
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RetryUserProvisioningEvent',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.RetryUserProvisioningEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def retry_user_provisioning_event_with_options_async(
        self,
        request: cloudsso_20210515_models.RetryUserProvisioningEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.RetryUserProvisioningEventResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.duplication_strategy):
            query['DuplicationStrategy'] = request.duplication_strategy
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RetryUserProvisioningEvent',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.RetryUserProvisioningEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def retry_user_provisioning_event(
        self,
        request: cloudsso_20210515_models.RetryUserProvisioningEventRequest,
    ) -> cloudsso_20210515_models.RetryUserProvisioningEventResponse:
        runtime = util_models.RuntimeOptions()
        return self.retry_user_provisioning_event_with_options(request, runtime)

    async def retry_user_provisioning_event_async(
        self,
        request: cloudsso_20210515_models.RetryUserProvisioningEventRequest,
    ) -> cloudsso_20210515_models.RetryUserProvisioningEventResponse:
        runtime = util_models.RuntimeOptions()
        return await self.retry_user_provisioning_event_with_options_async(request, runtime)

    def set_external_samlidentity_provider_with_options(
        self,
        request: cloudsso_20210515_models.SetExternalSAMLIdentityProviderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.SetExternalSAMLIdentityProviderResponse:
        """
        During SAML 2.0-based single sign-on (SSO) logon, CloudSSO is an SP, and the identity management system of an enterprise is an IdP.
        You can use one of the following methods to configure a SAML IdP. You can obtain the required metadata file or parameter values from your IdP.
        *   Use the metadata file. You can specify the `EncodedMetadataDocument` parameter to upload the metadata file.
        *   Manually configure the IdP. You can manually specify the following parameters for your IdP: `EntityId`, `LoginUrl`, `WantRequestSigned`, and `X509Certificate`.
        If you have configured a SAML IdP, the existing configurations are replaced after you call this operation.
        *   If the IdP is configured by using the metadata file, all existing configurations are replaced with new configurations.
        *   If the IdP is manually configured, the original parameter values that are different from the new parameter values are replaced.
        >  If SSO logon is enabled, new configurations immediately take effect. Take note of the impacts on the production environment.
        This topic provides an example on how to configure an IdP by using the metadata file within the directory `d-00fc2p61****`.
        
        @param request: SetExternalSAMLIdentityProviderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetExternalSAMLIdentityProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.encoded_metadata_document):
            query['EncodedMetadataDocument'] = request.encoded_metadata_document
        if not UtilClient.is_unset(request.entity_id):
            query['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.login_url):
            query['LoginUrl'] = request.login_url
        if not UtilClient.is_unset(request.ssostatus):
            query['SSOStatus'] = request.ssostatus
        if not UtilClient.is_unset(request.want_request_signed):
            query['WantRequestSigned'] = request.want_request_signed
        if not UtilClient.is_unset(request.x_509certificate):
            query['X509Certificate'] = request.x_509certificate
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetExternalSAMLIdentityProvider',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        During SAML 2.0-based single sign-on (SSO) logon, CloudSSO is an SP, and the identity management system of an enterprise is an IdP.
        You can use one of the following methods to configure a SAML IdP. You can obtain the required metadata file or parameter values from your IdP.
        *   Use the metadata file. You can specify the `EncodedMetadataDocument` parameter to upload the metadata file.
        *   Manually configure the IdP. You can manually specify the following parameters for your IdP: `EntityId`, `LoginUrl`, `WantRequestSigned`, and `X509Certificate`.
        If you have configured a SAML IdP, the existing configurations are replaced after you call this operation.
        *   If the IdP is configured by using the metadata file, all existing configurations are replaced with new configurations.
        *   If the IdP is manually configured, the original parameter values that are different from the new parameter values are replaced.
        >  If SSO logon is enabled, new configurations immediately take effect. Take note of the impacts on the production environment.
        This topic provides an example on how to configure an IdP by using the metadata file within the directory `d-00fc2p61****`.
        
        @param request: SetExternalSAMLIdentityProviderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetExternalSAMLIdentityProviderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.encoded_metadata_document):
            query['EncodedMetadataDocument'] = request.encoded_metadata_document
        if not UtilClient.is_unset(request.entity_id):
            query['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.login_url):
            query['LoginUrl'] = request.login_url
        if not UtilClient.is_unset(request.ssostatus):
            query['SSOStatus'] = request.ssostatus
        if not UtilClient.is_unset(request.want_request_signed):
            query['WantRequestSigned'] = request.want_request_signed
        if not UtilClient.is_unset(request.x_509certificate):
            query['X509Certificate'] = request.x_509certificate
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetExternalSAMLIdentityProvider',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        During SAML 2.0-based single sign-on (SSO) logon, CloudSSO is an SP, and the identity management system of an enterprise is an IdP.
        You can use one of the following methods to configure a SAML IdP. You can obtain the required metadata file or parameter values from your IdP.
        *   Use the metadata file. You can specify the `EncodedMetadataDocument` parameter to upload the metadata file.
        *   Manually configure the IdP. You can manually specify the following parameters for your IdP: `EntityId`, `LoginUrl`, `WantRequestSigned`, and `X509Certificate`.
        If you have configured a SAML IdP, the existing configurations are replaced after you call this operation.
        *   If the IdP is configured by using the metadata file, all existing configurations are replaced with new configurations.
        *   If the IdP is manually configured, the original parameter values that are different from the new parameter values are replaced.
        >  If SSO logon is enabled, new configurations immediately take effect. Take note of the impacts on the production environment.
        This topic provides an example on how to configure an IdP by using the metadata file within the directory `d-00fc2p61****`.
        
        @param request: SetExternalSAMLIdentityProviderRequest
        @return: SetExternalSAMLIdentityProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_external_samlidentity_provider_with_options(request, runtime)

    async def set_external_samlidentity_provider_async(
        self,
        request: cloudsso_20210515_models.SetExternalSAMLIdentityProviderRequest,
    ) -> cloudsso_20210515_models.SetExternalSAMLIdentityProviderResponse:
        """
        During SAML 2.0-based single sign-on (SSO) logon, CloudSSO is an SP, and the identity management system of an enterprise is an IdP.
        You can use one of the following methods to configure a SAML IdP. You can obtain the required metadata file or parameter values from your IdP.
        *   Use the metadata file. You can specify the `EncodedMetadataDocument` parameter to upload the metadata file.
        *   Manually configure the IdP. You can manually specify the following parameters for your IdP: `EntityId`, `LoginUrl`, `WantRequestSigned`, and `X509Certificate`.
        If you have configured a SAML IdP, the existing configurations are replaced after you call this operation.
        *   If the IdP is configured by using the metadata file, all existing configurations are replaced with new configurations.
        *   If the IdP is manually configured, the original parameter values that are different from the new parameter values are replaced.
        >  If SSO logon is enabled, new configurations immediately take effect. Take note of the impacts on the production environment.
        This topic provides an example on how to configure an IdP by using the metadata file within the directory `d-00fc2p61****`.
        
        @param request: SetExternalSAMLIdentityProviderRequest
        @return: SetExternalSAMLIdentityProviderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_external_samlidentity_provider_with_options_async(request, runtime)

    def set_mfaauthentication_status_with_options(
        self,
        request: cloudsso_20210515_models.SetMFAAuthenticationStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.SetMFAAuthenticationStatusResponse:
        """
        If a CloudSSO administrator enables username-password logon for users, CloudSSO automatically enables MFA to improve security. The administrator can call this operation to enable or disable MFA based on the business requirements.
        This topic provides an example on how to enable MFA for users.
        
        @param request: SetMFAAuthenticationStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetMFAAuthenticationStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.mfaauthentication_status):
            query['MFAAuthenticationStatus'] = request.mfaauthentication_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetMFAAuthenticationStatus',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        If a CloudSSO administrator enables username-password logon for users, CloudSSO automatically enables MFA to improve security. The administrator can call this operation to enable or disable MFA based on the business requirements.
        This topic provides an example on how to enable MFA for users.
        
        @param request: SetMFAAuthenticationStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetMFAAuthenticationStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.mfaauthentication_status):
            query['MFAAuthenticationStatus'] = request.mfaauthentication_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetMFAAuthenticationStatus',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        If a CloudSSO administrator enables username-password logon for users, CloudSSO automatically enables MFA to improve security. The administrator can call this operation to enable or disable MFA based on the business requirements.
        This topic provides an example on how to enable MFA for users.
        
        @param request: SetMFAAuthenticationStatusRequest
        @return: SetMFAAuthenticationStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_mfaauthentication_status_with_options(request, runtime)

    async def set_mfaauthentication_status_async(
        self,
        request: cloudsso_20210515_models.SetMFAAuthenticationStatusRequest,
    ) -> cloudsso_20210515_models.SetMFAAuthenticationStatusResponse:
        """
        If a CloudSSO administrator enables username-password logon for users, CloudSSO automatically enables MFA to improve security. The administrator can call this operation to enable or disable MFA based on the business requirements.
        This topic provides an example on how to enable MFA for users.
        
        @param request: SetMFAAuthenticationStatusRequest
        @return: SetMFAAuthenticationStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_mfaauthentication_status_with_options_async(request, runtime)

    def set_scimsynchronization_status_with_options(
        self,
        request: cloudsso_20210515_models.SetSCIMSynchronizationStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.SetSCIMSynchronizationStatusResponse:
        """
        You can synchronize users or groups from an external identity provider (IdP) that supports SCIM 2.0 to CloudSSO only after SCIM synchronization is enabled. If you disable SCIM synchronization, you can no longer synchronize users or groups to CloudSSO. The following list describes the impacts after SCIM synchronization is enabled or disabled:
        *   After you enable SCIM synchronization, you cannot modify or delete the users or groups that are synchronized to CloudSSO by using SCIM. In addition, you cannot add users to or remove users from the groups. However, you can change the passwords of the users and enable or disable the logon of the users.
        *   After you disable SCIM synchronization, you can modify and delete the users and groups that are synchronized to CloudSSO by using SCIM. You can also add users to or remove users from the groups.
        This topic provides an example on how to enable SCIM synchronization within the directory `d-00fc2p61****`.
        
        @param request: SetSCIMSynchronizationStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetSCIMSynchronizationStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.scimsynchronization_status):
            query['SCIMSynchronizationStatus'] = request.scimsynchronization_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetSCIMSynchronizationStatus',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        You can synchronize users or groups from an external identity provider (IdP) that supports SCIM 2.0 to CloudSSO only after SCIM synchronization is enabled. If you disable SCIM synchronization, you can no longer synchronize users or groups to CloudSSO. The following list describes the impacts after SCIM synchronization is enabled or disabled:
        *   After you enable SCIM synchronization, you cannot modify or delete the users or groups that are synchronized to CloudSSO by using SCIM. In addition, you cannot add users to or remove users from the groups. However, you can change the passwords of the users and enable or disable the logon of the users.
        *   After you disable SCIM synchronization, you can modify and delete the users and groups that are synchronized to CloudSSO by using SCIM. You can also add users to or remove users from the groups.
        This topic provides an example on how to enable SCIM synchronization within the directory `d-00fc2p61****`.
        
        @param request: SetSCIMSynchronizationStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetSCIMSynchronizationStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.scimsynchronization_status):
            query['SCIMSynchronizationStatus'] = request.scimsynchronization_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetSCIMSynchronizationStatus',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        You can synchronize users or groups from an external identity provider (IdP) that supports SCIM 2.0 to CloudSSO only after SCIM synchronization is enabled. If you disable SCIM synchronization, you can no longer synchronize users or groups to CloudSSO. The following list describes the impacts after SCIM synchronization is enabled or disabled:
        *   After you enable SCIM synchronization, you cannot modify or delete the users or groups that are synchronized to CloudSSO by using SCIM. In addition, you cannot add users to or remove users from the groups. However, you can change the passwords of the users and enable or disable the logon of the users.
        *   After you disable SCIM synchronization, you can modify and delete the users and groups that are synchronized to CloudSSO by using SCIM. You can also add users to or remove users from the groups.
        This topic provides an example on how to enable SCIM synchronization within the directory `d-00fc2p61****`.
        
        @param request: SetSCIMSynchronizationStatusRequest
        @return: SetSCIMSynchronizationStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_scimsynchronization_status_with_options(request, runtime)

    async def set_scimsynchronization_status_async(
        self,
        request: cloudsso_20210515_models.SetSCIMSynchronizationStatusRequest,
    ) -> cloudsso_20210515_models.SetSCIMSynchronizationStatusResponse:
        """
        You can synchronize users or groups from an external identity provider (IdP) that supports SCIM 2.0 to CloudSSO only after SCIM synchronization is enabled. If you disable SCIM synchronization, you can no longer synchronize users or groups to CloudSSO. The following list describes the impacts after SCIM synchronization is enabled or disabled:
        *   After you enable SCIM synchronization, you cannot modify or delete the users or groups that are synchronized to CloudSSO by using SCIM. In addition, you cannot add users to or remove users from the groups. However, you can change the passwords of the users and enable or disable the logon of the users.
        *   After you disable SCIM synchronization, you can modify and delete the users and groups that are synchronized to CloudSSO by using SCIM. You can also add users to or remove users from the groups.
        This topic provides an example on how to enable SCIM synchronization within the directory `d-00fc2p61****`.
        
        @param request: SetSCIMSynchronizationStatusRequest
        @return: SetSCIMSynchronizationStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_scimsynchronization_status_with_options_async(request, runtime)

    def update_access_configuration_with_options(
        self,
        request: cloudsso_20210515_models.UpdateAccessConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.UpdateAccessConfigurationResponse:
        """
        You can modify the `Description`, `SessionDuration`, and `RelayState` parameters for an access configuration.
        This topic provides an example on how to change the initial web page in the access configuration `ac-00jhtfl8thteu6uj****` to `https://cloudsso.console.aliyun.com`.
        
        @param request: UpdateAccessConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAccessConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.new_description):
            query['NewDescription'] = request.new_description
        if not UtilClient.is_unset(request.new_relay_state):
            query['NewRelayState'] = request.new_relay_state
        if not UtilClient.is_unset(request.new_session_duration):
            query['NewSessionDuration'] = request.new_session_duration
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAccessConfiguration',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        You can modify the `Description`, `SessionDuration`, and `RelayState` parameters for an access configuration.
        This topic provides an example on how to change the initial web page in the access configuration `ac-00jhtfl8thteu6uj****` to `https://cloudsso.console.aliyun.com`.
        
        @param request: UpdateAccessConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAccessConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.new_description):
            query['NewDescription'] = request.new_description
        if not UtilClient.is_unset(request.new_relay_state):
            query['NewRelayState'] = request.new_relay_state
        if not UtilClient.is_unset(request.new_session_duration):
            query['NewSessionDuration'] = request.new_session_duration
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAccessConfiguration',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        You can modify the `Description`, `SessionDuration`, and `RelayState` parameters for an access configuration.
        This topic provides an example on how to change the initial web page in the access configuration `ac-00jhtfl8thteu6uj****` to `https://cloudsso.console.aliyun.com`.
        
        @param request: UpdateAccessConfigurationRequest
        @return: UpdateAccessConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_access_configuration_with_options(request, runtime)

    async def update_access_configuration_async(
        self,
        request: cloudsso_20210515_models.UpdateAccessConfigurationRequest,
    ) -> cloudsso_20210515_models.UpdateAccessConfigurationResponse:
        """
        You can modify the `Description`, `SessionDuration`, and `RelayState` parameters for an access configuration.
        This topic provides an example on how to change the initial web page in the access configuration `ac-00jhtfl8thteu6uj****` to `https://cloudsso.console.aliyun.com`.
        
        @param request: UpdateAccessConfigurationRequest
        @return: UpdateAccessConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_access_configuration_with_options_async(request, runtime)

    def update_directory_with_options(
        self,
        request: cloudsso_20210515_models.UpdateDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.UpdateDirectoryResponse:
        """
        After you change the name of a directory, the URL that is used to log on to the Cloud SSO user portal is changed. You must notify the Cloud SSO users of the correct URL.
        This topic provides an example on how to change the name of a directory to `new-example`.
        
        @param request: UpdateDirectoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDirectoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.new_directory_name):
            query['NewDirectoryName'] = request.new_directory_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDirectory',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        After you change the name of a directory, the URL that is used to log on to the Cloud SSO user portal is changed. You must notify the Cloud SSO users of the correct URL.
        This topic provides an example on how to change the name of a directory to `new-example`.
        
        @param request: UpdateDirectoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDirectoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.new_directory_name):
            query['NewDirectoryName'] = request.new_directory_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDirectory',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        After you change the name of a directory, the URL that is used to log on to the Cloud SSO user portal is changed. You must notify the Cloud SSO users of the correct URL.
        This topic provides an example on how to change the name of a directory to `new-example`.
        
        @param request: UpdateDirectoryRequest
        @return: UpdateDirectoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_directory_with_options(request, runtime)

    async def update_directory_async(
        self,
        request: cloudsso_20210515_models.UpdateDirectoryRequest,
    ) -> cloudsso_20210515_models.UpdateDirectoryResponse:
        """
        After you change the name of a directory, the URL that is used to log on to the Cloud SSO user portal is changed. You must notify the Cloud SSO users of the correct URL.
        This topic provides an example on how to change the name of a directory to `new-example`.
        
        @param request: UpdateDirectoryRequest
        @return: UpdateDirectoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_directory_with_options_async(request, runtime)

    def update_group_with_options(
        self,
        request: cloudsso_20210515_models.UpdateGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.UpdateGroupResponse:
        """
        You can modify `GroupName` and `Description` for a group.
        >  If System for Cross-domain Identity Management (SCIM) synchronization is enabled, you cannot modify the information about a group that is synchronized by using SCIM.
        This topic provides an example on how to change the name of the group `g-00jqzghi2n3o5hkh****` to `NewTestGroup`.
        
        @param request: UpdateGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.new_description):
            query['NewDescription'] = request.new_description
        if not UtilClient.is_unset(request.new_group_name):
            query['NewGroupName'] = request.new_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGroup',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        You can modify `GroupName` and `Description` for a group.
        >  If System for Cross-domain Identity Management (SCIM) synchronization is enabled, you cannot modify the information about a group that is synchronized by using SCIM.
        This topic provides an example on how to change the name of the group `g-00jqzghi2n3o5hkh****` to `NewTestGroup`.
        
        @param request: UpdateGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.new_description):
            query['NewDescription'] = request.new_description
        if not UtilClient.is_unset(request.new_group_name):
            query['NewGroupName'] = request.new_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGroup',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        You can modify `GroupName` and `Description` for a group.
        >  If System for Cross-domain Identity Management (SCIM) synchronization is enabled, you cannot modify the information about a group that is synchronized by using SCIM.
        This topic provides an example on how to change the name of the group `g-00jqzghi2n3o5hkh****` to `NewTestGroup`.
        
        @param request: UpdateGroupRequest
        @return: UpdateGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_group_with_options(request, runtime)

    async def update_group_async(
        self,
        request: cloudsso_20210515_models.UpdateGroupRequest,
    ) -> cloudsso_20210515_models.UpdateGroupResponse:
        """
        You can modify `GroupName` and `Description` for a group.
        >  If System for Cross-domain Identity Management (SCIM) synchronization is enabled, you cannot modify the information about a group that is synchronized by using SCIM.
        This topic provides an example on how to change the name of the group `g-00jqzghi2n3o5hkh****` to `NewTestGroup`.
        
        @param request: UpdateGroupRequest
        @return: UpdateGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_group_with_options_async(request, runtime)

    def update_inline_policy_for_access_configuration_with_options(
        self,
        request: cloudsso_20210515_models.UpdateInlinePolicyForAccessConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.UpdateInlinePolicyForAccessConfigurationResponse:
        """
        This topic provides an example on how to modify an inline policy that is created for the access configuration `ac-00jhtfl8thteu6uj***`.
        
        @param request: UpdateInlinePolicyForAccessConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInlinePolicyForAccessConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.inline_policy_name):
            query['InlinePolicyName'] = request.inline_policy_name
        if not UtilClient.is_unset(request.new_inline_policy_document):
            query['NewInlinePolicyDocument'] = request.new_inline_policy_document
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInlinePolicyForAccessConfiguration',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to modify an inline policy that is created for the access configuration `ac-00jhtfl8thteu6uj***`.
        
        @param request: UpdateInlinePolicyForAccessConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInlinePolicyForAccessConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_configuration_id):
            query['AccessConfigurationId'] = request.access_configuration_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.inline_policy_name):
            query['InlinePolicyName'] = request.inline_policy_name
        if not UtilClient.is_unset(request.new_inline_policy_document):
            query['NewInlinePolicyDocument'] = request.new_inline_policy_document
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInlinePolicyForAccessConfiguration',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to modify an inline policy that is created for the access configuration `ac-00jhtfl8thteu6uj***`.
        
        @param request: UpdateInlinePolicyForAccessConfigurationRequest
        @return: UpdateInlinePolicyForAccessConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_inline_policy_for_access_configuration_with_options(request, runtime)

    async def update_inline_policy_for_access_configuration_async(
        self,
        request: cloudsso_20210515_models.UpdateInlinePolicyForAccessConfigurationRequest,
    ) -> cloudsso_20210515_models.UpdateInlinePolicyForAccessConfigurationResponse:
        """
        This topic provides an example on how to modify an inline policy that is created for the access configuration `ac-00jhtfl8thteu6uj***`.
        
        @param request: UpdateInlinePolicyForAccessConfigurationRequest
        @return: UpdateInlinePolicyForAccessConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_inline_policy_for_access_configuration_with_options_async(request, runtime)

    def update_mfaauthentication_settings_with_options(
        self,
        request: cloudsso_20210515_models.UpdateMFAAuthenticationSettingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.UpdateMFAAuthenticationSettingsResponse:
        """
        If you enable username-password logon for CloudSSO users, you can also configure MFA for the users.
        This topic provides an example on how to enable MFA for all CloudSSO users that belong to the directory named `d-00fc2p61****`.
        
        @param request: UpdateMFAAuthenticationSettingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMFAAuthenticationSettingsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.mfaauthentication_settings):
            query['MFAAuthenticationSettings'] = request.mfaauthentication_settings
        if not UtilClient.is_unset(request.operation_for_risk_login):
            query['OperationForRiskLogin'] = request.operation_for_risk_login
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMFAAuthenticationSettings',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.UpdateMFAAuthenticationSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_mfaauthentication_settings_with_options_async(
        self,
        request: cloudsso_20210515_models.UpdateMFAAuthenticationSettingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.UpdateMFAAuthenticationSettingsResponse:
        """
        If you enable username-password logon for CloudSSO users, you can also configure MFA for the users.
        This topic provides an example on how to enable MFA for all CloudSSO users that belong to the directory named `d-00fc2p61****`.
        
        @param request: UpdateMFAAuthenticationSettingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMFAAuthenticationSettingsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.mfaauthentication_settings):
            query['MFAAuthenticationSettings'] = request.mfaauthentication_settings
        if not UtilClient.is_unset(request.operation_for_risk_login):
            query['OperationForRiskLogin'] = request.operation_for_risk_login
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMFAAuthenticationSettings',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.UpdateMFAAuthenticationSettingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_mfaauthentication_settings(
        self,
        request: cloudsso_20210515_models.UpdateMFAAuthenticationSettingsRequest,
    ) -> cloudsso_20210515_models.UpdateMFAAuthenticationSettingsResponse:
        """
        If you enable username-password logon for CloudSSO users, you can also configure MFA for the users.
        This topic provides an example on how to enable MFA for all CloudSSO users that belong to the directory named `d-00fc2p61****`.
        
        @param request: UpdateMFAAuthenticationSettingsRequest
        @return: UpdateMFAAuthenticationSettingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_mfaauthentication_settings_with_options(request, runtime)

    async def update_mfaauthentication_settings_async(
        self,
        request: cloudsso_20210515_models.UpdateMFAAuthenticationSettingsRequest,
    ) -> cloudsso_20210515_models.UpdateMFAAuthenticationSettingsResponse:
        """
        If you enable username-password logon for CloudSSO users, you can also configure MFA for the users.
        This topic provides an example on how to enable MFA for all CloudSSO users that belong to the directory named `d-00fc2p61****`.
        
        @param request: UpdateMFAAuthenticationSettingsRequest
        @return: UpdateMFAAuthenticationSettingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_mfaauthentication_settings_with_options_async(request, runtime)

    def update_scimserver_credential_status_with_options(
        self,
        request: cloudsso_20210515_models.UpdateSCIMServerCredentialStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.UpdateSCIMServerCredentialStatusResponse:
        """
        This topic provides an example on how to disable the SCIM credential whose ID is `scimcred-004whl0kvfwcypbi***`. After the SCIM credential is disabled, the synchronization task that uses the SCIM credential fails. You can call this operation again to enable the SCIM credential.
        
        @param request: UpdateSCIMServerCredentialStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSCIMServerCredentialStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.credential_id):
            query['CredentialId'] = request.credential_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.new_status):
            query['NewStatus'] = request.new_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSCIMServerCredentialStatus',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to disable the SCIM credential whose ID is `scimcred-004whl0kvfwcypbi***`. After the SCIM credential is disabled, the synchronization task that uses the SCIM credential fails. You can call this operation again to enable the SCIM credential.
        
        @param request: UpdateSCIMServerCredentialStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSCIMServerCredentialStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.credential_id):
            query['CredentialId'] = request.credential_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.new_status):
            query['NewStatus'] = request.new_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSCIMServerCredentialStatus',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to disable the SCIM credential whose ID is `scimcred-004whl0kvfwcypbi***`. After the SCIM credential is disabled, the synchronization task that uses the SCIM credential fails. You can call this operation again to enable the SCIM credential.
        
        @param request: UpdateSCIMServerCredentialStatusRequest
        @return: UpdateSCIMServerCredentialStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_scimserver_credential_status_with_options(request, runtime)

    async def update_scimserver_credential_status_async(
        self,
        request: cloudsso_20210515_models.UpdateSCIMServerCredentialStatusRequest,
    ) -> cloudsso_20210515_models.UpdateSCIMServerCredentialStatusResponse:
        """
        This topic provides an example on how to disable the SCIM credential whose ID is `scimcred-004whl0kvfwcypbi***`. After the SCIM credential is disabled, the synchronization task that uses the SCIM credential fails. You can call this operation again to enable the SCIM credential.
        
        @param request: UpdateSCIMServerCredentialStatusRequest
        @return: UpdateSCIMServerCredentialStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_scimserver_credential_status_with_options_async(request, runtime)

    def update_user_with_options(
        self,
        request: cloudsso_20210515_models.UpdateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.UpdateUserResponse:
        """
        You can modify `FirstName`, `LastName`, `DisplayName`, `Email`, and `Description` for a user. You cannot modify `UserName` for a user.
        >  If System for Cross-domain Identity Management (SCIM) synchronization is enabled, you cannot modify the information about a user that is synchronized by using SCIM.
        This topic provides an example on how to change the email address of the user whose ID is `u-00q8wbq42wiltcrk****` to `AliceLee@example.com`.
        
        @param request: UpdateUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.new_description):
            query['NewDescription'] = request.new_description
        if not UtilClient.is_unset(request.new_display_name):
            query['NewDisplayName'] = request.new_display_name
        if not UtilClient.is_unset(request.new_email):
            query['NewEmail'] = request.new_email
        if not UtilClient.is_unset(request.new_first_name):
            query['NewFirstName'] = request.new_first_name
        if not UtilClient.is_unset(request.new_last_name):
            query['NewLastName'] = request.new_last_name
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUser',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        You can modify `FirstName`, `LastName`, `DisplayName`, `Email`, and `Description` for a user. You cannot modify `UserName` for a user.
        >  If System for Cross-domain Identity Management (SCIM) synchronization is enabled, you cannot modify the information about a user that is synchronized by using SCIM.
        This topic provides an example on how to change the email address of the user whose ID is `u-00q8wbq42wiltcrk****` to `AliceLee@example.com`.
        
        @param request: UpdateUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.new_description):
            query['NewDescription'] = request.new_description
        if not UtilClient.is_unset(request.new_display_name):
            query['NewDisplayName'] = request.new_display_name
        if not UtilClient.is_unset(request.new_email):
            query['NewEmail'] = request.new_email
        if not UtilClient.is_unset(request.new_first_name):
            query['NewFirstName'] = request.new_first_name
        if not UtilClient.is_unset(request.new_last_name):
            query['NewLastName'] = request.new_last_name
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUser',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        You can modify `FirstName`, `LastName`, `DisplayName`, `Email`, and `Description` for a user. You cannot modify `UserName` for a user.
        >  If System for Cross-domain Identity Management (SCIM) synchronization is enabled, you cannot modify the information about a user that is synchronized by using SCIM.
        This topic provides an example on how to change the email address of the user whose ID is `u-00q8wbq42wiltcrk****` to `AliceLee@example.com`.
        
        @param request: UpdateUserRequest
        @return: UpdateUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_user_with_options(request, runtime)

    async def update_user_async(
        self,
        request: cloudsso_20210515_models.UpdateUserRequest,
    ) -> cloudsso_20210515_models.UpdateUserResponse:
        """
        You can modify `FirstName`, `LastName`, `DisplayName`, `Email`, and `Description` for a user. You cannot modify `UserName` for a user.
        >  If System for Cross-domain Identity Management (SCIM) synchronization is enabled, you cannot modify the information about a user that is synchronized by using SCIM.
        This topic provides an example on how to change the email address of the user whose ID is `u-00q8wbq42wiltcrk****` to `AliceLee@example.com`.
        
        @param request: UpdateUserRequest
        @return: UpdateUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_user_with_options_async(request, runtime)

    def update_user_mfaauthentication_settings_with_options(
        self,
        request: cloudsso_20210515_models.UpdateUserMFAAuthenticationSettingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.UpdateUserMFAAuthenticationSettingsResponse:
        """
        If you call the [UpdateMFAAuthenticationSettings](~~450134~~) operation to set the MFAAuthenticationSettings parameter to `Byuser`, user-specific settings are applied. Then, you must call the UpdateUserMFAAuthenticationSettings operation to configure MFA for each user.
        By default, the MFAAuthenticationSettings parameter is set to `Enabled` for a new user.
        This topic provides an example on how to enable MFA for the user named `u-00q8wbq42wiltcrk****`.
        
        @param request: UpdateUserMFAAuthenticationSettingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUserMFAAuthenticationSettingsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_mfaauthentication_settings):
            query['UserMFAAuthenticationSettings'] = request.user_mfaauthentication_settings
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUserMFAAuthenticationSettings',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.UpdateUserMFAAuthenticationSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_mfaauthentication_settings_with_options_async(
        self,
        request: cloudsso_20210515_models.UpdateUserMFAAuthenticationSettingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.UpdateUserMFAAuthenticationSettingsResponse:
        """
        If you call the [UpdateMFAAuthenticationSettings](~~450134~~) operation to set the MFAAuthenticationSettings parameter to `Byuser`, user-specific settings are applied. Then, you must call the UpdateUserMFAAuthenticationSettings operation to configure MFA for each user.
        By default, the MFAAuthenticationSettings parameter is set to `Enabled` for a new user.
        This topic provides an example on how to enable MFA for the user named `u-00q8wbq42wiltcrk****`.
        
        @param request: UpdateUserMFAAuthenticationSettingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUserMFAAuthenticationSettingsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_mfaauthentication_settings):
            query['UserMFAAuthenticationSettings'] = request.user_mfaauthentication_settings
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUserMFAAuthenticationSettings',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.UpdateUserMFAAuthenticationSettingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user_mfaauthentication_settings(
        self,
        request: cloudsso_20210515_models.UpdateUserMFAAuthenticationSettingsRequest,
    ) -> cloudsso_20210515_models.UpdateUserMFAAuthenticationSettingsResponse:
        """
        If you call the [UpdateMFAAuthenticationSettings](~~450134~~) operation to set the MFAAuthenticationSettings parameter to `Byuser`, user-specific settings are applied. Then, you must call the UpdateUserMFAAuthenticationSettings operation to configure MFA for each user.
        By default, the MFAAuthenticationSettings parameter is set to `Enabled` for a new user.
        This topic provides an example on how to enable MFA for the user named `u-00q8wbq42wiltcrk****`.
        
        @param request: UpdateUserMFAAuthenticationSettingsRequest
        @return: UpdateUserMFAAuthenticationSettingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_user_mfaauthentication_settings_with_options(request, runtime)

    async def update_user_mfaauthentication_settings_async(
        self,
        request: cloudsso_20210515_models.UpdateUserMFAAuthenticationSettingsRequest,
    ) -> cloudsso_20210515_models.UpdateUserMFAAuthenticationSettingsResponse:
        """
        If you call the [UpdateMFAAuthenticationSettings](~~450134~~) operation to set the MFAAuthenticationSettings parameter to `Byuser`, user-specific settings are applied. Then, you must call the UpdateUserMFAAuthenticationSettings operation to configure MFA for each user.
        By default, the MFAAuthenticationSettings parameter is set to `Enabled` for a new user.
        This topic provides an example on how to enable MFA for the user named `u-00q8wbq42wiltcrk****`.
        
        @param request: UpdateUserMFAAuthenticationSettingsRequest
        @return: UpdateUserMFAAuthenticationSettingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_user_mfaauthentication_settings_with_options_async(request, runtime)

    def update_user_provisioning_with_options(
        self,
        request: cloudsso_20210515_models.UpdateUserProvisioningRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.UpdateUserProvisioningResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.new_deletion_strategy):
            query['NewDeletionStrategy'] = request.new_deletion_strategy
        if not UtilClient.is_unset(request.new_description):
            query['NewDescription'] = request.new_description
        if not UtilClient.is_unset(request.new_duplication_strategy):
            query['NewDuplicationStrategy'] = request.new_duplication_strategy
        if not UtilClient.is_unset(request.user_provisioning_id):
            query['UserProvisioningId'] = request.user_provisioning_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUserProvisioning',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.UpdateUserProvisioningResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_provisioning_with_options_async(
        self,
        request: cloudsso_20210515_models.UpdateUserProvisioningRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.UpdateUserProvisioningResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.new_deletion_strategy):
            query['NewDeletionStrategy'] = request.new_deletion_strategy
        if not UtilClient.is_unset(request.new_description):
            query['NewDescription'] = request.new_description
        if not UtilClient.is_unset(request.new_duplication_strategy):
            query['NewDuplicationStrategy'] = request.new_duplication_strategy
        if not UtilClient.is_unset(request.user_provisioning_id):
            query['UserProvisioningId'] = request.user_provisioning_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUserProvisioning',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.UpdateUserProvisioningResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user_provisioning(
        self,
        request: cloudsso_20210515_models.UpdateUserProvisioningRequest,
    ) -> cloudsso_20210515_models.UpdateUserProvisioningResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_user_provisioning_with_options(request, runtime)

    async def update_user_provisioning_async(
        self,
        request: cloudsso_20210515_models.UpdateUserProvisioningRequest,
    ) -> cloudsso_20210515_models.UpdateUserProvisioningResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_user_provisioning_with_options_async(request, runtime)

    def update_user_provisioning_configuration_with_options(
        self,
        request: cloudsso_20210515_models.UpdateUserProvisioningConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.UpdateUserProvisioningConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.new_default_landing_page):
            query['NewDefaultLandingPage'] = request.new_default_landing_page
        if not UtilClient.is_unset(request.new_session_duration):
            query['NewSessionDuration'] = request.new_session_duration
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUserProvisioningConfiguration',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.UpdateUserProvisioningConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_provisioning_configuration_with_options_async(
        self,
        request: cloudsso_20210515_models.UpdateUserProvisioningConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.UpdateUserProvisioningConfigurationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.new_default_landing_page):
            query['NewDefaultLandingPage'] = request.new_default_landing_page
        if not UtilClient.is_unset(request.new_session_duration):
            query['NewSessionDuration'] = request.new_session_duration
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUserProvisioningConfiguration',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudsso_20210515_models.UpdateUserProvisioningConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user_provisioning_configuration(
        self,
        request: cloudsso_20210515_models.UpdateUserProvisioningConfigurationRequest,
    ) -> cloudsso_20210515_models.UpdateUserProvisioningConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_user_provisioning_configuration_with_options(request, runtime)

    async def update_user_provisioning_configuration_async(
        self,
        request: cloudsso_20210515_models.UpdateUserProvisioningConfigurationRequest,
    ) -> cloudsso_20210515_models.UpdateUserProvisioningConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_user_provisioning_configuration_with_options_async(request, runtime)

    def update_user_status_with_options(
        self,
        request: cloudsso_20210515_models.UpdateUserStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cloudsso_20210515_models.UpdateUserStatusResponse:
        """
        This topic provides an example on how to change the status of the user whose ID is `u-00q8wbq42wiltcrk***` to Disabled. Users in the Disabled state cannot log on to the CloudSSO user portal.
        
        @param request: UpdateUserStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUserStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.new_status):
            query['NewStatus'] = request.new_status
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUserStatus',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to change the status of the user whose ID is `u-00q8wbq42wiltcrk***` to Disabled. Users in the Disabled state cannot log on to the CloudSSO user portal.
        
        @param request: UpdateUserStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUserStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.new_status):
            query['NewStatus'] = request.new_status
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUserStatus',
            version='2021-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        This topic provides an example on how to change the status of the user whose ID is `u-00q8wbq42wiltcrk***` to Disabled. Users in the Disabled state cannot log on to the CloudSSO user portal.
        
        @param request: UpdateUserStatusRequest
        @return: UpdateUserStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_user_status_with_options(request, runtime)

    async def update_user_status_async(
        self,
        request: cloudsso_20210515_models.UpdateUserStatusRequest,
    ) -> cloudsso_20210515_models.UpdateUserStatusResponse:
        """
        This topic provides an example on how to change the status of the user whose ID is `u-00q8wbq42wiltcrk***` to Disabled. Users in the Disabled state cannot log on to the CloudSSO user portal.
        
        @param request: UpdateUserStatusRequest
        @return: UpdateUserStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_user_status_with_options_async(request, runtime)
