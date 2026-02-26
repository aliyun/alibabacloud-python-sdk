# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GoodsShippingNoticeCreateCmd(DaraModel):
    def __init__(
        self,
        cp_code: str = None,
        dispute_id: str = None,
        logistics_no: str = None,
    ):
        # This parameter is required.
        self.cp_code = cp_code
        # This parameter is required.
        self.dispute_id = dispute_id
        # This parameter is required.
        self.logistics_no = logistics_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cp_code is not None:
            result['cpCode'] = self.cp_code

        if self.dispute_id is not None:
            result['disputeId'] = self.dispute_id

        if self.logistics_no is not None:
            result['logisticsNo'] = self.logistics_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cpCode') is not None:
            self.cp_code = m.get('cpCode')

        if m.get('disputeId') is not None:
            self.dispute_id = m.get('disputeId')

        if m.get('logisticsNo') is not None:
            self.logistics_no = m.get('logisticsNo')

        return self

