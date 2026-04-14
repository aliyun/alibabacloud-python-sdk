# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckDirectSendMessageSampleShrinkRequest(DaraModel):
    def __init__(
        self,
        cust_space_id: str = None,
        interactive_shrink: str = None,
        text_shrink: str = None,
        type: str = None,
    ):
        # This parameter is required.
        self.cust_space_id = cust_space_id
        self.interactive_shrink = interactive_shrink
        self.text_shrink = text_shrink
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

        if self.interactive_shrink is not None:
            result['Interactive'] = self.interactive_shrink

        if self.text_shrink is not None:
            result['Text'] = self.text_shrink

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')

        if m.get('Interactive') is not None:
            self.interactive_shrink = m.get('Interactive')

        if m.get('Text') is not None:
            self.text_shrink = m.get('Text')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

