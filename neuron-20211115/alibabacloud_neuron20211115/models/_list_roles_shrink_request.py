# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListRolesShrinkRequest(DaraModel):
    def __init__(
        self,
        authorizer_id: str = None,
        authorizer_type: str = None,
        enterprise_id: int = None,
        name: str = None,
        order_by: str = None,
        order_direction: str = None,
        page_number: int = None,
        page_size: int = None,
        platform: str = None,
        role_ids_shrink: str = None,
        role_type: str = None,
    ):
        self.authorizer_id = authorizer_id
        self.authorizer_type = authorizer_type
        self.enterprise_id = enterprise_id
        self.name = name
        self.order_by = order_by
        self.order_direction = order_direction
        self.page_number = page_number
        self.page_size = page_size
        self.platform = platform
        self.role_ids_shrink = role_ids_shrink
        self.role_type = role_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorizer_id is not None:
            result['authorizerId'] = self.authorizer_id

        if self.authorizer_type is not None:
            result['authorizerType'] = self.authorizer_type

        if self.enterprise_id is not None:
            result['enterpriseId'] = self.enterprise_id

        if self.name is not None:
            result['name'] = self.name

        if self.order_by is not None:
            result['orderBy'] = self.order_by

        if self.order_direction is not None:
            result['orderDirection'] = self.order_direction

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.platform is not None:
            result['platform'] = self.platform

        if self.role_ids_shrink is not None:
            result['roleIds'] = self.role_ids_shrink

        if self.role_type is not None:
            result['roleType'] = self.role_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authorizerId') is not None:
            self.authorizer_id = m.get('authorizerId')

        if m.get('authorizerType') is not None:
            self.authorizer_type = m.get('authorizerType')

        if m.get('enterpriseId') is not None:
            self.enterprise_id = m.get('enterpriseId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')

        if m.get('orderDirection') is not None:
            self.order_direction = m.get('orderDirection')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('platform') is not None:
            self.platform = m.get('platform')

        if m.get('roleIds') is not None:
            self.role_ids_shrink = m.get('roleIds')

        if m.get('roleType') is not None:
            self.role_type = m.get('roleType')

        return self

