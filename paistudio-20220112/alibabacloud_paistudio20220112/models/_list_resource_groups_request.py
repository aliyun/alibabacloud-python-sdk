# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListResourceGroupsRequest(DaraModel):
    def __init__(
        self,
        computing_resource_provider: str = None,
        has_resource: bool = None,
        name: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_ids: str = None,
        resource_type: str = None,
        show_all: bool = None,
        sort_by: str = None,
        status: str = None,
        versions: str = None,
    ):
        self.computing_resource_provider = computing_resource_provider
        self.has_resource = has_resource
        self.name = name
        self.order = order
        self.page_number = page_number
        self.page_size = page_size
        self.resource_group_ids = resource_group_ids
        self.resource_type = resource_type
        self.show_all = show_all
        self.sort_by = sort_by
        self.status = status
        self.versions = versions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.computing_resource_provider is not None:
            result['ComputingResourceProvider'] = self.computing_resource_provider

        if self.has_resource is not None:
            result['HasResource'] = self.has_resource

        if self.name is not None:
            result['Name'] = self.name

        if self.order is not None:
            result['Order'] = self.order

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_group_ids is not None:
            result['ResourceGroupIDs'] = self.resource_group_ids

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.show_all is not None:
            result['ShowAll'] = self.show_all

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.status is not None:
            result['Status'] = self.status

        if self.versions is not None:
            result['Versions'] = self.versions

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComputingResourceProvider') is not None:
            self.computing_resource_provider = m.get('ComputingResourceProvider')

        if m.get('HasResource') is not None:
            self.has_resource = m.get('HasResource')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceGroupIDs') is not None:
            self.resource_group_ids = m.get('ResourceGroupIDs')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('ShowAll') is not None:
            self.show_all = m.get('ShowAll')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Versions') is not None:
            self.versions = m.get('Versions')

        return self

