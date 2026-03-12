# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SaveContactTemplateCredentialRequest(DaraModel):
    def __init__(
        self,
        contact_template_id: int = None,
        credential: str = None,
        credential_no: str = None,
        lang: str = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.contact_template_id = contact_template_id
        # This parameter is required.
        self.credential = credential
        # This parameter is required.
        self.credential_no = credential_no
        self.lang = lang
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_template_id is not None:
            result['ContactTemplateId'] = self.contact_template_id

        if self.credential is not None:
            result['Credential'] = self.credential

        if self.credential_no is not None:
            result['CredentialNo'] = self.credential_no

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactTemplateId') is not None:
            self.contact_template_id = m.get('ContactTemplateId')

        if m.get('Credential') is not None:
            self.credential = m.get('Credential')

        if m.get('CredentialNo') is not None:
            self.credential_no = m.get('CredentialNo')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        return self

