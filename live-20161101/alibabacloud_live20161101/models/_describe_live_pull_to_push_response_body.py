# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLivePullToPushResponseBody(DaraModel):
    def __init__(
        self,
        current_file_index: int = None,
        current_offset: int = None,
        description: str = None,
        request_id: str = None,
        ret_code: int = None,
        task_exit_reason: str = None,
        task_exit_time: int = None,
        task_id: str = None,
        task_info: main_models.DescribeLivePullToPushResponseBodyTaskInfo = None,
        task_invalid_reason: str = None,
        task_status: int = None,
    ):
        # The current effective playlist sequence offset.
        self.current_file_index = current_file_index
        # The current effective video playback offset.
        self.current_offset = current_offset
        # The error description.
        self.description = description
        # The request ID.
        self.request_id = request_id
        # The return code.
        # > - "0" is returned in normal cases.
        # > - For error cases, refer to the error code list below.
        self.ret_code = ret_code
        # The reason why the task exited. Valid values:
        # 
        # - TriggerByUser: The task was actively ended by the user.
        # - OverEndTime: The preset end time was exceeded.
        # 
        # > This parameter is returned only when the task is in the exited state.
        self.task_exit_reason = task_exit_reason
        # The time when the task exited. The value is a UNIX timestamp in seconds.
        # > This parameter is returned only when the task is in the exited state.
        self.task_exit_time = task_exit_time
        # The ID of the node returned when you create task.
        self.task_id = task_id
        # The task information.
        self.task_info = task_info
        # The reason why the task stopped running. Valid values:
        # 
        # - PullStreamFailed: Source stream pulling is abnormal. Retrying.
        # - PushStreamFailed: Destination stream pushing is abnormal. Retrying.
        # - UnknownError: Unknown error.
        # 
        # > This parameter is returned only when the task is in the stopped state.
        self.task_invalid_reason = task_invalid_reason
        # The current status of the task. Valid values:
        # - 0: Not started (the start time has not been reached).
        # - 1: Running normally (stream pulling and pushing are both normal).
        # - 2: Running abnormally.
        # - 3: Stopped (stream pulling or pushing is abnormal, or the task was actively stopped by calling an API operation).
        # - -1: Exited.
        self.task_status = task_status

    def validate(self):
        if self.task_info:
            self.task_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_file_index is not None:
            result['CurrentFileIndex'] = self.current_file_index

        if self.current_offset is not None:
            result['CurrentOffset'] = self.current_offset

        if self.description is not None:
            result['Description'] = self.description

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.ret_code is not None:
            result['RetCode'] = self.ret_code

        if self.task_exit_reason is not None:
            result['TaskExitReason'] = self.task_exit_reason

        if self.task_exit_time is not None:
            result['TaskExitTime'] = self.task_exit_time

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_info is not None:
            result['TaskInfo'] = self.task_info.to_map()

        if self.task_invalid_reason is not None:
            result['TaskInvalidReason'] = self.task_invalid_reason

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentFileIndex') is not None:
            self.current_file_index = m.get('CurrentFileIndex')

        if m.get('CurrentOffset') is not None:
            self.current_offset = m.get('CurrentOffset')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RetCode') is not None:
            self.ret_code = m.get('RetCode')

        if m.get('TaskExitReason') is not None:
            self.task_exit_reason = m.get('TaskExitReason')

        if m.get('TaskExitTime') is not None:
            self.task_exit_time = m.get('TaskExitTime')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskInfo') is not None:
            temp_model = main_models.DescribeLivePullToPushResponseBodyTaskInfo()
            self.task_info = temp_model.from_map(m.get('TaskInfo'))

        if m.get('TaskInvalidReason') is not None:
            self.task_invalid_reason = m.get('TaskInvalidReason')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        return self

class DescribeLivePullToPushResponseBodyTaskInfo(DaraModel):
    def __init__(
        self,
        auth_key: str = None,
        callback_url: str = None,
        dst_url: str = None,
        end_time: str = None,
        file_index: int = None,
        notify_item_switch: str = None,
        offset: int = None,
        repeat_number: int = None,
        req_auth: str = None,
        retry_count: int = None,
        retry_interval: int = None,
        source_protocol: str = None,
        source_type: str = None,
        source_urls: List[str] = None,
        start_time: str = None,
        task_id: str = None,
        task_name: str = None,
    ):
        self.auth_key = auth_key
        # The HTTP callback URL.
        self.callback_url = callback_url
        # The destination ingest URL.
        self.dst_url = dst_url
        # The end time of the task. Format: <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z (UTC).
        self.end_time = end_time
        # The file index. Playback starts from the nth file.
        self.file_index = file_index
        self.notify_item_switch = notify_item_switch
        # The start offset of the video file. Unit: seconds. The value must be greater than 0.
        # > - Indicates the position from which reading starts, relative to the first frame.
        # > - This parameter is valid only for video-on-demand resources or video files.
        self.offset = offset
        # The number of times playback repeats after completion. Valid values:
        # - 0 (default): No repeat playback.
        # - -1: Infinite loop.
        # - Other positive integers: the number of times playback repeats after completion.
        # 
        # > This parameter applies only to video-on-demand or third-party video streams.
        self.repeat_number = repeat_number
        self.req_auth = req_auth
        # The number of retries.
        self.retry_count = retry_count
        # The retry interval. Unit: seconds.
        self.retry_interval = retry_interval
        # The source stream protocol name.
        self.source_protocol = source_protocol
        # The source stream type. Valid values:
        # 
        # - live: live stream.
        # - vod: ApsaraVideo VOD resource.
        # - url: third-party video file resource.
        self.source_type = source_type
        # The source stream URL.
        self.source_urls = source_urls
        # The start time of the task. Format: <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z (UTC).
        self.start_time = start_time
        # The task ID.
        self.task_id = task_id
        # The task name.
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
            result['CallbackURL'] = self.callback_url

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

        if self.source_urls is not None:
            result['SourceUrls'] = self.source_urls

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')

        if m.get('CallbackURL') is not None:
            self.callback_url = m.get('CallbackURL')

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
            self.source_urls = m.get('SourceUrls')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        return self

