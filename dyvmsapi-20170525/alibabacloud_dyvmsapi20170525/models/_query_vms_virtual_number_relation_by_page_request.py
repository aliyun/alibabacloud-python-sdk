# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryVmsVirtualNumberRelationByPageRequest(DaraModel):
    def __init__(
        self,
        number_city: str = None,
        number_province: str = None,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        real_number: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        state: int = None,
        virtual_number: str = None,
    ):
        # 号码归属地--城市
        self.number_city = number_city
        # 号码归属地--省
        self.number_province = number_province
        self.owner_id = owner_id
        self.page_no = page_no
        self.page_size = page_size
        # 真实号码
        self.real_number = real_number
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # 状态 1:有效；0:无效；-1:注销
        self.state = state
        # 虚拟号码
        self.virtual_number = virtual_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.number_city is not None:
            result['NumberCity'] = self.number_city

        if self.number_province is not None:
            result['NumberProvince'] = self.number_province

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.real_number is not None:
            result['RealNumber'] = self.real_number

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.state is not None:
            result['State'] = self.state

        if self.virtual_number is not None:
            result['VirtualNumber'] = self.virtual_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NumberCity') is not None:
            self.number_city = m.get('NumberCity')

        if m.get('NumberProvince') is not None:
            self.number_province = m.get('NumberProvince')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RealNumber') is not None:
            self.real_number = m.get('RealNumber')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('VirtualNumber') is not None:
            self.virtual_number = m.get('VirtualNumber')

        return self

