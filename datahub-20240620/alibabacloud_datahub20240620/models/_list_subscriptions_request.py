# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSubscriptionsRequest(DaraModel):
    def __init__(
        self,
        keyword: str = None,
        max_results: int = None,
        next_token: str = None,
        project_name: str = None,
        skip: int = None,
        topic_name: str = None,
    ):
        # The keyword used to filter results in a paged query.
        self.keyword = keyword
        # The maximum number of records to return for a paged query.
        self.max_results = max_results
        # The pagination token. If NextToken is empty, paged query starts from the beginning. Otherwise, paged query starts from the end of the previous query indicated by the token.
        self.next_token = next_token
        # The project name.
        # 
        # This parameter is required.
        self.project_name = project_name
        # The number of records to skip in a paged query.
        self.skip = skip
        # The topic name.
        # 
        # This parameter is required.
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.skip is not None:
            result['Skip'] = self.skip

        if self.topic_name is not None:
            result['TopicName'] = self.topic_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('Skip') is not None:
            self.skip = m.get('Skip')

        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')

        return self

