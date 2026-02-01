# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sysom20231230 import models as main_models
from darabonba.model import DaraModel

class GetVmcoreDiagnosisTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetVmcoreDiagnosisTaskResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetVmcoreDiagnosisTaskResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetVmcoreDiagnosisTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        diagnose_result: str = None,
        error_msg: str = None,
        task_id: str = None,
        task_status: str = None,
        task_type: str = None,
        urls: main_models.GetVmcoreDiagnosisTaskResponseBodyDataUrls = None,
    ):
        self.created_at = created_at
        self.diagnose_result = diagnose_result
        self.error_msg = error_msg
        self.task_id = task_id
        self.task_status = task_status
        self.task_type = task_type
        self.urls = urls

    def validate(self):
        if self.urls:
            self.urls.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.diagnose_result is not None:
            result['diagnoseResult'] = self.diagnose_result

        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.task_status is not None:
            result['taskStatus'] = self.task_status

        if self.task_type is not None:
            result['taskType'] = self.task_type

        if self.urls is not None:
            result['urls'] = self.urls.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('diagnoseResult') is not None:
            self.diagnose_result = m.get('diagnoseResult')

        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('taskStatus') is not None:
            self.task_status = m.get('taskStatus')

        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')

        if m.get('urls') is not None:
            temp_model = main_models.GetVmcoreDiagnosisTaskResponseBodyDataUrls()
            self.urls = temp_model.from_map(m.get('urls'))

        return self

class GetVmcoreDiagnosisTaskResponseBodyDataUrls(DaraModel):
    def __init__(
        self,
        debuginfo_common_url: str = None,
        debuginfo_url: str = None,
        dmesg_url: str = None,
        vmcore_url: str = None,
    ):
        self.debuginfo_common_url = debuginfo_common_url
        self.debuginfo_url = debuginfo_url
        self.dmesg_url = dmesg_url
        self.vmcore_url = vmcore_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.debuginfo_common_url is not None:
            result['debuginfoCommonUrl'] = self.debuginfo_common_url

        if self.debuginfo_url is not None:
            result['debuginfoUrl'] = self.debuginfo_url

        if self.dmesg_url is not None:
            result['dmesgUrl'] = self.dmesg_url

        if self.vmcore_url is not None:
            result['vmcoreUrl'] = self.vmcore_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('debuginfoCommonUrl') is not None:
            self.debuginfo_common_url = m.get('debuginfoCommonUrl')

        if m.get('debuginfoUrl') is not None:
            self.debuginfo_url = m.get('debuginfoUrl')

        if m.get('dmesgUrl') is not None:
            self.dmesg_url = m.get('dmesgUrl')

        if m.get('vmcoreUrl') is not None:
            self.vmcore_url = m.get('vmcoreUrl')

        return self

