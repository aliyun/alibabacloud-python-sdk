# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations
from darabonba.model import DaraModel 
from typing import Dict


class IcebergSnapshot(DaraModel):
    def __init__(
        self,
        added_rows: int = None,
        id: int = None,
        operation: str = None,
        parent_id: int = None,
        schema_id: int = None,
        sequence_number: int = None,
        summary: Dict[str, str] = None,
        timestamp_millis: int = None,
    ):
        self.added_rows = added_rows
        self.id = id
        self.operation = operation
        self.parent_id = parent_id
        self.schema_id = schema_id
        self.sequence_number = sequence_number
        self.summary = summary
        self.timestamp_millis = timestamp_millis

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.added_rows is not None:
            result['addedRows'] = self.added_rows

        if self.id is not None:
            result['id'] = self.id

        if self.operation is not None:
            result['operation'] = self.operation

        if self.parent_id is not None:
            result['parentId'] = self.parent_id

        if self.schema_id is not None:
            result['schemaId'] = self.schema_id

        if self.sequence_number is not None:
            result['sequenceNumber'] = self.sequence_number

        if self.summary is not None:
            result['summary'] = self.summary

        if self.timestamp_millis is not None:
            result['timestampMillis'] = self.timestamp_millis

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('addedRows') is not None:
            self.added_rows = m.get('addedRows')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('operation') is not None:
            self.operation = m.get('operation')

        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')

        if m.get('schemaId') is not None:
            self.schema_id = m.get('schemaId')

        if m.get('sequenceNumber') is not None:
            self.sequence_number = m.get('sequenceNumber')

        if m.get('summary') is not None:
            self.summary = m.get('summary')

        if m.get('timestampMillis') is not None:
            self.timestamp_millis = m.get('timestampMillis')

        return self

