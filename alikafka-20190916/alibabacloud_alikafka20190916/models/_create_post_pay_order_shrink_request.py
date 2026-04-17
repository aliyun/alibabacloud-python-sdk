# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alikafka20190916 import models as main_models
from darabonba.model import DaraModel

class CreatePostPayOrderShrinkRequest(DaraModel):
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
        serverless_config_shrink: str = None,
        spec_type: str = None,
        tag: List[main_models.CreatePostPayOrderShrinkRequestTag] = None,
        topic_quota: int = None,
    ):
        # The deployment mode of the instance. Valid values:
        # 
        # *   **4**: deploys the instance that allows access from the Internet and a VPC.
        # *   **5**: deploys the instance that allows access only from a VPC.
        # 
        # This parameter is required.
        self.deploy_type = deploy_type
        # The disk size.
        # 
        # For information about the valid values of this parameter, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # >  If you create a serverless ApsaraMQ for Kafka instance, you do not need to configure this parameter.
        self.disk_size = disk_size
        # The disk type of the instance. Valid values:
        # 
        # *   **0**: ultra disk
        # *   **1**: standard SSD
        # 
        # >  If you create a serverless ApsaraMQ for Kafka instance, you do not need to configure this parameter.
        self.disk_type = disk_type
        # The Internet traffic.
        # 
        # *   If you set **DeployType** to **4**, you must configure this parameter.
        # *   For information about the valid values of this parameter, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # >  If you create a serverless ApsaraMQ for Kafka instance, you do not need to configure this parameter.
        self.eip_max = eip_max
        # The maximum traffic in the instance. We recommend that you do not configure this parameter.
        # 
        # *   You must configure at least one of IoMax and IoMaxSpec. If you configure both parameters, the value of IoMaxSpec takes effect. We recommend that you configure only IoMaxSpec.
        # *   For information about the valid values of this parameter, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # >  If you create a serverless ApsaraMQ for Kafka instance, you do not need to configure this parameter.
        self.io_max = io_max
        # The traffic specification of the instance. We recommend that you configure this parameter.
        # 
        # *   You must configure at least one of IoMax and IoMaxSpec. If you configure both parameters, the value of IoMaxSpec takes effect. We recommend that you configure only IoMaxSpec.
        # *   For information about the valid values of this parameter, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # >  If you create a serverless ApsaraMQ for Kafka instance, you do not need to configure this parameter.
        self.io_max_spec = io_max_spec
        # The billing method of the instance. Valid values:
        # 
        # *   1: pay-as-you-go (reserved capacity).
        # *   3: pay-as-you-go (reserved capacity) + pay-as-you-go (on-demand capacity)
        self.paid_type = paid_type
        # The number of partitions. We recommend that you configure this parameter.
        # 
        # *   You must configure one of PartitionNum and TopicQuota. We recommend that you configure only ParittionNum.
        # *   If you configure PartitionNum and TopicQuota at the same time, the system verifies whether the price of the partitions equals the price of the topics based on the previous topic-based selling mode. If the price of the partitions does not equal the price of the topics, an error is returned. If the price of the partitions equals the price of the topics, the instance is purchased based on the partition number.
        # *   For information about the valid values of this parameter, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # >  If you create a serverless ApsaraMQ for Kafka instance, you do not need to configure this parameter.
        self.partition_num = partition_num
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        # 
        # If this parameter is left empty, the default resource group is used. You can view the resource group ID on the Resource Group page in the Resource Management console.
        self.resource_group_id = resource_group_id
        # The parameters configured for the serverless ApsaraMQ for Kafka instance. These parameters are required only when you create a serverless instance.
        self.serverless_config_shrink = serverless_config_shrink
        # The instance edition.
        # 
        # Valid values if you set PaidType to 1:
        # 
        # *   normal: Standard Edition (High Write)
        # *   professional: Professional Edition (High Write)
        # *   professionalForHighRead: Professional Edition (High Read)
        # 
        # Valid values if you set PaidType to 3:
        # 
        # *   normal: Serverless Standard Edition
        # 
        # For more information about the instance editions, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        self.spec_type = spec_type
        # The tags.
        self.tag = tag
        # The number of topics. We recommend that you do not configure this parameter.
        # 
        # *   You must configure one of PartitionNum and TopicQuota. We recommend that you configure only ParittionNum.
        # *   If you configure PartitionNum and TopicQuota at the same time, the system verifies whether the price of the partitions equals the price of the topics based on the previous topic-based selling mode. If the price of the partitions does not equal the price of the topics, an error is returned. If the price of the partitions equals the price of the topics, the instance is purchased based on the partition number.
        # *   The default value of TopicQuota varies based on the value of IoMaxSpec. If the number of topics that you consume exceeds the default value, you are charged additional fees.
        # *   For information about the valid values of this parameter, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # >  If you create a serverless ApsaraMQ for Kafka instance, you do not need to configure this parameter.
        self.topic_quota = topic_quota

    def validate(self):
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

        if self.serverless_config_shrink is not None:
            result['ServerlessConfig'] = self.serverless_config_shrink

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
            self.serverless_config_shrink = m.get('ServerlessConfig')

        if m.get('SpecType') is not None:
            self.spec_type = m.get('SpecType')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreatePostPayOrderShrinkRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TopicQuota') is not None:
            self.topic_quota = m.get('TopicQuota')

        return self

class CreatePostPayOrderShrinkRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N.
        # 
        # *   Valid values of N: 1 to 20.
        # *   If this parameter is left empty, the keys of all tags are matched.
        # *   The tag key must be up to 128 characters in length. It cannot start with acs: or aliyun or contain [http:// or https://.](http://https://。)
        # 
        # This parameter is required.
        self.key = key
        # The value of tag N.
        # 
        # *   Valid values of N: 1 to 20.
        # *   If you do not specify a tag key, you cannot specify a tag value. If this parameter is not configured, all tag values are matched.
        # *   The tag value must be 1 to 128 characters in length. It cannot start with acs: or aliyun or contain [http:// or https://.](http://https://。)
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

