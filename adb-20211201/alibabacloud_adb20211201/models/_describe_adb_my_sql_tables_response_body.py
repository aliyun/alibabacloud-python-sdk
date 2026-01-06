# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeAdbMySqlTablesResponseBody(DaraModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        schema: str = None,
        success: bool = None,
        tables: List[str] = None,
    ):
        # The message returned for the operation. Valid values:
        # 
        # *   **Success** is returned if the operation is successful.
        # *   An error message is returned if the operation fails.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # The name of the database.
        self.schema = schema
        # Indicates whether the operation is successful. Valid values:
        # 
        # *   **true**: The operation is successful.
        # *   **false**: The operation fails.
        self.success = success
        # The names of tables.
        self.tables = tables

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.schema is not None:
            result['Schema'] = self.schema

        if self.success is not None:
            result['Success'] = self.success

        if self.tables is not None:
            result['Tables'] = self.tables

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Schema') is not None:
            self.schema = m.get('Schema')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Tables') is not None:
            self.tables = m.get('Tables')

        return self

