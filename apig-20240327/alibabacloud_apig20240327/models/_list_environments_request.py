# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListEnvironmentsRequest(DaraModel):
    def __init__(
        self,
        alias_like: str = None,
        gateway_id: str = None,
        gateway_name_like: str = None,
        gateway_type: str = None,
        name_like: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
    ):
        # Environment alias, fuzzy search.
        self.alias_like = alias_like
        # Gateway ID, exact search.
        self.gateway_id = gateway_id
        # Gateway name, fuzzy search.
        self.gateway_name_like = gateway_name_like
        self.gateway_type = gateway_type
        # Environment name, fuzzy search.
        self.name_like = name_like
        # Page number, default is 1.
        self.page_number = page_number
        # Page size, default is 10.
        self.page_size = page_size
        # Resource group ID.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias_like is not None:
            result['aliasLike'] = self.alias_like

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.gateway_name_like is not None:
            result['gatewayNameLike'] = self.gateway_name_like

        if self.gateway_type is not None:
            result['gatewayType'] = self.gateway_type

        if self.name_like is not None:
            result['nameLike'] = self.name_like

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliasLike') is not None:
            self.alias_like = m.get('aliasLike')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('gatewayNameLike') is not None:
            self.gateway_name_like = m.get('gatewayNameLike')

        if m.get('gatewayType') is not None:
            self.gateway_type = m.get('gatewayType')

        if m.get('nameLike') is not None:
            self.name_like = m.get('nameLike')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        return self

