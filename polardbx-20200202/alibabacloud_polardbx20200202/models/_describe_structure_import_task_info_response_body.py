# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_polardbx20200202 import models as main_models
from darabonba.model import DaraModel

class DescribeStructureImportTaskInfoResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeStructureImportTaskInfoResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeStructureImportTaskInfoResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeStructureImportTaskInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        slink_stage: str = None,
        structure_import_result: main_models.DescribeStructureImportTaskInfoResponseBodyDataStructureImportResult = None,
    ):
        self.slink_stage = slink_stage
        self.structure_import_result = structure_import_result

    def validate(self):
        if self.structure_import_result:
            self.structure_import_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.slink_stage is not None:
            result['SlinkStage'] = self.slink_stage

        if self.structure_import_result is not None:
            result['StructureImportResult'] = self.structure_import_result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SlinkStage') is not None:
            self.slink_stage = m.get('SlinkStage')

        if m.get('StructureImportResult') is not None:
            temp_model = main_models.DescribeStructureImportTaskInfoResponseBodyDataStructureImportResult()
            self.structure_import_result = temp_model.from_map(m.get('StructureImportResult'))

        return self

class DescribeStructureImportTaskInfoResponseBodyDataStructureImportResult(DaraModel):
    def __init__(
        self,
        exception_detail: str = None,
        exception_full_table_name: str = None,
        finished_num: int = None,
        percentage: int = None,
        status: str = None,
        total_num: int = None,
    ):
        self.exception_detail = exception_detail
        self.exception_full_table_name = exception_full_table_name
        self.finished_num = finished_num
        self.percentage = percentage
        self.status = status
        self.total_num = total_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exception_detail is not None:
            result['ExceptionDetail'] = self.exception_detail

        if self.exception_full_table_name is not None:
            result['ExceptionFullTableName'] = self.exception_full_table_name

        if self.finished_num is not None:
            result['FinishedNum'] = self.finished_num

        if self.percentage is not None:
            result['Percentage'] = self.percentage

        if self.status is not None:
            result['Status'] = self.status

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExceptionDetail') is not None:
            self.exception_detail = m.get('ExceptionDetail')

        if m.get('ExceptionFullTableName') is not None:
            self.exception_full_table_name = m.get('ExceptionFullTableName')

        if m.get('FinishedNum') is not None:
            self.finished_num = m.get('FinishedNum')

        if m.get('Percentage') is not None:
            self.percentage = m.get('Percentage')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        return self

