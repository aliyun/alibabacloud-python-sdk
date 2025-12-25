# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BuyPayAsYouGoOrderRequest(DaraModel):
    def __init__(
        self,
        commodity_type: str = None,
        ins_num: int = None,
        tid: int = None,
        version_type: str = None,
    ):
        # The type of the resource that you want to purchase.
        # 
        # *   **VersionType**: DMS that supports control modes
        # *   **SensitiveDataProtection**: DMS that supports sensitive data protection
        # 
        # This parameter is required.
        self.commodity_type = commodity_type
        # The number of database instances that you want to use DMS to manage.
        # 
        # > A quota can be used for only one database instance.
        # 
        # This parameter is required.
        self.ins_num = ins_num
        # The ID of the tenant.
        # 
        # > To view the ID of the tenant, go to the Data Management (DMS) console and move the pointer over the profile picture in the upper-right corner. For more information, see [View information about the current tenant](https://help.aliyun.com/document_detail/181330.html).
        self.tid = tid
        # The control mode of DMS. Valid values:
        # 
        # *   **stand**: Stable Change
        # *   **safety**: Security Collaboration
        self.version_type = version_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.commodity_type is not None:
            result['CommodityType'] = self.commodity_type

        if self.ins_num is not None:
            result['InsNum'] = self.ins_num

        if self.tid is not None:
            result['Tid'] = self.tid

        if self.version_type is not None:
            result['VersionType'] = self.version_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityType') is not None:
            self.commodity_type = m.get('CommodityType')

        if m.get('InsNum') is not None:
            self.ins_num = m.get('InsNum')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        if m.get('VersionType') is not None:
            self.version_type = m.get('VersionType')

        return self

