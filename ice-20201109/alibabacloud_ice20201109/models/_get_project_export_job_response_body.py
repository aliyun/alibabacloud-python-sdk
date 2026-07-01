# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class GetProjectExportJobResponseBody(DaraModel):
    def __init__(
        self,
        project_export_job: main_models.GetProjectExportJobResponseBodyProjectExportJob = None,
        request_id: str = None,
    ):
        # The project export task.
        self.project_export_job = project_export_job
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.project_export_job:
            self.project_export_job.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.project_export_job is not None:
            result['ProjectExportJob'] = self.project_export_job.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectExportJob') is not None:
            temp_model = main_models.GetProjectExportJobResponseBodyProjectExportJob()
            self.project_export_job = temp_model.from_map(m.get('ProjectExportJob'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetProjectExportJobResponseBodyProjectExportJob(DaraModel):
    def __init__(
        self,
        code: str = None,
        export_result: main_models.GetProjectExportJobResponseBodyProjectExportJobExportResult = None,
        export_type: str = None,
        job_id: str = None,
        message: str = None,
        project_id: str = None,
        status: str = None,
        user_data: str = None,
    ):
        # The error code of the project export task.
        # >Notice: Check this field when the task fails.
        self.code = code
        # The export result.
        self.export_result = export_result
        # The type of the project export. Valid values:
        # - **BaseTimeline**: timeline.
        # - **AdobePremierePro**: Adobe Premiere Pro project.
        self.export_type = export_type
        # The ID of the project export task.
        self.job_id = job_id
        # The error message of the project export task.
        # 
        # >Notice: Check this field when the task fails.
        self.message = message
        # The ID of the online editing project.
        self.project_id = project_id
        # The status of the project export task. Valid values:
        # - **Init**: initial state.
        # - **Processing**: processing.
        # - **Success**: succeeded.
        # - **Failed**: failed.
        self.status = status
        # The custom settings in JSON format.
        self.user_data = user_data

    def validate(self):
        if self.export_result:
            self.export_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.export_result is not None:
            result['ExportResult'] = self.export_result.to_map()

        if self.export_type is not None:
            result['ExportType'] = self.export_type

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.message is not None:
            result['Message'] = self.message

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.status is not None:
            result['Status'] = self.status

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('ExportResult') is not None:
            temp_model = main_models.GetProjectExportJobResponseBodyProjectExportJobExportResult()
            self.export_result = temp_model.from_map(m.get('ExportResult'))

        if m.get('ExportType') is not None:
            self.export_type = m.get('ExportType')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class GetProjectExportJobResponseBodyProjectExportJobExportResult(DaraModel):
    def __init__(
        self,
        audio_url: str = None,
        project_url: str = None,
        srt_list: List[main_models.GetProjectExportJobResponseBodyProjectExportJobExportResultSrtList] = None,
        timeline: str = None,
    ):
        self.audio_url = audio_url
        # The file URL of the exported project, which is typically an authenticated OSS URL. This field is returned when the export type is AdobePremierePro.
        self.project_url = project_url
        self.srt_list = srt_list
        # The online editing timeline. This field is returned when the export type is BaseTimeline. For more information about the structure, see [Timeline configuration](https://help.aliyun.com/document_detail/198823.html).
        self.timeline = timeline

    def validate(self):
        if self.srt_list:
            for v1 in self.srt_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio_url is not None:
            result['AudioUrl'] = self.audio_url

        if self.project_url is not None:
            result['ProjectUrl'] = self.project_url

        result['SrtList'] = []
        if self.srt_list is not None:
            for k1 in self.srt_list:
                result['SrtList'].append(k1.to_map() if k1 else None)

        if self.timeline is not None:
            result['Timeline'] = self.timeline

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioUrl') is not None:
            self.audio_url = m.get('AudioUrl')

        if m.get('ProjectUrl') is not None:
            self.project_url = m.get('ProjectUrl')

        self.srt_list = []
        if m.get('SrtList') is not None:
            for k1 in m.get('SrtList'):
                temp_model = main_models.GetProjectExportJobResponseBodyProjectExportJobExportResultSrtList()
                self.srt_list.append(temp_model.from_map(k1))

        if m.get('Timeline') is not None:
            self.timeline = m.get('Timeline')

        return self

class GetProjectExportJobResponseBodyProjectExportJobExportResultSrtList(DaraModel):
    def __init__(
        self,
        srt_url: str = None,
        tag: str = None,
    ):
        self.srt_url = srt_url
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.srt_url is not None:
            result['SrtUrl'] = self.srt_url

        if self.tag is not None:
            result['Tag'] = self.tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SrtUrl') is not None:
            self.srt_url = m.get('SrtUrl')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        return self

