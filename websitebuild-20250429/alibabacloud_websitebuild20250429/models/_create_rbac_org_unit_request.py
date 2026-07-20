# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRbacOrgUnitRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        org_unit_data: str = None,
    ):
        self.biz_id = biz_id
        self.org_unit_data = org_unit_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.org_unit_data is not None:
            result['OrgUnitData'] = self.org_unit_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('OrgUnitData') is not None:
            self.org_unit_data = m.get('OrgUnitData')

        return self

