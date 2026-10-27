# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class UpdateIdentityProviderRequest(DaraModel):
    def __init__(
        self,
        body: main_models.UpdateIdentityProviderRequestBody = None,
    ):
        # The configuration fields to be modified. For DingTalk and Lark, you must submit at least one of loginEnabled, syncEnabled, metadata, and syncScope. For CustomSSO, use protocol, saml, and loginEnabled. You cannot submit vendor metadata, syncEnabled, or syncScope.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = main_models.UpdateIdentityProviderRequestBody()
            self.body = temp_model.from_map(m.get('body'))

        return self

class UpdateIdentityProviderRequestBody(DaraModel):
    def __init__(
        self,
        login_enabled: bool = None,
        metadata: main_models.UpdateIdentityProviderRequestBodyMetadata = None,
        protocol: str = None,
        saml: main_models.UpdateIdentityProviderRequestBodySaml = None,
        sync_enabled: bool = None,
        sync_scope: main_models.UpdateIdentityProviderRequestBodySyncScope = None,
    ):
        # Specifies whether to allow logon by using this identity provider. If this parameter is omitted or set to null during an update, the original value is retained. For CustomSSO, a valid SAML configuration must exist before logon is enabled. Disabling logon does not delete the saved SAML or SCIM configurations.
        self.login_enabled = login_enabled
        # Applies only to DingTalk and Lark. The application configuration is merged by field. Omitted fields and existing keys retain their original values. Explicitly submitted fields must not be null, empty strings, or blank strings. The merged configuration must meet the complete configuration requirements of the vendor. CustomSSO does not accept this field.
        self.metadata = metadata
        # The logon protocol, which applies only to CustomSSO. Currently, only SAML is supported. DingTalk and Lark do not accept this field. If submitted with a non-empty saml configuration, this field can be omitted and the server processes it as SAML.
        self.protocol = protocol
        # Applies only to CustomSSO. You can either provide metadataXml or provide the four complete manual configuration fields. The two methods cannot be mixed. If a valid configuration already exists, you can also modify only the JIT switches. Saving the configuration does not automatically enable logon.
        self.saml = saml
        # Applies only to DingTalk and Lark. Controls the incremental synchronization of subsequent address book change events. If this parameter is omitted or set to null during an update, the original value is retained. It does not control the initial synchronization or manual synchronization. When enabled, the merged metadata must include encryptKey and verificationToken. For CustomSSO, use UpdateIdentityProviderSCIM to manage the synchronization switch.
        self.sync_enabled = sync_enabled
        # The address book synchronization scope, which applies only to DingTalk and Lark. If this parameter is omitted or set to null, the current scope is retained. Saving the scope does not automatically trigger a full synchronization. CustomSSO does not accept this field.
        self.sync_scope = sync_scope

    def validate(self):
        if self.metadata:
            self.metadata.validate()
        if self.saml:
            self.saml.validate()
        if self.sync_scope:
            self.sync_scope.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.login_enabled is not None:
            result['loginEnabled'] = self.login_enabled

        if self.metadata is not None:
            result['metadata'] = self.metadata.to_map()

        if self.protocol is not None:
            result['protocol'] = self.protocol

        if self.saml is not None:
            result['saml'] = self.saml.to_map()

        if self.sync_enabled is not None:
            result['syncEnabled'] = self.sync_enabled

        if self.sync_scope is not None:
            result['syncScope'] = self.sync_scope.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('loginEnabled') is not None:
            self.login_enabled = m.get('loginEnabled')

        if m.get('metadata') is not None:
            temp_model = main_models.UpdateIdentityProviderRequestBodyMetadata()
            self.metadata = temp_model.from_map(m.get('metadata'))

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        if m.get('saml') is not None:
            temp_model = main_models.UpdateIdentityProviderRequestBodySaml()
            self.saml = temp_model.from_map(m.get('saml'))

        if m.get('syncEnabled') is not None:
            self.sync_enabled = m.get('syncEnabled')

        if m.get('syncScope') is not None:
            temp_model = main_models.UpdateIdentityProviderRequestBodySyncScope()
            self.sync_scope = temp_model.from_map(m.get('syncScope'))

        return self

class UpdateIdentityProviderRequestBodySyncScope(DaraModel):
    def __init__(
        self,
        department_ids: List[str] = None,
        mode: str = None,
    ):
        # The list of department IDs in the synchronization scope, obtained from ListIdentityProviderDepartments. In SelectedDepartments mode, at least one non-empty department ID must be provided. In AllAuthorized mode, this parameter should be omitted or an empty array should be passed.
        self.department_ids = department_ids
        # The synchronization scope mode. AllAuthorized: all members within the authorization scope of the application address book. SelectedDepartments: the selected departments and all their sub-departments. A valid mode must be provided when syncScope is explicitly submitted.
        self.mode = mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.department_ids is not None:
            result['departmentIds'] = self.department_ids

        if self.mode is not None:
            result['mode'] = self.mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('departmentIds') is not None:
            self.department_ids = m.get('departmentIds')

        if m.get('mode') is not None:
            self.mode = m.get('mode')

        return self

