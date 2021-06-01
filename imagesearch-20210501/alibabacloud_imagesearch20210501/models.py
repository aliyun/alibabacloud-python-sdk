# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import BinaryIO, List, Dict


class SearchByPicRequest(TeaModel):
    def __init__(
        self,
        pic_content: str = None,
        category_id: int = None,
        crop: bool = None,
        region: str = None,
        start: int = None,
        num: int = None,
        fields: str = None,
        relation_id: int = None,
    ):
        self.pic_content = pic_content
        self.category_id = category_id
        self.crop = crop
        self.region = region
        self.start = start
        self.num = num
        self.fields = fields
        self.relation_id = relation_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pic_content is not None:
            result['PicContent'] = self.pic_content
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.crop is not None:
            result['Crop'] = self.crop
        if self.region is not None:
            result['Region'] = self.region
        if self.start is not None:
            result['Start'] = self.start
        if self.num is not None:
            result['Num'] = self.num
        if self.fields is not None:
            result['Fields'] = self.fields
        if self.relation_id is not None:
            result['RelationId'] = self.relation_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PicContent') is not None:
            self.pic_content = m.get('PicContent')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Crop') is not None:
            self.crop = m.get('Crop')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('Fields') is not None:
            self.fields = m.get('Fields')
        if m.get('RelationId') is not None:
            self.relation_id = m.get('RelationId')
        return self


class SearchByPicAdvanceRequest(TeaModel):
    def __init__(
        self,
        pic_content_object: BinaryIO = None,
        category_id: int = None,
        crop: bool = None,
        region: str = None,
        start: int = None,
        num: int = None,
        fields: str = None,
        relation_id: int = None,
    ):
        self.pic_content_object = pic_content_object
        self.category_id = category_id
        self.crop = crop
        self.region = region
        self.start = start
        self.num = num
        self.fields = fields
        self.relation_id = relation_id

    def validate(self):
        self.validate_required(self.pic_content_object, 'pic_content_object')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pic_content_object is not None:
            result['PicContentObject'] = self.pic_content_object
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.crop is not None:
            result['Crop'] = self.crop
        if self.region is not None:
            result['Region'] = self.region
        if self.start is not None:
            result['Start'] = self.start
        if self.num is not None:
            result['Num'] = self.num
        if self.fields is not None:
            result['Fields'] = self.fields
        if self.relation_id is not None:
            result['RelationId'] = self.relation_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PicContentObject') is not None:
            self.pic_content_object = m.get('PicContentObject')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Crop') is not None:
            self.crop = m.get('Crop')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('Fields') is not None:
            self.fields = m.get('Fields')
        if m.get('RelationId') is not None:
            self.relation_id = m.get('RelationId')
        return self


