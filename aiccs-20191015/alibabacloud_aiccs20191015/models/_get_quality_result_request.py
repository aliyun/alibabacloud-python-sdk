# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetQualityResultRequest(DaraModel):
    def __init__(
        self,
        channel_type: str = None,
        group_ids: List[int] = None,
        hit_status: int = None,
        instance_id: str = None,
        page_no: int = None,
        page_size: int = None,
        project_ids: List[int] = None,
        quality_rule_ids: List[int] = None,
        touch_end_time: str = None,
        touch_start_time: str = None,
    ):
        self.channel_type = channel_type
        self.group_ids = group_ids
        self.hit_status = hit_status
        # This parameter is required.
        self.instance_id = instance_id
        self.page_no = page_no
        self.page_size = page_size
        self.project_ids = project_ids
        self.quality_rule_ids = quality_rule_ids
        # This parameter is required.
        self.touch_end_time = touch_end_time
        # This parameter is required.
        self.touch_start_time = touch_start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type

        if self.group_ids is not None:
            result['GroupIds'] = self.group_ids

        if self.hit_status is not None:
            result['HitStatus'] = self.hit_status

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_ids is not None:
            result['ProjectIds'] = self.project_ids

        if self.quality_rule_ids is not None:
            result['QualityRuleIds'] = self.quality_rule_ids

        if self.touch_end_time is not None:
            result['TouchEndTime'] = self.touch_end_time

        if self.touch_start_time is not None:
            result['TouchStartTime'] = self.touch_start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')

        if m.get('GroupIds') is not None:
            self.group_ids = m.get('GroupIds')

        if m.get('HitStatus') is not None:
            self.hit_status = m.get('HitStatus')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectIds') is not None:
            self.project_ids = m.get('ProjectIds')

        if m.get('QualityRuleIds') is not None:
            self.quality_rule_ids = m.get('QualityRuleIds')

        if m.get('TouchEndTime') is not None:
            self.touch_end_time = m.get('TouchEndTime')

        if m.get('TouchStartTime') is not None:
            self.touch_start_time = m.get('TouchStartTime')

        return self

