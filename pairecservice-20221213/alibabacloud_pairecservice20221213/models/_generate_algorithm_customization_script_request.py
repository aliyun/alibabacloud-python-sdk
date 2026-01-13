# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class GenerateAlgorithmCustomizationScriptRequest(DaraModel):
    def __init__(
        self,
        deploy_mode: str = None,
        instance_id: str = None,
        module_field_types: Dict[str, Any] = None,
    ):
        self.deploy_mode = deploy_mode
        self.instance_id = instance_id
        self.module_field_types = module_field_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deploy_mode is not None:
            result['DeployMode'] = self.deploy_mode

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.module_field_types is not None:
            result['ModuleFieldTypes'] = self.module_field_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeployMode') is not None:
            self.deploy_mode = m.get('DeployMode')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ModuleFieldTypes') is not None:
            self.module_field_types = m.get('ModuleFieldTypes')

        return self

