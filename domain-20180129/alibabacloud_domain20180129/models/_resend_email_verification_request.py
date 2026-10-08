# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResendEmailVerificationRequest(DaraModel):
    def __init__(
        self,
        email: str = None,
        lang: str = None,
        user_client_ip: str = None,
    ):
        # Mailboxes for which to resend the verification email. Separate multiple mailboxes with commas (,).
        # 
        # This parameter is required.
        self.email = email
        # Language of error messages returned by the API. Valid values:
        # - **zh**: Chinese.
        # - **en**: English.
        # 
        # Default value: **en**.
        self.lang = lang
        # User IP address. You can set it to 127.0.0.1.
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.email is not None:
            result['Email'] = self.email

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        return self