class UpdateIdentityProviderRequestBodySaml(DaraModel):
    def __init__(
        self,
        binding_type: str = None,
        entity_id: str = None,
        login_url: str = None,
        metadata_xml: str = None,
        x_509certificates: List[str] = None,
    ):
        # The binding type for manual SAML configuration. HTTP-Redirect and HTTP-POST are supported. This parameter must be submitted together with entityId, loginUrl, and x509Certificates, and cannot be mixed with metadataXml.
        self.binding_type = binding_type
        # The entity ID of the enterprise IdP. This parameter is required for manual configuration. It must be non-empty and up to 2,048 characters, and cannot be changed after saving. It must be submitted together with loginUrl, bindingType, and x509Certificates, and cannot be mixed with metadataXml.
        self.entity_id = entity_id
        # The SSO logon URL of the enterprise IdP. This parameter is required for manual configuration. It must be an absolute HTTPS URL without user credentials and fragments. It must be submitted together with entityId, bindingType, and x509Certificates, and cannot be mixed with metadataXml.
        self.login_url = login_url
        # The original SAML metadata XML text of the enterprise IdP, not a URL or file path. The maximum size is 1 MiB. It must contain a single EntityDescriptor. DTDs and external entities are prohibited. It cannot be mixed with the four manual configuration fields. After saving, queries return the standardized configuration and do not echo the original XML text.
        self.metadata_xml = metadata_xml
        # The list of X.509 signing certificates for the enterprise IdP. For manual configuration, a non-empty list must be provided, with a maximum of 10 certificates. The certificates must be valid. This parameter must be submitted together with entityId, loginUrl, and bindingType, and cannot be mixed with metadataXml.
        self.x_509certificates = x_509certificates

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.binding_type is not None:
            result['bindingType'] = self.binding_type

        if self.entity_id is not None:
            result['entityId'] = self.entity_id

        if self.login_url is not None:
            result['loginUrl'] = self.login_url

        if self.metadata_xml is not None:
            result['metadataXml'] = self.metadata_xml

        if self.x_509certificates is not None:
            result['x509Certificates'] = self.x_509certificates

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bindingType') is not None:
            self.binding_type = m.get('bindingType')

        if m.get('entityId') is not None:
            self.entity_id = m.get('entityId')

        if m.get('loginUrl') is not None:
            self.login_url = m.get('loginUrl')

        if m.get('metadataXml') is not None:
            self.metadata_xml = m.get('metadataXml')

        if m.get('x509Certificates') is not None:
            self.x_509certificates = m.get('x509Certificates')

        return self

class UpdateIdentityProviderRequestBodyMetadata(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_key: str = None,
        app_secret: str = None,
        corp_id: str = None,
        encrypt_key: str = None,
        verification_token: str = None,
    ):
        # The App ID of the Lark application. If this parameter is omitted during an update, the existing value is retained. If explicitly submitted, it must be a non-empty value. The merged configuration for Lark must include this field.
        self.app_id = app_id
        # The AppKey of the DingTalk application. If this parameter is omitted during an update, the existing value is retained. If explicitly submitted, it must be a non-empty value. The merged configuration for DingTalk must include this field.
        self.app_key = app_key
        # The AppSecret of the DingTalk or Lark application. If this parameter is omitted during an update, the existing secret is retained and does not need to be retransmitted each time. If explicitly submitted, it must be a non-empty value, and the merged configuration must include this field. This is sensitive input and is not echoed in queries. The example is a fictitious value.
        self.app_secret = app_secret
        # The CorpId of the organization to which the DingTalk application belongs. If this parameter is omitted during an update, the existing value is retained. If explicitly submitted, it must be a non-empty value and must match the organization to which the application belongs. The merged configuration for DingTalk must include this field.
        self.corp_id = corp_id
        # The encryption key for vendor event callbacks, which must be consistent with the vendor application configuration. If this parameter is omitted during an update, the existing value is retained. When incremental synchronization is enabled, the merged configuration must include this field. This is sensitive input and is not echoed in queries.
        self.encrypt_key = encrypt_key
        # The verification token for vendor event callbacks, which must be consistent with the vendor application configuration. If this parameter is omitted during an update, the existing value is retained. When incremental synchronization is enabled, the merged configuration must include this field. This is sensitive input and is not echoed in queries.
        self.verification_token = verification_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['appId'] = self.app_id

        if self.app_key is not None:
            result['appKey'] = self.app_key

        if self.app_secret is not None:
            result['appSecret'] = self.app_secret

        if self.corp_id is not None:
            result['corpId'] = self.corp_id

        if self.encrypt_key is not None:
            result['encryptKey'] = self.encrypt_key

        if self.verification_token is not None:
            result['verificationToken'] = self.verification_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')

        if m.get('appKey') is not None:
            self.app_key = m.get('appKey')

        if m.get('appSecret') is not None:
            self.app_secret = m.get('appSecret')

        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')

        if m.get('encryptKey') is not None:
            self.encrypt_key = m.get('encryptKey')

        if m.get('verificationToken') is not None:
            self.verification_token = m.get('verificationToken')

        return self

