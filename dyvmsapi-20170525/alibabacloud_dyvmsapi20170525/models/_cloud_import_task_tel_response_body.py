# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dyvmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class CloudImportTaskTelResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.CloudImportTaskTelResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.CloudImportTaskTelResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CloudImportTaskTelResponseBodyData(DaraModel):
    def __init__(
        self,
        file_id: str = None,
        import_total: str = None,
        invalid_total: str = None,
        success_total: str = None,
        task_id: str = None,
    ):
        # 批次Id
        self.file_id = file_id
        # 请求号码总数
        self.import_total = import_total
        # 非法号码数
        self.invalid_total = invalid_total
        # 成功导入号码数
        self.success_total = success_total
        # 任务Id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.import_total is not None:
            result['ImportTotal'] = self.import_total

        if self.invalid_total is not None:
            result['InvalidTotal'] = self.invalid_total

        if self.success_total is not None:
            result['SuccessTotal'] = self.success_total

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('ImportTotal') is not None:
            self.import_total = m.get('ImportTotal')

        if m.get('InvalidTotal') is not None:
            self.invalid_total = m.get('InvalidTotal')

        if m.get('SuccessTotal') is not None:
            self.success_total = m.get('SuccessTotal')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

