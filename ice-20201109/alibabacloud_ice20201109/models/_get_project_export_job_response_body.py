# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

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
        # The ID of the request.
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
        # The error code for the failed export task.
        # >Notice: Use the error code for troubleshooting.
        self.code = code
        # The exported data.
        self.export_result = export_result
        # The export type. Valid values:
        # 
        # *   **BaseTimeline**: exports the timeline.
        # *   **AdobePremierePro**: exports an Adobe Premiere Pro project.
        self.export_type = export_type
        # The ID of the project export task.
        self.job_id = job_id
        # The error message for the failed export task.
        # >Notice: Use the error message for troubleshooting.
        self.message = message
        # The ID of the online editing project.
        self.project_id = project_id
        # The status of the project export task. Valid values:
        # 
        # - Init: Initializing
        # - Processing
        # - Success
        # - Failed
        self.status = status
        # The user-defined data in the JSON format.
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
        project_url: str = None,
        timeline: str = None,
    ):
        # The URL of the exported project, which is typically a signed OSS URL. This field is returned when ExportType is AdobePremierePro.
        self.project_url = project_url
        # The timeline of the online editing job. This field is returned when ExportType is BaseTimeline. For data structure, see [Timeline](https://help.aliyun.com/document_detail/198823.html).
        self.timeline = timeline

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.project_url is not None:
            result['ProjectUrl'] = self.project_url

        if self.timeline is not None:
            result['Timeline'] = self.timeline

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectUrl') is not None:
            self.project_url = m.get('ProjectUrl')

        if m.get('Timeline') is not None:
            self.timeline = m.get('Timeline')

        return self

