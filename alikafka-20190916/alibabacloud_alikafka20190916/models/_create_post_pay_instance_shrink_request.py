# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alikafka20190916 import models as main_models
from darabonba.model import DaraModel

class CreatePostPayInstanceShrinkRequest(DaraModel):
    def __init__(
        self,
        deploy_type: int = None,
        disk_size: int = None,
        disk_type: str = None,
        eip_max: int = None,
        io_max_spec: str = None,
        paid_type: int = None,
        partition_num: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        serverless_config_shrink: str = None,
        spec_type: str = None,
        tag: List[main_models.CreatePostPayInstanceShrinkRequestTag] = None,
    ):
        # The deployment type. Valid values:
        # 
        # - **4**: instance that is accessible over the internet and a VPC
        # 
        # - **5**: instance that is accessible only over a VPC
        # 
        # This parameter is required.
        self.deploy_type = deploy_type
        # The disk capacity.
        # 
        # For more information about the value range, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # > This parameter is not required when you create a Serverless instance.
        self.disk_size = disk_size
        # The disk type. Valid values:
        # 
        # - **0**: ultra disk
        # 
        # - **1**: SSD
        # 
        # > This parameter is not required when you create a Serverless instance.
        self.disk_type = disk_type
        # The Internet traffic.
        # 
        # - This parameter is required if you set **DeployType** to **4**.
        # 
        # - For more information about the value range, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # > This parameter is not required when you create a Serverless instance.
        self.eip_max = eip_max
        # The traffic specification.
        # 
        # - For more information about the value range, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # > This parameter is not required when you create a Serverless instance.
        self.io_max_spec = io_max_spec
        # The billing method. Valid values:
        # 
        # - 1 (default): pay-as-you-go for reserved instances.
        # 
        # - 3: pay-as-you-go for reserved capacity and elastic scaling of Serverless instances.
        self.paid_type = paid_type
        # The number of partitions.
        # 
        # - For more information about the value range, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # > This parameter is not required if the instance is a Serverless instance.
        self.partition_num = partition_num
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        # 
        # If you do not specify this parameter, the instance is added to the default resource group. You can view the resource group ID in the Resource Group console.
        self.resource_group_id = resource_group_id
        # The settings of the Serverless instance. This parameter is required when you create a Serverless instance.
        self.serverless_config_shrink = serverless_config_shrink
        # The edition of the instance.
        # 
        # If you set the PaidType parameter to 1 (pay-as-you-go for reserved instances), valid values are:
        # 
        # - normal: Standard Edition (High-write)
        # 
        # - professional: Professional Edition (High-write)
        # 
        # - professionalForHighRead: Professional Edition (High-read)
        # 
        # If you set the PaidType parameter to 3 (pay-as-you-go for reserved capacity and elastic scaling of Serverless instances), valid values are:
        # 
        # - basic: Serverless Basic Edition
        # 
        # - normal: Serverless Standard Edition
        # 
        # - professional: Serverless Professional Edition
        # 
        # For more information about these instance editions, see [Billing](https://help.aliyun.com/document_detail/84737.html).
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
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type

        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size

        if self.disk_type is not None:
            result['DiskType'] = self.disk_type

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

        if self.serverless_config_shrink is not None:
            result['ServerlessConfig'] = self.serverless_config_shrink

        if self.spec_type is not None:
            result['SpecType'] = self.spec_type

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

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
                temp_model = main_models.CreatePostPayInstanceShrinkRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class CreatePostPayInstanceShrinkRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the resource.
        # 
        # - The value of N can be from 1 to 20.
        # 
        # - If this parameter is left empty, all tag keys are matched.
        # 
        # - The tag key can be up to 128 characters in length. It cannot start with aliyun or acs: and cannot contain http\\:// or https\\://.
        # 
        # This parameter is required.
        self.key = key
        # The tag value of the resource.
        # 
        # - The value of N can be from 1 to 20.
        # 
        # - If the tag key is empty, this parameter must also be empty. If this parameter is empty, all tag values are matched.
        # 
        # - The tag value can be up to 128 characters in length. It cannot start with aliyun or acs: and cannot contain http\\:// or https\\://.
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

