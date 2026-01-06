# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeDiagnosisSQLInfoResponseBody(DaraModel):
    def __init__(
        self,
        diagnosis_sqlinfo: str = None,
        request_id: str = None,
        stage_infos: List[main_models.DescribeDiagnosisSQLInfoResponseBodyStageInfos] = None,
    ):
        # The queried execution information, including the SQL statement, statistics, execution plan, and operator information.
        self.diagnosis_sqlinfo = diagnosis_sqlinfo
        # The request ID.
        self.request_id = request_id
        # The queried execution information by stage.
        self.stage_infos = stage_infos

    def validate(self):
        if self.stage_infos:
            for v1 in self.stage_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.diagnosis_sqlinfo is not None:
            result['DiagnosisSQLInfo'] = self.diagnosis_sqlinfo

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['StageInfos'] = []
        if self.stage_infos is not None:
            for k1 in self.stage_infos:
                result['StageInfos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiagnosisSQLInfo') is not None:
            self.diagnosis_sqlinfo = m.get('DiagnosisSQLInfo')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.stage_infos = []
        if m.get('StageInfos') is not None:
            for k1 in m.get('StageInfos'):
                temp_model = main_models.DescribeDiagnosisSQLInfoResponseBodyStageInfos()
                self.stage_infos.append(temp_model.from_map(k1))

        return self

class DescribeDiagnosisSQLInfoResponseBodyStageInfos(DaraModel):
    def __init__(
        self,
        execution_type: str = None,
        input_data_size: int = None,
        input_rows: int = None,
        operator_cost: int = None,
        output_data_size: int = None,
        output_rows: int = None,
        peak_memory: int = None,
        progress: float = None,
        stage_id: str = None,
        state: str = None,
    ):
        self.execution_type = execution_type
        # The total amount of input data in the stage. Unit: bytes.
        self.input_data_size = input_data_size
        # The total number of input rows in the stage.
        self.input_rows = input_rows
        # The total amount of time consumed by all operators in the stage. Unit: milliseconds.
        self.operator_cost = operator_cost
        # The total amount of output data in the stage. Unit: bytes.
        self.output_data_size = output_data_size
        # The total number of output rows in the stage.
        self.output_rows = output_rows
        # The total peak memory of the stage. Unit: bytes.
        self.peak_memory = peak_memory
        # The execution progress of the stage.
        self.progress = progress
        # The stage ID.
        self.stage_id = stage_id
        # The state of the stage.
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.execution_type is not None:
            result['ExecutionType'] = self.execution_type

        if self.input_data_size is not None:
            result['InputDataSize'] = self.input_data_size

        if self.input_rows is not None:
            result['InputRows'] = self.input_rows

        if self.operator_cost is not None:
            result['OperatorCost'] = self.operator_cost

        if self.output_data_size is not None:
            result['OutputDataSize'] = self.output_data_size

        if self.output_rows is not None:
            result['OutputRows'] = self.output_rows

        if self.peak_memory is not None:
            result['PeakMemory'] = self.peak_memory

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.stage_id is not None:
            result['StageId'] = self.stage_id

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutionType') is not None:
            self.execution_type = m.get('ExecutionType')

        if m.get('InputDataSize') is not None:
            self.input_data_size = m.get('InputDataSize')

        if m.get('InputRows') is not None:
            self.input_rows = m.get('InputRows')

        if m.get('OperatorCost') is not None:
            self.operator_cost = m.get('OperatorCost')

        if m.get('OutputDataSize') is not None:
            self.output_data_size = m.get('OutputDataSize')

        if m.get('OutputRows') is not None:
            self.output_rows = m.get('OutputRows')

        if m.get('PeakMemory') is not None:
            self.peak_memory = m.get('PeakMemory')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('StageId') is not None:
            self.stage_id = m.get('StageId')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

