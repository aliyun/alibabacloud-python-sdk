# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_tablestore20201209 import models as main_models
from darabonba.model import DaraModel

class CreateInstanceRequest(DaraModel):
    def __init__(
        self,
        cluster_type: str = None,
        disable_replication: bool = None,
        instance_description: str = None,
        instance_name: str = None,
        network: str = None,
        network_source_acl: List[str] = None,
        network_type_acl: List[str] = None,
        policy: str = None,
        resource_group_id: str = None,
        tags: List[main_models.CreateInstanceRequestTags] = None,
    ):
        # The type of the instance.
        # 
        # This parameter is required.
        self.cluster_type = cluster_type
        # (Deprecated) Specifies whether to enable disaster recovery for the instance.
        # 
        # Valid values:
        # 
        # *   false
        # *   true
        self.disable_replication = disable_replication
        # The description of the instance. The instance description must be 3 to 256 characters in length.
        self.instance_description = instance_description
        # The name of the instance. Instance naming conventions:
        # 
        # *   The name can contain only letters, digits, and hyphens (-).
        # *   The name must start with a letter.
        # *   The name cannot end with a hyphen (-).
        # *   The name is case-insensitive.
        # *   The name must be 3 to 16 characters in length.
        # *   The name cannot contain the following words: ali, ay, ots, taobao, and admin.
        # 
        # This parameter is required.
        self.instance_name = instance_name
        # (Deprecated) The network type of the instance. Valid values: NORMAL and VPC_CONSOLE. Default value: NORMAL.
        self.network = network
        # The types of the source from which access is allowed. By default, the following source type is allowed:
        # 
        # TRUST_PROXY: console
        self.network_source_acl = network_source_acl
        # The types of the network from which access is allowed. By default, the following network types are allowed:
        # 
        # *   INTERNET: Internet
        # *   VPC: virtual private cloud (VPC)
        # *   CLASSIC: classic network
        self.network_type_acl = network_type_acl
        # The instance policy in the JSON format.
        self.policy = policy
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        # The tags.
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        if self.disable_replication is not None:
            result['DisableReplication'] = self.disable_replication

        if self.instance_description is not None:
            result['InstanceDescription'] = self.instance_description

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.network is not None:
            result['Network'] = self.network

        if self.network_source_acl is not None:
            result['NetworkSourceACL'] = self.network_source_acl

        if self.network_type_acl is not None:
            result['NetworkTypeACL'] = self.network_type_acl

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        if m.get('DisableReplication') is not None:
            self.disable_replication = m.get('DisableReplication')

        if m.get('InstanceDescription') is not None:
            self.instance_description = m.get('InstanceDescription')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('Network') is not None:
            self.network = m.get('Network')

        if m.get('NetworkSourceACL') is not None:
            self.network_source_acl = m.get('NetworkSourceACL')

        if m.get('NetworkTypeACL') is not None:
            self.network_type_acl = m.get('NetworkTypeACL')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.CreateInstanceRequestTags()
                self.tags.append(temp_model.from_map(k1))

        return self



class CreateInstanceRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. The tag key can be up to 64 characters in length.
        # 
        # This parameter is required.
        self.key = key
        # The tag value. The tag value can be up to 64 characters in length.
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

