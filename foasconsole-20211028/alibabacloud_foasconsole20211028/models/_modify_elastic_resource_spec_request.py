# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_foasconsole20211028 import models as main_models
from darabonba.model import DaraModel

class ModifyElasticResourceSpecRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        region: str = None,
        resource_spec: main_models.ModifyElasticResourceSpecRequestResourceSpec = None,
    ):
        # The order instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID.
        # 
        # This parameter is required.
        self.region = region
        # The maximum pay-as-you-go resource specifications.
        # 
        # This parameter is required.
        self.resource_spec = resource_spec

    def validate(self):
        if self.resource_spec:
            self.resource_spec.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region is not None:
            result['Region'] = self.region

        if self.resource_spec is not None:
            result['ResourceSpec'] = self.resource_spec.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('ResourceSpec') is not None:
            temp_model = main_models.ModifyElasticResourceSpecRequestResourceSpec()
            self.resource_spec = temp_model.from_map(m.get('ResourceSpec'))

        return self

class ModifyElasticResourceSpecRequestResourceSpec(DaraModel):
    def __init__(
        self,
        cpu: int = None,
        memory_gb: int = None,
    ):
        # The number of CPUs.
        # 
        # This parameter is required.
        self.cpu = cpu
        # The memory size.
        # > The memory size must be 4 times the number of CPUs.
        # 
        # This parameter is required.
        self.memory_gb = memory_gb

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.memory_gb is not None:
            result['MemoryGB'] = self.memory_gb

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('MemoryGB') is not None:
            self.memory_gb = m.get('MemoryGB')

        return self