class SearchByPicResponseBodyDataAuctionsResult(TeaModel):
    def __init__(
        self,
        item_id: str = None,
        item_name: str = None,
        pic: str = None,
        price: str = None,
        promotion_price: str = None,
        price_after_coupon: str = None,
        user_type: int = None,
        provcity: str = None,
        seller_nick_name: str = None,
        seller_id: str = None,
        month_sell_count: int = None,
        level_one_category_name: str = None,
        category_name: str = None,
        coupon_activity_id: str = None,
        coupon_total_count: str = None,
        coupon_send_count: str = None,
        coupon_remain_count: int = None,
        coupon_start_time: str = None,
        coupon_end_time: str = None,
        coupon_start_fee: str = None,
        coupon_amount: int = None,
        coupon_sale_text_info: str = None,
        cal_tk_rate: str = None,
        coupon_share_url: str = None,
        click_url: str = None,
        short_url: str = None,
    ):
        self.item_id = item_id
        self.item_name = item_name
        self.pic = pic
        self.price = price
        self.promotion_price = promotion_price
        self.price_after_coupon = price_after_coupon
        self.user_type = user_type
        self.provcity = provcity
        self.seller_nick_name = seller_nick_name
        self.seller_id = seller_id
        self.month_sell_count = month_sell_count
        self.level_one_category_name = level_one_category_name
        self.category_name = category_name
        self.coupon_activity_id = coupon_activity_id
        self.coupon_total_count = coupon_total_count
        self.coupon_send_count = coupon_send_count
        self.coupon_remain_count = coupon_remain_count
        self.coupon_start_time = coupon_start_time
        self.coupon_end_time = coupon_end_time
        self.coupon_start_fee = coupon_start_fee
        self.coupon_amount = coupon_amount
        self.coupon_sale_text_info = coupon_sale_text_info
        self.cal_tk_rate = cal_tk_rate
        self.coupon_share_url = coupon_share_url
        self.click_url = click_url
        self.short_url = short_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.item_name is not None:
            result['ItemName'] = self.item_name
        if self.pic is not None:
            result['Pic'] = self.pic
        if self.price is not None:
            result['Price'] = self.price
        if self.promotion_price is not None:
            result['PromotionPrice'] = self.promotion_price
        if self.price_after_coupon is not None:
            result['PriceAfterCoupon'] = self.price_after_coupon
        if self.user_type is not None:
            result['UserType'] = self.user_type
        if self.provcity is not None:
            result['Provcity'] = self.provcity
        if self.seller_nick_name is not None:
            result['SellerNickName'] = self.seller_nick_name
        if self.seller_id is not None:
            result['SellerId'] = self.seller_id
        if self.month_sell_count is not None:
            result['MonthSellCount'] = self.month_sell_count
        if self.level_one_category_name is not None:
            result['LevelOneCategoryName'] = self.level_one_category_name
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.coupon_activity_id is not None:
            result['CouponActivityId'] = self.coupon_activity_id
        if self.coupon_total_count is not None:
            result['CouponTotalCount'] = self.coupon_total_count
        if self.coupon_send_count is not None:
            result['CouponSendCount'] = self.coupon_send_count
        if self.coupon_remain_count is not None:
            result['CouponRemainCount'] = self.coupon_remain_count
        if self.coupon_start_time is not None:
            result['CouponStartTime'] = self.coupon_start_time
        if self.coupon_end_time is not None:
            result['CouponEndTime'] = self.coupon_end_time
        if self.coupon_start_fee is not None:
            result['CouponStartFee'] = self.coupon_start_fee
        if self.coupon_amount is not None:
            result['CouponAmount'] = self.coupon_amount
        if self.coupon_sale_text_info is not None:
            result['CouponSaleTextInfo'] = self.coupon_sale_text_info
        if self.cal_tk_rate is not None:
            result['CalTkRate'] = self.cal_tk_rate
        if self.coupon_share_url is not None:
            result['CouponShareUrl'] = self.coupon_share_url
        if self.click_url is not None:
            result['ClickUrl'] = self.click_url
        if self.short_url is not None:
            result['ShortUrl'] = self.short_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ItemName') is not None:
            self.item_name = m.get('ItemName')
        if m.get('Pic') is not None:
            self.pic = m.get('Pic')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('PromotionPrice') is not None:
            self.promotion_price = m.get('PromotionPrice')
        if m.get('PriceAfterCoupon') is not None:
            self.price_after_coupon = m.get('PriceAfterCoupon')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        if m.get('Provcity') is not None:
            self.provcity = m.get('Provcity')
        if m.get('SellerNickName') is not None:
            self.seller_nick_name = m.get('SellerNickName')
        if m.get('SellerId') is not None:
            self.seller_id = m.get('SellerId')
        if m.get('MonthSellCount') is not None:
            self.month_sell_count = m.get('MonthSellCount')
        if m.get('LevelOneCategoryName') is not None:
            self.level_one_category_name = m.get('LevelOneCategoryName')
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('CouponActivityId') is not None:
            self.coupon_activity_id = m.get('CouponActivityId')
        if m.get('CouponTotalCount') is not None:
            self.coupon_total_count = m.get('CouponTotalCount')
        if m.get('CouponSendCount') is not None:
            self.coupon_send_count = m.get('CouponSendCount')
        if m.get('CouponRemainCount') is not None:
            self.coupon_remain_count = m.get('CouponRemainCount')
        if m.get('CouponStartTime') is not None:
            self.coupon_start_time = m.get('CouponStartTime')
        if m.get('CouponEndTime') is not None:
            self.coupon_end_time = m.get('CouponEndTime')
        if m.get('CouponStartFee') is not None:
            self.coupon_start_fee = m.get('CouponStartFee')
        if m.get('CouponAmount') is not None:
            self.coupon_amount = m.get('CouponAmount')
        if m.get('CouponSaleTextInfo') is not None:
            self.coupon_sale_text_info = m.get('CouponSaleTextInfo')
        if m.get('CalTkRate') is not None:
            self.cal_tk_rate = m.get('CalTkRate')
        if m.get('CouponShareUrl') is not None:
            self.coupon_share_url = m.get('CouponShareUrl')
        if m.get('ClickUrl') is not None:
            self.click_url = m.get('ClickUrl')
        if m.get('ShortUrl') is not None:
            self.short_url = m.get('ShortUrl')
        return self


