# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyCustVariableRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        condition: str = None,
        data_version: int = None,
        description: str = None,
        event_codes: str = None,
        id: int = None,
        name: str = None,
        outputs: str = None,
        reg_id: str = None,
    ):
        # Sets the language type for requests and received messages, default value is **zh**. Values: 
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Condition value.
        self.condition = condition
        # Data version.
        # 
        # This parameter is required.
        self.data_version = data_version
        # Description information.
        self.description = description
        # Event code.
        self.event_codes = event_codes
        # Variable ID
        # 
        # This parameter is required.
        self.id = id
        # Variable name
        # 
        # This parameter is required.
        self.name = name
        # Output
        self.outputs = outputs
        # Region code
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

        if self.condition is not None:
            result['condition'] = self.condition

        if self.data_version is not None:
            result['dataVersion'] = self.data_version

        if self.description is not None:
            result['description'] = self.description

        if self.event_codes is not None:
            result['eventCodes'] = self.event_codes

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.outputs is not None:
            result['outputs'] = self.outputs

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('condition') is not None:
            self.condition = m.get('condition')

        if m.get('dataVersion') is not None:
            self.data_version = m.get('dataVersion')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('eventCodes') is not None:
            self.event_codes = m.get('eventCodes')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('outputs') is not None:
            self.outputs = m.get('outputs')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        return self

