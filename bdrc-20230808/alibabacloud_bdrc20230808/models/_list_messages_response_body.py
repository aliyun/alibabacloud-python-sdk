# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bdrc20230808 import models as main_models
from darabonba.model import DaraModel

class ListMessagesResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListMessagesResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ListMessagesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListMessagesResponseBodyData(DaraModel):
    def __init__(
        self,
        content: List[main_models.ListMessagesResponseBodyDataContent] = None,
        max_results: int = None,
        next_token: str = None,
        total_count: int = None,
    ):
        # Response parameters.
        self.content = content
        # The maximum number of results requested.
        self.max_results = max_results
        # The pagination token.
        self.next_token = next_token
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.content:
            for v1 in self.content:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Content'] = []
        if self.content is not None:
            for k1 in self.content:
                result['Content'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content = []
        if m.get('Content') is not None:
            for k1 in m.get('Content'):
                temp_model = main_models.ListMessagesResponseBodyDataContent()
                self.content.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListMessagesResponseBodyDataContent(DaraModel):
    def __init__(
        self,
        message_id: str = None,
        message_level: str = None,
        message_name: str = None,
        message_source_id: str = None,
        message_source_region_id: str = None,
        message_source_type: str = None,
        message_time: int = None,
        message_type: str = None,
    ):
        # Message ID.
        self.message_id = message_id
        # Message level.
        self.message_level = message_level
        # Message name.
        self.message_name = message_name
        # Message source ID.
        self.message_source_id = message_source_id
        # Message source region ID.
        self.message_source_region_id = message_source_region_id
        # Message source type.
        self.message_source_type = message_source_type
        # Message time.
        self.message_time = message_time
        # Message type.
        self.message_type = message_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message_id is not None:
            result['MessageId'] = self.message_id

        if self.message_level is not None:
            result['MessageLevel'] = self.message_level

        if self.message_name is not None:
            result['MessageName'] = self.message_name

        if self.message_source_id is not None:
            result['MessageSourceId'] = self.message_source_id

        if self.message_source_region_id is not None:
            result['MessageSourceRegionId'] = self.message_source_region_id

        if self.message_source_type is not None:
            result['MessageSourceType'] = self.message_source_type

        if self.message_time is not None:
            result['MessageTime'] = self.message_time

        if self.message_type is not None:
            result['MessageType'] = self.message_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')

        if m.get('MessageLevel') is not None:
            self.message_level = m.get('MessageLevel')

        if m.get('MessageName') is not None:
            self.message_name = m.get('MessageName')

        if m.get('MessageSourceId') is not None:
            self.message_source_id = m.get('MessageSourceId')

        if m.get('MessageSourceRegionId') is not None:
            self.message_source_region_id = m.get('MessageSourceRegionId')

        if m.get('MessageSourceType') is not None:
            self.message_source_type = m.get('MessageSourceType')

        if m.get('MessageTime') is not None:
            self.message_time = m.get('MessageTime')

        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')

        return self

