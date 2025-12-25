# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryConsumerAuthorizationRulesRequest(DaraModel):
    def __init__(
        self,
        api_name_like: str = None,
        consumer_id: str = None,
        consumer_name_like: str = None,
        environment_id: str = None,
        group_by_api: bool = None,
        page_number: int = None,
        page_size: int = None,
        parent_resource_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
        resource_types: str = None,
    ):
        # The API name.
        self.api_name_like = api_name_like
        # The consumer ID.
        self.consumer_id = consumer_id
        # The consumer name.
        self.consumer_name_like = consumer_name_like
        # The environment ID.
        self.environment_id = environment_id
        # Specifies whether to group the results by API.
        self.group_by_api = group_by_api
        # The number of the page to return.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The parent resource ID.
        self.parent_resource_id = parent_resource_id
        # The resource ID.
        self.resource_id = resource_id
        # The resource type.
        self.resource_type = resource_type
        self.resource_types = resource_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_name_like is not None:
            result['apiNameLike'] = self.api_name_like

        if self.consumer_id is not None:
            result['consumerId'] = self.consumer_id

        if self.consumer_name_like is not None:
            result['consumerNameLike'] = self.consumer_name_like

        if self.environment_id is not None:
            result['environmentId'] = self.environment_id

        if self.group_by_api is not None:
            result['groupByApi'] = self.group_by_api

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.parent_resource_id is not None:
            result['parentResourceId'] = self.parent_resource_id

        if self.resource_id is not None:
            result['resourceId'] = self.resource_id

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        if self.resource_types is not None:
            result['resourceTypes'] = self.resource_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiNameLike') is not None:
            self.api_name_like = m.get('apiNameLike')

        if m.get('consumerId') is not None:
            self.consumer_id = m.get('consumerId')

        if m.get('consumerNameLike') is not None:
            self.consumer_name_like = m.get('consumerNameLike')

        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')

        if m.get('groupByApi') is not None:
            self.group_by_api = m.get('groupByApi')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('parentResourceId') is not None:
            self.parent_resource_id = m.get('parentResourceId')

        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        if m.get('resourceTypes') is not None:
            self.resource_types = m.get('resourceTypes')

        return self

