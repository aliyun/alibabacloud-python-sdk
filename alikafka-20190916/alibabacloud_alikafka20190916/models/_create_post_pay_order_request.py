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
        # - **4**: An instance that is accessible from the Internet and a VPC.
        # 
        # - **5**: An instance that is accessible only from a VPC.
        # 
        # This parameter is required.
        self.deploy_type = deploy_type
        # The disk capacity.
        # 
        # For the valid values, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # > Do not specify this parameter if you create a Serverless instance.
        self.disk_size = disk_size
        # The disk type. Valid values:
        # 
        # - **0**: Ultra disk
        # 
        # - **1**: SSD
        # 
        # > Do not specify this parameter if you create a Serverless instance.
        self.disk_type = disk_type
        # The Internet traffic.
        # 
        # - This parameter is required if you set **DeployType** to **4**.
        # 
        # - For the valid values, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # > Do not specify this parameter if you create a Serverless instance.
        self.eip_max = eip_max
        # The peak traffic. This parameter is not recommended.
        # 
        # - You must specify this parameter or \\`IoMaxSpec\\`. If you specify both parameters, the value of \\`IoMaxSpec\\` takes precedence. We recommend that you specify only \\`IoMaxSpec\\`.
        # 
        # - For the valid values, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # > Do not specify this parameter if you create a Serverless instance.
        self.io_max = io_max
        # The traffic specification. This parameter is recommended.
        # 
        # - You must specify this parameter or \\`IoMax\\`. If you specify both parameters, the value of this parameter takes precedence. We recommend that you specify only this parameter.
        # 
        # - For the valid values, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # > Do not specify this parameter if you create a Serverless instance.
        self.io_max_spec = io_max_spec
        # The billing method. Valid values:
        # 
        # - 1 (default): Pay-as-you-go for a reserved instance.
        # 
        # - 3: Pay-as-you-go for a reserved Serverless instance and pay-as-you-go for elastic scaling of a Serverless instance.
        self.paid_type = paid_type
        # The number of partitions. This parameter is recommended.
        # 
        # - You must specify this parameter or \\`TopicQuota\\`. We recommend that you specify only this parameter.
        # 
        # - If you specify both this parameter and \\`TopicQuota\\`, the system verifies whether the values of the two parameters are equivalent based on the previous topic-based sales model. If the values are not equivalent, the system returns a failure. If the values are equivalent, the purchase is made based on the number of partitions.
        # 
        # - For the valid values, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # > Do not specify this parameter if you create a Serverless instance.
        self.partition_num = partition_num
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        # 
        # If you do not set this parameter, the instance is added to the default resource group. You can view the resource group ID in the Resource Group console.
        self.resource_group_id = resource_group_id
        # The settings of the Serverless instance. This parameter is required if you create a Serverless instance.
        self.serverless_config = serverless_config
        # The specification type.
        # 
        # If you set \\`PaidType\\` to 1 (pay-as-you-go for a reserved instance), valid values are:
        # 
        # - normal: Standard Edition (High-write)
        # 
        # - professional: Professional Edition (High-write)
        # 
        # - professionalForHighRead: Professional Edition (High-read)
        # 
        # If you set \\`PaidType\\` to 3 (pay-as-you-go for a reserved Serverless instance and pay-as-you-go for elastic scaling of a Serverless instance), valid values are:
        # 
        # - basic: Serverless Basic Edition
        # 
        # - normal: Serverless Standard Edition
        # 
        # - professional: Serverless Professional Edition
        # 
        # For more information about these specification types, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        self.spec_type = spec_type
        # The tags.
        self.tag = tag
        # The number of topics. This parameter is not recommended.
        # 
        # - You must specify this parameter or \\`PartitionNum\\`. We recommend that you specify only \\`PartitionNum\\`.
        # 
        # - If you specify both this parameter and \\`PartitionNum\\`, the system verifies whether the values of the two parameters are equivalent based on the previous topic-based sales model. If the values are not equivalent, the system returns a failure. If the values are equivalent, the purchase is made based on the number of partitions.
        # 
        # - The default value of this parameter varies based on the traffic specification. You are charged for the extra topics that exceed the default value.
        # 
        # - For the valid values, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # > Do not specify this parameter if you create a Serverless instance.
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
        # The tag key.
        # 
        # - N can be an integer from 1 to 20.
        # 
        # - If this parameter is empty, all tag keys are matched.
        # 
        # - The tag key can be up to 128 characters in length. It cannot start with \\`aliyun\\` or \\`acs:\\` and cannot contain \\`http\\://\\` or \\`https\\://\\`.
        # 
        # This parameter is required.
        self.key = key
        # The tag value.
        # 
        # - N can be an integer from 1 to 20.
        # 
        # - This parameter must be empty if the tag key is empty. If this parameter is empty, all tag values are matched.
        # 
        # - The tag value can be up to 128 characters in length. It cannot start with \\`aliyun\\` or \\`acs:\\` and cannot contain \\`http\\://\\` or \\`https\\://\\`.
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
        # The reserved capacity for message publishing. You can specify only an integer for this parameter. The minimum value is 60. This parameter is required if you create a Serverless instance.
        # 
        # > The actual upper limit is subject to the inventory in the current region. For more information, see the instance purchase page.
        self.reserved_publish_capacity = reserved_publish_capacity
        # The reserved capacity for message subscription. You can specify only an integer for this parameter. The minimum value is 20. This parameter is required if you create a Serverless instance.
        # 
        # > The actual upper limit is subject to the inventory in the current region. For more information, see the instance purchase page.
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

