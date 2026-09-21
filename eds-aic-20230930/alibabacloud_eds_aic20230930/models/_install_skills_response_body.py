# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class InstallSkillsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        install_results: List[main_models.InstallSkillsResponseBodyInstallResults] = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code. A value of 200 indicates success.
        self.code = code
        # The installation results.
        self.install_results = install_results
        # The response message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.install_results:
            for v1 in self.install_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['InstallResults'] = []
        if self.install_results is not None:
            for k1 in self.install_results:
                result['InstallResults'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.install_results = []
        if m.get('InstallResults') is not None:
            for k1 in m.get('InstallResults'):
                temp_model = main_models.InstallSkillsResponseBodyInstallResults()
                self.install_results.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class InstallSkillsResponseBodyInstallResults(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        status: str = None,
    ):
        # The cloud phone instance ID.
        self.instance_id = instance_id
        # The installation status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

