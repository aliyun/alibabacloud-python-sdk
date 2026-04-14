# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class CheckDirectSendMessageSampleRequest(DaraModel):
    def __init__(
        self,
        cust_space_id: str = None,
        interactive: Dict[str, Any] = None,
        text: Dict[str, Any] = None,
        type: str = None,
    ):
        # This parameter is required.
        self.cust_space_id = cust_space_id
        self.interactive = interactive
        self.text = text
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id

        if self.interactive is not None:
            result['Interactive'] = self.interactive

        if self.text is not None:
            result['Text'] = self.text

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')

        if m.get('Interactive') is not None:
            self.interactive = m.get('Interactive')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

