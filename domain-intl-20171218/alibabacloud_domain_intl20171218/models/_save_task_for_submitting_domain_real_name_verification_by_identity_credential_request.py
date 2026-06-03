# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SaveTaskForSubmittingDomainRealNameVerificationByIdentityCredentialRequest(DaraModel):
    def __init__(
        self,
        domain_name: List[str] = None,
        identity_credential: str = None,
        identity_credential_no: str = None,
        identity_credential_type: str = None,
        lang: str = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.domain_name = domain_name
        # This parameter is required.
        self.identity_credential = identity_credential
        # This parameter is required.
        self.identity_credential_no = identity_credential_no
        # This parameter is required.
        self.identity_credential_type = identity_credential_type
        self.lang = lang
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.identity_credential is not None:
            result['IdentityCredential'] = self.identity_credential

        if self.identity_credential_no is not None:
            result['IdentityCredentialNo'] = self.identity_credential_no

        if self.identity_credential_type is not None:
            result['IdentityCredentialType'] = self.identity_credential_type

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('IdentityCredential') is not None:
            self.identity_credential = m.get('IdentityCredential')

        if m.get('IdentityCredentialNo') is not None:
            self.identity_credential_no = m.get('IdentityCredentialNo')

        if m.get('IdentityCredentialType') is not None:
            self.identity_credential_type = m.get('IdentityCredentialType')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        return self

