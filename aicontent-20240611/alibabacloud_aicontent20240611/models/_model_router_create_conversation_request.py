# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModelRouterCreateConversationRequest(DaraModel):
    def __init__(
        self,
        chat_data: str = None,
        model_ids: str = None,
        title: str = None,
    ):
        self.chat_data = chat_data
        self.model_ids = model_ids
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chat_data is not None:
            result['chatData'] = self.chat_data

        if self.model_ids is not None:
            result['modelIds'] = self.model_ids

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chatData') is not None:
            self.chat_data = m.get('chatData')

        if m.get('modelIds') is not None:
            self.model_ids = m.get('modelIds')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

