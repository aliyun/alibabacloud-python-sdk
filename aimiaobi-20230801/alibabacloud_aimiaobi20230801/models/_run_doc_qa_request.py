# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class RunDocQaRequest(DaraModel):
    def __init__(
        self,
        category_ids: List[str] = None,
        conversation_contexts: List[main_models.RunDocQaRequestConversationContexts] = None,
        doc_ids: List[str] = None,
        model_name: str = None,
        query: str = None,
        reference_content: str = None,
        search_source: str = None,
        session_id: str = None,
        workspace_id: str = None,
    ):
        self.category_ids = category_ids
        self.conversation_contexts = conversation_contexts
        self.doc_ids = doc_ids
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
        if self.conversation_contexts:
            for v1 in self.conversation_contexts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_ids is not None:
            result['CategoryIds'] = self.category_ids

        result['ConversationContexts'] = []
        if self.conversation_contexts is not None:
            for k1 in self.conversation_contexts:
                result['ConversationContexts'].append(k1.to_map() if k1 else None)

        if self.doc_ids is not None:
            result['DocIds'] = self.doc_ids

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
            self.category_ids = m.get('CategoryIds')

        self.conversation_contexts = []
        if m.get('ConversationContexts') is not None:
            for k1 in m.get('ConversationContexts'):
                temp_model = main_models.RunDocQaRequestConversationContexts()
                self.conversation_contexts.append(temp_model.from_map(k1))

        if m.get('DocIds') is not None:
            self.doc_ids = m.get('DocIds')

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

class RunDocQaRequestConversationContexts(DaraModel):
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
            result['Content'] = self.content

        if self.role is not None:
            result['Role'] = self.role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        return self

