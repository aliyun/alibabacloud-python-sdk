# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryRecallManagementTableRecordsRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        primary_keys: bytes = None,
        recall_management_table_version_id: str = None,
    ):
        self.instance_id = instance_id
        self.primary_keys = primary_keys
        self.recall_management_table_version_id = recall_management_table_version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.primary_keys is not None:
            result['PrimaryKeys'] = self.primary_keys

        if self.recall_management_table_version_id is not None:
            result['RecallManagementTableVersionId'] = self.recall_management_table_version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PrimaryKeys') is not None:
            self.primary_keys = m.get('PrimaryKeys')

        if m.get('RecallManagementTableVersionId') is not None:
            self.recall_management_table_version_id = m.get('RecallManagementTableVersionId')

        return self

