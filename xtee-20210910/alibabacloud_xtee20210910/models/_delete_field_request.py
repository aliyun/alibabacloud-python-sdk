# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteFieldRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        id: int = None,
        name: str = None,
        reg_id: str = None,
    ):
        # Set the language type for requests and received messages, default value is **zh**. Values: 
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Primary key ID of the field
        self.id = id
        # Name of the field.
        self.name = name
        # Region code
        # 
        # This parameter is required.
        self.reg_id = reg_id

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

        if self.name is not None:
            result['name'] = self.name

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        return self

