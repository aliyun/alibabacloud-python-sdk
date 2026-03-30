# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ims20190815 import models as main_models
from darabonba.model import DaraModel

class ListOIDCProvidersResponseBody(DaraModel):
    def __init__(
        self,
        is_truncated: bool = None,
        marker: str = None,
        oidcproviders: main_models.ListOIDCProvidersResponseBodyOIDCProviders = None,
        request_id: str = None,
    ):
        # Indicates whether the response is truncated. Valid values:
        # 
        # *   true
        # *   false
        self.is_truncated = is_truncated
        # The `marker`. This parameter is returned only if the value of `IsTruncated` is `true`. If the parameter is returned, you can call this operation again and set this parameter to obtain the truncated part.``
        self.marker = marker
        self.oidcproviders = oidcproviders
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.oidcproviders:
            self.oidcproviders.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated

        if self.marker is not None:
            result['Marker'] = self.marker

        if self.oidcproviders is not None:
            result['OIDCProviders'] = self.oidcproviders.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')

        if m.get('Marker') is not None:
            self.marker = m.get('Marker')

        if m.get('OIDCProviders') is not None:
            temp_model = main_models.ListOIDCProvidersResponseBodyOIDCProviders()
            self.oidcproviders = temp_model.from_map(m.get('OIDCProviders'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListOIDCProvidersResponseBodyOIDCProviders(DaraModel):
    def __init__(
        self,
        oidcprovider: List[main_models.ListOIDCProvidersResponseBodyOIDCProvidersOIDCProvider] = None,
    ):
        self.oidcprovider = oidcprovider

    def validate(self):
        if self.oidcprovider:
            for v1 in self.oidcprovider:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['OIDCProvider'] = []
        if self.oidcprovider is not None:
            for k1 in self.oidcprovider:
                result['OIDCProvider'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.oidcprovider = []
        if m.get('OIDCProvider') is not None:
            for k1 in m.get('OIDCProvider'):
                temp_model = main_models.ListOIDCProvidersResponseBodyOIDCProvidersOIDCProvider()
                self.oidcprovider.append(temp_model.from_map(k1))

        return self

class ListOIDCProvidersResponseBodyOIDCProvidersOIDCProvider(DaraModel):
    def __init__(
        self,
        arn: str = None,
        client_ids: str = None,
        create_date: str = None,
        description: str = None,
        fingerprints: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        issuance_limit_time: int = None,
        issuer_url: str = None,
        oidcprovider_name: str = None,
        update_date: str = None,
    ):
        self.arn = arn
        self.client_ids = client_ids
        self.create_date = create_date
        self.description = description
        self.fingerprints = fingerprints
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.issuance_limit_time = issuance_limit_time
        self.issuer_url = issuer_url
        self.oidcprovider_name = oidcprovider_name
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

        if self.client_ids is not None:
            result['ClientIds'] = self.client_ids

        if self.create_date is not None:
            result['CreateDate'] = self.create_date

        if self.description is not None:
            result['Description'] = self.description

        if self.fingerprints is not None:
            result['Fingerprints'] = self.fingerprints

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.issuance_limit_time is not None:
            result['IssuanceLimitTime'] = self.issuance_limit_time

        if self.issuer_url is not None:
            result['IssuerUrl'] = self.issuer_url

        if self.oidcprovider_name is not None:
            result['OIDCProviderName'] = self.oidcprovider_name

        if self.update_date is not None:
            result['UpdateDate'] = self.update_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')

        if m.get('ClientIds') is not None:
            self.client_ids = m.get('ClientIds')

        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Fingerprints') is not None:
            self.fingerprints = m.get('Fingerprints')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('IssuanceLimitTime') is not None:
            self.issuance_limit_time = m.get('IssuanceLimitTime')

        if m.get('IssuerUrl') is not None:
            self.issuer_url = m.get('IssuerUrl')

        if m.get('OIDCProviderName') is not None:
            self.oidcprovider_name = m.get('OIDCProviderName')

        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')

        return self