class SearchByPicResponseBodyDataAuctions(TeaModel):
    def __init__(
        self,
        result: SearchByPicResponseBodyDataAuctionsResult = None,
        rank_score: float = None,
    ):
        self.result = result
        self.rank_score = rank_score

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.rank_score is not None:
            result['RankScore'] = self.rank_score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Result') is not None:
            temp_model = SearchByPicResponseBodyDataAuctionsResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('RankScore') is not None:
            self.rank_score = m.get('RankScore')
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
        region: str = None,
        multi_category_id: List[SearchByPicResponseBodyPicInfoMainRegionMultiCategoryId] = None,
    ):
        self.region = region
        self.multi_category_id = multi_category_id

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
        if self.region is not None:
            result['Region'] = self.region
        result['MultiCategoryId'] = []
        if self.multi_category_id is not None:
            for k in self.multi_category_id:
                result['MultiCategoryId'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        self.multi_category_id = []
        if m.get('MultiCategoryId') is not None:
            for k in m.get('MultiCategoryId'):
                temp_model = SearchByPicResponseBodyPicInfoMainRegionMultiCategoryId()
                self.multi_category_id.append(temp_model.from_map(k))
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
        success: bool = None,
        code: int = None,
        message: str = None,
        data: SearchByPicResponseBodyData = None,
        request_id: str = None,
        pic_info: SearchByPicResponseBodyPicInfo = None,
    ):
        self.success = success
        self.code = code
        self.message = message
        self.data = data
        self.request_id = request_id
        self.pic_info = pic_info

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
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.pic_info is not None:
            result['PicInfo'] = self.pic_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = SearchByPicResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PicInfo') is not None:
            temp_model = SearchByPicResponseBodyPicInfo()
            self.pic_info = temp_model.from_map(m['PicInfo'])
        return self


class SearchByPicResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SearchByPicResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SearchByPicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchByUrlRequest(TeaModel):
    def __init__(
        self,
        pic_url: str = None,
        category_id: int = None,
        crop: bool = None,
        region: str = None,
        start: int = None,
        num: int = None,
        fields: str = None,
        relation_id: int = None,
    ):
        self.pic_url = pic_url
        self.category_id = category_id
        self.crop = crop
        self.region = region
        self.start = start
        self.num = num
        self.fields = fields
        self.relation_id = relation_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.crop is not None:
            result['Crop'] = self.crop
        if self.region is not None:
            result['Region'] = self.region
        if self.start is not None:
            result['Start'] = self.start
        if self.num is not None:
            result['Num'] = self.num
        if self.fields is not None:
            result['Fields'] = self.fields
        if self.relation_id is not None:
            result['RelationId'] = self.relation_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Crop') is not None:
            self.crop = m.get('Crop')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('Fields') is not None:
            self.fields = m.get('Fields')
        if m.get('RelationId') is not None:
            self.relation_id = m.get('RelationId')
        return self


