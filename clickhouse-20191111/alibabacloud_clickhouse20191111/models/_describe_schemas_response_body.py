# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_clickhouse20191111 import models as main_models
from darabonba.model import DaraModel

class DescribeSchemasResponseBody(DaraModel):
    def __init__(
        self,
        items: main_models.DescribeSchemasResponseBodyItems = None,
        request_id: str = None,
    ):
        # The information about the databases of the cluster.
        self.items = items
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.items is not None:
            result['Items'] = self.items.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Items') is not None:
            temp_model = main_models.DescribeSchemasResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeSchemasResponseBodyItems(DaraModel):
    def __init__(
        self,
        schema: List[main_models.DescribeSchemasResponseBodyItemsSchema] = None,
    ):
        self.schema = schema

    def validate(self):
        if self.schema:
            for v1 in self.schema:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Schema'] = []
        if self.schema is not None:
            for k1 in self.schema:
                result['Schema'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.schema = []
        if m.get('Schema') is not None:
            for k1 in m.get('Schema'):
                temp_model = main_models.DescribeSchemasResponseBodyItemsSchema()
                self.schema.append(temp_model.from_map(k1))

        return self

class DescribeSchemasResponseBodyItemsSchema(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        schema_name: str = None,
    ):
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The database name.
        self.schema_name = schema_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        return self

