# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyLogDeliveryConfigRequest(DaraModel):
    def __init__(
        self,
        delivery_detail: str = None,
        delivery_name: str = None,
        delivery_type: str = None,
        instance_id: str = None,
        region_id: str = None,
        resource_manager_resource_group_id: str = None,
    ):
        # The content of the log delivery configuration. Set the value to a JSON string that contains multiple parameters.
        # 
        # >  This parameter is the same as the **DeliveryDetail** parameter of the **CreateLogDeliveryConfig** operation. For more information, see **Parameter description for log delivery configuration** of the [CreateLogDeliveryConfig](~~CreateLogDeliveryConfig~~) operation.
        # 
        # This parameter is required.
        self.delivery_detail = delivery_detail
        # The name of the log delivery configuration that you want to modify.
        # 
        # This parameter is required.
        self.delivery_name = delivery_name
        # The type of the log delivery configuration that you want to modify. Valid values:
        # 
        # *   **syslog**: Logs are delivered to a syslog service.
        # *   **kafka**: Logs are delivered to a Kafka service.
        # 
        # This parameter is required.
        self.delivery_type = delivery_type
        # The ID of the Web Application Firewall (WAF) instance.
        # 
        # >  You can call the [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) operation to query the ID of the WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID of the WAF instance. Valid values:
        # 
        # *   **cn-hangzhou**: the Chinese mainland.
        # *   **ap-southeast-1**: outside the Chinese mainland.
        self.region_id = region_id
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delivery_detail is not None:
            result['DeliveryDetail'] = self.delivery_detail

        if self.delivery_name is not None:
            result['DeliveryName'] = self.delivery_name

        if self.delivery_type is not None:
            result['DeliveryType'] = self.delivery_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryDetail') is not None:
            self.delivery_detail = m.get('DeliveryDetail')

        if m.get('DeliveryName') is not None:
            self.delivery_name = m.get('DeliveryName')

        if m.get('DeliveryType') is not None:
            self.delivery_type = m.get('DeliveryType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        return self

