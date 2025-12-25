# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListMcpServersRequest(DaraModel):
    def __init__(
        self,
        create_from_types: str = None,
        deploy_statuses: str = None,
        gateway_id: str = None,
        name_like: str = None,
        page_number: int = None,
        page_size: int = None,
        type: str = None,
    ):
        # The type of source to create from.
        self.create_from_types = create_from_types
        # The deployment status of the MCP server.
        self.deploy_statuses = deploy_statuses
        # The gateway instance ID.
        # 
        # This parameter is required.
        self.gateway_id = gateway_id
        # The name to perform a fuzzy search on the MCP server.
        self.name_like = name_like
        # The page number to return. Pages start from 1. Default value: 1.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries per page. Default value: 10.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The type of the MCP server.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_from_types is not None:
            result['createFromTypes'] = self.create_from_types

        if self.deploy_statuses is not None:
            result['deployStatuses'] = self.deploy_statuses

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.name_like is not None:
            result['nameLike'] = self.name_like

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createFromTypes') is not None:
            self.create_from_types = m.get('createFromTypes')

        if m.get('deployStatuses') is not None:
            self.deploy_statuses = m.get('deployStatuses')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('nameLike') is not None:
            self.name_like = m.get('nameLike')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

