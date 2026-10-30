# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class UpdateIdentityProviderResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.UpdateIdentityProviderResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business status code for this API request. A value of SUCCESS indicates that the request succeeded, but does not indicate that the asynchronous configuration or synchronization task is complete.
        self.code = code
        # The currently saved identity provider binding information, including the expected configuration and resource status. The actual update may still be executing in the background.
        self.data = data
        # The HTTP status code for this API request. This does not indicate the execution result of the background task.
        self.http_status_code = http_status_code
        # The response message for this API request. An error description is returned if the request fails.
        self.message = message
        # The unique identifier for this request. Provide this value when you troubleshoot issues.
        self.request_id = request_id
        # Indicates whether this API request succeeded. To check whether the background configuration has taken effect, you must query the identity provider status separately.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.UpdateIdentityProviderResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class UpdateIdentityProviderResponseBodyData(DaraModel):
    def __init__(
        self,
        configuration: main_models.UpdateIdentityProviderResponseBodyDataConfiguration = None,
        identity_provider_type: str = None,
        login_enabled: bool = None,
        protocol: str = None,
        saml: main_models.UpdateIdentityProviderResponseBodyDataSaml = None,
        status: str = None,
        sync_enabled: bool = None,
        sync_scope: main_models.UpdateIdentityProviderResponseBodyDataSyncScope = None,
        workspace_id: str = None,
    ):
        # The actual SAML configuration read back from the upstream. This update API does not perform this read-back and usually does not return this field. Use GetIdentityProvider to obtain it.
        self.configuration = configuration
        # The type of the identity provider. DingTalk indicates DingTalk. Feishu indicates Feishu. CustomSSO indicates a custom enterprise identity provider connected through SAML. The value must be the same as the type of the identity provider bound to the current workspace.
        self.identity_provider_type = identity_provider_type
        # The currently saved expected value for the logon switch. This alone does not prove that the upstream logon configuration has taken effect.
        self.login_enabled = login_enabled
        # The currently saved logon protocol for CustomSSO. The value is SAML when configured. This field is not returned for DingTalk or Lark.
        self.protocol = protocol
        # The saved standardized SAML configuration for CustomSSO. The original metadata XML is not echoed. This field is not returned if no valid configuration is saved or if the identity provider is DingTalk or Lark. This value is the locally saved configuration and is not equivalent to the actual upstream configuration.
        self.saml = saml
        # The status of the identity provider resource and logon configuration. Valid values:
        # - CONFIGURED: The configuration is accepted.
        # - UPDATING: The configuration is being updated.
        # - SYNCING: Synchronization is in progress.
        # - SYNCED: The synchronization phase is complete.
        # - READY: The resource is ready.
        # - SYNC_FAILED: Synchronization failed.
        # - UPDATE_FAILED: The update failed.
        # - DISCONNECTING: Unbinding is in progress.
        # - DISCONNECT_FAILED: Unbinding failed.
        # A value of READY does not alone indicate that users are imported. Query the SCIM operation results for CustomSSO separately.
        self.status = status
        # The currently saved expected value for the synchronization switch. For DingTalk and Lark, this is used for subsequent address book change events. For CustomSSO, the SCIM switch is managed by using UpdateIdentityProviderSCIM, and the operation results are queried by using GetIdentityProviderSCIM.
        self.sync_enabled = sync_enabled
        # The saved synchronization scope for DingTalk and Lark. The default value for valid historical configurations is AllAuthorized. This field may not be returned for corrupted historical configurations. This field is not returned for CustomSSO.
        self.sync_scope = sync_scope
        # The ID of the workspace to which the identity provider belongs.
        self.workspace_id = workspace_id

    def validate(self):
        if self.configuration:
            self.configuration.validate()
        if self.saml:
            self.saml.validate()
        if self.sync_scope:
            self.sync_scope.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.configuration is not None:
            result['configuration'] = self.configuration.to_map()

        if self.identity_provider_type is not None:
            result['identityProviderType'] = self.identity_provider_type

        if self.login_enabled is not None:
            result['loginEnabled'] = self.login_enabled

        if self.protocol is not None:
            result['protocol'] = self.protocol

        if self.saml is not None:
            result['saml'] = self.saml.to_map()

        if self.status is not None:
            result['status'] = self.status

        if self.sync_enabled is not None:
            result['syncEnabled'] = self.sync_enabled

        if self.sync_scope is not None:
            result['syncScope'] = self.sync_scope.to_map()

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configuration') is not None:
            temp_model = main_models.UpdateIdentityProviderResponseBodyDataConfiguration()
            self.configuration = temp_model.from_map(m.get('configuration'))

        if m.get('identityProviderType') is not None:
            self.identity_provider_type = m.get('identityProviderType')

        if m.get('loginEnabled') is not None:
            self.login_enabled = m.get('loginEnabled')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        if m.get('saml') is not None:
            temp_model = main_models.UpdateIdentityProviderResponseBodyDataSaml()
            self.saml = temp_model.from_map(m.get('saml'))

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('syncEnabled') is not None:
            self.sync_enabled = m.get('syncEnabled')

        if m.get('syncScope') is not None:
            temp_model = main_models.UpdateIdentityProviderResponseBodyDataSyncScope()
            self.sync_scope = temp_model.from_map(m.get('syncScope'))

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

