# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BillDownOrUpgradeCmd(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        active_date: str = None,
        code_type: str = None,
        operate_typ_enum: str = None,
        qps: int = None,
    ):
        self.account_id = account_id
        self.active_date = active_date
        self.code_type = code_type
        self.operate_typ_enum = operate_typ_enum
        self.qps = qps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['accountId'] = self.account_id

        if self.active_date is not None:
            result['activeDate'] = self.active_date

        if self.code_type is not None:
            result['codeType'] = self.code_type

        if self.operate_typ_enum is not None:
            result['operateTypEnum'] = self.operate_typ_enum

        if self.qps is not None:
            result['qps'] = self.qps

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')

        if m.get('activeDate') is not None:
            self.active_date = m.get('activeDate')

        if m.get('codeType') is not None:
            self.code_type = m.get('codeType')

        if m.get('operateTypEnum') is not None:
            self.operate_typ_enum = m.get('operateTypEnum')

        if m.get('qps') is not None:
            self.qps = m.get('qps')

        return self

