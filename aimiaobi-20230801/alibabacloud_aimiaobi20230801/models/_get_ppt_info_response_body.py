# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class GetPptInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetPptInfoResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetPptInfoResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetPptInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        export_file_link: List[str] = None,
        export_task_id: str = None,
        ppt_artifact_cover: str = None,
        ppt_artifact_id: str = None,
        ppt_process_id: str = None,
        query: str = None,
        task_id: str = None,
    ):
        self.export_file_link = export_file_link
        self.export_task_id = export_task_id
        self.ppt_artifact_cover = ppt_artifact_cover
        self.ppt_artifact_id = ppt_artifact_id
        self.ppt_process_id = ppt_process_id
        self.query = query
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.export_file_link is not None:
            result['ExportFileLink'] = self.export_file_link

        if self.export_task_id is not None:
            result['ExportTaskId'] = self.export_task_id

        if self.ppt_artifact_cover is not None:
            result['PptArtifactCover'] = self.ppt_artifact_cover

        if self.ppt_artifact_id is not None:
            result['PptArtifactId'] = self.ppt_artifact_id

        if self.ppt_process_id is not None:
            result['PptProcessId'] = self.ppt_process_id

        if self.query is not None:
            result['Query'] = self.query

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExportFileLink') is not None:
            self.export_file_link = m.get('ExportFileLink')

        if m.get('ExportTaskId') is not None:
            self.export_task_id = m.get('ExportTaskId')

        if m.get('PptArtifactCover') is not None:
            self.ppt_artifact_cover = m.get('PptArtifactCover')

        if m.get('PptArtifactId') is not None:
            self.ppt_artifact_id = m.get('PptArtifactId')

        if m.get('PptProcessId') is not None:
            self.ppt_process_id = m.get('PptProcessId')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

