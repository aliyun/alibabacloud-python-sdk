# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_milvus20231012 import models as main_models
from darabonba.model import DaraModel

class DBVersionDetail(DaraModel):
    def __init__(
        self,
        specs: List[main_models.DBVersionDetailSpecs] = None,
        status: str = None,
        version: str = None,
    ):
        self.specs = specs
        self.status = status
        self.version = version

    def validate(self):
        if self.specs:
            for v1 in self.specs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['specs'] = []
        if self.specs is not None:
            for k1 in self.specs:
                result['specs'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['status'] = self.status

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.specs = []
        if m.get('specs') is not None:
            for k1 in m.get('specs'):
                temp_model = main_models.DBVersionDetailSpecs()
                self.specs.append(temp_model.from_map(k1))

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class DBVersionDetailSpecs(DaraModel):
    def __init__(
        self,
        component_specs: List[main_models.DBVersionDetailSpecsComponentSpecs] = None,
        is_ha: bool = None,
        is_standalone: bool = None,
        zone_mode: str = None,
    ):
        self.component_specs = component_specs
        self.is_ha = is_ha
        self.is_standalone = is_standalone
        self.zone_mode = zone_mode

    def validate(self):
        if self.component_specs:
            for v1 in self.component_specs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['componentSpecs'] = []
        if self.component_specs is not None:
            for k1 in self.component_specs:
                result['componentSpecs'].append(k1.to_map() if k1 else None)

        if self.is_ha is not None:
            result['isHA'] = self.is_ha

        if self.is_standalone is not None:
            result['isStandalone'] = self.is_standalone

        if self.zone_mode is not None:
            result['zoneMode'] = self.zone_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.component_specs = []
        if m.get('componentSpecs') is not None:
            for k1 in m.get('componentSpecs'):
                temp_model = main_models.DBVersionDetailSpecsComponentSpecs()
                self.component_specs.append(temp_model.from_map(k1))

        if m.get('isHA') is not None:
            self.is_ha = m.get('isHA')

        if m.get('isStandalone') is not None:
            self.is_standalone = m.get('isStandalone')

        if m.get('zoneMode') is not None:
            self.zone_mode = m.get('zoneMode')

        return self



class DBVersionDetailSpecsComponentSpecs(DaraModel):
    def __init__(
        self,
        default_replicas: int = None,
        max_replicas: int = None,
        min_replicas: int = None,
        name: str = None,
        specs: List[str] = None,
        step: int = None,
        type: str = None,
    ):
        self.default_replicas = default_replicas
        self.max_replicas = max_replicas
        self.min_replicas = min_replicas
        self.name = name
        self.specs = specs
        self.step = step
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_replicas is not None:
            result['defaultReplicas'] = self.default_replicas

        if self.max_replicas is not None:
            result['maxReplicas'] = self.max_replicas

        if self.min_replicas is not None:
            result['minReplicas'] = self.min_replicas

        if self.name is not None:
            result['name'] = self.name

        if self.specs is not None:
            result['specs'] = self.specs

        if self.step is not None:
            result['step'] = self.step

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('defaultReplicas') is not None:
            self.default_replicas = m.get('defaultReplicas')

        if m.get('maxReplicas') is not None:
            self.max_replicas = m.get('maxReplicas')

        if m.get('minReplicas') is not None:
            self.min_replicas = m.get('minReplicas')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('specs') is not None:
            self.specs = m.get('specs')

        if m.get('step') is not None:
            self.step = m.get('step')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

