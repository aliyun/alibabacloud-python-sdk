# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetInstanceModuleInfoRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        module_key: str = None,
    ):
        # IDaaS EIAM实例的ID。
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # 一级模块标识，必填
        # 
        # This parameter is required.
        self.module_key = module_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.module_key is not None:
            result['ModuleKey'] = self.module_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ModuleKey') is not None:
            self.module_key = m.get('ModuleKey')

        return self

