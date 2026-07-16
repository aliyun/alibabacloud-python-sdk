# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListGeneratedContentsRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        content_domain: str = None,
        current: int = None,
        data_type: str = None,
        end_time: str = None,
        query: str = None,
        size: int = None,
        start_time: str = None,
        task_id: str = None,
        title: str = None,
    ):
        # Workspace ID: [AgentKey](https://help.aliyun.com/document_detail/2587494.html)
        # 
        # This parameter is required.
        self.agent_key = agent_key
        # Content domain (content category)
        # 
        # - media: Media writing
        # 
        # - government: Government document writing
        # 
        # - office: Office writing
        # 
        # - market: Marketing writing
        # 
        # - custom: Custom writing
        # 
        # - commentGenerate: Opinion generation
        self.content_domain = content_domain
        # Page number
        self.current = current
        # Data type filter
        # 
        # - plainText: Plain text
        # 
        # - richText: Rich text
        # 
        # - html: HTML
        # 
        # - pdf: PDF
        # 
        # - word: Word
        # 
        # - excel: Excel
        # 
        # - csv: CSV
        # 
        # - image: Image
        # 
        # - video: Video
        # 
        # - audio: Audio
        self.data_type = data_type
        # End time
        self.end_time = end_time
        # Search keyword: Supports fuzzy search on titles and content
        self.query = query
        # Items per page. Default is 10.
        self.size = size
        # Start time
        self.start_time = start_time
        # Task ID
        # 
        # > You do not need to specify TaskId. The system generates it automatically. If you use the same TaskId for multiple tasks, those tasks belong to the same conversation.
        self.task_id = task_id
        # Title text
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

        if self.content_domain is not None:
            result['ContentDomain'] = self.content_domain

        if self.current is not None:
            result['Current'] = self.current

        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.query is not None:
            result['Query'] = self.query

        if self.size is not None:
            result['Size'] = self.size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('ContentDomain') is not None:
            self.content_domain = m.get('ContentDomain')

        if m.get('Current') is not None:
            self.current = m.get('Current')

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

