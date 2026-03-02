# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListPdpServiceGroupsRequest(DaraModel):
    def __init__(
        self,
        alias: str = None,
        enterprise_id: int = None,
        env: str = None,
        env_type: str = None,
        group_type: str = None,
        ids: List[int] = None,
        name: str = None,
        order_by: str = None,
        order_direction: str = None,
        org_type: str = None,
        page_number: int = None,
        page_size: int = None,
        pbc_id: int = None,
        product_id: int = None,
        region: str = None,
        repo_id: str = None,
        service_id: int = None,
    ):
        self.alias = alias
        self.enterprise_id = enterprise_id
        # This parameter is required.
        self.env = env
        self.env_type = env_type
        self.group_type = group_type
        self.ids = ids
        self.name = name
        self.order_by = order_by
        self.order_direction = order_direction
        self.org_type = org_type
        self.page_number = page_number
        self.page_size = page_size
        # pbcId
        self.pbc_id = pbc_id
        self.product_id = product_id
        self.region = region
        self.repo_id = repo_id
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['alias'] = self.alias

        if self.enterprise_id is not None:
            result['enterpriseId'] = self.enterprise_id

        if self.env is not None:
            result['env'] = self.env

        if self.env_type is not None:
            result['envType'] = self.env_type

        if self.group_type is not None:
            result['groupType'] = self.group_type

        if self.ids is not None:
            result['ids'] = self.ids

        if self.name is not None:
            result['name'] = self.name

        if self.order_by is not None:
            result['orderBy'] = self.order_by

        if self.order_direction is not None:
            result['orderDirection'] = self.order_direction

        if self.org_type is not None:
            result['orgType'] = self.org_type

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.pbc_id is not None:
            result['pbcId'] = self.pbc_id

        if self.product_id is not None:
            result['productId'] = self.product_id

        if self.region is not None:
            result['region'] = self.region

        if self.repo_id is not None:
            result['repoId'] = self.repo_id

        if self.service_id is not None:
            result['serviceId'] = self.service_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alias') is not None:
            self.alias = m.get('alias')

        if m.get('enterpriseId') is not None:
            self.enterprise_id = m.get('enterpriseId')

        if m.get('env') is not None:
            self.env = m.get('env')

        if m.get('envType') is not None:
            self.env_type = m.get('envType')

        if m.get('groupType') is not None:
            self.group_type = m.get('groupType')

        if m.get('ids') is not None:
            self.ids = m.get('ids')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')

        if m.get('orderDirection') is not None:
            self.order_direction = m.get('orderDirection')

        if m.get('orgType') is not None:
            self.org_type = m.get('orgType')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('pbcId') is not None:
            self.pbc_id = m.get('pbcId')

        if m.get('productId') is not None:
            self.product_id = m.get('productId')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('repoId') is not None:
            self.repo_id = m.get('repoId')

        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')

        return self

