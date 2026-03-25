# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20230930 import models as main_models
from darabonba.model import DaraModel

class DescribeCouponRequest(DaraModel):
    def __init__(
        self,
        coupon_id: int = None,
        coupon_no: str = None,
        coupon_type: str = None,
        current_page: int = None,
        ec_id_account_ids: List[main_models.DescribeCouponRequestEcIdAccountIds] = None,
        effective_end_time: int = None,
        effective_start_time: int = None,
        expire_end_date: int = None,
        expire_start_date: int = None,
        max_results: int = None,
        nbid: str = None,
        next_token: str = None,
        page_size: int = None,
        status: str = None,
    ):
        self.coupon_id = coupon_id
        self.coupon_no = coupon_no
        self.coupon_type = coupon_type
        # This parameter is required.
        self.current_page = current_page
        self.ec_id_account_ids = ec_id_account_ids
        self.effective_end_time = effective_end_time
        self.effective_start_time = effective_start_time
        self.expire_end_date = expire_end_date
        self.expire_start_date = expire_start_date
        self.max_results = max_results
        self.nbid = nbid
        self.next_token = next_token
        # This parameter is required.
        self.page_size = page_size
        self.status = status

    def validate(self):
        if self.ec_id_account_ids:
            for v1 in self.ec_id_account_ids:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.coupon_id is not None:
            result['CouponId'] = self.coupon_id

        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no

        if self.coupon_type is not None:
            result['CouponType'] = self.coupon_type

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['EcIdAccountIds'] = []
        if self.ec_id_account_ids is not None:
            for k1 in self.ec_id_account_ids:
                result['EcIdAccountIds'].append(k1.to_map() if k1 else None)

        if self.effective_end_time is not None:
            result['EffectiveEndTime'] = self.effective_end_time

        if self.effective_start_time is not None:
            result['EffectiveStartTime'] = self.effective_start_time

        if self.expire_end_date is not None:
            result['ExpireEndDate'] = self.expire_end_date

        if self.expire_start_date is not None:
            result['ExpireStartDate'] = self.expire_start_date

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.nbid is not None:
            result['Nbid'] = self.nbid

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CouponId') is not None:
            self.coupon_id = m.get('CouponId')

        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')

        if m.get('CouponType') is not None:
            self.coupon_type = m.get('CouponType')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.ec_id_account_ids = []
        if m.get('EcIdAccountIds') is not None:
            for k1 in m.get('EcIdAccountIds'):
                temp_model = main_models.DescribeCouponRequestEcIdAccountIds()
                self.ec_id_account_ids.append(temp_model.from_map(k1))

        if m.get('EffectiveEndTime') is not None:
            self.effective_end_time = m.get('EffectiveEndTime')

        if m.get('EffectiveStartTime') is not None:
            self.effective_start_time = m.get('EffectiveStartTime')

        if m.get('ExpireEndDate') is not None:
            self.expire_end_date = m.get('ExpireEndDate')

        if m.get('ExpireStartDate') is not None:
            self.expire_start_date = m.get('ExpireStartDate')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeCouponRequestEcIdAccountIds(DaraModel):
    def __init__(
        self,
        account_ids: List[int] = None,
        ec_id: str = None,
    ):
        self.account_ids = account_ids
        # This parameter is required.
        self.ec_id = ec_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids

        if self.ec_id is not None:
            result['EcId'] = self.ec_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')

        if m.get('EcId') is not None:
            self.ec_id = m.get('EcId')

        return self

