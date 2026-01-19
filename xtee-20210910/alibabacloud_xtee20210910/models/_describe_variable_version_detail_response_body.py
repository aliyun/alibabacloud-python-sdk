# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeVariableVersionDetailResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_object: main_models.DescribeVariableVersionDetailResponseBodyResultObject = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Returned object.
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
            result['RequestId'] = self.request_id

        if self.result_object is not None:
            result['resultObject'] = self.result_object.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('resultObject') is not None:
            temp_model = main_models.DescribeVariableVersionDetailResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('resultObject'))

        return self

class DescribeVariableVersionDetailResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        condition: str = None,
        data_version: int = None,
        description: str = None,
        event_codes: str = None,
        global_: bool = None,
        history_value_type: str = None,
        id: int = None,
        object: str = None,
        status: str = None,
        subject: str = None,
        time_type: str = None,
        title: str = None,
        top_n: int = None,
        tw_count: int = None,
        velocity_fc: str = None,
        velocity_tw: str = None,
    ):
        # Condition value.
        self.condition = condition
        # Data version.
        self.data_version = data_version
        # Variable description information.
        self.description = description
        # Event code.
        self.event_codes = event_codes
        # Global cumulative. Not currently available externally.
        self.global_ = global_
        # Historical value parameter type.
        self.history_value_type = history_value_type
        # Primary key ID of the version.
        self.id = id
        # Subordinate attribute (single selection, sourced from the event attribute list code).
        self.object = object
        # Status.
        self.status = status
        # Main attribute (multiple separated by commas, up to 5, sourced from the event attribute list code).
        self.subject = subject
        # Time slice type.
        self.time_type = time_type
        # Title.
        self.title = title
        # Top N.
        self.top_n = top_n
        # Number of time slices.
        self.tw_count = tw_count
        # Cumulative indicator processing function.
        self.velocity_fc = velocity_fc
        # Cumulative indicator time window.
        self.velocity_tw = velocity_tw

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.condition is not None:
            result['condition'] = self.condition

        if self.data_version is not None:
            result['dataVersion'] = self.data_version

        if self.description is not None:
            result['description'] = self.description

        if self.event_codes is not None:
            result['eventCodes'] = self.event_codes

        if self.global_ is not None:
            result['global'] = self.global_

        if self.history_value_type is not None:
            result['historyValueType'] = self.history_value_type

        if self.id is not None:
            result['id'] = self.id

        if self.object is not None:
            result['object'] = self.object

        if self.status is not None:
            result['status'] = self.status

        if self.subject is not None:
            result['subject'] = self.subject

        if self.time_type is not None:
            result['timeType'] = self.time_type

        if self.title is not None:
            result['title'] = self.title

        if self.top_n is not None:
            result['topN'] = self.top_n

        if self.tw_count is not None:
            result['twCount'] = self.tw_count

        if self.velocity_fc is not None:
            result['velocityFC'] = self.velocity_fc

        if self.velocity_tw is not None:
            result['velocityTW'] = self.velocity_tw

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('condition') is not None:
            self.condition = m.get('condition')

        if m.get('dataVersion') is not None:
            self.data_version = m.get('dataVersion')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('eventCodes') is not None:
            self.event_codes = m.get('eventCodes')

        if m.get('global') is not None:
            self.global_ = m.get('global')

        if m.get('historyValueType') is not None:
            self.history_value_type = m.get('historyValueType')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('object') is not None:
            self.object = m.get('object')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('subject') is not None:
            self.subject = m.get('subject')

        if m.get('timeType') is not None:
            self.time_type = m.get('timeType')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('topN') is not None:
            self.top_n = m.get('topN')

        if m.get('twCount') is not None:
            self.tw_count = m.get('twCount')

        if m.get('velocityFC') is not None:
            self.velocity_fc = m.get('velocityFC')

        if m.get('velocityTW') is not None:
            self.velocity_tw = m.get('velocityTW')

        return self

