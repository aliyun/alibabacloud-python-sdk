# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class QueryTouchListRequest(DaraModel):
    def __init__(
        self,
        channel_id: List[str] = None,
        channel_type: List[int] = None,
        close_time_end: int = None,
        close_time_start: int = None,
        current_page: int = None,
        evaluation_level: List[int] = None,
        evaluation_score: List[int] = None,
        evaluation_status: List[int] = None,
        first_time_end: int = None,
        first_time_start: int = None,
        instance_id: str = None,
        member_id: List[int] = None,
        member_name: List[str] = None,
        page_size: int = None,
        queue_id: List[int] = None,
        servicer_id: List[int] = None,
        servicer_name: List[str] = None,
        touch_id: List[int] = None,
        touch_type: List[int] = None,
    ):
        self.channel_id = channel_id
        self.channel_type = channel_type
        self.close_time_end = close_time_end
        self.close_time_start = close_time_start
        self.current_page = current_page
        self.evaluation_level = evaluation_level
        self.evaluation_score = evaluation_score
        self.evaluation_status = evaluation_status
        self.first_time_end = first_time_end
        self.first_time_start = first_time_start
        # This parameter is required.
        self.instance_id = instance_id
        self.member_id = member_id
        self.member_name = member_name
        self.page_size = page_size
        self.queue_id = queue_id
        self.servicer_id = servicer_id
        self.servicer_name = servicer_name
        self.touch_id = touch_id
        self.touch_type = touch_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type

        if self.close_time_end is not None:
            result['CloseTimeEnd'] = self.close_time_end

        if self.close_time_start is not None:
            result['CloseTimeStart'] = self.close_time_start

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.evaluation_level is not None:
            result['EvaluationLevel'] = self.evaluation_level

        if self.evaluation_score is not None:
            result['EvaluationScore'] = self.evaluation_score

        if self.evaluation_status is not None:
            result['EvaluationStatus'] = self.evaluation_status

        if self.first_time_end is not None:
            result['FirstTimeEnd'] = self.first_time_end

        if self.first_time_start is not None:
            result['FirstTimeStart'] = self.first_time_start

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.member_id is not None:
            result['MemberId'] = self.member_id

        if self.member_name is not None:
            result['MemberName'] = self.member_name

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.queue_id is not None:
            result['QueueId'] = self.queue_id

        if self.servicer_id is not None:
            result['ServicerId'] = self.servicer_id

        if self.servicer_name is not None:
            result['ServicerName'] = self.servicer_name

        if self.touch_id is not None:
            result['TouchId'] = self.touch_id

        if self.touch_type is not None:
            result['TouchType'] = self.touch_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')

        if m.get('CloseTimeEnd') is not None:
            self.close_time_end = m.get('CloseTimeEnd')

        if m.get('CloseTimeStart') is not None:
            self.close_time_start = m.get('CloseTimeStart')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EvaluationLevel') is not None:
            self.evaluation_level = m.get('EvaluationLevel')

        if m.get('EvaluationScore') is not None:
            self.evaluation_score = m.get('EvaluationScore')

        if m.get('EvaluationStatus') is not None:
            self.evaluation_status = m.get('EvaluationStatus')

        if m.get('FirstTimeEnd') is not None:
            self.first_time_end = m.get('FirstTimeEnd')

        if m.get('FirstTimeStart') is not None:
            self.first_time_start = m.get('FirstTimeStart')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')

        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('QueueId') is not None:
            self.queue_id = m.get('QueueId')

        if m.get('ServicerId') is not None:
            self.servicer_id = m.get('ServicerId')

        if m.get('ServicerName') is not None:
            self.servicer_name = m.get('ServicerName')

        if m.get('TouchId') is not None:
            self.touch_id = m.get('TouchId')

        if m.get('TouchType') is not None:
            self.touch_type = m.get('TouchType')

        return self

