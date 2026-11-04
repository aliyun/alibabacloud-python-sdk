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
        # The name of the attached application access point (AAP).
        # 
        # This parameter is required.
        self.aap_name = aap_name
        # The end time of the validity period of the ClientKey.
        # 
        # The time is specified in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time must be in UTC.
        #  >
        #  >- If you do not specify NotAfter, the default value is the creation time of the ClientKey plus 5 years.
        #  >- If you specify NotAfter, you must also specify NotBefore.
        self.not_after = not_after
        # The start time of the validity period of the ClientKey.
        # 
        # The time is specified in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time must be in UTC.
        #  >
        #  >- If you do not specify NotBefore, the default value is the creation time of the ClientKey.
        #  >- If you specify NotBefore, you must also specify NotAfter.
        self.not_before = not_before
        # The passphrase of the ClientKey.
        # 
        # The passphrase must be 8 to 64 characters in length and can contain digits, uppercase and lowercase letters, and special characters such as `~!@#$%^&*?_-`. It must contain at least two of these character types.
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

