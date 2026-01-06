# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteSparkTemplateRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        id: int = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Lakehouse Edition cluster.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The directory ID or application ID of the template files that you want to delete.
        # 
        # > 
        # 
        # *   You can call the [GetSparkTemplateFullTree](https://help.aliyun.com/document_detail/612467.html) operation to query the directory ID or application ID.
        # 
        # *   When you specify a directory ID, the directory and all template files that are included in the directory are deleted.
        # 
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

