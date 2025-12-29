# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class ForeignInstanceCredInfo(DaraModel):
    def __init__(
        self,
        cred_info: Dict[str, str] = None,
        cred_type: str = None,
    ):
        self.cred_info = cred_info
        self.cred_type = cred_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cred_info is not None:
            result['CredInfo'] = self.cred_info

        if self.cred_type is not None:
            result['CredType'] = self.cred_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredInfo') is not None:
            self.cred_info = m.get('CredInfo')

        if m.get('CredType') is not None:
            self.cred_type = m.get('CredType')

        return self

