# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeTemplateCountResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_object: main_models.DescribeTemplateCountResponseBodyResultObject = None,
    ):
        # Request ID
        self.request_id = request_id
        # Returned object
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.result_object is not None:
            result['resultObject'] = self.result_object.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('resultObject') is not None:
            temp_model = main_models.DescribeTemplateCountResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('resultObject'))

        return self

class DescribeTemplateCountResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        limit: bool = None,
        max_total_item: int = None,
        total_item: int = None,
    ):
        # Template quantity limit.
        self.limit = limit
        # Maximum count
        self.max_total_item = max_total_item
        # Total count.
        self.total_item = total_item

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.limit is not None:
            result['limit'] = self.limit

        if self.max_total_item is not None:
            result['maxTotalItem'] = self.max_total_item

        if self.total_item is not None:
            result['totalItem'] = self.total_item

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')

        if m.get('maxTotalItem') is not None:
            self.max_total_item = m.get('maxTotalItem')

        if m.get('totalItem') is not None:
            self.total_item = m.get('totalItem')

        return self

