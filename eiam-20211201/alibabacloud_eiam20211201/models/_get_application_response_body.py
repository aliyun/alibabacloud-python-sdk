# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class GetApplicationResponseBody(DaraModel):
    def __init__(
        self,
        application: main_models.GetApplicationResponseBodyApplication = None,
        request_id: str = None,
    ):
        # The information about the application.
        self.application = application
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.application:
            self.application.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application is not None:
            result['Application'] = self.application.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Application') is not None:
            temp_model = main_models.GetApplicationResponseBodyApplication()
            self.application = temp_model.from_map(m.get('Application'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetApplicationResponseBodyApplication(DaraModel):
    def __init__(
        self,
        api_invoke_status: str = None,
        application_creation_type: str = None,
        application_id: str = None,
        application_identity_type: str = None,
        application_name: str = None,
        application_owner: main_models.GetApplicationResponseBodyApplicationApplicationOwner = None,
        application_source_type: str = None,
        application_template_id: str = None,
        application_visibility: List[str] = None,
        authorization_type: str = None,
        client_id: str = None,
        create_time: int = None,
        custom_fields: List[main_models.GetApplicationResponseBodyApplicationCustomFields] = None,
        custom_subject_status: str = None,
        description: str = None,
        features: str = None,
        instance_id: str = None,
        logo_url: str = None,
        m_2mclient_status: str = None,
        managed_service_code: str = None,
        resource_server_identifier: str = None,
        resource_server_source_type: str = None,
        resource_server_status: str = None,
        service_managed: bool = None,
        smart_config_capabilities: List[str] = None,
        sso_type: str = None,
        status: str = None,
        update_time: int = None,
    ):
        # The status of the Developer API feature for the application. Valid values:
        # 
        # - enabled
        # 
        # - disabled
        self.api_invoke_status = api_invoke_status
        # The application creation type.
        self.application_creation_type = application_creation_type
        # The application ID.
        self.application_id = application_id
        # The identity type of the application. Valid values:
        # 
        # - application: application.
        # 
        # - agent: agent.
        self.application_identity_type = application_identity_type
        # The application name.
        self.application_name = application_name
        # The application owners.
        self.application_owner = application_owner
        # The source from which the application was created. Valid values:
        # 
        # - urn:alibaba:idaas:app:source:template: The application was created from a template.
        # 
        # - urn:alibaba:idaas:app:source:standard: The application was created based on a standard protocol.
        self.application_source_type = application_source_type
        # The ID of the application template that is associated with the application. This parameter is returned only if the application was created from a template.
        self.application_template_id = application_template_id
        # The visibility of the application.
        self.application_visibility = application_visibility
        # The authorization type for application access. Valid values:
        # 
        # - authorize_required: Explicit authorization is required for access.
        # 
        # - default_all: All members have access by default.
        self.authorization_type = authorization_type
        # The client ID of the application.
        self.client_id = client_id
        # The time when the application was created. This value is a UNIX timestamp. Unit: milliseconds.
        self.create_time = create_time
        # The custom fields of the application.
        self.custom_fields = custom_fields
        # Indicates whether to customize the Subject field in the token. If this feature is enabled, the issued access token changes from \\<clientId> to \\<clientId>:\\<client.activeSubjectUrn>. The client.activeSubjectUrn is set in the attribute mapping of the application\\"s federated identity provider.
        self.custom_subject_status = custom_subject_status
        # The description of the application.
        self.description = description
        # The features that the application supports. This parameter is returned as a JSON array string. Valid values:
        # 
        # - sso: single sign-on (SSO).
        # 
        # - provision: account synchronization.
        # 
        # - api_invoke: API calling.
        self.features = features
        # The instance ID.
        self.instance_id = instance_id
        # The URL of the application icon.
        self.logo_url = logo_url
        # The status of the M2M client.
        self.m_2mclient_status = m_2mclient_status
        # The service code of the cloud product that hosts the application template.
        self.managed_service_code = managed_service_code
        # The unique identifier of the resource server. This corresponds to the audience of the resource server.
        self.resource_server_identifier = resource_server_identifier
        # The source type of the resource server.
        self.resource_server_source_type = resource_server_source_type
        # The status of the resource server.
        self.resource_server_status = resource_server_status
        # Indicates whether the application template is hosted by a cloud service.
        self.service_managed = service_managed
        self.smart_config_capabilities = smart_config_capabilities
        # The single sign-on (SSO) protocol. Valid values:
        # 
        # - saml2: SAML 2.0.
        # 
        # - oidc: OpenID Connect.
        # 
        # - oauth2/m2m: OAuth 2.0.
        # 
        # - oidc+oauth2/m2m: OpenID Connect and OAuth 2.0.
        self.sso_type = sso_type
        # The application status. Valid values:
        # 
        # - enabled
        # 
        # - disabled
        self.status = status
        # The time when the application was last updated. This value is a UNIX timestamp. Unit: milliseconds.
        self.update_time = update_time

    def validate(self):
        if self.application_owner:
            self.application_owner.validate()
        if self.custom_fields:
            for v1 in self.custom_fields:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_invoke_status is not None:
            result['ApiInvokeStatus'] = self.api_invoke_status

        if self.application_creation_type is not None:
            result['ApplicationCreationType'] = self.application_creation_type

        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.application_identity_type is not None:
            result['ApplicationIdentityType'] = self.application_identity_type

        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        if self.application_owner is not None:
            result['ApplicationOwner'] = self.application_owner.to_map()

        if self.application_source_type is not None:
            result['ApplicationSourceType'] = self.application_source_type

        if self.application_template_id is not None:
            result['ApplicationTemplateId'] = self.application_template_id

        if self.application_visibility is not None:
            result['ApplicationVisibility'] = self.application_visibility

        if self.authorization_type is not None:
            result['AuthorizationType'] = self.authorization_type

        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        result['CustomFields'] = []
        if self.custom_fields is not None:
            for k1 in self.custom_fields:
                result['CustomFields'].append(k1.to_map() if k1 else None)

        if self.custom_subject_status is not None:
            result['CustomSubjectStatus'] = self.custom_subject_status

        if self.description is not None:
            result['Description'] = self.description

        if self.features is not None:
            result['Features'] = self.features

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.logo_url is not None:
            result['LogoUrl'] = self.logo_url

        if self.m_2mclient_status is not None:
            result['M2MClientStatus'] = self.m_2mclient_status

        if self.managed_service_code is not None:
            result['ManagedServiceCode'] = self.managed_service_code

        if self.resource_server_identifier is not None:
            result['ResourceServerIdentifier'] = self.resource_server_identifier

        if self.resource_server_source_type is not None:
            result['ResourceServerSourceType'] = self.resource_server_source_type

        if self.resource_server_status is not None:
            result['ResourceServerStatus'] = self.resource_server_status

        if self.service_managed is not None:
            result['ServiceManaged'] = self.service_managed

        if self.smart_config_capabilities is not None:
            result['SmartConfigCapabilities'] = self.smart_config_capabilities

        if self.sso_type is not None:
            result['SsoType'] = self.sso_type

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiInvokeStatus') is not None:
            self.api_invoke_status = m.get('ApiInvokeStatus')

        if m.get('ApplicationCreationType') is not None:
            self.application_creation_type = m.get('ApplicationCreationType')

        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ApplicationIdentityType') is not None:
            self.application_identity_type = m.get('ApplicationIdentityType')

        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        if m.get('ApplicationOwner') is not None:
            temp_model = main_models.GetApplicationResponseBodyApplicationApplicationOwner()
            self.application_owner = temp_model.from_map(m.get('ApplicationOwner'))

        if m.get('ApplicationSourceType') is not None:
            self.application_source_type = m.get('ApplicationSourceType')

        if m.get('ApplicationTemplateId') is not None:
            self.application_template_id = m.get('ApplicationTemplateId')

        if m.get('ApplicationVisibility') is not None:
            self.application_visibility = m.get('ApplicationVisibility')

        if m.get('AuthorizationType') is not None:
            self.authorization_type = m.get('AuthorizationType')

        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        self.custom_fields = []
        if m.get('CustomFields') is not None:
            for k1 in m.get('CustomFields'):
                temp_model = main_models.GetApplicationResponseBodyApplicationCustomFields()
                self.custom_fields.append(temp_model.from_map(k1))

        if m.get('CustomSubjectStatus') is not None:
            self.custom_subject_status = m.get('CustomSubjectStatus')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Features') is not None:
            self.features = m.get('Features')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LogoUrl') is not None:
            self.logo_url = m.get('LogoUrl')

        if m.get('M2MClientStatus') is not None:
            self.m_2mclient_status = m.get('M2MClientStatus')

        if m.get('ManagedServiceCode') is not None:
            self.managed_service_code = m.get('ManagedServiceCode')

        if m.get('ResourceServerIdentifier') is not None:
            self.resource_server_identifier = m.get('ResourceServerIdentifier')

        if m.get('ResourceServerSourceType') is not None:
            self.resource_server_source_type = m.get('ResourceServerSourceType')

        if m.get('ResourceServerStatus') is not None:
            self.resource_server_status = m.get('ResourceServerStatus')

        if m.get('ServiceManaged') is not None:
            self.service_managed = m.get('ServiceManaged')

        if m.get('SmartConfigCapabilities') is not None:
            self.smart_config_capabilities = m.get('SmartConfigCapabilities')

        if m.get('SsoType') is not None:
            self.sso_type = m.get('SsoType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class GetApplicationResponseBodyApplicationCustomFields(DaraModel):
    def __init__(
        self,
        field_name: str = None,
        field_value: str = None,
    ):
        # The custom field name.
        self.field_name = field_name
        # The custom field value.
        self.field_value = field_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field_name is not None:
            result['FieldName'] = self.field_name

        if self.field_value is not None:
            result['FieldValue'] = self.field_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')

        if m.get('FieldValue') is not None:
            self.field_value = m.get('FieldValue')

        return self

class GetApplicationResponseBodyApplicationApplicationOwner(DaraModel):
    def __init__(
        self,
        group_ids: List[str] = None,
        user_ids: List[str] = None,
    ):
        # The group IDs of the application owners.
        self.group_ids = group_ids
        # The user IDs of the application owners.
        self.user_ids = user_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_ids is not None:
            result['GroupIds'] = self.group_ids

        if self.user_ids is not None:
            result['UserIds'] = self.user_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupIds') is not None:
            self.group_ids = m.get('GroupIds')

        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')

        return self