class UpdateIdentityProviderResponseBodyDataSyncScope(DaraModel):
    def __init__(
        self,
        department_ids: List[str] = None,
        mode: str = None,
    ):
        # The list of department IDs in the synchronization scope, which are obtained from ListIdentityProviderDepartments. In SelectedDepartments mode, you must provide at least one non-empty department ID. In AllAuthorized mode, this field should be omitted or an empty array should be passed.
        self.department_ids = department_ids
        # The synchronization scope mode. Valid values: AllAuthorized and SelectedDepartments. AllAuthorized indicates all members within the authorization scope of the application address book. SelectedDepartments indicates the selected departments and all their sub-departments. When explicitly submitting syncScope, you must provide a valid mode.
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

class UpdateIdentityProviderResponseBodyDataSaml(DaraModel):
    def __init__(
        self,
        binding_type: str = None,
        entity_id: str = None,
        login_url: str = None,
        x_509certificates: List[str] = None,
    ):
        # The saved SAML binding type, which is HTTP-Redirect or HTTP-POST.
        self.binding_type = binding_type
        # The saved enterprise IdP entity ID, which is different from the entity ID of the service provider (SP).
        self.entity_id = entity_id
        # The saved enterprise IdP SSO logon URL.
        self.login_url = login_url
        # The list of saved enterprise IdP X.509 signing certificates.
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

        if m.get('x509Certificates') is not None:
            self.x_509certificates = m.get('x509Certificates')

        return self

class UpdateIdentityProviderResponseBodyDataConfiguration(DaraModel):
    def __init__(
        self,
        binding_type: str = None,
        entity_id: str = None,
        login_url: str = None,
        sso_status: str = None,
    ):
        # The actual SAML binding type saved upstream, which is HTTP-Redirect or HTTP-POST.
        self.binding_type = binding_type
        # The actual enterprise IdP entity ID saved upstream.
        self.entity_id = entity_id
        # The actual enterprise IdP SSO logon URL saved upstream.
        self.login_url = login_url
        # The actual SSO logon status upstream. Enabled indicates that it is turned on, and Disabled indicates that it is turned off. This should be evaluated separately from the expected value of loginEnabled.
        self.sso_status = sso_status

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

        if self.sso_status is not None:
            result['ssoStatus'] = self.sso_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bindingType') is not None:
            self.binding_type = m.get('bindingType')

        if m.get('entityId') is not None:
            self.entity_id = m.get('entityId')

        if m.get('loginUrl') is not None:
            self.login_url = m.get('loginUrl')

        if m.get('ssoStatus') is not None:
            self.sso_status = m.get('ssoStatus')

        return self

