# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class MediaConvertOutputDetail(DaraModel):
    def __init__(
        self,
        code: str = None,
        create_time: str = None,
        finish_time: str = None,
        message: str = None,
        name: str = None,
        result: main_models.MediaConvertOutputDetailResult = None,
        status: str = None,
        task_id: str = None,
    ):
        # The error code for a failed task.
        self.code = code
        # The time the output task was created, in UTC format (*yyyy-MM-dd*T*HH:mm:ss*Z)
        self.create_time = create_time
        # The time the output task finished, in UTC format (*yyyy-MM-dd*T*HH:mm:ss*Z)
        self.finish_time = finish_time
        # The reason for a task failure.
        self.message = message
        # The name of the output.
        self.name = name
        # The detailed output results.
        self.result = result
        # The task status. Valid values:
        # 
        # *   Init: Initializing the task.
        # *   Scheduled: The task is scheduled for processing.
        # *   Success: The task is completed.
        # *   Failed: The task failed.
        # *   Skipped: The task was skipped.
        self.status = status
        # The task ID.
        self.task_id = task_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.message is not None:
            result['Message'] = self.message

        if self.name is not None:
            result['Name'] = self.name

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Result') is not None:
            temp_model = main_models.MediaConvertOutputDetailResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

class MediaConvertOutputDetailResult(DaraModel):
    def __init__(
        self,
        out_file_meta: main_models.MediaConvertOutputDetailFileMeta = None,
        output_file: main_models.MediaConvertOutputDetailResultOutputFile = None,
    ):
        # The metadata of the audio and video streams.
        self.out_file_meta = out_file_meta
        # Details about the generated output file.
        self.output_file = output_file

    def validate(self):
        if self.out_file_meta:
            self.out_file_meta.validate()
        if self.output_file:
            self.output_file.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.out_file_meta is not None:
            result['OutFileMeta'] = self.out_file_meta.to_map()

        if self.output_file is not None:
            result['OutputFile'] = self.output_file.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutFileMeta') is not None:
            temp_model = main_models.MediaConvertOutputDetailFileMeta()
            self.out_file_meta = temp_model.from_map(m.get('OutFileMeta'))

        if m.get('OutputFile') is not None:
            temp_model = main_models.MediaConvertOutputDetailResultOutputFile()
            self.output_file = temp_model.from_map(m.get('OutputFile'))

        return self

class MediaConvertOutputDetailResultOutputFile(DaraModel):
    def __init__(
        self,
        media: str = None,
        type: str = None,
        url: str = None,
    ):
        # The value depends on the Type field:
        # 
        # *   If Type is set to OSS, the value is the URL of the output file. The following formats are supported: oss://... and https://...
        # *   If Type is set to Media, the value is the ID of the media asset.
        self.media = media
        # The type of the output file. Valid values:
        # 
        # *   OSS: an Object Storage Service (OSS) object.
        # *   Media: a media asset.
        self.type = type
        # If Type is set to Media, this field provides the actual storage URL of the media asset.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media is not None:
            result['Media'] = self.media

        if self.type is not None:
            result['Type'] = self.type

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Media') is not None:
            self.media = m.get('Media')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

