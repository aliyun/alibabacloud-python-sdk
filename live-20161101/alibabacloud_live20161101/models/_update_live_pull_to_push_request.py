# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateLivePullToPushRequest(DaraModel):
    def __init__(
        self,
        callback_url: str = None,
        end_time: str = None,
        file_index: int = None,
        offset: int = None,
        owner_id: int = None,
        region: str = None,
        region_id: str = None,
        repeat_number: int = None,
        source_urls: List[str] = None,
        start_time: str = None,
        task_id: str = None,
    ):
        # The callback URL. By default, this parameter is left empty.
        # 
        # > 
        # 
        # *   The URL is used to receive callbacks related to the task.
        # 
        # *   The URL can be up to 2,000 characters in length.
        # 
        # *   If you do not specify this parameter, no callbacks are returned for events related to the task.
        # 
        # *   The update takes effect for subsequent events that occur.
        self.callback_url = callback_url
        # The end time of the task.
        # 
        # > 
        # 
        # *   Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        # 
        # *   The time range specified by the StartTime and EndTime parameters cannot exceed seven days.
        # 
        # *   The end time must be later than the start time.
        # 
        # *   The end time must be later than the current time.
        # 
        # *   If the task has ended, the update does not take effect.
        self.end_time = end_time
        # The file index. Default value: 0.
        # 
        # >  You can modify this parameter only if the task is stopped. The update takes effect after you restart the task.
        self.file_index = file_index
        # The offset of the position where the system starts to read the video resource. Unit: seconds. Valid values: positive numbers.
        # 
        # > 
        # 
        # *   This parameter indicates an offset from the first frame.
        # 
        # *   This parameter is applicable to only video resources from ApsaraVideo VOD or a third party.
        # 
        # *   The update takes effect only for the first video in a video list.
        # 
        # *   You can modify this parameter only if the task is stopped. The update takes effect immediately.
        self.offset = offset
        self.owner_id = owner_id
        # The region where the task is started. Valid values:
        # 
        # *   ap-southeast-1: Singapore
        # *   ap-southeast-5: Indonesia (Jakarta)
        # *   cn-beijing: China (Beijing)
        # *   cn-shanghai: China (Shanghai)
        # 
        # This parameter is required.
        self.region = region
        self.region_id = region_id
        # The number of playbacks after the first playback is complete. Valid values:
        # 
        # *   0 (default): specifies that the video list is played only once.
        # *   \\-1: specifies that the video list is played in loop mode.
        # *   Positive integer: specifies the number of times the video list repeats after the first playback is complete.
        # 
        # > 
        # 
        # *   This parameter is applicable to only video resources from ApsaraVideo VOD or a third party.
        # 
        # *   The update can take effect immediately.
        self.repeat_number = repeat_number
        # The source URLs.
        # 
        # > 
        # 
        # *   If SourceType is set to live, you can specify only one streaming URL.
        # 
        # *   If SourceType is set to vod or url, you can specify up to 30 IDs or URLs.
        # 
        # *   If SourceType is set to live, the supported protocols for URLs are Real-Time Messaging Protocol (RTMP), Real-Time Streaming Protocol (RTSP), Secure Reliable Transport Protocol (SRT), and HTTP-FLV.
        # 
        # *   If SourceType is set to vod, specify the IDs of media assets from ApsaraVideo VOD.
        # 
        # *   If SourceType is set to url, the supported protocols for URLs are MP4 and HTTP-FLV.
        # 
        # *   If the source is a live stream, the update takes effect immediately. If the source is a list of video resources from ApsaraVideo VOD or a third party, the update does not take effect until the playback of the current video ends. After the update takes effect, the video list starts to play from the beginning.
        # 
        # *   You can modify this parameter only if the task is stopped. The update takes effect immediately.
        self.source_urls = source_urls
        # The start time of the task.
        # 
        # > 
        # 
        # *   Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        # 
        # *   The time range specified by the StartTime and EndTime parameters cannot exceed seven days.
        # 
        # *   If the task has already started, the update does not take effect.
        self.start_time = start_time
        # The task ID.
        # 
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.file_index is not None:
            result['FileIndex'] = self.file_index

        if self.offset is not None:
            result['Offset'] = self.offset

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region is not None:
            result['Region'] = self.region

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.repeat_number is not None:
            result['RepeatNumber'] = self.repeat_number

        if self.source_urls is not None:
            result['SourceUrls'] = self.source_urls

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('FileIndex') is not None:
            self.file_index = m.get('FileIndex')

        if m.get('Offset') is not None:
            self.offset = m.get('Offset')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RepeatNumber') is not None:
            self.repeat_number = m.get('RepeatNumber')

        if m.get('SourceUrls') is not None:
            self.source_urls = m.get('SourceUrls')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

