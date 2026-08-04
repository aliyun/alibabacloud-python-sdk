# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRealNameCertificationRequest(DaraModel):
    def __init__(
        self,
        account_certify_type: str = None,
        corporate_license_number: str = None,
        corporate_name: str = None,
        license_number: str = None,
        license_type: str = None,
        name: str = None,
        pk: str = None,
    ):
        self.account_certify_type = account_certify_type
        self.corporate_license_number = corporate_license_number
        self.corporate_name = corporate_name
        self.license_number = license_number
        self.license_type = license_type
        self.name = name
        self.pk = pk

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_certify_type is not None:
            result['AccountCertifyType'] = self.account_certify_type

        if self.corporate_license_number is not None:
            result['CorporateLicenseNumber'] = self.corporate_license_number

        if self.corporate_name is not None:
            result['CorporateName'] = self.corporate_name

        if self.license_number is not None:
            result['LicenseNumber'] = self.license_number

        if self.license_type is not None:
            result['LicenseType'] = self.license_type

        if self.name is not None:
            result['Name'] = self.name

        if self.pk is not None:
            result['Pk'] = self.pk

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountCertifyType') is not None:
            self.account_certify_type = m.get('AccountCertifyType')

        if m.get('CorporateLicenseNumber') is not None:
            self.corporate_license_number = m.get('CorporateLicenseNumber')

        if m.get('CorporateName') is not None:
            self.corporate_name = m.get('CorporateName')

        if m.get('LicenseNumber') is not None:
            self.license_number = m.get('LicenseNumber')

        if m.get('LicenseType') is not None:
            self.license_type = m.get('LicenseType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Pk') is not None:
            self.pk = m.get('Pk')

        return self

