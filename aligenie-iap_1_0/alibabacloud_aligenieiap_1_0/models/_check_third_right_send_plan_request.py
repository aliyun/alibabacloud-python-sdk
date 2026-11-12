# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class CheckThirdRightSendPlanRequest(DaraModel):
    def __init__(
        self,
        biz_group: str = None,
        biz_type: str = None,
        extend_info: Dict[str, Any] = None,
        sn: str = None,
        supplier_id: int = None,
    ):
        # Device group
        self.biz_group = biz_group
        # Device type
        self.biz_type = biz_type
        # Extension field
        self.extend_info = extend_info
        # Device SN
        self.sn = sn
        # Supplier ID
        self.supplier_id = supplier_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_group is not None:
            result['BizGroup'] = self.biz_group

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info

        if self.sn is not None:
            result['Sn'] = self.sn

        if self.supplier_id is not None:
            result['SupplierId'] = self.supplier_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizGroup') is not None:
            self.biz_group = m.get('BizGroup')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')

        if m.get('Sn') is not None:
            self.sn = m.get('Sn')

        if m.get('SupplierId') is not None:
            self.supplier_id = m.get('SupplierId')

        return self

