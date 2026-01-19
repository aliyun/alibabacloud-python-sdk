# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SwitchExpressionVariableRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        data_version: int = None,
        id: int = None,
        reg_id: str = None,
        status: str = None,
    ):
        # Sets the language type for requests and received messages, with a default value of **zh**. Values: 
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Data version.
        # 
        # This parameter is required.
        self.data_version = data_version
        # Variable ID
        # 
        # This parameter is required.
        self.id = id
        # Region code
        # 
        # This parameter is required.
        self.reg_id = reg_id
        # Status.
        # 
        # This parameter is required.
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

        if self.data_version is not None:
            result['dataVersion'] = self.data_version

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

        if m.get('dataVersion') is not None:
            self.data_version = m.get('dataVersion')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

