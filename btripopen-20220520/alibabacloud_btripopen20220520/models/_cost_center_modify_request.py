# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CostCenterModifyRequest(DaraModel):
    def __init__(
        self,
        alipay_no: str = None,
        disable: int = None,
        number: str = None,
        scope: int = None,
        thirdpart_id: str = None,
        title: str = None,
    ):
        self.alipay_no = alipay_no
        self.disable = disable
        self.number = number
        # This parameter is required.
        self.scope = scope
        # This parameter is required.
        self.thirdpart_id = thirdpart_id
        # This parameter is required.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alipay_no is not None:
            result['alipay_no'] = self.alipay_no

        if self.disable is not None:
            result['disable'] = self.disable

        if self.number is not None:
            result['number'] = self.number

        if self.scope is not None:
            result['scope'] = self.scope

        if self.thirdpart_id is not None:
            result['thirdpart_id'] = self.thirdpart_id

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alipay_no') is not None:
            self.alipay_no = m.get('alipay_no')

        if m.get('disable') is not None:
            self.disable = m.get('disable')

        if m.get('number') is not None:
            self.number = m.get('number')

        if m.get('scope') is not None:
            self.scope = m.get('scope')

        if m.get('thirdpart_id') is not None:
            self.thirdpart_id = m.get('thirdpart_id')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

