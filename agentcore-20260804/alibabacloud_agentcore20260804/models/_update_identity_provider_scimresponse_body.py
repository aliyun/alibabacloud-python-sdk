# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class UpdateIdentityProviderSCIMResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.UpdateIdentityProviderSCIMResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # If the call fails, troubleshoot the issue based on the HTTP status code and the message.
        self.code = code
        # The original fields and the meaning of the status field are retained. The new scimStatus field corresponds to the data.status field in the query operation. The operationStatus field retains the status of the most recent SCIM task.
        self.data = data
        # The processing status of the current request. This status is not equivalent to the final result of the background task.
        self.http_status_code = http_status_code
        # The message about request acceptance or errors. For an asynchronous task, verify the result by calling the corresponding query operation.
        self.message = message
        # The request ID. You can use this ID to associate the call with troubleshooting. Retain this ID if the call fails.
        self.request_id = request_id
        # Indicates whether the current request was processed successfully. A value of true indicates success. For asynchronous writes, you must continue to query the task result.
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
            temp_model = main_models.UpdateIdentityProviderSCIMResponseBodyData()
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

class UpdateIdentityProviderSCIMResponseBodyData(DaraModel):
    def __init__(
        self,
        configuration: main_models.UpdateIdentityProviderSCIMResponseBodyDataConfiguration = None,
        created_at: str = None,
        event_subscription_callback_url: str = None,
        identity_provider_type: str = None,
        login_callback_url: str = None,
        login_enabled: bool = None,
        metadata: main_models.UpdateIdentityProviderSCIMResponseBodyDataMetadata = None,
        operation_status: str = None,
        protocol: str = None,
        saml: main_models.UpdateIdentityProviderSCIMResponseBodyDataSaml = None,
        scim_status: str = None,
        status: str = None,
        sync_enabled: bool = None,
        updated_at: str = None,
        workspace_id: str = None,
    ):
        # The actual SAML configuration is read back on demand only by GetIdentityProvider. The SCIM query and preparation operations return the actual receiving status and URL.
        self.configuration = configuration
        # The creation time recorded on the server.
        self.created_at = created_at
        # For CustomSSO, an empty string is returned. You must obtain the SCIM receiving URL by calling the SCIM query or preparation operation. The example shows an empty JSON string. The actual value does not contain double quotation marks.
        self.event_subscription_callback_url = event_subscription_callback_url
        # The type of the identity provider. General CRUD operations support DingTalk, Feishu, and CustomSSO. Service provider (SP) queries support only CustomSSO. The SCIM path uses the CustomSSO shared pool.
        self.identity_provider_type = identity_provider_type
        # For CustomSSO, an empty string is returned. You must obtain the Assertion Consumer Service (ACS) URL for SAML by calling the SP query operation. The example shows an empty JSON string. The actual value does not contain double quotation marks.
        self.login_callback_url = login_callback_url
        # Specifies whether logon is enabled. Do not set this parameter to true during CustomSSO initialization. You must save a valid SAML configuration before enabling logon. Disabling logon does not delete the configuration. If an asynchronous task fails, this expected value does not indicate that the change has taken effect on the upstream side.
        self.login_enabled = login_enabled
        # Vendor parameters are used for DingTalk and Feishu. CustomSSO updates use the protocol and saml fields and do not accept this field. The return value does not contain vendor keys.
        self.metadata = metadata
        # The original status of the most recent independent SCIM operation task. An empty string ("") is returned if no historical tasks exist.
        self.operation_status = operation_status
        # Only SAML is supported. This field may not be returned if no valid configuration is saved. Initialization with an OIDC placeholder is not supported.
        self.protocol = protocol
        # You can specify either XML or manual fields for the input. The query returns a standardized configuration and does not return the original XML. This field can be omitted if it is not configured.
        self.saml = saml
        # The independent SCIM status. This field does not change the meaning of shared resources and logon configurations in the original status field. This field corresponds to the data.status field in the query operation.
        self.scim_status = scim_status
        # The lifecycle of the CustomSSO user pool and the task status of the logon configuration. This field does not indicate the SCIM operation result. You can query the SCIM switch result by checking the operationStatus field returned by GetIdentityProviderSCIM. You cannot use this field to determine whether all protocols are configured.
        self.status = status
        # Specifies whether to enable SCIM synchronization. Do not set this parameter to true during CustomSSO initialization. You can update this parameter only by calling UpdateIdentityProviderSCIM. Check the operationStatus field to determine the result.
        self.sync_enabled = sync_enabled
        # The most recent update time recorded on the server.
        self.updated_at = updated_at
        # Required. The ID of the destination workspace. The region of the request must be the same as the region of the destination workspace.
        self.workspace_id = workspace_id

    def validate(self):
        if self.configuration:
            self.configuration.validate()
        if self.metadata:
            self.metadata.validate()
        if self.saml:
            self.saml.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.configuration is not None:
            result['configuration'] = self.configuration.to_map()

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.event_subscription_callback_url is not None:
            result['eventSubscriptionCallbackUrl'] = self.event_subscription_callback_url

        if self.identity_provider_type is not None:
            result['identityProviderType'] = self.identity_provider_type

        if self.login_callback_url is not None:
            result['loginCallbackUrl'] = self.login_callback_url

        if self.login_enabled is not None:
            result['loginEnabled'] = self.login_enabled

        if self.metadata is not None:
            result['metadata'] = self.metadata.to_map()

        if self.operation_status is not None:
            result['operationStatus'] = self.operation_status

        if self.protocol is not None:
            result['protocol'] = self.protocol

        if self.saml is not None:
            result['saml'] = self.saml.to_map()

        if self.scim_status is not None:
            result['scimStatus'] = self.scim_status

        if self.status is not None:
            result['status'] = self.status

        if self.sync_enabled is not None:
            result['syncEnabled'] = self.sync_enabled

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configuration') is not None:
            temp_model = main_models.UpdateIdentityProviderSCIMResponseBodyDataConfiguration()
            self.configuration = temp_model.from_map(m.get('configuration'))

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('eventSubscriptionCallbackUrl') is not None:
            self.event_subscription_callback_url = m.get('eventSubscriptionCallbackUrl')

        if m.get('identityProviderType') is not None:
            self.identity_provider_type = m.get('identityProviderType')

        if m.get('loginCallbackUrl') is not None:
            self.login_callback_url = m.get('loginCallbackUrl')

        if m.get('loginEnabled') is not None:
            self.login_enabled = m.get('loginEnabled')

        if m.get('metadata') is not None:
            temp_model = main_models.UpdateIdentityProviderSCIMResponseBodyDataMetadata()
            self.metadata = temp_model.from_map(m.get('metadata'))

        if m.get('operationStatus') is not None:
            self.operation_status = m.get('operationStatus')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        if m.get('saml') is not None:
            temp_model = main_models.UpdateIdentityProviderSCIMResponseBodyDataSaml()
            self.saml = temp_model.from_map(m.get('saml'))

        if m.get('scimStatus') is not None:
            self.scim_status = m.get('scimStatus')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('syncEnabled') is not None:
            self.sync_enabled = m.get('syncEnabled')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

