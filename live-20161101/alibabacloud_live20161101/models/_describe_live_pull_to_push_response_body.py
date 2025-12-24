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
        # The current file index.
        self.current_file_index = current_file_index
        # The current offset for video playback.
        self.current_offset = current_offset
        # The error description.
        self.description = description
        # The request ID.
        self.request_id = request_id
        # The code that is returned for the request.
        # 
        # > 
        # 
        # *   0 is returned if the request is normal.
        # 
        # *   For information about codes that are returned when exceptions occur, see the following Error codes table.
        self.ret_code = ret_code
        # The reason why the task is stopped.
        # 
        # *   TriggerByUser: You proactively stopped the task.
        # *   OverEndTime: The specified end time was exceeded.
        # 
        # >  This parameter is returned only if the task is stopped.
        self.task_exit_reason = task_exit_reason
        # The time when the task was exited. The value is a Unix timestamp in seconds.
        # 
        # >  This parameter is returned only if the task status is exited.
        self.task_exit_time = task_exit_time
        # The task ID.
        self.task_id = task_id
        # The information about the task.
        self.task_info = task_info
        # The reason why the task was stopped.
        # 
        # *   PullStreamFailed: An exception occurred while pulling the source stream. A retry is in progress.
        # *   PushStreamFailed: An exception occurred while ingesting the stream. A retry is in progress.
        # *   UnknownError: An unknown exception occurred.
        # 
        # >  This parameter is returned only if the task status is stopped.
        self.task_invalid_reason = task_invalid_reason
        # The current status of the task.
        # 
        # *   0: not started.
        # *   1: running. Stream pulling and stream relay are normal.
        # *   2: abnormal.
        # *   3: stopped. It may be because exceptions occur during stream pulling or stream relay or you proactively call the StopLivePullToPush operation.
        # *   \\-1: exited.
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
        callback_url: str = None,
        dst_url: str = None,
        end_time: str = None,
        file_index: int = None,
        offset: int = None,
        repeat_number: int = None,
        retry_count: int = None,
        retry_interval: int = None,
        source_protocol: str = None,
        source_type: str = None,
        source_urls: List[str] = None,
        start_time: str = None,
        task_id: str = None,
        task_name: str = None,
    ):
        # The HTTP callback URL.
        self.callback_url = callback_url
        # The destination URL to which the stream is relayed.
        self.dst_url = dst_url
        # The end time of the task. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.end_time = end_time
        # The file index, which indicates the sequence of the file where the playback starts.
        self.file_index = file_index
        # The offset of the position where the system starts to read the video resource. Unit: seconds. Valid values: positive numbers.
        # 
        # > 
        # 
        # *   This parameter indicates an offset from the first frame.
        # 
        # *   This parameter is applicable to only video resources from ApsaraVideo VOD or a third party.
        self.offset = offset
        # The number of playbacks after the first playback is complete. Valid values:
        # 
        # *   0 (default): specifies that the video list is played only once.
        # *   \\-1: specifies that the video list is played in loop mode.
        # *   Positive integer: specifies the number of times the video list repeats after the first playback is complete.
        # 
        # >  This parameter is applicable to only video resources from ApsaraVideo VOD or a third party.
        self.repeat_number = repeat_number
        # The number of retries allowed.
        self.retry_count = retry_count
        # The retry interval. Unit: seconds.
        self.retry_interval = retry_interval
        # The protocol of the source stream.
        self.source_protocol = source_protocol
        # The type of the source stream. Valid values:
        # 
        # *   live: a live stream
        # *   vod: a list of ApsaraVideo VOD resources
        # *   url: a list of video resources from a third party
        self.source_type = source_type
        # The source URLs.
        self.source_urls = source_urls
        # The start time of the task. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
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
        if self.callback_url is not None:
            result['CallbackURL'] = self.callback_url

        if self.dst_url is not None:
            result['DstUrl'] = self.dst_url

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.file_index is not None:
            result['FileIndex'] = self.file_index

        if self.offset is not None:
            result['Offset'] = self.offset

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
        if m.get('CallbackURL') is not None:
            self.callback_url = m.get('CallbackURL')

        if m.get('DstUrl') is not None:
            self.dst_url = m.get('DstUrl')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('FileIndex') is not None:
            self.file_index = m.get('FileIndex')

        if m.get('Offset') is not None:
            self.offset = m.get('Offset')

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
            self.source_urls = m.get('SourceUrls')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        return self

