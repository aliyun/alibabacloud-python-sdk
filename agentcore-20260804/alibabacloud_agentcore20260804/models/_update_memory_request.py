# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class UpdateMemoryRequest(DaraModel):
    def __init__(
        self,
        body: main_models.UpdateMemoryRequestBody = None,
    ):
        # The update memory request.
        # 
        # This parameter is required.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = main_models.UpdateMemoryRequestBody()
            self.body = temp_model.from_map(m.get('body'))

        return self

class UpdateMemoryRequestBody(DaraModel):
    def __init__(
        self,
        metadata: Dict[str, str] = None,
        text: str = None,
    ):
        # The updated string key-value metadata. You must provide at least one of Metadata or Text. A maximum of 16 keys are allowed. The maximum length of a key is 64 characters, and the maximum length of a value is 1,024 characters.
        self.metadata = metadata
        # The updated memory text. You must provide at least one of Text or Metadata. The maximum size is 32,000 UTF-8 bytes.
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.metadata is not None:
            result['metadata'] = self.metadata

        if self.text is not None:
            result['text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('metadata') is not None:
            self.metadata = m.get('metadata')

        if m.get('text') is not None:
            self.text = m.get('text')

        return self

