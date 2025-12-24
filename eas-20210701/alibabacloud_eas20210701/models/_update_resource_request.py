# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_eas20210701 import models as main_models
from darabonba.model import DaraModel

class UpdateResourceRequest(DaraModel):
    def __init__(
        self,
        resource_name: str = None,
        self_managed_resource_options: main_models.UpdateResourceRequestSelfManagedResourceOptions = None,
    ):
        # The new name of the resource group after the update. The name can be up to 27 characters in length.
        self.resource_name = resource_name
        # The configuration items of the self-managed resource group.
        self.self_managed_resource_options = self_managed_resource_options

    def validate(self):
        if self.self_managed_resource_options:
            self.self_managed_resource_options.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        if self.self_managed_resource_options is not None:
            result['SelfManagedResourceOptions'] = self.self_managed_resource_options.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        if m.get('SelfManagedResourceOptions') is not None:
            temp_model = main_models.UpdateResourceRequestSelfManagedResourceOptions()
            self.self_managed_resource_options = temp_model.from_map(m.get('SelfManagedResourceOptions'))

        return self

class UpdateResourceRequestSelfManagedResourceOptions(DaraModel):
    def __init__(
        self,
        node_match_labels: Dict[str, str] = None,
        node_tolerations: List[main_models.UpdateResourceRequestSelfManagedResourceOptionsNodeTolerations] = None,
    ):
        # Tag tag key-value pairs for nodes.
        self.node_match_labels = node_match_labels
        # Tolerations for nodes.
        self.node_tolerations = node_tolerations

    def validate(self):
        if self.node_tolerations:
            for v1 in self.node_tolerations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_match_labels is not None:
            result['NodeMatchLabels'] = self.node_match_labels

        result['NodeTolerations'] = []
        if self.node_tolerations is not None:
            for k1 in self.node_tolerations:
                result['NodeTolerations'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeMatchLabels') is not None:
            self.node_match_labels = m.get('NodeMatchLabels')

        self.node_tolerations = []
        if m.get('NodeTolerations') is not None:
            for k1 in m.get('NodeTolerations'):
                temp_model = main_models.UpdateResourceRequestSelfManagedResourceOptionsNodeTolerations()
                self.node_tolerations.append(temp_model.from_map(k1))

        return self

class UpdateResourceRequestSelfManagedResourceOptionsNodeTolerations(DaraModel):
    def __init__(
        self,
        effect: str = None,
        key: str = None,
        operator: str = None,
        value: str = None,
    ):
        # The effect.
        # Valid values:
        # - PreferNoSchedule
        # - NoSchedule
        # - NoExecute
        self.effect = effect
        # The key name.
        self.key = key
        # Relationship between key names and key values.
        # Valid values:
        # - Equal
        # - Exists
        self.operator = operator
        # The key value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.effect is not None:
            result['effect'] = self.effect

        if self.key is not None:
            result['key'] = self.key

        if self.operator is not None:
            result['operator'] = self.operator

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('effect') is not None:
            self.effect = m.get('effect')

        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('operator') is not None:
            self.operator = m.get('operator')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

