# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCouponUsageRequest(DaraModel):
    def __init__(
        self,
        account: str = None,
        coupon_template_id: int = None,
        page: int = None,
        page_size: int = None,
        status: str = None,
        t_2partner_uid: int = None,
        uid: int = None,
    ):
        self.account = account
        self.coupon_template_id = coupon_template_id
        self.page = page
        self.page_size = page_size
        self.status = status
        self.t_2partner_uid = t_2partner_uid
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account is not None:
            result['Account'] = self.account

        if self.coupon_template_id is not None:
            result['CouponTemplateId'] = self.coupon_template_id

        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.status is not None:
            result['Status'] = self.status

        if self.t_2partner_uid is not None:
            result['T2PartnerUid'] = self.t_2partner_uid

        if self.uid is not None:
            result['Uid'] = self.uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')

        if m.get('CouponTemplateId') is not None:
            self.coupon_template_id = m.get('CouponTemplateId')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('T2PartnerUid') is not None:
            self.t_2partner_uid = m.get('T2PartnerUid')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        return self

