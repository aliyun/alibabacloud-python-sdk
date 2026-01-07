# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDataAgentSubAccountInfoRequest(DaraModel):
    def __init__(
        self,
        dms_unit: str = None,
        sub_account_id: str = None,
    ):
        self.dms_unit = dms_unit
        self.sub_account_id = sub_account_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dms_unit is not None:
            result['DmsUnit'] = self.dms_unit

        if self.sub_account_id is not None:
            result['SubAccountId'] = self.sub_account_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DmsUnit') is not None:
            self.dms_unit = m.get('DmsUnit')

        if m.get('SubAccountId') is not None:
            self.sub_account_id = m.get('SubAccountId')

        return self

