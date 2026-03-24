# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCdnCertificateSigningRequestRequest(DaraModel):
    def __init__(
        self,
        city: str = None,
        common_name: str = None,
        country: str = None,
        email: str = None,
        organization: str = None,
        organization_unit: str = None,
        sans: str = None,
        state: str = None,
    ):
        # The city. Default value: Hangzhou.
        self.city = city
        # The Common Name of the certificate.
        # 
        # This parameter is required.
        self.common_name = common_name
        # The country or region in which the organization is located. Default value: CN.
        self.country = country
        # The email address.
        self.email = email
        # The name of the organization. Default value: Alibaba Inc.
        self.organization = organization
        # The name of the department. Default value: Aliyun CDN.
        self.organization_unit = organization_unit
        # The Subject Alternative Name (SAN) extension of the SSL certificate. This extension is used to add domain names to the certificate. Separate multiple domain names with commas (,).
        self.sans = sans
        # The provincial district. Default value: Zhejiang.
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.city is not None:
            result['City'] = self.city

        if self.common_name is not None:
            result['CommonName'] = self.common_name

        if self.country is not None:
            result['Country'] = self.country

        if self.email is not None:
            result['Email'] = self.email

        if self.organization is not None:
            result['Organization'] = self.organization

        if self.organization_unit is not None:
            result['OrganizationUnit'] = self.organization_unit

        if self.sans is not None:
            result['SANs'] = self.sans

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('City') is not None:
            self.city = m.get('City')

        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')

        if m.get('Country') is not None:
            self.country = m.get('Country')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('Organization') is not None:
            self.organization = m.get('Organization')

        if m.get('OrganizationUnit') is not None:
            self.organization_unit = m.get('OrganizationUnit')

        if m.get('SANs') is not None:
            self.sans = m.get('SANs')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

