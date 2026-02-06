# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class ListTranscodeTaskResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        transcode_task_list: List[main_models.ListTranscodeTaskResponseBodyTranscodeTaskList] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # Details about transcoding tasks.
        self.transcode_task_list = transcode_task_list

    def validate(self):
        if self.transcode_task_list:
            for v1 in self.transcode_task_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TranscodeTaskList'] = []
        if self.transcode_task_list is not None:
            for k1 in self.transcode_task_list:
                result['TranscodeTaskList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.transcode_task_list = []
        if m.get('TranscodeTaskList') is not None:
            for k1 in m.get('TranscodeTaskList'):
                temp_model = main_models.ListTranscodeTaskResponseBodyTranscodeTaskList()
                self.transcode_task_list.append(temp_model.from_map(k1))

        return self

class ListTranscodeTaskResponseBodyTranscodeTaskList(DaraModel):
    def __init__(
        self,
        complete_time: str = None,
        creation_time: str = None,
        task_status: str = None,
        transcode_task_id: str = None,
        transcode_template_group_id: str = None,
        trigger: str = None,
        video_id: str = None,
    ):
        # The time when the transcoding task was complete. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.complete_time = complete_time
        # The time when the transcoding task was created. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The status of the transcoding task. Valid values:
        # *   **Processing**: In progress.
        # *   **Partial**: Some transcoding jobs were complete.
        # *   **CompleteAllSucc**: All transcoding jobs were successful.
        # *   **CompleteAllFail**: All transcoding jobs failed. If an exception occurs in the source file, no transcoding job is initiated and the transcoding task fails.
        # *   **CompletePartialSucc**: All transcoding jobs were complete but only some were successful.
        self.task_status = task_status
        # The ID of the transcoding task.
        self.transcode_task_id = transcode_task_id
        # The ID of the transcoding template group.
        self.transcode_template_group_id = transcode_template_group_id
        # The mode in which the transcoding task is triggered. Valid values:
        # *   **Auto**: The transcoding task is automatically triggered when the video is uploaded.
        # *   **Manual**: The transcoding task is triggered by calling the SubmitTranscodeJobs operation.
        self.trigger = trigger
        # The ID of the audio or video file.
        self.video_id = video_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.transcode_task_id is not None:
            result['TranscodeTaskId'] = self.transcode_task_id

        if self.transcode_template_group_id is not None:
            result['TranscodeTemplateGroupId'] = self.transcode_template_group_id

        if self.trigger is not None:
            result['Trigger'] = self.trigger

        if self.video_id is not None:
            result['VideoId'] = self.video_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('TranscodeTaskId') is not None:
            self.transcode_task_id = m.get('TranscodeTaskId')

        if m.get('TranscodeTemplateGroupId') is not None:
            self.transcode_template_group_id = m.get('TranscodeTemplateGroupId')

        if m.get('Trigger') is not None:
            self.trigger = m.get('Trigger')

        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')

        return self