class UpdateIdentityProviderSCIMResponseBodyDataSaml(DaraModel):
    def __init__(
        self,
        binding_type: str = None,
        entity_id: str = None,
        login_url: str = None,
        x_509certificates: List[str] = None,
    ):
        # The SAML binding type. Valid values: HTTP-Redirect and HTTP-POST. Required when manually specified. The query returns the short name.
        self.binding_type = binding_type
        # Required when manually specified. The value must be non-empty and up to 2,048 characters in length. You cannot change this value after it is configured. This value is different from the local entity ID queried by the SP.
        self.entity_id = entity_id
        # Required when manually specified. The value must be an absolute HTTPS URL and must not contain user credentials or fragments.
        self.login_url = login_url
        # Required when manually specified. The value must be a non-empty array of PEM X.509 certificate texts. The system verifies the current validity period. A maximum of two certificates are allowed after deduplication.
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

class UpdateIdentityProviderSCIMResponseBodyDataMetadata(DaraModel):
    def __init__(
        self,
        binding: str = None,
        certificates: str = None,
        entity_id: str = None,
        login_url: str = None,
    ):
        # The SAML binding URI in the historical metadata snapshot. For CustomSSO updates, use the saml.bindingType field.
        self.binding = binding
        # The certificate string in the historical metadata snapshot. To edit the configuration, use the saml.x509Certificates field and do not submit the old metadata.
        self.certificates = certificates
        # Required when manually specified. The value must be non-empty and up to 2,048 characters in length. You cannot change this value after it is configured. This value is different from the local entity ID queried by the SP.
        self.entity_id = entity_id
        # Required when manually specified. The value must be an absolute HTTPS URL and must not contain user credentials or fragments.
        self.login_url = login_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.binding is not None:
            result['binding'] = self.binding

        if self.certificates is not None:
            result['certificates'] = self.certificates

        if self.entity_id is not None:
            result['entityId'] = self.entity_id

        if self.login_url is not None:
            result['loginUrl'] = self.login_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('binding') is not None:
            self.binding = m.get('binding')

        if m.get('certificates') is not None:
            self.certificates = m.get('certificates')

        if m.get('entityId') is not None:
            self.entity_id = m.get('entityId')

        if m.get('loginUrl') is not None:
            self.login_url = m.get('loginUrl')

        return self

class UpdateIdentityProviderSCIMResponseBodyDataConfiguration(DaraModel):
    def __init__(
        self,
        binding_type: str = None,
        entity_id: str = None,
        login_url: str = None,
        sso_status: str = None,
    ):
        # The SAML binding type. Valid values: HTTP-Redirect and HTTP-POST. Required when manually specified. The query returns the short name.
        self.binding_type = binding_type
        # Required when manually specified. The value must be non-empty and up to 2,048 characters in length. You cannot change this value after it is configured. This value is different from the local entity ID queried by the SP.
        self.entity_id = entity_id
        # Required when manually specified. The value must be an absolute HTTPS URL and must not contain user credentials or fragments.
        self.login_url = login_url
        # The actual switch value, which is Enabled or Disabled. This value is not equivalent to the expected value of loginEnabled saved by AgentCore.
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

