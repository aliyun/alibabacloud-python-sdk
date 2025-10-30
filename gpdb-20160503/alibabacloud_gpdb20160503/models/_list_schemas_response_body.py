# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class ListSchemasResponseBody(DaraModel):
    def __init__(
        self,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        schemas: main_models.ListSchemasResponseBodySchemas = None,
        status: str = None,
    ):
        # The returned message.
        self.message = message
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The queried schemas.
        self.schemas = schemas
        # The status of the operation. Valid values:
        # 
        # *   **success**
        # *   **fail**
        self.status = status

    def validate(self):
        if self.schemas:
            self.schemas.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['Message'] = self.message

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.schemas is not None:
            result['Schemas'] = self.schemas.to_map()

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Schemas') is not None:
            temp_model = main_models.ListSchemasResponseBodySchemas()
            self.schemas = temp_model.from_map(m.get('Schemas'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ListSchemasResponseBodySchemas(DaraModel):
    def __init__(
        self,
        schemas: List[str] = None,
    ):
        self.schemas = schemas

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.schemas is not None:
            result['Schemas'] = self.schemas

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Schemas') is not None:
            self.schemas = m.get('Schemas')

        return self

