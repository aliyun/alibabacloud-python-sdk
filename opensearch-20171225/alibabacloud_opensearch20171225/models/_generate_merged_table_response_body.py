# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_opensearch20171225 import models as main_models
from darabonba.model import DaraModel

class GenerateMergedTableResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.GenerateMergedTableResponseBodyResult = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The response parameters.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.result is not None:
            result['result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('result') is not None:
            temp_model = main_models.GenerateMergedTableResponseBodyResult()
            self.result = temp_model.from_map(m.get('result'))

        return self

class GenerateMergedTableResponseBodyResult(DaraModel):
    def __init__(
        self,
        from_table: Dict[str, Any] = None,
        merge_table: Dict[str, Any] = None,
        primary_key: str = None,
    ):
        # The tables on which the JOIN operation is performed.
        self.from_table = from_table
        # The wide table that is generated after the JOIN operation is performed on multiple tables.
        self.merge_table = merge_table
        # The primary key.
        self.primary_key = primary_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_table is not None:
            result['fromTable'] = self.from_table

        if self.merge_table is not None:
            result['mergeTable'] = self.merge_table

        if self.primary_key is not None:
            result['primaryKey'] = self.primary_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fromTable') is not None:
            self.from_table = m.get('fromTable')

        if m.get('mergeTable') is not None:
            self.merge_table = m.get('mergeTable')

        if m.get('primaryKey') is not None:
            self.primary_key = m.get('primaryKey')

        return self

