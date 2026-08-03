# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_actiontrail20200706 import models as main_models
from darabonba.model import DaraModel

class LookupEventsRequest(DaraModel):
    def __init__(
        self,
        direction: str = None,
        end_time: str = None,
        lookup_attribute: List[main_models.LookupEventsRequestLookupAttribute] = None,
        max_results: str = None,
        next_token: str = None,
        start_time: str = None,
    ):
        # The order in which events are retrieved. Valid values:
        # 
        # - FORWARD: Chronological order.
        # 
        # - BACKWARD (default): Reverse chronological order.
        self.direction = direction
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # > You must specify both `StartTime` and `EndTime`, or leave both unspecified. If you leave them unspecified, the default value of `EndTime` is the current time.
        self.end_time = end_time
        # The filter conditions.
        # 
        # > You can specify one or two filter conditions at a time. For more information, see [Limitations](https://help.aliyun.com/document_detail/2920829.html).
        self.lookup_attribute = lookup_attribute
        # The maximum number of results to return.<br>Valid values: 1 to 50.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results.
        # 
        # > You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time must be in UTC.
        # 
        # > You must specify both `StartTime` and `EndTime`, or leave both unspecified. If you leave them unspecified, the default value of `StartTime` is 7 days before the current time.
        self.start_time = start_time

    def validate(self):
        if self.lookup_attribute:
            for v1 in self.lookup_attribute:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.direction is not None:
            result['Direction'] = self.direction

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        result['LookupAttribute'] = []
        if self.lookup_attribute is not None:
            for k1 in self.lookup_attribute:
                result['LookupAttribute'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        self.lookup_attribute = []
        if m.get('LookupAttribute') is not None:
            for k1 in m.get('LookupAttribute'):
                temp_model = main_models.LookupEventsRequestLookupAttribute()
                self.lookup_attribute.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class LookupEventsRequestLookupAttribute(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The attribute key. For information about valid values, see [How do I configure the LookupAttribute parameter when calling LookupInsightEvents?](https://help.aliyun.com/document_detail/2920829.html)
        self.key = key
        # The attribute value. For information about valid values, see [How do I configure the LookupAttribute parameter when calling LookupInsightEvents?](https://help.aliyun.com/document_detail/2920829.html)
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

