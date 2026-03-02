# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PdpLaneInfo(DaraModel):
    def __init__(
        self,
        alias: str = None,
        company_id: int = None,
        creator_name: str = None,
        creator_uid: str = None,
        description: str = None,
        env: str = None,
        gmt_create: str = None,
        id: int = None,
        init_group_flag: bool = None,
        inlet_services: str = None,
        name: str = None,
        product_id: int = None,
        product_name: str = None,
        service_group_ids: str = None,
        type: str = None,
    ):
        self.alias = alias
        self.company_id = company_id
        self.creator_name = creator_name
        self.creator_uid = creator_uid
        self.description = description
        self.env = env
        self.gmt_create = gmt_create
        self.id = id
        self.init_group_flag = init_group_flag
        self.inlet_services = inlet_services
        self.name = name
        self.product_id = product_id
        self.product_name = product_name
        self.service_group_ids = service_group_ids
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['alias'] = self.alias

        if self.company_id is not None:
            result['companyId'] = self.company_id

        if self.creator_name is not None:
            result['creatorName'] = self.creator_name

        if self.creator_uid is not None:
            result['creatorUid'] = self.creator_uid

        if self.description is not None:
            result['description'] = self.description

        if self.env is not None:
            result['env'] = self.env

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.id is not None:
            result['id'] = self.id

        if self.init_group_flag is not None:
            result['initGroupFlag'] = self.init_group_flag

        if self.inlet_services is not None:
            result['inletServices'] = self.inlet_services

        if self.name is not None:
            result['name'] = self.name

        if self.product_id is not None:
            result['productId'] = self.product_id

        if self.product_name is not None:
            result['productName'] = self.product_name

        if self.service_group_ids is not None:
            result['serviceGroupIds'] = self.service_group_ids

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alias') is not None:
            self.alias = m.get('alias')

        if m.get('companyId') is not None:
            self.company_id = m.get('companyId')

        if m.get('creatorName') is not None:
            self.creator_name = m.get('creatorName')

        if m.get('creatorUid') is not None:
            self.creator_uid = m.get('creatorUid')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('env') is not None:
            self.env = m.get('env')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('initGroupFlag') is not None:
            self.init_group_flag = m.get('initGroupFlag')

        if m.get('inletServices') is not None:
            self.inlet_services = m.get('inletServices')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('productId') is not None:
            self.product_id = m.get('productId')

        if m.get('productName') is not None:
            self.product_name = m.get('productName')

        if m.get('serviceGroupIds') is not None:
            self.service_group_ids = m.get('serviceGroupIds')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

