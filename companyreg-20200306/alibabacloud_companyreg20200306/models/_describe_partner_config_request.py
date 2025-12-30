# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePartnerConfigRequest(DaraModel):
    def __init__(
        self,
        biz_type: str = None,
        partner_code: str = None,
    ):
        # This parameter is required.
        self.biz_type = biz_type
        # This parameter is required.
        self.partner_code = partner_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.partner_code is not None:
            result['PartnerCode'] = self.partner_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('PartnerCode') is not None:
            self.partner_code = m.get('PartnerCode')

        return self

