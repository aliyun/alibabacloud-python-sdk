# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListEventBusesRequest(DaraModel):
    def __init__(
        self,
        limit: int = None,
        name_prefix: str = None,
        next_token: str = None,
        resource_group_id: str = None,
    ):
        # The maximum number of entries to return per page. You can use this parameter together with NextToken to implement pagination.
        # 
        # >Notice: The maximum number of entries returned per request is 100.</notice>
        self.limit = limit
        # The name prefix of the event buses to retrieve.
        self.name_prefix = name_prefix
        # The pagination token. If the specified Limit is reached and more results are available, this token is returned. You can use this token together with Limit to implement pagination.
        self.next_token = next_token
        # The ID of the resource group, used to filter event buses in the specified resource group.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.limit is not None:
            result['Limit'] = self.limit

        if self.name_prefix is not None:
            result['NamePrefix'] = self.name_prefix

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('NamePrefix') is not None:
            self.name_prefix = m.get('NamePrefix')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

