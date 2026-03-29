# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pairecservice20221213 import models as main_models
from darabonba.model import DaraModel

class ListDataDiagnosesResponseBody(DaraModel):
    def __init__(
        self,
        data_diagnoses: List[main_models.ListDataDiagnosesResponseBodyDataDiagnoses] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.data_diagnoses = data_diagnoses
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.data_diagnoses:
            for v1 in self.data_diagnoses:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataDiagnoses'] = []
        if self.data_diagnoses is not None:
            for k1 in self.data_diagnoses:
                result['DataDiagnoses'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_diagnoses = []
        if m.get('DataDiagnoses') is not None:
            for k1 in m.get('DataDiagnoses'):
                temp_model = main_models.ListDataDiagnosesResponseBodyDataDiagnoses()
                self.data_diagnoses.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListDataDiagnosesResponseBodyDataDiagnoses(DaraModel):
    def __init__(
        self,
        config: str = None,
        cycle_time: str = None,
        data_diagnosis_id: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        left_table_meta_id: str = None,
        left_table_partition_field: str = None,
        name: str = None,
        partition_field: str = None,
        right_table_meta_id: str = None,
        right_table_partition_field: str = None,
        table_meta_id: str = None,
        table_meta_name: str = None,
        top_nquantity: int = None,
        type: str = None,
    ):
        self.config = config
        self.cycle_time = cycle_time
        self.data_diagnosis_id = data_diagnosis_id
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.left_table_meta_id = left_table_meta_id
        self.left_table_partition_field = left_table_partition_field
        self.name = name
        self.partition_field = partition_field
        self.right_table_meta_id = right_table_meta_id
        self.right_table_partition_field = right_table_partition_field
        self.table_meta_id = table_meta_id
        self.table_meta_name = table_meta_name
        self.top_nquantity = top_nquantity
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

        if self.data_diagnosis_id is not None:
            result['DataDiagnosisId'] = self.data_diagnosis_id

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

        if m.get('DataDiagnosisId') is not None:
            self.data_diagnosis_id = m.get('DataDiagnosisId')

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

