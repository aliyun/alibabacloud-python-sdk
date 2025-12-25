# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RunSearchSimilarArticlesShrinkRequest(DaraModel):
    def __init__(
        self,
        chat_config_shrink: str = None,
        doc_type: str = None,
        title: str = None,
        url: str = None,
        workspace_id: str = None,
    ):
        self.chat_config_shrink = chat_config_shrink
        self.doc_type = doc_type
        self.title = title
        # This parameter is required.
        self.url = url
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chat_config_shrink is not None:
            result['ChatConfig'] = self.chat_config_shrink

        if self.doc_type is not None:
            result['DocType'] = self.doc_type

        if self.title is not None:
            result['Title'] = self.title

        if self.url is not None:
            result['Url'] = self.url

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChatConfig') is not None:
            self.chat_config_shrink = m.get('ChatConfig')

        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

