# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SqlFile(DaraModel):
    def __init__(
        self,
        batch_mode: str = None,
        description: str = None,
        name: str = None,
        namespace: str = None,
        parent_id: str = None,
        session_cluster_name: str = None,
        sql_file_id: str = None,
        sql_script: str = None,
        workspace: str = None,
    ):
        self.batch_mode = batch_mode
        self.description = description
        self.name = name
        self.namespace = namespace
        self.parent_id = parent_id
        self.session_cluster_name = session_cluster_name
        self.sql_file_id = sql_file_id
        self.sql_script = sql_script
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_mode is not None:
            result['batchMode'] = self.batch_mode

        if self.description is not None:
            result['description'] = self.description

        if self.name is not None:
            result['name'] = self.name

        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.parent_id is not None:
            result['parentId'] = self.parent_id

        if self.session_cluster_name is not None:
            result['sessionClusterName'] = self.session_cluster_name

        if self.sql_file_id is not None:
            result['sqlFileId'] = self.sql_file_id

        if self.sql_script is not None:
            result['sqlScript'] = self.sql_script

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('batchMode') is not None:
            self.batch_mode = m.get('batchMode')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')

        if m.get('sessionClusterName') is not None:
            self.session_cluster_name = m.get('sessionClusterName')

        if m.get('sqlFileId') is not None:
            self.sql_file_id = m.get('sqlFileId')

        if m.get('sqlScript') is not None:
            self.sql_script = m.get('sqlScript')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

