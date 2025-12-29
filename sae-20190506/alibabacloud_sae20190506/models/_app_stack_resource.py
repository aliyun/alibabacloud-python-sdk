# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AppStackResource(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        instance_id: str = None,
        product_code: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
        stack_id: str = None,
        status: str = None,
    ):
        self.create_time = create_time
        self.instance_id = instance_id
        self.product_code = product_code
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_type = resource_type
        self.stack_id = stack_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.stack_id is not None:
            result['StackId'] = self.stack_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

