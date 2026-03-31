# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class CreateApplicationRequest(DaraModel):
    def __init__(
        self,
        application_identity_type: str = None,
        application_name: str = None,
        application_owner: main_models.CreateApplicationRequestApplicationOwner = None,
        application_source_type: str = None,
        application_template_id: str = None,
        custom_fields: List[main_models.CreateApplicationRequestCustomFields] = None,
        description: str = None,
        instance_id: str = None,
        logo_url: str = None,
        sso_type: str = None,
    ):
        self.application_identity_type = application_identity_type
        # The name of the application.
        # 
        # This parameter is required.
        self.application_name = application_name
        self.application_owner = application_owner
        # The type of the application source. Valid values:
        # 
        # *   urn:alibaba:idaas:app:source:template: application template
        # *   urn:alibaba:idaas:app:source:standard: standard protocol
        # 
        # This parameter is required.
        self.application_source_type = application_source_type
        # The ID of the application template. This parameter is required if you set the ApplicationSourceType parameter to urn:alibaba:idaas:app:source:template.
        self.application_template_id = application_template_id
        self.custom_fields = custom_fields
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

        result['CustomFields'] = []
        if self.custom_fields is not None:
            for k1 in self.custom_fields:
                result['CustomFields'].append(k1.to_map() if k1 else None)

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
        if m.get('ApplicationIdentityType') is not None:
            self.application_identity_type = m.get('ApplicationIdentityType')

        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        if m.get('ApplicationOwner') is not None:
            temp_model = main_models.CreateApplicationRequestApplicationOwner()
            self.application_owner = temp_model.from_map(m.get('ApplicationOwner'))

        if m.get('ApplicationSourceType') is not None:
            self.application_source_type = m.get('ApplicationSourceType')

        if m.get('ApplicationTemplateId') is not None:
            self.application_template_id = m.get('ApplicationTemplateId')

        self.custom_fields = []
        if m.get('CustomFields') is not None:
            for k1 in m.get('CustomFields'):
                temp_model = main_models.CreateApplicationRequestCustomFields()
                self.custom_fields.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LogoUrl') is not None:
            self.logo_url = m.get('LogoUrl')

        if m.get('SsoType') is not None:
            self.sso_type = m.get('SsoType')

        return self

class CreateApplicationRequestCustomFields(DaraModel):
    def __init__(
        self,
        field_name: str = None,
        field_value: str = None,
    ):
        self.field_name = field_name
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

class CreateApplicationRequestApplicationOwner(DaraModel):
    def __init__(
        self,
        group_ids: List[str] = None,
        user_ids: List[str] = None,
    ):
        self.group_ids = group_ids
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

