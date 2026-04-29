# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class ExportRecallManagementTableRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        maxcompute_project_name: str = None,
        maxcompute_schema: str = None,
        maxcompute_table_name: str = None,
        partitions: Dict[str, str] = None,
    ):
        self.instance_id = instance_id
        self.maxcompute_project_name = maxcompute_project_name
        # maxcompute schema。
        self.maxcompute_schema = maxcompute_schema
        self.maxcompute_table_name = maxcompute_table_name
        self.partitions = partitions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.maxcompute_project_name is not None:
            result['MaxcomputeProjectName'] = self.maxcompute_project_name

        if self.maxcompute_schema is not None:
            result['MaxcomputeSchema'] = self.maxcompute_schema

        if self.maxcompute_table_name is not None:
            result['MaxcomputeTableName'] = self.maxcompute_table_name

        if self.partitions is not None:
            result['Partitions'] = self.partitions

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MaxcomputeProjectName') is not None:
            self.maxcompute_project_name = m.get('MaxcomputeProjectName')

        if m.get('MaxcomputeSchema') is not None:
            self.maxcompute_schema = m.get('MaxcomputeSchema')

        if m.get('MaxcomputeTableName') is not None:
            self.maxcompute_table_name = m.get('MaxcomputeTableName')

        if m.get('Partitions') is not None:
            self.partitions = m.get('Partitions')

        return self

