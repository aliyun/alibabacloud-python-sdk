# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCouponItemListShrinkRequest(DaraModel):
    def __init__(
        self,
        coupon_id: int = None,
        current_page: int = None,
        ec_id_account_ids_shrink: str = None,
        name: str = None,
        nbid: str = None,
        page_size: int = None,
    ):
        self.coupon_id = coupon_id
        self.current_page = current_page
        self.ec_id_account_ids_shrink = ec_id_account_ids_shrink
        self.name = name
        self.nbid = nbid
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.coupon_id is not None:
            result['CouponId'] = self.coupon_id

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.ec_id_account_ids_shrink is not None:
            result['EcIdAccountIds'] = self.ec_id_account_ids_shrink

        if self.name is not None:
            result['Name'] = self.name

        if self.nbid is not None:
            result['Nbid'] = self.nbid

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CouponId') is not None:
            self.coupon_id = m.get('CouponId')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EcIdAccountIds') is not None:
            self.ec_id_account_ids_shrink = m.get('EcIdAccountIds')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

