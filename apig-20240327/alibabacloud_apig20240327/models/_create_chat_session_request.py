# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateChatSessionRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        products: List[str] = None,
        talk_type: str = None,
    ):
        # The name of the chat session.
        self.name = name
        # The list of API products associated with the chat session.
        self.products = products
        # The conversation type of the session. Valid values: MODEL and AGENT.
        self.talk_type = talk_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.products is not None:
            result['products'] = self.products

        if self.talk_type is not None:
            result['talkType'] = self.talk_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('products') is not None:
            self.products = m.get('products')

        if m.get('talkType') is not None:
            self.talk_type = m.get('talkType')

        return self

