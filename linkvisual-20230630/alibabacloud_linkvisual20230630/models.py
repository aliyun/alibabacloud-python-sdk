# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class BindStorageOrderRequest(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        enable_default_plan: bool = None,
        event_record_duration: int = None,
        event_record_prolong: bool = None,
        iot_id: str = None,
        max_record_file_duration: int = None,
        order_id: str = None,
        pre_record_duration: int = None,
        product_key: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.device_name = device_name
        self.enable_default_plan = enable_default_plan
        self.event_record_duration = event_record_duration
        self.event_record_prolong = event_record_prolong
        self.iot_id = iot_id
        self.max_record_file_duration = max_record_file_duration
        self.order_id = order_id
        self.pre_record_duration = pre_record_duration
        self.product_key = product_key
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.enable_default_plan is not None:
            result['EnableDefaultPlan'] = self.enable_default_plan
        if self.event_record_duration is not None:
            result['EventRecordDuration'] = self.event_record_duration
        if self.event_record_prolong is not None:
            result['EventRecordProlong'] = self.event_record_prolong
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.max_record_file_duration is not None:
            result['MaxRecordFileDuration'] = self.max_record_file_duration
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.pre_record_duration is not None:
            result['PreRecordDuration'] = self.pre_record_duration
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('EnableDefaultPlan') is not None:
            self.enable_default_plan = m.get('EnableDefaultPlan')
        if m.get('EventRecordDuration') is not None:
            self.event_record_duration = m.get('EventRecordDuration')
        if m.get('EventRecordProlong') is not None:
            self.event_record_prolong = m.get('EventRecordProlong')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('MaxRecordFileDuration') is not None:
            self.max_record_file_duration = m.get('MaxRecordFileDuration')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PreRecordDuration') is not None:
            self.pre_record_duration = m.get('PreRecordDuration')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class BindStorageOrderResponseBodyData(TeaModel):
    def __init__(
        self,
        commodity_code: str = None,
        copies: int = None,
        end_time: str = None,
        end_time_utc: str = None,
        identity_id: str = None,
        iot_id: str = None,
        order_id: str = None,
        order_type: int = None,
        out_order_no: str = None,
        payment_status: int = None,
        pre_consume: int = None,
        price: str = None,
        record_type: int = None,
        specification: str = None,
        start_time: str = None,
        start_time_utc: str = None,
        status: int = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.commodity_code = commodity_code
        self.copies = copies
        self.end_time = end_time
        self.end_time_utc = end_time_utc
        self.identity_id = identity_id
        self.iot_id = iot_id
        self.order_id = order_id
        self.order_type = order_type
        self.out_order_no = out_order_no
        self.payment_status = payment_status
        self.pre_consume = pre_consume
        self.price = price
        self.record_type = record_type
        self.specification = specification
        self.start_time = start_time
        self.start_time_utc = start_time_utc
        self.status = status
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.copies is not None:
            result['Copies'] = self.copies
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.end_time_utc is not None:
            result['EndTimeUTC'] = self.end_time_utc
        if self.identity_id is not None:
            result['IdentityId'] = self.identity_id
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.out_order_no is not None:
            result['OutOrderNo'] = self.out_order_no
        if self.payment_status is not None:
            result['PaymentStatus'] = self.payment_status
        if self.pre_consume is not None:
            result['PreConsume'] = self.pre_consume
        if self.price is not None:
            result['Price'] = self.price
        if self.record_type is not None:
            result['RecordType'] = self.record_type
        if self.specification is not None:
            result['Specification'] = self.specification
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.start_time_utc is not None:
            result['StartTimeUTC'] = self.start_time_utc
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('Copies') is not None:
            self.copies = m.get('Copies')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EndTimeUTC') is not None:
            self.end_time_utc = m.get('EndTimeUTC')
        if m.get('IdentityId') is not None:
            self.identity_id = m.get('IdentityId')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('OutOrderNo') is not None:
            self.out_order_no = m.get('OutOrderNo')
        if m.get('PaymentStatus') is not None:
            self.payment_status = m.get('PaymentStatus')
        if m.get('PreConsume') is not None:
            self.pre_consume = m.get('PreConsume')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StartTimeUTC') is not None:
            self.start_time_utc = m.get('StartTimeUTC')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class BindStorageOrderResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: BindStorageOrderResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = BindStorageOrderResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BindStorageOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BindStorageOrderResponseBody = None,
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
            temp_model = BindStorageOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckFreeStorageValidRequest(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        iot_id: str = None,
        product_key: str = None,
    ):
        self.device_name = device_name
        self.iot_id = iot_id
        self.product_key = product_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class CheckFreeStorageValidResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
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
        if self.code is not None:
            result['Code'] = self.code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckFreeStorageValidResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckFreeStorageValidResponseBody = None,
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
            temp_model = CheckFreeStorageValidResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConsumeFreeStorageRequest(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        enable_default_plan: bool = None,
        event_record_duration: int = None,
        event_record_prolong: bool = None,
        immediate_use: bool = None,
        iot_id: str = None,
        pre_record_duration: int = None,
        product_key: str = None,
        quota: int = None,
    ):
        self.device_name = device_name
        self.enable_default_plan = enable_default_plan
        self.event_record_duration = event_record_duration
        self.event_record_prolong = event_record_prolong
        self.immediate_use = immediate_use
        self.iot_id = iot_id
        self.pre_record_duration = pre_record_duration
        self.product_key = product_key
        self.quota = quota

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.enable_default_plan is not None:
            result['EnableDefaultPlan'] = self.enable_default_plan
        if self.event_record_duration is not None:
            result['EventRecordDuration'] = self.event_record_duration
        if self.event_record_prolong is not None:
            result['EventRecordProlong'] = self.event_record_prolong
        if self.immediate_use is not None:
            result['ImmediateUse'] = self.immediate_use
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.pre_record_duration is not None:
            result['PreRecordDuration'] = self.pre_record_duration
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.quota is not None:
            result['Quota'] = self.quota
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('EnableDefaultPlan') is not None:
            self.enable_default_plan = m.get('EnableDefaultPlan')
        if m.get('EventRecordDuration') is not None:
            self.event_record_duration = m.get('EventRecordDuration')
        if m.get('EventRecordProlong') is not None:
            self.event_record_prolong = m.get('EventRecordProlong')
        if m.get('ImmediateUse') is not None:
            self.immediate_use = m.get('ImmediateUse')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('PreRecordDuration') is not None:
            self.pre_record_duration = m.get('PreRecordDuration')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('Quota') is not None:
            self.quota = m.get('Quota')
        return self


class ConsumeFreeStorageResponseBodyData(TeaModel):
    def __init__(
        self,
        consumed: int = None,
        end_time: str = None,
        end_time_utc: str = None,
        expired: int = None,
        lifecycle: int = None,
        months: int = None,
        remain_quota: int = None,
        start_time: str = None,
        start_time_utc: str = None,
        type: int = None,
    ):
        self.consumed = consumed
        self.end_time = end_time
        self.end_time_utc = end_time_utc
        self.expired = expired
        self.lifecycle = lifecycle
        self.months = months
        self.remain_quota = remain_quota
        self.start_time = start_time
        self.start_time_utc = start_time_utc
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumed is not None:
            result['Consumed'] = self.consumed
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.end_time_utc is not None:
            result['EndTimeUTC'] = self.end_time_utc
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.lifecycle is not None:
            result['Lifecycle'] = self.lifecycle
        if self.months is not None:
            result['Months'] = self.months
        if self.remain_quota is not None:
            result['RemainQuota'] = self.remain_quota
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.start_time_utc is not None:
            result['StartTimeUTC'] = self.start_time_utc
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Consumed') is not None:
            self.consumed = m.get('Consumed')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EndTimeUTC') is not None:
            self.end_time_utc = m.get('EndTimeUTC')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('Lifecycle') is not None:
            self.lifecycle = m.get('Lifecycle')
        if m.get('Months') is not None:
            self.months = m.get('Months')
        if m.get('RemainQuota') is not None:
            self.remain_quota = m.get('RemainQuota')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StartTimeUTC') is not None:
            self.start_time_utc = m.get('StartTimeUTC')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ConsumeFreeStorageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ConsumeFreeStorageResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = ConsumeFreeStorageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ConsumeFreeStorageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConsumeFreeStorageResponseBody = None,
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
            temp_model = ConsumeFreeStorageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAndPayStorageOrderRequest(TeaModel):
    def __init__(
        self,
        commodity_code: str = None,
        copies: int = None,
        device_name: str = None,
        device_no_owner: bool = None,
        enable_default_plan: bool = None,
        event_record_duration: int = None,
        event_record_prolong: bool = None,
        immediate_use: bool = None,
        iot_id: str = None,
        max_record_file_duration: int = None,
        pre_record_duration: int = None,
        product_key: str = None,
        specification: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.commodity_code = commodity_code
        self.copies = copies
        self.device_name = device_name
        self.device_no_owner = device_no_owner
        self.enable_default_plan = enable_default_plan
        self.event_record_duration = event_record_duration
        self.event_record_prolong = event_record_prolong
        self.immediate_use = immediate_use
        self.iot_id = iot_id
        self.max_record_file_duration = max_record_file_duration
        self.pre_record_duration = pre_record_duration
        self.product_key = product_key
        self.specification = specification
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.copies is not None:
            result['Copies'] = self.copies
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.device_no_owner is not None:
            result['DeviceNoOwner'] = self.device_no_owner
        if self.enable_default_plan is not None:
            result['EnableDefaultPlan'] = self.enable_default_plan
        if self.event_record_duration is not None:
            result['EventRecordDuration'] = self.event_record_duration
        if self.event_record_prolong is not None:
            result['EventRecordProlong'] = self.event_record_prolong
        if self.immediate_use is not None:
            result['ImmediateUse'] = self.immediate_use
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.max_record_file_duration is not None:
            result['MaxRecordFileDuration'] = self.max_record_file_duration
        if self.pre_record_duration is not None:
            result['PreRecordDuration'] = self.pre_record_duration
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.specification is not None:
            result['Specification'] = self.specification
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('Copies') is not None:
            self.copies = m.get('Copies')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('DeviceNoOwner') is not None:
            self.device_no_owner = m.get('DeviceNoOwner')
        if m.get('EnableDefaultPlan') is not None:
            self.enable_default_plan = m.get('EnableDefaultPlan')
        if m.get('EventRecordDuration') is not None:
            self.event_record_duration = m.get('EventRecordDuration')
        if m.get('EventRecordProlong') is not None:
            self.event_record_prolong = m.get('EventRecordProlong')
        if m.get('ImmediateUse') is not None:
            self.immediate_use = m.get('ImmediateUse')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('MaxRecordFileDuration') is not None:
            self.max_record_file_duration = m.get('MaxRecordFileDuration')
        if m.get('PreRecordDuration') is not None:
            self.pre_record_duration = m.get('PreRecordDuration')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class CreateAndPayStorageOrderResponseBodyData(TeaModel):
    def __init__(
        self,
        commodity_code: str = None,
        copies: int = None,
        end_time: str = None,
        end_time_utc: str = None,
        identity_id: str = None,
        iot_id: str = None,
        order_id: str = None,
        order_type: int = None,
        out_order_no: str = None,
        payment_status: int = None,
        pre_consume: int = None,
        price: str = None,
        record_type: int = None,
        specification: str = None,
        start_time: str = None,
        start_time_utc: str = None,
        status: int = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.commodity_code = commodity_code
        self.copies = copies
        self.end_time = end_time
        self.end_time_utc = end_time_utc
        self.identity_id = identity_id
        self.iot_id = iot_id
        self.order_id = order_id
        self.order_type = order_type
        self.out_order_no = out_order_no
        self.payment_status = payment_status
        self.pre_consume = pre_consume
        self.price = price
        self.record_type = record_type
        self.specification = specification
        self.start_time = start_time
        self.start_time_utc = start_time_utc
        self.status = status
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.copies is not None:
            result['Copies'] = self.copies
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.end_time_utc is not None:
            result['EndTimeUTC'] = self.end_time_utc
        if self.identity_id is not None:
            result['IdentityId'] = self.identity_id
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.out_order_no is not None:
            result['OutOrderNo'] = self.out_order_no
        if self.payment_status is not None:
            result['PaymentStatus'] = self.payment_status
        if self.pre_consume is not None:
            result['PreConsume'] = self.pre_consume
        if self.price is not None:
            result['Price'] = self.price
        if self.record_type is not None:
            result['RecordType'] = self.record_type
        if self.specification is not None:
            result['Specification'] = self.specification
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.start_time_utc is not None:
            result['StartTimeUTC'] = self.start_time_utc
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('Copies') is not None:
            self.copies = m.get('Copies')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EndTimeUTC') is not None:
            self.end_time_utc = m.get('EndTimeUTC')
        if m.get('IdentityId') is not None:
            self.identity_id = m.get('IdentityId')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('OutOrderNo') is not None:
            self.out_order_no = m.get('OutOrderNo')
        if m.get('PaymentStatus') is not None:
            self.payment_status = m.get('PaymentStatus')
        if m.get('PreConsume') is not None:
            self.pre_consume = m.get('PreConsume')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StartTimeUTC') is not None:
            self.start_time_utc = m.get('StartTimeUTC')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class CreateAndPayStorageOrderResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateAndPayStorageOrderResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = CreateAndPayStorageOrderResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateAndPayStorageOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAndPayStorageOrderResponseBody = None,
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
            temp_model = CreateAndPayStorageOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableFreeStorageRequest(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        iot_id: str = None,
        product_key: str = None,
    ):
        self.device_name = device_name
        self.iot_id = iot_id
        self.product_key = product_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class EnableFreeStorageResponseBodyData(TeaModel):
    def __init__(
        self,
        consumed: int = None,
        end_time: str = None,
        end_time_utc: str = None,
        expired: int = None,
        lifecycle: int = None,
        months: int = None,
        remain_quota: int = None,
        start_time: str = None,
        start_time_utc: str = None,
        type: int = None,
    ):
        self.consumed = consumed
        self.end_time = end_time
        self.end_time_utc = end_time_utc
        self.expired = expired
        self.lifecycle = lifecycle
        self.months = months
        self.remain_quota = remain_quota
        self.start_time = start_time
        self.start_time_utc = start_time_utc
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumed is not None:
            result['Consumed'] = self.consumed
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.end_time_utc is not None:
            result['EndTimeUTC'] = self.end_time_utc
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.lifecycle is not None:
            result['Lifecycle'] = self.lifecycle
        if self.months is not None:
            result['Months'] = self.months
        if self.remain_quota is not None:
            result['RemainQuota'] = self.remain_quota
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.start_time_utc is not None:
            result['StartTimeUTC'] = self.start_time_utc
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Consumed') is not None:
            self.consumed = m.get('Consumed')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EndTimeUTC') is not None:
            self.end_time_utc = m.get('EndTimeUTC')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('Lifecycle') is not None:
            self.lifecycle = m.get('Lifecycle')
        if m.get('Months') is not None:
            self.months = m.get('Months')
        if m.get('RemainQuota') is not None:
            self.remain_quota = m.get('RemainQuota')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StartTimeUTC') is not None:
            self.start_time_utc = m.get('StartTimeUTC')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class EnableFreeStorageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: EnableFreeStorageResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = EnableFreeStorageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EnableFreeStorageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableFreeStorageResponseBody = None,
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
            temp_model = EnableFreeStorageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableStorageOrderRequest(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        iot_id: str = None,
        order_id: str = None,
        product_key: str = None,
    ):
        self.device_name = device_name
        self.iot_id = iot_id
        self.order_id = order_id
        self.product_key = product_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class EnableStorageOrderResponseBodyData(TeaModel):
    def __init__(
        self,
        commodity_code: str = None,
        copies: int = None,
        end_time: str = None,
        end_time_utc: str = None,
        identity_id: str = None,
        iot_id: str = None,
        order_id: str = None,
        order_type: int = None,
        out_order_no: str = None,
        payment_status: int = None,
        pre_consume: int = None,
        price: str = None,
        record_type: int = None,
        specification: str = None,
        start_time: str = None,
        start_time_utc: str = None,
        status: int = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.commodity_code = commodity_code
        self.copies = copies
        self.end_time = end_time
        self.end_time_utc = end_time_utc
        self.identity_id = identity_id
        self.iot_id = iot_id
        self.order_id = order_id
        self.order_type = order_type
        self.out_order_no = out_order_no
        self.payment_status = payment_status
        self.pre_consume = pre_consume
        self.price = price
        self.record_type = record_type
        self.specification = specification
        self.start_time = start_time
        self.start_time_utc = start_time_utc
        self.status = status
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.copies is not None:
            result['Copies'] = self.copies
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.end_time_utc is not None:
            result['EndTimeUTC'] = self.end_time_utc
        if self.identity_id is not None:
            result['IdentityId'] = self.identity_id
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.out_order_no is not None:
            result['OutOrderNo'] = self.out_order_no
        if self.payment_status is not None:
            result['PaymentStatus'] = self.payment_status
        if self.pre_consume is not None:
            result['PreConsume'] = self.pre_consume
        if self.price is not None:
            result['Price'] = self.price
        if self.record_type is not None:
            result['RecordType'] = self.record_type
        if self.specification is not None:
            result['Specification'] = self.specification
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.start_time_utc is not None:
            result['StartTimeUTC'] = self.start_time_utc
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('Copies') is not None:
            self.copies = m.get('Copies')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EndTimeUTC') is not None:
            self.end_time_utc = m.get('EndTimeUTC')
        if m.get('IdentityId') is not None:
            self.identity_id = m.get('IdentityId')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('OutOrderNo') is not None:
            self.out_order_no = m.get('OutOrderNo')
        if m.get('PaymentStatus') is not None:
            self.payment_status = m.get('PaymentStatus')
        if m.get('PreConsume') is not None:
            self.pre_consume = m.get('PreConsume')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StartTimeUTC') is not None:
            self.start_time_utc = m.get('StartTimeUTC')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class EnableStorageOrderResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: EnableStorageOrderResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = EnableStorageOrderResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EnableStorageOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableStorageOrderResponseBody = None,
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
            temp_model = EnableStorageOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FreezeFreeStorageRequest(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        iot_id: str = None,
        product_key: str = None,
    ):
        self.device_name = device_name
        self.iot_id = iot_id
        self.product_key = product_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class FreezeFreeStorageResponseBodyData(TeaModel):
    def __init__(
        self,
        consumed: int = None,
        end_time: str = None,
        end_time_utc: str = None,
        expired: int = None,
        lifecycle: int = None,
        months: int = None,
        remain_quota: int = None,
        start_time: str = None,
        start_time_utc: str = None,
        type: int = None,
    ):
        self.consumed = consumed
        self.end_time = end_time
        self.end_time_utc = end_time_utc
        self.expired = expired
        self.lifecycle = lifecycle
        self.months = months
        self.remain_quota = remain_quota
        self.start_time = start_time
        self.start_time_utc = start_time_utc
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumed is not None:
            result['Consumed'] = self.consumed
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.end_time_utc is not None:
            result['EndTimeUTC'] = self.end_time_utc
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.lifecycle is not None:
            result['Lifecycle'] = self.lifecycle
        if self.months is not None:
            result['Months'] = self.months
        if self.remain_quota is not None:
            result['RemainQuota'] = self.remain_quota
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.start_time_utc is not None:
            result['StartTimeUTC'] = self.start_time_utc
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Consumed') is not None:
            self.consumed = m.get('Consumed')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EndTimeUTC') is not None:
            self.end_time_utc = m.get('EndTimeUTC')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('Lifecycle') is not None:
            self.lifecycle = m.get('Lifecycle')
        if m.get('Months') is not None:
            self.months = m.get('Months')
        if m.get('RemainQuota') is not None:
            self.remain_quota = m.get('RemainQuota')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StartTimeUTC') is not None:
            self.start_time_utc = m.get('StartTimeUTC')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class FreezeFreeStorageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: FreezeFreeStorageResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = FreezeFreeStorageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class FreezeFreeStorageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FreezeFreeStorageResponseBody = None,
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
            temp_model = FreezeFreeStorageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FreezeStorageOrderRequest(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        device_no_owner: bool = None,
        iot_id: str = None,
        order_id: str = None,
        product_key: str = None,
    ):
        self.device_name = device_name
        self.device_no_owner = device_no_owner
        self.iot_id = iot_id
        self.order_id = order_id
        self.product_key = product_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.device_no_owner is not None:
            result['DeviceNoOwner'] = self.device_no_owner
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('DeviceNoOwner') is not None:
            self.device_no_owner = m.get('DeviceNoOwner')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class FreezeStorageOrderResponseBodyData(TeaModel):
    def __init__(
        self,
        commodity_code: str = None,
        copies: int = None,
        end_time: str = None,
        end_time_utc: str = None,
        identity_id: str = None,
        iot_id: str = None,
        order_id: str = None,
        order_type: int = None,
        out_order_no: str = None,
        payment_status: int = None,
        pre_consume: int = None,
        price: str = None,
        record_type: int = None,
        specification: str = None,
        start_time: str = None,
        start_time_utc: str = None,
        status: int = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.commodity_code = commodity_code
        self.copies = copies
        self.end_time = end_time
        self.end_time_utc = end_time_utc
        self.identity_id = identity_id
        self.iot_id = iot_id
        self.order_id = order_id
        self.order_type = order_type
        self.out_order_no = out_order_no
        self.payment_status = payment_status
        self.pre_consume = pre_consume
        self.price = price
        self.record_type = record_type
        self.specification = specification
        self.start_time = start_time
        self.start_time_utc = start_time_utc
        self.status = status
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.copies is not None:
            result['Copies'] = self.copies
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.end_time_utc is not None:
            result['EndTimeUTC'] = self.end_time_utc
        if self.identity_id is not None:
            result['IdentityId'] = self.identity_id
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.out_order_no is not None:
            result['OutOrderNo'] = self.out_order_no
        if self.payment_status is not None:
            result['PaymentStatus'] = self.payment_status
        if self.pre_consume is not None:
            result['PreConsume'] = self.pre_consume
        if self.price is not None:
            result['Price'] = self.price
        if self.record_type is not None:
            result['RecordType'] = self.record_type
        if self.specification is not None:
            result['Specification'] = self.specification
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.start_time_utc is not None:
            result['StartTimeUTC'] = self.start_time_utc
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('Copies') is not None:
            self.copies = m.get('Copies')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EndTimeUTC') is not None:
            self.end_time_utc = m.get('EndTimeUTC')
        if m.get('IdentityId') is not None:
            self.identity_id = m.get('IdentityId')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('OutOrderNo') is not None:
            self.out_order_no = m.get('OutOrderNo')
        if m.get('PaymentStatus') is not None:
            self.payment_status = m.get('PaymentStatus')
        if m.get('PreConsume') is not None:
            self.pre_consume = m.get('PreConsume')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StartTimeUTC') is not None:
            self.start_time_utc = m.get('StartTimeUTC')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class FreezeStorageOrderResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: FreezeStorageOrderResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = FreezeStorageOrderResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class FreezeStorageOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FreezeStorageOrderResponseBody = None,
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
            temp_model = FreezeStorageOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateDeviceRequest(TeaModel):
    def __init__(
        self,
        amount: int = None,
        product_key: str = None,
        project_id: str = None,
    ):
        self.amount = amount
        self.product_key = product_key
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class GenerateDeviceResponseBodyData(TeaModel):
    def __init__(
        self,
        batch_id: str = None,
    ):
        self.batch_id = batch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')
        return self


class GenerateDeviceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GenerateDeviceResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = GenerateDeviceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GenerateDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateDeviceResponseBody = None,
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
            temp_model = GenerateDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateDeviceByBatchIdRequest(TeaModel):
    def __init__(
        self,
        batch_id: str = None,
        product_key: str = None,
        project_id: str = None,
    ):
        self.batch_id = batch_id
        self.product_key = product_key
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class GenerateDeviceByBatchIdResponseBodyData(TeaModel):
    def __init__(
        self,
        batch_id: str = None,
    ):
        self.batch_id = batch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')
        return self


class GenerateDeviceByBatchIdResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GenerateDeviceByBatchIdResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = GenerateDeviceByBatchIdResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GenerateDeviceByBatchIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateDeviceByBatchIdResponseBody = None,
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
            temp_model = GenerateDeviceByBatchIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryBatchStatusRequest(TeaModel):
    def __init__(
        self,
        batch_id: str = None,
        product_key: str = None,
        project_id: str = None,
    ):
        self.batch_id = batch_id
        self.product_key = product_key
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class QueryBatchStatusResponseBodyDataInvalidDetailList(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        error_msg: str = None,
    ):
        self.device_name = device_name
        self.error_msg = error_msg

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        return self


class QueryBatchStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        invalid_detail_list: List[QueryBatchStatusResponseBodyDataInvalidDetailList] = None,
        invalid_list: List[str] = None,
        status: str = None,
        valid_list: List[str] = None,
    ):
        self.invalid_detail_list = invalid_detail_list
        self.invalid_list = invalid_list
        self.status = status
        self.valid_list = valid_list

    def validate(self):
        if self.invalid_detail_list:
            for k in self.invalid_detail_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InvalidDetailList'] = []
        if self.invalid_detail_list is not None:
            for k in self.invalid_detail_list:
                result['InvalidDetailList'].append(k.to_map() if k else None)
        if self.invalid_list is not None:
            result['InvalidList'] = self.invalid_list
        if self.status is not None:
            result['Status'] = self.status
        if self.valid_list is not None:
            result['ValidList'] = self.valid_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.invalid_detail_list = []
        if m.get('InvalidDetailList') is not None:
            for k in m.get('InvalidDetailList'):
                temp_model = QueryBatchStatusResponseBodyDataInvalidDetailList()
                self.invalid_detail_list.append(temp_model.from_map(k))
        if m.get('InvalidList') is not None:
            self.invalid_list = m.get('InvalidList')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ValidList') is not None:
            self.valid_list = m.get('ValidList')
        return self


class QueryBatchStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryBatchStatusResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryBatchStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryBatchStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryBatchStatusResponseBody = None,
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
            temp_model = QueryBatchStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDevicesDownloadUrlRequest(TeaModel):
    def __init__(
        self,
        batch_id: str = None,
        product_key: str = None,
    ):
        self.batch_id = batch_id
        self.product_key = product_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class QueryDevicesDownloadUrlResponseBodyData(TeaModel):
    def __init__(
        self,
        oss_download_url: str = None,
    ):
        self.oss_download_url = oss_download_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss_download_url is not None:
            result['OssDownloadUrl'] = self.oss_download_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OssDownloadUrl') is not None:
            self.oss_download_url = m.get('OssDownloadUrl')
        return self


class QueryDevicesDownloadUrlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryDevicesDownloadUrlResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryDevicesDownloadUrlResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryDevicesDownloadUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryDevicesDownloadUrlResponseBody = None,
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
            temp_model = QueryDevicesDownloadUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryFreeStorageRequest(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        iot_id: str = None,
        product_key: str = None,
    ):
        self.device_name = device_name
        self.iot_id = iot_id
        self.product_key = product_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class QueryFreeStorageResponseBodyData(TeaModel):
    def __init__(
        self,
        consumed: int = None,
        end_time: str = None,
        end_time_utc: str = None,
        expired: int = None,
        lifecycle: int = None,
        months: int = None,
        remain_quota: int = None,
        start_time: str = None,
        start_time_utc: str = None,
        type: int = None,
    ):
        self.consumed = consumed
        self.end_time = end_time
        self.end_time_utc = end_time_utc
        self.expired = expired
        self.lifecycle = lifecycle
        self.months = months
        self.remain_quota = remain_quota
        self.start_time = start_time
        self.start_time_utc = start_time_utc
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumed is not None:
            result['Consumed'] = self.consumed
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.end_time_utc is not None:
            result['EndTimeUTC'] = self.end_time_utc
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.lifecycle is not None:
            result['Lifecycle'] = self.lifecycle
        if self.months is not None:
            result['Months'] = self.months
        if self.remain_quota is not None:
            result['RemainQuota'] = self.remain_quota
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.start_time_utc is not None:
            result['StartTimeUTC'] = self.start_time_utc
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Consumed') is not None:
            self.consumed = m.get('Consumed')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EndTimeUTC') is not None:
            self.end_time_utc = m.get('EndTimeUTC')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('Lifecycle') is not None:
            self.lifecycle = m.get('Lifecycle')
        if m.get('Months') is not None:
            self.months = m.get('Months')
        if m.get('RemainQuota') is not None:
            self.remain_quota = m.get('RemainQuota')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StartTimeUTC') is not None:
            self.start_time_utc = m.get('StartTimeUTC')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryFreeStorageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryFreeStorageResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryFreeStorageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryFreeStorageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryFreeStorageResponseBody = None,
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
            temp_model = QueryFreeStorageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryGenerateDevicesInfoListRequest(TeaModel):
    def __init__(
        self,
        batch_id: str = None,
        page_no: int = None,
        page_size: int = None,
        project_id: str = None,
    ):
        self.batch_id = batch_id
        self.page_no = page_no
        self.page_size = page_size
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class QueryGenerateDevicesInfoListResponseBodyDataListData(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        device_secret: str = None,
        iot_id: str = None,
    ):
        self.device_name = device_name
        self.device_secret = device_secret
        self.iot_id = iot_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.device_secret is not None:
            result['DeviceSecret'] = self.device_secret
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('DeviceSecret') is not None:
            self.device_secret = m.get('DeviceSecret')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        return self


class QueryGenerateDevicesInfoListResponseBodyData(TeaModel):
    def __init__(
        self,
        list_data: List[QueryGenerateDevicesInfoListResponseBodyDataListData] = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.list_data = list_data
        self.page_no = page_no
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.list_data:
            for k in self.list_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ListData'] = []
        if self.list_data is not None:
            for k in self.list_data:
                result['ListData'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list_data = []
        if m.get('ListData') is not None:
            for k in m.get('ListData'):
                temp_model = QueryGenerateDevicesInfoListResponseBodyDataListData()
                self.list_data.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryGenerateDevicesInfoListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryGenerateDevicesInfoListResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryGenerateDevicesInfoListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryGenerateDevicesInfoListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryGenerateDevicesInfoListResponseBody = None,
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
            temp_model = QueryGenerateDevicesInfoListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryGenerateDevicesRecordRequest(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        page_no: int = None,
        page_size: int = None,
        start_time: int = None,
    ):
        self.end_time = end_time
        self.page_no = page_no
        self.page_size = page_size
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class QueryGenerateDevicesRecordResponseBodyDataListData(TeaModel):
    def __init__(
        self,
        apply_device_count: int = None,
        batch_id: str = None,
        batch_status: str = None,
        create_time: int = None,
        network_type: str = None,
        operate_uid: int = None,
        product_key: str = None,
        product_name: str = None,
        spec_code: str = None,
        success_count: int = None,
    ):
        self.apply_device_count = apply_device_count
        self.batch_id = batch_id
        self.batch_status = batch_status
        self.create_time = create_time
        self.network_type = network_type
        self.operate_uid = operate_uid
        self.product_key = product_key
        self.product_name = product_name
        self.spec_code = spec_code
        self.success_count = success_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_device_count is not None:
            result['ApplyDeviceCount'] = self.apply_device_count
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id
        if self.batch_status is not None:
            result['BatchStatus'] = self.batch_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.operate_uid is not None:
            result['OperateUid'] = self.operate_uid
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.spec_code is not None:
            result['SpecCode'] = self.spec_code
        if self.success_count is not None:
            result['SuccessCount'] = self.success_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyDeviceCount') is not None:
            self.apply_device_count = m.get('ApplyDeviceCount')
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')
        if m.get('BatchStatus') is not None:
            self.batch_status = m.get('BatchStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('OperateUid') is not None:
            self.operate_uid = m.get('OperateUid')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('SpecCode') is not None:
            self.spec_code = m.get('SpecCode')
        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')
        return self


class QueryGenerateDevicesRecordResponseBodyData(TeaModel):
    def __init__(
        self,
        list_data: List[QueryGenerateDevicesRecordResponseBodyDataListData] = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.list_data = list_data
        self.page_no = page_no
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.list_data:
            for k in self.list_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ListData'] = []
        if self.list_data is not None:
            for k in self.list_data:
                result['ListData'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list_data = []
        if m.get('ListData') is not None:
            for k in m.get('ListData'):
                temp_model = QueryGenerateDevicesRecordResponseBodyDataListData()
                self.list_data.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryGenerateDevicesRecordResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryGenerateDevicesRecordResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryGenerateDevicesRecordResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryGenerateDevicesRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryGenerateDevicesRecordResponseBody = None,
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
            temp_model = QueryGenerateDevicesRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryStorageCommodityListResponseBodyData(TeaModel):
    def __init__(
        self,
        commodity_code: str = None,
        commodity_name: str = None,
        lifecycle: int = None,
        months: int = None,
        price: str = None,
        record_type: int = None,
        specification: str = None,
    ):
        self.commodity_code = commodity_code
        self.commodity_name = commodity_name
        self.lifecycle = lifecycle
        self.months = months
        self.price = price
        self.record_type = record_type
        self.specification = specification

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.commodity_name is not None:
            result['CommodityName'] = self.commodity_name
        if self.lifecycle is not None:
            result['Lifecycle'] = self.lifecycle
        if self.months is not None:
            result['Months'] = self.months
        if self.price is not None:
            result['Price'] = self.price
        if self.record_type is not None:
            result['RecordType'] = self.record_type
        if self.specification is not None:
            result['Specification'] = self.specification
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('CommodityName') is not None:
            self.commodity_name = m.get('CommodityName')
        if m.get('Lifecycle') is not None:
            self.lifecycle = m.get('Lifecycle')
        if m.get('Months') is not None:
            self.months = m.get('Months')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        return self


class QueryStorageCommodityListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[QueryStorageCommodityListResponseBodyData] = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

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
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryStorageCommodityListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryStorageCommodityListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryStorageCommodityListResponseBody = None,
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
            temp_model = QueryStorageCommodityListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryStorageOrderRequest(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        device_no_owner: bool = None,
        iot_id: str = None,
        order_id: str = None,
        product_key: str = None,
    ):
        self.device_name = device_name
        self.device_no_owner = device_no_owner
        self.iot_id = iot_id
        self.order_id = order_id
        self.product_key = product_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.device_no_owner is not None:
            result['DeviceNoOwner'] = self.device_no_owner
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('DeviceNoOwner') is not None:
            self.device_no_owner = m.get('DeviceNoOwner')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class QueryStorageOrderResponseBodyData(TeaModel):
    def __init__(
        self,
        commodity_code: str = None,
        copies: int = None,
        end_time: str = None,
        end_time_utc: str = None,
        identity_id: str = None,
        iot_id: str = None,
        order_id: str = None,
        order_type: int = None,
        out_order_no: str = None,
        payment_status: int = None,
        pre_consume: int = None,
        price: str = None,
        record_type: int = None,
        specification: str = None,
        start_time: str = None,
        start_time_utc: str = None,
        status: int = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.commodity_code = commodity_code
        self.copies = copies
        self.end_time = end_time
        self.end_time_utc = end_time_utc
        self.identity_id = identity_id
        self.iot_id = iot_id
        self.order_id = order_id
        self.order_type = order_type
        self.out_order_no = out_order_no
        self.payment_status = payment_status
        self.pre_consume = pre_consume
        self.price = price
        self.record_type = record_type
        self.specification = specification
        self.start_time = start_time
        self.start_time_utc = start_time_utc
        self.status = status
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.copies is not None:
            result['Copies'] = self.copies
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.end_time_utc is not None:
            result['EndTimeUTC'] = self.end_time_utc
        if self.identity_id is not None:
            result['IdentityId'] = self.identity_id
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.out_order_no is not None:
            result['OutOrderNo'] = self.out_order_no
        if self.payment_status is not None:
            result['PaymentStatus'] = self.payment_status
        if self.pre_consume is not None:
            result['PreConsume'] = self.pre_consume
        if self.price is not None:
            result['Price'] = self.price
        if self.record_type is not None:
            result['RecordType'] = self.record_type
        if self.specification is not None:
            result['Specification'] = self.specification
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.start_time_utc is not None:
            result['StartTimeUTC'] = self.start_time_utc
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('Copies') is not None:
            self.copies = m.get('Copies')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EndTimeUTC') is not None:
            self.end_time_utc = m.get('EndTimeUTC')
        if m.get('IdentityId') is not None:
            self.identity_id = m.get('IdentityId')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('OutOrderNo') is not None:
            self.out_order_no = m.get('OutOrderNo')
        if m.get('PaymentStatus') is not None:
            self.payment_status = m.get('PaymentStatus')
        if m.get('PreConsume') is not None:
            self.pre_consume = m.get('PreConsume')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StartTimeUTC') is not None:
            self.start_time_utc = m.get('StartTimeUTC')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class QueryStorageOrderResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryStorageOrderResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryStorageOrderResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryStorageOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryStorageOrderResponseBody = None,
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
            temp_model = QueryStorageOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryStorageOrderListRequest(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        device_no_owner: bool = None,
        iot_id: str = None,
        page_no: int = None,
        page_size: int = None,
        product_key: str = None,
    ):
        self.device_name = device_name
        self.device_no_owner = device_no_owner
        self.iot_id = iot_id
        self.page_no = page_no
        self.page_size = page_size
        self.product_key = product_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.device_no_owner is not None:
            result['DeviceNoOwner'] = self.device_no_owner
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('DeviceNoOwner') is not None:
            self.device_no_owner = m.get('DeviceNoOwner')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class QueryStorageOrderListResponseBodyDataStorageOrderList(TeaModel):
    def __init__(
        self,
        commodity_code: str = None,
        copies: int = None,
        end_time: str = None,
        end_time_utc: str = None,
        identity_id: str = None,
        iot_id: str = None,
        order_id: str = None,
        order_type: int = None,
        out_order_no: str = None,
        payment_status: int = None,
        pre_consume: int = None,
        price: str = None,
        record_type: int = None,
        specification: str = None,
        start_time: str = None,
        start_time_utc: str = None,
        status: int = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.commodity_code = commodity_code
        self.copies = copies
        self.end_time = end_time
        self.end_time_utc = end_time_utc
        self.identity_id = identity_id
        self.iot_id = iot_id
        self.order_id = order_id
        self.order_type = order_type
        self.out_order_no = out_order_no
        self.payment_status = payment_status
        self.pre_consume = pre_consume
        self.price = price
        self.record_type = record_type
        self.specification = specification
        self.start_time = start_time
        self.start_time_utc = start_time_utc
        self.status = status
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.copies is not None:
            result['Copies'] = self.copies
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.end_time_utc is not None:
            result['EndTimeUTC'] = self.end_time_utc
        if self.identity_id is not None:
            result['IdentityId'] = self.identity_id
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.out_order_no is not None:
            result['OutOrderNo'] = self.out_order_no
        if self.payment_status is not None:
            result['PaymentStatus'] = self.payment_status
        if self.pre_consume is not None:
            result['PreConsume'] = self.pre_consume
        if self.price is not None:
            result['Price'] = self.price
        if self.record_type is not None:
            result['RecordType'] = self.record_type
        if self.specification is not None:
            result['Specification'] = self.specification
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.start_time_utc is not None:
            result['StartTimeUTC'] = self.start_time_utc
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('Copies') is not None:
            self.copies = m.get('Copies')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EndTimeUTC') is not None:
            self.end_time_utc = m.get('EndTimeUTC')
        if m.get('IdentityId') is not None:
            self.identity_id = m.get('IdentityId')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('OutOrderNo') is not None:
            self.out_order_no = m.get('OutOrderNo')
        if m.get('PaymentStatus') is not None:
            self.payment_status = m.get('PaymentStatus')
        if m.get('PreConsume') is not None:
            self.pre_consume = m.get('PreConsume')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StartTimeUTC') is not None:
            self.start_time_utc = m.get('StartTimeUTC')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class QueryStorageOrderListResponseBodyData(TeaModel):
    def __init__(
        self,
        page_count: int = None,
        page_no: int = None,
        page_size: int = None,
        storage_order_list: List[QueryStorageOrderListResponseBodyDataStorageOrderList] = None,
        total: int = None,
    ):
        self.page_count = page_count
        self.page_no = page_no
        self.page_size = page_size
        self.storage_order_list = storage_order_list
        self.total = total

    def validate(self):
        if self.storage_order_list:
            for k in self.storage_order_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['StorageOrderList'] = []
        if self.storage_order_list is not None:
            for k in self.storage_order_list:
                result['StorageOrderList'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.storage_order_list = []
        if m.get('StorageOrderList') is not None:
            for k in m.get('StorageOrderList'):
                temp_model = QueryStorageOrderListResponseBodyDataStorageOrderList()
                self.storage_order_list.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryStorageOrderListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryStorageOrderListResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryStorageOrderListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryStorageOrderListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryStorageOrderListResponseBody = None,
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
            temp_model = QueryStorageOrderListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TransferStorageOrderRequest(TeaModel):
    def __init__(
        self,
        dst_iot_id: str = None,
        enable_default_plan: bool = None,
        event_record_duration: int = None,
        event_record_prolong: bool = None,
        immediate_use: bool = None,
        pre_record_duration: int = None,
        src_iot_id: str = None,
        src_order_id: str = None,
        support_cross_identity_transfer: bool = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.dst_iot_id = dst_iot_id
        self.enable_default_plan = enable_default_plan
        self.event_record_duration = event_record_duration
        self.event_record_prolong = event_record_prolong
        self.immediate_use = immediate_use
        self.pre_record_duration = pre_record_duration
        self.src_iot_id = src_iot_id
        self.src_order_id = src_order_id
        self.support_cross_identity_transfer = support_cross_identity_transfer
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dst_iot_id is not None:
            result['DstIotId'] = self.dst_iot_id
        if self.enable_default_plan is not None:
            result['EnableDefaultPlan'] = self.enable_default_plan
        if self.event_record_duration is not None:
            result['EventRecordDuration'] = self.event_record_duration
        if self.event_record_prolong is not None:
            result['EventRecordProlong'] = self.event_record_prolong
        if self.immediate_use is not None:
            result['ImmediateUse'] = self.immediate_use
        if self.pre_record_duration is not None:
            result['PreRecordDuration'] = self.pre_record_duration
        if self.src_iot_id is not None:
            result['SrcIotId'] = self.src_iot_id
        if self.src_order_id is not None:
            result['SrcOrderId'] = self.src_order_id
        if self.support_cross_identity_transfer is not None:
            result['SupportCrossIdentityTransfer'] = self.support_cross_identity_transfer
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DstIotId') is not None:
            self.dst_iot_id = m.get('DstIotId')
        if m.get('EnableDefaultPlan') is not None:
            self.enable_default_plan = m.get('EnableDefaultPlan')
        if m.get('EventRecordDuration') is not None:
            self.event_record_duration = m.get('EventRecordDuration')
        if m.get('EventRecordProlong') is not None:
            self.event_record_prolong = m.get('EventRecordProlong')
        if m.get('ImmediateUse') is not None:
            self.immediate_use = m.get('ImmediateUse')
        if m.get('PreRecordDuration') is not None:
            self.pre_record_duration = m.get('PreRecordDuration')
        if m.get('SrcIotId') is not None:
            self.src_iot_id = m.get('SrcIotId')
        if m.get('SrcOrderId') is not None:
            self.src_order_id = m.get('SrcOrderId')
        if m.get('SupportCrossIdentityTransfer') is not None:
            self.support_cross_identity_transfer = m.get('SupportCrossIdentityTransfer')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class TransferStorageOrderResponseBodyData(TeaModel):
    def __init__(
        self,
        commodity_code: str = None,
        copies: int = None,
        end_time: str = None,
        end_time_utc: str = None,
        identity_id: str = None,
        iot_id: str = None,
        order_id: str = None,
        order_type: int = None,
        out_order_no: str = None,
        payment_status: int = None,
        pre_consume: int = None,
        price: str = None,
        record_type: int = None,
        specification: str = None,
        start_time: str = None,
        start_time_utc: str = None,
        status: int = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.commodity_code = commodity_code
        self.copies = copies
        self.end_time = end_time
        self.end_time_utc = end_time_utc
        self.identity_id = identity_id
        self.iot_id = iot_id
        self.order_id = order_id
        self.order_type = order_type
        self.out_order_no = out_order_no
        self.payment_status = payment_status
        self.pre_consume = pre_consume
        self.price = price
        self.record_type = record_type
        self.specification = specification
        self.start_time = start_time
        self.start_time_utc = start_time_utc
        self.status = status
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.copies is not None:
            result['Copies'] = self.copies
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.end_time_utc is not None:
            result['EndTimeUTC'] = self.end_time_utc
        if self.identity_id is not None:
            result['IdentityId'] = self.identity_id
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.out_order_no is not None:
            result['OutOrderNo'] = self.out_order_no
        if self.payment_status is not None:
            result['PaymentStatus'] = self.payment_status
        if self.pre_consume is not None:
            result['PreConsume'] = self.pre_consume
        if self.price is not None:
            result['Price'] = self.price
        if self.record_type is not None:
            result['RecordType'] = self.record_type
        if self.specification is not None:
            result['Specification'] = self.specification
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.start_time_utc is not None:
            result['StartTimeUTC'] = self.start_time_utc
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('Copies') is not None:
            self.copies = m.get('Copies')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EndTimeUTC') is not None:
            self.end_time_utc = m.get('EndTimeUTC')
        if m.get('IdentityId') is not None:
            self.identity_id = m.get('IdentityId')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('OutOrderNo') is not None:
            self.out_order_no = m.get('OutOrderNo')
        if m.get('PaymentStatus') is not None:
            self.payment_status = m.get('PaymentStatus')
        if m.get('PreConsume') is not None:
            self.pre_consume = m.get('PreConsume')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StartTimeUTC') is not None:
            self.start_time_utc = m.get('StartTimeUTC')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class TransferStorageOrderResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: TransferStorageOrderResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = TransferStorageOrderResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class TransferStorageOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TransferStorageOrderResponseBody = None,
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
            temp_model = TransferStorageOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadDeviceNameListRequest(TeaModel):
    def __init__(
        self,
        device_names: List[str] = None,
        product_key: str = None,
        project_id: str = None,
    ):
        self.device_names = device_names
        self.product_key = product_key
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_names is not None:
            result['DeviceNames'] = self.device_names
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceNames') is not None:
            self.device_names = m.get('DeviceNames')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class UploadDeviceNameListResponseBodyDataInvalidDetailList(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        error_msg: str = None,
    ):
        self.device_name = device_name
        self.error_msg = error_msg

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        return self


class UploadDeviceNameListResponseBodyData(TeaModel):
    def __init__(
        self,
        batch_id: str = None,
        invalid_detail_list: List[UploadDeviceNameListResponseBodyDataInvalidDetailList] = None,
        invalid_device_name_list: List[str] = None,
        repeated_device_name_list: List[str] = None,
    ):
        self.batch_id = batch_id
        self.invalid_detail_list = invalid_detail_list
        self.invalid_device_name_list = invalid_device_name_list
        self.repeated_device_name_list = repeated_device_name_list

    def validate(self):
        if self.invalid_detail_list:
            for k in self.invalid_detail_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id
        result['InvalidDetailList'] = []
        if self.invalid_detail_list is not None:
            for k in self.invalid_detail_list:
                result['InvalidDetailList'].append(k.to_map() if k else None)
        if self.invalid_device_name_list is not None:
            result['InvalidDeviceNameList'] = self.invalid_device_name_list
        if self.repeated_device_name_list is not None:
            result['RepeatedDeviceNameList'] = self.repeated_device_name_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')
        self.invalid_detail_list = []
        if m.get('InvalidDetailList') is not None:
            for k in m.get('InvalidDetailList'):
                temp_model = UploadDeviceNameListResponseBodyDataInvalidDetailList()
                self.invalid_detail_list.append(temp_model.from_map(k))
        if m.get('InvalidDeviceNameList') is not None:
            self.invalid_device_name_list = m.get('InvalidDeviceNameList')
        if m.get('RepeatedDeviceNameList') is not None:
            self.repeated_device_name_list = m.get('RepeatedDeviceNameList')
        return self


class UploadDeviceNameListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: UploadDeviceNameListResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = UploadDeviceNameListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UploadDeviceNameListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UploadDeviceNameListResponseBody = None,
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
            temp_model = UploadDeviceNameListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


