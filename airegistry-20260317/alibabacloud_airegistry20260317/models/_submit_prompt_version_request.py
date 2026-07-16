# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitPromptVersionRequest(DaraModel):
    def __init__(
        self,
        namespace_id: str = None,
        prompt_key: str = None,
        prompt_version: str = None,
    ):
        # This parameter is required.
        self.namespace_id = namespace_id
        # This parameter is required.
        self.prompt_key = prompt_key
        self.prompt_version = prompt_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.prompt_key is not None:
            result['PromptKey'] = self.prompt_key

        if self.prompt_version is not None:
            result['PromptVersion'] = self.prompt_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('PromptKey') is not None:
            self.prompt_key = m.get('PromptKey')

        if m.get('PromptVersion') is not None:
            self.prompt_version = m.get('PromptVersion')

        return self

