# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alikafka20190916 import models as main_models
from darabonba.model import DaraModel

class CreatePostPayOrderRequest(DaraModel):
    def __init__(
        self,
        deploy_type: int = None,
        disk_size: int = None,
        disk_type: str = None,
        eip_max: int = None,
        io_max: int = None,
        io_max_spec: str = None,
        paid_type: int = None,
        partition_num: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        serverless_config: main_models.CreatePostPayOrderRequestServerlessConfig = None,
        spec_type: str = None,
        tag: List[main_models.CreatePostPayOrderRequestTag] = None,
        topic_quota: int = None,
    ):
        # The deployment type. Valid values:
        # 
        # - **4**: Internet- and VPC-connected instance
        # 
        # - **5**: VPC-connected instance
        # 
        # This parameter is required.
        self.deploy_type = deploy_type
        # The disk capacity.
        # 
        # For the value range, see [Billing overview](https://help.aliyun.com/document_detail/84737.html).
        # > If you create a serverless instance, you do not need to set this parameter.
        self.disk_size = disk_size
        # The disk type. Valid values:
        # 
        # - **0**: premium cloud disk
        # 
        # - **1**: SSD
        # > If you create a serverless instance, you do not need to set this parameter.
        self.disk_type = disk_type
        # The Internet traffic.
        # 
        # - If **DeployType** is set to **4**, this parameter is required.
        # 
        # - For the value range, see [Billing overview](https://help.aliyun.com/document_detail/84737.html).
        # 
        # > If you create a serverless instance, you do not need to set this parameter.
        self.eip_max = eip_max
        # The maximum traffic (not recommended).
        # 
        # - You must specify one of IoMax and IoMaxSpec. If both parameters are specified, the value of IoMaxSpec takes precedence. Specify only IoMaxSpec.
        # 
        # - For the value range, see [Billing overview](https://help.aliyun.com/document_detail/84737.html).
        # 
        # > If you create a serverless instance, you do not need to set this parameter.
        self.io_max = io_max
        # The traffic specification (recommended).
        # 
        # - You must specify one of IoMax and IoMaxSpec. If both parameters are specified, the value of IoMaxSpec takes precedence. Specify only IoMaxSpec.
        # 
        # - For the value range, see [Billing overview](https://help.aliyun.com/document_detail/84737.html).
        # 
        # > If you create a serverless instance, you do not need to set this parameter.
        self.io_max_spec = io_max_spec
        # The billing type. Valid values:
        # 
        # - 1 (default): reserved instance with pay-as-you-go billing.
        # - 3: serverless instance with reserved specification pay-as-you-go billing + serverless elastic scaling pay-as-you-go billing.
        self.paid_type = paid_type
        # The number of partitions (recommended).
        # 
        # * You must specify one of PartitionNum and TopicQuota. Specify only PartitionNum.
        # 
        # * If both PartitionNum and TopicQuota are specified, the system verifies whether the values are equivalent based on the legacy topic sales model. If the values are not equivalent, the request fails. If the values are equivalent, the purchase is made based on the number of partitions.
        # 
        # * For the value range, see [Billing overview](https://help.aliyun.com/document_detail/84737.html).
        # 
        # > If you create a serverless instance, you do not need to set this parameter.
        self.partition_num = partition_num
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID.
        # 
        # If this parameter is not specified, the instance is placed in the default resource group. You can view the resource group ID in the Resource Management console.
        self.resource_group_id = resource_group_id
        # The settings of the serverless instance. This parameter is required when you create a serverless instance.
        self.serverless_config = serverless_config
        # The specification type.
        # 
        # Valid values when PaidType is set to 1 (reserved instance with pay-as-you-go billing):
        # 
        # - normal: Standard Edition (shared throughput for writes)
        # - professional: Professional Edition (shared throughput for writes)
        # - professionalForHighRead: Professional Edition (shared throughput for reads)
        # 
        # Valid values when PaidType is set to 3 (serverless instance with reserved specification pay-as-you-go billing + serverless elastic scaling pay-as-you-go billing):
        # 
        # - basic: Serverless Basic Edition
        # - normal: Serverless Standard Edition
        # - professional: Serverless Professional Edition
        # 
        # For more information about these specification types, see [Billing overview](https://help.aliyun.com/document_detail/84737.html).
        self.spec_type = spec_type
        # The list of tags.
        self.tag = tag
        # The number of topics (not recommended).
        # 
        # - You must specify one of PartitionNum and TopicQuota. Specify only PartitionNum.
        # 
        # - If both PartitionNum and TopicQuota are specified, the system verifies whether the values are equivalent based on the legacy topic sales model. If the values are not equivalent, the request fails. If the values are equivalent, the purchase is made based on the number of partitions.
        # 
        # - The default value varies based on the traffic specification. If the value exceeds the default value, additional fees are charged.
        # 
        # - For the value range, see [Billing overview](https://help.aliyun.com/document_detail/84737.html).
        # 
        # > If you create a serverless instance, you do not need to set this parameter.
        self.topic_quota = topic_quota

    def validate(self):
        if self.serverless_config:
            self.serverless_config.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type

        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size

        if self.disk_type is not None:
            result['DiskType'] = self.disk_type

        if self.eip_max is not None:
            result['EipMax'] = self.eip_max

        if self.io_max is not None:
            result['IoMax'] = self.io_max

        if self.io_max_spec is not None:
            result['IoMaxSpec'] = self.io_max_spec

        if self.paid_type is not None:
            result['PaidType'] = self.paid_type

        if self.partition_num is not None:
            result['PartitionNum'] = self.partition_num

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.serverless_config is not None:
            result['ServerlessConfig'] = self.serverless_config.to_map()

        if self.spec_type is not None:
            result['SpecType'] = self.spec_type

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.topic_quota is not None:
            result['TopicQuota'] = self.topic_quota

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')

        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')

        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')

        if m.get('EipMax') is not None:
            self.eip_max = m.get('EipMax')

        if m.get('IoMax') is not None:
            self.io_max = m.get('IoMax')

        if m.get('IoMaxSpec') is not None:
            self.io_max_spec = m.get('IoMaxSpec')

        if m.get('PaidType') is not None:
            self.paid_type = m.get('PaidType')

        if m.get('PartitionNum') is not None:
            self.partition_num = m.get('PartitionNum')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ServerlessConfig') is not None:
            temp_model = main_models.CreatePostPayOrderRequestServerlessConfig()
            self.serverless_config = temp_model.from_map(m.get('ServerlessConfig'))

        if m.get('SpecType') is not None:
            self.spec_type = m.get('SpecType')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreatePostPayOrderRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TopicQuota') is not None:
            self.topic_quota = m.get('TopicQuota')

        return self

class CreatePostPayOrderRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the resource.
        # - N ranges from 1 to 20.
        # - If this parameter is left empty, all tag keys are matched.
        # - The tag key can be up to 128 characters in length and cannot start with aliyun or acs:. It cannot contain http:// or https://.
        # 
        # This parameter is required.
        self.key = key
        # The tag value of the resource.
        # - N ranges from 1 to 20.
        # - If the tag key is left empty, this parameter must also be left empty. If this parameter is left empty, all tag values are matched.
        # - The tag value can be up to 128 characters in length and cannot start with aliyun or acs:. It cannot contain http:// or https://.
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

class CreatePostPayOrderRequestServerlessConfig(DaraModel):
    def __init__(
        self,
        reserved_publish_capacity: int = None,
        reserved_subscribe_capacity: int = None,
    ):
        # The reserved publish traffic specification value. Only integers are supported. The minimum value is 60. This parameter is required for serverless instances.
        # 
        # 
        # > The actual upper limit depends on the inventory in the current region. Refer to the purchase page for the available range.
        self.reserved_publish_capacity = reserved_publish_capacity
        # The reserved subscribe traffic specification value. Only integers are supported. The minimum value is 20. This parameter is required for serverless instances.
        # 
        # > The actual upper limit depends on the inventory in the current region. Refer to the purchase page for the available range.
        self.reserved_subscribe_capacity = reserved_subscribe_capacity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.reserved_publish_capacity is not None:
            result['ReservedPublishCapacity'] = self.reserved_publish_capacity

        if self.reserved_subscribe_capacity is not None:
            result['ReservedSubscribeCapacity'] = self.reserved_subscribe_capacity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReservedPublishCapacity') is not None:
            self.reserved_publish_capacity = m.get('ReservedPublishCapacity')

        if m.get('ReservedSubscribeCapacity') is not None:
            self.reserved_subscribe_capacity = m.get('ReservedSubscribeCapacity')

        return self

