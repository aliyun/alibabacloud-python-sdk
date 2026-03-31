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
        self.delivery_type = delivery_type
        self.extend_config = extend_config
        # This parameter is required.
        self.field_list = field_list
        # This parameter is required.
        self.instance_id = instance_id
        self.log_delivery_strategy = log_delivery_strategy
        self.region_id = region_id
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

