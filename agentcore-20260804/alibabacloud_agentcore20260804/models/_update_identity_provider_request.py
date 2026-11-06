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
        # Submit business parameters as described in this operation. The body parameters of public APIs are mapped to backend wrappers by the gateway. Do not mix them with direct backend body wrappers.
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
        # Do not set this parameter to true during CustomSSO initialization. A valid SAML configuration must be saved before you enable logon. Disabling logon does not delete the configuration. If an asynchronous failure occurs, this expected value does not mean that the change has taken effect upstream.
        self.login_enabled = login_enabled
        # The vendor configurations for DingTalk and Feishu support partial updates. Omitted fields retain their saved values. Submitted values cannot be null, empty strings, or blank strings. The complete configuration is verified after merging. CustomSSO updates use protocol and saml, and do not accept this field. The response does not contain vendor keys.
        self.metadata = metadata
        # The logon protocol for CustomSSO. Currently, only SAML is supported. You can pass SAML when saving the SAML configuration. You can omit this parameter if you only modify loginEnabled. DingTalk and Feishu do not accept this field.
        self.protocol = protocol
        # The SAML configuration for CustomSSO. Choose between metadataXml and the four manually entered fields: entityId, loginUrl, bindingType, and x509Certificates. If not submitted, the existing configuration is retained. DingTalk and Feishu do not accept this field.
        self.saml = saml
        # Specifies whether to enable incremental synchronization for subsequent directory change events of DingTalk or Feishu. If not passed, the original value is retained. It does not control the initial synchronization or manual synchronization. CustomSSO does not accept this field. You must use UpdateIdentityProviderSCIM.
        self.sync_enabled = sync_enabled
        # Uses the definition of the department-based synchronization scope. If omitted during creation, the default value is AllAuthorized. The initial vendor synchronization is determined by syncOnBind. If omitted or set to null during an update, the original value is retained. Updating and saving the scope does not automatically execute a full synchronization.
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
        # When the mode is SelectedDepartments, it must contain at least one non-empty department ID, which should be obtained from ListIdentityProviderDepartments. When the mode is AllAuthorized, pass an empty array or omit this parameter.
        self.department_ids = department_ids
        # AllAuthorized: the full authorization scope, which is subject to the application directory authorization limits. SelectedDepartments: the selected departments and all their sub-departments. When explicitly submitting syncScope, you must provide a valid mode, which is verified by the backend.
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
        # HTTP-Redirect or HTTP-POST. Required for manual entry. The query returns the short name.
        self.binding_type = binding_type
        # Required for manual entry. It must be non-empty and contain a maximum of 2,048 characters. The existing configuration does not support replacement. It is different from our Entity ID returned by the SP query.
        self.entity_id = entity_id
        # Required for manual entry. It must be an absolute HTTPS URL and cannot contain user credentials or fragments.
        self.login_url = login_url
        # The input is the XML text of a single IdP EntityDescriptor, with a maximum size of 1 MiB. It cannot be a URL or file path. It is mutually exclusive with the four manually entered fields. DTDs and external entities are prohibited. If both SSO bindings are declared at the same time, HTTP-POST takes precedence.
        self.metadata_xml = metadata_xml
        # Required for manual entry. It must be a non-empty array and use PEM X.509 certificate text. The current validity period is verified. A maximum of two certificates are allowed after deduplication.
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
        # The App ID of the Feishu application. You can omit this parameter during an update to retain the saved value. The merged Feishu configuration of the old and new values must include this parameter.
        self.app_id = app_id
        # The AppKey of the DingTalk application. You can omit this parameter during an update to retain the saved value. The merged DingTalk configuration of the old and new values must include this parameter.
        self.app_key = app_key
        # The secret of the vendor application. If you omit this parameter during an update, the saved value is retained. You can submit only this field to update the secret. An explicit value cannot be empty. This is a sensitive input and is not echoed in the response.
        self.app_secret = app_secret
        # The CorpId of the DingTalk enterprise. You can omit this parameter during an update to retain the saved value. The merged DingTalk configuration of the old and new values must include this parameter.
        self.corp_id = corp_id
        # Required when you enable synchronization for DingTalk or Feishu. This is a sensitive input and is unrelated to the SCIM token.
        self.encrypt_key = encrypt_key
        # Required when you enable synchronization for DingTalk or Feishu. This is a sensitive input and is unrelated to the SCIM token.
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

