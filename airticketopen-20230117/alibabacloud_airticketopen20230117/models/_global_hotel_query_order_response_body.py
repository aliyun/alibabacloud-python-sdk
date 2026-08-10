# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_airticketopen20230117 import models as main_models
from darabonba.model import DaraModel

class GlobalHotelQueryOrderResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GlobalHotelQueryOrderResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
        tracer_id: str = None,
    ):
        # The business data.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # The unique ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success
        # TracerId
        self.tracer_id = tracer_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.tracer_id is not None:
            result['TracerId'] = self.tracer_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GlobalHotelQueryOrderResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TracerId') is not None:
            self.tracer_id = m.get('TracerId')

        return self

class GlobalHotelQueryOrderResponseBodyData(DaraModel):
    def __init__(
        self,
        buyer_id: str = None,
        external_order_no: str = None,
        gmt_create: int = None,
        item_info: main_models.GlobalHotelQueryOrderResponseBodyDataItemInfo = None,
        order_no: str = None,
        payment: main_models.GlobalHotelQueryOrderResponseBodyDataPayment = None,
        refund_orders: List[main_models.GlobalHotelQueryOrderResponseBodyDataRefundOrders] = None,
        room_stays: List[main_models.GlobalHotelQueryOrderResponseBodyDataRoomStays] = None,
        sales_channel: str = None,
        status: str = None,
        tracer_id: str = None,
    ):
        # The buyer ID.
        self.buyer_id = buyer_id
        # The external order number of the buyer.
        self.external_order_no = external_order_no
        # The creation time in UTC millisecond timestamp.
        self.gmt_create = gmt_create
        # The item information.
        self.item_info = item_info
        # The order number.
        self.order_no = order_no
        # The payment information.
        self.payment = payment
        # The list of refund orders.
        self.refund_orders = refund_orders
        # The list of room stays.
        self.room_stays = room_stays
        # The sales channel.
        self.sales_channel = sales_channel
        # The unified order status.
        self.status = status
        # TracerId
        self.tracer_id = tracer_id

    def validate(self):
        if self.item_info:
            self.item_info.validate()
        if self.payment:
            self.payment.validate()
        if self.refund_orders:
            for v1 in self.refund_orders:
                 if v1:
                    v1.validate()
        if self.room_stays:
            for v1 in self.room_stays:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.buyer_id is not None:
            result['BuyerId'] = self.buyer_id

        if self.external_order_no is not None:
            result['ExternalOrderNo'] = self.external_order_no

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.item_info is not None:
            result['ItemInfo'] = self.item_info.to_map()

        if self.order_no is not None:
            result['OrderNo'] = self.order_no

        if self.payment is not None:
            result['Payment'] = self.payment.to_map()

        result['RefundOrders'] = []
        if self.refund_orders is not None:
            for k1 in self.refund_orders:
                result['RefundOrders'].append(k1.to_map() if k1 else None)

        result['RoomStays'] = []
        if self.room_stays is not None:
            for k1 in self.room_stays:
                result['RoomStays'].append(k1.to_map() if k1 else None)

        if self.sales_channel is not None:
            result['SalesChannel'] = self.sales_channel

        if self.status is not None:
            result['Status'] = self.status

        if self.tracer_id is not None:
            result['TracerId'] = self.tracer_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuyerId') is not None:
            self.buyer_id = m.get('BuyerId')

        if m.get('ExternalOrderNo') is not None:
            self.external_order_no = m.get('ExternalOrderNo')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('ItemInfo') is not None:
            temp_model = main_models.GlobalHotelQueryOrderResponseBodyDataItemInfo()
            self.item_info = temp_model.from_map(m.get('ItemInfo'))

        if m.get('OrderNo') is not None:
            self.order_no = m.get('OrderNo')

        if m.get('Payment') is not None:
            temp_model = main_models.GlobalHotelQueryOrderResponseBodyDataPayment()
            self.payment = temp_model.from_map(m.get('Payment'))

        self.refund_orders = []
        if m.get('RefundOrders') is not None:
            for k1 in m.get('RefundOrders'):
                temp_model = main_models.GlobalHotelQueryOrderResponseBodyDataRefundOrders()
                self.refund_orders.append(temp_model.from_map(k1))

        self.room_stays = []
        if m.get('RoomStays') is not None:
            for k1 in m.get('RoomStays'):
                temp_model = main_models.GlobalHotelQueryOrderResponseBodyDataRoomStays()
                self.room_stays.append(temp_model.from_map(k1))

        if m.get('SalesChannel') is not None:
            self.sales_channel = m.get('SalesChannel')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TracerId') is not None:
            self.tracer_id = m.get('TracerId')

        return self

