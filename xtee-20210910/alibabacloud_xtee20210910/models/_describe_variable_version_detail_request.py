# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVariableVersionDetailRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        object_code: str = None,
        object_id: int = None,
        reg_id: str = None,
        type: str = None,
        version: int = None,
    ):
        # Sets the language type for requests and received messages, default value is **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Associated variable name.
        self.object_code = object_code
        # Associated variable ID.
        self.object_id = object_id
        # Region code.
        self.reg_id = reg_id
        # Type.
        self.type = type
        # Version.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.object_code is not None:
            result['objectCode'] = self.object_code

        if self.object_id is not None:
            result['objectId'] = self.object_id

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.type is not None:
            result['type'] = self.type

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('objectCode') is not None:
            self.object_code = m.get('objectCode')

        if m.get('objectId') is not None:
            self.object_id = m.get('objectId')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

