# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListMaterialDocumentsShrinkRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        content: str = None,
        create_time_end: str = None,
        create_time_start: str = None,
        current: int = None,
        doc_type: str = None,
        doc_type_list_shrink: str = None,
        generate_public_url: bool = None,
        id: int = None,
        keywords_shrink: str = None,
        query: str = None,
        share_attr: int = None,
        size: int = None,
        title: str = None,
        update_time_end: str = None,
        update_time_start: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.content = content
        self.create_time_end = create_time_end
        self.create_time_start = create_time_start
        self.current = current
        self.doc_type = doc_type
        self.doc_type_list_shrink = doc_type_list_shrink
        self.generate_public_url = generate_public_url
        self.id = id
        self.keywords_shrink = keywords_shrink
        self.query = query
        self.share_attr = share_attr
        self.size = size
        self.title = title
        self.update_time_end = update_time_end
        self.update_time_start = update_time_start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.content is not None:
            result['Content'] = self.content

        if self.create_time_end is not None:
            result['CreateTimeEnd'] = self.create_time_end

        if self.create_time_start is not None:
            result['CreateTimeStart'] = self.create_time_start

        if self.current is not None:
            result['Current'] = self.current

        if self.doc_type is not None:
            result['DocType'] = self.doc_type

        if self.doc_type_list_shrink is not None:
            result['DocTypeList'] = self.doc_type_list_shrink

        if self.generate_public_url is not None:
            result['GeneratePublicUrl'] = self.generate_public_url

        if self.id is not None:
            result['Id'] = self.id

        if self.keywords_shrink is not None:
            result['Keywords'] = self.keywords_shrink

        if self.query is not None:
            result['Query'] = self.query

        if self.share_attr is not None:
            result['ShareAttr'] = self.share_attr

        if self.size is not None:
            result['Size'] = self.size

        if self.title is not None:
            result['Title'] = self.title

        if self.update_time_end is not None:
            result['UpdateTimeEnd'] = self.update_time_end

        if self.update_time_start is not None:
            result['UpdateTimeStart'] = self.update_time_start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('CreateTimeEnd') is not None:
            self.create_time_end = m.get('CreateTimeEnd')

        if m.get('CreateTimeStart') is not None:
            self.create_time_start = m.get('CreateTimeStart')

        if m.get('Current') is not None:
            self.current = m.get('Current')

        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')

        if m.get('DocTypeList') is not None:
            self.doc_type_list_shrink = m.get('DocTypeList')

        if m.get('GeneratePublicUrl') is not None:
            self.generate_public_url = m.get('GeneratePublicUrl')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Keywords') is not None:
            self.keywords_shrink = m.get('Keywords')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('ShareAttr') is not None:
            self.share_attr = m.get('ShareAttr')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('UpdateTimeEnd') is not None:
            self.update_time_end = m.get('UpdateTimeEnd')

        if m.get('UpdateTimeStart') is not None:
            self.update_time_start = m.get('UpdateTimeStart')

        return self