class GlobalHotelQueryOrderResponseBodyDataRoomStays(DaraModel):
    def __init__(
        self,
        confirmation_id: str = None,
        guests: List[main_models.GlobalHotelQueryOrderResponseBodyDataRoomStaysGuests] = None,
        room_index: int = None,
        status: str = None,
    ):
        # The room confirmation ID.
        self.confirmation_id = confirmation_id
        # The list of guests.
        self.guests = guests
        # The room index, starting from 1.
        self.room_index = room_index
        # The delivery status. Valid values: PENDING_CHECKIN, CHECKED_IN, CHECKED_OUT, and CANCELLED. The value is null before the delivery is created.
        self.status = status

    def validate(self):
        if self.guests:
            for v1 in self.guests:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.confirmation_id is not None:
            result['ConfirmationId'] = self.confirmation_id

        result['Guests'] = []
        if self.guests is not None:
            for k1 in self.guests:
                result['Guests'].append(k1.to_map() if k1 else None)

        if self.room_index is not None:
            result['RoomIndex'] = self.room_index

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfirmationId') is not None:
            self.confirmation_id = m.get('ConfirmationId')

        self.guests = []
        if m.get('Guests') is not None:
            for k1 in m.get('Guests'):
                temp_model = main_models.GlobalHotelQueryOrderResponseBodyDataRoomStaysGuests()
                self.guests.append(temp_model.from_map(k1))

        if m.get('RoomIndex') is not None:
            self.room_index = m.get('RoomIndex')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GlobalHotelQueryOrderResponseBodyDataRoomStaysGuests(DaraModel):
    def __init__(
        self,
        first_name: str = None,
        last_name: str = None,
        tracer_id: str = None,
    ):
        # The first name of the guest.
        self.first_name = first_name
        # The last name of the guest.
        self.last_name = last_name
        # TraceId
        self.tracer_id = tracer_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.first_name is not None:
            result['FirstName'] = self.first_name

        if self.last_name is not None:
            result['LastName'] = self.last_name

        if self.tracer_id is not None:
            result['TracerId'] = self.tracer_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FirstName') is not None:
            self.first_name = m.get('FirstName')

        if m.get('LastName') is not None:
            self.last_name = m.get('LastName')

        if m.get('TracerId') is not None:
            self.tracer_id = m.get('TracerId')

        return self

