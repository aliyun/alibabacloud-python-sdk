# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class GetVideoModerationResultResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        end_time: str = None,
        event_id: str = None,
        message: str = None,
        moderation_result: main_models.GetVideoModerationResultResponseBodyModerationResult = None,
        project_name: str = None,
        request_id: str = None,
        start_time: str = None,
        status: str = None,
        task_id: str = None,
        task_type: str = None,
        user_data: str = None,
    ):
        # The error code of the task.
        self.code = code
        # The end time of the task.
        self.end_time = end_time
        # The event ID.
        self.event_id = event_id
        # The error message of the task.
        self.message = message
        # The result of the image compliance detection task.
        self.moderation_result = moderation_result
        # The project name.
        self.project_name = project_name
        # The request ID.
        self.request_id = request_id
        # The start time of the task.
        self.start_time = start_time
        # The task status. Valid values:
        # 
        # *   Running: The task is running.
        # *   Succeeded: The task is successful.
        # *   Failed: The task failed.
        self.status = status
        # The task ID.
        self.task_id = task_id
        # The type of the task.
        self.task_type = task_type
        # The user-defined data.
        self.user_data = user_data

    def validate(self):
        if self.moderation_result:
            self.moderation_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.message is not None:
            result['Message'] = self.message

        if self.moderation_result is not None:
            result['ModerationResult'] = self.moderation_result.to_map()

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('ModerationResult') is not None:
            temp_model = main_models.GetVideoModerationResultResponseBodyModerationResult()
            self.moderation_result = temp_model.from_map(m.get('ModerationResult'))

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class GetVideoModerationResultResponseBodyModerationResult(DaraModel):
    def __init__(
        self,
        categories: List[str] = None,
        frames: main_models.GetVideoModerationResultResponseBodyModerationResultFrames = None,
        suggestion: str = None,
        uri: str = None,
    ):
        # The category list.
        self.categories = categories
        # The information about video and motion detection frames.
        self.frames = frames
        # The recommended operation. Valid values:
        # 
        # *   pass: The image has passed the check. No action is required.
        # *   review: The image contains suspected violations and requires human review.
        # *   block: The image contains violations. Further actions, such as deleting or blocking the image, are recommended.
        self.suggestion = suggestion
        # The OSS URI of the file. The URI follows the oss://${bucketname}/${objectname} format. bucketname indicates the name of an OSS bucket that is in the same region as the current project, and objectname is the file path.
        self.uri = uri

    def validate(self):
        if self.frames:
            self.frames.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.categories is not None:
            result['Categories'] = self.categories

        if self.frames is not None:
            result['Frames'] = self.frames.to_map()

        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion

        if self.uri is not None:
            result['URI'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')

        if m.get('Frames') is not None:
            temp_model = main_models.GetVideoModerationResultResponseBodyModerationResultFrames()
            self.frames = temp_model.from_map(m.get('Frames'))

        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')

        if m.get('URI') is not None:
            self.uri = m.get('URI')

        return self

class GetVideoModerationResultResponseBodyModerationResultFrames(DaraModel):
    def __init__(
        self,
        block_frames: List[main_models.GetVideoModerationResultResponseBodyModerationResultFramesBlockFrames] = None,
        total_count: int = None,
    ):
        # The information about violated frames.
        self.block_frames = block_frames
        # The total number of detected frames.
        self.total_count = total_count

    def validate(self):
        if self.block_frames:
            for v1 in self.block_frames:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BlockFrames'] = []
        if self.block_frames is not None:
            for k1 in self.block_frames:
                result['BlockFrames'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.block_frames = []
        if m.get('BlockFrames') is not None:
            for k1 in m.get('BlockFrames'):
                temp_model = main_models.GetVideoModerationResultResponseBodyModerationResultFramesBlockFrames()
                self.block_frames.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class GetVideoModerationResultResponseBodyModerationResultFramesBlockFrames(DaraModel):
    def __init__(
        self,
        label: str = None,
        offset: int = None,
        rate: float = None,
    ):
        # The label of the violation.
        self.label = label
        # The offset of the frame.
        self.offset = offset
        # The confidence level of the violation.
        self.rate = rate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label is not None:
            result['Label'] = self.label

        if self.offset is not None:
            result['Offset'] = self.offset

        if self.rate is not None:
            result['Rate'] = self.rate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Offset') is not None:
            self.offset = m.get('Offset')

        if m.get('Rate') is not None:
            self.rate = m.get('Rate')

        return self

