# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListKnowledgeTagsRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        file_location: str = None,
    ):
        # The ID of the AnalyticDB for MySQL instance.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The location of the knowledge base document.
        # 
        # This parameter is required.
        self.file_location = file_location

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.file_location is not None:
            result['FileLocation'] = self.file_location

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('FileLocation') is not None:
            self.file_location = m.get('FileLocation')

        return self

