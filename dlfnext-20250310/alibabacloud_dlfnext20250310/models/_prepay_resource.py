# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PrepayResource(DaraModel):
    def __init__(
        self,
        catalog_id: str = None,
        catalog_name: str = None,
        cu: int = None,
        expire_time: int = None,
        gmt_create: int = None,
        instance_id: str = None,
        instance_status: str = None,
    ):
        self.catalog_id = catalog_id
        self.catalog_name = catalog_name
        self.cu = cu
        self.expire_time = expire_time
        self.gmt_create = gmt_create
        self.instance_id = instance_id
        self.instance_status = instance_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog_id is not None:
            result['catalogId'] = self.catalog_id

        if self.catalog_name is not None:
            result['catalogName'] = self.catalog_name

        if self.cu is not None:
            result['cu'] = self.cu

        if self.expire_time is not None:
            result['expireTime'] = self.expire_time

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.instance_status is not None:
            result['instanceStatus'] = self.instance_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('catalogId') is not None:
            self.catalog_id = m.get('catalogId')

        if m.get('catalogName') is not None:
            self.catalog_name = m.get('catalogName')

        if m.get('cu') is not None:
            self.cu = m.get('cu')

        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('instanceStatus') is not None:
            self.instance_status = m.get('instanceStatus')

        return self

