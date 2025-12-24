# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_eas20210701 import models as main_models
from darabonba.model import DaraModel

class CreateResourceRequest(DaraModel):
    def __init__(
        self,
        auto_renewal: bool = None,
        charge_type: str = None,
        ecs_instance_count: int = None,
        ecs_instance_type: str = None,
        labels: Dict[str, str] = None,
        resource_name: str = None,
        resource_type: str = None,
        self_managed_resource_options: main_models.CreateResourceRequestSelfManagedResourceOptions = None,
        system_disk_size: int = None,
        zone: str = None,
    ):
        # Specifies whether to enable auto-renewal. Valid values:
        # 
        # *   false (default)
        # *   true
        self.auto_renewal = auto_renewal
        # The billing method. Valid values:
        # 
        # *   PrePaid: the subscription billing method.
        # *   PostPaid: the pay-as-you-go billing method.
        # 
        # >  This parameter is required when the ResourceType parameter is set to Dedicated.
        self.charge_type = charge_type
        # The number of ECS instances.
        # 
        # >  This parameter is required when the ResourceType parameter is set to Dedicated.
        self.ecs_instance_count = ecs_instance_count
        # The type of the Elastic Compute Service (ECS) instance.
        # 
        # >  This parameter is required when the ResourceType parameter is set to Dedicated.
        self.ecs_instance_type = ecs_instance_type
        # The labels.
        self.labels = labels
        self.resource_name = resource_name
        # The type of the resource group. Valid values:
        # 
        # *   Dedicated: the dedicated resource group.
        # *   SelfManaged: the self-managed resource group.
        # 
        # >  If you use a self-managed resource group, you must configure a whitelist.
        self.resource_type = resource_type
        # The configurations of the self-managed resource group.
        self.self_managed_resource_options = self_managed_resource_options
        # The size of the system disk. Unit: GiB. Valid values: 200 to 2000. Default value: 200.
        self.system_disk_size = system_disk_size
        # The ID of the zone in which the instance resides.
        self.zone = zone

    def validate(self):
        if self.self_managed_resource_options:
            self.self_managed_resource_options.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_renewal is not None:
            result['AutoRenewal'] = self.auto_renewal

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.ecs_instance_count is not None:
            result['EcsInstanceCount'] = self.ecs_instance_count

        if self.ecs_instance_type is not None:
            result['EcsInstanceType'] = self.ecs_instance_type

        if self.labels is not None:
            result['Labels'] = self.labels

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.self_managed_resource_options is not None:
            result['SelfManagedResourceOptions'] = self.self_managed_resource_options.to_map()

        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size

        if self.zone is not None:
            result['Zone'] = self.zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenewal') is not None:
            self.auto_renewal = m.get('AutoRenewal')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('EcsInstanceCount') is not None:
            self.ecs_instance_count = m.get('EcsInstanceCount')

        if m.get('EcsInstanceType') is not None:
            self.ecs_instance_type = m.get('EcsInstanceType')

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('SelfManagedResourceOptions') is not None:
            temp_model = main_models.CreateResourceRequestSelfManagedResourceOptions()
            self.self_managed_resource_options = temp_model.from_map(m.get('SelfManagedResourceOptions'))

        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')

        if m.get('Zone') is not None:
            self.zone = m.get('Zone')

        return self

class CreateResourceRequestSelfManagedResourceOptions(DaraModel):
    def __init__(
        self,
        external_cluster_id: str = None,
        node_match_labels: Dict[str, str] = None,
        node_tolerations: List[main_models.CreateResourceRequestSelfManagedResourceOptionsNodeTolerations] = None,
        role_name: str = None,
    ):
        # The ID of the self-managed cluster.
        self.external_cluster_id = external_cluster_id
        # The tag key-value pairs of the node.
        self.node_match_labels = node_match_labels
        # The tolerations for the node taint.
        self.node_tolerations = node_tolerations
        # The name of the RAM user to which the permissions on Elastic Algorithm Service (EAS) of Platform for AI (PAI) are granted.
        self.role_name = role_name

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
        if self.external_cluster_id is not None:
            result['ExternalClusterId'] = self.external_cluster_id

        if self.node_match_labels is not None:
            result['NodeMatchLabels'] = self.node_match_labels

        result['NodeTolerations'] = []
        if self.node_tolerations is not None:
            for k1 in self.node_tolerations:
                result['NodeTolerations'].append(k1.to_map() if k1 else None)

        if self.role_name is not None:
            result['RoleName'] = self.role_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternalClusterId') is not None:
            self.external_cluster_id = m.get('ExternalClusterId')

        if m.get('NodeMatchLabels') is not None:
            self.node_match_labels = m.get('NodeMatchLabels')

        self.node_tolerations = []
        if m.get('NodeTolerations') is not None:
            for k1 in m.get('NodeTolerations'):
                temp_model = main_models.CreateResourceRequestSelfManagedResourceOptionsNodeTolerations()
                self.node_tolerations.append(temp_model.from_map(k1))

        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')

        return self

class CreateResourceRequestSelfManagedResourceOptionsNodeTolerations(DaraModel):
    def __init__(
        self,
        effect: str = None,
        key: str = None,
        operator: str = None,
        value: str = None,
    ):
        # The effect.
        # 
        # Valid values:
        # 
        # *   PreferNoSchedule
        # *   NoSchedule
        # *   NoExecute
        self.effect = effect
        # The key name.
        self.key = key
        # The relationship between key names and key values.
        # 
        # Valid values:
        # 
        # *   Equal
        # *   Exists
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

