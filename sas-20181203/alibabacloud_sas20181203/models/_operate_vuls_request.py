# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class OperateVulsRequest(DaraModel):
    def __init__(
        self,
        operate_type: str = None,
        type: str = None,
        uuids: List[str] = None,
        vul_names: List[str] = None,
    ):
        # The operation on the vulnerabilities. Set the value to **vul_fix**, which indicates vulnerability fixing.
        # 
        # This parameter is required.
        self.operate_type = operate_type
        # The type of the vulnerabilities that you want to fix. Set the value to **cve**, which indicates Linux software vulnerabilities.
        # 
        # This parameter is required.
        self.type = type
        # The UUIDs of servers for which you want to fix vulnerabilities.
        # 
        # This parameter is required.
        self.uuids = uuids
        # The names of the vulnerabilities that you want to fix.
        # 
        # This parameter is required.
        self.vul_names = vul_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type

        if self.type is not None:
            result['Type'] = self.type

        if self.uuids is not None:
            result['Uuids'] = self.uuids

        if self.vul_names is not None:
            result['VulNames'] = self.vul_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Uuids') is not None:
            self.uuids = m.get('Uuids')

        if m.get('VulNames') is not None:
            self.vul_names = m.get('VulNames')

        return self

