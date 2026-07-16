# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeAnalysisConditionFavoriteListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_object: List[main_models.DescribeAnalysisConditionFavoriteListResponseBodyResultObject] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The response object.
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            for v1 in self.result_object:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['resultObject'] = []
        if self.result_object is not None:
            for k1 in self.result_object:
                result['resultObject'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result_object = []
        if m.get('resultObject') is not None:
            for k1 in m.get('resultObject'):
                temp_model = main_models.DescribeAnalysisConditionFavoriteListResponseBodyResultObject()
                self.result_object.append(temp_model.from_map(k1))

        return self

class DescribeAnalysisConditionFavoriteListResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        condition: str = None,
        event_begin_time: int = None,
        event_codes: str = None,
        event_end_time: int = None,
        field_name: str = None,
        field_value: str = None,
        id: int = None,
        name: str = None,
        type: str = None,
    ):
        # The condition value.
        self.condition = condition
        # The event start timestamp.
        self.event_begin_time = event_begin_time
        # The event code.
        self.event_codes = event_codes
        # The event end timestamp.
        self.event_end_time = event_end_time
        # The field name.
        self.field_name = field_name
        # The field value.
        self.field_value = field_value
        # The primary key ID.
        self.id = id
        # The condition name.
        self.name = name
        # The type. Valid values: BASIC: basic query. ADVANCE: advanced query. BATCH: batch query.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.condition is not None:
            result['condition'] = self.condition

        if self.event_begin_time is not None:
            result['eventBeginTime'] = self.event_begin_time

        if self.event_codes is not None:
            result['eventCodes'] = self.event_codes

        if self.event_end_time is not None:
            result['eventEndTime'] = self.event_end_time

        if self.field_name is not None:
            result['fieldName'] = self.field_name

        if self.field_value is not None:
            result['fieldValue'] = self.field_value

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('condition') is not None:
            self.condition = m.get('condition')

        if m.get('eventBeginTime') is not None:
            self.event_begin_time = m.get('eventBeginTime')

        if m.get('eventCodes') is not None:
            self.event_codes = m.get('eventCodes')

        if m.get('eventEndTime') is not None:
            self.event_end_time = m.get('eventEndTime')

        if m.get('fieldName') is not None:
            self.field_name = m.get('fieldName')

        if m.get('fieldValue') is not None:
            self.field_value = m.get('fieldValue')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

