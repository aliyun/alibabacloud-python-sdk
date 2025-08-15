# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_dlfnext20250310 import models as main_models
from darabonba.model import DaraModel

class IcebergTableMetadata(DaraModel):
    def __init__(
        self,
        current_snapshot: main_models.IcebergSnapshot = None,
        fields: List[main_models.IcebergNestedField] = None,
        partition_fields: List[main_models.IcebergPartitionField] = None,
        properties: Dict[str, str] = None,
    ):
        self.current_snapshot = current_snapshot
        self.fields = fields
        self.partition_fields = partition_fields
        self.properties = properties

    def validate(self):
        if self.current_snapshot:
            self.current_snapshot.validate()
        if self.fields:
            for v1 in self.fields:
                 if v1:
                    v1.validate()
        if self.partition_fields:
            for v1 in self.partition_fields:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_snapshot is not None:
            result['currentSnapshot'] = self.current_snapshot.to_map()

        result['fields'] = []
        if self.fields is not None:
            for k1 in self.fields:
                result['fields'].append(k1.to_map() if k1 else None)

        result['partitionFields'] = []
        if self.partition_fields is not None:
            for k1 in self.partition_fields:
                result['partitionFields'].append(k1.to_map() if k1 else None)

        if self.properties is not None:
            result['properties'] = self.properties

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentSnapshot') is not None:
            temp_model = main_models.IcebergSnapshot()
            self.current_snapshot = temp_model.from_map(m.get('currentSnapshot'))

        self.fields = []
        if m.get('fields') is not None:
            for k1 in m.get('fields'):
                temp_model = main_models.IcebergNestedField()
                self.fields.append(temp_model.from_map(k1))

        self.partition_fields = []
        if m.get('partitionFields') is not None:
            for k1 in m.get('partitionFields'):
                temp_model = main_models.IcebergPartitionField()
                self.partition_fields.append(temp_model.from_map(k1))

        if m.get('properties') is not None:
            self.properties = m.get('properties')

        return self

