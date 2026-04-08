# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class CreatePADiagnosisTaskRequest(DaraModel):
    def __init__(
        self,
        dev_tag: str = None,
        diagnose_type: str = None,
        host: str = None,
        pop_id: str = None,
        pop_mode: str = None,
        port: str = None,
        protocol: str = None,
        udp_extra_configs: main_models.CreatePADiagnosisTaskRequestUdpExtraConfigs = None,
        user_group_id: str = None,
        username: str = None,
    ):
        self.dev_tag = dev_tag
        # This parameter is required.
        self.diagnose_type = diagnose_type
        # This parameter is required.
        self.host = host
        self.pop_id = pop_id
        # This parameter is required.
        self.pop_mode = pop_mode
        # This parameter is required.
        self.port = port
        # This parameter is required.
        self.protocol = protocol
        self.udp_extra_configs = udp_extra_configs
        self.user_group_id = user_group_id
        self.username = username

    def validate(self):
        if self.udp_extra_configs:
            self.udp_extra_configs.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dev_tag is not None:
            result['DevTag'] = self.dev_tag

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

        if self.udp_extra_configs is not None:
            result['UdpExtraConfigs'] = self.udp_extra_configs.to_map()

        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DevTag') is not None:
            self.dev_tag = m.get('DevTag')

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

        if m.get('UdpExtraConfigs') is not None:
            temp_model = main_models.CreatePADiagnosisTaskRequestUdpExtraConfigs()
            self.udp_extra_configs = temp_model.from_map(m.get('UdpExtraConfigs'))

        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

class CreatePADiagnosisTaskRequestUdpExtraConfigs(DaraModel):
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

