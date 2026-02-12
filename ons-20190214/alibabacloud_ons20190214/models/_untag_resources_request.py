# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UntagResourcesRequest(DaraModel):
    def __init__(
        self,
        all: bool = None,
        instance_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag_key: List[str] = None,
    ):
        # Specifies whether to remove all tags that are attached to the specified resource. This parameter takes effect only if the **TagKey** parameter is empty. Default value: **false**.
        self.all = all
        # This parameter is required when you detach tags from a topic or a group.
        self.instance_id = instance_id
        # The resource IDs.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The type of the resource from which you want to detach tags. Valid values:
        # 
        # *   **INSTANCE**
        # *   **TOPIC**
        # *   **GROUP**
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tag keys of the resource.
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.all is not None:
            result['All'] = self.all

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        return self

