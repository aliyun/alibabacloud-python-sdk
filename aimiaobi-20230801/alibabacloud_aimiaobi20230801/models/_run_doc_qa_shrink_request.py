# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RunDocQaShrinkRequest(DaraModel):
    def __init__(
        self,
        category_ids_shrink: str = None,
        conversation_contexts_shrink: str = None,
        doc_ids_shrink: str = None,
        model_name: str = None,
        query: str = None,
        reference_content: str = None,
        search_source: str = None,
        session_id: str = None,
        workspace_id: str = None,
    ):
        self.category_ids_shrink = category_ids_shrink
        self.conversation_contexts_shrink = conversation_contexts_shrink
        self.doc_ids_shrink = doc_ids_shrink
        self.model_name = model_name
        # This parameter is required.
        self.query = query
        self.reference_content = reference_content
        # This parameter is required.
        self.search_source = search_source
        # This parameter is required.
        self.session_id = session_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_ids_shrink is not None:
            result['CategoryIds'] = self.category_ids_shrink

        if self.conversation_contexts_shrink is not None:
            result['ConversationContexts'] = self.conversation_contexts_shrink

        if self.doc_ids_shrink is not None:
            result['DocIds'] = self.doc_ids_shrink

        if self.model_name is not None:
            result['ModelName'] = self.model_name

        if self.query is not None:
            result['Query'] = self.query

        if self.reference_content is not None:
            result['ReferenceContent'] = self.reference_content

        if self.search_source is not None:
            result['SearchSource'] = self.search_source

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryIds') is not None:
            self.category_ids_shrink = m.get('CategoryIds')

        if m.get('ConversationContexts') is not None:
            self.conversation_contexts_shrink = m.get('ConversationContexts')

        if m.get('DocIds') is not None:
            self.doc_ids_shrink = m.get('DocIds')

        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('ReferenceContent') is not None:
            self.reference_content = m.get('ReferenceContent')

        if m.get('SearchSource') is not None:
            self.search_source = m.get('SearchSource')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

