# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryTicketsShrinkRequest(DaraModel):
    def __init__(
        self,
        case_id: int = None,
        case_status: int = None,
        case_type: int = None,
        channel_id: str = None,
        channel_type: int = None,
        current_page: int = None,
        deal_id: int = None,
        extra_shrink: str = None,
        instance_id: str = None,
        page_size: int = None,
        sr_type: int = None,
        task_status: int = None,
        touch_id: int = None,
    ):
        self.case_id = case_id
        self.case_status = case_status
        self.case_type = case_type
        self.channel_id = channel_id
        self.channel_type = channel_type
        self.current_page = current_page
        self.deal_id = deal_id
        self.extra_shrink = extra_shrink
        # This parameter is required.
        self.instance_id = instance_id
        self.page_size = page_size
        self.sr_type = sr_type
        self.task_status = task_status
        self.touch_id = touch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.case_id is not None:
            result['CaseId'] = self.case_id

        if self.case_status is not None:
            result['CaseStatus'] = self.case_status

        if self.case_type is not None:
            result['CaseType'] = self.case_type

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.deal_id is not None:
            result['DealId'] = self.deal_id

        if self.extra_shrink is not None:
            result['Extra'] = self.extra_shrink

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sr_type is not None:
            result['SrType'] = self.sr_type

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.touch_id is not None:
            result['TouchId'] = self.touch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaseId') is not None:
            self.case_id = m.get('CaseId')

        if m.get('CaseStatus') is not None:
            self.case_status = m.get('CaseStatus')

        if m.get('CaseType') is not None:
            self.case_type = m.get('CaseType')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('DealId') is not None:
            self.deal_id = m.get('DealId')

        if m.get('Extra') is not None:
            self.extra_shrink = m.get('Extra')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SrType') is not None:
            self.sr_type = m.get('SrType')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('TouchId') is not None:
            self.touch_id = m.get('TouchId')

        return self

