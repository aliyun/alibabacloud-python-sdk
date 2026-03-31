# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateQuotaRequest(DaraModel):
    def __init__(
        self,
        charge_type: str = None,
        commodity_code: str = None,
        commodity_data: str = None,
        part_nick_name: str = None,
    ):
        # This parameter is required.
        self.charge_type = charge_type
        # This parameter is required.
        self.commodity_code = commodity_code
        self.commodity_data = commodity_data
        self.part_nick_name = part_nick_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type

        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code

        if self.commodity_data is not None:
            result['commodityData'] = self.commodity_data

        if self.part_nick_name is not None:
            result['partNickName'] = self.part_nick_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')

        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')

        if m.get('commodityData') is not None:
            self.commodity_data = m.get('commodityData')

        if m.get('partNickName') is not None:
            self.part_nick_name = m.get('partNickName')

        return self