class GlobalHotelQueryOrderResponseBodyDataRefundOrders(DaraModel):
    def __init__(
        self,
        gmt_create: int = None,
        refund_transaction_id: str = None,
        reject_reason: str = None,
        sell_refund_order_no: str = None,
        status: str = None,
        total_penalty_amount: main_models.GlobalHotelQueryOrderResponseBodyDataRefundOrdersTotalPenaltyAmount = None,
        total_refund_amount: main_models.GlobalHotelQueryOrderResponseBodyDataRefundOrdersTotalRefundAmount = None,
    ):
        # The creation time of the refund order, in UTC millisecond timestamp.
        self.gmt_create = gmt_create
        # The refund transaction ID.
        self.refund_transaction_id = refund_transaction_id
        # The reason for rejection.
        self.reject_reason = reject_reason
        # The external refund order number.
        self.sell_refund_order_no = sell_refund_order_no
        # The unified refund status.
        self.status = status
        # The penalty amount on the sales side.
        self.total_penalty_amount = total_penalty_amount
        # The actual refund amount.
        self.total_refund_amount = total_refund_amount

    def validate(self):
        if self.total_penalty_amount:
            self.total_penalty_amount.validate()
        if self.total_refund_amount:
            self.total_refund_amount.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.refund_transaction_id is not None:
            result['RefundTransactionId'] = self.refund_transaction_id

        if self.reject_reason is not None:
            result['RejectReason'] = self.reject_reason

        if self.sell_refund_order_no is not None:
            result['SellRefundOrderNo'] = self.sell_refund_order_no

        if self.status is not None:
            result['Status'] = self.status

        if self.total_penalty_amount is not None:
            result['TotalPenaltyAmount'] = self.total_penalty_amount.to_map()

        if self.total_refund_amount is not None:
            result['TotalRefundAmount'] = self.total_refund_amount.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('RefundTransactionId') is not None:
            self.refund_transaction_id = m.get('RefundTransactionId')

        if m.get('RejectReason') is not None:
            self.reject_reason = m.get('RejectReason')

        if m.get('SellRefundOrderNo') is not None:
            self.sell_refund_order_no = m.get('SellRefundOrderNo')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TotalPenaltyAmount') is not None:
            temp_model = main_models.GlobalHotelQueryOrderResponseBodyDataRefundOrdersTotalPenaltyAmount()
            self.total_penalty_amount = temp_model.from_map(m.get('TotalPenaltyAmount'))

        if m.get('TotalRefundAmount') is not None:
            temp_model = main_models.GlobalHotelQueryOrderResponseBodyDataRefundOrdersTotalRefundAmount()
            self.total_refund_amount = temp_model.from_map(m.get('TotalRefundAmount'))

        return self

class GlobalHotelQueryOrderResponseBodyDataRefundOrdersTotalRefundAmount(DaraModel):
    def __init__(
        self,
        amount: str = None,
        currency: str = None,
        tracer_id: str = None,
    ):
        # The amount in the smallest currency unit.
        self.amount = amount
        # The currency code in ISO 4217 format.
        self.currency = currency
        # TraceId
        self.tracer_id = tracer_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.currency is not None:
            result['Currency'] = self.currency

        if self.tracer_id is not None:
            result['TracerId'] = self.tracer_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('TracerId') is not None:
            self.tracer_id = m.get('TracerId')

        return self

class GlobalHotelQueryOrderResponseBodyDataRefundOrdersTotalPenaltyAmount(DaraModel):
    def __init__(
        self,
        amount: str = None,
        currency: str = None,
        tracer_id: str = None,
    ):
        # The amount in the smallest currency unit.
        self.amount = amount
        # The currency code in ISO 4217 format.
        self.currency = currency
        # TraceId
        self.tracer_id = tracer_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.currency is not None:
            result['Currency'] = self.currency

        if self.tracer_id is not None:
            result['TracerId'] = self.tracer_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('TracerId') is not None:
            self.tracer_id = m.get('TracerId')

        return self

