# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteCouponDeductTagShrinkRequest(DaraModel):
    def __init__(
        self,
        coupon_id: str = None,
        ec_id_account_ids_shrink: str = None,
        nbid: str = None,
        tag_keys_shrink: str = None,
    ):
        self.coupon_id = coupon_id
        self.ec_id_account_ids_shrink = ec_id_account_ids_shrink
        self.nbid = nbid
        self.tag_keys_shrink = tag_keys_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.coupon_id is not None:
            result['CouponId'] = self.coupon_id

        if self.ec_id_account_ids_shrink is not None:
            result['EcIdAccountIds'] = self.ec_id_account_ids_shrink

        if self.nbid is not None:
            result['Nbid'] = self.nbid

        if self.tag_keys_shrink is not None:
            result['TagKeys'] = self.tag_keys_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CouponId') is not None:
            self.coupon_id = m.get('CouponId')

        if m.get('EcIdAccountIds') is not None:
            self.ec_id_account_ids_shrink = m.get('EcIdAccountIds')

        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')

        if m.get('TagKeys') is not None:
            self.tag_keys_shrink = m.get('TagKeys')

        return self

