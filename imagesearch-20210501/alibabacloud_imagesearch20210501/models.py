# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, BinaryIO


class GetProductInfoByIdsRequest(TeaModel):
    def __init__(
        self,
        fields: str = None,
        item_ids: str = None,
        pid: str = None,
    ):
        self.fields = fields
        self.item_ids = item_ids
        self.pid = pid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fields is not None:
            result['Fields'] = self.fields
        if self.item_ids is not None:
            result['ItemIds'] = self.item_ids
        if self.pid is not None:
            result['Pid'] = self.pid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Fields') is not None:
            self.fields = m.get('Fields')
        if m.get('ItemIds') is not None:
            self.item_ids = m.get('ItemIds')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        return self


class GetProductInfoByIdsResponseBodyDataAuctionsResultMaxCommission(TeaModel):
    def __init__(
        self,
        max_commission_click_url: str = None,
        max_commission_coupon_share_url: str = None,
        max_commission_rate: str = None,
    ):
        self.max_commission_click_url = max_commission_click_url
        self.max_commission_coupon_share_url = max_commission_coupon_share_url
        self.max_commission_rate = max_commission_rate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_commission_click_url is not None:
            result['MaxCommissionClickUrl'] = self.max_commission_click_url
        if self.max_commission_coupon_share_url is not None:
            result['MaxCommissionCouponShareUrl'] = self.max_commission_coupon_share_url
        if self.max_commission_rate is not None:
            result['MaxCommissionRate'] = self.max_commission_rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxCommissionClickUrl') is not None:
            self.max_commission_click_url = m.get('MaxCommissionClickUrl')
        if m.get('MaxCommissionCouponShareUrl') is not None:
            self.max_commission_coupon_share_url = m.get('MaxCommissionCouponShareUrl')
        if m.get('MaxCommissionRate') is not None:
            self.max_commission_rate = m.get('MaxCommissionRate')
        return self


