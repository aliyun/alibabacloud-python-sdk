# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyInstancePropertiesRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_ids: List[str] = None,
        key: str = None,
        resource_type: str = None,
        value: str = None,
    ):
        # The ID of the instance.
        self.instance_id = instance_id
        # The instance ID.
        self.instance_ids = instance_ids
        # The key of the attribute.
        self.key = key
        # The resource type.
        # > This parameter is case-sensitive. Ensure that the value is spelled correctly.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The value of the attribute.
        # 
        # - PackageUsedUpStrategy: Valid values:
        #    - Postpaid: Enters the pay-as-you-go phase.
        #    - Shutdown: Hibernation.
        #    - Maintenance: Shuts down and enters O&M mode. Client connections are not allowed.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.key is not None:
            result['Key'] = self.key

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

