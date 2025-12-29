# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_opensearch20171225 import models as main_models
from darabonba.model import DaraModel

class ListSortExpressionsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.ListSortExpressionsResponseBodyResult] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the rough sort or fine sort expressions that are returned.
        # 
        # For more information, see [FirstRank](https://help.aliyun.com/document_detail/170007.html) and [SecondRank](https://help.aliyun.com/document_detail/170008.html).
        self.result = result

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.result = []
        if m.get('result') is not None:
            for k1 in m.get('result'):
                temp_model = main_models.ListSortExpressionsResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class ListSortExpressionsResponseBodyResult(DaraModel):
    def __init__(
        self,
        active: bool = None,
        created: int = None,
        description: str = None,
        name: str = None,
        updated: int = None,
    ):
        # Indicates whether the expression is the default one.
        self.active = active
        # The timestamp when the sort expression was created.
        self.created = created
        # The description of the sort expression.
        self.description = description
        # The name of the sort expression.
        self.name = name
        # The timestamp when the sort expression was updated.
        self.updated = updated

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active is not None:
            result['active'] = self.active

        if self.created is not None:
            result['created'] = self.created

        if self.description is not None:
            result['description'] = self.description

        if self.name is not None:
            result['name'] = self.name

        if self.updated is not None:
            result['updated'] = self.updated

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')

        if m.get('created') is not None:
            self.created = m.get('created')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('updated') is not None:
            self.updated = m.get('updated')

        return self