class GetProductInfoByIdsResponseBodyDataAuctionsResult(TeaModel):
    def __init__(
        self,
        category_name: str = None,
        commission_rate: str = None,
        coupon_amount: int = None,
        coupon_end_time: str = None,
        coupon_info: str = None,
        coupon_remain_count: int = None,
        coupon_share_url: str = None,
        coupon_start_fee: str = None,
        coupon_start_time: str = None,
        coupon_total_count: str = None,
        deeplink_coupon_share_url: str = None,
        deeplink_url: str = None,
        input_item_id: str = None,
        item_id: str = None,
        level_one_category_name: str = None,
        max_commission: GetProductInfoByIdsResponseBodyDataAuctionsResultMaxCommission = None,
        nick: str = None,
        pic_url: str = None,
        price_after_coupon: str = None,
        provcity: str = None,
        reserve_price: str = None,
        seller_id: str = None,
        shop_title: str = None,
        short_title: str = None,
        sub_title: str = None,
        title: str = None,
        url: str = None,
        user_type: int = None,
        volume: int = None,
        zk_final_price: str = None,
    ):
        self.category_name = category_name
        self.commission_rate = commission_rate
        self.coupon_amount = coupon_amount
        self.coupon_end_time = coupon_end_time
        self.coupon_info = coupon_info
        self.coupon_remain_count = coupon_remain_count
        self.coupon_share_url = coupon_share_url
        self.coupon_start_fee = coupon_start_fee
        self.coupon_start_time = coupon_start_time
        self.coupon_total_count = coupon_total_count
        self.deeplink_coupon_share_url = deeplink_coupon_share_url
        self.deeplink_url = deeplink_url
        self.input_item_id = input_item_id
        self.item_id = item_id
        self.level_one_category_name = level_one_category_name
        self.max_commission = max_commission
        self.nick = nick
        self.pic_url = pic_url
        self.price_after_coupon = price_after_coupon
        self.provcity = provcity
        self.reserve_price = reserve_price
        self.seller_id = seller_id
        self.shop_title = shop_title
        self.short_title = short_title
        self.sub_title = sub_title
        self.title = title
        self.url = url
        self.user_type = user_type
        self.volume = volume
        self.zk_final_price = zk_final_price

    def validate(self):
        if self.max_commission:
            self.max_commission.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.commission_rate is not None:
            result['CommissionRate'] = self.commission_rate
        if self.coupon_amount is not None:
            result['CouponAmount'] = self.coupon_amount
        if self.coupon_end_time is not None:
            result['CouponEndTime'] = self.coupon_end_time
        if self.coupon_info is not None:
            result['CouponInfo'] = self.coupon_info
        if self.coupon_remain_count is not None:
            result['CouponRemainCount'] = self.coupon_remain_count
        if self.coupon_share_url is not None:
            result['CouponShareUrl'] = self.coupon_share_url
        if self.coupon_start_fee is not None:
            result['CouponStartFee'] = self.coupon_start_fee
        if self.coupon_start_time is not None:
            result['CouponStartTime'] = self.coupon_start_time
        if self.coupon_total_count is not None:
            result['CouponTotalCount'] = self.coupon_total_count
        if self.deeplink_coupon_share_url is not None:
            result['DeeplinkCouponShareUrl'] = self.deeplink_coupon_share_url
        if self.deeplink_url is not None:
            result['DeeplinkUrl'] = self.deeplink_url
        if self.input_item_id is not None:
            result['InputItemId'] = self.input_item_id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.level_one_category_name is not None:
            result['LevelOneCategoryName'] = self.level_one_category_name
        if self.max_commission is not None:
            result['MaxCommission'] = self.max_commission.to_map()
        if self.nick is not None:
            result['Nick'] = self.nick
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        if self.price_after_coupon is not None:
            result['PriceAfterCoupon'] = self.price_after_coupon
        if self.provcity is not None:
            result['Provcity'] = self.provcity
        if self.reserve_price is not None:
            result['ReservePrice'] = self.reserve_price
        if self.seller_id is not None:
            result['SellerId'] = self.seller_id
        if self.shop_title is not None:
            result['ShopTitle'] = self.shop_title
        if self.short_title is not None:
            result['ShortTitle'] = self.short_title
        if self.sub_title is not None:
            result['SubTitle'] = self.sub_title
        if self.title is not None:
            result['Title'] = self.title
        if self.url is not None:
            result['Url'] = self.url
        if self.user_type is not None:
            result['UserType'] = self.user_type
        if self.volume is not None:
            result['Volume'] = self.volume
        if self.zk_final_price is not None:
            result['ZkFinalPrice'] = self.zk_final_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('CommissionRate') is not None:
            self.commission_rate = m.get('CommissionRate')
        if m.get('CouponAmount') is not None:
            self.coupon_amount = m.get('CouponAmount')
        if m.get('CouponEndTime') is not None:
            self.coupon_end_time = m.get('CouponEndTime')
        if m.get('CouponInfo') is not None:
            self.coupon_info = m.get('CouponInfo')
        if m.get('CouponRemainCount') is not None:
            self.coupon_remain_count = m.get('CouponRemainCount')
        if m.get('CouponShareUrl') is not None:
            self.coupon_share_url = m.get('CouponShareUrl')
        if m.get('CouponStartFee') is not None:
            self.coupon_start_fee = m.get('CouponStartFee')
        if m.get('CouponStartTime') is not None:
            self.coupon_start_time = m.get('CouponStartTime')
        if m.get('CouponTotalCount') is not None:
            self.coupon_total_count = m.get('CouponTotalCount')
        if m.get('DeeplinkCouponShareUrl') is not None:
            self.deeplink_coupon_share_url = m.get('DeeplinkCouponShareUrl')
        if m.get('DeeplinkUrl') is not None:
            self.deeplink_url = m.get('DeeplinkUrl')
        if m.get('InputItemId') is not None:
            self.input_item_id = m.get('InputItemId')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('LevelOneCategoryName') is not None:
            self.level_one_category_name = m.get('LevelOneCategoryName')
        if m.get('MaxCommission') is not None:
            temp_model = GetProductInfoByIdsResponseBodyDataAuctionsResultMaxCommission()
            self.max_commission = temp_model.from_map(m['MaxCommission'])
        if m.get('Nick') is not None:
            self.nick = m.get('Nick')
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        if m.get('PriceAfterCoupon') is not None:
            self.price_after_coupon = m.get('PriceAfterCoupon')
        if m.get('Provcity') is not None:
            self.provcity = m.get('Provcity')
        if m.get('ReservePrice') is not None:
            self.reserve_price = m.get('ReservePrice')
        if m.get('SellerId') is not None:
            self.seller_id = m.get('SellerId')
        if m.get('ShopTitle') is not None:
            self.shop_title = m.get('ShopTitle')
        if m.get('ShortTitle') is not None:
            self.short_title = m.get('ShortTitle')
        if m.get('SubTitle') is not None:
            self.sub_title = m.get('SubTitle')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        if m.get('ZkFinalPrice') is not None:
            self.zk_final_price = m.get('ZkFinalPrice')
        return self


