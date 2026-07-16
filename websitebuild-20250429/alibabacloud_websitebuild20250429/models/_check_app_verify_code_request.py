# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckAppVerifyCodeRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        code: str = None,
        target: str = None,
        type: str = None,
    ):
        # The business ID.
        self.biz_id = biz_id
        # The verification code.
        self.code = code
        # The phone number or email address.
        self.target = target
        # The recipient type: phone or email.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.code is not None:
            result['Code'] = self.code

        if self.target is not None:
            result['Target'] = self.target

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

