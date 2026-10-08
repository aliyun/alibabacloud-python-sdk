# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDatasetsRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        prefix: str = None,
        project_name: str = None,
    ):
        # The maximum number of datasets to return. Valid values: 0 to 200. If you do not specify this parameter or set it to 0, the default value 100 is used.
        self.max_results = max_results
        # The pagination token.
        # 
        # If the total number of datasets exceeds the value of MaxResults, this token is used for pagination. The list of dataset information is returned in lexicographical order starting from NextToken.
        # 
        # > When you call this operation for the first time in a query, leave this parameter empty.
        self.next_token = next_token
        # The prefix of the dataset name.
        self.prefix = prefix
        # The name of the project. For more information about how to obtain the project name, see [Create a project](https://help.aliyun.com/document_detail/478153.html).
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

        if self.prefix is not None:
            result['Prefix'] = self.prefix

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        return self

