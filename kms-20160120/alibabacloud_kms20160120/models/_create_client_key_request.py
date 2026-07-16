# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateClientKeyRequest(DaraModel):
    def __init__(
        self,
        aap_name: str = None,
        not_after: str = None,
        not_before: str = None,
        password: str = None,
    ):
        # The operation that you want to perform. Set the value to **CreateClientKey**.
        # 
        # This parameter is required.
        self.aap_name = aap_name
        # The encryption password of the client key.
        # 
        # The password must be 8 to 64 characters in length and must contain at least two of the following types: digits, letters, and special characters. Special characters include `~ ! @ # $ % ^ & * ? _ -`.
        self.not_after = not_after
        # The end of the validity period of the client key.
        # 
        # Specify the time in the ISO 8601 standard. The time must be in UTC. The time must be in the yyyy-MM-ddTHH:mm:ssZ format.
        # 
        # > 
        # 
        # *   If you do not configure NotAfter, the default value is the time when the client key was created plus five years.
        # *   If you configure NotAfter, you must configure NotBefore.
        self.not_before = not_before
        # The name of the AAP.
        # 
        # This parameter is required.
        self.password = password

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aap_name is not None:
            result['AapName'] = self.aap_name

        if self.not_after is not None:
            result['NotAfter'] = self.not_after

        if self.not_before is not None:
            result['NotBefore'] = self.not_before

        if self.password is not None:
            result['Password'] = self.password

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AapName') is not None:
            self.aap_name = m.get('AapName')

        if m.get('NotAfter') is not None:
            self.not_after = m.get('NotAfter')

        if m.get('NotBefore') is not None:
            self.not_before = m.get('NotBefore')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        return self

