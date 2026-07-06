# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alikafka20190916 import models as main_models
from darabonba.model import DaraModel

class CreatePrePayOrderShrinkRequest(DaraModel):
    def __init__(
        self,
        confluent_config_shrink: str = None,
        deploy_type: int = None,
        disk_size: int = None,
        disk_type: str = None,
        duration: int = None,
        eip_max: int = None,
        io_max: int = None,
        io_max_spec: str = None,
        paid_type: int = None,
        partition_num: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        spec_type: str = None,
        tag: List[main_models.CreatePrePayOrderShrinkRequestTag] = None,
        topic_quota: int = None,
    ):
        # The configuration of Confluent components.
        # 
        # > This parameter is required when you create a Confluent series instance.
        self.confluent_config_shrink = confluent_config_shrink
        # The deployment type. Valid values:
        # 
        # - **4**: Internet/VPC instance
        # 
        # - **5**: VPC instance
        # 
        # > If you are creating a Confluent series instance, you cannot select the deployment type. You can only set the value to 5. After the purchase, you can adjust whether each component is open to the Internet.
        self.deploy_type = deploy_type
        # The disk capacity. Unit: GB.
        # 
        # For the valid values, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # > If you are creating a Confluent series instance, you do not need to pass this parameter.
        self.disk_size = disk_size
        # The disk type. Valid values:
        # 
        # - **0**: ultra disk
        # 
        # - **1**: SSD
        # 
        # > If you are creating a Confluent series instance, you do not need to pass this parameter.
        self.disk_type = disk_type
        # The subscription duration. Unit: month. Default value: 1. Valid values:
        # 
        # - **Confluent instances: 1 or 12**
        # 
        # - **Kafka instances: 1**
        self.duration = duration
        # The Internet traffic.
        # 
        # - If **DeployType** is set to **4**, you must specify this parameter.
        # 
        # - For the valid values, see [pay-as-you-go](https://help.aliyun.com/document_detail/72142.html).
        # 
        # > If you are creating a Confluent series instance, you do not need to pass this parameter.
        self.eip_max = eip_max
        # The traffic peak (not recommended).
        # 
        # - You must specify either **IoMax** or **IoMaxSpec**. If you specify both parameters, **IoMaxSpec** takes precedence. We recommend that you specify only **IoMaxSpec**.
        # 
        # - For the valid values, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # > If you are creating a Confluent series instance, you do not need to pass this parameter.
        self.io_max = io_max
        # The traffic specification (recommended).
        # 
        # - You must specify either **IoMax** or **IoMaxSpec**. If you specify both parameters, **IoMaxSpec** takes precedence. We recommend that you specify only **IoMaxSpec**.
        # 
        # - For the valid values, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # > If you are creating a Confluent series instance, you do not need to pass this parameter.
        self.io_max_spec = io_max_spec
        # The billing method. Valid values:
        # 
        # - **0**: subscription
        # 
        # - **4**: Confluent series subscription
        self.paid_type = paid_type
        # The number of partitions (recommended).
        # 
        # - You must specify either the number of partitions or the topic specification. We recommend that you specify only the number of partitions.
        # 
        # - If you specify both the number of partitions and the topic specification, the system verifies whether the number of partitions is equivalent to the topic specification based on the old topic sales model. If they are not equivalent, the system returns a failure. If they are equivalent, the system makes the purchase based on the number of partitions.
        # 
        # - For the valid values, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # > If you are creating a Confluent series instance, you do not need to pass this parameter.
        self.partition_num = partition_num
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID.
        # 
        # If you do not specify this parameter, the instance is added to the default resource group. You can view the resource group ID in the Resource Group console.
        self.resource_group_id = resource_group_id
        # The specification type.
        # 
        # Valid values for Kafka instances:
        # 
        # - **normal**: Standard Edition (high write)
        # 
        # - **professional**: Professional Edition (high write)
        # 
        # - **professionalForHighRead**: Professional Edition (high read)
        # 
        # Valid values for Confluent instances:
        # 
        # - **professional**: Professional Edition
        # 
        # - **enterprise**: Enterprise Edition
        # 
        # For more information, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        self.spec_type = spec_type
        # The list of tags.
        self.tag = tag
        # The number of topics (not recommended).
        # 
        # - You must specify either the number of partitions or the topic specification. We recommend that you specify only the number of partitions.
        # 
        # - If you specify both the number of partitions and the topic specification, the system verifies whether the number of partitions is equivalent to the topic specification based on the old topic sales model. If they are not equivalent, the system returns a failure. If they are equivalent, the system makes the purchase based on the number of partitions.
        # 
        # - The default value varies based on the traffic specification. Additional fees are charged if the value exceeds the default value.
        # 
        # - For the valid values, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # > If you are creating a Confluent series instance, you do not need to pass this parameter.
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
        if self.confluent_config_shrink is not None:
            result['ConfluentConfig'] = self.confluent_config_shrink

        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type

        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size

        if self.disk_type is not None:
            result['DiskType'] = self.disk_type

        if self.duration is not None:
            result['Duration'] = self.duration

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
        if m.get('ConfluentConfig') is not None:
            self.confluent_config_shrink = m.get('ConfluentConfig')

        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')

        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')

        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

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

        if m.get('SpecType') is not None:
            self.spec_type = m.get('SpecType')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreatePrePayOrderShrinkRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TopicQuota') is not None:
            self.topic_quota = m.get('TopicQuota')

        return self

class CreatePrePayOrderShrinkRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the resource.
        # 
        # - N ranges from 1 to 20.
        # 
        # - If this parameter is empty, all tag keys are matched.
        # 
        # - The tag key can be up to 128 characters in length and cannot start with aliyun or acs:. It cannot contain http\\:// or https\\://.
        # 
        # This parameter is required.
        self.key = key
        # The tag value of the resource.
        # 
        # - N ranges from 1 to 20.
        # 
        # - This parameter can be empty.
        # 
        # - The tag value can be up to 128 characters in length and cannot start with aliyun or acs:. It cannot contain http\\:// or https\\://.
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

