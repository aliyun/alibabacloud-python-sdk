# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateBusinessOpportunityRequest(DaraModel):
    def __init__(
        self,
        biz_type: str = None,
        contact_name: str = None,
        mobile: str = None,
        source: int = None,
        vcode: str = None,
    ):
        # This parameter is required.
        self.biz_type = biz_type
        self.contact_name = contact_name
        # This parameter is required.
        self.mobile = mobile
        # This parameter is required.
        self.source = source
        self.vcode = vcode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.contact_name is not None:
            result['ContactName'] = self.contact_name

        if self.mobile is not None:
            result['Mobile'] = self.mobile

        if self.source is not None:
            result['Source'] = self.source

        if self.vcode is not None:
            result['VCode'] = self.vcode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')

        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('VCode') is not None:
            self.vcode = m.get('VCode')

        return self