class GetProductInfoByIdsResponseBodyDataAuctions(TeaModel):
    def __init__(
        self,
        rank_score: float = None,
        result: GetProductInfoByIdsResponseBodyDataAuctionsResult = None,
    ):
        self.rank_score = rank_score
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rank_score is not None:
            result['RankScore'] = self.rank_score
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RankScore') is not None:
            self.rank_score = m.get('RankScore')
        if m.get('Result') is not None:
            temp_model = GetProductInfoByIdsResponseBodyDataAuctionsResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetProductInfoByIdsResponseBodyData(TeaModel):
    def __init__(
        self,
        auctions: List[GetProductInfoByIdsResponseBodyDataAuctions] = None,
    ):
        self.auctions = auctions

    def validate(self):
        if self.auctions:
            for k in self.auctions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Auctions'] = []
        if self.auctions is not None:
            for k in self.auctions:
                result['Auctions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.auctions = []
        if m.get('Auctions') is not None:
            for k in m.get('Auctions'):
                temp_model = GetProductInfoByIdsResponseBodyDataAuctions()
                self.auctions.append(temp_model.from_map(k))
        return self


class GetProductInfoByIdsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetProductInfoByIdsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetProductInfoByIdsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetProductInfoByIdsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetProductInfoByIdsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetProductInfoByIdsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchByPicRequest(TeaModel):
    def __init__(
        self,
        category_id: int = None,
        crop: bool = None,
        fields: str = None,
        num: int = None,
        pic_content: str = None,
        pid: str = None,
        region: str = None,
        relation_id: int = None,
        start: int = None,
        user_type: int = None,
    ):
        self.category_id = category_id
        self.crop = crop
        self.fields = fields
        self.num = num
        self.pic_content = pic_content
        self.pid = pid
        self.region = region
        self.relation_id = relation_id
        self.start = start
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.crop is not None:
            result['Crop'] = self.crop
        if self.fields is not None:
            result['Fields'] = self.fields
        if self.num is not None:
            result['Num'] = self.num
        if self.pic_content is not None:
            result['PicContent'] = self.pic_content
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.region is not None:
            result['Region'] = self.region
        if self.relation_id is not None:
            result['RelationId'] = self.relation_id
        if self.start is not None:
            result['Start'] = self.start
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Crop') is not None:
            self.crop = m.get('Crop')
        if m.get('Fields') is not None:
            self.fields = m.get('Fields')
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('PicContent') is not None:
            self.pic_content = m.get('PicContent')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RelationId') is not None:
            self.relation_id = m.get('RelationId')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class SearchByPicAdvanceRequest(TeaModel):
    def __init__(
        self,
        category_id: int = None,
        crop: bool = None,
        fields: str = None,
        num: int = None,
        pic_content_object: BinaryIO = None,
        pid: str = None,
        region: str = None,
        relation_id: int = None,
        start: int = None,
        user_type: int = None,
    ):
        self.category_id = category_id
        self.crop = crop
        self.fields = fields
        self.num = num
        self.pic_content_object = pic_content_object
        self.pid = pid
        self.region = region
        self.relation_id = relation_id
        self.start = start
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.crop is not None:
            result['Crop'] = self.crop
        if self.fields is not None:
            result['Fields'] = self.fields
        if self.num is not None:
            result['Num'] = self.num
        if self.pic_content_object is not None:
            result['PicContent'] = self.pic_content_object
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.region is not None:
            result['Region'] = self.region
        if self.relation_id is not None:
            result['RelationId'] = self.relation_id
        if self.start is not None:
            result['Start'] = self.start
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Crop') is not None:
            self.crop = m.get('Crop')
        if m.get('Fields') is not None:
            self.fields = m.get('Fields')
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('PicContent') is not None:
            self.pic_content_object = m.get('PicContent')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RelationId') is not None:
            self.relation_id = m.get('RelationId')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class SearchByPicResponseBodyDataAuctionsResultMaxCommission(TeaModel):
    def __init__(
        self,
        max_commission_click_url: str = None,
        max_commission_coupon_share_url: str = None,
        max_commission_rate: str = None,
    ):
        self.max_commission_click_url = max_commission_click_url
        self.max_commission_coupon_share_url = max_commission_coupon_share_url
        self.max_commission_rate = max_commission_rate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_commission_click_url is not None:
            result['MaxCommissionClickUrl'] = self.max_commission_click_url
        if self.max_commission_coupon_share_url is not None:
            result['MaxCommissionCouponShareUrl'] = self.max_commission_coupon_share_url
        if self.max_commission_rate is not None:
            result['MaxCommissionRate'] = self.max_commission_rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxCommissionClickUrl') is not None:
            self.max_commission_click_url = m.get('MaxCommissionClickUrl')
        if m.get('MaxCommissionCouponShareUrl') is not None:
            self.max_commission_coupon_share_url = m.get('MaxCommissionCouponShareUrl')
        if m.get('MaxCommissionRate') is not None:
            self.max_commission_rate = m.get('MaxCommissionRate')
        return self


class SearchByPicResponseBodyDataAuctionsResult(TeaModel):
    def __init__(
        self,
        category_name: str = None,
        commission_rate: str = None,
        coupon_amount: int = None,
        coupon_end_time: str = None,
        coupon_info: str = None,
        coupon_remain_count: int = None,
        coupon_share_url: str = None,
        coupon_start_fee: str = None,
        coupon_start_time: str = None,
        coupon_total_count: str = None,
        deeplink_coupon_share_url: str = None,
        deeplink_url: str = None,
        item_id: str = None,
        level_one_category_name: str = None,
        max_commission: SearchByPicResponseBodyDataAuctionsResultMaxCommission = None,
        nick: str = None,
        pic_url: str = None,
        price_after_coupon: str = None,
        provcity: str = None,
        reserve_price: str = None,
        seller_id: str = None,
        shop_title: str = None,
        short_title: str = None,
        sub_title: str = None,
        title: str = None,
        url: str = None,
        user_type: int = None,
        volume: int = None,
        zk_final_price: str = None,
    ):
        self.category_name = category_name
        self.commission_rate = commission_rate
        self.coupon_amount = coupon_amount
        self.coupon_end_time = coupon_end_time
        self.coupon_info = coupon_info
        self.coupon_remain_count = coupon_remain_count
        self.coupon_share_url = coupon_share_url
        self.coupon_start_fee = coupon_start_fee
        self.coupon_start_time = coupon_start_time
        self.coupon_total_count = coupon_total_count
        self.deeplink_coupon_share_url = deeplink_coupon_share_url
        self.deeplink_url = deeplink_url
        self.item_id = item_id
        self.level_one_category_name = level_one_category_name
        self.max_commission = max_commission
        self.nick = nick
        self.pic_url = pic_url
        self.price_after_coupon = price_after_coupon
        self.provcity = provcity
        self.reserve_price = reserve_price
        self.seller_id = seller_id
        self.shop_title = shop_title
        self.short_title = short_title
        self.sub_title = sub_title
        self.title = title
        self.url = url
        self.user_type = user_type
        self.volume = volume
        self.zk_final_price = zk_final_price

    def validate(self):
        if self.max_commission:
            self.max_commission.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.commission_rate is not None:
            result['CommissionRate'] = self.commission_rate
        if self.coupon_amount is not None:
            result['CouponAmount'] = self.coupon_amount
        if self.coupon_end_time is not None:
            result['CouponEndTime'] = self.coupon_end_time
        if self.coupon_info is not None:
            result['CouponInfo'] = self.coupon_info
        if self.coupon_remain_count is not None:
            result['CouponRemainCount'] = self.coupon_remain_count
        if self.coupon_share_url is not None:
            result['CouponShareUrl'] = self.coupon_share_url
        if self.coupon_start_fee is not None:
            result['CouponStartFee'] = self.coupon_start_fee
        if self.coupon_start_time is not None:
            result['CouponStartTime'] = self.coupon_start_time
        if self.coupon_total_count is not None:
            result['CouponTotalCount'] = self.coupon_total_count
        if self.deeplink_coupon_share_url is not None:
            result['DeeplinkCouponShareUrl'] = self.deeplink_coupon_share_url
        if self.deeplink_url is not None:
            result['DeeplinkUrl'] = self.deeplink_url
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.level_one_category_name is not None:
            result['LevelOneCategoryName'] = self.level_one_category_name
        if self.max_commission is not None:
            result['MaxCommission'] = self.max_commission.to_map()
        if self.nick is not None:
            result['Nick'] = self.nick
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        if self.price_after_coupon is not None:
            result['PriceAfterCoupon'] = self.price_after_coupon
        if self.provcity is not None:
            result['Provcity'] = self.provcity
        if self.reserve_price is not None:
            result['ReservePrice'] = self.reserve_price
        if self.seller_id is not None:
            result['SellerId'] = self.seller_id
        if self.shop_title is not None:
            result['ShopTitle'] = self.shop_title
        if self.short_title is not None:
            result['ShortTitle'] = self.short_title
        if self.sub_title is not None:
            result['SubTitle'] = self.sub_title
        if self.title is not None:
            result['Title'] = self.title
        if self.url is not None:
            result['Url'] = self.url
        if self.user_type is not None:
            result['UserType'] = self.user_type
        if self.volume is not None:
            result['Volume'] = self.volume
        if self.zk_final_price is not None:
            result['ZkFinalPrice'] = self.zk_final_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('CommissionRate') is not None:
            self.commission_rate = m.get('CommissionRate')
        if m.get('CouponAmount') is not None:
            self.coupon_amount = m.get('CouponAmount')
        if m.get('CouponEndTime') is not None:
            self.coupon_end_time = m.get('CouponEndTime')
        if m.get('CouponInfo') is not None:
            self.coupon_info = m.get('CouponInfo')
        if m.get('CouponRemainCount') is not None:
            self.coupon_remain_count = m.get('CouponRemainCount')
        if m.get('CouponShareUrl') is not None:
            self.coupon_share_url = m.get('CouponShareUrl')
        if m.get('CouponStartFee') is not None:
            self.coupon_start_fee = m.get('CouponStartFee')
        if m.get('CouponStartTime') is not None:
            self.coupon_start_time = m.get('CouponStartTime')
        if m.get('CouponTotalCount') is not None:
            self.coupon_total_count = m.get('CouponTotalCount')
        if m.get('DeeplinkCouponShareUrl') is not None:
            self.deeplink_coupon_share_url = m.get('DeeplinkCouponShareUrl')
        if m.get('DeeplinkUrl') is not None:
            self.deeplink_url = m.get('DeeplinkUrl')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('LevelOneCategoryName') is not None:
            self.level_one_category_name = m.get('LevelOneCategoryName')
        if m.get('MaxCommission') is not None:
            temp_model = SearchByPicResponseBodyDataAuctionsResultMaxCommission()
            self.max_commission = temp_model.from_map(m['MaxCommission'])
        if m.get('Nick') is not None:
            self.nick = m.get('Nick')
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        if m.get('PriceAfterCoupon') is not None:
            self.price_after_coupon = m.get('PriceAfterCoupon')
        if m.get('Provcity') is not None:
            self.provcity = m.get('Provcity')
        if m.get('ReservePrice') is not None:
            self.reserve_price = m.get('ReservePrice')
        if m.get('SellerId') is not None:
            self.seller_id = m.get('SellerId')
        if m.get('ShopTitle') is not None:
            self.shop_title = m.get('ShopTitle')
        if m.get('ShortTitle') is not None:
            self.short_title = m.get('ShortTitle')
        if m.get('SubTitle') is not None:
            self.sub_title = m.get('SubTitle')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        if m.get('ZkFinalPrice') is not None:
            self.zk_final_price = m.get('ZkFinalPrice')
        return self


class SearchByPicResponseBodyDataAuctions(TeaModel):
    def __init__(
        self,
        rank_score: float = None,
        result: SearchByPicResponseBodyDataAuctionsResult = None,
    ):
        self.rank_score = rank_score
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rank_score is not None:
            result['RankScore'] = self.rank_score
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RankScore') is not None:
            self.rank_score = m.get('RankScore')
        if m.get('Result') is not None:
            temp_model = SearchByPicResponseBodyDataAuctionsResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class SearchByPicResponseBodyData(TeaModel):
    def __init__(
        self,
        auctions: List[SearchByPicResponseBodyDataAuctions] = None,
    ):
        self.auctions = auctions

    def validate(self):
        if self.auctions:
            for k in self.auctions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Auctions'] = []
        if self.auctions is not None:
            for k in self.auctions:
                result['Auctions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.auctions = []
        if m.get('Auctions') is not None:
            for k in m.get('Auctions'):
                temp_model = SearchByPicResponseBodyDataAuctions()
                self.auctions.append(temp_model.from_map(k))
        return self


class SearchByPicResponseBodyPicInfoMainRegionMultiCategoryId(TeaModel):
    def __init__(
        self,
        category_id: int = None,
        score: float = None,
    ):
        self.category_id = category_id
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class SearchByPicResponseBodyPicInfoMainRegion(TeaModel):
    def __init__(
        self,
        multi_category_id: List[SearchByPicResponseBodyPicInfoMainRegionMultiCategoryId] = None,
        region: str = None,
    ):
        self.multi_category_id = multi_category_id
        self.region = region

    def validate(self):
        if self.multi_category_id:
            for k in self.multi_category_id:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MultiCategoryId'] = []
        if self.multi_category_id is not None:
            for k in self.multi_category_id:
                result['MultiCategoryId'].append(k.to_map() if k else None)
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.multi_category_id = []
        if m.get('MultiCategoryId') is not None:
            for k in m.get('MultiCategoryId'):
                temp_model = SearchByPicResponseBodyPicInfoMainRegionMultiCategoryId()
                self.multi_category_id.append(temp_model.from_map(k))
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class SearchByPicResponseBodyPicInfoMultiRegion(TeaModel):
    def __init__(
        self,
        region: str = None,
    ):
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class SearchByPicResponseBodyPicInfo(TeaModel):
    def __init__(
        self,
        main_region: SearchByPicResponseBodyPicInfoMainRegion = None,
        multi_region: List[SearchByPicResponseBodyPicInfoMultiRegion] = None,
    ):
        self.main_region = main_region
        self.multi_region = multi_region

    def validate(self):
        if self.main_region:
            self.main_region.validate()
        if self.multi_region:
            for k in self.multi_region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.main_region is not None:
            result['MainRegion'] = self.main_region.to_map()
        result['MultiRegion'] = []
        if self.multi_region is not None:
            for k in self.multi_region:
                result['MultiRegion'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MainRegion') is not None:
            temp_model = SearchByPicResponseBodyPicInfoMainRegion()
            self.main_region = temp_model.from_map(m['MainRegion'])
        self.multi_region = []
        if m.get('MultiRegion') is not None:
            for k in m.get('MultiRegion'):
                temp_model = SearchByPicResponseBodyPicInfoMultiRegion()
                self.multi_region.append(temp_model.from_map(k))
        return self


class SearchByPicResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: SearchByPicResponseBodyData = None,
        message: str = None,
        pic_info: SearchByPicResponseBodyPicInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.pic_info = pic_info
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()
        if self.pic_info:
            self.pic_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.pic_info is not None:
            result['PicInfo'] = self.pic_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = SearchByPicResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PicInfo') is not None:
            temp_model = SearchByPicResponseBodyPicInfo()
            self.pic_info = temp_model.from_map(m['PicInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SearchByPicResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchByPicResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SearchByPicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchByUrlRequest(TeaModel):
    def __init__(
        self,
        category_id: int = None,
        crop: bool = None,
        fields: str = None,
        num: int = None,
        pic_url: str = None,
        pid: str = None,
        region: str = None,
        relation_id: int = None,
        start: int = None,
        user_type: int = None,
    ):
        self.category_id = category_id
        self.crop = crop
        self.fields = fields
        self.num = num
        self.pic_url = pic_url
        self.pid = pid
        self.region = region
        self.relation_id = relation_id
        self.start = start
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.crop is not None:
            result['Crop'] = self.crop
        if self.fields is not None:
            result['Fields'] = self.fields
        if self.num is not None:
            result['Num'] = self.num
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.region is not None:
            result['Region'] = self.region
        if self.relation_id is not None:
            result['RelationId'] = self.relation_id
        if self.start is not None:
            result['Start'] = self.start
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Crop') is not None:
            self.crop = m.get('Crop')
        if m.get('Fields') is not None:
            self.fields = m.get('Fields')
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RelationId') is not None:
            self.relation_id = m.get('RelationId')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class SearchByUrlResponseBodyDataAuctionsResultMaxCommission(TeaModel):
    def __init__(
        self,
        max_commission_click_url: str = None,
        max_commission_coupon_share_url: str = None,
        max_commission_rate: str = None,
    ):
        self.max_commission_click_url = max_commission_click_url
        self.max_commission_coupon_share_url = max_commission_coupon_share_url
        self.max_commission_rate = max_commission_rate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_commission_click_url is not None:
            result['MaxCommissionClickUrl'] = self.max_commission_click_url
        if self.max_commission_coupon_share_url is not None:
            result['MaxCommissionCouponShareUrl'] = self.max_commission_coupon_share_url
        if self.max_commission_rate is not None:
            result['MaxCommissionRate'] = self.max_commission_rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxCommissionClickUrl') is not None:
            self.max_commission_click_url = m.get('MaxCommissionClickUrl')
        if m.get('MaxCommissionCouponShareUrl') is not None:
            self.max_commission_coupon_share_url = m.get('MaxCommissionCouponShareUrl')
        if m.get('MaxCommissionRate') is not None:
            self.max_commission_rate = m.get('MaxCommissionRate')
        return self


class SearchByUrlResponseBodyDataAuctionsResult(TeaModel):
    def __init__(
        self,
        category_name: str = None,
        commission_rate: str = None,
        coupon_amount: int = None,
        coupon_end_time: str = None,
        coupon_info: str = None,
        coupon_remain_count: int = None,
        coupon_share_url: str = None,
        coupon_start_fee: str = None,
        coupon_start_time: str = None,
        coupon_total_count: str = None,
        deeplink_coupon_share_url: str = None,
        deeplink_url: str = None,
        item_id: str = None,
        level_one_category_name: str = None,
        max_commission: SearchByUrlResponseBodyDataAuctionsResultMaxCommission = None,
        nick: str = None,
        pic_url: str = None,
        price_after_coupon: str = None,
        provcity: str = None,
        reserve_price: str = None,
        seller_id: str = None,
        shop_title: str = None,
        short_title: str = None,
        sub_title: str = None,
        title: str = None,
        url: str = None,
        user_type: int = None,
        volume: int = None,
        zk_final_price: str = None,
    ):
        self.category_name = category_name
        self.commission_rate = commission_rate
        self.coupon_amount = coupon_amount
        self.coupon_end_time = coupon_end_time
        self.coupon_info = coupon_info
        self.coupon_remain_count = coupon_remain_count
        self.coupon_share_url = coupon_share_url
        self.coupon_start_fee = coupon_start_fee
        self.coupon_start_time = coupon_start_time
        self.coupon_total_count = coupon_total_count
        self.deeplink_coupon_share_url = deeplink_coupon_share_url
        self.deeplink_url = deeplink_url
        self.item_id = item_id
        self.level_one_category_name = level_one_category_name
        self.max_commission = max_commission
        self.nick = nick
        self.pic_url = pic_url
        self.price_after_coupon = price_after_coupon
        self.provcity = provcity
        self.reserve_price = reserve_price
        self.seller_id = seller_id
        self.shop_title = shop_title
        self.short_title = short_title
        self.sub_title = sub_title
        self.title = title
        self.url = url
        self.user_type = user_type
        self.volume = volume
        self.zk_final_price = zk_final_price

    def validate(self):
        if self.max_commission:
            self.max_commission.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.commission_rate is not None:
            result['CommissionRate'] = self.commission_rate
        if self.coupon_amount is not None:
            result['CouponAmount'] = self.coupon_amount
        if self.coupon_end_time is not None:
            result['CouponEndTime'] = self.coupon_end_time
        if self.coupon_info is not None:
            result['CouponInfo'] = self.coupon_info
        if self.coupon_remain_count is not None:
            result['CouponRemainCount'] = self.coupon_remain_count
        if self.coupon_share_url is not None:
            result['CouponShareUrl'] = self.coupon_share_url
        if self.coupon_start_fee is not None:
            result['CouponStartFee'] = self.coupon_start_fee
        if self.coupon_start_time is not None:
            result['CouponStartTime'] = self.coupon_start_time
        if self.coupon_total_count is not None:
            result['CouponTotalCount'] = self.coupon_total_count
        if self.deeplink_coupon_share_url is not None:
            result['DeeplinkCouponShareUrl'] = self.deeplink_coupon_share_url
        if self.deeplink_url is not None:
            result['DeeplinkUrl'] = self.deeplink_url
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.level_one_category_name is not None:
            result['LevelOneCategoryName'] = self.level_one_category_name
        if self.max_commission is not None:
            result['MaxCommission'] = self.max_commission.to_map()
        if self.nick is not None:
            result['Nick'] = self.nick
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        if self.price_after_coupon is not None:
            result['PriceAfterCoupon'] = self.price_after_coupon
        if self.provcity is not None:
            result['Provcity'] = self.provcity
        if self.reserve_price is not None:
            result['ReservePrice'] = self.reserve_price
        if self.seller_id is not None:
            result['SellerId'] = self.seller_id
        if self.shop_title is not None:
            result['ShopTitle'] = self.shop_title
        if self.short_title is not None:
            result['ShortTitle'] = self.short_title
        if self.sub_title is not None:
            result['SubTitle'] = self.sub_title
        if self.title is not None:
            result['Title'] = self.title
        if self.url is not None:
            result['Url'] = self.url
        if self.user_type is not None:
            result['UserType'] = self.user_type
        if self.volume is not None:
            result['Volume'] = self.volume
        if self.zk_final_price is not None:
            result['ZkFinalPrice'] = self.zk_final_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('CommissionRate') is not None:
            self.commission_rate = m.get('CommissionRate')
        if m.get('CouponAmount') is not None:
            self.coupon_amount = m.get('CouponAmount')
        if m.get('CouponEndTime') is not None:
            self.coupon_end_time = m.get('CouponEndTime')
        if m.get('CouponInfo') is not None:
            self.coupon_info = m.get('CouponInfo')
        if m.get('CouponRemainCount') is not None:
            self.coupon_remain_count = m.get('CouponRemainCount')
        if m.get('CouponShareUrl') is not None:
            self.coupon_share_url = m.get('CouponShareUrl')
        if m.get('CouponStartFee') is not None:
            self.coupon_start_fee = m.get('CouponStartFee')
        if m.get('CouponStartTime') is not None:
            self.coupon_start_time = m.get('CouponStartTime')
        if m.get('CouponTotalCount') is not None:
            self.coupon_total_count = m.get('CouponTotalCount')
        if m.get('DeeplinkCouponShareUrl') is not None:
            self.deeplink_coupon_share_url = m.get('DeeplinkCouponShareUrl')
        if m.get('DeeplinkUrl') is not None:
            self.deeplink_url = m.get('DeeplinkUrl')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('LevelOneCategoryName') is not None:
            self.level_one_category_name = m.get('LevelOneCategoryName')
        if m.get('MaxCommission') is not None:
            temp_model = SearchByUrlResponseBodyDataAuctionsResultMaxCommission()
            self.max_commission = temp_model.from_map(m['MaxCommission'])
        if m.get('Nick') is not None:
            self.nick = m.get('Nick')
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        if m.get('PriceAfterCoupon') is not None:
            self.price_after_coupon = m.get('PriceAfterCoupon')
        if m.get('Provcity') is not None:
            self.provcity = m.get('Provcity')
        if m.get('ReservePrice') is not None:
            self.reserve_price = m.get('ReservePrice')
        if m.get('SellerId') is not None:
            self.seller_id = m.get('SellerId')
        if m.get('ShopTitle') is not None:
            self.shop_title = m.get('ShopTitle')
        if m.get('ShortTitle') is not None:
            self.short_title = m.get('ShortTitle')
        if m.get('SubTitle') is not None:
            self.sub_title = m.get('SubTitle')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        if m.get('ZkFinalPrice') is not None:
            self.zk_final_price = m.get('ZkFinalPrice')
        return self


class SearchByUrlResponseBodyDataAuctions(TeaModel):
    def __init__(
        self,
        rank_score: float = None,
        result: SearchByUrlResponseBodyDataAuctionsResult = None,
    ):
        self.rank_score = rank_score
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rank_score is not None:
            result['RankScore'] = self.rank_score
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RankScore') is not None:
            self.rank_score = m.get('RankScore')
        if m.get('Result') is not None:
            temp_model = SearchByUrlResponseBodyDataAuctionsResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class SearchByUrlResponseBodyData(TeaModel):
    def __init__(
        self,
        auctions: List[SearchByUrlResponseBodyDataAuctions] = None,
    ):
        self.auctions = auctions

    def validate(self):
        if self.auctions:
            for k in self.auctions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Auctions'] = []
        if self.auctions is not None:
            for k in self.auctions:
                result['Auctions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.auctions = []
        if m.get('Auctions') is not None:
            for k in m.get('Auctions'):
                temp_model = SearchByUrlResponseBodyDataAuctions()
                self.auctions.append(temp_model.from_map(k))
        return self


class SearchByUrlResponseBodyPicInfoMainRegionMultiCategoryId(TeaModel):
    def __init__(
        self,
        category_id: int = None,
        score: float = None,
    ):
        self.category_id = category_id
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class SearchByUrlResponseBodyPicInfoMainRegion(TeaModel):
    def __init__(
        self,
        multi_category_id: List[SearchByUrlResponseBodyPicInfoMainRegionMultiCategoryId] = None,
        region: str = None,
    ):
        self.multi_category_id = multi_category_id
        self.region = region

    def validate(self):
        if self.multi_category_id:
            for k in self.multi_category_id:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MultiCategoryId'] = []
        if self.multi_category_id is not None:
            for k in self.multi_category_id:
                result['MultiCategoryId'].append(k.to_map() if k else None)
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.multi_category_id = []
        if m.get('MultiCategoryId') is not None:
            for k in m.get('MultiCategoryId'):
                temp_model = SearchByUrlResponseBodyPicInfoMainRegionMultiCategoryId()
                self.multi_category_id.append(temp_model.from_map(k))
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class SearchByUrlResponseBodyPicInfoMultiRegion(TeaModel):
    def __init__(
        self,
        region: str = None,
    ):
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class SearchByUrlResponseBodyPicInfo(TeaModel):
    def __init__(
        self,
        main_region: SearchByUrlResponseBodyPicInfoMainRegion = None,
        multi_region: List[SearchByUrlResponseBodyPicInfoMultiRegion] = None,
    ):
        self.main_region = main_region
        self.multi_region = multi_region

    def validate(self):
        if self.main_region:
            self.main_region.validate()
        if self.multi_region:
            for k in self.multi_region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.main_region is not None:
            result['MainRegion'] = self.main_region.to_map()
        result['MultiRegion'] = []
        if self.multi_region is not None:
            for k in self.multi_region:
                result['MultiRegion'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MainRegion') is not None:
            temp_model = SearchByUrlResponseBodyPicInfoMainRegion()
            self.main_region = temp_model.from_map(m['MainRegion'])
        self.multi_region = []
        if m.get('MultiRegion') is not None:
            for k in m.get('MultiRegion'):
                temp_model = SearchByUrlResponseBodyPicInfoMultiRegion()
                self.multi_region.append(temp_model.from_map(k))
        return self


class SearchByUrlResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: SearchByUrlResponseBodyData = None,
        message: str = None,
        pic_info: SearchByUrlResponseBodyPicInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.pic_info = pic_info
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()
        if self.pic_info:
            self.pic_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.pic_info is not None:
            result['PicInfo'] = self.pic_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = SearchByUrlResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PicInfo') is not None:
            temp_model = SearchByUrlResponseBodyPicInfo()
            self.pic_info = temp_model.from_map(m['PicInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SearchByUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchByUrlResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SearchByUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


