# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class CheckInstanceModuleStatusResponseBody(DaraModel):
    def __init__(
        self,
        module: main_models.CheckInstanceModuleStatusResponseBodyModule = None,
        request_id: str = None,
    ):
        self.module = module
        self.request_id = request_id

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.module is not None:
            result['Module'] = self.module.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Module') is not None:
            temp_model = main_models.CheckInstanceModuleStatusResponseBodyModule()
            self.module = temp_model.from_map(m.get('Module'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CheckInstanceModuleStatusResponseBodyModule(DaraModel):
    def __init__(
        self,
        module_status: str = None,
    ):
        # 模块状态
        self.module_status = module_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.module_status is not None:
            result['ModuleStatus'] = self.module_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModuleStatus') is not None:
            self.module_status = m.get('ModuleStatus')

        return self

