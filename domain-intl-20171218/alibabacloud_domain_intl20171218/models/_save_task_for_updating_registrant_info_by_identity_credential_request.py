# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SaveTaskForUpdatingRegistrantInfoByIdentityCredentialRequest(DaraModel):
    def __init__(
        self,
        address: str = None,
        city: str = None,
        country: str = None,
        domain_name: List[str] = None,
        email: str = None,
        identity_credential: str = None,
        identity_credential_no: str = None,
        identity_credential_type: str = None,
        lang: str = None,
        postal_code: str = None,
        province: str = None,
        registrant_name: str = None,
        registrant_organization: str = None,
        registrant_type: str = None,
        tel_area: str = None,
        tel_ext: str = None,
        telephone: str = None,
        transfer_out_prohibited: bool = None,
        user_client_ip: str = None,
    ):
        self.address = address
        self.city = city
        self.country = country
        # This parameter is required.
        self.domain_name = domain_name
        self.email = email
        # This parameter is required.
        self.identity_credential = identity_credential
        # This parameter is required.
        self.identity_credential_no = identity_credential_no
        # This parameter is required.
        self.identity_credential_type = identity_credential_type
        self.lang = lang
        self.postal_code = postal_code
        self.province = province
        self.registrant_name = registrant_name
        self.registrant_organization = registrant_organization
        # This parameter is required.
        self.registrant_type = registrant_type
        # This parameter is required.
        self.tel_area = tel_area
        self.tel_ext = tel_ext
        # This parameter is required.
        self.telephone = telephone
        # This parameter is required.
        self.transfer_out_prohibited = transfer_out_prohibited
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        if self.city is not None:
            result['City'] = self.city

        if self.country is not None:
            result['Country'] = self.country

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.email is not None:
            result['Email'] = self.email

        if self.identity_credential is not None:
            result['IdentityCredential'] = self.identity_credential

        if self.identity_credential_no is not None:
            result['IdentityCredentialNo'] = self.identity_credential_no

        if self.identity_credential_type is not None:
            result['IdentityCredentialType'] = self.identity_credential_type

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.postal_code is not None:
            result['PostalCode'] = self.postal_code

        if self.province is not None:
            result['Province'] = self.province

        if self.registrant_name is not None:
            result['RegistrantName'] = self.registrant_name

        if self.registrant_organization is not None:
            result['RegistrantOrganization'] = self.registrant_organization

        if self.registrant_type is not None:
            result['RegistrantType'] = self.registrant_type

        if self.tel_area is not None:
            result['TelArea'] = self.tel_area

        if self.tel_ext is not None:
            result['TelExt'] = self.tel_ext

        if self.telephone is not None:
            result['Telephone'] = self.telephone

        if self.transfer_out_prohibited is not None:
            result['TransferOutProhibited'] = self.transfer_out_prohibited

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('City') is not None:
            self.city = m.get('City')

        if m.get('Country') is not None:
            self.country = m.get('Country')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('IdentityCredential') is not None:
            self.identity_credential = m.get('IdentityCredential')

        if m.get('IdentityCredentialNo') is not None:
            self.identity_credential_no = m.get('IdentityCredentialNo')

        if m.get('IdentityCredentialType') is not None:
            self.identity_credential_type = m.get('IdentityCredentialType')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PostalCode') is not None:
            self.postal_code = m.get('PostalCode')

        if m.get('Province') is not None:
            self.province = m.get('Province')

        if m.get('RegistrantName') is not None:
            self.registrant_name = m.get('RegistrantName')

        if m.get('RegistrantOrganization') is not None:
            self.registrant_organization = m.get('RegistrantOrganization')

        if m.get('RegistrantType') is not None:
            self.registrant_type = m.get('RegistrantType')

        if m.get('TelArea') is not None:
            self.tel_area = m.get('TelArea')

        if m.get('TelExt') is not None:
            self.tel_ext = m.get('TelExt')

        if m.get('Telephone') is not None:
            self.telephone = m.get('Telephone')

        if m.get('TransferOutProhibited') is not None:
            self.transfer_out_prohibited = m.get('TransferOutProhibited')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        return self

