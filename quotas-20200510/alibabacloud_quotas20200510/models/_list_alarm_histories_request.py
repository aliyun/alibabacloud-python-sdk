# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAlarmHistoriesRequest(DaraModel):
    def __init__(
        self,
        alarm_id: str = None,
        end_time: int = None,
        keyword: str = None,
        max_results: int = None,
        next_token: str = None,
        product_code: str = None,
        start_time: int = None,
    ):
        # The alert ID.
        self.alarm_id = alarm_id
        # The end time of the query.
        self.end_time = end_time
        # The search keyword.
        self.keyword = keyword
        # The maximum number of entries to return for the current query.
        # 
        # Valid values: 1 to 200. Default value: 30.
        self.max_results = max_results
        # The token that specifies the starting position of the query. An empty value indicates that the query starts from the beginning.
        self.next_token = next_token
        # The abbreviation of the cloud service name.
        # 
        # > For more information about the cloud services that support Quota Center, see [Cloud services that support Quota Center](https://help.aliyun.com/document_detail/182368.html).
        self.product_code = product_code
        # The start time of the query.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

