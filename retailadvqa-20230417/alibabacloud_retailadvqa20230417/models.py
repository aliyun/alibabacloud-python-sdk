# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class AddMemberBasicInfoRequestBodyChannels(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        channel_code: str = None,
        channel_open_id: str = None,
        channel_union_id: str = None,
        scene: str = None,
    ):
        self.app_id = app_id
        # This parameter is required.
        self.channel_code = channel_code
        self.channel_open_id = channel_open_id
        self.channel_union_id = channel_union_id
        self.scene = scene

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_code is not None:
            result['ChannelCode'] = self.channel_code
        if self.channel_open_id is not None:
            result['ChannelOpenId'] = self.channel_open_id
        if self.channel_union_id is not None:
            result['ChannelUnionId'] = self.channel_union_id
        if self.scene is not None:
            result['Scene'] = self.scene
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelCode') is not None:
            self.channel_code = m.get('ChannelCode')
        if m.get('ChannelOpenId') is not None:
            self.channel_open_id = m.get('ChannelOpenId')
        if m.get('ChannelUnionId') is not None:
            self.channel_union_id = m.get('ChannelUnionId')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        return self


class AddMemberBasicInfoRequestBody(TeaModel):
    def __init__(
        self,
        area: str = None,
        avatar: str = None,
        birthday: str = None,
        channels: List[AddMemberBasicInfoRequestBodyChannels] = None,
        city: str = None,
        country: str = None,
        email: str = None,
        extra: str = None,
        gmt_create: str = None,
        member_name: str = None,
        member_nick_name: str = None,
        mix_mobile: str = None,
        mobile: str = None,
        open_merchant_id: str = None,
        plat_form_type: str = None,
        province: str = None,
        sex: str = None,
    ):
        self.area = area
        self.avatar = avatar
        self.birthday = birthday
        # This parameter is required.
        self.channels = channels
        self.city = city
        self.country = country
        self.email = email
        self.extra = extra
        self.gmt_create = gmt_create
        self.member_name = member_name
        self.member_nick_name = member_nick_name
        self.mix_mobile = mix_mobile
        self.mobile = mobile
        # This parameter is required.
        self.open_merchant_id = open_merchant_id
        # This parameter is required.
        self.plat_form_type = plat_form_type
        self.province = province
        self.sex = sex

    def validate(self):
        if self.channels:
            for k in self.channels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area is not None:
            result['Area'] = self.area
        if self.avatar is not None:
            result['Avatar'] = self.avatar
        if self.birthday is not None:
            result['Birthday'] = self.birthday
        result['Channels'] = []
        if self.channels is not None:
            for k in self.channels:
                result['Channels'].append(k.to_map() if k else None)
        if self.city is not None:
            result['City'] = self.city
        if self.country is not None:
            result['Country'] = self.country
        if self.email is not None:
            result['Email'] = self.email
        if self.extra is not None:
            result['Extra'] = self.extra
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        if self.member_nick_name is not None:
            result['MemberNickName'] = self.member_nick_name
        if self.mix_mobile is not None:
            result['MixMobile'] = self.mix_mobile
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.open_merchant_id is not None:
            result['OpenMerchantId'] = self.open_merchant_id
        if self.plat_form_type is not None:
            result['PlatFormType'] = self.plat_form_type
        if self.province is not None:
            result['Province'] = self.province
        if self.sex is not None:
            result['Sex'] = self.sex
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')
        if m.get('Avatar') is not None:
            self.avatar = m.get('Avatar')
        if m.get('Birthday') is not None:
            self.birthday = m.get('Birthday')
        self.channels = []
        if m.get('Channels') is not None:
            for k in m.get('Channels'):
                temp_model = AddMemberBasicInfoRequestBodyChannels()
                self.channels.append(temp_model.from_map(k))
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        if m.get('MemberNickName') is not None:
            self.member_nick_name = m.get('MemberNickName')
        if m.get('MixMobile') is not None:
            self.mix_mobile = m.get('MixMobile')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('OpenMerchantId') is not None:
            self.open_merchant_id = m.get('OpenMerchantId')
        if m.get('PlatFormType') is not None:
            self.plat_form_type = m.get('PlatFormType')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('Sex') is not None:
            self.sex = m.get('Sex')
        return self


