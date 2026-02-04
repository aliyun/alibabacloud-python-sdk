# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChangeAccountEmailRequest(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        email: str = None,
    ):
        # The Alibaba Cloud account ID of the member.
        # 
        # This parameter is required.
        self.account_id = account_id
        # The email address to be bound to the member.
        # 
        # > The system automatically sends a verification email to the email address. After the verification is passed, the email address takes effect, and the system changes both the logon email address and secure email address of the member.
        # 
        # This parameter is required.
        self.email = email

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.email is not None:
            result['Email'] = self.email

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        return self