class GlobalHotelQueryOrderResponseBodyDataPayment(DaraModel):
    def __init__(
        self,
        amount: main_models.GlobalHotelQueryOrderResponseBodyDataPaymentAmount = None,
        gmt_paid: int = None,
        payment_method: str = None,
        payment_transaction_id: str = None,
    ):
        # The payment amount.
        self.amount = amount
        # The payment completion time in UTC millisecond timestamp.
        self.gmt_paid = gmt_paid
        # The payment method.
        self.payment_method = payment_method
        # The payment transaction ID.
        self.payment_transaction_id = payment_transaction_id

    def validate(self):
        if self.amount:
            self.amount.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount.to_map()

        if self.gmt_paid is not None:
            result['GmtPaid'] = self.gmt_paid

        if self.payment_method is not None:
            result['PaymentMethod'] = self.payment_method

        if self.payment_transaction_id is not None:
            result['PaymentTransactionId'] = self.payment_transaction_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            temp_model = main_models.GlobalHotelQueryOrderResponseBodyDataPaymentAmount()
            self.amount = temp_model.from_map(m.get('Amount'))

        if m.get('GmtPaid') is not None:
            self.gmt_paid = m.get('GmtPaid')

        if m.get('PaymentMethod') is not None:
            self.payment_method = m.get('PaymentMethod')

        if m.get('PaymentTransactionId') is not None:
            self.payment_transaction_id = m.get('PaymentTransactionId')

        return self

class GlobalHotelQueryOrderResponseBodyDataPaymentAmount(DaraModel):
    def __init__(
        self,
        amount: str = None,
        currency: str = None,
        tracer_id: str = None,
    ):
        # The amount in the smallest currency unit.
        self.amount = amount
        # The currency code in ISO 4217 format.
        self.currency = currency
        # TracerId
        self.tracer_id = tracer_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.currency is not None:
            result['Currency'] = self.currency

        if self.tracer_id is not None:
            result['TracerId'] = self.tracer_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('TracerId') is not None:
            self.tracer_id = m.get('TracerId')

        return self

class GlobalHotelQueryOrderResponseBodyDataItemInfo(DaraModel):
    def __init__(
        self,
        cancel_policy: main_models.GlobalHotelQueryOrderResponseBodyDataItemInfoCancelPolicy = None,
        check_in: str = None,
        check_in_number: int = None,
        check_out: str = None,
        daily_prices: List[main_models.GlobalHotelQueryOrderResponseBodyDataItemInfoDailyPrices] = None,
        meal: main_models.GlobalHotelQueryOrderResponseBodyDataItemInfoMeal = None,
        room_count: int = None,
        selling_total_price: main_models.GlobalHotelQueryOrderResponseBodyDataItemInfoSellingTotalPrice = None,
    ):
        # The cancellation policy.
        self.cancel_policy = cancel_policy
        # The check-in date in yyyy-MM-dd format.
        self.check_in = check_in
        # The number of guests checking in.
        self.check_in_number = check_in_number
        # The check-out date in yyyy-MM-dd format.
        self.check_out = check_out
        # The list of nightly rates.
        self.daily_prices = daily_prices
        # The meal information.
        self.meal = meal
        # The number of rooms.
        self.room_count = room_count
        # The total selling price.
        self.selling_total_price = selling_total_price

    def validate(self):
        if self.cancel_policy:
            self.cancel_policy.validate()
        if self.daily_prices:
            for v1 in self.daily_prices:
                 if v1:
                    v1.validate()
        if self.meal:
            self.meal.validate()
        if self.selling_total_price:
            self.selling_total_price.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cancel_policy is not None:
            result['CancelPolicy'] = self.cancel_policy.to_map()

        if self.check_in is not None:
            result['CheckIn'] = self.check_in

        if self.check_in_number is not None:
            result['CheckInNumber'] = self.check_in_number

        if self.check_out is not None:
            result['CheckOut'] = self.check_out

        result['DailyPrices'] = []
        if self.daily_prices is not None:
            for k1 in self.daily_prices:
                result['DailyPrices'].append(k1.to_map() if k1 else None)

        if self.meal is not None:
            result['Meal'] = self.meal.to_map()

        if self.room_count is not None:
            result['RoomCount'] = self.room_count

        if self.selling_total_price is not None:
            result['SellingTotalPrice'] = self.selling_total_price.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CancelPolicy') is not None:
            temp_model = main_models.GlobalHotelQueryOrderResponseBodyDataItemInfoCancelPolicy()
            self.cancel_policy = temp_model.from_map(m.get('CancelPolicy'))

        if m.get('CheckIn') is not None:
            self.check_in = m.get('CheckIn')

        if m.get('CheckInNumber') is not None:
            self.check_in_number = m.get('CheckInNumber')

        if m.get('CheckOut') is not None:
            self.check_out = m.get('CheckOut')

        self.daily_prices = []
        if m.get('DailyPrices') is not None:
            for k1 in m.get('DailyPrices'):
                temp_model = main_models.GlobalHotelQueryOrderResponseBodyDataItemInfoDailyPrices()
                self.daily_prices.append(temp_model.from_map(k1))

        if m.get('Meal') is not None:
            temp_model = main_models.GlobalHotelQueryOrderResponseBodyDataItemInfoMeal()
            self.meal = temp_model.from_map(m.get('Meal'))

        if m.get('RoomCount') is not None:
            self.room_count = m.get('RoomCount')

        if m.get('SellingTotalPrice') is not None:
            temp_model = main_models.GlobalHotelQueryOrderResponseBodyDataItemInfoSellingTotalPrice()
            self.selling_total_price = temp_model.from_map(m.get('SellingTotalPrice'))

        return self

