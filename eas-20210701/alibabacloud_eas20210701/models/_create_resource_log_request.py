# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateResourceLogRequest(DaraModel):
    def __init__(
        self,
        log_store: str = None,
        project_name: str = None,
    ):
        # The Logstore of Log Service. For more information about how to query a Logstore, see [ListLogStores](https://help.aliyun.com/document_detail/426970.html).
        # 
        # This parameter is required.
        self.log_store = log_store
        # The Log Service project that is associated with the resource group. For more information about how to query the project, see [ListProject](https://help.aliyun.com/document_detail/74955.html).
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
        if self.log_store is not None:
            result['LogStore'] = self.log_store

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogStore') is not None:
            self.log_store = m.get('LogStore')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        return self

