# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class CreateClusterNodePoolRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        kubernetes_config: main_models.CreateClusterNodePoolRequestKubernetesConfig = None,
        nodepool_info: main_models.CreateClusterNodePoolRequestNodepoolInfo = None,
        scaling_group: main_models.CreateClusterNodePoolRequestScalingGroup = None,
    ):
        # This parameter is required.
        self.cluster_id = cluster_id
        self.kubernetes_config = kubernetes_config
        # This parameter is required.
        self.nodepool_info = nodepool_info
        # This parameter is required.
        self.scaling_group = scaling_group

    def validate(self):
        if self.kubernetes_config:
            self.kubernetes_config.validate()
        if self.nodepool_info:
            self.nodepool_info.validate()
        if self.scaling_group:
            self.scaling_group.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.kubernetes_config is not None:
            result['KubernetesConfig'] = self.kubernetes_config.to_map()

        if self.nodepool_info is not None:
            result['NodepoolInfo'] = self.nodepool_info.to_map()

        if self.scaling_group is not None:
            result['ScalingGroup'] = self.scaling_group.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('KubernetesConfig') is not None:
            temp_model = main_models.CreateClusterNodePoolRequestKubernetesConfig()
            self.kubernetes_config = temp_model.from_map(m.get('KubernetesConfig'))

        if m.get('NodepoolInfo') is not None:
            temp_model = main_models.CreateClusterNodePoolRequestNodepoolInfo()
            self.nodepool_info = temp_model.from_map(m.get('NodepoolInfo'))

        if m.get('ScalingGroup') is not None:
            temp_model = main_models.CreateClusterNodePoolRequestScalingGroup()
            self.scaling_group = temp_model.from_map(m.get('ScalingGroup'))

        return self

class CreateClusterNodePoolRequestScalingGroup(DaraModel):
    def __init__(
        self,
        data_disks: List[main_models.CreateClusterNodePoolRequestScalingGroupDataDisks] = None,
        desired_size: int = None,
        image_id: str = None,
        instance_charge_type: str = None,
        instance_types: List[str] = None,
        key_pair_name: str = None,
        password: str = None,
        system_disk_category: str = None,
        system_disk_size: int = None,
        vswitch_ids: List[str] = None,
    ):
        self.data_disks = data_disks
        self.desired_size = desired_size
        # This parameter is required.
        self.image_id = image_id
        self.instance_charge_type = instance_charge_type
        # This parameter is required.
        self.instance_types = instance_types
        self.key_pair_name = key_pair_name
        self.password = password
        self.system_disk_category = system_disk_category
        self.system_disk_size = system_disk_size
        # This parameter is required.
        self.vswitch_ids = vswitch_ids

    def validate(self):
        if self.data_disks:
            for v1 in self.data_disks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataDisks'] = []
        if self.data_disks is not None:
            for k1 in self.data_disks:
                result['DataDisks'].append(k1.to_map() if k1 else None)

        if self.desired_size is not None:
            result['DesiredSize'] = self.desired_size

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.instance_types is not None:
            result['InstanceTypes'] = self.instance_types

        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name

        if self.password is not None:
            result['Password'] = self.password

        if self.system_disk_category is not None:
            result['SystemDiskCategory'] = self.system_disk_category

        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size

        if self.vswitch_ids is not None:
            result['VswitchIds'] = self.vswitch_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_disks = []
        if m.get('DataDisks') is not None:
            for k1 in m.get('DataDisks'):
                temp_model = main_models.CreateClusterNodePoolRequestScalingGroupDataDisks()
                self.data_disks.append(temp_model.from_map(k1))

        if m.get('DesiredSize') is not None:
            self.desired_size = m.get('DesiredSize')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('InstanceTypes') is not None:
            self.instance_types = m.get('InstanceTypes')

        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('SystemDiskCategory') is not None:
            self.system_disk_category = m.get('SystemDiskCategory')

        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')

        if m.get('VswitchIds') is not None:
            self.vswitch_ids = m.get('VswitchIds')

        return self

class CreateClusterNodePoolRequestScalingGroupDataDisks(DaraModel):
    def __init__(
        self,
        category: str = None,
        size: int = None,
    ):
        self.category = category
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.size is not None:
            result['Size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self

class CreateClusterNodePoolRequestNodepoolInfo(DaraModel):
    def __init__(
        self,
        name: str = None,
    ):
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class CreateClusterNodePoolRequestKubernetesConfig(DaraModel):
    def __init__(
        self,
        pre_user_data: str = None,
        user_data: str = None,
    ):
        self.pre_user_data = pre_user_data
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pre_user_data is not None:
            result['PreUserData'] = self.pre_user_data

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PreUserData') is not None:
            self.pre_user_data = m.get('PreUserData')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

