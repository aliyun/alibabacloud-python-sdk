# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ims20190815 import models as main_models
from darabonba.model import DaraModel

class ListSAMLProvidersResponseBody(DaraModel):
    def __init__(
        self,
        is_truncated: bool = None,
        marker: str = None,
        request_id: str = None,
        samlproviders: main_models.ListSAMLProvidersResponseBodySAMLProviders = None,
    ):
        self.is_truncated = is_truncated
        self.marker = marker
        self.request_id = request_id
        self.samlproviders = samlproviders

    def validate(self):
        if self.samlproviders:
            self.samlproviders.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated

        if self.marker is not None:
            result['Marker'] = self.marker

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.samlproviders is not None:
            result['SAMLProviders'] = self.samlproviders.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')

        if m.get('Marker') is not None:
            self.marker = m.get('Marker')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SAMLProviders') is not None:
            temp_model = main_models.ListSAMLProvidersResponseBodySAMLProviders()
            self.samlproviders = temp_model.from_map(m.get('SAMLProviders'))

        return self

class ListSAMLProvidersResponseBodySAMLProviders(DaraModel):
    def __init__(
        self,
        samlprovider: List[main_models.ListSAMLProvidersResponseBodySAMLProvidersSAMLProvider] = None,
    ):
        self.samlprovider = samlprovider

    def validate(self):
        if self.samlprovider:
            for v1 in self.samlprovider:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SAMLProvider'] = []
        if self.samlprovider is not None:
            for k1 in self.samlprovider:
                result['SAMLProvider'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.samlprovider = []
        if m.get('SAMLProvider') is not None:
            for k1 in m.get('SAMLProvider'):
                temp_model = main_models.ListSAMLProvidersResponseBodySAMLProvidersSAMLProvider()
                self.samlprovider.append(temp_model.from_map(k1))

        return self

class ListSAMLProvidersResponseBodySAMLProvidersSAMLProvider(DaraModel):
    def __init__(
        self,
        arn: str = None,
        create_date: str = None,
        description: str = None,
        samlprovider_name: str = None,
        update_date: str = None,
    ):
        self.arn = arn
        self.create_date = create_date
        self.description = description
        self.samlprovider_name = samlprovider_name
        self.update_date = update_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arn is not None:
            result['Arn'] = self.arn

        if self.create_date is not None:
            result['CreateDate'] = self.create_date

        if self.description is not None:
            result['Description'] = self.description

        if self.samlprovider_name is not None:
            result['SAMLProviderName'] = self.samlprovider_name

        if self.update_date is not None:
            result['UpdateDate'] = self.update_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')

        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('SAMLProviderName') is not None:
            self.samlprovider_name = m.get('SAMLProviderName')

        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')

        return self

