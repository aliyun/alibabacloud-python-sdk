# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardbx20200202 import models as main_models
from darabonba.model import DaraModel

class DescribeDistributeTableListResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeDistributeTableListResponseBodyData = None,
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
            temp_model = main_models.DescribeDistributeTableListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeDistributeTableListResponseBodyData(DaraModel):
    def __init__(
        self,
        tables: List[main_models.DescribeDistributeTableListResponseBodyDataTables] = None,
    ):
        self.tables = tables

    def validate(self):
        if self.tables:
            for v1 in self.tables:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tables'] = []
        if self.tables is not None:
            for k1 in self.tables:
                result['Tables'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tables = []
        if m.get('Tables') is not None:
            for k1 in m.get('Tables'):
                temp_model = main_models.DescribeDistributeTableListResponseBodyDataTables()
                self.tables.append(temp_model.from_map(k1))

        return self

class DescribeDistributeTableListResponseBodyDataTables(DaraModel):
    def __init__(
        self,
        db_key: str = None,
        table_name: str = None,
        table_type: str = None,
        tb_key: str = None,
    ):
        self.db_key = db_key
        self.table_name = table_name
        self.table_type = table_type
        self.tb_key = tb_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_key is not None:
            result['DbKey'] = self.db_key

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.table_type is not None:
            result['TableType'] = self.table_type

        if self.tb_key is not None:
            result['TbKey'] = self.tb_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbKey') is not None:
            self.db_key = m.get('DbKey')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('TableType') is not None:
            self.table_type = m.get('TableType')

        if m.get('TbKey') is not None:
            self.tb_key = m.get('TbKey')

        return self

