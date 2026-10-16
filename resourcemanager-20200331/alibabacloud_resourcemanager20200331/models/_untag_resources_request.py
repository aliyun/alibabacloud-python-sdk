# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UntagResourcesRequest(DaraModel):
    def __init__(
        self,
        all: bool = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag_key: List[str] = None,
    ):
        # Specifies whether to unbind all tags from the specified resource group or resource directory member. Valid values:
        # - false (default): No.
        # - true: Yes.
        self.all = all
        # The ID of the resource group or resource directory member.
        # 
        # You can specify up to 50 IDs.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The resource type. Valid values:
        # 
        # - ResourceGroup (default): Unbinds tags from a resource group.
        # - Account: Unbinds tags from a resource directory member.
        # 
        # > This parameter is required when you unbind tags from a resource directory member.
        self.resource_type = resource_type
        # The tag key.
        # 
        # You can unbind up to 20 tag keys.
        # 
        # > If the `All` parameter for unbinding all tags is set to `true`, you do not need to specify tag keys.
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

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        return self

