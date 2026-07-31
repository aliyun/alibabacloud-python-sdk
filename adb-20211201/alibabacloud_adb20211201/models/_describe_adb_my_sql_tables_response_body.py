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
        # Additional information about the call. Valid values:
        # 
        # - **Success** is returned if the request is successful.
        # 
        # - A specific error code is returned if the request fails.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The name of the database.
        self.schema = schema
        # Indicates whether the call was successful. Valid values:
        # 
        # - **true**: The call was successful.
        # 
        # - **false**: The call failed.
        self.success = success
        # Information about the tables.
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

