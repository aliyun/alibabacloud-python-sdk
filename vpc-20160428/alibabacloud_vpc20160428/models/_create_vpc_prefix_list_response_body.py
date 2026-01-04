# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateVpcPrefixListResponseBody(DaraModel):
    def __init__(
        self,
        prefix_list_id: str = None,
        request_id: str = None,
        resource_group_id: str = None,
    ):
        # The ID of the prefix list.
        self.prefix_list_id = prefix_list_id
        # The ID of the request.
        self.request_id = request_id
        # The ID of the resource group to which the prefix list belongs.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.prefix_list_id is not None:
            result['PrefixListId'] = self.prefix_list_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrefixListId') is not None:
            self.prefix_list_id = m.get('PrefixListId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

