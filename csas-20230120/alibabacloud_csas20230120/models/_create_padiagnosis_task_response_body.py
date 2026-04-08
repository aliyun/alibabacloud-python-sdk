# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class CreatePADiagnosisTaskResponseBody(DaraModel):
    def __init__(
        self,
        diagnosis_task: main_models.CreatePADiagnosisTaskResponseBodyDiagnosisTask = None,
        request_id: str = None,
    ):
        self.diagnosis_task = diagnosis_task
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.diagnosis_task:
            self.diagnosis_task.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.diagnosis_task is not None:
            result['DiagnosisTask'] = self.diagnosis_task.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiagnosisTask') is not None:
            temp_model = main_models.CreatePADiagnosisTaskResponseBodyDiagnosisTask()
            self.diagnosis_task = temp_model.from_map(m.get('DiagnosisTask'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreatePADiagnosisTaskResponseBodyDiagnosisTask(DaraModel):
    def __init__(
        self,
        dev_tag: str = None,
        diagnose_id: str = None,
        diagnose_type: str = None,
        host: str = None,
        pop_id: str = None,
        pop_mode: str = None,
        port: str = None,
        protocol: str = None,
        status: str = None,
        udp_extra_configs: main_models.CreatePADiagnosisTaskResponseBodyDiagnosisTaskUdpExtraConfigs = None,
        user_group: main_models.CreatePADiagnosisTaskResponseBodyDiagnosisTaskUserGroup = None,
        username: str = None,
    ):
        self.dev_tag = dev_tag
        self.diagnose_id = diagnose_id
        self.diagnose_type = diagnose_type
        self.host = host
        self.pop_id = pop_id
        self.pop_mode = pop_mode
        self.port = port
        self.protocol = protocol
        self.status = status
        self.udp_extra_configs = udp_extra_configs
        self.user_group = user_group
        self.username = username

    def validate(self):
        if self.udp_extra_configs:
            self.udp_extra_configs.validate()
        if self.user_group:
            self.user_group.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dev_tag is not None:
            result['DevTag'] = self.dev_tag

        if self.diagnose_id is not None:
            result['DiagnoseId'] = self.diagnose_id

        if self.diagnose_type is not None:
            result['DiagnoseType'] = self.diagnose_type

        if self.host is not None:
            result['Host'] = self.host

        if self.pop_id is not None:
            result['PopId'] = self.pop_id

        if self.pop_mode is not None:
            result['PopMode'] = self.pop_mode

        if self.port is not None:
            result['Port'] = self.port

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.status is not None:
            result['Status'] = self.status

        if self.udp_extra_configs is not None:
            result['UdpExtraConfigs'] = self.udp_extra_configs.to_map()

        if self.user_group is not None:
            result['UserGroup'] = self.user_group.to_map()

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DevTag') is not None:
            self.dev_tag = m.get('DevTag')

        if m.get('DiagnoseId') is not None:
            self.diagnose_id = m.get('DiagnoseId')

        if m.get('DiagnoseType') is not None:
            self.diagnose_type = m.get('DiagnoseType')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('PopId') is not None:
            self.pop_id = m.get('PopId')

        if m.get('PopMode') is not None:
            self.pop_mode = m.get('PopMode')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UdpExtraConfigs') is not None:
            temp_model = main_models.CreatePADiagnosisTaskResponseBodyDiagnosisTaskUdpExtraConfigs()
            self.udp_extra_configs = temp_model.from_map(m.get('UdpExtraConfigs'))

        if m.get('UserGroup') is not None:
            temp_model = main_models.CreatePADiagnosisTaskResponseBodyDiagnosisTaskUserGroup()
            self.user_group = temp_model.from_map(m.get('UserGroup'))

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

class CreatePADiagnosisTaskResponseBodyDiagnosisTaskUserGroup(DaraModel):
    def __init__(
        self,
        user_group_id: str = None,
        user_group_name: str = None,
    ):
        self.user_group_id = user_group_id
        self.user_group_name = user_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id

        if self.user_group_name is not None:
            result['UserGroupName'] = self.user_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')

        if m.get('UserGroupName') is not None:
            self.user_group_name = m.get('UserGroupName')

        return self

class CreatePADiagnosisTaskResponseBodyDiagnosisTaskUdpExtraConfigs(DaraModel):
    def __init__(
        self,
        expected_response: str = None,
        request_content: str = None,
    ):
        self.expected_response = expected_response
        self.request_content = request_content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expected_response is not None:
            result['ExpectedResponse'] = self.expected_response

        if self.request_content is not None:
            result['RequestContent'] = self.request_content

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpectedResponse') is not None:
            self.expected_response = m.get('ExpectedResponse')

        if m.get('RequestContent') is not None:
            self.request_content = m.get('RequestContent')

        return self

