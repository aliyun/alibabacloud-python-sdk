# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class DescribeTableResponseBody(DaraModel):
    def __init__(
        self,
        column_list: main_models.DescribeTableResponseBodyColumnList = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
    ):
        # The columns of the table.
        self.column_list = column_list
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The status of the operation. Valid values:
        # 
        # *   **success**
        # *   **fail**
        self.status = status

    def validate(self):
        if self.column_list:
            self.column_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column_list is not None:
            result['ColumnList'] = self.column_list.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnList') is not None:
            temp_model = main_models.DescribeTableResponseBodyColumnList()
            self.column_list = temp_model.from_map(m.get('ColumnList'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeTableResponseBodyColumnList(DaraModel):
    def __init__(
        self,
        column_list: List[main_models.ColumnMetadata] = None,
    ):
        self.column_list = column_list

    def validate(self):
        if self.column_list:
            for v1 in self.column_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ColumnList'] = []
        if self.column_list is not None:
            for k1 in self.column_list:
                result['ColumnList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.column_list = []
        if m.get('ColumnList') is not None:
            for k1 in m.get('ColumnList'):
                temp_model = main_models.ColumnMetadata()
                self.column_list.append(temp_model.from_map(k1))

        return self

