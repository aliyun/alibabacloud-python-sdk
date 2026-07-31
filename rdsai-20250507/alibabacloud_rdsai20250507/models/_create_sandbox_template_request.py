# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSandboxTemplateRequest(DaraModel):
    def __init__(
        self,
        default_cpu: str = None,
        default_memory: str = None,
        description: str = None,
        instance_name: str = None,
        region_id: str = None,
        replicas: int = None,
        template_name: str = None,
    ):
        # The number of CPUs for sandboxes created by using this template. Valid values: 1 to 4.
        self.default_cpu = default_cpu
        # The memory size for sandboxes created by using this template. Unit: Gi. Valid values: 1Gi to 8Gi.
        self.default_memory = default_memory
        # The description of the sandbox template. The description must be unique within the VPC.
        self.description = description
        # The instance ID of the AI application.
        # 
        # This parameter is required.
        self.instance_name = instance_name
        # The region ID.
        self.region_id = region_id
        # The number of prewarmed sandboxes. Valid values: 1 to 1000.
        self.replicas = replicas
        # The name of the sandbox template.
        # 
        # This parameter is required.
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_cpu is not None:
            result['DefaultCpu'] = self.default_cpu

        if self.default_memory is not None:
            result['DefaultMemory'] = self.default_memory

        if self.description is not None:
            result['Description'] = self.description

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.replicas is not None:
            result['Replicas'] = self.replicas

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultCpu') is not None:
            self.default_cpu = m.get('DefaultCpu')

        if m.get('DefaultMemory') is not None:
            self.default_memory = m.get('DefaultMemory')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Replicas') is not None:
            self.replicas = m.get('Replicas')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        return self

