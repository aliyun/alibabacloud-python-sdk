# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CompanyFourElementsVerificationRequest(DaraModel):
    def __init__(
        self,
        auth_code: str = None,
        ep_cert_name: str = None,
        ep_cert_no: str = None,
        legal_person_cert_name: str = None,
        legal_person_cert_no: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The authorization code.
        # 
        # >  On the [My Applications](https://dytns.console.aliyun.com/analysis/apply) page in the [Cell Phone Number Service console](https://dytns.console.aliyun.com/overview?spm=a2c4g.608385.0.0.79847f8b3awqUC), you can obtain the authorization code (also known as authorization ID).
        # 
        # This parameter is required.
        self.auth_code = auth_code
        # The enterprise name.
        self.ep_cert_name = ep_cert_name
        # The business license number.
        # 
        # This parameter is required.
        self.ep_cert_no = ep_cert_no
        # The name of the legal representative.
        # 
        # >  If an enterprise has multiple legal representatives, separate them with commas (,).
        # 
        # This parameter is required.
        self.legal_person_cert_name = legal_person_cert_name
        # The ID card number of the legal representative.
        # 
        # >  If an enterprise has multiple legal representatives, separate the ID card numbers with commas (,).
        # 
        # This parameter is required.
        self.legal_person_cert_no = legal_person_cert_no
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_code is not None:
            result['AuthCode'] = self.auth_code

        if self.ep_cert_name is not None:
            result['EpCertName'] = self.ep_cert_name

        if self.ep_cert_no is not None:
            result['EpCertNo'] = self.ep_cert_no

        if self.legal_person_cert_name is not None:
            result['LegalPersonCertName'] = self.legal_person_cert_name

        if self.legal_person_cert_no is not None:
            result['LegalPersonCertNo'] = self.legal_person_cert_no

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')

        if m.get('EpCertName') is not None:
            self.ep_cert_name = m.get('EpCertName')

        if m.get('EpCertNo') is not None:
            self.ep_cert_no = m.get('EpCertNo')

        if m.get('LegalPersonCertName') is not None:
            self.legal_person_cert_name = m.get('LegalPersonCertName')

        if m.get('LegalPersonCertNo') is not None:
            self.legal_person_cert_no = m.get('LegalPersonCertNo')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

