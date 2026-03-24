# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetSupportedModulesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        supported_module_response: List[main_models.GetSupportedModulesResponseBodySupportedModuleResponse] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The supported modules. The module information is classified by cloud service provider.
        self.supported_module_response = supported_module_response

    def validate(self):
        if self.supported_module_response:
            for v1 in self.supported_module_response:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SupportedModuleResponse'] = []
        if self.supported_module_response is not None:
            for k1 in self.supported_module_response:
                result['SupportedModuleResponse'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.supported_module_response = []
        if m.get('SupportedModuleResponse') is not None:
            for k1 in m.get('SupportedModuleResponse'):
                temp_model = main_models.GetSupportedModulesResponseBodySupportedModuleResponse()
                self.supported_module_response.append(temp_model.from_map(k1))

        return self

class GetSupportedModulesResponseBodySupportedModuleResponse(DaraModel):
    def __init__(
        self,
        supported_modules: List[main_models.GetSupportedModulesResponseBodySupportedModuleResponseSupportedModules] = None,
        vendor: str = None,
    ):
        # The modules supported by the cloud service provider.
        self.supported_modules = supported_modules
        # The cloud service provider. Valid values:
        # 
        # *   **Tencent**: Tencent Cloud
        # *   **HUAWEICLOUD**:Huawei Cloud
        # *   **Azure**: Microsoft Azure
        # *   **AWS**: Amazon Web Services (AWS)
        self.vendor = vendor

    def validate(self):
        if self.supported_modules:
            for v1 in self.supported_modules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SupportedModules'] = []
        if self.supported_modules is not None:
            for k1 in self.supported_modules:
                result['SupportedModules'].append(k1.to_map() if k1 else None)

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.supported_modules = []
        if m.get('SupportedModules') is not None:
            for k1 in m.get('SupportedModules'):
                temp_model = main_models.GetSupportedModulesResponseBodySupportedModuleResponseSupportedModules()
                self.supported_modules.append(temp_model.from_map(k1))

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        return self

class GetSupportedModulesResponseBodySupportedModuleResponseSupportedModules(DaraModel):
    def __init__(
        self,
        module: str = None,
        module_auth: bool = None,
        module_disp: str = None,
    ):
        # The code of the module. Valid values:
        # 
        # *   **HOST**: host
        # *   **CSPM**: configuration assessment
        # *   **SIEM**: CloudSiem
        # *   **TRIAL**: log audit
        self.module = module
        # Module authorization switch indicator. Values: 
        # - **true**: Enabled
        #  - **false**: Not enabled
        self.module_auth = module_auth
        # The display name of the module.
        self.module_disp = module_disp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.module is not None:
            result['Module'] = self.module

        if self.module_auth is not None:
            result['ModuleAuth'] = self.module_auth

        if self.module_disp is not None:
            result['ModuleDisp'] = self.module_disp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Module') is not None:
            self.module = m.get('Module')

        if m.get('ModuleAuth') is not None:
            self.module_auth = m.get('ModuleAuth')

        if m.get('ModuleDisp') is not None:
            self.module_disp = m.get('ModuleDisp')

        return self

