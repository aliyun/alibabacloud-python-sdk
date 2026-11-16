# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yike20260707 import models as main_models
from darabonba.model import DaraModel

class GetVideoCharacterReplaceJobResponseBody(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_params: str = None,
        execution_finish_time: str = None,
        execution_start_time: str = None,
        folder_id: str = None,
        job_id: str = None,
        project_id: str = None,
        request_id: str = None,
        result: main_models.GetVideoCharacterReplaceJobResponseBodyResult = None,
        status: str = None,
    ):
        # The ID of the video character replacement application. Use a configured application.
        self.app_id = app_id
        # The application input parameters, which are serialized into a JSON string. The field names and material requirements are subject to the input definition of the corresponding AppId.
        self.app_params = app_params
        # The time when the task finished execution, in ISO 8601 format with time zone.
        self.execution_finish_time = execution_finish_time
        # The time when the task started execution, in ISO 8601 format with time zone.
        self.execution_start_time = execution_start_time
        # The folder ID.
        self.folder_id = folder_id
        # The task ID, which is returned by SubmitVideoCharacterReplaceJob.
        self.job_id = job_id
        # The project ID.
        self.project_id = project_id
        # The request ID, which is used to locate and troubleshoot the request.
        self.request_id = request_id
        # The task output results, which are categorized by image, video, and audio.
        self.result = result
        # The task status. Valid values:
        # - Created: The task is created.
        # - Queuing: The task is queuing.
        # - Executing: The task is executing.
        # - Finished: The task is finished.
        # - Failed: The task failed.
        self.status = status

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_params is not None:
            result['AppParams'] = self.app_params

        if self.execution_finish_time is not None:
            result['ExecutionFinishTime'] = self.execution_finish_time

        if self.execution_start_time is not None:
            result['ExecutionStartTime'] = self.execution_start_time

        if self.folder_id is not None:
            result['FolderId'] = self.folder_id

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppParams') is not None:
            self.app_params = m.get('AppParams')

        if m.get('ExecutionFinishTime') is not None:
            self.execution_finish_time = m.get('ExecutionFinishTime')

        if m.get('ExecutionStartTime') is not None:
            self.execution_start_time = m.get('ExecutionStartTime')

        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.GetVideoCharacterReplaceJobResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetVideoCharacterReplaceJobResponseBodyResult(DaraModel):
    def __init__(
        self,
        audio_result: List[main_models.GetVideoCharacterReplaceJobResponseBodyResultAudioResult] = None,
        image_result: List[main_models.GetVideoCharacterReplaceJobResponseBodyResultImageResult] = None,
        video_result: List[main_models.GetVideoCharacterReplaceJobResponseBodyResultVideoResult] = None,
    ):
        # The list of output audio.
        self.audio_result = audio_result
        # The list of output images.
        self.image_result = image_result
        # The list of output videos.
        self.video_result = video_result

    def validate(self):
        if self.audio_result:
            for v1 in self.audio_result:
                 if v1:
                    v1.validate()
        if self.image_result:
            for v1 in self.image_result:
                 if v1:
                    v1.validate()
        if self.video_result:
            for v1 in self.video_result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AudioResult'] = []
        if self.audio_result is not None:
            for k1 in self.audio_result:
                result['AudioResult'].append(k1.to_map() if k1 else None)

        result['ImageResult'] = []
        if self.image_result is not None:
            for k1 in self.image_result:
                result['ImageResult'].append(k1.to_map() if k1 else None)

        result['VideoResult'] = []
        if self.video_result is not None:
            for k1 in self.video_result:
                result['VideoResult'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.audio_result = []
        if m.get('AudioResult') is not None:
            for k1 in m.get('AudioResult'):
                temp_model = main_models.GetVideoCharacterReplaceJobResponseBodyResultAudioResult()
                self.audio_result.append(temp_model.from_map(k1))

        self.image_result = []
        if m.get('ImageResult') is not None:
            for k1 in m.get('ImageResult'):
                temp_model = main_models.GetVideoCharacterReplaceJobResponseBodyResultImageResult()
                self.image_result.append(temp_model.from_map(k1))

        self.video_result = []
        if m.get('VideoResult') is not None:
            for k1 in m.get('VideoResult'):
                temp_model = main_models.GetVideoCharacterReplaceJobResponseBodyResultVideoResult()
                self.video_result.append(temp_model.from_map(k1))

        return self

class GetVideoCharacterReplaceJobResponseBodyResultVideoResult(DaraModel):
    def __init__(
        self,
        media_id: str = None,
        output_url: str = None,
    ):
        # The output media asset ID.
        self.media_id = media_id
        # The download URL of the output media asset.
        self.output_url = output_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.output_url is not None:
            result['OutputUrl'] = self.output_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('OutputUrl') is not None:
            self.output_url = m.get('OutputUrl')

        return self

class GetVideoCharacterReplaceJobResponseBodyResultImageResult(DaraModel):
    def __init__(
        self,
        media_id: str = None,
        output_url: str = None,
    ):
        # The output media asset ID.
        self.media_id = media_id
        # The download URL of the output media asset.
        self.output_url = output_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.output_url is not None:
            result['OutputUrl'] = self.output_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('OutputUrl') is not None:
            self.output_url = m.get('OutputUrl')

        return self

class GetVideoCharacterReplaceJobResponseBodyResultAudioResult(DaraModel):
    def __init__(
        self,
        media_id: str = None,
        output_url: str = None,
    ):
        # The output media asset ID.
        self.media_id = media_id
        # The download URL of the output media asset.
        self.output_url = output_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.output_url is not None:
            result['OutputUrl'] = self.output_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('OutputUrl') is not None:
            self.output_url = m.get('OutputUrl')

        return self

