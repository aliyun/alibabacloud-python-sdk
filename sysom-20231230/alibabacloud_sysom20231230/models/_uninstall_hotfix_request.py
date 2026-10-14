# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sysom20231230 import models as main_models
from darabonba.model import DaraModel

class UninstallHotfixRequest(DaraModel):
    def __init__(
        self,
        cve_id: str = None,
        instances: List[main_models.UninstallHotfixRequestInstances] = None,
    ):
        # CVE ID
        # 
        # This parameter is required.
        self.cve_id = cve_id
        # The target instances.
        # 
        # This parameter is required.
        self.instances = instances

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
        if self.cve_id is not None:
            result['cveId'] = self.cve_id

        result['instances'] = []
        if self.instances is not None:
            for k1 in self.instances:
                result['instances'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cveId') is not None:
            self.cve_id = m.get('cveId')

        self.instances = []
        if m.get('instances') is not None:
            for k1 in m.get('instances'):
                temp_model = main_models.UninstallHotfixRequestInstances()
                self.instances.append(temp_model.from_map(k1))

        return self

class UninstallHotfixRequestInstances(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.region_id is not None:
            result['regionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        return self

