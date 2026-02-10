# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetModuleConfigStatusResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetModuleConfigStatusResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetModuleConfigStatusResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetModuleConfigStatusResponseBodyData(DaraModel):
    def __init__(
        self,
        module_config_results: List[main_models.GetModuleConfigStatusResponseBodyDataModuleConfigResults] = None,
    ):
        # The check results of the service modules.
        self.module_config_results = module_config_results

    def validate(self):
        if self.module_config_results:
            for v1 in self.module_config_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ModuleConfigResults'] = []
        if self.module_config_results is not None:
            for k1 in self.module_config_results:
                result['ModuleConfigResults'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.module_config_results = []
        if m.get('ModuleConfigResults') is not None:
            for k1 in m.get('ModuleConfigResults'):
                temp_model = main_models.GetModuleConfigStatusResponseBodyDataModuleConfigResults()
                self.module_config_results.append(temp_model.from_map(k1))

        return self

class GetModuleConfigStatusResponseBodyDataModuleConfigResults(DaraModel):
    def __init__(
        self,
        module_name: str = None,
        pass_: bool = None,
    ):
        # The name of the check item. Valid values:
        # 
        # *   **Ransom**: The anti-ransomware policy is enabled.
        # *   **WebLock**: The web tamper proofing feature is enabled.
        # *   **Rasp**: Applications are added to the application protection feature.
        # *   **Image**: The container images that can be scanned are specified.
        # *   **Virus**: The periodic virus scan policy is enabled.
        self.module_name = module_name
        # Indicates whether the service module passed the status check. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.pass_ = pass_

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.module_name is not None:
            result['ModuleName'] = self.module_name

        if self.pass_ is not None:
            result['Pass'] = self.pass_

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')

        if m.get('Pass') is not None:
            self.pass_ = m.get('Pass')

        return self

