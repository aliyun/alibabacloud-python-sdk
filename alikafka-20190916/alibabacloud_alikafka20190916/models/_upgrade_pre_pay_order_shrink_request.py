# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpgradePrePayOrderShrinkRequest(DaraModel):
    def __init__(
        self,
        confluent_config_shrink: str = None,
        disk_size: int = None,
        eip_max: int = None,
        eip_model: bool = None,
        instance_id: str = None,
        io_max: int = None,
        io_max_spec: str = None,
        paid_type: int = None,
        partition_num: int = None,
        region_id: str = None,
        spec_type: str = None,
        topic_quota: int = None,
    ):
        # Configurations for the Confluent components.
        self.confluent_config_shrink = confluent_config_shrink
        # The disk capacity.
        # 
        # - The specified disk capacity must be greater than or equal to the current disk capacity of the instance.
        # 
        # - For the valid values, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # > This parameter is required for subscription instances but not for Confluent-series instances.
        self.disk_size = disk_size
        # The maximum Internet traffic bandwidth.
        # 
        # - The specified Internet traffic bandwidth must be greater than or equal to the current Internet traffic bandwidth of the instance.
        # 
        # - For the valid values, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # > * If **EipModel** is set to **true**, **EipMax** must be greater than 0.
        # >
        # > * If **EipModel** is set to **false**, **EipMax** must be set to **0**.
        self.eip_max = eip_max
        # Specifies whether to enable Internet access. Valid values:
        # 
        # - `true`: enables Internet access.
        # 
        # - `false`: disables Internet access.
        # 
        # > This parameter is required for subscription instances but not for Confluent-series instances.
        self.eip_model = eip_model
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The traffic peak (not recommended).
        # 
        # - The specified traffic peak must be greater than or equal to the current traffic peak of the instance.
        # 
        # - You must specify either this parameter or `IoMaxSpec`. If you specify both, `IoMaxSpec` takes precedence. We recommend that you specify only `IoMaxSpec`.
        # 
        # - For the valid values, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        self.io_max = io_max
        # The traffic specification (recommended).
        # 
        # - The specified traffic specification must be greater than or equal to the current traffic specification of the instance.
        # 
        # - You must specify either this parameter or `IoMax`. If you specify both, this parameter takes precedence. We recommend that you specify only this parameter.
        # 
        # - For the valid values, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # > This parameter is required for subscription instances but not for Confluent-series instances.
        self.io_max_spec = io_max_spec
        # The billing method. Valid values:
        # 
        # - **0**: subscription
        # 
        # - **4**: subscription for Confluent instances
        self.paid_type = paid_type
        # The number of partitions (recommended).
        # 
        # - You must specify either this parameter or `TopicQuota`. We recommend that you specify only this parameter.
        # 
        # - If you specify both `PartitionNum` and `TopicQuota`, the system checks if their values are equivalent under the previous topic pricing model. A mismatch causes the request to fail. If they match, the system uses `PartitionNum` to process the purchase.
        # 
        # - For the valid values, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        # 
        # > This parameter is required for subscription instances but not for Confluent-series instances.
        self.partition_num = partition_num
        # The ID of the region where the instance is located.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The specification type.
        # 
        # Valid values for ApsaraMQ for Kafka instances:
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
        # You cannot downgrade an instance from Professional Edition to Standard Edition. For more information about these specification types, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        self.spec_type = spec_type
        # The number of topics (not recommended).
        # 
        # - You must specify either this parameter or `PartitionNum`. We recommend that you specify only `PartitionNum`.
        # 
        # - If you specify both `TopicQuota` and `PartitionNum`, the system checks if their values are equivalent under the previous topic pricing model. A mismatch causes the request to fail. If they match, the system uses `PartitionNum` to process the purchase.
        # 
        # - The default value of this parameter varies based on the traffic specification. You are charged additional fees if the specified value exceeds the default value.
        # 
        # - For the valid values, see [Billing](https://help.aliyun.com/document_detail/84737.html).
        self.topic_quota = topic_quota

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.confluent_config_shrink is not None:
            result['ConfluentConfig'] = self.confluent_config_shrink

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

        if self.paid_type is not None:
            result['PaidType'] = self.paid_type

        if self.partition_num is not None:
            result['PartitionNum'] = self.partition_num

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.spec_type is not None:
            result['SpecType'] = self.spec_type

        if self.topic_quota is not None:
            result['TopicQuota'] = self.topic_quota

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfluentConfig') is not None:
            self.confluent_config_shrink = m.get('ConfluentConfig')

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

        if m.get('PaidType') is not None:
            self.paid_type = m.get('PaidType')

        if m.get('PartitionNum') is not None:
            self.partition_num = m.get('PartitionNum')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SpecType') is not None:
            self.spec_type = m.get('SpecType')

        if m.get('TopicQuota') is not None:
            self.topic_quota = m.get('TopicQuota')

        return self

