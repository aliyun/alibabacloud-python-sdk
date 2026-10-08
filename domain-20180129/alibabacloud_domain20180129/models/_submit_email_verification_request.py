# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitEmailVerificationRequest(DaraModel):
    def __init__(
        self,
        email: str = None,
        lang: str = None,
        send_if_exist: bool = None,
        user_client_ip: str = None,
    ):
        # The mailbox that requires verification. Separate multiple mailboxes with commas (,).
        # 
        # This parameter is required.
        self.email = email
        # The language of the error message returned by the API. Valid values:
        # - **zh**: Chinese.
        # - **en**: English.
        # 
        # Default Value: **en**.
        self.lang = lang
        # Specifies whether to resend the verification email if it already exists. Valid values:
        # 
        # - **true**: Resend the verification email.
        # - **false**: Do not resend the verification email.
        # 
        # Default Value: **false**.
        self.send_if_exist = send_if_exist
        # The user IP address. You can set it to 127.0.0.1.
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

        if self.send_if_exist is not None:
            result['SendIfExist'] = self.send_if_exist

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('SendIfExist') is not None:
            self.send_if_exist = m.get('SendIfExist')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        return self

