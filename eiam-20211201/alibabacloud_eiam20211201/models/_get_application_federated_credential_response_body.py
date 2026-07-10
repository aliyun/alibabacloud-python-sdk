# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class GetApplicationFederatedCredentialResponseBody(DaraModel):
    def __init__(
        self,
        application_federated_credential: main_models.GetApplicationFederatedCredentialResponseBodyApplicationFederatedCredential = None,
        request_id: str = None,
    ):
        # The application federated credential object.
        self.application_federated_credential = application_federated_credential
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.application_federated_credential:
            self.application_federated_credential.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_federated_credential is not None:
            result['ApplicationFederatedCredential'] = self.application_federated_credential.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationFederatedCredential') is not None:
            temp_model = main_models.GetApplicationFederatedCredentialResponseBodyApplicationFederatedCredential()
            self.application_federated_credential = temp_model.from_map(m.get('ApplicationFederatedCredential'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetApplicationFederatedCredentialResponseBodyApplicationFederatedCredential(DaraModel):
    def __init__(
        self,
        application_federated_credential_id: str = None,
        application_federated_credential_name: str = None,
        application_federated_credential_type: str = None,
        application_id: str = None,
        attribute_mappings: List[main_models.GetApplicationFederatedCredentialResponseBodyApplicationFederatedCredentialAttributeMappings] = None,
        create_time: int = None,
        description: str = None,
        federated_credential_provider_id: str = None,
        instance_id: str = None,
        last_used_time: int = None,
        oidc_verification_config: main_models.GetApplicationFederatedCredentialResponseBodyApplicationFederatedCredentialOidcVerificationConfig = None,
        pkcs_7verification_config: main_models.GetApplicationFederatedCredentialResponseBodyApplicationFederatedCredentialPkcs7VerificationConfig = None,
        status: str = None,
        update_time: int = None,
        verification_condition: str = None,
        verification_mode: str = None,
    ):
        # The application federated credential ID.
        self.application_federated_credential_id = application_federated_credential_id
        # The application federated credential name.
        self.application_federated_credential_name = application_federated_credential_name
        # The application federated credential type.
        self.application_federated_credential_type = application_federated_credential_type
        # The application ID.
        self.application_id = application_id
        # The attribute mappings.
        self.attribute_mappings = attribute_mappings
        # The time when the credential was created.
        self.create_time = create_time
        # The application federated credential description.
        self.description = description
        # The federated trust source ID.
        self.federated_credential_provider_id = federated_credential_provider_id
        # The instance ID.
        self.instance_id = instance_id
        # The time when the credential was last used.
        self.last_used_time = last_used_time
        # The OIDC structured configuration. This parameter applies when the verification mode is structured and the credential type is oidc.
        self.oidc_verification_config = oidc_verification_config
        # The PKCS#7 structured configuration. This parameter applies when the verification mode is structured and the credential type is pkcs7.
        self.pkcs_7verification_config = pkcs_7verification_config
        # The application federated credential status.
        self.status = status
        # The time when the credential was last updated.
        self.update_time = update_time
        # The verification condition.
        self.verification_condition = verification_condition
        # The verification mode. Valid values: freedom and structured.
        self.verification_mode = verification_mode

    def validate(self):
        if self.attribute_mappings:
            for v1 in self.attribute_mappings:
                 if v1:
                    v1.validate()
        if self.oidc_verification_config:
            self.oidc_verification_config.validate()
        if self.pkcs_7verification_config:
            self.pkcs_7verification_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_federated_credential_id is not None:
            result['ApplicationFederatedCredentialId'] = self.application_federated_credential_id

        if self.application_federated_credential_name is not None:
            result['ApplicationFederatedCredentialName'] = self.application_federated_credential_name

        if self.application_federated_credential_type is not None:
            result['ApplicationFederatedCredentialType'] = self.application_federated_credential_type

        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        result['AttributeMappings'] = []
        if self.attribute_mappings is not None:
            for k1 in self.attribute_mappings:
                result['AttributeMappings'].append(k1.to_map() if k1 else None)

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.federated_credential_provider_id is not None:
            result['FederatedCredentialProviderId'] = self.federated_credential_provider_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.last_used_time is not None:
            result['LastUsedTime'] = self.last_used_time

        if self.oidc_verification_config is not None:
            result['OidcVerificationConfig'] = self.oidc_verification_config.to_map()

        if self.pkcs_7verification_config is not None:
            result['Pkcs7VerificationConfig'] = self.pkcs_7verification_config.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.verification_condition is not None:
            result['VerificationCondition'] = self.verification_condition

        if self.verification_mode is not None:
            result['VerificationMode'] = self.verification_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationFederatedCredentialId') is not None:
            self.application_federated_credential_id = m.get('ApplicationFederatedCredentialId')

        if m.get('ApplicationFederatedCredentialName') is not None:
            self.application_federated_credential_name = m.get('ApplicationFederatedCredentialName')

        if m.get('ApplicationFederatedCredentialType') is not None:
            self.application_federated_credential_type = m.get('ApplicationFederatedCredentialType')

        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        self.attribute_mappings = []
        if m.get('AttributeMappings') is not None:
            for k1 in m.get('AttributeMappings'):
                temp_model = main_models.GetApplicationFederatedCredentialResponseBodyApplicationFederatedCredentialAttributeMappings()
                self.attribute_mappings.append(temp_model.from_map(k1))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FederatedCredentialProviderId') is not None:
            self.federated_credential_provider_id = m.get('FederatedCredentialProviderId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LastUsedTime') is not None:
            self.last_used_time = m.get('LastUsedTime')

        if m.get('OidcVerificationConfig') is not None:
            temp_model = main_models.GetApplicationFederatedCredentialResponseBodyApplicationFederatedCredentialOidcVerificationConfig()
            self.oidc_verification_config = temp_model.from_map(m.get('OidcVerificationConfig'))

        if m.get('Pkcs7VerificationConfig') is not None:
            temp_model = main_models.GetApplicationFederatedCredentialResponseBodyApplicationFederatedCredentialPkcs7VerificationConfig()
            self.pkcs_7verification_config = temp_model.from_map(m.get('Pkcs7VerificationConfig'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('VerificationCondition') is not None:
            self.verification_condition = m.get('VerificationCondition')

        if m.get('VerificationMode') is not None:
            self.verification_mode = m.get('VerificationMode')

        return self

class GetApplicationFederatedCredentialResponseBodyApplicationFederatedCredentialPkcs7VerificationConfig(DaraModel):
    def __init__(
        self,
        instance_ids: List[str] = None,
    ):
        # The list of allowed instance IDs. A maximum of 10 instance IDs are supported.
        self.instance_ids = instance_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        return self

class GetApplicationFederatedCredentialResponseBodyApplicationFederatedCredentialOidcVerificationConfig(DaraModel):
    def __init__(
        self,
        azure_vm_config: main_models.GetApplicationFederatedCredentialResponseBodyApplicationFederatedCredentialOidcVerificationConfigAzureVmConfig = None,
        gcp_vm_config: main_models.GetApplicationFederatedCredentialResponseBodyApplicationFederatedCredentialOidcVerificationConfigGcpVmConfig = None,
        generic_config: main_models.GetApplicationFederatedCredentialResponseBodyApplicationFederatedCredentialOidcVerificationConfigGenericConfig = None,
        kubernetes_config: main_models.GetApplicationFederatedCredentialResponseBodyApplicationFederatedCredentialOidcVerificationConfigKubernetesConfig = None,
        profile: str = None,
    ):
        # The Azure VM scenario configuration.
        self.azure_vm_config = azure_vm_config
        # The GCP VM scenario configuration.
        self.gcp_vm_config = gcp_vm_config
        self.generic_config = generic_config
        # The Kubernetes scenario configuration.
        self.kubernetes_config = kubernetes_config
        # The OIDC scenario profile. Valid values: generic, kubernetes, gcp_vm, and azure_vm.
        self.profile = profile

    def validate(self):
        if self.azure_vm_config:
            self.azure_vm_config.validate()
        if self.gcp_vm_config:
            self.gcp_vm_config.validate()
        if self.generic_config:
            self.generic_config.validate()
        if self.kubernetes_config:
            self.kubernetes_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.azure_vm_config is not None:
            result['AzureVmConfig'] = self.azure_vm_config.to_map()

        if self.gcp_vm_config is not None:
            result['GcpVmConfig'] = self.gcp_vm_config.to_map()

        if self.generic_config is not None:
            result['GenericConfig'] = self.generic_config.to_map()

        if self.kubernetes_config is not None:
            result['KubernetesConfig'] = self.kubernetes_config.to_map()

        if self.profile is not None:
            result['Profile'] = self.profile

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AzureVmConfig') is not None:
            temp_model = main_models.GetApplicationFederatedCredentialResponseBodyApplicationFederatedCredentialOidcVerificationConfigAzureVmConfig()
            self.azure_vm_config = temp_model.from_map(m.get('AzureVmConfig'))

        if m.get('GcpVmConfig') is not None:
            temp_model = main_models.GetApplicationFederatedCredentialResponseBodyApplicationFederatedCredentialOidcVerificationConfigGcpVmConfig()
            self.gcp_vm_config = temp_model.from_map(m.get('GcpVmConfig'))

        if m.get('GenericConfig') is not None:
            temp_model = main_models.GetApplicationFederatedCredentialResponseBodyApplicationFederatedCredentialOidcVerificationConfigGenericConfig()
            self.generic_config = temp_model.from_map(m.get('GenericConfig'))

        if m.get('KubernetesConfig') is not None:
            temp_model = main_models.GetApplicationFederatedCredentialResponseBodyApplicationFederatedCredentialOidcVerificationConfigKubernetesConfig()
            self.kubernetes_config = temp_model.from_map(m.get('KubernetesConfig'))

        if m.get('Profile') is not None:
            self.profile = m.get('Profile')

        return self

class GetApplicationFederatedCredentialResponseBodyApplicationFederatedCredentialOidcVerificationConfigKubernetesConfig(DaraModel):
    def __init__(
        self,
        namespace: str = None,
        pod_name_prefix: str = None,
        service_account_name: str = None,
    ):
        # The Kubernetes namespace.
        self.namespace = namespace
        # The pod name prefix.
        self.pod_name_prefix = pod_name_prefix
        # The Kubernetes service account name.
        self.service_account_name = service_account_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.pod_name_prefix is not None:
            result['PodNamePrefix'] = self.pod_name_prefix

        if self.service_account_name is not None:
            result['ServiceAccountName'] = self.service_account_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('PodNamePrefix') is not None:
            self.pod_name_prefix = m.get('PodNamePrefix')

        if m.get('ServiceAccountName') is not None:
            self.service_account_name = m.get('ServiceAccountName')

        return self

class GetApplicationFederatedCredentialResponseBodyApplicationFederatedCredentialOidcVerificationConfigGenericConfig(DaraModel):
    def __init__(
        self,
        subject: str = None,
    ):
        self.subject = subject

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.subject is not None:
            result['Subject'] = self.subject

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Subject') is not None:
            self.subject = m.get('Subject')

        return self

class GetApplicationFederatedCredentialResponseBodyApplicationFederatedCredentialOidcVerificationConfigGcpVmConfig(DaraModel):
    def __init__(
        self,
        instance_ids: List[str] = None,
        project_id: str = None,
        service_account_id: str = None,
    ):
        # The list of VM instance IDs. A maximum of 10 instance IDs are supported.
        self.instance_ids = instance_ids
        self.project_id = project_id
        # The service account ID that corresponds to the sub claim.
        self.service_account_id = service_account_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.service_account_id is not None:
            result['ServiceAccountId'] = self.service_account_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ServiceAccountId') is not None:
            self.service_account_id = m.get('ServiceAccountId')

        return self

class GetApplicationFederatedCredentialResponseBodyApplicationFederatedCredentialOidcVerificationConfigAzureVmConfig(DaraModel):
    def __init__(
        self,
        principal_id: str = None,
        resource_group_name: str = None,
        subscription_id: str = None,
        vm_names: List[str] = None,
    ):
        self.principal_id = principal_id
        self.resource_group_name = resource_group_name
        self.subscription_id = subscription_id
        self.vm_names = vm_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.principal_id is not None:
            result['PrincipalId'] = self.principal_id

        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name

        if self.subscription_id is not None:
            result['SubscriptionId'] = self.subscription_id

        if self.vm_names is not None:
            result['VmNames'] = self.vm_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrincipalId') is not None:
            self.principal_id = m.get('PrincipalId')

        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')

        if m.get('SubscriptionId') is not None:
            self.subscription_id = m.get('SubscriptionId')

        if m.get('VmNames') is not None:
            self.vm_names = m.get('VmNames')

        return self

class GetApplicationFederatedCredentialResponseBodyApplicationFederatedCredentialAttributeMappings(DaraModel):
    def __init__(
        self,
        source_value_expression: str = None,
        target_field: str = None,
    ):
        # The source value expression.
        self.source_value_expression = source_value_expression
        # The target field.
        self.target_field = target_field

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source_value_expression is not None:
            result['SourceValueExpression'] = self.source_value_expression

        if self.target_field is not None:
            result['TargetField'] = self.target_field

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceValueExpression') is not None:
            self.source_value_expression = m.get('SourceValueExpression')

        if m.get('TargetField') is not None:
            self.target_field = m.get('TargetField')

        return self

