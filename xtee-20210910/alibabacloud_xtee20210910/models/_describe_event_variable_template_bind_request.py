# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeEventVariableTemplateBindRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        inputs: str = None,
        reg_id: str = None,
        template_code: str = None,
        type: str = None,
    ):
        # Sets the language type for requests and received messages. Default value is **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Input parameters, separated by commas if multiple.
        # 
        # This parameter is required.
        self.inputs = inputs
        # Region code
        self.reg_id = reg_id
        # Template code.
        self.template_code = template_code
        # Type
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.inputs is not None:
            result['inputs'] = self.inputs

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.template_code is not None:
            result['templateCode'] = self.template_code

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('inputs') is not None:
            self.inputs = m.get('inputs')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('templateCode') is not None:
            self.template_code = m.get('templateCode')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