class GlobalHotelQueryOrderResponseBodyDataItemInfoSellingTotalPrice(DaraModel):
    def __init__(
        self,
        amount: str = None,
        currency: str = None,
        tracer_id: str = None,
    ):
        # The amount in the smallest currency unit.
        self.amount = amount
        # The currency code in ISO 4217 format.
        self.currency = currency
        # TracerId
        self.tracer_id = tracer_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.currency is not None:
            result['Currency'] = self.currency

        if self.tracer_id is not None:
            result['TracerId'] = self.tracer_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('TracerId') is not None:
            self.tracer_id = m.get('TracerId')

        return self

class GlobalHotelQueryOrderResponseBodyDataItemInfoMeal(DaraModel):
    def __init__(
        self,
        description: str = None,
        meal_type: str = None,
        tracer_id: str = None,
    ):
        # The description.
        self.description = description
        # The meal type.
        self.meal_type = meal_type
        # TracerId
        self.tracer_id = tracer_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.meal_type is not None:
            result['MealType'] = self.meal_type

        if self.tracer_id is not None:
            result['TracerId'] = self.tracer_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('MealType') is not None:
            self.meal_type = m.get('MealType')

        if m.get('TracerId') is not None:
            self.tracer_id = m.get('TracerId')

        return self

class GlobalHotelQueryOrderResponseBodyDataItemInfoDailyPrices(DaraModel):
    def __init__(
        self,
        date: str = None,
        price: main_models.GlobalHotelQueryOrderResponseBodyDataItemInfoDailyPricesPrice = None,
    ):
        # LocalDate
        self.date = date
        # The price.
        self.price = price

    def validate(self):
        if self.price:
            self.price.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date is not None:
            result['Date'] = self.date

        if self.price is not None:
            result['Price'] = self.price.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')

        if m.get('Price') is not None:
            temp_model = main_models.GlobalHotelQueryOrderResponseBodyDataItemInfoDailyPricesPrice()
            self.price = temp_model.from_map(m.get('Price'))

        return self

class GlobalHotelQueryOrderResponseBodyDataItemInfoDailyPricesPrice(DaraModel):
    def __init__(
        self,
        cent: int = None,
        currency: main_models.GlobalHotelQueryOrderResponseBodyDataItemInfoDailyPricesPriceCurrency = None,
    ):
        # cent
        self.cent = cent
        # The currency.
        self.currency = currency

    def validate(self):
        if self.currency:
            self.currency.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cent is not None:
            result['Cent'] = self.cent

        if self.currency is not None:
            result['Currency'] = self.currency.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cent') is not None:
            self.cent = m.get('Cent')

        if m.get('Currency') is not None:
            temp_model = main_models.GlobalHotelQueryOrderResponseBodyDataItemInfoDailyPricesPriceCurrency()
            self.currency = temp_model.from_map(m.get('Currency'))

        return self

