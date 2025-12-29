# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_opensearch20171225 import models as main_models
from darabonba.model import DaraModel

class ListABTestGroupsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.ListABTestGroupsResponseBodyResult] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The test groups.
        # 
        # For more information, see [ABTestGroup](https://help.aliyun.com/document_detail/178935.html).
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
                temp_model = main_models.ListABTestGroupsResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class ListABTestGroupsResponseBodyResult(DaraModel):
    def __init__(
        self,
        created: int = None,
        id: str = None,
        name: str = None,
        status: int = None,
        updated: int = None,
    ):
        # The time when the test group was created.
        self.created = created
        # The ID of the test group.
        self.id = id
        # The name of the test group.
        self.name = name
        # The status of the test group. Valid values:
        # 
        # *   0: not in effect
        # *   1: in effect
        self.status = status
        # The time when the test group was last modified.
        self.updated = updated

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created is not None:
            result['created'] = self.created

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.status is not None:
            result['status'] = self.status

        if self.updated is not None:
            result['updated'] = self.updated

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('updated') is not None:
            self.updated = m.get('updated')

        return self