class SearchByUrlResponseBodyDataAuctionsResult(TeaModel):
    def __init__(
        self,
        item_id: str = None,
        item_name: str = None,
        pic: str = None,
        price: str = None,
        promotion_price: str = None,
        price_after_coupon: str = None,
        user_type: int = None,
        provcity: str = None,
        seller_nick_name: str = None,
        seller_id: str = None,
        month_sell_count: int = None,
        level_one_category_name: str = None,
        category_name: str = None,
        coupon_activity_id: str = None,
        coupon_total_count: str = None,
        coupon_send_count: str = None,
        coupon_remain_count: int = None,
        coupon_start_time: str = None,
        coupon_end_time: str = None,
        coupon_start_fee: str = None,
        coupon_amount: int = None,
        coupon_sale_text_info: str = None,
        cal_tk_rate: str = None,
        coupon_share_url: str = None,
        click_url: str = None,
        short_url: str = None,
    ):
        self.item_id = item_id
        self.item_name = item_name
        self.pic = pic
        self.price = price
        self.promotion_price = promotion_price
        self.price_after_coupon = price_after_coupon
        self.user_type = user_type
        self.provcity = provcity
        self.seller_nick_name = seller_nick_name
        self.seller_id = seller_id
        self.month_sell_count = month_sell_count
        self.level_one_category_name = level_one_category_name
        self.category_name = category_name
        self.coupon_activity_id = coupon_activity_id
        self.coupon_total_count = coupon_total_count
        self.coupon_send_count = coupon_send_count
        self.coupon_remain_count = coupon_remain_count
        self.coupon_start_time = coupon_start_time
        self.coupon_end_time = coupon_end_time
        self.coupon_start_fee = coupon_start_fee
        self.coupon_amount = coupon_amount
        self.coupon_sale_text_info = coupon_sale_text_info
        self.cal_tk_rate = cal_tk_rate
        self.coupon_share_url = coupon_share_url
        self.click_url = click_url
        self.short_url = short_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.item_name is not None:
            result['ItemName'] = self.item_name
        if self.pic is not None:
            result['Pic'] = self.pic
        if self.price is not None:
            result['Price'] = self.price
        if self.promotion_price is not None:
            result['PromotionPrice'] = self.promotion_price
        if self.price_after_coupon is not None:
            result['PriceAfterCoupon'] = self.price_after_coupon
        if self.user_type is not None:
            result['UserType'] = self.user_type
        if self.provcity is not None:
            result['Provcity'] = self.provcity
        if self.seller_nick_name is not None:
            result['SellerNickName'] = self.seller_nick_name
        if self.seller_id is not None:
            result['SellerId'] = self.seller_id
        if self.month_sell_count is not None:
            result['MonthSellCount'] = self.month_sell_count
        if self.level_one_category_name is not None:
            result['LevelOneCategoryName'] = self.level_one_category_name
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.coupon_activity_id is not None:
            result['CouponActivityId'] = self.coupon_activity_id
        if self.coupon_total_count is not None:
            result['CouponTotalCount'] = self.coupon_total_count
        if self.coupon_send_count is not None:
            result['CouponSendCount'] = self.coupon_send_count
        if self.coupon_remain_count is not None:
            result['CouponRemainCount'] = self.coupon_remain_count
        if self.coupon_start_time is not None:
            result['CouponStartTime'] = self.coupon_start_time
        if self.coupon_end_time is not None:
            result['CouponEndTime'] = self.coupon_end_time
        if self.coupon_start_fee is not None:
            result['CouponStartFee'] = self.coupon_start_fee
        if self.coupon_amount is not None:
            result['CouponAmount'] = self.coupon_amount
        if self.coupon_sale_text_info is not None:
            result['CouponSaleTextInfo'] = self.coupon_sale_text_info
        if self.cal_tk_rate is not None:
            result['CalTkRate'] = self.cal_tk_rate
        if self.coupon_share_url is not None:
            result['CouponShareUrl'] = self.coupon_share_url
        if self.click_url is not None:
            result['ClickUrl'] = self.click_url
        if self.short_url is not None:
            result['ShortUrl'] = self.short_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ItemName') is not None:
            self.item_name = m.get('ItemName')
        if m.get('Pic') is not None:
            self.pic = m.get('Pic')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('PromotionPrice') is not None:
            self.promotion_price = m.get('PromotionPrice')
        if m.get('PriceAfterCoupon') is not None:
            self.price_after_coupon = m.get('PriceAfterCoupon')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        if m.get('Provcity') is not None:
            self.provcity = m.get('Provcity')
        if m.get('SellerNickName') is not None:
            self.seller_nick_name = m.get('SellerNickName')
        if m.get('SellerId') is not None:
            self.seller_id = m.get('SellerId')
        if m.get('MonthSellCount') is not None:
            self.month_sell_count = m.get('MonthSellCount')
        if m.get('LevelOneCategoryName') is not None:
            self.level_one_category_name = m.get('LevelOneCategoryName')
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('CouponActivityId') is not None:
            self.coupon_activity_id = m.get('CouponActivityId')
        if m.get('CouponTotalCount') is not None:
            self.coupon_total_count = m.get('CouponTotalCount')
        if m.get('CouponSendCount') is not None:
            self.coupon_send_count = m.get('CouponSendCount')
        if m.get('CouponRemainCount') is not None:
            self.coupon_remain_count = m.get('CouponRemainCount')
        if m.get('CouponStartTime') is not None:
            self.coupon_start_time = m.get('CouponStartTime')
        if m.get('CouponEndTime') is not None:
            self.coupon_end_time = m.get('CouponEndTime')
        if m.get('CouponStartFee') is not None:
            self.coupon_start_fee = m.get('CouponStartFee')
        if m.get('CouponAmount') is not None:
            self.coupon_amount = m.get('CouponAmount')
        if m.get('CouponSaleTextInfo') is not None:
            self.coupon_sale_text_info = m.get('CouponSaleTextInfo')
        if m.get('CalTkRate') is not None:
            self.cal_tk_rate = m.get('CalTkRate')
        if m.get('CouponShareUrl') is not None:
            self.coupon_share_url = m.get('CouponShareUrl')
        if m.get('ClickUrl') is not None:
            self.click_url = m.get('ClickUrl')
        if m.get('ShortUrl') is not None:
            self.short_url = m.get('ShortUrl')
        return self


