# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateLivePullToPushRequest(DaraModel):
    def __init__(
        self,
        auth_key: str = None,
        callback_url: str = None,
        end_time: str = None,
        file_index: int = None,
        notify_item_switch: str = None,
        offset: int = None,
        owner_id: int = None,
        region: str = None,
        region_id: str = None,
        repeat_number: int = None,
        req_auth: str = None,
        source_urls: List[str] = None,
        start_time: str = None,
        task_id: str = None,
    ):
        self.auth_key = auth_key
        # The callback URL. Default value: empty.
        # > - The URL that receives task-related callbacks.
        # > - Maximum length: 2000 characters.
        # > - If this parameter is not specified, task events are not sent as callbacks.
        # > - The update takes effect only when the next event is triggered.
        self.callback_url = callback_url
        # The end time of the task.
        # > - Format: <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z (UTC).
        # > - EndTime must be later than StartTime.
        # > - EndTime must be later than the current time.
        # > - If the task has ended, the update does not take effect.
        self.end_time = end_time
        # The video index. Default value: 0.
        # > The update must be performed when the task is stopped and takes effect after the task is restarted.
        self.file_index = file_index
        self.notify_item_switch = notify_item_switch
        # The start offset of the video file, in seconds. Valid values: greater than 0.
        # > - Specifies the position to start reading from, relative to the first frame.
        # > - This parameter applies only to video-on-demand or third-party video streams.
        # > - This parameter takes effect only when the first video in the playlist is played.
        # > - The update must be performed when the task is stopped and takes effect after the task is restarted.
        self.offset = offset
        self.owner_id = owner_id
        # The region where the task is started. Valid values:
        # 
        # - ap-southeast-1 (Singapore)
        # - ap-southeast-5 (Indonesia)
        # - cn-beijing (Beijing)
        # - cn-shanghai (Shanghai)
        # 
        # This parameter is required.
        self.region = region
        # The region ID.
        self.region_id = region_id
        # The number of times playback repeats after the playlist finishes. Valid values:
        # 
        # - 0 (default): No repeat playback.
        # - -1: Loops indefinitely.
        # - Other positive integers: The number of times playback repeats after the playlist finishes.
        # 
        # > - This parameter applies only to video-on-demand or third-party video streams.
        # > - The update takes effect immediately.
        self.repeat_number = repeat_number
        self.req_auth = req_auth
        # The list of source stream URLs.
        # 
        # > - For the live type, only one complete live streaming URL is supported.
        # > - For the vod and url types, up to 30 URLs can be specified.
        # > - The live type supports RTMP, SRT, and HTTP-FLV protocols.
        # > - For the vod type, specify ApsaraVideo VOD media asset IDs.
        # > - The url type supports MP4 and HTTP-FLV protocols.
        # > - For live source streams, the update takes effect immediately. For video file source streams, the update takes effect after the currently playing video ends, and playback restarts from the beginning of the updated video list.
        # > - The update must be performed when the task is stopped and takes effect after the task is restarted.
        self.source_urls = source_urls
        # The start time of the task.
        # > - Format: <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z (UTC).
        # > - If the task has already started running, the update does not take effect.
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
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key

        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url

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

        if self.source_urls is not None:
            result['SourceUrls'] = self.source_urls

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')

        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')

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

        if m.get('SourceUrls') is not None:
            self.source_urls = m.get('SourceUrls')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

