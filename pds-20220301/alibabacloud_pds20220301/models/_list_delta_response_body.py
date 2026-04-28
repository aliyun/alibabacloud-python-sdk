# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class ListDeltaResponseBody(DaraModel):
    def __init__(
        self,
        cursor: str = None,
        has_more: bool = None,
        items: List[main_models.ListDeltaResponseBodyItems] = None,
    ):
        # The cursor of the incremental information.
        self.cursor = cursor
        # Indicates whether more information is returned.
        self.has_more = has_more
        # The incremental information returned.
        self.items = items

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cursor is not None:
            result['cursor'] = self.cursor

        if self.has_more is not None:
            result['has_more'] = self.has_more

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cursor') is not None:
            self.cursor = m.get('cursor')

        if m.get('has_more') is not None:
            self.has_more = m.get('has_more')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.ListDeltaResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        return self

class ListDeltaResponseBodyItems(DaraModel):
    def __init__(
        self,
        file: main_models.File = None,
        file_id: str = None,
        op: str = None,
    ):
        # The information about the file.
        self.file = file
        # The file ID.
        self.file_id = file_id
        # The operation that is performed. Valid values: Valid values:
        # 
        # *   create
        # *   overwrite
        # *   delete
        # *   update
        # *   move
        # *   trash
        # *   restore
        # *   rename
        self.op = op

    def validate(self):
        if self.file:
            self.file.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file is not None:
            result['file'] = self.file.to_map()

        if self.file_id is not None:
            result['file_id'] = self.file_id

        if self.op is not None:
            result['op'] = self.op

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('file') is not None:
            temp_model = main_models.File()
            self.file = temp_model.from_map(m.get('file'))

        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')

        if m.get('op') is not None:
            self.op = m.get('op')

        return self

