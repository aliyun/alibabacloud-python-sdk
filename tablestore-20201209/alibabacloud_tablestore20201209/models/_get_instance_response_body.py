# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_tablestore20201209 import models as main_models
from darabonba.model import DaraModel

class GetInstanceResponseBody(DaraModel):
    def __init__(
        self,
        alias_name: str = None,
        create_time: str = None,
        elastic_vcuupper_limit: float = None,
        instance_description: str = None,
        instance_name: str = None,
        instance_specification: str = None,
        instance_status: str = None,
        is_multi_az: bool = None,
        network: str = None,
        network_source_acl: List[str] = None,
        network_type_acl: List[str] = None,
        payment_type: str = None,
        policy: str = None,
        policy_version: int = None,
        region_id: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        spinstance_id: str = None,
        storage_type: str = None,
        table_quota: int = None,
        tags: List[main_models.GetInstanceResponseBodyTags] = None,
        user_id: str = None,
        vcuquota: int = None,
    ):
        # The instance alias.
        self.alias_name = alias_name
        # The time when the instance was created.
        self.create_time = create_time
        # The upper limit for the VCUs of the instance.
        self.elastic_vcuupper_limit = elastic_vcuupper_limit
        # The description of the instance.
        self.instance_description = instance_description
        # The name of the instance.
        self.instance_name = instance_name
        # The type of the instance.
        # 
        # *   SSD: high-performance instance
        # *   HYBRID: capacity instance
        self.instance_specification = instance_specification
        # The status of the instance.
        # 
        # *   normal: The instance works as expected.
        # *   forbidden: The instance is disabled.
        # *   Deleting: The instance is being deleted.
        self.instance_status = instance_status
        # Indicates whether zone-redundant storage (ZRS) is enabled for the instance.
        # 
        # *   true: ZRS is enabled for the instance.
        # *   false: Locally redundant storage (LRS) is enabled for the instance.
        self.is_multi_az = is_multi_az
        # The network type of the instance. Valid values:
        # 
        # *   VPC: The instance can be accessed only over the bound virtual private clouds (VPCs).
        # *   VPC_CONSOLE: The instance can be accessed from the Tablestore console or over the bound VPCs.
        # *   NORMAL: The instance can be accessed from networks of the custom types.
        self.network = network
        # The sources of the network from which access is allowed. Valid value:
        # 
        # TRUST_PROXY: console
        self.network_source_acl = network_source_acl
        # The types of the network from which access is allowed. Valid values:
        # 
        # *   CLASSIC: the classic network
        # *   INTERNET: the Internet
        # *   VPC: VPCs
        self.network_type_acl = network_type_acl
        # The billing method. Valid values:
        # 
        # *   Subscription: subscription
        # *   PayAsYouGo: pay-as-you-go
        self.payment_type = payment_type
        # The instance policy.
        self.policy = policy
        # The version of the instance policy.
        self.policy_version = policy_version
        # The region ID of the instance.
        self.region_id = region_id
        # The request ID, which can be used to troubleshoot issues.
        self.request_id = request_id
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        # The ID of the instance.
        self.spinstance_id = spinstance_id
        # The storage type.
        # 
        # *   SSD: high-performance
        # *   HYBRID: capacity
        self.storage_type = storage_type
        # The total number of tables in the instance.
        self.table_quota = table_quota
        # The tags of the instance.
        self.tags = tags
        # The user ID.
        self.user_id = user_id
        # The VCU quota.
        self.vcuquota = vcuquota

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
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.elastic_vcuupper_limit is not None:
            result['ElasticVCUUpperLimit'] = self.elastic_vcuupper_limit

        if self.instance_description is not None:
            result['InstanceDescription'] = self.instance_description

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_specification is not None:
            result['InstanceSpecification'] = self.instance_specification

        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status

        if self.is_multi_az is not None:
            result['IsMultiAZ'] = self.is_multi_az

        if self.network is not None:
            result['Network'] = self.network

        if self.network_source_acl is not None:
            result['NetworkSourceACL'] = self.network_source_acl

        if self.network_type_acl is not None:
            result['NetworkTypeACL'] = self.network_type_acl

        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.policy_version is not None:
            result['PolicyVersion'] = self.policy_version

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.spinstance_id is not None:
            result['SPInstanceId'] = self.spinstance_id

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.table_quota is not None:
            result['TableQuota'] = self.table_quota

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.vcuquota is not None:
            result['VCUQuota'] = self.vcuquota

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ElasticVCUUpperLimit') is not None:
            self.elastic_vcuupper_limit = m.get('ElasticVCUUpperLimit')

        if m.get('InstanceDescription') is not None:
            self.instance_description = m.get('InstanceDescription')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceSpecification') is not None:
            self.instance_specification = m.get('InstanceSpecification')

        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')

        if m.get('IsMultiAZ') is not None:
            self.is_multi_az = m.get('IsMultiAZ')

        if m.get('Network') is not None:
            self.network = m.get('Network')

        if m.get('NetworkSourceACL') is not None:
            self.network_source_acl = m.get('NetworkSourceACL')

        if m.get('NetworkTypeACL') is not None:
            self.network_type_acl = m.get('NetworkTypeACL')

        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('PolicyVersion') is not None:
            self.policy_version = m.get('PolicyVersion')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SPInstanceId') is not None:
            self.spinstance_id = m.get('SPInstanceId')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('TableQuota') is not None:
            self.table_quota = m.get('TableQuota')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetInstanceResponseBodyTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('VCUQuota') is not None:
            self.vcuquota = m.get('VCUQuota')

        return self

class GetInstanceResponseBodyTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        tag_key: str = None,
        tag_value: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # (Deprecated) The tag key.
        self.tag_key = tag_key
        # (Deprecated) The tag value.
        self.tag_value = tag_value
        # The tag value.
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

        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

