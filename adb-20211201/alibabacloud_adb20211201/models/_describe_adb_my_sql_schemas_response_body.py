# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeAdbMySqlSchemasResponseBody(DaraModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        schemas: List[str] = None,
        success: bool = None,
    ):
        # The returned message.
        # 
        # *   If the request was successful, a **success** message is returned.
        # *   If the request failed, an error message is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The queried databases.
        self.schemas = schemas
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success

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

        if self.schemas is not None:
            result['Schemas'] = self.schemas

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Schemas') is not None:
            self.schemas = m.get('Schemas')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

