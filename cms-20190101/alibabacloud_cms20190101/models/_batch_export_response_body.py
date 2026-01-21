# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class BatchExportResponseBody(DaraModel):
    def __init__(
        self,
        anchor: int = None,
        code: int = None,
        cursor: str = None,
        data_results: List[main_models.MetricStat] = None,
        has_next: bool = None,
        length: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The timestamp of the data requested by the backend. A larger timestamp indicates that the data export time is closer to the current time.
        self.anchor = anchor
        # The HTTP status code.
        # 
        # >  The status code 200 indicates that the request was successful.
        self.code = code
        # The Cursor information that is used to call this operation again.
        # 
        # >  If `null` is returned, the monitoring data is exported.
        self.cursor = cursor
        # The data returned in this call.
        self.data_results = data_results
        # Indicates whether the data has been exported. Valid values:
        # 
        # *   true: Some data is not exported.
        # *   false: All the data is exported.
        self.has_next = has_next
        # The number of data entries returned in this call.
        self.length = length
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.data_results:
            for v1 in self.data_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.anchor is not None:
            result['Anchor'] = self.anchor

        if self.code is not None:
            result['Code'] = self.code

        if self.cursor is not None:
            result['Cursor'] = self.cursor

        result['DataResults'] = []
        if self.data_results is not None:
            for k1 in self.data_results:
                result['DataResults'].append(k1.to_map() if k1 else None)

        if self.has_next is not None:
            result['HasNext'] = self.has_next

        if self.length is not None:
            result['Length'] = self.length

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Anchor') is not None:
            self.anchor = m.get('Anchor')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Cursor') is not None:
            self.cursor = m.get('Cursor')

        self.data_results = []
        if m.get('DataResults') is not None:
            for k1 in m.get('DataResults'):
                temp_model = main_models.MetricStat()
                self.data_results.append(temp_model.from_map(k1))

        if m.get('HasNext') is not None:
            self.has_next = m.get('HasNext')

        if m.get('Length') is not None:
            self.length = m.get('Length')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

