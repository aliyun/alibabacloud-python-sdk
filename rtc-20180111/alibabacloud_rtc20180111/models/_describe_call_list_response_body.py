# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class DescribeCallListResponseBody(DaraModel):
    def __init__(
        self,
        call_list: List[main_models.DescribeCallListResponseBodyCallList] = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total_cnt: int = None,
    ):
        self.call_list = call_list
        self.page_no = page_no
        self.page_size = page_size
        self.request_id = request_id
        self.total_cnt = total_cnt

    def validate(self):
        if self.call_list:
            for v1 in self.call_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CallList'] = []
        if self.call_list is not None:
            for k1 in self.call_list:
                result['CallList'].append(k1.to_map() if k1 else None)

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_cnt is not None:
            result['TotalCnt'] = self.total_cnt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.call_list = []
        if m.get('CallList') is not None:
            for k1 in m.get('CallList'):
                temp_model = main_models.DescribeCallListResponseBodyCallList()
                self.call_list.append(temp_model.from_map(k1))

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCnt') is not None:
            self.total_cnt = m.get('TotalCnt')

        return self

class DescribeCallListResponseBodyCallList(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        bad_exp_user_cnt: int = None,
        call_status: str = None,
        channel_id: str = None,
        created_ts: int = None,
        destroyed_ts: int = None,
        duration: int = None,
        user_cnt: int = None,
    ):
        # App ID。
        self.app_id = app_id
        self.bad_exp_user_cnt = bad_exp_user_cnt
        self.call_status = call_status
        self.channel_id = channel_id
        self.created_ts = created_ts
        self.destroyed_ts = destroyed_ts
        self.duration = duration
        self.user_cnt = user_cnt

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.bad_exp_user_cnt is not None:
            result['BadExpUserCnt'] = self.bad_exp_user_cnt

        if self.call_status is not None:
            result['CallStatus'] = self.call_status

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.created_ts is not None:
            result['CreatedTs'] = self.created_ts

        if self.destroyed_ts is not None:
            result['DestroyedTs'] = self.destroyed_ts

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.user_cnt is not None:
            result['UserCnt'] = self.user_cnt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('BadExpUserCnt') is not None:
            self.bad_exp_user_cnt = m.get('BadExpUserCnt')

        if m.get('CallStatus') is not None:
            self.call_status = m.get('CallStatus')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('CreatedTs') is not None:
            self.created_ts = m.get('CreatedTs')

        if m.get('DestroyedTs') is not None:
            self.destroyed_ts = m.get('DestroyedTs')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('UserCnt') is not None:
            self.user_cnt = m.get('UserCnt')

        return self

