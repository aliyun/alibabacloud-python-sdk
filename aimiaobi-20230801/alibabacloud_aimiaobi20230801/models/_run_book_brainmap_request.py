# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RunBookBrainmapRequest(DaraModel):
    def __init__(
        self,
        clean_cache: bool = None,
        doc_id: str = None,
        node_number: int = None,
        prompt: str = None,
        session_id: str = None,
        word_number: int = None,
        workspace_id: str = None,
    ):
        self.clean_cache = clean_cache
        # This parameter is required.
        self.doc_id = doc_id
        self.node_number = node_number
        self.prompt = prompt
        # This parameter is required.
        self.session_id = session_id
        self.word_number = word_number
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.clean_cache is not None:
            result['CleanCache'] = self.clean_cache

        if self.doc_id is not None:
            result['DocId'] = self.doc_id

        if self.node_number is not None:
            result['NodeNumber'] = self.node_number

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.word_number is not None:
            result['WordNumber'] = self.word_number

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CleanCache') is not None:
            self.clean_cache = m.get('CleanCache')

        if m.get('DocId') is not None:
            self.doc_id = m.get('DocId')

        if m.get('NodeNumber') is not None:
            self.node_number = m.get('NodeNumber')

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('WordNumber') is not None:
            self.word_number = m.get('WordNumber')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

