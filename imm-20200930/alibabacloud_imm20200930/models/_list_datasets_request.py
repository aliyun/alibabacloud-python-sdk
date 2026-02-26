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
        # The maximum number of datasets to return. Valid values: 0 to 200.
        # 
        # If this parameter is left empty or set to 0, 100 datasets are returned.
        self.max_results = max_results
        # The pagination token.
        # 
        # If the total number of datasets is greater than the value of MaxResults, you must specify this parameter. The list is returned in lexicographic order starting from the value of NextToken.
        # 
        # >  The first time you call this operation in a query, set this parameter to null.
        self.next_token = next_token
        # The dataset prefix.
        self.prefix = prefix
        # The name of the project. For more information, see [CreateProject](https://help.aliyun.com/document_detail/478153.html).
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

