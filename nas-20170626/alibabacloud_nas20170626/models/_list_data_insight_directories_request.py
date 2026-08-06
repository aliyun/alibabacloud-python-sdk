# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDataInsightDirectoriesRequest(DaraModel):
    def __init__(
        self,
        file_system_id: str = None,
        max_results: int = None,
        next_token: str = None,
        parent_dir: str = None,
    ):
        # This parameter is required.
        self.file_system_id = file_system_id
        self.max_results = max_results
        self.next_token = next_token
        self.parent_dir = parent_dir

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.parent_dir is not None:
            result['ParentDir'] = self.parent_dir

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ParentDir') is not None:
            self.parent_dir = m.get('ParentDir')

        return self

