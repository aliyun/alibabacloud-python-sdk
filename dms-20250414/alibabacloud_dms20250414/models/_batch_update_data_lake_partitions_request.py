# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class BatchUpdateDataLakePartitionsRequest(DaraModel):
    def __init__(
        self,
        catalog_name: str = None,
        db_name: str = None,
        partition_inputs: List[main_models.DLPartitionInput] = None,
        table_name: str = None,
        tid: int = None,
        workspace_id: int = None,
    ):
        # This parameter is required.
        self.catalog_name = catalog_name
        # This parameter is required.
        self.db_name = db_name
        # This parameter is required.
        self.partition_inputs = partition_inputs
        # This parameter is required.
        self.table_name = table_name
        self.tid = tid
        self.workspace_id = workspace_id

    def validate(self):
        if self.partition_inputs:
            for v1 in self.partition_inputs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name

        if self.db_name is not None:
            result['DbName'] = self.db_name

        result['PartitionInputs'] = []
        if self.partition_inputs is not None:
            for k1 in self.partition_inputs:
                result['PartitionInputs'].append(k1.to_map() if k1 else None)

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.tid is not None:
            result['Tid'] = self.tid

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')

        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        self.partition_inputs = []
        if m.get('PartitionInputs') is not None:
            for k1 in m.get('PartitionInputs'):
                temp_model = main_models.DLPartitionInput()
                self.partition_inputs.append(temp_model.from_map(k1))

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

