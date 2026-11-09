# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_wss20211221 import models as main_models
from darabonba.model import DaraModel

class ModifyInstancePropertiesRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_ids: List[str] = None,
        key: str = None,
        properties: List[main_models.ModifyInstancePropertiesRequestProperties] = None,
        resource_type: str = None,
        value: str = None,
    ):
        # The ID of the instance.
        self.instance_id = instance_id
        # The instance IDs.
        self.instance_ids = instance_ids
        # The key of the attribute.
        self.key = key
        # The list of instance attributes to modify. You can modify multiple key-value pairs at a time. These pairs are merged with the original Key and Value request parameters. If an attribute with the same name has the same value, it is deduplicated. If the values are different, a parameter error is returned.
        self.properties = properties
        # The resource type.
        # > This parameter is case-sensitive. Ensure correct spelling.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The value of the attribute.
        # 
        # - PackageUsedUpStrategy: [enum]
        #    - Postpaid (switches to the pay-as-you-go billing method)
        #    - Shutdown (hibernates or shuts down the instance)
        #    - Maintenance (stops the instance and enters O&M mode, and does not allow client connections)
        self.value = value

    def validate(self):
        if self.properties:
            for v1 in self.properties:
                 if v1:
                    v1.validate()

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

        result['Properties'] = []
        if self.properties is not None:
            for k1 in self.properties:
                result['Properties'].append(k1.to_map() if k1 else None)

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

        self.properties = []
        if m.get('Properties') is not None:
            for k1 in m.get('Properties'):
                temp_model = main_models.ModifyInstancePropertiesRequestProperties()
                self.properties.append(temp_model.from_map(k1))

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ModifyInstancePropertiesRequestProperties(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The name of the instance attribute. For example, DisableRemainingNotify specifies whether to disable the remaining duration reminder for the client, and PackageUsedUpStrategy specifies the policy applied when the package duration is used up.
        self.key = key
        # The value of the instance attribute. When Key is set to DisableRemainingNotify, only the string true or false is supported, and ResourceType must be set to DurationPackage. A value of true indicates that the remaining duration reminder for the client is disabled. A value of false indicates that the reminder is retained and triggered based on the original conditions. Administrator notifications continue to be triggered based on the original conditions. For other attributes, pass values based on their respective definitions.
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

