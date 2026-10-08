# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class StopPipelineIntegratedTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.StopPipelineIntegratedTaskResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
            temp_model = main_models.StopPipelineIntegratedTaskResponseBodyData()
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

class StopPipelineIntegratedTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        dev_ops_action_res_dtolist: List[main_models.StopPipelineIntegratedTaskResponseBodyDataDevOpsActionResDTOList] = None,
        fail: int = None,
        success: int = None,
    ):
        self.dev_ops_action_res_dtolist = dev_ops_action_res_dtolist
        self.fail = fail
        self.success = success

    def validate(self):
        if self.dev_ops_action_res_dtolist:
            for v1 in self.dev_ops_action_res_dtolist:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DevOpsActionResDTOList'] = []
        if self.dev_ops_action_res_dtolist is not None:
            for k1 in self.dev_ops_action_res_dtolist:
                result['DevOpsActionResDTOList'].append(k1.to_map() if k1 else None)

        if self.fail is not None:
            result['Fail'] = self.fail

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dev_ops_action_res_dtolist = []
        if m.get('DevOpsActionResDTOList') is not None:
            for k1 in m.get('DevOpsActionResDTOList'):
                temp_model = main_models.StopPipelineIntegratedTaskResponseBodyDataDevOpsActionResDTOList()
                self.dev_ops_action_res_dtolist.append(temp_model.from_map(k1))

        if m.get('Fail') is not None:
            self.fail = m.get('Fail')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class StopPipelineIntegratedTaskResponseBodyDataDevOpsActionResDTOList(DaraModel):
    def __init__(
        self,
        job_name: str = None,
        owner: str = None,
        status: str = None,
    ):
        self.job_name = job_name
        self.owner = owner
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

