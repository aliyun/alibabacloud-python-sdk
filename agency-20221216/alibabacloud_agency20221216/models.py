# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CancelSubscriptionBillRequest(TeaModel):
    def __init__(
        self,
        subscribe_type: str = None,
    ):
        # The type of the bill to which you want to cancel the subscription. Valid values: PartnerBillingItemDetailForBillingPeriod, PartnerBillingItemDetailMonthly, PartnerInstanceDetailForBillingPeriod, and PartnerInstanceDetailMonthly.
        self.subscribe_type = subscribe_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.subscribe_type is not None:
            result['SubscribeType'] = self.subscribe_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubscribeType') is not None:
            self.subscribe_type = m.get('SubscribeType')
        return self


class CancelSubscriptionBillResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code that is returned.
        self.code = code
        # The data that is returned.
        self.data = data
        # The message that is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful.
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
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CancelSubscriptionBillResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelSubscriptionBillResponseBody = None,
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
            temp_model = CancelSubscriptionBillResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCustomerRequest(TeaModel):
    def __init__(
        self,
        customer_name: str = None,
        customer_source: str = None,
        customer_sub_trade: str = None,
        customer_trade: str = None,
        nation: str = None,
    ):
        self.customer_name = customer_name
        self.customer_source = customer_source
        self.customer_sub_trade = customer_sub_trade
        self.customer_trade = customer_trade
        self.nation = nation

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.customer_name is not None:
            result['CustomerName'] = self.customer_name
        if self.customer_source is not None:
            result['CustomerSource'] = self.customer_source
        if self.customer_sub_trade is not None:
            result['CustomerSubTrade'] = self.customer_sub_trade
        if self.customer_trade is not None:
            result['CustomerTrade'] = self.customer_trade
        if self.nation is not None:
            result['Nation'] = self.nation
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomerName') is not None:
            self.customer_name = m.get('CustomerName')
        if m.get('CustomerSource') is not None:
            self.customer_source = m.get('CustomerSource')
        if m.get('CustomerSubTrade') is not None:
            self.customer_sub_trade = m.get('CustomerSubTrade')
        if m.get('CustomerTrade') is not None:
            self.customer_trade = m.get('CustomerTrade')
        if m.get('Nation') is not None:
            self.nation = m.get('Nation')
        return self


class CreateCustomerResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateCustomerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCustomerResponseBody = None,
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
            temp_model = CreateCustomerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeductOutstandingBalanceRequest(TeaModel):
    def __init__(
        self,
        deduct_amount: str = None,
        uid: int = None,
    ):
        self.deduct_amount = deduct_amount
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deduct_amount is not None:
            result['DeductAmount'] = self.deduct_amount
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeductAmount') is not None:
            self.deduct_amount = m.get('DeductAmount')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class DeductOutstandingBalanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
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
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeductOutstandingBalanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeductOutstandingBalanceResponseBody = None,
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
            temp_model = DeductOutstandingBalanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EditEndUserStatusRequest(TeaModel):
    def __init__(
        self,
        credit_status: str = None,
        uid: int = None,
    ):
        self.credit_status = credit_status
        # uid
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credit_status is not None:
            result['CreditStatus'] = self.credit_status
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreditStatus') is not None:
            self.credit_status = m.get('CreditStatus')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class EditEndUserStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        msg: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.msg = msg
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EditEndUserStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EditEndUserStatusResponseBody = None,
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
            temp_model = EditEndUserStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EditNewBuyStatusRequest(TeaModel):
    def __init__(
        self,
        new_buy_status: str = None,
        uid: int = None,
    ):
        self.new_buy_status = new_buy_status
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_buy_status is not None:
            result['NewBuyStatus'] = self.new_buy_status
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewBuyStatus') is not None:
            self.new_buy_status = m.get('NewBuyStatus')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class EditNewBuyStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        msg: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.msg = msg
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EditNewBuyStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EditNewBuyStatusResponseBody = None,
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
            temp_model = EditNewBuyStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EditZeroCreditShutdownRequest(TeaModel):
    def __init__(
        self,
        shutdown_policy: str = None,
        uid: int = None,
    ):
        self.shutdown_policy = shutdown_policy
        # uid
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.shutdown_policy is not None:
            result['ShutdownPolicy'] = self.shutdown_policy
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ShutdownPolicy') is not None:
            self.shutdown_policy = m.get('ShutdownPolicy')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class EditZeroCreditShutdownResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        msg: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.msg = msg
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EditZeroCreditShutdownResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EditZeroCreditShutdownResponseBody = None,
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
            temp_model = EditZeroCreditShutdownResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAccountInfoRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        uid: int = None,
        user_type: str = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.uid = uid
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class GetAccountInfoResponseBodyAccountInfoListAccountInfo(TeaModel):
    def __init__(
        self,
        account_nickname: str = None,
        aliyun_id: str = None,
        association_success_time: str = None,
        cid: int = None,
        email: str = None,
        mobile: str = None,
        remark: str = None,
        sub_account_type: int = None,
        uid: int = None,
    ):
        self.account_nickname = account_nickname
        self.aliyun_id = aliyun_id
        self.association_success_time = association_success_time
        self.cid = cid
        self.email = email
        self.mobile = mobile
        self.remark = remark
        self.sub_account_type = sub_account_type
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_nickname is not None:
            result['AccountNickname'] = self.account_nickname
        if self.aliyun_id is not None:
            result['AliyunId'] = self.aliyun_id
        if self.association_success_time is not None:
            result['AssociationSuccessTime'] = self.association_success_time
        if self.cid is not None:
            result['Cid'] = self.cid
        if self.email is not None:
            result['Email'] = self.email
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.sub_account_type is not None:
            result['SubAccountType'] = self.sub_account_type
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountNickname') is not None:
            self.account_nickname = m.get('AccountNickname')
        if m.get('AliyunId') is not None:
            self.aliyun_id = m.get('AliyunId')
        if m.get('AssociationSuccessTime') is not None:
            self.association_success_time = m.get('AssociationSuccessTime')
        if m.get('Cid') is not None:
            self.cid = m.get('Cid')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('SubAccountType') is not None:
            self.sub_account_type = m.get('SubAccountType')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class GetAccountInfoResponseBodyAccountInfoList(TeaModel):
    def __init__(
        self,
        account_info: List[GetAccountInfoResponseBodyAccountInfoListAccountInfo] = None,
    ):
        self.account_info = account_info

    def validate(self):
        if self.account_info:
            for k in self.account_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AccountInfo'] = []
        if self.account_info is not None:
            for k in self.account_info:
                result['AccountInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.account_info = []
        if m.get('AccountInfo') is not None:
            for k in m.get('AccountInfo'):
                temp_model = GetAccountInfoResponseBodyAccountInfoListAccountInfo()
                self.account_info.append(temp_model.from_map(k))
        return self


class GetAccountInfoResponseBodyPageInfo(TeaModel):
    def __init__(
        self,
        page: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.page = page
        self.page_size = page_size
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetAccountInfoResponseBody(TeaModel):
    def __init__(
        self,
        account_info_list: GetAccountInfoResponseBodyAccountInfoList = None,
        code: str = None,
        message: str = None,
        page_info: GetAccountInfoResponseBodyPageInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.account_info_list = account_info_list
        self.code = code
        # message
        self.message = message
        self.page_info = page_info
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.account_info_list:
            self.account_info_list.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_info_list is not None:
            result['AccountInfoList'] = self.account_info_list.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountInfoList') is not None:
            temp_model = GetAccountInfoResponseBodyAccountInfoList()
            self.account_info_list = temp_model.from_map(m['AccountInfoList'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageInfo') is not None:
            temp_model = GetAccountInfoResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAccountInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAccountInfoResponseBody = None,
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
            temp_model = GetAccountInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCreditInfoRequest(TeaModel):
    def __init__(
        self,
        uid: int = None,
    ):
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class GetCreditInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        account_status: str = None,
        alarm_threshold: str = None,
        available_credit: str = None,
        credit_line: str = None,
        outstanding_balance: str = None,
        zero_credit_shutdown_policy: str = None,
        new_buy_status: str = None,
    ):
        self.account_status = account_status
        self.alarm_threshold = alarm_threshold
        self.available_credit = available_credit
        self.credit_line = credit_line
        self.outstanding_balance = outstanding_balance
        self.zero_credit_shutdown_policy = zero_credit_shutdown_policy
        self.new_buy_status = new_buy_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_status is not None:
            result['AccountStatus'] = self.account_status
        if self.alarm_threshold is not None:
            result['AlarmThreshold'] = self.alarm_threshold
        if self.available_credit is not None:
            result['AvailableCredit'] = self.available_credit
        if self.credit_line is not None:
            result['CreditLine'] = self.credit_line
        if self.outstanding_balance is not None:
            result['OutstandingBalance'] = self.outstanding_balance
        if self.zero_credit_shutdown_policy is not None:
            result['ZeroCreditShutdownPolicy'] = self.zero_credit_shutdown_policy
        if self.new_buy_status is not None:
            result['newBuyStatus'] = self.new_buy_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountStatus') is not None:
            self.account_status = m.get('AccountStatus')
        if m.get('AlarmThreshold') is not None:
            self.alarm_threshold = m.get('AlarmThreshold')
        if m.get('AvailableCredit') is not None:
            self.available_credit = m.get('AvailableCredit')
        if m.get('CreditLine') is not None:
            self.credit_line = m.get('CreditLine')
        if m.get('OutstandingBalance') is not None:
            self.outstanding_balance = m.get('OutstandingBalance')
        if m.get('ZeroCreditShutdownPolicy') is not None:
            self.zero_credit_shutdown_policy = m.get('ZeroCreditShutdownPolicy')
        if m.get('newBuyStatus') is not None:
            self.new_buy_status = m.get('newBuyStatus')
        return self


class GetCreditInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetCreditInfoResponseBodyData = None,
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
            temp_model = GetCreditInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetCreditInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCreditInfoResponseBody = None,
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
            temp_model = GetCreditInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDailyBillRequest(TeaModel):
    def __init__(
        self,
        bill_owner: str = None,
        bill_type: str = None,
        date: str = None,
    ):
        self.bill_owner = bill_owner
        self.bill_type = bill_type
        # Billing date. Format YYYY-MM-DD
        self.date = date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_owner is not None:
            result['BillOwner'] = self.bill_owner
        if self.bill_type is not None:
            result['BillType'] = self.bill_type
        if self.date is not None:
            result['Date'] = self.date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillOwner') is not None:
            self.bill_owner = m.get('BillOwner')
        if m.get('BillType') is not None:
            self.bill_type = m.get('BillType')
        if m.get('Date') is not None:
            self.date = m.get('Date')
        return self


class GetDailyBillResponseBodyData(TeaModel):
    def __init__(
        self,
        bill_link_csv: str = None,
        bill_link_xlsx: str = None,
        bill_owner: str = None,
        bill_type: str = None,
        spending_time: str = None,
    ):
        self.bill_link_csv = bill_link_csv
        self.bill_link_xlsx = bill_link_xlsx
        self.bill_owner = bill_owner
        self.bill_type = bill_type
        self.spending_time = spending_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_link_csv is not None:
            result['BillLinkCSV'] = self.bill_link_csv
        if self.bill_link_xlsx is not None:
            result['BillLinkXLSX'] = self.bill_link_xlsx
        if self.bill_owner is not None:
            result['BillOwner'] = self.bill_owner
        if self.bill_type is not None:
            result['BillType'] = self.bill_type
        if self.spending_time is not None:
            result['SpendingTime'] = self.spending_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillLinkCSV') is not None:
            self.bill_link_csv = m.get('BillLinkCSV')
        if m.get('BillLinkXLSX') is not None:
            self.bill_link_xlsx = m.get('BillLinkXLSX')
        if m.get('BillOwner') is not None:
            self.bill_owner = m.get('BillOwner')
        if m.get('BillType') is not None:
            self.bill_type = m.get('BillType')
        if m.get('SpendingTime') is not None:
            self.spending_time = m.get('SpendingTime')
        return self


class GetDailyBillResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetDailyBillResponseBodyData = None,
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
            temp_model = GetDailyBillResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetDailyBillResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDailyBillResponseBody = None,
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
            temp_model = GetDailyBillResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInviteStatusRequestInviteStatusList(TeaModel):
    def __init__(
        self,
        invite_id: int = None,
    ):
        self.invite_id = invite_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.invite_id is not None:
            result['InviteId'] = self.invite_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InviteId') is not None:
            self.invite_id = m.get('InviteId')
        return self


class GetInviteStatusRequest(TeaModel):
    def __init__(
        self,
        invite_status_list: List[GetInviteStatusRequestInviteStatusList] = None,
    ):
        # inviteId list
        self.invite_status_list = invite_status_list

    def validate(self):
        if self.invite_status_list:
            for k in self.invite_status_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InviteStatusList'] = []
        if self.invite_status_list is not None:
            for k in self.invite_status_list:
                result['InviteStatusList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.invite_status_list = []
        if m.get('InviteStatusList') is not None:
            for k in m.get('InviteStatusList'):
                temp_model = GetInviteStatusRequestInviteStatusList()
                self.invite_status_list.append(temp_model.from_map(k))
        return self


class GetInviteStatusResponseBodyDataInviteStatusInviteStatusList(TeaModel):
    def __init__(
        self,
        association_success_time: str = None,
        cid: int = None,
        gmt_create: str = None,
        parent_id: str = None,
        status: int = None,
        sub_account_type: str = None,
        uid: int = None,
    ):
        self.association_success_time = association_success_time
        self.cid = cid
        self.gmt_create = gmt_create
        self.parent_id = parent_id
        self.status = status
        self.sub_account_type = sub_account_type
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.association_success_time is not None:
            result['AssociationSuccessTime'] = self.association_success_time
        if self.cid is not None:
            result['Cid'] = self.cid
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.status is not None:
            result['Status'] = self.status
        if self.sub_account_type is not None:
            result['SubAccountType'] = self.sub_account_type
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociationSuccessTime') is not None:
            self.association_success_time = m.get('AssociationSuccessTime')
        if m.get('Cid') is not None:
            self.cid = m.get('Cid')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubAccountType') is not None:
            self.sub_account_type = m.get('SubAccountType')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class GetInviteStatusResponseBodyDataInviteStatus(TeaModel):
    def __init__(
        self,
        code: str = None,
        invite_status_list: GetInviteStatusResponseBodyDataInviteStatusInviteStatusList = None,
        message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.invite_status_list = invite_status_list
        self.message = message
        self.success = success

    def validate(self):
        if self.invite_status_list:
            self.invite_status_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.invite_status_list is not None:
            result['InviteStatusList'] = self.invite_status_list.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('InviteStatusList') is not None:
            temp_model = GetInviteStatusResponseBodyDataInviteStatusInviteStatusList()
            self.invite_status_list = temp_model.from_map(m['InviteStatusList'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetInviteStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        invite_status: List[GetInviteStatusResponseBodyDataInviteStatus] = None,
    ):
        self.invite_status = invite_status

    def validate(self):
        if self.invite_status:
            for k in self.invite_status:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InviteStatus'] = []
        if self.invite_status is not None:
            for k in self.invite_status:
                result['InviteStatus'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.invite_status = []
        if m.get('InviteStatus') is not None:
            for k in m.get('InviteStatus'):
                temp_model = GetInviteStatusResponseBodyDataInviteStatus()
                self.invite_status.append(temp_model.from_map(k))
        return self


class GetInviteStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetInviteStatusResponseBodyData = None,
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
            temp_model = GetInviteStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetInviteStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetInviteStatusResponseBody = None,
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
            temp_model = GetInviteStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMonthlyBillRequest(TeaModel):
    def __init__(
        self,
        bill_owner: str = None,
        bill_type: str = None,
        month: str = None,
    ):
        # Bill Owner type.
        # 
        #  Value range:
        # 
        # 1: Master account 
        # 
        # 2: Sub account
        self.bill_owner = bill_owner
        # Value Range:
        # 
        # MonthlyInvoice
        # 
        # MonthRefundInvoice
        # 
        # MonthlySummary
        # 
        # MonthlyInstanceAddAdjustBill 
        # 
        # MonthlyInstanceRefundBill
        # 
        # MonthlyAddAdjustInvoce
        # 
        # MonthlyRefundAdjustInvoce 
        # 
        # MonthlyInstanceConsumeV2 
        # 
        # MarginReportV2
        self.bill_type = bill_type
        # Billing Month, Format is YYYY-MM
        self.month = month

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_owner is not None:
            result['BillOwner'] = self.bill_owner
        if self.bill_type is not None:
            result['BillType'] = self.bill_type
        if self.month is not None:
            result['Month'] = self.month
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillOwner') is not None:
            self.bill_owner = m.get('BillOwner')
        if m.get('BillType') is not None:
            self.bill_type = m.get('BillType')
        if m.get('Month') is not None:
            self.month = m.get('Month')
        return self


class GetMonthlyBillResponseBodyData(TeaModel):
    def __init__(
        self,
        bill_link_csv: str = None,
        bill_link_xlsx: str = None,
        bill_owner: str = None,
        bill_type: str = None,
        invoice_link: str = None,
        refund_invoice_flag: bool = None,
        refund_invoice_link: str = None,
        spending_time: str = None,
    ):
        self.bill_link_csv = bill_link_csv
        self.bill_link_xlsx = bill_link_xlsx
        self.bill_owner = bill_owner
        self.bill_type = bill_type
        self.invoice_link = invoice_link
        self.refund_invoice_flag = refund_invoice_flag
        self.refund_invoice_link = refund_invoice_link
        self.spending_time = spending_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_link_csv is not None:
            result['BillLinkCSV'] = self.bill_link_csv
        if self.bill_link_xlsx is not None:
            result['BillLinkXLSX'] = self.bill_link_xlsx
        if self.bill_owner is not None:
            result['BillOwner'] = self.bill_owner
        if self.bill_type is not None:
            result['BillType'] = self.bill_type
        if self.invoice_link is not None:
            result['InvoiceLink'] = self.invoice_link
        if self.refund_invoice_flag is not None:
            result['RefundInvoiceFlag'] = self.refund_invoice_flag
        if self.refund_invoice_link is not None:
            result['RefundInvoiceLink'] = self.refund_invoice_link
        if self.spending_time is not None:
            result['SpendingTime'] = self.spending_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillLinkCSV') is not None:
            self.bill_link_csv = m.get('BillLinkCSV')
        if m.get('BillLinkXLSX') is not None:
            self.bill_link_xlsx = m.get('BillLinkXLSX')
        if m.get('BillOwner') is not None:
            self.bill_owner = m.get('BillOwner')
        if m.get('BillType') is not None:
            self.bill_type = m.get('BillType')
        if m.get('InvoiceLink') is not None:
            self.invoice_link = m.get('InvoiceLink')
        if m.get('RefundInvoiceFlag') is not None:
            self.refund_invoice_flag = m.get('RefundInvoiceFlag')
        if m.get('RefundInvoiceLink') is not None:
            self.refund_invoice_link = m.get('RefundInvoiceLink')
        if m.get('SpendingTime') is not None:
            self.spending_time = m.get('SpendingTime')
        return self


class GetMonthlyBillResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetMonthlyBillResponseBodyData = None,
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
            temp_model = GetMonthlyBillResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetMonthlyBillResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMonthlyBillResponseBody = None,
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
            temp_model = GetMonthlyBillResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUnassociatedCustomerRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class GetUnassociatedCustomerResponseBodyInviteInfoListInviteInfo(TeaModel):
    def __init__(
        self,
        account_nickname: str = None,
        email: str = None,
        gmt_create: str = None,
        invite_id: int = None,
        status: int = None,
    ):
        self.account_nickname = account_nickname
        self.email = email
        self.gmt_create = gmt_create
        self.invite_id = invite_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_nickname is not None:
            result['AccountNickname'] = self.account_nickname
        if self.email is not None:
            result['Email'] = self.email
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.invite_id is not None:
            result['InviteId'] = self.invite_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountNickname') is not None:
            self.account_nickname = m.get('AccountNickname')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('InviteId') is not None:
            self.invite_id = m.get('InviteId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetUnassociatedCustomerResponseBodyInviteInfoList(TeaModel):
    def __init__(
        self,
        invite_info: List[GetUnassociatedCustomerResponseBodyInviteInfoListInviteInfo] = None,
    ):
        self.invite_info = invite_info

    def validate(self):
        if self.invite_info:
            for k in self.invite_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InviteInfo'] = []
        if self.invite_info is not None:
            for k in self.invite_info:
                result['InviteInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.invite_info = []
        if m.get('InviteInfo') is not None:
            for k in m.get('InviteInfo'):
                temp_model = GetUnassociatedCustomerResponseBodyInviteInfoListInviteInfo()
                self.invite_info.append(temp_model.from_map(k))
        return self


class GetUnassociatedCustomerResponseBodyPageInfo(TeaModel):
    def __init__(
        self,
        page: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.page = page
        self.page_size = page_size
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetUnassociatedCustomerResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        invite_info_list: GetUnassociatedCustomerResponseBodyInviteInfoList = None,
        message: str = None,
        page_info: GetUnassociatedCustomerResponseBodyPageInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.invite_info_list = invite_info_list
        self.message = message
        self.page_info = page_info
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.invite_info_list:
            self.invite_info_list.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.invite_info_list is not None:
            result['InviteInfoList'] = self.invite_info_list.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('InviteInfoList') is not None:
            temp_model = GetUnassociatedCustomerResponseBodyInviteInfoList()
            self.invite_info_list = temp_model.from_map(m['InviteInfoList'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageInfo') is not None:
            temp_model = GetUnassociatedCustomerResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetUnassociatedCustomerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUnassociatedCustomerResponseBody = None,
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
            temp_model = GetUnassociatedCustomerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InviteSubAccountRequestAccountInfoList(TeaModel):
    def __init__(
        self,
        account_nickname: str = None,
        credit_line: str = None,
        customer_id: str = None,
        email_address: str = None,
        new_buy_status: str = None,
        remark: str = None,
        sub_account_type: str = None,
        zero_credit_shutdown_policy: str = None,
    ):
        self.account_nickname = account_nickname
        self.credit_line = credit_line
        self.customer_id = customer_id
        self.email_address = email_address
        self.new_buy_status = new_buy_status
        self.remark = remark
        self.sub_account_type = sub_account_type
        self.zero_credit_shutdown_policy = zero_credit_shutdown_policy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_nickname is not None:
            result['AccountNickname'] = self.account_nickname
        if self.credit_line is not None:
            result['CreditLine'] = self.credit_line
        if self.customer_id is not None:
            result['CustomerId'] = self.customer_id
        if self.email_address is not None:
            result['EmailAddress'] = self.email_address
        if self.new_buy_status is not None:
            result['NewBuyStatus'] = self.new_buy_status
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.sub_account_type is not None:
            result['SubAccountType'] = self.sub_account_type
        if self.zero_credit_shutdown_policy is not None:
            result['ZeroCreditShutdownPolicy'] = self.zero_credit_shutdown_policy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountNickname') is not None:
            self.account_nickname = m.get('AccountNickname')
        if m.get('CreditLine') is not None:
            self.credit_line = m.get('CreditLine')
        if m.get('CustomerId') is not None:
            self.customer_id = m.get('CustomerId')
        if m.get('EmailAddress') is not None:
            self.email_address = m.get('EmailAddress')
        if m.get('NewBuyStatus') is not None:
            self.new_buy_status = m.get('NewBuyStatus')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('SubAccountType') is not None:
            self.sub_account_type = m.get('SubAccountType')
        if m.get('ZeroCreditShutdownPolicy') is not None:
            self.zero_credit_shutdown_policy = m.get('ZeroCreditShutdownPolicy')
        return self


class InviteSubAccountRequest(TeaModel):
    def __init__(
        self,
        account_info_list: List[InviteSubAccountRequestAccountInfoList] = None,
    ):
        self.account_info_list = account_info_list

    def validate(self):
        if self.account_info_list:
            for k in self.account_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AccountInfoList'] = []
        if self.account_info_list is not None:
            for k in self.account_info_list:
                result['AccountInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.account_info_list = []
        if m.get('AccountInfoList') is not None:
            for k in m.get('AccountInfoList'):
                temp_model = InviteSubAccountRequestAccountInfoList()
                self.account_info_list.append(temp_model.from_map(k))
        return self


class InviteSubAccountResponseBodyResultsResultResult(TeaModel):
    def __init__(
        self,
        days: int = None,
        invite_id: int = None,
        reg_url: str = None,
    ):
        self.days = days
        self.invite_id = invite_id
        self.reg_url = reg_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.days is not None:
            result['Days'] = self.days
        if self.invite_id is not None:
            result['InviteId'] = self.invite_id
        if self.reg_url is not None:
            result['RegUrl'] = self.reg_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Days') is not None:
            self.days = m.get('Days')
        if m.get('InviteId') is not None:
            self.invite_id = m.get('InviteId')
        if m.get('RegUrl') is not None:
            self.reg_url = m.get('RegUrl')
        return self


class InviteSubAccountResponseBodyResultsResult(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        result: InviteSubAccountResponseBodyResultsResultResult = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Result') is not None:
            temp_model = InviteSubAccountResponseBodyResultsResultResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class InviteSubAccountResponseBodyResults(TeaModel):
    def __init__(
        self,
        result: List[InviteSubAccountResponseBodyResultsResult] = None,
    ):
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = InviteSubAccountResponseBodyResultsResult()
                self.result.append(temp_model.from_map(k))
        return self


class InviteSubAccountResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        results: InviteSubAccountResponseBodyResults = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.results = results
        self.success = success

    def validate(self):
        if self.results:
            self.results.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.results is not None:
            result['Results'] = self.results.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Results') is not None:
            temp_model = InviteSubAccountResponseBodyResults()
            self.results = temp_model.from_map(m['Results'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class InviteSubAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InviteSubAccountResponseBody = None,
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
            temp_model = InviteSubAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCountriesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[str] = None,
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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListCountriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCountriesResponseBody = None,
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
            temp_model = ListCountriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResendEmailRequest(TeaModel):
    def __init__(
        self,
        invite_id: int = None,
    ):
        self.invite_id = invite_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.invite_id is not None:
            result['InviteId'] = self.invite_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InviteId') is not None:
            self.invite_id = m.get('InviteId')
        return self


class ResendEmailResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
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
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ResendEmailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResendEmailResponseBody = None,
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
            temp_model = ResendEmailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetAccountInfoRequest(TeaModel):
    def __init__(
        self,
        account_nickname: str = None,
        remark: str = None,
        uid: int = None,
    ):
        self.account_nickname = account_nickname
        self.remark = remark
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_nickname is not None:
            result['AccountNickname'] = self.account_nickname
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountNickname') is not None:
            self.account_nickname = m.get('AccountNickname')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class SetAccountInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
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
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SetAccountInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetAccountInfoResponseBody = None,
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
            temp_model = SetAccountInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetCreditLineRequest(TeaModel):
    def __init__(
        self,
        credit_line: str = None,
        uid: int = None,
    ):
        self.credit_line = credit_line
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credit_line is not None:
            result['CreditLine'] = self.credit_line
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreditLine') is not None:
            self.credit_line = m.get('CreditLine')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class SetCreditLineResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
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
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SetCreditLineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetCreditLineResponseBody = None,
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
            temp_model = SetCreditLineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetWarningThresholdRequest(TeaModel):
    def __init__(
        self,
        uid: int = None,
        warning_value: str = None,
    ):
        self.uid = uid
        self.warning_value = warning_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.warning_value is not None:
            result['WarningValue'] = self.warning_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('WarningValue') is not None:
            self.warning_value = m.get('WarningValue')
        return self


class SetWarningThresholdResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
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
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SetWarningThresholdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetWarningThresholdResponseBody = None,
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
            temp_model = SetWarningThresholdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubscriptionBillRequest(TeaModel):
    def __init__(
        self,
        begin_billing_cycle: str = None,
        bill_format: str = None,
        bucket_owner_id: int = None,
        subscribe_bucket: str = None,
        subscribe_segment_size: int = None,
        subscribe_type: str = None,
    ):
        # The start month from which the bills are pushed. Specify the value in the yyyy-MM format.
        # 
        # After the subscription is generated, the system automatically pushes the bill data that is generated from the month that you specified to the current point in time. Data of up to six months can be pushed. The current month is included. If you subscribe to the bills for more than six months, the subscription is invalid.
        self.begin_billing_cycle = begin_billing_cycle
        # The file format of the bill. Valid values: csv and parquet.
        # 
        # If you subscribe to the bills of multiple file formats, we recommend that you store the bills in different OSS buckets to prevent file overwriting.
        self.bill_format = bill_format
        # The ID of the user to which the OSS bucket belongs.
        # 
        # If you are an eco-partner of Alibaba Cloud and you need to push the bills to the OSS bucket of a subordinate partner account, you must set this parameter to the ID of the subordinate partner account and grant the [AliyunConsumeDump2OSSRole](https://ram.console.aliyun.com/?spm=api-workbench.API%20Document.0.0.68c71e0fhmTSJp#/role/authorize?request=%7B%22Requests%22:%20%7B%22request1%22:%20%7B%22RoleName%22:%20%22AliyunConsumeDump2OSSRole%22,%20%22TemplateId%22:%20%22Dump2OSSRole%22%7D%7D,%20%22ReturnUrl%22:%20%22https:%2F%2Fusercenter2.aliyun.com%22,%20%22Service%22:%20%22Consume%22%7D) permission to the subordinate partner account.
        # 
        # If you are an eco-partner of Alibaba Cloud and you need to push the bills to the OSS bucket of your own account, your account must be granted the [AliyunConsumeDump2OSSRole](https://ram.console.aliyun.com/?spm=api-workbench.API%20Document.0.0.68c71e0fhmTSJp#/role/authorize?request=%7B%22Requests%22:%20%7B%22request1%22:%20%7B%22RoleName%22:%20%22AliyunConsumeDump2OSSRole%22,%20%22TemplateId%22:%20%22Dump2OSSRole%22%7D%7D,%20%22ReturnUrl%22:%20%22https:%2F%2Fusercenter2.aliyun.com%22,%20%22Service%22:%20%22Consume%22%7D) permission.
        self.bucket_owner_id = bucket_owner_id
        # The name of the Object Storage Service (OSS) bucket in which you want to store the bills.
        self.subscribe_bucket = subscribe_bucket
        # The maximum rows in a single bill file. If the number of bill rows exceed the upper limit, the bill is automatically split into multiple files. The name of each split file is in the `uid_billType_billCycle_SquenceNo_fileNo` format.
        # 
        # Files whose names are the same except for the fileNo field are of the same type and belong to the same billing cycle.
        self.subscribe_segment_size = subscribe_segment_size
        # The type of the bill to which you want to subscribe. Valid values: PartnerBillingItemDetailForBillingPeriod, PartnerBillingItemDetailMonthly, PartnerInstanceDetailForBillingPeriod, and PartnerInstanceDetailMonthly.
        self.subscribe_type = subscribe_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_billing_cycle is not None:
            result['BeginBillingCycle'] = self.begin_billing_cycle
        if self.bill_format is not None:
            result['BillFormat'] = self.bill_format
        if self.bucket_owner_id is not None:
            result['BucketOwnerId'] = self.bucket_owner_id
        if self.subscribe_bucket is not None:
            result['SubscribeBucket'] = self.subscribe_bucket
        if self.subscribe_segment_size is not None:
            result['SubscribeSegmentSize'] = self.subscribe_segment_size
        if self.subscribe_type is not None:
            result['SubscribeType'] = self.subscribe_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginBillingCycle') is not None:
            self.begin_billing_cycle = m.get('BeginBillingCycle')
        if m.get('BillFormat') is not None:
            self.bill_format = m.get('BillFormat')
        if m.get('BucketOwnerId') is not None:
            self.bucket_owner_id = m.get('BucketOwnerId')
        if m.get('SubscribeBucket') is not None:
            self.subscribe_bucket = m.get('SubscribeBucket')
        if m.get('SubscribeSegmentSize') is not None:
            self.subscribe_segment_size = m.get('SubscribeSegmentSize')
        if m.get('SubscribeType') is not None:
            self.subscribe_type = m.get('SubscribeType')
        return self


class SubscriptionBillResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code that is returned.
        self.code = code
        # The data that is returned.
        self.data = data
        # The message that is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful.
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
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SubscriptionBillResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubscriptionBillResponseBody = None,
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
            temp_model = SubscriptionBillResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


