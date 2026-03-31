# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PatchMemoryConfigRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        auto_update: bool = None,
        expiration_time: int = None,
        prompt: str = None,
        threshold: float = None,
        top_k: int = None,
        user_defined_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.auto_update = auto_update
        self.expiration_time = expiration_time
        self.prompt = prompt
        self.threshold = threshold
        self.top_k = top_k
        self.user_defined_id = user_defined_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.auto_update is not None:
            result['AutoUpdate'] = self.auto_update

        if self.expiration_time is not None:
            result['ExpirationTime'] = self.expiration_time

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        if self.top_k is not None:
            result['TopK'] = self.top_k

        if self.user_defined_id is not None:
            result['UserDefinedId'] = self.user_defined_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AutoUpdate') is not None:
            self.auto_update = m.get('AutoUpdate')

        if m.get('ExpirationTime') is not None:
            self.expiration_time = m.get('ExpirationTime')

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        if m.get('TopK') is not None:
            self.top_k = m.get('TopK')

        if m.get('UserDefinedId') is not None:
            self.user_defined_id = m.get('UserDefinedId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

