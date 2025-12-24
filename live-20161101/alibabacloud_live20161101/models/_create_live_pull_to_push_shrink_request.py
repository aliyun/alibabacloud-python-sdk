# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateLivePullToPushShrinkRequest(DaraModel):
    def __init__(
        self,
        callback_url: str = None,
        dst_url: str = None,
        end_time: str = None,
        file_index: int = None,
        offset: int = None,
        owner_id: int = None,
        region: str = None,
        region_id: str = None,
        repeat_number: int = None,
        retry_count: int = None,
        retry_interval: int = None,
        source_protocol: str = None,
        source_type: str = None,
        source_urls_shrink: str = None,
        start_time: str = None,
        task_name: str = None,
    ):
        # The HTTP callback URL. By default, this parameter is left empty.
        # 
        # > 
        # 
        # *   The URL is used to receive callbacks related to the task.
        # 
        # *   The URL can be up to 2,000 characters in length.
        # 
        # *   If you do not specify this parameter, no callbacks are returned for events related to the task.
        self.callback_url = callback_url
        # The destination URL to which the stream is relayed.
        # 
        # > 
        # 
        # *   The supported protocol for the URL is RTMP.
        # 
        # *   The URL can be up to 2,000 characters in length.
        # 
        # This parameter is required.
        self.dst_url = dst_url
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
        # This parameter is required.
        self.end_time = end_time
        # The file index, which specifies the sequence of the file where the playback starts.
        self.file_index = file_index
        # The offset of the position where the system starts to read the video resource. Unit: seconds. Valid values: positive numbers.
        # 
        # > 
        # 
        # *   This parameter indicates an offset from the first frame of the first video resource in the list.
        # 
        # *   This parameter is applicable to only video resources from ApsaraVideo VOD or a third party.
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
        # >  This parameter is applicable to only video resources from ApsaraVideo VOD or a third party.
        self.repeat_number = repeat_number
        # The number of retries allowed. Default value: 3.
        self.retry_count = retry_count
        # The retry interval. Unit: seconds. Valid values: [60,300]. Default value: 60.
        self.retry_interval = retry_interval
        # The protocol of the source stream.
        # 
        # Valid values:
        # 
        # *   rtmp
        # *   rtsp
        # *   srt
        # *   http-flv
        # *   flv
        # 
        # >  This parameter is required if you set the **SourceType** parameter to live, but does not take effect if you set the SourceType parameter to vod or url.
        self.source_protocol = source_protocol
        # The type of the source stream. Valid values:
        # 
        # *   live: a live stream
        # *   vod: a list of ApsaraVideo VOD resources
        # *   url: a list of video resources from a third party
        # 
        # This parameter is required.
        self.source_type = source_type
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
        # This parameter is required.
        self.source_urls_shrink = source_urls_shrink
        # The start time of the task.
        # 
        # > 
        # 
        # *   Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        # 
        # *   The time range specified by the StartTime and EndTime parameters cannot exceed seven days.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The name of the task. Default value: "". Fuzzy search for task names is supported.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url

        if self.dst_url is not None:
            result['DstUrl'] = self.dst_url

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

        if self.retry_count is not None:
            result['RetryCount'] = self.retry_count

        if self.retry_interval is not None:
            result['RetryInterval'] = self.retry_interval

        if self.source_protocol is not None:
            result['SourceProtocol'] = self.source_protocol

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.source_urls_shrink is not None:
            result['SourceUrls'] = self.source_urls_shrink

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')

        if m.get('DstUrl') is not None:
            self.dst_url = m.get('DstUrl')

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

        if m.get('RetryCount') is not None:
            self.retry_count = m.get('RetryCount')

        if m.get('RetryInterval') is not None:
            self.retry_interval = m.get('RetryInterval')

        if m.get('SourceProtocol') is not None:
            self.source_protocol = m.get('SourceProtocol')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('SourceUrls') is not None:
            self.source_urls_shrink = m.get('SourceUrls')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        return self

