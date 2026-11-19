# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dds20151201 import models as main_models
from darabonba.model import DaraModel

class DescribeDatabasesResponseBody(DaraModel):
    def __init__(
        self,
        databases: main_models.DescribeDatabasesResponseBodyDatabases = None,
        request_id: str = None,
    ):
        self.databases = databases
        # The request ID.
        self.request_id = request_id

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Databases') is not None:
            temp_model = main_models.DescribeDatabasesResponseBodyDatabases()
            self.databases = temp_model.from_map(m.get('Databases'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDatabasesResponseBodyDatabases(DaraModel):
    def __init__(
        self,
        database: List[str] = None,
    ):
        self.database = database

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database is not None:
            result['Database'] = self.database

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Database') is not None:
            self.database = m.get('Database')

        return self