class GlobalHotelQueryOrderResponseBodyDataItemInfoDailyPricesPriceCurrency(DaraModel):
    def __init__(
        self,
        currency_code: str = None,
        default_fraction_digits: int = None,
        numeric_code: int = None,
    ):
        # The currency code.
        self.currency_code = currency_code
        # DefaultFractionDigits
        self.default_fraction_digits = default_fraction_digits
        # NumericCode
        self.numeric_code = numeric_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.currency_code is not None:
            result['CurrencyCode'] = self.currency_code

        if self.default_fraction_digits is not None:
            result['DefaultFractionDigits'] = self.default_fraction_digits

        if self.numeric_code is not None:
            result['NumericCode'] = self.numeric_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrencyCode') is not None:
            self.currency_code = m.get('CurrencyCode')

        if m.get('DefaultFractionDigits') is not None:
            self.default_fraction_digits = m.get('DefaultFractionDigits')

        if m.get('NumericCode') is not None:
            self.numeric_code = m.get('NumericCode')

        return self

class GlobalHotelQueryOrderResponseBodyDataItemInfoCancelPolicy(DaraModel):
    def __init__(
        self,
        penalties: List[main_models.GlobalHotelQueryOrderResponseBodyDataItemInfoCancelPolicyPenalties] = None,
        policy_type: str = None,
        tracer_id: str = None,
    ):
        # The list of cancellation penalties.
        self.penalties = penalties
        # The cancellation policy type.
        self.policy_type = policy_type
        # TracerId
        self.tracer_id = tracer_id

    def validate(self):
        if self.penalties:
            for v1 in self.penalties:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Penalties'] = []
        if self.penalties is not None:
            for k1 in self.penalties:
                result['Penalties'].append(k1.to_map() if k1 else None)

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        if self.tracer_id is not None:
            result['TracerId'] = self.tracer_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.penalties = []
        if m.get('Penalties') is not None:
            for k1 in m.get('Penalties'):
                temp_model = main_models.GlobalHotelQueryOrderResponseBodyDataItemInfoCancelPolicyPenalties()
                self.penalties.append(temp_model.from_map(k1))

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        if m.get('TracerId') is not None:
            self.tracer_id = m.get('TracerId')

        return self

class GlobalHotelQueryOrderResponseBodyDataItemInfoCancelPolicyPenalties(DaraModel):
    def __init__(
        self,
        currency: str = None,
        end: int = None,
        penalty_type: str = None,
        penalty_value: str = None,
        start: int = None,
        tracer_id: str = None,
    ):
        # The currency code. This parameter is valid only when the penalty type is AMOUNT.
        self.currency = currency
        # The effective end time in UTC millisecond timestamp.
        self.end = end
        # The penalty type.
        self.penalty_type = penalty_type
        # The penalty value, which can be a percentage, amount, or number of nights.
        self.penalty_value = penalty_value
        # The effective start time in UTC millisecond timestamp.
        self.start = start
        # TracerId
        self.tracer_id = tracer_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.currency is not None:
            result['Currency'] = self.currency

        if self.end is not None:
            result['End'] = self.end

        if self.penalty_type is not None:
            result['PenaltyType'] = self.penalty_type

        if self.penalty_value is not None:
            result['PenaltyValue'] = self.penalty_value

        if self.start is not None:
            result['Start'] = self.start

        if self.tracer_id is not None:
            result['TracerId'] = self.tracer_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('End') is not None:
            self.end = m.get('End')

        if m.get('PenaltyType') is not None:
            self.penalty_type = m.get('PenaltyType')

        if m.get('PenaltyValue') is not None:
            self.penalty_value = m.get('PenaltyValue')

        if m.get('Start') is not None:
            self.start = m.get('Start')

        if m.get('TracerId') is not None:
            self.tracer_id = m.get('TracerId')

        return self

