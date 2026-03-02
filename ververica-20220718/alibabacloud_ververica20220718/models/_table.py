# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List, Any

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class Table(DaraModel):
    def __init__(
        self,
        comment: str = None,
        metadata: Dict[str, str] = None,
        name: str = None,
        partition_keys: List[str] = None,
        properties: Dict[str, Any] = None,
        schema: main_models.Schema = None,
        table_type: str = None,
    ):
        # The comment.
        self.comment = comment
        self.metadata = metadata
        # The name of the table.
        # 
        # This parameter is required.
        self.name = name
        # The partition key column.
        self.partition_keys = partition_keys
        # The parameter configurations of the table.
        self.properties = properties
        # The schema information about the table.
        self.schema = schema
        # TABLE;
        #   MATERIALIZED_TABLE;
        #   VIEW;
        # 
        # This parameter is required.
        self.table_type = table_type

    def validate(self):
        if self.schema:
            self.schema.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['comment'] = self.comment

        if self.metadata is not None:
            result['metadata'] = self.metadata

        if self.name is not None:
            result['name'] = self.name

        if self.partition_keys is not None:
            result['partitionKeys'] = self.partition_keys

        if self.properties is not None:
            result['properties'] = self.properties

        if self.schema is not None:
            result['schema'] = self.schema.to_map()

        if self.table_type is not None:
            result['tableType'] = self.table_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comment') is not None:
            self.comment = m.get('comment')

        if m.get('metadata') is not None:
            self.metadata = m.get('metadata')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('partitionKeys') is not None:
            self.partition_keys = m.get('partitionKeys')

        if m.get('properties') is not None:
            self.properties = m.get('properties')

        if m.get('schema') is not None:
            temp_model = main_models.Schema()
            self.schema = temp_model.from_map(m.get('schema'))

        if m.get('tableType') is not None:
            self.table_type = m.get('tableType')

        return self

