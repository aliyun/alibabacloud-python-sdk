# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListApplicationsForSwimmingLaneRequest(DaraModel):
    def __init__(
        self,
        group_id: int = None,
        namespace_id: str = None,
        tag: str = None,
    ):
        # The ID of the application group. You can call the [DescribeApplicationGroups](https://help.aliyun.com/document_detail/126249.html) operation to obtain the ID.
        self.group_id = group_id
        # The ID of a namespace.
        # 
        # This parameter is required.
        self.namespace_id = namespace_id
        # The canary tag
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.tag is not None:
            result['Tag'] = self.tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        return self

