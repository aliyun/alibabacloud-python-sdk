# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class BatchGetYikeAIAppJobResponseBody(DaraModel):
    def __init__(
        self,
        job_list: List[main_models.BatchGetYikeAIAppJobResponseBodyJobList] = None,
        request_id: str = None,
    ):
        # The list of jobs. Each object mirrors the details returned by the `GetYikeAIAppJob` operation.
        self.job_list = job_list
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.job_list:
            for v1 in self.job_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['JobList'] = []
        if self.job_list is not None:
            for k1 in self.job_list:
                result['JobList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.job_list = []
        if m.get('JobList') is not None:
            for k1 in m.get('JobList'):
                temp_model = main_models.BatchGetYikeAIAppJobResponseBodyJobList()
                self.job_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class BatchGetYikeAIAppJobResponseBodyJobList(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_input_config: str = None,
        execution_finish_time: str = None,
        execution_start_time: str = None,
        folder_id: str = None,
        job_id: str = None,
        production_id: str = None,
        result: main_models.BatchGetYikeAIAppJobResponseBodyJobListResult = None,
        status: str = None,
    ):
        # The ID of the application.
        self.app_id = app_id
        # The AI application\\"s input parameters, formatted as a JSON-serialized string.
        self.app_input_config = app_input_config
        # The time the job execution finished. The time is in UTC and formatted as `yyyy-MM-ddTHH:mm:ssZ`.
        self.execution_finish_time = execution_finish_time
        # The time the job execution started. The time is in UTC and formatted as `yyyy-MM-ddTHH:mm:ssZ`.
        self.execution_start_time = execution_start_time
        # The ID of the folder.
        self.folder_id = folder_id
        # The ID of the job.
        self.job_id = job_id
        # The ID of the project.
        self.production_id = production_id
        # The execution result of the job.
        self.result = result
        # The status of the job. Valid values are:
        # 
        # - `Created`: The job has been created.
        # 
        # - `Queuing`: The job is in the queue.
        # 
        # - `Executing`: The job is executing.
        # 
        # - `Finished`: The job completed successfully.
        # 
        # - `Failed`: The job failed to complete.
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

        if self.app_input_config is not None:
            result['AppInputConfig'] = self.app_input_config

        if self.execution_finish_time is not None:
            result['ExecutionFinishTime'] = self.execution_finish_time

        if self.execution_start_time is not None:
            result['ExecutionStartTime'] = self.execution_start_time

        if self.folder_id is not None:
            result['FolderId'] = self.folder_id

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.production_id is not None:
            result['ProductionId'] = self.production_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppInputConfig') is not None:
            self.app_input_config = m.get('AppInputConfig')

        if m.get('ExecutionFinishTime') is not None:
            self.execution_finish_time = m.get('ExecutionFinishTime')

        if m.get('ExecutionStartTime') is not None:
            self.execution_start_time = m.get('ExecutionStartTime')

        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('ProductionId') is not None:
            self.production_id = m.get('ProductionId')

        if m.get('Result') is not None:
            temp_model = main_models.BatchGetYikeAIAppJobResponseBodyJobListResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class BatchGetYikeAIAppJobResponseBodyJobListResult(DaraModel):
    def __init__(
        self,
        audio_result: List[main_models.BatchGetYikeAIAppJobResponseBodyJobListResultAudioResult] = None,
        image_result: List[main_models.BatchGetYikeAIAppJobResponseBodyJobListResultImageResult] = None,
        video_result: List[main_models.BatchGetYikeAIAppJobResponseBodyJobListResultVideoResult] = None,
    ):
        # The audio result.
        self.audio_result = audio_result
        # The image result.
        self.image_result = image_result
        # The video result.
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
                temp_model = main_models.BatchGetYikeAIAppJobResponseBodyJobListResultAudioResult()
                self.audio_result.append(temp_model.from_map(k1))

        self.image_result = []
        if m.get('ImageResult') is not None:
            for k1 in m.get('ImageResult'):
                temp_model = main_models.BatchGetYikeAIAppJobResponseBodyJobListResultImageResult()
                self.image_result.append(temp_model.from_map(k1))

        self.video_result = []
        if m.get('VideoResult') is not None:
            for k1 in m.get('VideoResult'):
                temp_model = main_models.BatchGetYikeAIAppJobResponseBodyJobListResultVideoResult()
                self.video_result.append(temp_model.from_map(k1))

        return self

class BatchGetYikeAIAppJobResponseBodyJobListResultVideoResult(DaraModel):
    def __init__(
        self,
        media_id: str = None,
        output_url: str = None,
    ):
        # The ID of the media asset.
        self.media_id = media_id
        # The output URL.
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

class BatchGetYikeAIAppJobResponseBodyJobListResultImageResult(DaraModel):
    def __init__(
        self,
        media_id: str = None,
        output_url: str = None,
    ):
        # The ID of the media asset.
        self.media_id = media_id
        # The output URL.
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

class BatchGetYikeAIAppJobResponseBodyJobListResultAudioResult(DaraModel):
    def __init__(
        self,
        media_id: str = None,
        output_url: str = None,
    ):
        # The ID of the media asset.
        self.media_id = media_id
        # The output URL.
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

