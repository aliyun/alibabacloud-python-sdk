# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpgradePostPayOrderShrinkRequest(DaraModel):
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
        serverless_config_shrink: str = None,
        spec_type: str = None,
        topic_quota: int = None,
    ):
        # The disk size. Unit: GB.
        # 
        # *   The disk size that you specify must be greater than or equal to the current disk size of the instance.
        # *   For information about the valid values of this parameter, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # >  If the instance is a serverless ApsaraMQ for Kafka instance, you do not need to configure this parameter.
        self.disk_size = disk_size
        # The maximum Internet traffic of the instance.
        # 
        # *   The Internet traffic that you specify must be greater than or equal to the current Internet traffic of the instance.
        # *   For information about the valid values of this parameter, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # > 
        # 
        # *   If you set **EipModel** to **true**, set **EipMax** to a value that is greater than 0.
        # 
        # *   If you set **EipModel** to **false**, set **EipMax** to **0**.
        # 
        # *   If the instance is a serverless ApsaraMQ for Kafka instance, you do not need to configure this parameter.
        self.eip_max = eip_max
        # Specifies whether to enable Internet access for the instance. Valid values:
        # 
        # *   true: enables Internet access.
        # *   false: disables Internet access.
        self.eip_model = eip_model
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The maximum traffic of the instance. We recommend that you do not configure this parameter.
        # 
        # *   The maximum traffic that you specify must be greater than or equal to the current maximum traffic of the instance.
        # *   You must configure at least one of IoMax and IoMaxSpec. If you configure both parameters, the value of IoMaxSpec takes effect. We recommend that you configure only IoMaxSpec.
        # *   For information about the valid values of this parameter, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # >  If the instance is a serverless ApsaraMQ for Kafka instance, you do not need to configure this parameter.
        self.io_max = io_max
        # The traffic specification of the instance. We recommend that you configure this parameter.
        # 
        # *   The traffic specification that you specify must be greater than or equal to the current traffic specification of the instance.
        # *   You must configure at least one of IoMax and IoMaxSpec. If you configure both parameters, the value of IoMaxSpec takes effect. We recommend that you configure only IoMaxSpec.
        # *   For information about the valid values of this parameter, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # >  If the instance is a serverless ApsaraMQ for Kafka instance, you do not need to configure this parameter.
        self.io_max_spec = io_max_spec
        # The number of partitions. We recommend that you configure this parameter.
        # 
        # *   You must configure one of PartitionNum and TopicQuota. We recommend that you configure only PartitionNum.
        # *   If you configure PartitionNum and TopicQuota at the same time, the system verifies whether the price of the partitions equals the price of the topics based on the previous topic-based selling mode. If the price of the partitions does not equal the price of the topics, an error is returned. If the price of the partitions equals the price of the topics, the instance is purchased based on the partition number.
        # *   For information about the valid values of this parameter, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # >  If the instance is a serverless ApsaraMQ for Kafka instance, you do not need to configure this parameter.
        self.partition_num = partition_num
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The parameters that are configured for the serverless instance. These parameters are required only when you create a serverless instance.
        self.serverless_config_shrink = serverless_config_shrink
        # The instance edition.
        # 
        # Valid values for this parameter if you set PaidType to 1:
        # 
        # *   normal: Standard Edition (High Write)
        # *   professional: Professional Edition (High Write)
        # *   professionalForHighRead: Professional Edition (High Read)
        # 
        # Valid values for this parameter if you set PaidType to 3:
        # 
        # *   normal: Serverless Standard Edition
        # 
        # For more information, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        self.spec_type = spec_type
        # The number of topics. We recommend that you do not configure this parameter.
        # 
        # *   You must configure one of PartitionNum and TopicQuota. We recommend that you configure only PartitionNum.
        # *   If you configure PartitionNum and TopicQuota at the same time, the system verifies whether the price of the partitions equals the price of the topics based on the previous topic-based selling mode. If the price of the partitions does not equal the price of the topics, an error is returned. If the price of the partitions equals the price of the topics, the instance is purchased based on the partition number.
        # *   The default value of TopicQuota varies based on the value of IoMaxSpec. If the number of topics that you use exceeds the default value, you are charged additional fees.
        # *   For information about the valid values of this parameter, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # >  If the instance is a serverless ApsaraMQ for Kafka instance, you do not need to configure this parameter.
        self.topic_quota = topic_quota

    def validate(self):
        pass

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

        if self.serverless_config_shrink is not None:
            result['ServerlessConfig'] = self.serverless_config_shrink

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
            self.serverless_config_shrink = m.get('ServerlessConfig')

        if m.get('SpecType') is not None:
            self.spec_type = m.get('SpecType')

        if m.get('TopicQuota') is not None:
            self.topic_quota = m.get('TopicQuota')

        return self

