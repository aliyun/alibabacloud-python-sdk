# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAttachedOSSBucketsRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        project_name: str = None,
    ):
        # The maximum number of tasks in the returned result list. The value range is (0, 200], with a default value of 100.
        self.max_results = max_results
        # Pagination token.
        # 
        # When the total number of files exceeds the set MaxResults, this token is used for pagination. It returns the list of file information in lexicographical order starting from NextToken.
        # 
        # > When calling this interface for the first time in a single query, set this value to empty.
        self.next_token = next_token
        # Project name, for more information on how to obtain it, see [Create Project](https://help.aliyun.com/document_detail/478153.html).
        # 
        # This parameter is required.
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        return self

