# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListHistoricalSkillGroupReportRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        instance_id: str = None,
        media_type: str = None,
        page_number: int = None,
        page_size: int = None,
        skill_group_id_list: str = None,
        start_time: int = None,
        summarize_by_instance_id: bool = None,
    ):
        # The end time of the historical data to retrieve. Specify a UNIX timestamp in milliseconds. This parameter is optional. Default value: the current time. The statistical time precision is in hours. The end time is rounded up to the nearest hour, and the interval is open. For example, if the start time is 11:12:20 and the end time is 11:45:50, the aligned time range is [11:00:00, 12:00:00), which means greater than or equal to 11:00:00 and less than 12:00:00.
        self.end_time = end_time
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The media type. Default value: Audio. Valid values: Audio, Chat, and Video.
        self.media_type = media_type
        # The page number. Valid values: 1 to 100.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 100.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The list of skill group IDs to query. The value is a character string in the JSON array format, where each array element is a skill group ID. This parameter is optional. Default value: empty. An empty value indicates that all skill groups in the current paging are queried.
        self.skill_group_id_list = skill_group_id_list
        # The start time of the historical data to retrieve. Specify a UNIX timestamp in milliseconds. This parameter is optional. Default value: 00:00:00 on the current day. The earliest allowed time is 180 days before the current time. The statistical time precision is in hours. The start time is rounded down to the nearest hour, and the interval is closed.
        self.start_time = start_time
        # Specifies whether to aggregate data by instance ID.
        self.summarize_by_instance_id = summarize_by_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.media_type is not None:
            result['MediaType'] = self.media_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.skill_group_id_list is not None:
            result['SkillGroupIdList'] = self.skill_group_id_list

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.summarize_by_instance_id is not None:
            result['SummarizeByInstanceId'] = self.summarize_by_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SkillGroupIdList') is not None:
            self.skill_group_id_list = m.get('SkillGroupIdList')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('SummarizeByInstanceId') is not None:
            self.summarize_by_instance_id = m.get('SummarizeByInstanceId')

        return self

