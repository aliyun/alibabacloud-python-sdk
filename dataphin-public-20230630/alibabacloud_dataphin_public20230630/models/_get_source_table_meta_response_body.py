# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetSourceTableMetaResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetSourceTableMetaResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetSourceTableMetaResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetSourceTableMetaResponseBodyData(DaraModel):
    def __init__(
        self,
        columns: List[main_models.GetSourceTableMetaResponseBodyDataColumns] = None,
        guid: str = None,
        table_comment: str = None,
        table_name: str = None,
    ):
        self.columns = columns
        self.guid = guid
        self.table_comment = table_comment
        self.table_name = table_name

    def validate(self):
        if self.columns:
            for v1 in self.columns:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Columns'] = []
        if self.columns is not None:
            for k1 in self.columns:
                result['Columns'].append(k1.to_map() if k1 else None)

        if self.guid is not None:
            result['Guid'] = self.guid

        if self.table_comment is not None:
            result['TableComment'] = self.table_comment

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.columns = []
        if m.get('Columns') is not None:
            for k1 in m.get('Columns'):
                temp_model = main_models.GetSourceTableMetaResponseBodyDataColumns()
                self.columns.append(temp_model.from_map(k1))

        if m.get('Guid') is not None:
            self.guid = m.get('Guid')

        if m.get('TableComment') is not None:
            self.table_comment = m.get('TableComment')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

class GetSourceTableMetaResponseBodyDataColumns(DaraModel):
    def __init__(
        self,
        comment: str = None,
        data_type: str = None,
        name: str = None,
        pk: bool = None,
        pt: bool = None,
        raw_data_type: str = None,
        seq_number: int = None,
    ):
        self.comment = comment
        self.data_type = data_type
        self.name = name
        self.pk = pk
        self.pt = pt
        self.raw_data_type = raw_data_type
        self.seq_number = seq_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.name is not None:
            result['Name'] = self.name

        if self.pk is not None:
            result['Pk'] = self.pk

        if self.pt is not None:
            result['Pt'] = self.pt

        if self.raw_data_type is not None:
            result['RawDataType'] = self.raw_data_type

        if self.seq_number is not None:
            result['SeqNumber'] = self.seq_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Pk') is not None:
            self.pk = m.get('Pk')

        if m.get('Pt') is not None:
            self.pt = m.get('Pt')

        if m.get('RawDataType') is not None:
            self.raw_data_type = m.get('RawDataType')

        if m.get('SeqNumber') is not None:
            self.seq_number = m.get('SeqNumber')

        return self

