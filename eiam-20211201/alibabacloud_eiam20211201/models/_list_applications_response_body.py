# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class ListApplicationsResponseBody(DaraModel):
    def __init__(
        self,
        applications: List[main_models.ListApplicationsResponseBodyApplications] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The details of the applications.
        self.applications = applications
        # The ID of the request.
        self.request_id = request_id
        # The total number of the returned entries.
        self.total_count = total_count

    def validate(self):
        if self.applications:
            for v1 in self.applications:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Applications'] = []
        if self.applications is not None:
            for k1 in self.applications:
                result['Applications'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.applications = []
        if m.get('Applications') is not None:
            for k1 in m.get('Applications'):
                temp_model = main_models.ListApplicationsResponseBodyApplications()
                self.applications.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListApplicationsResponseBodyApplications(DaraModel):
    def __init__(
        self,
        application_creation_type: str = None,
        application_id: str = None,
        application_name: str = None,
        application_source_type: str = None,
        application_template_id: str = None,
        client_id: str = None,
        create_time: int = None,
        description: str = None,
        features: str = None,
        instance_id: str = None,
        logo_url: str = None,
        managed_service_code: str = None,
        resource_server_identifier: str = None,
        resource_server_source_type: str = None,
        resource_server_status: str = None,
        service_managed: bool = None,
        sso_type: str = None,
        status: str = None,
        update_time: int = None,
    ):
        self.application_creation_type = application_creation_type
        # The ID of the application.
        self.application_id = application_id
        # The name of the application.
        self.application_name = application_name
        # The origin of the application. Valid values:
        # 
        # *   urn:alibaba:idaas:app:source:template: The application is created based on a template.
        # *   urn:alibaba:idaas: The application is created based on the standard protocol.
        self.application_source_type = application_source_type
        # The application template ID.
        self.application_template_id = application_template_id
        # The client ID of the application.
        self.client_id = client_id
        # The time when the application was created. The value is a UNIX timestamp. Unit: milliseconds.
        self.create_time = create_time
        # The description of the application.
        self.description = description
        # The features that are supported by the application. The value is a JSON array. Valid values:
        # 
        # *   sso: The application supports SSO.
        # *   slo: The application supports SLO.
        # *   provision: The application supports account synchronization.
        # *   api_invoke: The application supports custom APIs.
        # *   m2m_client: The application supports M2M Client.
        # *   resource_server: The application supports Resource Server.
        # *   other: undertake.
        self.features = features
        # The ID of the instance.
        self.instance_id = instance_id
        # The URL of the application icon.
        self.logo_url = logo_url
        # The service code of the cloud service that manages the application template.
        self.managed_service_code = managed_service_code
        self.resource_server_identifier = resource_server_identifier
        self.resource_server_source_type = resource_server_source_type
        self.resource_server_status = resource_server_status
        # Indicates whether the application template is managed by a cloud service.
        self.service_managed = service_managed
        # The type of the single sign-on (SSO) protocol. Valid values:
        # 
        # *   saml2: the Security Assertion Markup Language (SAML) 2.0 protocol.
        # *   oidc: the OpenID Connect (OIDC) protocol.
        # *   oauth2/m2m: the OAuth2.0  protocol M2M.
        self.sso_type = sso_type
        # The status of the application. Valid values:
        # 
        # *   enabled: The application is enabled.
        # *   disabled: The application is disabled.
        # *   deleted: The application is deleted.
        self.status = status
        # The time when the application was last updated. The value is a UNIX timestamp. Unit: milliseconds.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_creation_type is not None:
            result['ApplicationCreationType'] = self.application_creation_type

        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        if self.application_source_type is not None:
            result['ApplicationSourceType'] = self.application_source_type

        if self.application_template_id is not None:
            result['ApplicationTemplateId'] = self.application_template_id

        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.features is not None:
            result['Features'] = self.features

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.logo_url is not None:
            result['LogoUrl'] = self.logo_url

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

        if self.sso_type is not None:
            result['SsoType'] = self.sso_type

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationCreationType') is not None:
            self.application_creation_type = m.get('ApplicationCreationType')

        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        if m.get('ApplicationSourceType') is not None:
            self.application_source_type = m.get('ApplicationSourceType')

        if m.get('ApplicationTemplateId') is not None:
            self.application_template_id = m.get('ApplicationTemplateId')

        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Features') is not None:
            self.features = m.get('Features')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LogoUrl') is not None:
            self.logo_url = m.get('LogoUrl')

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

        if m.get('SsoType') is not None:
            self.sso_type = m.get('SsoType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

