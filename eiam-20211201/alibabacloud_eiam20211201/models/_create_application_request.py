# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateApplicationRequest(DaraModel):
    def __init__(
        self,
        application_name: str = None,
        application_source_type: str = None,
        application_template_id: str = None,
        description: str = None,
        instance_id: str = None,
        logo_url: str = None,
        sso_type: str = None,
    ):
        # The name of the application.
        # 
        # This parameter is required.
        self.application_name = application_name
        # The type of the application source. Valid values:
        # 
        # *   urn:alibaba:idaas:app:source:template: application template
        # *   urn:alibaba:idaas:app:source:standard: standard protocol
        # 
        # This parameter is required.
        self.application_source_type = application_source_type
        # The ID of the application template. This parameter is required if you set the ApplicationSourceType parameter to urn:alibaba:idaas:app:source:template.
        self.application_template_id = application_template_id
        # The description of the application.
        self.description = description
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The URL of the application logo.
        self.logo_url = logo_url
        # The SSO protocol. Valid values:
        # 
        # *   saml2: the SAML 2.0 protocol.
        # *   oidc: the OpenID Connect protocol.
        # 
        # This parameter is required.
        self.sso_type = sso_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        if self.application_source_type is not None:
            result['ApplicationSourceType'] = self.application_source_type

        if self.application_template_id is not None:
            result['ApplicationTemplateId'] = self.application_template_id

        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.logo_url is not None:
            result['LogoUrl'] = self.logo_url

        if self.sso_type is not None:
            result['SsoType'] = self.sso_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        if m.get('ApplicationSourceType') is not None:
            self.application_source_type = m.get('ApplicationSourceType')

        if m.get('ApplicationTemplateId') is not None:
            self.application_template_id = m.get('ApplicationTemplateId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LogoUrl') is not None:
            self.logo_url = m.get('LogoUrl')

        if m.get('SsoType') is not None:
            self.sso_type = m.get('SsoType')

        return self

