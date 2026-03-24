# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDocShrinkRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        category_id: int = None,
        config: str = None,
        content: str = None,
        doc_metadata_shrink: str = None,
        doc_name: str = None,
        end_date: str = None,
        knowledge_id: int = None,
        meta: str = None,
        start_date: str = None,
        tag_ids_shrink: str = None,
        title: str = None,
    ):
        self.agent_key = agent_key
        self.category_id = category_id
        self.config = config
        self.content = content
        self.doc_metadata_shrink = doc_metadata_shrink
        self.doc_name = doc_name
        self.end_date = end_date
        # This parameter is required.
        self.knowledge_id = knowledge_id
        self.meta = meta
        self.start_date = start_date
        self.tag_ids_shrink = tag_ids_shrink
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.config is not None:
            result['Config'] = self.config

        if self.content is not None:
            result['Content'] = self.content

        if self.doc_metadata_shrink is not None:
            result['DocMetadata'] = self.doc_metadata_shrink

        if self.doc_name is not None:
            result['DocName'] = self.doc_name

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id

        if self.meta is not None:
            result['Meta'] = self.meta

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.tag_ids_shrink is not None:
            result['TagIds'] = self.tag_ids_shrink

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('DocMetadata') is not None:
            self.doc_metadata_shrink = m.get('DocMetadata')

        if m.get('DocName') is not None:
            self.doc_name = m.get('DocName')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')

        if m.get('Meta') is not None:
            self.meta = m.get('Meta')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('TagIds') is not None:
            self.tag_ids_shrink = m.get('TagIds')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

