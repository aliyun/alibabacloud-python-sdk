# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20230930 import models as main_models
from darabonba.model import DaraModel

class DescribeCouponResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        data: List[main_models.DescribeCouponResponseBodyData] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.data = data
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeCouponResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeCouponResponseBodyData(DaraModel):
    def __init__(
        self,
        amount: str = None,
        certain_amount: str = None,
        coupon_id: int = None,
        coupon_no: str = None,
        coupon_type: str = None,
        coupon_type_name: str = None,
        currency: str = None,
        end_time: str = None,
        first_buy: bool = None,
        gmt_create: str = None,
        item_names: List[str] = None,
        money_limit: str = None,
        order_time_rule: str = None,
        remain_amount: str = None,
        remark: str = None,
        share_uid_list: List[main_models.DescribeCouponResponseBodyDataShareUidList] = None,
        show_set_deduct_tag_button: bool = None,
        site: str = None,
        site_name: str = None,
        start_time: str = None,
        status: str = None,
        suit_account: str = None,
        suit_item_type: str = None,
        universal_type: str = None,
        yh_order_types: List[str] = None,
    ):
        self.amount = amount
        self.certain_amount = certain_amount
        self.coupon_id = coupon_id
        self.coupon_no = coupon_no
        self.coupon_type = coupon_type
        self.coupon_type_name = coupon_type_name
        self.currency = currency
        self.end_time = end_time
        self.first_buy = first_buy
        self.gmt_create = gmt_create
        self.item_names = item_names
        self.money_limit = money_limit
        self.order_time_rule = order_time_rule
        self.remain_amount = remain_amount
        self.remark = remark
        self.share_uid_list = share_uid_list
        self.show_set_deduct_tag_button = show_set_deduct_tag_button
        self.site = site
        self.site_name = site_name
        self.start_time = start_time
        self.status = status
        self.suit_account = suit_account
        self.suit_item_type = suit_item_type
        self.universal_type = universal_type
        self.yh_order_types = yh_order_types

    def validate(self):
        if self.share_uid_list:
            for v1 in self.share_uid_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.certain_amount is not None:
            result['CertainAmount'] = self.certain_amount

        if self.coupon_id is not None:
            result['CouponId'] = self.coupon_id

        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no

        if self.coupon_type is not None:
            result['CouponType'] = self.coupon_type

        if self.coupon_type_name is not None:
            result['CouponTypeName'] = self.coupon_type_name

        if self.currency is not None:
            result['Currency'] = self.currency

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.first_buy is not None:
            result['FirstBuy'] = self.first_buy

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.item_names is not None:
            result['ItemNames'] = self.item_names

        if self.money_limit is not None:
            result['MoneyLimit'] = self.money_limit

        if self.order_time_rule is not None:
            result['OrderTimeRule'] = self.order_time_rule

        if self.remain_amount is not None:
            result['RemainAmount'] = self.remain_amount

        if self.remark is not None:
            result['Remark'] = self.remark

        result['ShareUidList'] = []
        if self.share_uid_list is not None:
            for k1 in self.share_uid_list:
                result['ShareUidList'].append(k1.to_map() if k1 else None)

        if self.show_set_deduct_tag_button is not None:
            result['ShowSetDeductTagButton'] = self.show_set_deduct_tag_button

        if self.site is not None:
            result['Site'] = self.site

        if self.site_name is not None:
            result['SiteName'] = self.site_name

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.suit_account is not None:
            result['SuitAccount'] = self.suit_account

        if self.suit_item_type is not None:
            result['SuitItemType'] = self.suit_item_type

        if self.universal_type is not None:
            result['UniversalType'] = self.universal_type

        if self.yh_order_types is not None:
            result['YhOrderTypes'] = self.yh_order_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('CertainAmount') is not None:
            self.certain_amount = m.get('CertainAmount')

        if m.get('CouponId') is not None:
            self.coupon_id = m.get('CouponId')

        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')

        if m.get('CouponType') is not None:
            self.coupon_type = m.get('CouponType')

        if m.get('CouponTypeName') is not None:
            self.coupon_type_name = m.get('CouponTypeName')

        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('FirstBuy') is not None:
            self.first_buy = m.get('FirstBuy')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('ItemNames') is not None:
            self.item_names = m.get('ItemNames')

        if m.get('MoneyLimit') is not None:
            self.money_limit = m.get('MoneyLimit')

        if m.get('OrderTimeRule') is not None:
            self.order_time_rule = m.get('OrderTimeRule')

        if m.get('RemainAmount') is not None:
            self.remain_amount = m.get('RemainAmount')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        self.share_uid_list = []
        if m.get('ShareUidList') is not None:
            for k1 in m.get('ShareUidList'):
                temp_model = main_models.DescribeCouponResponseBodyDataShareUidList()
                self.share_uid_list.append(temp_model.from_map(k1))

        if m.get('ShowSetDeductTagButton') is not None:
            self.show_set_deduct_tag_button = m.get('ShowSetDeductTagButton')

        if m.get('Site') is not None:
            self.site = m.get('Site')

        if m.get('SiteName') is not None:
            self.site_name = m.get('SiteName')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SuitAccount') is not None:
            self.suit_account = m.get('SuitAccount')

        if m.get('SuitItemType') is not None:
            self.suit_item_type = m.get('SuitItemType')

        if m.get('UniversalType') is not None:
            self.universal_type = m.get('UniversalType')

        if m.get('YhOrderTypes') is not None:
            self.yh_order_types = m.get('YhOrderTypes')

        return self

class DescribeCouponResponseBodyDataShareUidList(DaraModel):
    def __init__(
        self,
        uid: str = None,
        user_nick: str = None,
    ):
        self.uid = uid
        self.user_nick = user_nick

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.uid is not None:
            result['Uid'] = self.uid

        if self.user_nick is not None:
            result['UserNick'] = self.user_nick

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        if m.get('UserNick') is not None:
            self.user_nick = m.get('UserNick')

        return self

