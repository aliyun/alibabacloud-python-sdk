# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class GetStreamTagListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        next_token: str = None,
        request_id: str = None,
        stream_tag_list: List[main_models.GetStreamTagListResponseBodyStreamTagList] = None,
        success: str = None,
        total: int = None,
    ):
        # The return code.
        self.code = code
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The tag information.
        self.stream_tag_list = stream_tag_list
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The total number of entries that are returned.
        self.total = total

    def validate(self):
        if self.stream_tag_list:
            for v1 in self.stream_tag_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['StreamTagList'] = []
        if self.stream_tag_list is not None:
            for k1 in self.stream_tag_list:
                result['StreamTagList'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.stream_tag_list = []
        if m.get('StreamTagList') is not None:
            for k1 in m.get('StreamTagList'):
                temp_model = main_models.GetStreamTagListResponseBodyStreamTagList()
                self.stream_tag_list.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class GetStreamTagListResponseBodyStreamTagList(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
        user_data: str = None,
    ):
        # The end time. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.end_time = end_time
        # The start time. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.start_time = start_time
        # The user-defined data.
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

