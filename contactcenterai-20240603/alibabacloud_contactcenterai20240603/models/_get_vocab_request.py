# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetVocabRequest(DaraModel):
    def __init__(
        self,
        vocabulary_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.vocabulary_id = vocabulary_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.vocabulary_id is not None:
            result['vocabularyId'] = self.vocabulary_id

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('vocabularyId') is not None:
            self.vocabulary_id = m.get('vocabularyId')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

