# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_alikafka20190916 import models as main_models
from darabonba.model import DaraModel

class UpgradePostPayOrderRequest(DaraModel):
    def __init__(
        self,
        disk_size: int = None,
        eip_max: int = None,
        eip_model: bool = None,
        instance_id: str = None,
        io_max: int = None,
        io_max_spec: str = None,
        partition_num: int = None,
        region_id: str = None,
        serverless_config: main_models.UpgradePostPayOrderRequestServerlessConfig = None,
        spec_type: str = None,
        topic_quota: int = None,
    ):
        # The disk capacity. Unit: GB.
        # 
        # - The disk capacity that you specify must be greater than or equal to the current disk capacity of the instance.
        # 
        # - For the value range, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # > If the instance is a serverless instance, you do not need to specify this parameter. This parameter is required for pay-as-you-go instances.
        self.disk_size = disk_size
        # The public network traffic.
        # 
        # - The public network traffic that you specify must be greater than or equal to the current public network traffic of the instance.
        # - For the value range, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # > - If **EipModel** is set to **true**, the value of **EipMax** must be greater than 0.
        # > - If **EipModel** is set to **false**, the value of **EipMax** must be **0**.
        # > - If the instance is a serverless instance, you do not need to specify this parameter.
        self.eip_max = eip_max
        # Specifies whether the instance requires Internet access. Valid values:
        # 
        # - true: Internet access is required.
        # 
        # - false: Internet access is not required.
        # > This parameter is optional for pay-as-you-go instances. This parameter is required for serverless instances.
        self.eip_model = eip_model
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The peak traffic (not recommended).
        # 
        # - The peak traffic that you specify must be greater than or equal to the current peak traffic of the instance.
        # 
        # - You must specify either the traffic specification or the peak traffic. If you specify both, the traffic specification takes precedence. Specify only the traffic specification.
        # 
        # - For the value range, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # > If the instance is a serverless instance, you do not need to specify this parameter.
        self.io_max = io_max
        # The traffic specification (recommended).
        # 
        # - The traffic specification that you specify must be greater than or equal to the current traffic specification of the instance.
        # 
        # - You must specify either the traffic specification or the peak traffic. If you specify both, the traffic specification takes precedence. Specify only the traffic specification.
        # 
        # - For the value range, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # > If the instance is a serverless instance, you do not need to specify this parameter. This parameter is required for pay-as-you-go instances.
        self.io_max_spec = io_max_spec
        # The number of partitions (recommended).
        # 
        # * You must specify either the number of partitions or the topic specification. Specify only the number of partitions.
        # 
        # * If you specify both the number of partitions and the topic specification, the system verifies whether the number of partitions and the topic specification are equivalent based on the legacy topic sales model. If they are not equivalent, the request fails. If they are equivalent, the purchase is made based on the number of partitions.
        # 
        # * For the value range, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # > If the instance is a serverless instance, you do not need to specify this parameter. This parameter is required for pay-as-you-go instances.
        self.partition_num = partition_num
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The settings of the serverless instance. This parameter is required when you upgrade a serverless instance.
        self.serverless_config = serverless_config
        # The specification type.
        # 
        # If the PaidType of the instance is 1 (pay-as-you-go), valid values:
        # 
        # - normal: Standard Edition (shared throughput)
        # - professional: Professional Edition (shared throughput)
        # - professionalForHighRead: Professional Edition (shared throughput for high read)
        # 
        # If the PaidType of the instance is 3 (reserved specification pay-as-you-go + serverless elastic scaling pay-as-you-go), valid values:
        # - normal: Serverless Standard Edition
        # 
        # For more information, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        self.spec_type = spec_type
        # The number of topics (not recommended).
        # 
        # - You must specify either the number of partitions or the topic specification. Specify only the number of partitions.
        # 
        # - If you specify both the number of partitions and the topic specification, the system verifies whether the number of partitions and the topic specification are equivalent based on the legacy topic sales model. If they are not equivalent, the request fails. If they are equivalent, the purchase is made based on the number of partitions.
        # 
        # - The default value varies based on the traffic specification. Additional fees are charged if the value exceeds the default value.
        # 
        # - For the value range, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # > If the instance is a serverless instance, you do not need to specify this parameter.
        self.topic_quota = topic_quota

    def validate(self):
        if self.serverless_config:
            self.serverless_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size

        if self.eip_max is not None:
            result['EipMax'] = self.eip_max

        if self.eip_model is not None:
            result['EipModel'] = self.eip_model

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.io_max is not None:
            result['IoMax'] = self.io_max

        if self.io_max_spec is not None:
            result['IoMaxSpec'] = self.io_max_spec

        if self.partition_num is not None:
            result['PartitionNum'] = self.partition_num

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.serverless_config is not None:
            result['ServerlessConfig'] = self.serverless_config.to_map()

        if self.spec_type is not None:
            result['SpecType'] = self.spec_type

        if self.topic_quota is not None:
            result['TopicQuota'] = self.topic_quota

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')

        if m.get('EipMax') is not None:
            self.eip_max = m.get('EipMax')

        if m.get('EipModel') is not None:
            self.eip_model = m.get('EipModel')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IoMax') is not None:
            self.io_max = m.get('IoMax')

        if m.get('IoMaxSpec') is not None:
            self.io_max_spec = m.get('IoMaxSpec')

        if m.get('PartitionNum') is not None:
            self.partition_num = m.get('PartitionNum')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ServerlessConfig') is not None:
            temp_model = main_models.UpgradePostPayOrderRequestServerlessConfig()
            self.serverless_config = temp_model.from_map(m.get('ServerlessConfig'))

        if m.get('SpecType') is not None:
            self.spec_type = m.get('SpecType')

        if m.get('TopicQuota') is not None:
            self.topic_quota = m.get('TopicQuota')

        return self

class UpgradePostPayOrderRequestServerlessConfig(DaraModel):
    def __init__(
        self,
        reserved_publish_capacity: int = None,
        reserved_subscribe_capacity: int = None,
    ):
        # The reserved publish capacity. Only integers are supported. The minimum value is 60. This parameter is required for serverless instances.
        # > The actual upper limit is subject to the available inventory in the current region. Refer to the purchase page for the available range.
        self.reserved_publish_capacity = reserved_publish_capacity
        # The reserved subscribe capacity. Only integers are supported. The minimum value is 20. This parameter is required for serverless instances.
        # 
        # > The actual upper limit is subject to the available inventory in the current region. Refer to the purchase page for the available range.
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

