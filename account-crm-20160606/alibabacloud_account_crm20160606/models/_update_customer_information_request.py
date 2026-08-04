# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateCustomerInformationRequest(DaraModel):
    def __init__(
        self,
        biz: str = None,
        customer_category: str = None,
        customer_sub_category: str = None,
        user_id: int = None,
        website: str = None,
    ):
        self.biz = biz
        self.customer_category = customer_category
        self.customer_sub_category = customer_sub_category
        # This parameter is required.
        self.user_id = user_id
        self.website = website

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz is not None:
            result['Biz'] = self.biz

        if self.customer_category is not None:
            result['CustomerCategory'] = self.customer_category

        if self.customer_sub_category is not None:
            result['CustomerSubCategory'] = self.customer_sub_category

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.website is not None:
            result['Website'] = self.website

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Biz') is not None:
            self.biz = m.get('Biz')

        if m.get('CustomerCategory') is not None:
            self.customer_category = m.get('CustomerCategory')

        if m.get('CustomerSubCategory') is not None:
            self.customer_sub_category = m.get('CustomerSubCategory')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('Website') is not None:
            self.website = m.get('Website')

        return self

