# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sysom20231230 import models as main_models
from darabonba.model import DaraModel

class AuthDiagnosisRequest(DaraModel):
    def __init__(
        self,
        x_debug_id: str = None,
        auto_create_role: bool = None,
        auto_install_agent: bool = None,
        instances: List[main_models.AuthDiagnosisRequestInstances] = None,
        x_sysom_invoke_source: str = None,
    ):
        self.x_debug_id = x_debug_id
        # Specifies whether to enable automatic creation of the service-linked role.
        self.auto_create_role = auto_create_role
        # Specifies whether to automatically install the latest version of the agent if it is not installed.
        self.auto_install_agent = auto_install_agent
        # The list of instances authorized for diagnosis.
        self.instances = instances
        self.x_sysom_invoke_source = x_sysom_invoke_source

    def validate(self):
        if self.instances:
            for v1 in self.instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.x_debug_id is not None:
            result['X-Debug-Id'] = self.x_debug_id

        if self.auto_create_role is not None:
            result['autoCreateRole'] = self.auto_create_role

        if self.auto_install_agent is not None:
            result['autoInstallAgent'] = self.auto_install_agent

        result['instances'] = []
        if self.instances is not None:
            for k1 in self.instances:
                result['instances'].append(k1.to_map() if k1 else None)

        if self.x_sysom_invoke_source is not None:
            result['x-sysom-invoke-source'] = self.x_sysom_invoke_source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Debug-Id') is not None:
            self.x_debug_id = m.get('X-Debug-Id')

        if m.get('autoCreateRole') is not None:
            self.auto_create_role = m.get('autoCreateRole')

        if m.get('autoInstallAgent') is not None:
            self.auto_install_agent = m.get('autoInstallAgent')

        self.instances = []
        if m.get('instances') is not None:
            for k1 in m.get('instances'):
                temp_model = main_models.AuthDiagnosisRequestInstances()
                self.instances.append(temp_model.from_map(k1))

        if m.get('x-sysom-invoke-source') is not None:
            self.x_sysom_invoke_source = m.get('x-sysom-invoke-source')

        return self



class AuthDiagnosisRequestInstances(DaraModel):
    def __init__(
        self,
        instance: str = None,
        region: str = None,
    ):
        # The instance ID.
        self.instance = instance
        # The region ID.
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance is not None:
            result['instance'] = self.instance

        if self.region is not None:
            result['region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instance') is not None:
            self.instance = m.get('instance')

        if m.get('region') is not None:
            self.region = m.get('region')

        return self

