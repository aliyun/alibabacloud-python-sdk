# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alikafka20190916 import models as main_models
from darabonba.model import DaraModel

class CreatePrePayInstanceShrinkRequest(DaraModel):
    def __init__(
        self,
        confluent_config_shrink: str = None,
        deploy_type: int = None,
        disk_size: int = None,
        disk_type: str = None,
        duration: int = None,
        eip_max: int = None,
        io_max_spec: str = None,
        paid_type: int = None,
        partition_num: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        spec_type: str = None,
        tag: List[main_models.CreatePrePayInstanceShrinkRequestTag] = None,
    ):
        # The Confluent component configurations.
        # 
        # 
        # > This parameter is required when you create a Confluent instance.
        self.confluent_config_shrink = confluent_config_shrink
        # The deployment type. Valid values:
        # 
        # - **4**: Internet- and VPC-connected instance
        # 
        # - **5**: VPC-connected instance
        # 
        # 
        # > When you create a Confluent instance, you cannot select the deployment type. Only the value 5 is allowed. After the purchase, you can configure whether to enable public access for each component.
        self.deploy_type = deploy_type
        # The disk capacity. Unit: GB.
        # 
        # For the value range, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # > This parameter is not required when you create a Confluent instance.
        self.disk_size = disk_size
        # The disk type. Valid values:
        # 
        # - **0**: ultra cloud disk
        # 
        # - **1**: SSD
        # 
        # > This parameter is not required when you create a Confluent instance.
        self.disk_type = disk_type
        # The subscription duration. Unit: months. Default value: 1. Valid values:
        # 
        # - **Confluent instances: 1 or 12**
        # - **ApsaraMQ for Kafka instances: 1**
        self.duration = duration
        # The Internet traffic.
        # 
        # - This parameter is required if **DeployType** is set to **4**.
        # 
        # - For the value range, see [Pay-as-you-go billing method](https://help.aliyun.com/document_detail/72142.html).
        # 
        # 
        # > This parameter is not required when you create a Confluent instance.
        self.eip_max = eip_max
        # The traffic specification.
        #  
        # 
        # - For the value range, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # > This parameter is not required when you create a Confluent instance.
        self.io_max_spec = io_max_spec
        # The billing type. Valid values:
        # 
        # - **0**: subscription
        # 
        # - **4**: Confluent subscription
        self.paid_type = paid_type
        # The number of partitions to purchase.
        # 
        # * For the value range, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # > This parameter is not required when you create a Confluent instance.
        self.partition_num = partition_num
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID.
        # 
        # If you do not specify this parameter, the instance is placed in the default resource group. You can view the resource group ID in the Resource Management console.
        self.resource_group_id = resource_group_id
        # The edition type.
        # 
        # Valid values for ApsaraMQ for Kafka instances:
        # 
        # - **normal**: Standard Edition (shared throughput for writes)
        # 
        # - **professional**: Professional Edition (shared throughput for writes)
        # 
        # - **professionalForHighRead**: Professional Edition (shared throughput for reads)
        # 
        # Valid values for Confluent instances:
        # 
        # - **professional**: Professional Edition
        # 
        # - **enterprise**: Enterprise Edition
        # 
        # For more information, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        self.spec_type = spec_type
        # The tags.
        self.tag = tag

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
                temp_model = main_models.CreatePrePayInstanceShrinkRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class CreatePrePayInstanceShrinkRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the resource.
        # 
        # - N ranges from 1 to 20.
        # 
        # - If this parameter is left empty, all tag keys are matched.
        # 
        # - The tag key can be up to 128 characters in length and cannot start with aliyun or acs:. It cannot contain http:// or https://.
        # 
        # This parameter is required.
        self.key = key
        # The tag value of the resource.
        # 
        # - N ranges from 1 to 20.
        # 
        # - This parameter can be left empty.
        # 
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

