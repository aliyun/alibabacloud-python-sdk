# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifySandboxTemplateShrinkRequest(DaraModel):
    def __init__(
        self,
        default_cpu: str = None,
        default_memory: str = None,
        image: str = None,
        instance_name: str = None,
        region_id: str = None,
        replicas: int = None,
        tags_shrink: str = None,
        template_id: str = None,
    ):
        # The number of CPUs for sandboxes created from this template. Valid values: 1 to 4.
        self.default_cpu = default_cpu
        # The memory size for sandboxes created from this template. Unit: Gi. Valid values: 1Gi to 8Gi.
        self.default_memory = default_memory
        self.image = image
        # The instance ID of the AI application.
        # 
        # This parameter is required.
        self.instance_name = instance_name
        # The region ID.
        self.region_id = region_id
        # The initial number of instances. Valid values: 1 to 1000.
        self.replicas = replicas
        self.tags_shrink = tags_shrink
        # The sandbox template ID.
        # 
        # This parameter is required.
        self.template_id = template_id

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

        if self.image is not None:
            result['Image'] = self.image

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.replicas is not None:
            result['Replicas'] = self.replicas

        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultCpu') is not None:
            self.default_cpu = m.get('DefaultCpu')

        if m.get('DefaultMemory') is not None:
            self.default_memory = m.get('DefaultMemory')

        if m.get('Image') is not None:
            self.image = m.get('Image')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Replicas') is not None:
            self.replicas = m.get('Replicas')

        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

