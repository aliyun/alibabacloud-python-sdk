# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_foasconsole20211028 import models as main_models
from darabonba.model import DaraModel

class ModifyNamespaceSpecV2Request(DaraModel):
    def __init__(
        self,
        elastic_resource_spec: main_models.ModifyNamespaceSpecV2RequestElasticResourceSpec = None,
        guaranteed_resource_spec: main_models.ModifyNamespaceSpecV2RequestGuaranteedResourceSpec = None,
        ha: bool = None,
        instance_id: str = None,
        namespace: str = None,
        region: str = None,
    ):
        self.elastic_resource_spec = elastic_resource_spec
        self.guaranteed_resource_spec = guaranteed_resource_spec
        # This parameter is required.
        self.ha = ha
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.namespace = namespace
        # This parameter is required.
        self.region = region

    def validate(self):
        if self.elastic_resource_spec:
            self.elastic_resource_spec.validate()
        if self.guaranteed_resource_spec:
            self.guaranteed_resource_spec.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.elastic_resource_spec is not None:
            result['ElasticResourceSpec'] = self.elastic_resource_spec.to_map()

        if self.guaranteed_resource_spec is not None:
            result['GuaranteedResourceSpec'] = self.guaranteed_resource_spec.to_map()

        if self.ha is not None:
            result['Ha'] = self.ha

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.region is not None:
            result['Region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ElasticResourceSpec') is not None:
            temp_model = main_models.ModifyNamespaceSpecV2RequestElasticResourceSpec()
            self.elastic_resource_spec = temp_model.from_map(m.get('ElasticResourceSpec'))

        if m.get('GuaranteedResourceSpec') is not None:
            temp_model = main_models.ModifyNamespaceSpecV2RequestGuaranteedResourceSpec()
            self.guaranteed_resource_spec = temp_model.from_map(m.get('GuaranteedResourceSpec'))

        if m.get('Ha') is not None:
            self.ha = m.get('Ha')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        return self

class ModifyNamespaceSpecV2RequestGuaranteedResourceSpec(DaraModel):
    def __init__(
        self,
        cpu: int = None,
        memory_gb: int = None,
    ):
        # This parameter is required.
        self.cpu = cpu
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

class ModifyNamespaceSpecV2RequestElasticResourceSpec(DaraModel):
    def __init__(
        self,
        cpu: int = None,
        memory_gb: int = None,
    ):
        # This parameter is required.
        self.cpu = cpu
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

