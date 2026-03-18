# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PaidResourceDTO(DaraModel):
    def __init__(
        self,
        effective_time: str = None,
        expire_time: str = None,
        instance_id: str = None,
        quantity: int = None,
        remain_quantity: int = None,
        resource_catalog_code: str = None,
        resource_catalog_name: str = None,
        resource_package_code: str = None,
        resource_package_name: str = None,
        resource_status: str = None,
    ):
        self.effective_time = effective_time
        self.expire_time = expire_time
        self.instance_id = instance_id
        self.quantity = quantity
        self.remain_quantity = remain_quantity
        self.resource_catalog_code = resource_catalog_code
        self.resource_catalog_name = resource_catalog_name
        self.resource_package_code = resource_package_code
        self.resource_package_name = resource_package_name
        self.resource_status = resource_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.effective_time is not None:
            result['effectiveTime'] = self.effective_time

        if self.expire_time is not None:
            result['expireTime'] = self.expire_time

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.quantity is not None:
            result['quantity'] = self.quantity

        if self.remain_quantity is not None:
            result['remainQuantity'] = self.remain_quantity

        if self.resource_catalog_code is not None:
            result['resourceCatalogCode'] = self.resource_catalog_code

        if self.resource_catalog_name is not None:
            result['resourceCatalogName'] = self.resource_catalog_name

        if self.resource_package_code is not None:
            result['resourcePackageCode'] = self.resource_package_code

        if self.resource_package_name is not None:
            result['resourcePackageName'] = self.resource_package_name

        if self.resource_status is not None:
            result['resourceStatus'] = self.resource_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('effectiveTime') is not None:
            self.effective_time = m.get('effectiveTime')

        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('quantity') is not None:
            self.quantity = m.get('quantity')

        if m.get('remainQuantity') is not None:
            self.remain_quantity = m.get('remainQuantity')

        if m.get('resourceCatalogCode') is not None:
            self.resource_catalog_code = m.get('resourceCatalogCode')

        if m.get('resourceCatalogName') is not None:
            self.resource_catalog_name = m.get('resourceCatalogName')

        if m.get('resourcePackageCode') is not None:
            self.resource_package_code = m.get('resourcePackageCode')

        if m.get('resourcePackageName') is not None:
            self.resource_package_name = m.get('resourcePackageName')

        if m.get('resourceStatus') is not None:
            self.resource_status = m.get('resourceStatus')

        return self

