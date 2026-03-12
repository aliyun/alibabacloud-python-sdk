# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SaveTaskForSubmittingDomainNameCredentialRequest(DaraModel):
    def __init__(
        self,
        credential: str = None,
        credential_no: str = None,
        credential_type: str = None,
        domain_name: str = None,
        lang: str = None,
        sale_id: str = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.credential = credential
        # This parameter is required.
        self.credential_no = credential_no
        self.credential_type = credential_type
        # This parameter is required.
        self.domain_name = domain_name
        self.lang = lang
        self.sale_id = sale_id
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credential is not None:
            result['Credential'] = self.credential

        if self.credential_no is not None:
            result['CredentialNo'] = self.credential_no

        if self.credential_type is not None:
            result['CredentialType'] = self.credential_type

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.sale_id is not None:
            result['SaleId'] = self.sale_id

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Credential') is not None:
            self.credential = m.get('Credential')

        if m.get('CredentialNo') is not None:
            self.credential_no = m.get('CredentialNo')

        if m.get('CredentialType') is not None:
            self.credential_type = m.get('CredentialType')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('SaleId') is not None:
            self.sale_id = m.get('SaleId')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        return self