class SearchByUrlResponseBodyDataAuctions(TeaModel):
    def __init__(
        self,
        result: SearchByUrlResponseBodyDataAuctionsResult = None,
        rank_score: float = None,
    ):
        self.result = result
        self.rank_score = rank_score

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.rank_score is not None:
            result['RankScore'] = self.rank_score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Result') is not None:
            temp_model = SearchByUrlResponseBodyDataAuctionsResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('RankScore') is not None:
            self.rank_score = m.get('RankScore')
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
        region: str = None,
        multi_category_id: List[SearchByUrlResponseBodyPicInfoMainRegionMultiCategoryId] = None,
    ):
        self.region = region
        self.multi_category_id = multi_category_id

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
        if self.region is not None:
            result['Region'] = self.region
        result['MultiCategoryId'] = []
        if self.multi_category_id is not None:
            for k in self.multi_category_id:
                result['MultiCategoryId'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        self.multi_category_id = []
        if m.get('MultiCategoryId') is not None:
            for k in m.get('MultiCategoryId'):
                temp_model = SearchByUrlResponseBodyPicInfoMainRegionMultiCategoryId()
                self.multi_category_id.append(temp_model.from_map(k))
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
        success: bool = None,
        code: int = None,
        message: str = None,
        data: SearchByUrlResponseBodyData = None,
        request_id: str = None,
        pic_info: SearchByUrlResponseBodyPicInfo = None,
    ):
        self.success = success
        self.code = code
        self.message = message
        self.data = data
        self.request_id = request_id
        self.pic_info = pic_info

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
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.pic_info is not None:
            result['PicInfo'] = self.pic_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = SearchByUrlResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PicInfo') is not None:
            temp_model = SearchByUrlResponseBodyPicInfo()
            self.pic_info = temp_model.from_map(m['PicInfo'])
        return self


class SearchByUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SearchByUrlResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SearchByUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


