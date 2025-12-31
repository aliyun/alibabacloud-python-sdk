# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cas20200630 import models as main_models
from darabonba.model import DaraModel

class CreateExternalCACertificateRequest(DaraModel):
    def __init__(
        self,
        api_passthrough: main_models.CreateExternalCACertificateRequestApiPassthrough = None,
        csr: str = None,
        instance_id: str = None,
        resource_group_id: str = None,
        tags: List[main_models.CreateExternalCACertificateRequestTags] = None,
        validity: str = None,
    ):
        self.api_passthrough = api_passthrough
        self.csr = csr
        self.instance_id = instance_id
        self.resource_group_id = resource_group_id
        self.tags = tags
        self.validity = validity

    def validate(self):
        if self.api_passthrough:
            self.api_passthrough.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_passthrough is not None:
            result['ApiPassthrough'] = self.api_passthrough.to_map()

        if self.csr is not None:
            result['Csr'] = self.csr

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.validity is not None:
            result['Validity'] = self.validity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiPassthrough') is not None:
            temp_model = main_models.CreateExternalCACertificateRequestApiPassthrough()
            self.api_passthrough = temp_model.from_map(m.get('ApiPassthrough'))

        if m.get('Csr') is not None:
            self.csr = m.get('Csr')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.CreateExternalCACertificateRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('Validity') is not None:
            self.validity = m.get('Validity')

        return self

class CreateExternalCACertificateRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateExternalCACertificateRequestApiPassthrough(DaraModel):
    def __init__(
        self,
        extensions: main_models.CreateExternalCACertificateRequestApiPassthroughExtensions = None,
        subject: main_models.CreateExternalCACertificateRequestApiPassthroughSubject = None,
    ):
        self.extensions = extensions
        self.subject = subject

    def validate(self):
        if self.extensions:
            self.extensions.validate()
        if self.subject:
            self.subject.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extensions is not None:
            result['Extensions'] = self.extensions.to_map()

        if self.subject is not None:
            result['Subject'] = self.subject.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extensions') is not None:
            temp_model = main_models.CreateExternalCACertificateRequestApiPassthroughExtensions()
            self.extensions = temp_model.from_map(m.get('Extensions'))

        if m.get('Subject') is not None:
            temp_model = main_models.CreateExternalCACertificateRequestApiPassthroughSubject()
            self.subject = temp_model.from_map(m.get('Subject'))

        return self

class CreateExternalCACertificateRequestApiPassthroughSubject(DaraModel):
    def __init__(
        self,
        common_name: str = None,
        country: str = None,
        locality: str = None,
        organization: str = None,
        organization_unit: str = None,
        state: str = None,
    ):
        self.common_name = common_name
        self.country = country
        self.locality = locality
        self.organization = organization
        self.organization_unit = organization_unit
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.common_name is not None:
            result['CommonName'] = self.common_name

        if self.country is not None:
            result['Country'] = self.country

        if self.locality is not None:
            result['Locality'] = self.locality

        if self.organization is not None:
            result['Organization'] = self.organization

        if self.organization_unit is not None:
            result['OrganizationUnit'] = self.organization_unit

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')

        if m.get('Country') is not None:
            self.country = m.get('Country')

        if m.get('Locality') is not None:
            self.locality = m.get('Locality')

        if m.get('Organization') is not None:
            self.organization = m.get('Organization')

        if m.get('OrganizationUnit') is not None:
            self.organization_unit = m.get('OrganizationUnit')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

class CreateExternalCACertificateRequestApiPassthroughExtensions(DaraModel):
    def __init__(
        self,
        extended_key_usages: List[str] = None,
        path_len_constraint: int = None,
    ):
        self.extended_key_usages = extended_key_usages
        self.path_len_constraint = path_len_constraint

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extended_key_usages is not None:
            result['ExtendedKeyUsages'] = self.extended_key_usages

        if self.path_len_constraint is not None:
            result['PathLenConstraint'] = self.path_len_constraint

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtendedKeyUsages') is not None:
            self.extended_key_usages = m.get('ExtendedKeyUsages')

        if m.get('PathLenConstraint') is not None:
            self.path_len_constraint = m.get('PathLenConstraint')

        return self

