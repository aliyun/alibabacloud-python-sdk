# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class InitiatePptCreationV2ResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.InitiatePptCreationV2ResponseBodyData = None,
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
            temp_model = main_models.InitiatePptCreationV2ResponseBodyData()
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

class InitiatePptCreationV2ResponseBodyData(DaraModel):
    def __init__(
        self,
        app_key: str = None,
        export_task_id: str = None,
        ppt_artifact_cover: str = None,
        ppt_artifact_id: str = None,
        ppt_process_id: str = None,
        signature: str = None,
    ):
        self.app_key = app_key
        self.export_task_id = export_task_id
        self.ppt_artifact_cover = ppt_artifact_cover
        self.ppt_artifact_id = ppt_artifact_id
        self.ppt_process_id = ppt_process_id
        self.signature = signature

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_key is not None:
            result['AppKey'] = self.app_key

        if self.export_task_id is not None:
            result['ExportTaskId'] = self.export_task_id

        if self.ppt_artifact_cover is not None:
            result['PptArtifactCover'] = self.ppt_artifact_cover

        if self.ppt_artifact_id is not None:
            result['PptArtifactId'] = self.ppt_artifact_id

        if self.ppt_process_id is not None:
            result['PptProcessId'] = self.ppt_process_id

        if self.signature is not None:
            result['Signature'] = self.signature

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('ExportTaskId') is not None:
            self.export_task_id = m.get('ExportTaskId')

        if m.get('PptArtifactCover') is not None:
            self.ppt_artifact_cover = m.get('PptArtifactCover')

        if m.get('PptArtifactId') is not None:
            self.ppt_artifact_id = m.get('PptArtifactId')

        if m.get('PptProcessId') is not None:
            self.ppt_process_id = m.get('PptProcessId')

        if m.get('Signature') is not None:
            self.signature = m.get('Signature')

        return self

