# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class NeuronApp(DaraModel):
    def __init__(
        self,
        access_type: str = None,
        account_id: str = None,
        alias: str = None,
        biz_type: str = None,
        description: str = None,
        enterprise_id: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        icon_url: str = None,
        id: int = None,
        name: str = None,
        owner: str = None,
        product_id: int = None,
        status: str = None,
    ):
        # This parameter is required.
        self.access_type = access_type
        self.account_id = account_id
        # This parameter is required.
        self.alias = alias
        # This parameter is required.
        self.biz_type = biz_type
        # This parameter is required.
        self.description = description
        # This parameter is required.
        self.enterprise_id = enterprise_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        # This parameter is required.
        self.icon_url = icon_url
        self.id = id
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.owner = owner
        # This parameter is required.
        self.product_id = product_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_type is not None:
            result['accessType'] = self.access_type

        if self.account_id is not None:
            result['accountId'] = self.account_id

        if self.alias is not None:
            result['alias'] = self.alias

        if self.biz_type is not None:
            result['bizType'] = self.biz_type

        if self.description is not None:
            result['description'] = self.description

        if self.enterprise_id is not None:
            result['enterpriseId'] = self.enterprise_id

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.icon_url is not None:
            result['iconUrl'] = self.icon_url

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.owner is not None:
            result['owner'] = self.owner

        if self.product_id is not None:
            result['productId'] = self.product_id

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessType') is not None:
            self.access_type = m.get('accessType')

        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')

        if m.get('alias') is not None:
            self.alias = m.get('alias')

        if m.get('bizType') is not None:
            self.biz_type = m.get('bizType')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('enterpriseId') is not None:
            self.enterprise_id = m.get('enterpriseId')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('iconUrl') is not None:
            self.icon_url = m.get('iconUrl')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('owner') is not None:
            self.owner = m.get('owner')

        if m.get('productId') is not None:
            self.product_id = m.get('productId')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

