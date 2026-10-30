# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class QueryWithSQLResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryWithSQLResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code returned by the API operation. Valid values:
        # 
        # - Success: The request is successful.    
        # 
        # - Other values: An error code. For more information, see Error codes.
        self.code = code
        # The event trace information.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the operation is successful. Valid values:
        # 
        # - true: The operation is successful.
        # 
        # - false: The operation fails.
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
            temp_model = main_models.QueryWithSQLResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryWithSQLResponseBodyData(DaraModel):
    def __init__(
        self,
        rows: List[main_models.Row] = None,
        total: int = None,
    ):
        # The rows in the query result.
        self.rows = rows
        # The total number of entries.
        self.total = total

    def validate(self):
        if self.rows:
            for v1 in self.rows:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Rows'] = []
        if self.rows is not None:
            for k1 in self.rows:
                result['Rows'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rows = []
        if m.get('Rows') is not None:
            for k1 in m.get('Rows'):
                temp_model = main_models.Row()
                self.rows.append(temp_model.from_map(k1))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

