# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_searchplat20240529 import models as main_models
from darabonba.model import DaraModel

class GetTextGenerationRequest(DaraModel):
    def __init__(
        self,
        csi_level: str = None,
        enable_search: bool = None,
        messages: List[main_models.GetTextGenerationRequestMessages] = None,
        parameters: Dict[str, Any] = None,
        stream: bool = None,
    ):
        self.csi_level = csi_level
        self.enable_search = enable_search
        # This parameter is required.
        self.messages = messages
        self.parameters = parameters
        self.stream = stream

    def validate(self):
        if self.messages:
            for v1 in self.messages:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.csi_level is not None:
            result['csi_level'] = self.csi_level

        if self.enable_search is not None:
            result['enable_search'] = self.enable_search

        result['messages'] = []
        if self.messages is not None:
            for k1 in self.messages:
                result['messages'].append(k1.to_map() if k1 else None)

        if self.parameters is not None:
            result['parameters'] = self.parameters

        if self.stream is not None:
            result['stream'] = self.stream

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('csi_level') is not None:
            self.csi_level = m.get('csi_level')

        if m.get('enable_search') is not None:
            self.enable_search = m.get('enable_search')

        self.messages = []
        if m.get('messages') is not None:
            for k1 in m.get('messages'):
                temp_model = main_models.GetTextGenerationRequestMessages()
                self.messages.append(temp_model.from_map(k1))

        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')

        if m.get('stream') is not None:
            self.stream = m.get('stream')

        return self

class GetTextGenerationRequestMessages(DaraModel):
    def __init__(
        self,
        content: str = None,
        role: str = None,
    ):
        self.content = content
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.role is not None:
            result['role'] = self.role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('role') is not None:
            self.role = m.get('role')

        return self

