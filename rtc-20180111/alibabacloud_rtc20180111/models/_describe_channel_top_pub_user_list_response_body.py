# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class DescribeChannelTopPubUserListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        top_pub_user_detail_list: List[main_models.DescribeChannelTopPubUserListResponseBodyTopPubUserDetailList] = None,
    ):
        self.request_id = request_id
        self.top_pub_user_detail_list = top_pub_user_detail_list

    def validate(self):
        if self.top_pub_user_detail_list:
            for v1 in self.top_pub_user_detail_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TopPubUserDetailList'] = []
        if self.top_pub_user_detail_list is not None:
            for k1 in self.top_pub_user_detail_list:
                result['TopPubUserDetailList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.top_pub_user_detail_list = []
        if m.get('TopPubUserDetailList') is not None:
            for k1 in m.get('TopPubUserDetailList'):
                temp_model = main_models.DescribeChannelTopPubUserListResponseBodyTopPubUserDetailList()
                self.top_pub_user_detail_list.append(temp_model.from_map(k1))

        return self

class DescribeChannelTopPubUserListResponseBodyTopPubUserDetailList(DaraModel):
    def __init__(
        self,
        created_ts: int = None,
        destroyed_ts: int = None,
        duration: int = None,
        location: str = None,
        online_duration: int = None,
        online_periods: List[main_models.DescribeChannelTopPubUserListResponseBodyTopPubUserDetailListOnlinePeriods] = None,
        user_id: str = None,
    ):
        self.created_ts = created_ts
        self.destroyed_ts = destroyed_ts
        self.duration = duration
        self.location = location
        self.online_duration = online_duration
        self.online_periods = online_periods
        self.user_id = user_id

    def validate(self):
        if self.online_periods:
            for v1 in self.online_periods:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts

        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.location is not None:
            result['Location'] = self.location

        if self.online_duration is not None:
            result['OnlineDuration'] = self.online_duration

        result['OnlinePeriods'] = []
        if self.online_periods is not None:
            for k1 in self.online_periods:
                result['OnlinePeriods'].append(k1.to_map() if k1 else None)

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')

        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        if m.get('OnlineDuration') is not None:
            self.online_duration = m.get('OnlineDuration')

        self.online_periods = []
        if m.get('OnlinePeriods') is not None:
            for k1 in m.get('OnlinePeriods'):
                temp_model = main_models.DescribeChannelTopPubUserListResponseBodyTopPubUserDetailListOnlinePeriods()
                self.online_periods.append(temp_model.from_map(k1))

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class DescribeChannelTopPubUserListResponseBodyTopPubUserDetailListOnlinePeriods(DaraModel):
    def __init__(
        self,
        join_ts: int = None,
        leave_ts: int = None,
    ):
        self.join_ts = join_ts
        self.leave_ts = leave_ts

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.join_ts is not None:
            result['JoinTs'] = self.join_ts

        if self.leave_ts is not None:
            result['LeaveTs'] = self.leave_ts

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JoinTs') is not None:
            self.join_ts = m.get('JoinTs')

        if m.get('LeaveTs') is not None:
            self.leave_ts = m.get('LeaveTs')

        return self

