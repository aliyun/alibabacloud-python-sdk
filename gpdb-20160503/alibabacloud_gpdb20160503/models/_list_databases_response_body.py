# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class ListDatabasesResponseBody(DaraModel):
    def __init__(
        self,
        databases: main_models.ListDatabasesResponseBodyDatabases = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        status: str = None,
    ):
        # The queried databases.
        self.databases = databases
        # The returned message.
        self.message = message
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The status of the operation. Valid values:
        # 
        # *   **success**
        # *   **fail**
        self.status = status

    def validate(self):
        if self.databases:
            self.databases.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.databases is not None:
            result['Databases'] = self.databases.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Databases') is not None:
            temp_model = main_models.ListDatabasesResponseBodyDatabases()
            self.databases = temp_model.from_map(m.get('Databases'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ListDatabasesResponseBodyDatabases(DaraModel):
    def __init__(
        self,
        databases: List[str] = None,
    ):
        self.databases = databases

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.databases is not None:
            result['Databases'] = self.databases

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Databases') is not None:
            self.databases = m.get('Databases')

        return self

