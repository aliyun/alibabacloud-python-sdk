# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class ComponentInstanceSelector(DaraModel):
    def __init__(
        self,
        action_scope: str = None,
        application_name: str = None,
        component_instances: List[main_models.ComponentInstanceSelectorComponentInstances] = None,
        components: List[main_models.ComponentInstanceSelectorComponents] = None,
        run_action_scope: str = None,
    ):
        # The action scope. Valid values:
        # 
        # - APPLICATION: The application level.
        # 
        # - COMPONENT: The component level.
        # 
        # - COMPONENT_INSTANCE: The component instance level.
        self.action_scope = action_scope
        # The application name.
        self.application_name = application_name
        # A list of component instances. This parameter is used when `RunActionScope` is set to `COMPONENT_INSTANCE`.
        self.component_instances = component_instances
        # A list of components. This parameter is used when `RunActionScope` is set to `COMPONENT`.
        self.components = components
        # The action scope. Valid values:
        # 
        # - APPLICATION: The application level.
        # 
        # - COMPONENT: The component level.
        # 
        # - COMPONENT_INSTANCE: The component instance level.
        # 
        # This parameter is required.
        self.run_action_scope = run_action_scope

    def validate(self):
        if self.component_instances:
            for v1 in self.component_instances:
                 if v1:
                    v1.validate()
        if self.components:
            for v1 in self.components:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_scope is not None:
            result['ActionScope'] = self.action_scope

        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        result['ComponentInstances'] = []
        if self.component_instances is not None:
            for k1 in self.component_instances:
                result['ComponentInstances'].append(k1.to_map() if k1 else None)

        result['Components'] = []
        if self.components is not None:
            for k1 in self.components:
                result['Components'].append(k1.to_map() if k1 else None)

        if self.run_action_scope is not None:
            result['RunActionScope'] = self.run_action_scope

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionScope') is not None:
            self.action_scope = m.get('ActionScope')

        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        self.component_instances = []
        if m.get('ComponentInstances') is not None:
            for k1 in m.get('ComponentInstances'):
                temp_model = main_models.ComponentInstanceSelectorComponentInstances()
                self.component_instances.append(temp_model.from_map(k1))

        self.components = []
        if m.get('Components') is not None:
            for k1 in m.get('Components'):
                temp_model = main_models.ComponentInstanceSelectorComponents()
                self.components.append(temp_model.from_map(k1))

        if m.get('RunActionScope') is not None:
            self.run_action_scope = m.get('RunActionScope')

        return self

class ComponentInstanceSelectorComponents(DaraModel):
    def __init__(
        self,
        application_name: str = None,
        component_name: str = None,
    ):
        # The application name.
        self.application_name = application_name
        # The component name.
        self.component_name = component_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        if self.component_name is not None:
            result['ComponentName'] = self.component_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')

        return self

class ComponentInstanceSelectorComponentInstances(DaraModel):
    def __init__(
        self,
        application_name: str = None,
        component_name: str = None,
        node_id: str = None,
    ):
        # The application name.
        self.application_name = application_name
        # The component name.
        self.component_name = component_name
        # The node ID.
        self.node_id = node_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        if self.component_name is not None:
            result['ComponentName'] = self.component_name

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        return self

