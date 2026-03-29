# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDataDiagnosisRequest(DaraModel):
    def __init__(
        self,
        config: str = None,
        cycle_time: str = None,
        instance_id: str = None,
        left_table_meta_id: str = None,
        left_table_partition_field: str = None,
        name: str = None,
        partition_field: str = None,
        right_table_meta_id: str = None,
        right_table_partition_field: str = None,
        table_meta_id: str = None,
        top_nquantity: int = None,
        type: str = None,
    ):
        # This parameter is required.
        self.config = config
        self.cycle_time = cycle_time
        # This parameter is required.
        self.instance_id = instance_id
        self.left_table_meta_id = left_table_meta_id
        self.left_table_partition_field = left_table_partition_field
        # This parameter is required.
        self.name = name
        self.partition_field = partition_field
        self.right_table_meta_id = right_table_meta_id
        self.right_table_partition_field = right_table_partition_field
        self.table_meta_id = table_meta_id
        self.top_nquantity = top_nquantity
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.cycle_time is not None:
            result['CycleTime'] = self.cycle_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.left_table_meta_id is not None:
            result['LeftTableMetaId'] = self.left_table_meta_id

        if self.left_table_partition_field is not None:
            result['LeftTablePartitionField'] = self.left_table_partition_field

        if self.name is not None:
            result['Name'] = self.name

        if self.partition_field is not None:
            result['PartitionField'] = self.partition_field

        if self.right_table_meta_id is not None:
            result['RightTableMetaId'] = self.right_table_meta_id

        if self.right_table_partition_field is not None:
            result['RightTablePartitionField'] = self.right_table_partition_field

        if self.table_meta_id is not None:
            result['TableMetaId'] = self.table_meta_id

        if self.top_nquantity is not None:
            result['TopNQuantity'] = self.top_nquantity

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('CycleTime') is not None:
            self.cycle_time = m.get('CycleTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LeftTableMetaId') is not None:
            self.left_table_meta_id = m.get('LeftTableMetaId')

        if m.get('LeftTablePartitionField') is not None:
            self.left_table_partition_field = m.get('LeftTablePartitionField')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PartitionField') is not None:
            self.partition_field = m.get('PartitionField')

        if m.get('RightTableMetaId') is not None:
            self.right_table_meta_id = m.get('RightTableMetaId')

        if m.get('RightTablePartitionField') is not None:
            self.right_table_partition_field = m.get('RightTablePartitionField')

        if m.get('TableMetaId') is not None:
            self.table_meta_id = m.get('TableMetaId')

        if m.get('TopNQuantity') is not None:
            self.top_nquantity = m.get('TopNQuantity')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