class AddMemberBasicInfoRequest(TeaModel):
    def __init__(
        self,
        body: AddMemberBasicInfoRequestBody = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = AddMemberBasicInfoRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddMemberBasicInfoShrinkRequest(TeaModel):
    def __init__(
        self,
        body_shrink: str = None,
    ):
        self.body_shrink = body_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body_shrink is not None:
            result['body'] = self.body_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body_shrink = m.get('body')
        return self


class AddMemberBasicInfoResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        outer_member_id: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.outer_member_id = outer_member_id
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.outer_member_id is not None:
            result['OuterMemberId'] = self.outer_member_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('OuterMemberId') is not None:
            self.outer_member_id = m.get('OuterMemberId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddMemberBasicInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddMemberBasicInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = AddMemberBasicInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchSaveOrderPopRequestOrdersSubOrderModelList(TeaModel):
    def __init__(
        self,
        feature: str = None,
        open_sub_order_id: str = None,
        order_payment: str = None,
        out_product_id: str = None,
        product_amount: str = None,
        product_id: str = None,
        product_name: str = None,
        refund_status: str = None,
        status: str = None,
        total_fee: str = None,
    ):
        self.feature = feature
        # This parameter is required.
        self.open_sub_order_id = open_sub_order_id
        # This parameter is required.
        self.order_payment = order_payment
        self.out_product_id = out_product_id
        # This parameter is required.
        self.product_amount = product_amount
        self.product_id = product_id
        self.product_name = product_name
        self.refund_status = refund_status
        # This parameter is required.
        self.status = status
        # This parameter is required.
        self.total_fee = total_fee

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature is not None:
            result['Feature'] = self.feature
        if self.open_sub_order_id is not None:
            result['OpenSubOrderId'] = self.open_sub_order_id
        if self.order_payment is not None:
            result['OrderPayment'] = self.order_payment
        if self.out_product_id is not None:
            result['OutProductId'] = self.out_product_id
        if self.product_amount is not None:
            result['ProductAmount'] = self.product_amount
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.refund_status is not None:
            result['RefundStatus'] = self.refund_status
        if self.status is not None:
            result['Status'] = self.status
        if self.total_fee is not None:
            result['TotalFee'] = self.total_fee
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Feature') is not None:
            self.feature = m.get('Feature')
        if m.get('OpenSubOrderId') is not None:
            self.open_sub_order_id = m.get('OpenSubOrderId')
        if m.get('OrderPayment') is not None:
            self.order_payment = m.get('OrderPayment')
        if m.get('OutProductId') is not None:
            self.out_product_id = m.get('OutProductId')
        if m.get('ProductAmount') is not None:
            self.product_amount = m.get('ProductAmount')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('RefundStatus') is not None:
            self.refund_status = m.get('RefundStatus')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalFee') is not None:
            self.total_fee = m.get('TotalFee')
        return self


class BatchSaveOrderPopRequestOrders(TeaModel):
    def __init__(
        self,
        channel_code: str = None,
        channel_open_id: str = None,
        end_time: str = None,
        feature: str = None,
        open_merchant_id: str = None,
        open_order_id: str = None,
        order_create_time: str = None,
        order_payment: str = None,
        pay_time: str = None,
        platform_type: str = None,
        shop_id: str = None,
        status: str = None,
        sub_order_model_list: List[BatchSaveOrderPopRequestOrdersSubOrderModelList] = None,
        total_fee: str = None,
        buyer_open_uid: str = None,
    ):
        # This parameter is required.
        self.channel_code = channel_code
        # This parameter is required.
        self.channel_open_id = channel_open_id
        self.end_time = end_time
        self.feature = feature
        # This parameter is required.
        self.open_merchant_id = open_merchant_id
        # This parameter is required.
        self.open_order_id = open_order_id
        # This parameter is required.
        self.order_create_time = order_create_time
        # This parameter is required.
        self.order_payment = order_payment
        self.pay_time = pay_time
        # This parameter is required.
        self.platform_type = platform_type
        # This parameter is required.
        self.shop_id = shop_id
        # This parameter is required.
        self.status = status
        # This parameter is required.
        self.sub_order_model_list = sub_order_model_list
        # This parameter is required.
        self.total_fee = total_fee
        self.buyer_open_uid = buyer_open_uid

    def validate(self):
        if self.sub_order_model_list:
            for k in self.sub_order_model_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_code is not None:
            result['ChannelCode'] = self.channel_code
        if self.channel_open_id is not None:
            result['ChannelOpenId'] = self.channel_open_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.feature is not None:
            result['Feature'] = self.feature
        if self.open_merchant_id is not None:
            result['OpenMerchantId'] = self.open_merchant_id
        if self.open_order_id is not None:
            result['OpenOrderId'] = self.open_order_id
        if self.order_create_time is not None:
            result['OrderCreateTime'] = self.order_create_time
        if self.order_payment is not None:
            result['OrderPayment'] = self.order_payment
        if self.pay_time is not None:
            result['PayTime'] = self.pay_time
        if self.platform_type is not None:
            result['PlatformType'] = self.platform_type
        if self.shop_id is not None:
            result['ShopId'] = self.shop_id
        if self.status is not None:
            result['Status'] = self.status
        result['SubOrderModelList'] = []
        if self.sub_order_model_list is not None:
            for k in self.sub_order_model_list:
                result['SubOrderModelList'].append(k.to_map() if k else None)
        if self.total_fee is not None:
            result['TotalFee'] = self.total_fee
        if self.buyer_open_uid is not None:
            result['buyerOpenUid'] = self.buyer_open_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelCode') is not None:
            self.channel_code = m.get('ChannelCode')
        if m.get('ChannelOpenId') is not None:
            self.channel_open_id = m.get('ChannelOpenId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Feature') is not None:
            self.feature = m.get('Feature')
        if m.get('OpenMerchantId') is not None:
            self.open_merchant_id = m.get('OpenMerchantId')
        if m.get('OpenOrderId') is not None:
            self.open_order_id = m.get('OpenOrderId')
        if m.get('OrderCreateTime') is not None:
            self.order_create_time = m.get('OrderCreateTime')
        if m.get('OrderPayment') is not None:
            self.order_payment = m.get('OrderPayment')
        if m.get('PayTime') is not None:
            self.pay_time = m.get('PayTime')
        if m.get('PlatformType') is not None:
            self.platform_type = m.get('PlatformType')
        if m.get('ShopId') is not None:
            self.shop_id = m.get('ShopId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.sub_order_model_list = []
        if m.get('SubOrderModelList') is not None:
            for k in m.get('SubOrderModelList'):
                temp_model = BatchSaveOrderPopRequestOrdersSubOrderModelList()
                self.sub_order_model_list.append(temp_model.from_map(k))
        if m.get('TotalFee') is not None:
            self.total_fee = m.get('TotalFee')
        if m.get('buyerOpenUid') is not None:
            self.buyer_open_uid = m.get('buyerOpenUid')
        return self


class BatchSaveOrderPopRequest(TeaModel):
    def __init__(
        self,
        orders: List[BatchSaveOrderPopRequestOrders] = None,
    ):
        self.orders = orders

    def validate(self):
        if self.orders:
            for k in self.orders:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Orders'] = []
        if self.orders is not None:
            for k in self.orders:
                result['Orders'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.orders = []
        if m.get('Orders') is not None:
            for k in m.get('Orders'):
                temp_model = BatchSaveOrderPopRequestOrders()
                self.orders.append(temp_model.from_map(k))
        return self


class BatchSaveOrderPopShrinkRequest(TeaModel):
    def __init__(
        self,
        orders_shrink: str = None,
    ):
        self.orders_shrink = orders_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.orders_shrink is not None:
            result['Orders'] = self.orders_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Orders') is not None:
            self.orders_shrink = m.get('Orders')
        return self


class BatchSaveOrderPopResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        http_status_code: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.http_status_code = http_status_code
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BatchSaveOrderPopResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchSaveOrderPopResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = BatchSaveOrderPopResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CalculateMemberLevelRequestBody(TeaModel):
    def __init__(
        self,
        current_grade: int = None,
        current_grade_name: str = None,
        member_id: str = None,
        open_merchant_id: str = None,
        platform_type: str = None,
        score: str = None,
        serial_no: str = None,
    ):
        # This parameter is required.
        self.current_grade = current_grade
        # This parameter is required.
        self.current_grade_name = current_grade_name
        # This parameter is required.
        self.member_id = member_id
        # This parameter is required.
        self.open_merchant_id = open_merchant_id
        # This parameter is required.
        self.platform_type = platform_type
        self.score = score
        # This parameter is required.
        self.serial_no = serial_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_grade is not None:
            result['CurrentGrade'] = self.current_grade
        if self.current_grade_name is not None:
            result['CurrentGradeName'] = self.current_grade_name
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.open_merchant_id is not None:
            result['OpenMerchantId'] = self.open_merchant_id
        if self.platform_type is not None:
            result['PlatformType'] = self.platform_type
        if self.score is not None:
            result['Score'] = self.score
        if self.serial_no is not None:
            result['SerialNo'] = self.serial_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentGrade') is not None:
            self.current_grade = m.get('CurrentGrade')
        if m.get('CurrentGradeName') is not None:
            self.current_grade_name = m.get('CurrentGradeName')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('OpenMerchantId') is not None:
            self.open_merchant_id = m.get('OpenMerchantId')
        if m.get('PlatformType') is not None:
            self.platform_type = m.get('PlatformType')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('SerialNo') is not None:
            self.serial_no = m.get('SerialNo')
        return self


class CalculateMemberLevelRequest(TeaModel):
    def __init__(
        self,
        body: CalculateMemberLevelRequestBody = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = CalculateMemberLevelRequestBody()
            self.body = temp_model.from_map(m['Body'])
        return self


class CalculateMemberLevelShrinkRequest(TeaModel):
    def __init__(
        self,
        body_shrink: str = None,
    ):
        self.body_shrink = body_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body_shrink is not None:
            result['Body'] = self.body_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            self.body_shrink = m.get('Body')
        return self


class CalculateMemberLevelResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        grade: str = None,
        http_status_code: str = None,
        message: str = None,
        outer_member_id: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.grade = grade
        self.http_status_code = http_status_code
        self.message = message
        self.outer_member_id = outer_member_id
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.grade is not None:
            result['Grade'] = self.grade
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.outer_member_id is not None:
            result['OuterMemberId'] = self.outer_member_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Grade') is not None:
            self.grade = m.get('Grade')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OuterMemberId') is not None:
            self.outer_member_id = m.get('OuterMemberId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CalculateMemberLevelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CalculateMemberLevelResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CalculateMemberLevelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EditMemberBasicInfoRequestBody(TeaModel):
    def __init__(
        self,
        area: str = None,
        avatar: str = None,
        birthday: str = None,
        city: str = None,
        country: str = None,
        email: str = None,
        member_name: str = None,
        member_nick_name: str = None,
        mobile: str = None,
        open_merchant_id: str = None,
        platform_type: str = None,
        province: str = None,
        sex: str = None,
    ):
        self.area = area
        self.avatar = avatar
        self.birthday = birthday
        self.city = city
        self.country = country
        self.email = email
        self.member_name = member_name
        self.member_nick_name = member_nick_name
        # This parameter is required.
        self.mobile = mobile
        # This parameter is required.
        self.open_merchant_id = open_merchant_id
        # This parameter is required.
        self.platform_type = platform_type
        self.province = province
        self.sex = sex

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area is not None:
            result['Area'] = self.area
        if self.avatar is not None:
            result['Avatar'] = self.avatar
        if self.birthday is not None:
            result['Birthday'] = self.birthday
        if self.city is not None:
            result['City'] = self.city
        if self.country is not None:
            result['Country'] = self.country
        if self.email is not None:
            result['Email'] = self.email
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        if self.member_nick_name is not None:
            result['MemberNickName'] = self.member_nick_name
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.open_merchant_id is not None:
            result['OpenMerchantId'] = self.open_merchant_id
        if self.platform_type is not None:
            result['PlatformType'] = self.platform_type
        if self.province is not None:
            result['Province'] = self.province
        if self.sex is not None:
            result['Sex'] = self.sex
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')
        if m.get('Avatar') is not None:
            self.avatar = m.get('Avatar')
        if m.get('Birthday') is not None:
            self.birthday = m.get('Birthday')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        if m.get('MemberNickName') is not None:
            self.member_nick_name = m.get('MemberNickName')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('OpenMerchantId') is not None:
            self.open_merchant_id = m.get('OpenMerchantId')
        if m.get('PlatformType') is not None:
            self.platform_type = m.get('PlatformType')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('Sex') is not None:
            self.sex = m.get('Sex')
        return self


class EditMemberBasicInfoRequest(TeaModel):
    def __init__(
        self,
        body: EditMemberBasicInfoRequestBody = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = EditMemberBasicInfoRequestBody()
            self.body = temp_model.from_map(m['Body'])
        return self


class EditMemberBasicInfoShrinkRequest(TeaModel):
    def __init__(
        self,
        body_shrink: str = None,
    ):
        self.body_shrink = body_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body_shrink is not None:
            result['Body'] = self.body_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            self.body_shrink = m.get('Body')
        return self


class EditMemberBasicInfoResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EditMemberBasicInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EditMemberBasicInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = EditMemberBasicInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MemberAccountDetailPageQueryRequestBody(TeaModel):
    def __init__(
        self,
        account_type: int = None,
        end_time: str = None,
        open_merchant_id: str = None,
        outer_member_id: str = None,
        page: int = None,
        page_size: int = None,
        plat_form_type: str = None,
        start_time: str = None,
    ):
        # This parameter is required.
        self.account_type = account_type
        self.end_time = end_time
        # This parameter is required.
        self.open_merchant_id = open_merchant_id
        # This parameter is required.
        self.outer_member_id = outer_member_id
        self.page = page
        self.page_size = page_size
        # This parameter is required.
        self.plat_form_type = plat_form_type
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.open_merchant_id is not None:
            result['OpenMerchantId'] = self.open_merchant_id
        if self.outer_member_id is not None:
            result['OuterMemberId'] = self.outer_member_id
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.plat_form_type is not None:
            result['PlatFormType'] = self.plat_form_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OpenMerchantId') is not None:
            self.open_merchant_id = m.get('OpenMerchantId')
        if m.get('OuterMemberId') is not None:
            self.outer_member_id = m.get('OuterMemberId')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PlatFormType') is not None:
            self.plat_form_type = m.get('PlatFormType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class MemberAccountDetailPageQueryRequest(TeaModel):
    def __init__(
        self,
        body: MemberAccountDetailPageQueryRequestBody = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = MemberAccountDetailPageQueryRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MemberAccountDetailPageQueryShrinkRequest(TeaModel):
    def __init__(
        self,
        body_shrink: str = None,
    ):
        self.body_shrink = body_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body_shrink is not None:
            result['body'] = self.body_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body_shrink = m.get('body')
        return self


class MemberAccountDetailPageQueryResponseBodyData(TeaModel):
    def __init__(
        self,
        account_balance: str = None,
        account_type: int = None,
        activity_type: str = None,
        channel_code: str = None,
        detail_value: str = None,
        extra: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        open_merchant_id: str = None,
        operate_type: str = None,
        outer_member_id: str = None,
        remark: str = None,
    ):
        self.account_balance = account_balance
        self.account_type = account_type
        # This parameter is required.
        self.activity_type = activity_type
        self.channel_code = channel_code
        self.detail_value = detail_value
        # This parameter is required.
        self.extra = extra
        # This parameter is required.
        self.gmt_create = gmt_create
        # This parameter is required.
        self.gmt_modified = gmt_modified
        self.open_merchant_id = open_merchant_id
        self.operate_type = operate_type
        self.outer_member_id = outer_member_id
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_balance is not None:
            result['AccountBalance'] = self.account_balance
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.activity_type is not None:
            result['ActivityType'] = self.activity_type
        if self.channel_code is not None:
            result['ChannelCode'] = self.channel_code
        if self.detail_value is not None:
            result['DetailValue'] = self.detail_value
        if self.extra is not None:
            result['Extra'] = self.extra
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.open_merchant_id is not None:
            result['OpenMerchantId'] = self.open_merchant_id
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        if self.outer_member_id is not None:
            result['OuterMemberId'] = self.outer_member_id
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountBalance') is not None:
            self.account_balance = m.get('AccountBalance')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('ActivityType') is not None:
            self.activity_type = m.get('ActivityType')
        if m.get('ChannelCode') is not None:
            self.channel_code = m.get('ChannelCode')
        if m.get('DetailValue') is not None:
            self.detail_value = m.get('DetailValue')
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('OpenMerchantId') is not None:
            self.open_merchant_id = m.get('OpenMerchantId')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        if m.get('OuterMemberId') is not None:
            self.outer_member_id = m.get('OuterMemberId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class MemberAccountDetailPageQueryResponseBody(TeaModel):
    def __init__(
        self,
        data: List[MemberAccountDetailPageQueryResponseBodyData] = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: str = None,
        total_count: int = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        # Id of the request
        self.request_id = request_id
        # This parameter is required.
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = MemberAccountDetailPageQueryResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class MemberAccountDetailPageQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: MemberAccountDetailPageQueryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = MemberAccountDetailPageQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MemberPointChangeRequestBody(TeaModel):
    def __init__(
        self,
        account_type: str = None,
        channel_code: str = None,
        extra: str = None,
        open_merchant_id: str = None,
        operate_type: str = None,
        outer_member_id: str = None,
        plat_form_type: str = None,
        quantity: str = None,
        serial_no: str = None,
    ):
        # This parameter is required.
        self.account_type = account_type
        self.channel_code = channel_code
        self.extra = extra
        # This parameter is required.
        self.open_merchant_id = open_merchant_id
        # This parameter is required.
        self.operate_type = operate_type
        # This parameter is required.
        self.outer_member_id = outer_member_id
        # This parameter is required.
        self.plat_form_type = plat_form_type
        # This parameter is required.
        self.quantity = quantity
        # This parameter is required.
        self.serial_no = serial_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.channel_code is not None:
            result['ChannelCode'] = self.channel_code
        if self.extra is not None:
            result['Extra'] = self.extra
        if self.open_merchant_id is not None:
            result['OpenMerchantId'] = self.open_merchant_id
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        if self.outer_member_id is not None:
            result['OuterMemberId'] = self.outer_member_id
        if self.plat_form_type is not None:
            result['PlatFormType'] = self.plat_form_type
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.serial_no is not None:
            result['SerialNo'] = self.serial_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('ChannelCode') is not None:
            self.channel_code = m.get('ChannelCode')
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        if m.get('OpenMerchantId') is not None:
            self.open_merchant_id = m.get('OpenMerchantId')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        if m.get('OuterMemberId') is not None:
            self.outer_member_id = m.get('OuterMemberId')
        if m.get('PlatFormType') is not None:
            self.plat_form_type = m.get('PlatFormType')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('SerialNo') is not None:
            self.serial_no = m.get('SerialNo')
        return self


class MemberPointChangeRequest(TeaModel):
    def __init__(
        self,
        body: MemberPointChangeRequestBody = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = MemberPointChangeRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MemberPointChangeShrinkRequest(TeaModel):
    def __init__(
        self,
        body_shrink: str = None,
    ):
        self.body_shrink = body_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body_shrink is not None:
            result['body'] = self.body_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body_shrink = m.get('body')
        return self


class MemberPointChangeResponseBody(TeaModel):
    def __init__(
        self,
        account_balance: str = None,
        error_code: str = None,
        error_message: str = None,
        level_name: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.account_balance = account_balance
        self.error_code = error_code
        self.error_message = error_message
        # This parameter is required.
        self.level_name = level_name
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_balance is not None:
            result['AccountBalance'] = self.account_balance
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.level_name is not None:
            result['LevelName'] = self.level_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountBalance') is not None:
            self.account_balance = m.get('AccountBalance')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('LevelName') is not None:
            self.level_name = m.get('LevelName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class MemberPointChangeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: MemberPointChangeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = MemberPointChangeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMemberBasicInfoRequestBody(TeaModel):
    def __init__(
        self,
        channel_code: str = None,
        channel_open_id: str = None,
        mobile: str = None,
        open_merchant_id: str = None,
        outer_member_id: str = None,
        plat_form_type: str = None,
        type: str = None,
    ):
        self.channel_code = channel_code
        self.channel_open_id = channel_open_id
        self.mobile = mobile
        # This parameter is required.
        self.open_merchant_id = open_merchant_id
        self.outer_member_id = outer_member_id
        # This parameter is required.
        self.plat_form_type = plat_form_type
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_code is not None:
            result['ChannelCode'] = self.channel_code
        if self.channel_open_id is not None:
            result['ChannelOpenId'] = self.channel_open_id
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.open_merchant_id is not None:
            result['OpenMerchantId'] = self.open_merchant_id
        if self.outer_member_id is not None:
            result['OuterMemberId'] = self.outer_member_id
        if self.plat_form_type is not None:
            result['PlatFormType'] = self.plat_form_type
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelCode') is not None:
            self.channel_code = m.get('ChannelCode')
        if m.get('ChannelOpenId') is not None:
            self.channel_open_id = m.get('ChannelOpenId')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('OpenMerchantId') is not None:
            self.open_merchant_id = m.get('OpenMerchantId')
        if m.get('OuterMemberId') is not None:
            self.outer_member_id = m.get('OuterMemberId')
        if m.get('PlatFormType') is not None:
            self.plat_form_type = m.get('PlatFormType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryMemberBasicInfoRequest(TeaModel):
    def __init__(
        self,
        body: QueryMemberBasicInfoRequestBody = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = QueryMemberBasicInfoRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMemberBasicInfoShrinkRequest(TeaModel):
    def __init__(
        self,
        body_shrink: str = None,
    ):
        self.body_shrink = body_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body_shrink is not None:
            result['body'] = self.body_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body_shrink = m.get('body')
        return self


class QueryMemberBasicInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        area: str = None,
        avatar: str = None,
        birthday: str = None,
        city: str = None,
        country: str = None,
        email: str = None,
        extra: str = None,
        level_name: str = None,
        level_num: str = None,
        member_name: str = None,
        member_nick_name: str = None,
        mobile: str = None,
        near_expired_score: str = None,
        open_merchant_id: str = None,
        outer_member_id: str = None,
        points: str = None,
        province: str = None,
        score: str = None,
        sex: str = None,
    ):
        self.area = area
        # This parameter is required.
        self.avatar = avatar
        self.birthday = birthday
        self.city = city
        self.country = country
        self.email = email
        self.extra = extra
        self.level_name = level_name
        self.level_num = level_num
        self.member_name = member_name
        self.member_nick_name = member_nick_name
        self.mobile = mobile
        self.near_expired_score = near_expired_score
        self.open_merchant_id = open_merchant_id
        self.outer_member_id = outer_member_id
        self.points = points
        self.province = province
        self.score = score
        self.sex = sex

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area is not None:
            result['Area'] = self.area
        if self.avatar is not None:
            result['Avatar'] = self.avatar
        if self.birthday is not None:
            result['Birthday'] = self.birthday
        if self.city is not None:
            result['City'] = self.city
        if self.country is not None:
            result['Country'] = self.country
        if self.email is not None:
            result['Email'] = self.email
        if self.extra is not None:
            result['Extra'] = self.extra
        if self.level_name is not None:
            result['LevelName'] = self.level_name
        if self.level_num is not None:
            result['LevelNum'] = self.level_num
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        if self.member_nick_name is not None:
            result['MemberNickName'] = self.member_nick_name
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.near_expired_score is not None:
            result['NearExpiredScore'] = self.near_expired_score
        if self.open_merchant_id is not None:
            result['OpenMerchantId'] = self.open_merchant_id
        if self.outer_member_id is not None:
            result['OuterMemberId'] = self.outer_member_id
        if self.points is not None:
            result['Points'] = self.points
        if self.province is not None:
            result['Province'] = self.province
        if self.score is not None:
            result['Score'] = self.score
        if self.sex is not None:
            result['Sex'] = self.sex
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')
        if m.get('Avatar') is not None:
            self.avatar = m.get('Avatar')
        if m.get('Birthday') is not None:
            self.birthday = m.get('Birthday')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        if m.get('LevelName') is not None:
            self.level_name = m.get('LevelName')
        if m.get('LevelNum') is not None:
            self.level_num = m.get('LevelNum')
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        if m.get('MemberNickName') is not None:
            self.member_nick_name = m.get('MemberNickName')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('NearExpiredScore') is not None:
            self.near_expired_score = m.get('NearExpiredScore')
        if m.get('OpenMerchantId') is not None:
            self.open_merchant_id = m.get('OpenMerchantId')
        if m.get('OuterMemberId') is not None:
            self.outer_member_id = m.get('OuterMemberId')
        if m.get('Points') is not None:
            self.points = m.get('Points')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Sex') is not None:
            self.sex = m.get('Sex')
        return self


class QueryMemberBasicInfoResponseBody(TeaModel):
    def __init__(
        self,
        data: QueryMemberBasicInfoResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
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
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = QueryMemberBasicInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryMemberBasicInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryMemberBasicInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = QueryMemberBasicInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SyncCardInfoRequestBodyGifters(TeaModel):
    def __init__(
        self,
        header_img: str = None,
        id: str = None,
        nickname: str = None,
        open_id: str = None,
        phone: str = None,
    ):
        self.header_img = header_img
        self.id = id
        self.nickname = nickname
        # openId
        self.open_id = open_id
        self.phone = phone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.header_img is not None:
            result['HeaderImg'] = self.header_img
        if self.id is not None:
            result['Id'] = self.id
        if self.nickname is not None:
            result['Nickname'] = self.nickname
        if self.open_id is not None:
            result['OpenId'] = self.open_id
        if self.phone is not None:
            result['Phone'] = self.phone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HeaderImg') is not None:
            self.header_img = m.get('HeaderImg')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Nickname') is not None:
            self.nickname = m.get('Nickname')
        if m.get('OpenId') is not None:
            self.open_id = m.get('OpenId')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        return self


class SyncCardInfoRequestBodyPresentDetail(TeaModel):
    def __init__(
        self,
        count: int = None,
        item_id: str = None,
        name: str = None,
        price: float = None,
        sku_id: str = None,
    ):
        self.count = count
        self.item_id = item_id
        self.name = name
        self.price = price
        self.sku_id = sku_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.name is not None:
            result['Name'] = self.name
        if self.price is not None:
            result['Price'] = self.price
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        return self


class SyncCardInfoRequestBodyRecipient(TeaModel):
    def __init__(
        self,
        header_img: str = None,
        id: str = None,
        nickname: str = None,
        open_id: str = None,
        phone: str = None,
    ):
        self.header_img = header_img
        self.id = id
        self.nickname = nickname
        # openId
        self.open_id = open_id
        self.phone = phone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.header_img is not None:
            result['HeaderImg'] = self.header_img
        if self.id is not None:
            result['Id'] = self.id
        if self.nickname is not None:
            result['Nickname'] = self.nickname
        if self.open_id is not None:
            result['OpenId'] = self.open_id
        if self.phone is not None:
            result['Phone'] = self.phone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HeaderImg') is not None:
            self.header_img = m.get('HeaderImg')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Nickname') is not None:
            self.nickname = m.get('Nickname')
        if m.get('OpenId') is not None:
            self.open_id = m.get('OpenId')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        return self


class SyncCardInfoRequestBody(TeaModel):
    def __init__(
        self,
        buyer_id: str = None,
        extra: str = None,
        gifters: SyncCardInfoRequestBodyGifters = None,
        occurred_at: str = None,
        open_merchant_id: str = None,
        order_id: str = None,
        present_detail: List[SyncCardInfoRequestBodyPresentDetail] = None,
        received_at: str = None,
        recipient: SyncCardInfoRequestBodyRecipient = None,
        status: str = None,
        theme: str = None,
        transfer_id: str = None,
        transferred_at: str = None,
    ):
        self.buyer_id = buyer_id
        self.extra = extra
        self.gifters = gifters
        self.occurred_at = occurred_at
        self.open_merchant_id = open_merchant_id
        self.order_id = order_id
        self.present_detail = present_detail
        self.received_at = received_at
        self.recipient = recipient
        self.status = status
        self.theme = theme
        self.transfer_id = transfer_id
        self.transferred_at = transferred_at

    def validate(self):
        if self.gifters:
            self.gifters.validate()
        if self.present_detail:
            for k in self.present_detail:
                if k:
                    k.validate()
        if self.recipient:
            self.recipient.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.buyer_id is not None:
            result['BuyerId'] = self.buyer_id
        if self.extra is not None:
            result['Extra'] = self.extra
        if self.gifters is not None:
            result['Gifters'] = self.gifters.to_map()
        if self.occurred_at is not None:
            result['OccurredAt'] = self.occurred_at
        if self.open_merchant_id is not None:
            result['OpenMerchantId'] = self.open_merchant_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        result['PresentDetail'] = []
        if self.present_detail is not None:
            for k in self.present_detail:
                result['PresentDetail'].append(k.to_map() if k else None)
        if self.received_at is not None:
            result['ReceivedAt'] = self.received_at
        if self.recipient is not None:
            result['Recipient'] = self.recipient.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.theme is not None:
            result['Theme'] = self.theme
        if self.transfer_id is not None:
            result['TransferId'] = self.transfer_id
        if self.transferred_at is not None:
            result['TransferredAt'] = self.transferred_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuyerId') is not None:
            self.buyer_id = m.get('BuyerId')
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        if m.get('Gifters') is not None:
            temp_model = SyncCardInfoRequestBodyGifters()
            self.gifters = temp_model.from_map(m['Gifters'])
        if m.get('OccurredAt') is not None:
            self.occurred_at = m.get('OccurredAt')
        if m.get('OpenMerchantId') is not None:
            self.open_merchant_id = m.get('OpenMerchantId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        self.present_detail = []
        if m.get('PresentDetail') is not None:
            for k in m.get('PresentDetail'):
                temp_model = SyncCardInfoRequestBodyPresentDetail()
                self.present_detail.append(temp_model.from_map(k))
        if m.get('ReceivedAt') is not None:
            self.received_at = m.get('ReceivedAt')
        if m.get('Recipient') is not None:
            temp_model = SyncCardInfoRequestBodyRecipient()
            self.recipient = temp_model.from_map(m['Recipient'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Theme') is not None:
            self.theme = m.get('Theme')
        if m.get('TransferId') is not None:
            self.transfer_id = m.get('TransferId')
        if m.get('TransferredAt') is not None:
            self.transferred_at = m.get('TransferredAt')
        return self


class SyncCardInfoRequest(TeaModel):
    def __init__(
        self,
        body: SyncCardInfoRequestBody = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = SyncCardInfoRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SyncCardInfoShrinkRequest(TeaModel):
    def __init__(
        self,
        body_shrink: str = None,
    ):
        self.body_shrink = body_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body_shrink is not None:
            result['body'] = self.body_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body_shrink = m.get('body')
        return self


class SyncCardInfoResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SyncCardInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SyncCardInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = SyncCardInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SyncMemberBehaviorInfoRequestBody(TeaModel):
    def __init__(
        self,
        action_duration: str = None,
        action_end_date: str = None,
        action_result: bool = None,
        action_start_date: str = None,
        action_sub_type: str = None,
        action_type: str = None,
        extra: str = None,
        open_merchant_id: str = None,
        outer_member_id: str = None,
        plat_form_type: str = None,
    ):
        self.action_duration = action_duration
        self.action_end_date = action_end_date
        self.action_result = action_result
        self.action_start_date = action_start_date
        self.action_sub_type = action_sub_type
        # This parameter is required.
        self.action_type = action_type
        self.extra = extra
        # This parameter is required.
        self.open_merchant_id = open_merchant_id
        # This parameter is required.
        self.outer_member_id = outer_member_id
        # This parameter is required.
        self.plat_form_type = plat_form_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_duration is not None:
            result['ActionDuration'] = self.action_duration
        if self.action_end_date is not None:
            result['ActionEndDate'] = self.action_end_date
        if self.action_result is not None:
            result['ActionResult'] = self.action_result
        if self.action_start_date is not None:
            result['ActionStartDate'] = self.action_start_date
        if self.action_sub_type is not None:
            result['ActionSubType'] = self.action_sub_type
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.extra is not None:
            result['Extra'] = self.extra
        if self.open_merchant_id is not None:
            result['OpenMerchantId'] = self.open_merchant_id
        if self.outer_member_id is not None:
            result['OuterMemberId'] = self.outer_member_id
        if self.plat_form_type is not None:
            result['PlatFormType'] = self.plat_form_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionDuration') is not None:
            self.action_duration = m.get('ActionDuration')
        if m.get('ActionEndDate') is not None:
            self.action_end_date = m.get('ActionEndDate')
        if m.get('ActionResult') is not None:
            self.action_result = m.get('ActionResult')
        if m.get('ActionStartDate') is not None:
            self.action_start_date = m.get('ActionStartDate')
        if m.get('ActionSubType') is not None:
            self.action_sub_type = m.get('ActionSubType')
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        if m.get('OpenMerchantId') is not None:
            self.open_merchant_id = m.get('OpenMerchantId')
        if m.get('OuterMemberId') is not None:
            self.outer_member_id = m.get('OuterMemberId')
        if m.get('PlatFormType') is not None:
            self.plat_form_type = m.get('PlatFormType')
        return self


class SyncMemberBehaviorInfoRequest(TeaModel):
    def __init__(
        self,
        body: SyncMemberBehaviorInfoRequestBody = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = SyncMemberBehaviorInfoRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SyncMemberBehaviorInfoShrinkRequest(TeaModel):
    def __init__(
        self,
        body_shrink: str = None,
    ):
        self.body_shrink = body_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body_shrink is not None:
            result['body'] = self.body_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body_shrink = m.get('body')
        return self


class SyncMemberBehaviorInfoResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SyncMemberBehaviorInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SyncMemberBehaviorInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = SyncMemberBehaviorInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


