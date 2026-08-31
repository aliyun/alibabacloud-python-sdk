# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class CreateComputeClusterRequest(DaraModel):
    def __init__(
        self,
        cluster_config: main_models.CreateComputeClusterRequestClusterConfig = None,
        op_tenant_id: int = None,
        op_user_id: str = None,
    ):
        # The cluster configuration.
        # 
        # This parameter is required.
        self.cluster_config = cluster_config
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # The ID of the operator user.
        self.op_user_id = op_user_id

    def validate(self):
        if self.cluster_config:
            self.cluster_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_config is not None:
            result['ClusterConfig'] = self.cluster_config.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.op_user_id is not None:
            result['OpUserId'] = self.op_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterConfig') is not None:
            temp_model = main_models.CreateComputeClusterRequestClusterConfig()
            self.cluster_config = temp_model.from_map(m.get('ClusterConfig'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

        return self

class CreateComputeClusterRequestClusterConfig(DaraModel):
    def __init__(
        self,
        cluster_admins: List[str] = None,
        cluster_safety_control: main_models.CreateComputeClusterRequestClusterConfigClusterSafetyControl = None,
        config_list: List[main_models.CreateComputeClusterRequestClusterConfigConfigList] = None,
        des: str = None,
        name: str = None,
        type: str = None,
        type_version: str = None,
    ):
        # The list of cluster administrator IDs.
        self.cluster_admins = cluster_admins
        # The cluster security control configuration.
        self.cluster_safety_control = cluster_safety_control
        # The connection configuration items.
        # 
        # This parameter is required.
        self.config_list = config_list
        # The cluster description.
        self.des = des
        # The cluster name.
        # 
        # This parameter is required.
        self.name = name
        # The cluster type.
        # 
        # This parameter is required.
        self.type = type
        # The cluster version.
        self.type_version = type_version

    def validate(self):
        if self.cluster_safety_control:
            self.cluster_safety_control.validate()
        if self.config_list:
            for v1 in self.config_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_admins is not None:
            result['ClusterAdmins'] = self.cluster_admins

        if self.cluster_safety_control is not None:
            result['ClusterSafetyControl'] = self.cluster_safety_control.to_map()

        result['ConfigList'] = []
        if self.config_list is not None:
            for k1 in self.config_list:
                result['ConfigList'].append(k1.to_map() if k1 else None)

        if self.des is not None:
            result['Des'] = self.des

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        if self.type_version is not None:
            result['TypeVersion'] = self.type_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterAdmins') is not None:
            self.cluster_admins = m.get('ClusterAdmins')

        if m.get('ClusterSafetyControl') is not None:
            temp_model = main_models.CreateComputeClusterRequestClusterConfigClusterSafetyControl()
            self.cluster_safety_control = temp_model.from_map(m.get('ClusterSafetyControl'))

        self.config_list = []
        if m.get('ConfigList') is not None:
            for k1 in m.get('ConfigList'):
                temp_model = main_models.CreateComputeClusterRequestClusterConfigConfigList()
                self.config_list.append(temp_model.from_map(k1))

        if m.get('Des') is not None:
            self.des = m.get('Des')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('TypeVersion') is not None:
            self.type_version = m.get('TypeVersion')

        return self

class CreateComputeClusterRequestClusterConfigConfigList(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The configuration item.
        # 
        # This parameter is required.
        self.key = key
        # The value of the configuration item.
        # 
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateComputeClusterRequestClusterConfigClusterSafetyControl(DaraModel):
    def __init__(
        self,
        cluster_safety_auth_type: str = None,
        user_group_ids: List[str] = None,
        user_ids: List[str] = None,
    ):
        # The control mode.
        self.cluster_safety_auth_type = cluster_safety_auth_type
        # The list of whitelist user group IDs.
        self.user_group_ids = user_group_ids
        # The list of whitelist user IDs.
        self.user_ids = user_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_safety_auth_type is not None:
            result['ClusterSafetyAuthType'] = self.cluster_safety_auth_type

        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids

        if self.user_ids is not None:
            result['UserIds'] = self.user_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterSafetyAuthType') is not None:
            self.cluster_safety_auth_type = m.get('ClusterSafetyAuthType')

        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')

        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')

        return self

