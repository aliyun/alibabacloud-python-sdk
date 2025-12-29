# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_opensearch20171225 import models as main_models
from darabonba.model import DaraModel

class DescribeABTestSceneResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.DescribeABTestSceneResponseBodyResult = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The details of the test scenario.
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
            temp_model = main_models.DescribeABTestSceneResponseBodyResult()
            self.result = temp_model.from_map(m.get('result'))

        return self

class DescribeABTestSceneResponseBodyResult(DaraModel):
    def __init__(
        self,
        created: int = None,
        id: str = None,
        name: str = None,
        status: int = None,
        updated: int = None,
        values: List[str] = None,
    ):
        # The time when the test scenario was created.
        self.created = created
        # The ID of the test scenario.
        self.id = id
        # The name of the test scenario.
        self.name = name
        # The status of the test scenario. Valid values:
        # 
        # *   0: The test is stopped.
        # *   1: The test is started.
        self.status = status
        # The time when the test was last modified.
        self.updated = updated
        # The indicators of the test scenarios.
        self.values = values

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

        if self.values is not None:
            result['values'] = self.values

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

        if m.get('values') is not None:
            self.values = m.get('values')

        return self

