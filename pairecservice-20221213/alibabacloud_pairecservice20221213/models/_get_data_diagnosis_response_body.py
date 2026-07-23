# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDataDiagnosisResponseBody(DaraModel):
    def __init__(
        self,
        config: str = None,
        cycle_time: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        left_table_meta_id: str = None,
        left_table_partition_field: str = None,
        name: str = None,
        partition_field: str = None,
        request_id: str = None,
        right_table_meta_id: str = None,
        right_table_partition_field: str = None,
        table_meta_id: str = None,
        table_meta_name: str = None,
        top_nquantity: int = None,
        type: str = None,
    ):
        # The configuration of the data diagnosis task.
        self.config = config
        # The time for periodic execution. If this field is empty, the task does not execute periodically.
        self.cycle_time = cycle_time
        # The creation time.
        self.gmt_create_time = gmt_create_time
        # The modification time.
        self.gmt_modified_time = gmt_modified_time
        # The ID of the left data table.
        self.left_table_meta_id = left_table_meta_id
        # The partition field of the left data table.
        self.left_table_partition_field = left_table_partition_field
        # The name of the data diagnosis task.
        self.name = name
        # The partition field.
        self.partition_field = partition_field
        # The request ID.
        self.request_id = request_id
        # The ID of the right data table.
        self.right_table_meta_id = right_table_meta_id
        # The partition field of the right data table.
        self.right_table_partition_field = right_table_partition_field
        # The ID of the data table.
        self.table_meta_id = table_meta_id
        # The name of the data table.
        self.table_meta_name = table_meta_name
        # The Top-N quantity.
        self.top_nquantity = top_nquantity
        # The type of the data diagnosis task.
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

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.left_table_meta_id is not None:
            result['LeftTableMetaId'] = self.left_table_meta_id

        if self.left_table_partition_field is not None:
            result['LeftTablePartitionField'] = self.left_table_partition_field

        if self.name is not None:
            result['Name'] = self.name

        if self.partition_field is not None:
            result['PartitionField'] = self.partition_field

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.right_table_meta_id is not None:
            result['RightTableMetaId'] = self.right_table_meta_id

        if self.right_table_partition_field is not None:
            result['RightTablePartitionField'] = self.right_table_partition_field

        if self.table_meta_id is not None:
            result['TableMetaId'] = self.table_meta_id

        if self.table_meta_name is not None:
            result['TableMetaName'] = self.table_meta_name

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

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('LeftTableMetaId') is not None:
            self.left_table_meta_id = m.get('LeftTableMetaId')

        if m.get('LeftTablePartitionField') is not None:
            self.left_table_partition_field = m.get('LeftTablePartitionField')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PartitionField') is not None:
            self.partition_field = m.get('PartitionField')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RightTableMetaId') is not None:
            self.right_table_meta_id = m.get('RightTableMetaId')

        if m.get('RightTablePartitionField') is not None:
            self.right_table_partition_field = m.get('RightTablePartitionField')

        if m.get('TableMetaId') is not None:
            self.table_meta_id = m.get('TableMetaId')

        if m.get('TableMetaName') is not None:
            self.table_meta_name = m.get('TableMetaName')

        if m.get('TopNQuantity') is not None:
            self.top_nquantity = m.get('TopNQuantity')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

