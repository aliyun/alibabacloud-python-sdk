# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateLivePullToPushShrinkRequest(DaraModel):
    def __init__(
        self,
        auth_key: str = None,
        callback_url: str = None,
        dst_url: str = None,
        end_time: str = None,
        file_index: int = None,
        notify_item_switch: str = None,
        offset: int = None,
        owner_id: int = None,
        region: str = None,
        region_id: str = None,
        repeat_number: int = None,
        req_auth: str = None,
        retry_count: int = None,
        retry_interval: int = None,
        source_protocol: str = None,
        source_type: str = None,
        source_urls_shrink: str = None,
        start_time: str = None,
        task_name: str = None,
    ):
        self.auth_key = auth_key
        # HTTP callback URL. Default value: empty.
        # 
        # > - The URL that receives task-related callbacks.
        # > - Maximum length is 2000 characters.
        # > - If this parameter is not specified, no task event callbacks will be sent.
        self.callback_url = callback_url
        # Destination URL address for pushing the stream.
        # 
        # > - The rtmp protocol is supported.
        # > - Maximum length is 2000 characters.
        # 
        # This parameter is required.
        self.dst_url = dst_url
        # Task end time.
        # 
        # > - Format: <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z (UTC time).
        # > - EndTime must be later than StartTime.
        # > - EndTime must be later than the current time.
        # 
        # This parameter is required.
        self.end_time = end_time
        # File index. Starts playback from the nth file.
        self.file_index = file_index
        self.notify_item_switch = notify_item_switch
        # Start offset. The offset value from the beginning of the video file. Unit: seconds. Valid values: greater than 0.
        # 
        # > - Indicates the position to start reading from, relative to the first frame (applies to the first video).
        # > - This parameter applies only to VOD or third-party video streams.
        self.offset = offset
        self.owner_id = owner_id
        # Specifies the region where the task is launched. Valid values:
        # 
        # - ap-southeast-1 (Singapore)
        # - ap-southeast-5 (Indonesia)
        # - cn-beijing (Beijing)
        # - cn-shanghai (Shanghai)
        # - cn-shenzhen (Shenzhen)
        # 
        # This parameter is required.
        self.region = region
        # Region ID.
        self.region_id = region_id
        # Number of times to repeat playback after the initial playback is complete. Valid values:
        # 
        # - 0 (default): no repeat playback.
        # - -1: loop indefinitely.
        # - Other positive integers: number of times to repeat playback after the initial playback is complete.
        # 
        # > This parameter applies only to VOD or third-party video streams.
        self.repeat_number = repeat_number
        self.req_auth = req_auth
        # Number of retries. Default value: 3.
        self.retry_count = retry_count
        # Retry interval, in seconds. Valid values: [60, 300]. Default value: 60 seconds.
        self.retry_interval = retry_interval
        # Source stream protocol name.
        # 
        # Valid values:
        # - rtmp
        # - srt
        # - http-flv
        # - hls
        # > This parameter is **required only when the SourceType parameter is set to live**, and is invalid when the value is vod or url.
        self.source_protocol = source_protocol
        # Source stream type. Valid values:
        # 
        # - live: live stream.
        # - vod: ApsaraVideo VOD resource.
        # - url: third-party video file resource.
        # 
        # This parameter is required.
        self.source_type = source_type
        # List of source stream URL addresses.
        # 
        # > - For the live type, only one complete live playback URL is supported.
        # > - For the vod and url types, a maximum of 30 URLs can be specified.
        # > - The live type supports: rtmp, srt, and http-flv protocols.
        # > - For the vod type, specify ApsaraVideo VOD media asset IDs.
        # > - The url type supports: mp4 and http-flv protocols.
        # 
        # This parameter is required.
        self.source_urls_shrink = source_urls_shrink
        # Task start time.
        # 
        # > - Format: <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z (UTC time).
        # 
        # This parameter is required.
        self.start_time = start_time
        # Task name, used to support fuzzy query. Default value: "".
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key

        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url

        if self.dst_url is not None:
            result['DstUrl'] = self.dst_url

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.file_index is not None:
            result['FileIndex'] = self.file_index

        if self.notify_item_switch is not None:
            result['NotifyItemSwitch'] = self.notify_item_switch

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

        if self.req_auth is not None:
            result['ReqAuth'] = self.req_auth

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
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')

        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')

        if m.get('DstUrl') is not None:
            self.dst_url = m.get('DstUrl')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('FileIndex') is not None:
            self.file_index = m.get('FileIndex')

        if m.get('NotifyItemSwitch') is not None:
            self.notify_item_switch = m.get('NotifyItemSwitch')

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

        if m.get('ReqAuth') is not None:
            self.req_auth = m.get('ReqAuth')

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

