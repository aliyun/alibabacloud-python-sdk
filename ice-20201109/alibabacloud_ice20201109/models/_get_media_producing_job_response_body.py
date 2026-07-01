# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class GetMediaProducingJobResponseBody(DaraModel):
    def __init__(
        self,
        media_producing_job: main_models.GetMediaProducingJobResponseBodyMediaProducingJob = None,
        request_id: str = None,
    ):
        # The details of the media producing job.
        self.media_producing_job = media_producing_job
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.media_producing_job:
            self.media_producing_job.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media_producing_job is not None:
            result['MediaProducingJob'] = self.media_producing_job.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaProducingJob') is not None:
            temp_model = main_models.GetMediaProducingJobResponseBodyMediaProducingJob()
            self.media_producing_job = temp_model.from_map(m.get('MediaProducingJob'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetMediaProducingJobResponseBodyMediaProducingJob(DaraModel):
    def __init__(
        self,
        clips_param: str = None,
        code: str = None,
        complete_time: str = None,
        create_time: str = None,
        duration: float = None,
        job_id: str = None,
        media_id: str = None,
        media_url: str = None,
        message: str = None,
        modified_time: str = None,
        progress: int = None,
        project_id: str = None,
        status: str = None,
        sub_job_materials: str = None,
        template_id: str = None,
        timeline: str = None,
        user_data: str = None,
        vod_media_id: str = None,
    ):
        # The clip parameters of the template used for the job.
        self.clips_param = clips_param
        # The error code of the media producing job. >Notice: This parameter is returned only if the job fails.
        self.code = code
        # The time in UTC when the media producing job was completed, formatted as `YYYY-MM-DD\\"T\\"hh:mm:ss\\"Z\\"`.
        self.complete_time = complete_time
        # The time in UTC when the media producing job was created, formatted as `YYYY-MM-DD\\"T\\"hh:mm:ss\\"Z\\"`.
        self.create_time = create_time
        # The duration of the output media. >Notice: This parameter is returned only if the job is successful and the output is an audio or video file.
        self.duration = duration
        # The job ID.
        self.job_id = job_id
        # The ID of the output media asset.
        self.media_id = media_id
        # The URL of the output media file.
        self.media_url = media_url
        # The error message of the media producing job.
        # 
        # >Notice: 
        # 
        # This parameter is returned only if the job fails.
        self.message = message
        # The time in UTC when the media producing job was last modified, formatted as `YYYY-MM-DD\\"T\\"hh:mm:ss\\"Z\\"`.
        self.modified_time = modified_time
        # The progress of the job. Valid values: 0 to 100.
        self.progress = progress
        # The project ID.
        self.project_id = project_id
        # The status of the media producing job. Valid values:
        # 
        # - `Init` (Initialized)
        # 
        # - `Queuing` (In queue)
        # 
        # - `Processing` (In progress)
        # 
        # - `Success` (Successful)
        # 
        # - `Failed` (Failed)
        self.status = status
        # If the job is a subtask of a batch smart one-click video creation task, this parameter contains the subtask\\"s materials, such as the title and speech script.
        self.sub_job_materials = sub_job_materials
        # The ID of the template used for the job.
        self.template_id = template_id
        # The timeline of the media producing job.
        self.timeline = timeline
        # The user data, in JSON format.
        self.user_data = user_data
        # The ID of the media asset in VOD (Video on Demand). This ID is returned if the job\\"s output is stored in VOD.
        self.vod_media_id = vod_media_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.clips_param is not None:
            result['ClipsParam'] = self.clips_param

        if self.code is not None:
            result['Code'] = self.code

        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.media_url is not None:
            result['MediaURL'] = self.media_url

        if self.message is not None:
            result['Message'] = self.message

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.status is not None:
            result['Status'] = self.status

        if self.sub_job_materials is not None:
            result['SubJobMaterials'] = self.sub_job_materials

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.timeline is not None:
            result['Timeline'] = self.timeline

        if self.user_data is not None:
            result['UserData'] = self.user_data

        if self.vod_media_id is not None:
            result['VodMediaId'] = self.vod_media_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClipsParam') is not None:
            self.clips_param = m.get('ClipsParam')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('MediaURL') is not None:
            self.media_url = m.get('MediaURL')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubJobMaterials') is not None:
            self.sub_job_materials = m.get('SubJobMaterials')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('Timeline') is not None:
            self.timeline = m.get('Timeline')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('VodMediaId') is not None:
            self.vod_media_id = m.get('VodMediaId')

        return self

