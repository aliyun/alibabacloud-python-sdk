# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SwitchQueryVariableRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        id: int = None,
        reg_id: str = None,
        status: str = None,
    ):
        # The language of the request and response. Default value: **zh**. Valid values:
        # - **zh**: Chinese.
        # - **en**: English.
        self.lang = lang
        # The primary key ID.
        # 
        # This parameter is required.
        self.id = id
        # The region code.
        # 
        # This parameter is required.
        self.reg_id = reg_id
        # The status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.id is not None:
            result['id'] = self.id

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

