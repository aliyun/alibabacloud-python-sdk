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
        # The Simple Log Service (SLS) Logstore. For more information about how to query Logstores, see [ListLogStores](https://help.aliyun.com/document_detail/426970.html).
        # 
        # This parameter is required.
        self.log_store = log_store
        # The name of the Simple Log Service (SLS) project for the resource group. The project must be created in Simple Log Service in advance. This operation does not support automatic creation of the project. You can call the ListProject operation to query existing projects, or call the CreateProject operation to create a project first.
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

