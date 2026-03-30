# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateWHClientCertificateRequest(DaraModel):
    def __init__(
        self,
        after_time: int = None,
        algorithm: str = None,
        before_time: int = None,
        common_name: str = None,
        country: str = None,
        csr: str = None,
        days: int = None,
        immediately: int = None,
        locality: str = None,
        months: int = None,
        organization: str = None,
        organization_unit: str = None,
        parent_identifier: str = None,
        san_type: int = None,
        san_value: str = None,
        state: str = None,
        years: int = None,
    ):
        self.after_time = after_time
        self.algorithm = algorithm
        self.before_time = before_time
        self.common_name = common_name
        self.country = country
        self.csr = csr
        self.days = days
        self.immediately = immediately
        self.locality = locality
        self.months = months
        self.organization = organization
        self.organization_unit = organization_unit
        # This parameter is required.
        self.parent_identifier = parent_identifier
        self.san_type = san_type
        self.san_value = san_value
        self.state = state
        self.years = years

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.after_time is not None:
            result['AfterTime'] = self.after_time

        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm

        if self.before_time is not None:
            result['BeforeTime'] = self.before_time

        if self.common_name is not None:
            result['CommonName'] = self.common_name

        if self.country is not None:
            result['Country'] = self.country

        if self.csr is not None:
            result['Csr'] = self.csr

        if self.days is not None:
            result['Days'] = self.days

        if self.immediately is not None:
            result['Immediately'] = self.immediately

        if self.locality is not None:
            result['Locality'] = self.locality

        if self.months is not None:
            result['Months'] = self.months

        if self.organization is not None:
            result['Organization'] = self.organization

        if self.organization_unit is not None:
            result['OrganizationUnit'] = self.organization_unit

        if self.parent_identifier is not None:
            result['ParentIdentifier'] = self.parent_identifier

        if self.san_type is not None:
            result['SanType'] = self.san_type

        if self.san_value is not None:
            result['SanValue'] = self.san_value

        if self.state is not None:
            result['State'] = self.state

        if self.years is not None:
            result['Years'] = self.years

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AfterTime') is not None:
            self.after_time = m.get('AfterTime')

        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')

        if m.get('BeforeTime') is not None:
            self.before_time = m.get('BeforeTime')

        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')

        if m.get('Country') is not None:
            self.country = m.get('Country')

        if m.get('Csr') is not None:
            self.csr = m.get('Csr')

        if m.get('Days') is not None:
            self.days = m.get('Days')

        if m.get('Immediately') is not None:
            self.immediately = m.get('Immediately')

        if m.get('Locality') is not None:
            self.locality = m.get('Locality')

        if m.get('Months') is not None:
            self.months = m.get('Months')

        if m.get('Organization') is not None:
            self.organization = m.get('Organization')

        if m.get('OrganizationUnit') is not None:
            self.organization_unit = m.get('OrganizationUnit')

        if m.get('ParentIdentifier') is not None:
            self.parent_identifier = m.get('ParentIdentifier')

        if m.get('SanType') is not None:
            self.san_type = m.get('SanType')

        if m.get('SanValue') is not None:
            self.san_value = m.get('SanValue')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Years') is not None:
            self.years = m.get('Years')

        return self

