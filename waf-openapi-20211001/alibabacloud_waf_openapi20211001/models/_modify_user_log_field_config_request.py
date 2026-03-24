# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyUserLogFieldConfigRequest(DaraModel):
    def __init__(
        self,
        delivery_type: str = None,
        extend_config: str = None,
        field_list: str = None,
        instance_id: str = None,
        log_delivery_strategy: str = None,
        region_id: str = None,
        resource_manager_resource_group_id: str = None,
    ):
        # The delivery type. Valid value:
        # 
        # - **sls**: Simple Log Service.
        self.delivery_type = delivery_type
        # The extended configuration for log delivery, in JSON format.
        # 
        # > For more information, see the description of the **ExtendConfig** parameter.
        self.extend_config = extend_config
        # The list of log fields to deliver. Use the \\`a,b,c,...\\` format.
        # 
        # > - You must include all required log fields. Call the [DescribeCommonLogFields](~~DescribeCommonLogFields~~) operation to view the log fields that WAF supports.
        # >
        # > - If the log fields include **request_header**, use the **ExtendConfig** parameter to specify the request headers to deliver.
        # 
        # This parameter is required.
        self.field_list = field_list
        # The ID of the WAF instance.
        # 
        # > Call the [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) operation to view the ID of your WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The log delivery strategy, in JSON array format. You can specify multiple strategies.
        # 
        # > For more information, see the description of the **LogDeliveryStrategy** parameter.
        self.log_delivery_strategy = log_delivery_strategy
        # The region in which the WAF instance resides. Valid values:
        # 
        # - **cn-hangzhou**: the Chinese mainland.
        # 
        # - **ap-southeast-1**: outside the Chinese mainland.
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
        if self.delivery_type is not None:
            result['DeliveryType'] = self.delivery_type

        if self.extend_config is not None:
            result['ExtendConfig'] = self.extend_config

        if self.field_list is not None:
            result['FieldList'] = self.field_list

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.log_delivery_strategy is not None:
            result['LogDeliveryStrategy'] = self.log_delivery_strategy

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryType') is not None:
            self.delivery_type = m.get('DeliveryType')

        if m.get('ExtendConfig') is not None:
            self.extend_config = m.get('ExtendConfig')

        if m.get('FieldList') is not None:
            self.field_list = m.get('FieldList')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LogDeliveryStrategy') is not None:
            self.log_delivery_strategy = m.get('LogDeliveryStrategy')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        return self

