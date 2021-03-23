# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class AllocateCostUnitResourceRequestResourceInstanceList(TeaModel):
    def __init__(
        self,
        apportion_code: str = None,
        commodity_code: str = None,
        resource_id: str = None,
        resource_user_id: int = None,
    ):
        self.apportion_code = apportion_code
        self.commodity_code = commodity_code
        self.resource_id = resource_id
        self.resource_user_id = resource_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.apportion_code is not None:
            result['ApportionCode'] = self.apportion_code
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_user_id is not None:
            result['ResourceUserId'] = self.resource_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApportionCode') is not None:
            self.apportion_code = m.get('ApportionCode')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceUserId') is not None:
            self.resource_user_id = m.get('ResourceUserId')
        return self


class AllocateCostUnitResourceRequest(TeaModel):
    def __init__(
        self,
        from_unit_user_id: int = None,
        from_unit_id: int = None,
        to_unit_user_id: int = None,
        to_unit_id: int = None,
        resource_instance_list: List[AllocateCostUnitResourceRequestResourceInstanceList] = None,
    ):
        self.from_unit_user_id = from_unit_user_id
        self.from_unit_id = from_unit_id
        self.to_unit_user_id = to_unit_user_id
        self.to_unit_id = to_unit_id
        self.resource_instance_list = resource_instance_list

    def validate(self):
        if self.resource_instance_list:
            for k in self.resource_instance_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.from_unit_user_id is not None:
            result['FromUnitUserId'] = self.from_unit_user_id
        if self.from_unit_id is not None:
            result['FromUnitId'] = self.from_unit_id
        if self.to_unit_user_id is not None:
            result['ToUnitUserId'] = self.to_unit_user_id
        if self.to_unit_id is not None:
            result['ToUnitId'] = self.to_unit_id
        result['ResourceInstanceList'] = []
        if self.resource_instance_list is not None:
            for k in self.resource_instance_list:
                result['ResourceInstanceList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromUnitUserId') is not None:
            self.from_unit_user_id = m.get('FromUnitUserId')
        if m.get('FromUnitId') is not None:
            self.from_unit_id = m.get('FromUnitId')
        if m.get('ToUnitUserId') is not None:
            self.to_unit_user_id = m.get('ToUnitUserId')
        if m.get('ToUnitId') is not None:
            self.to_unit_id = m.get('ToUnitId')
        self.resource_instance_list = []
        if m.get('ResourceInstanceList') is not None:
            for k in m.get('ResourceInstanceList'):
                temp_model = AllocateCostUnitResourceRequestResourceInstanceList()
                self.resource_instance_list.append(temp_model.from_map(k))
        return self


class AllocateCostUnitResourceResponseBodyData(TeaModel):
    def __init__(
        self,
        is_success: bool = None,
        to_unit_user_id: int = None,
        to_unit_id: int = None,
    ):
        self.is_success = is_success
        self.to_unit_user_id = to_unit_user_id
        self.to_unit_id = to_unit_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.to_unit_user_id is not None:
            result['ToUnitUserId'] = self.to_unit_user_id
        if self.to_unit_id is not None:
            result['ToUnitId'] = self.to_unit_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('ToUnitUserId') is not None:
            self.to_unit_user_id = m.get('ToUnitUserId')
        if m.get('ToUnitId') is not None:
            self.to_unit_id = m.get('ToUnitId')
        return self


class AllocateCostUnitResourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        code: str = None,
        success: bool = None,
        data: AllocateCostUnitResourceResponseBodyData = None,
    ):
        self.request_id = request_id
        self.message = message
        self.code = code
        self.success = success
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Data') is not None:
            temp_model = AllocateCostUnitResourceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class AllocateCostUnitResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AllocateCostUnitResourceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = AllocateCostUnitResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApplyInvoiceRequest(TeaModel):
    def __init__(
        self,
        invoice_amount: int = None,
        owner_id: int = None,
        customer_id: int = None,
        address_id: int = None,
        invoicing_type: int = None,
        process_way: int = None,
        apply_user_nick: str = None,
        selected_ids: List[int] = None,
        invoice_by_amount: bool = None,
    ):
        self.invoice_amount = invoice_amount
        self.owner_id = owner_id
        self.customer_id = customer_id
        self.address_id = address_id
        self.invoicing_type = invoicing_type
        self.process_way = process_way
        self.apply_user_nick = apply_user_nick
        self.selected_ids = selected_ids
        self.invoice_by_amount = invoice_by_amount

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.invoice_amount is not None:
            result['InvoiceAmount'] = self.invoice_amount
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.customer_id is not None:
            result['CustomerId'] = self.customer_id
        if self.address_id is not None:
            result['AddressId'] = self.address_id
        if self.invoicing_type is not None:
            result['InvoicingType'] = self.invoicing_type
        if self.process_way is not None:
            result['ProcessWay'] = self.process_way
        if self.apply_user_nick is not None:
            result['ApplyUserNick'] = self.apply_user_nick
        if self.selected_ids is not None:
            result['SelectedIds'] = self.selected_ids
        if self.invoice_by_amount is not None:
            result['InvoiceByAmount'] = self.invoice_by_amount
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InvoiceAmount') is not None:
            self.invoice_amount = m.get('InvoiceAmount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('CustomerId') is not None:
            self.customer_id = m.get('CustomerId')
        if m.get('AddressId') is not None:
            self.address_id = m.get('AddressId')
        if m.get('InvoicingType') is not None:
            self.invoicing_type = m.get('InvoicingType')
        if m.get('ProcessWay') is not None:
            self.process_way = m.get('ProcessWay')
        if m.get('ApplyUserNick') is not None:
            self.apply_user_nick = m.get('ApplyUserNick')
        if m.get('SelectedIds') is not None:
            self.selected_ids = m.get('SelectedIds')
        if m.get('InvoiceByAmount') is not None:
            self.invoice_by_amount = m.get('InvoiceByAmount')
        return self


class ApplyInvoiceResponseBodyData(TeaModel):
    def __init__(
        self,
        invoice_apply_id: int = None,
    ):
        self.invoice_apply_id = invoice_apply_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.invoice_apply_id is not None:
            result['InvoiceApplyId'] = self.invoice_apply_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InvoiceApplyId') is not None:
            self.invoice_apply_id = m.get('InvoiceApplyId')
        return self


class ApplyInvoiceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        data: ApplyInvoiceResponseBodyData = None,
    ):
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = ApplyInvoiceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class ApplyInvoiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ApplyInvoiceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ApplyInvoiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelOrderRequest(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        owner_id: int = None,
    ):
        self.order_id = order_id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class CancelOrderResponseBodyData(TeaModel):
    def __init__(
        self,
        host_id: str = None,
    ):
        self.host_id = host_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        return self


class CancelOrderResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        data: CancelOrderResponseBodyData = None,
    ):
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = CancelOrderResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class CancelOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CancelOrderResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = CancelOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeResellerConsumeAmountRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        adjust_type: str = None,
        amount: str = None,
        currency: str = None,
        business_type: str = None,
        source: str = None,
        out_biz_id: str = None,
        extend_map: str = None,
    ):
        self.owner_id = owner_id
        self.adjust_type = adjust_type
        self.amount = amount
        self.currency = currency
        self.business_type = business_type
        self.source = source
        self.out_biz_id = out_biz_id
        self.extend_map = extend_map

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.adjust_type is not None:
            result['AdjustType'] = self.adjust_type
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.source is not None:
            result['Source'] = self.source
        if self.out_biz_id is not None:
            result['OutBizId'] = self.out_biz_id
        if self.extend_map is not None:
            result['ExtendMap'] = self.extend_map
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('AdjustType') is not None:
            self.adjust_type = m.get('AdjustType')
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('OutBizId') is not None:
            self.out_biz_id = m.get('OutBizId')
        if m.get('ExtendMap') is not None:
            self.extend_map = m.get('ExtendMap')
        return self


class ChangeResellerConsumeAmountResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
        success: bool = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.message = message
        self.success = success
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class ChangeResellerConsumeAmountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ChangeResellerConsumeAmountResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ChangeResellerConsumeAmountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConvertChargeTypeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        product_type: str = None,
        subscription_type: str = None,
        period: int = None,
        product_code: str = None,
        instance_id: str = None,
    ):
        self.owner_id = owner_id
        self.product_type = product_type
        self.subscription_type = subscription_type
        self.period = period
        self.product_code = product_code
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.period is not None:
            result['Period'] = self.period
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ConvertChargeTypeResponseBodyData(TeaModel):
    def __init__(
        self,
        order_id: str = None,
    ):
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class ConvertChargeTypeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        data: ConvertChargeTypeResponseBodyData = None,
    ):
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = ConvertChargeTypeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class ConvertChargeTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ConvertChargeTypeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ConvertChargeTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAgAccountRequest(TeaModel):
    def __init__(
        self,
        login_email: str = None,
        account_attr: str = None,
        enterprise_name: str = None,
        first_name: str = None,
        last_name: str = None,
        nation_code: str = None,
        province_name: str = None,
        city_name: str = None,
        postcode: str = None,
    ):
        self.login_email = login_email
        self.account_attr = account_attr
        self.enterprise_name = enterprise_name
        self.first_name = first_name
        self.last_name = last_name
        self.nation_code = nation_code
        self.province_name = province_name
        self.city_name = city_name
        self.postcode = postcode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.login_email is not None:
            result['LoginEmail'] = self.login_email
        if self.account_attr is not None:
            result['AccountAttr'] = self.account_attr
        if self.enterprise_name is not None:
            result['EnterpriseName'] = self.enterprise_name
        if self.first_name is not None:
            result['FirstName'] = self.first_name
        if self.last_name is not None:
            result['LastName'] = self.last_name
        if self.nation_code is not None:
            result['NationCode'] = self.nation_code
        if self.province_name is not None:
            result['ProvinceName'] = self.province_name
        if self.city_name is not None:
            result['CityName'] = self.city_name
        if self.postcode is not None:
            result['Postcode'] = self.postcode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoginEmail') is not None:
            self.login_email = m.get('LoginEmail')
        if m.get('AccountAttr') is not None:
            self.account_attr = m.get('AccountAttr')
        if m.get('EnterpriseName') is not None:
            self.enterprise_name = m.get('EnterpriseName')
        if m.get('FirstName') is not None:
            self.first_name = m.get('FirstName')
        if m.get('LastName') is not None:
            self.last_name = m.get('LastName')
        if m.get('NationCode') is not None:
            self.nation_code = m.get('NationCode')
        if m.get('ProvinceName') is not None:
            self.province_name = m.get('ProvinceName')
        if m.get('CityName') is not None:
            self.city_name = m.get('CityName')
        if m.get('Postcode') is not None:
            self.postcode = m.get('Postcode')
        return self


class CreateAgAccountResponseBodyAgRelationDto(TeaModel):
    def __init__(
        self,
        pk: str = None,
        type: str = None,
        mpk: str = None,
        ram_admin_role_name: str = None,
    ):
        self.pk = pk
        self.type = type
        self.mpk = mpk
        self.ram_admin_role_name = ram_admin_role_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.pk is not None:
            result['Pk'] = self.pk
        if self.type is not None:
            result['Type'] = self.type
        if self.mpk is not None:
            result['Mpk'] = self.mpk
        if self.ram_admin_role_name is not None:
            result['RamAdminRoleName'] = self.ram_admin_role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Mpk') is not None:
            self.mpk = m.get('Mpk')
        if m.get('RamAdminRoleName') is not None:
            self.ram_admin_role_name = m.get('RamAdminRoleName')
        return self


class CreateAgAccountResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
        success: bool = None,
        ag_relation_dto: CreateAgAccountResponseBodyAgRelationDto = None,
    ):
        self.request_id = request_id
        self.code = code
        self.message = message
        self.success = success
        self.ag_relation_dto = ag_relation_dto

    def validate(self):
        if self.ag_relation_dto:
            self.ag_relation_dto.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        if self.ag_relation_dto is not None:
            result['AgRelationDto'] = self.ag_relation_dto.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('AgRelationDto') is not None:
            temp_model = CreateAgAccountResponseBodyAgRelationDto()
            self.ag_relation_dto = temp_model.from_map(m['AgRelationDto'])
        return self


class CreateAgAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAgAccountResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = CreateAgAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCostUnitRequestUnitEntityList(TeaModel):
    def __init__(
        self,
        owner_uid: int = None,
        parent_unit_id: int = None,
        unit_name: str = None,
    ):
        self.owner_uid = owner_uid
        self.parent_unit_id = parent_unit_id
        self.unit_name = unit_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid
        if self.parent_unit_id is not None:
            result['ParentUnitId'] = self.parent_unit_id
        if self.unit_name is not None:
            result['UnitName'] = self.unit_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')
        if m.get('ParentUnitId') is not None:
            self.parent_unit_id = m.get('ParentUnitId')
        if m.get('UnitName') is not None:
            self.unit_name = m.get('UnitName')
        return self


class CreateCostUnitRequest(TeaModel):
    def __init__(
        self,
        unit_entity_list: List[CreateCostUnitRequestUnitEntityList] = None,
    ):
        self.unit_entity_list = unit_entity_list

    def validate(self):
        if self.unit_entity_list:
            for k in self.unit_entity_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['UnitEntityList'] = []
        if self.unit_entity_list is not None:
            for k in self.unit_entity_list:
                result['UnitEntityList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.unit_entity_list = []
        if m.get('UnitEntityList') is not None:
            for k in m.get('UnitEntityList'):
                temp_model = CreateCostUnitRequestUnitEntityList()
                self.unit_entity_list.append(temp_model.from_map(k))
        return self


class CreateCostUnitResponseBodyDataCostUnitDtoList(TeaModel):
    def __init__(
        self,
        unit_id: int = None,
        parent_unit_id: int = None,
        owner_uid: int = None,
        unit_name: str = None,
    ):
        self.unit_id = unit_id
        self.parent_unit_id = parent_unit_id
        self.owner_uid = owner_uid
        self.unit_name = unit_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.unit_id is not None:
            result['UnitId'] = self.unit_id
        if self.parent_unit_id is not None:
            result['ParentUnitId'] = self.parent_unit_id
        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid
        if self.unit_name is not None:
            result['UnitName'] = self.unit_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UnitId') is not None:
            self.unit_id = m.get('UnitId')
        if m.get('ParentUnitId') is not None:
            self.parent_unit_id = m.get('ParentUnitId')
        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')
        if m.get('UnitName') is not None:
            self.unit_name = m.get('UnitName')
        return self


class CreateCostUnitResponseBodyData(TeaModel):
    def __init__(
        self,
        cost_unit_dto_list: List[CreateCostUnitResponseBodyDataCostUnitDtoList] = None,
    ):
        self.cost_unit_dto_list = cost_unit_dto_list

    def validate(self):
        if self.cost_unit_dto_list:
            for k in self.cost_unit_dto_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['CostUnitDtoList'] = []
        if self.cost_unit_dto_list is not None:
            for k in self.cost_unit_dto_list:
                result['CostUnitDtoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cost_unit_dto_list = []
        if m.get('CostUnitDtoList') is not None:
            for k in m.get('CostUnitDtoList'):
                temp_model = CreateCostUnitResponseBodyDataCostUnitDtoList()
                self.cost_unit_dto_list.append(temp_model.from_map(k))
        return self


class CreateCostUnitResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        code: str = None,
        success: bool = None,
        data: CreateCostUnitResponseBodyData = None,
    ):
        self.request_id = request_id
        self.message = message
        self.code = code
        self.success = success
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Data') is not None:
            temp_model = CreateCostUnitResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class CreateCostUnitResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateCostUnitResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = CreateCostUnitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceRequestParameter(TeaModel):
    def __init__(
        self,
        code: str = None,
        value: str = None,
    ):
        self.code = code
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateInstanceRequest(TeaModel):
    def __init__(
        self,
        product_code: str = None,
        parameter: List[CreateInstanceRequestParameter] = None,
        owner_id: int = None,
        product_type: str = None,
        subscription_type: str = None,
        period: int = None,
        renewal_status: str = None,
        renew_period: int = None,
        client_token: str = None,
        logistics: str = None,
    ):
        self.product_code = product_code
        self.parameter = parameter
        self.owner_id = owner_id
        self.product_type = product_type
        self.subscription_type = subscription_type
        self.period = period
        self.renewal_status = renewal_status
        self.renew_period = renew_period
        self.client_token = client_token
        self.logistics = logistics

    def validate(self):
        if self.parameter:
            for k in self.parameter:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        result['Parameter'] = []
        if self.parameter is not None:
            for k in self.parameter:
                result['Parameter'].append(k.to_map() if k else None)
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.period is not None:
            result['Period'] = self.period
        if self.renewal_status is not None:
            result['RenewalStatus'] = self.renewal_status
        if self.renew_period is not None:
            result['RenewPeriod'] = self.renew_period
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.logistics is not None:
            result['Logistics'] = self.logistics
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        self.parameter = []
        if m.get('Parameter') is not None:
            for k in m.get('Parameter'):
                temp_model = CreateInstanceRequestParameter()
                self.parameter.append(temp_model.from_map(k))
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('RenewalStatus') is not None:
            self.renewal_status = m.get('RenewalStatus')
        if m.get('RenewPeriod') is not None:
            self.renew_period = m.get('RenewPeriod')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Logistics') is not None:
            self.logistics = m.get('Logistics')
        return self


class CreateInstanceResponseBodyData(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        order_id: str = None,
    ):
        self.instance_id = instance_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class CreateInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        data: CreateInstanceResponseBodyData = None,
    ):
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = CreateInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class CreateInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = CreateInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateResellerUserQuotaRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        amount: str = None,
        currency: str = None,
        out_biz_id: str = None,
    ):
        self.owner_id = owner_id
        self.amount = amount
        self.currency = currency
        self.out_biz_id = out_biz_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.out_biz_id is not None:
            result['OutBizId'] = self.out_biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('OutBizId') is not None:
            self.out_biz_id = m.get('OutBizId')
        return self


class CreateResellerUserQuotaResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
        success: bool = None,
        data: bool = None,
    ):
        self.request_id = request_id
        self.code = code
        self.message = message
        self.success = success
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class CreateResellerUserQuotaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateResellerUserQuotaResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = CreateResellerUserQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateResourcePackageRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        product_code: str = None,
        package_type: str = None,
        effective_date: str = None,
        specification: str = None,
        duration: int = None,
        pricing_cycle: str = None,
    ):
        self.owner_id = owner_id
        self.product_code = product_code
        self.package_type = package_type
        self.effective_date = effective_date
        self.specification = specification
        self.duration = duration
        self.pricing_cycle = pricing_cycle

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.effective_date is not None:
            result['EffectiveDate'] = self.effective_date
        if self.specification is not None:
            result['Specification'] = self.specification
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('EffectiveDate') is not None:
            self.effective_date = m.get('EffectiveDate')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        return self


class CreateResourcePackageResponseBodyData(TeaModel):
    def __init__(
        self,
        order_id: int = None,
        instance_id: str = None,
    ):
        self.order_id = order_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class CreateResourcePackageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        order_id: int = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        data: CreateResourcePackageResponseBodyData = None,
    ):
        self.request_id = request_id
        self.order_id = order_id
        self.success = success
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = CreateResourcePackageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class CreateResourcePackageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateResourcePackageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = CreateResourcePackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCostUnitRequest(TeaModel):
    def __init__(
        self,
        owner_uid: int = None,
        unit_id: int = None,
    ):
        self.owner_uid = owner_uid
        self.unit_id = unit_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid
        if self.unit_id is not None:
            result['UnitId'] = self.unit_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')
        if m.get('UnitId') is not None:
            self.unit_id = m.get('UnitId')
        return self


class DeleteCostUnitResponseBodyData(TeaModel):
    def __init__(
        self,
        is_success: bool = None,
        unit_id: int = None,
        owner_uid: int = None,
    ):
        self.is_success = is_success
        self.unit_id = unit_id
        self.owner_uid = owner_uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.unit_id is not None:
            result['UnitId'] = self.unit_id
        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('UnitId') is not None:
            self.unit_id = m.get('UnitId')
        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')
        return self


class DeleteCostUnitResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        code: str = None,
        success: bool = None,
        data: DeleteCostUnitResponseBodyData = None,
    ):
        self.request_id = request_id
        self.message = message
        self.code = code
        self.success = success
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Data') is not None:
            temp_model = DeleteCostUnitResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DeleteCostUnitResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteCostUnitResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DeleteCostUnitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePricingModuleRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        product_code: str = None,
        product_type: str = None,
        subscription_type: str = None,
    ):
        self.owner_id = owner_id
        self.product_code = product_code
        self.product_type = product_type
        self.subscription_type = subscription_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        return self


class DescribePricingModuleResponseBodyDataModuleListModuleConfigList(TeaModel):
    def __init__(
        self,
        config_list: List[str] = None,
    ):
        self.config_list = config_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.config_list is not None:
            result['ConfigList'] = self.config_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigList') is not None:
            self.config_list = m.get('ConfigList')
        return self


class DescribePricingModuleResponseBodyDataModuleListModule(TeaModel):
    def __init__(
        self,
        module_code: str = None,
        module_name: str = None,
        price_type: str = None,
        currency: str = None,
        config_list: DescribePricingModuleResponseBodyDataModuleListModuleConfigList = None,
    ):
        self.module_code = module_code
        self.module_name = module_name
        self.price_type = price_type
        self.currency = currency
        self.config_list = config_list

    def validate(self):
        if self.config_list:
            self.config_list.validate()

    def to_map(self):
        result = dict()
        if self.module_code is not None:
            result['ModuleCode'] = self.module_code
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        if self.price_type is not None:
            result['PriceType'] = self.price_type
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.config_list is not None:
            result['ConfigList'] = self.config_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModuleCode') is not None:
            self.module_code = m.get('ModuleCode')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        if m.get('PriceType') is not None:
            self.price_type = m.get('PriceType')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('ConfigList') is not None:
            temp_model = DescribePricingModuleResponseBodyDataModuleListModuleConfigList()
            self.config_list = temp_model.from_map(m['ConfigList'])
        return self


class DescribePricingModuleResponseBodyDataModuleList(TeaModel):
    def __init__(
        self,
        module: List[DescribePricingModuleResponseBodyDataModuleListModule] = None,
    ):
        self.module = module

    def validate(self):
        if self.module:
            for k in self.module:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Module'] = []
        if self.module is not None:
            for k in self.module:
                result['Module'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.module = []
        if m.get('Module') is not None:
            for k in m.get('Module'):
                temp_model = DescribePricingModuleResponseBodyDataModuleListModule()
                self.module.append(temp_model.from_map(k))
        return self


class DescribePricingModuleResponseBodyDataAttributeListAttributeValuesAttributeValue(TeaModel):
    def __init__(
        self,
        type: str = None,
        name: str = None,
        value: str = None,
        remark: str = None,
    ):
        self.type = type
        self.name = name
        self.value = value
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class DescribePricingModuleResponseBodyDataAttributeListAttributeValues(TeaModel):
    def __init__(
        self,
        attribute_value: List[DescribePricingModuleResponseBodyDataAttributeListAttributeValuesAttributeValue] = None,
    ):
        self.attribute_value = attribute_value

    def validate(self):
        if self.attribute_value:
            for k in self.attribute_value:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['AttributeValue'] = []
        if self.attribute_value is not None:
            for k in self.attribute_value:
                result['AttributeValue'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attribute_value = []
        if m.get('AttributeValue') is not None:
            for k in m.get('AttributeValue'):
                temp_model = DescribePricingModuleResponseBodyDataAttributeListAttributeValuesAttributeValue()
                self.attribute_value.append(temp_model.from_map(k))
        return self


class DescribePricingModuleResponseBodyDataAttributeListAttribute(TeaModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
        unit: str = None,
        values: DescribePricingModuleResponseBodyDataAttributeListAttributeValues = None,
    ):
        self.code = code
        self.name = name
        self.unit = unit
        self.values = values

    def validate(self):
        if self.values:
            self.values.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.name is not None:
            result['Name'] = self.name
        if self.unit is not None:
            result['Unit'] = self.unit
        if self.values is not None:
            result['Values'] = self.values.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Unit') is not None:
            self.unit = m.get('Unit')
        if m.get('Values') is not None:
            temp_model = DescribePricingModuleResponseBodyDataAttributeListAttributeValues()
            self.values = temp_model.from_map(m['Values'])
        return self


class DescribePricingModuleResponseBodyDataAttributeList(TeaModel):
    def __init__(
        self,
        attribute: List[DescribePricingModuleResponseBodyDataAttributeListAttribute] = None,
    ):
        self.attribute = attribute

    def validate(self):
        if self.attribute:
            for k in self.attribute:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Attribute'] = []
        if self.attribute is not None:
            for k in self.attribute:
                result['Attribute'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attribute = []
        if m.get('Attribute') is not None:
            for k in m.get('Attribute'):
                temp_model = DescribePricingModuleResponseBodyDataAttributeListAttribute()
                self.attribute.append(temp_model.from_map(k))
        return self


class DescribePricingModuleResponseBodyData(TeaModel):
    def __init__(
        self,
        module_list: DescribePricingModuleResponseBodyDataModuleList = None,
        attribute_list: DescribePricingModuleResponseBodyDataAttributeList = None,
    ):
        self.module_list = module_list
        self.attribute_list = attribute_list

    def validate(self):
        if self.module_list:
            self.module_list.validate()
        if self.attribute_list:
            self.attribute_list.validate()

    def to_map(self):
        result = dict()
        if self.module_list is not None:
            result['ModuleList'] = self.module_list.to_map()
        if self.attribute_list is not None:
            result['AttributeList'] = self.attribute_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModuleList') is not None:
            temp_model = DescribePricingModuleResponseBodyDataModuleList()
            self.module_list = temp_model.from_map(m['ModuleList'])
        if m.get('AttributeList') is not None:
            temp_model = DescribePricingModuleResponseBodyDataAttributeList()
            self.attribute_list = temp_model.from_map(m['AttributeList'])
        return self


class DescribePricingModuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        data: DescribePricingModuleResponseBodyData = None,
    ):
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = DescribePricingModuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DescribePricingModuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePricingModuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribePricingModuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeResourcePackageProductRequest(TeaModel):
    def __init__(
        self,
        product_code: str = None,
    ):
        self.product_code = product_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageTypePropertiesProperty(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageTypeProperties(TeaModel):
    def __init__(
        self,
        property: List[DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageTypePropertiesProperty] = None,
    ):
        self.property = property

    def validate(self):
        if self.property:
            for k in self.property:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Property'] = []
        if self.property is not None:
            for k in self.property:
                result['Property'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.property = []
        if m.get('Property') is not None:
            for k in m.get('Property'):
                temp_model = DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageTypePropertiesProperty()
                self.property.append(temp_model.from_map(k))
        return self


class DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageTypeSpecificationsSpecificationAvailableDurationsAvailableDuration(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: int = None,
        unit: str = None,
    ):
        self.name = name
        self.value = value
        self.unit = unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        if self.unit is not None:
            result['Unit'] = self.unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Unit') is not None:
            self.unit = m.get('Unit')
        return self


class DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageTypeSpecificationsSpecificationAvailableDurations(TeaModel):
    def __init__(
        self,
        available_duration: List[DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageTypeSpecificationsSpecificationAvailableDurationsAvailableDuration] = None,
    ):
        self.available_duration = available_duration

    def validate(self):
        if self.available_duration:
            for k in self.available_duration:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['AvailableDuration'] = []
        if self.available_duration is not None:
            for k in self.available_duration:
                result['AvailableDuration'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.available_duration = []
        if m.get('AvailableDuration') is not None:
            for k in m.get('AvailableDuration'):
                temp_model = DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageTypeSpecificationsSpecificationAvailableDurationsAvailableDuration()
                self.available_duration.append(temp_model.from_map(k))
        return self


class DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageTypeSpecificationsSpecification(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
        available_durations: DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageTypeSpecificationsSpecificationAvailableDurations = None,
    ):
        self.name = name
        self.value = value
        self.available_durations = available_durations

    def validate(self):
        if self.available_durations:
            self.available_durations.validate()

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        if self.available_durations is not None:
            result['AvailableDurations'] = self.available_durations.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('AvailableDurations') is not None:
            temp_model = DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageTypeSpecificationsSpecificationAvailableDurations()
            self.available_durations = temp_model.from_map(m['AvailableDurations'])
        return self


class DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageTypeSpecifications(TeaModel):
    def __init__(
        self,
        specification: List[DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageTypeSpecificationsSpecification] = None,
    ):
        self.specification = specification

    def validate(self):
        if self.specification:
            for k in self.specification:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Specification'] = []
        if self.specification is not None:
            for k in self.specification:
                result['Specification'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.specification = []
        if m.get('Specification') is not None:
            for k in m.get('Specification'):
                temp_model = DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageTypeSpecificationsSpecification()
                self.specification.append(temp_model.from_map(k))
        return self


class DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageType(TeaModel):
    def __init__(
        self,
        name: str = None,
        code: str = None,
        properties: DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageTypeProperties = None,
        specifications: DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageTypeSpecifications = None,
    ):
        self.name = name
        self.code = code
        self.properties = properties
        self.specifications = specifications

    def validate(self):
        if self.properties:
            self.properties.validate()
        if self.specifications:
            self.specifications.validate()

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.code is not None:
            result['Code'] = self.code
        if self.properties is not None:
            result['Properties'] = self.properties.to_map()
        if self.specifications is not None:
            result['Specifications'] = self.specifications.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Properties') is not None:
            temp_model = DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageTypeProperties()
            self.properties = temp_model.from_map(m['Properties'])
        if m.get('Specifications') is not None:
            temp_model = DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageTypeSpecifications()
            self.specifications = temp_model.from_map(m['Specifications'])
        return self


class DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypes(TeaModel):
    def __init__(
        self,
        package_type: List[DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageType] = None,
    ):
        self.package_type = package_type

    def validate(self):
        if self.package_type:
            for k in self.package_type:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['PackageType'] = []
        if self.package_type is not None:
            for k in self.package_type:
                result['PackageType'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.package_type = []
        if m.get('PackageType') is not None:
            for k in m.get('PackageType'):
                temp_model = DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageType()
                self.package_type.append(temp_model.from_map(k))
        return self


class DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackage(TeaModel):
    def __init__(
        self,
        product_code: str = None,
        product_type: str = None,
        name: str = None,
        package_types: DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypes = None,
    ):
        self.product_code = product_code
        self.product_type = product_type
        self.name = name
        self.package_types = package_types

    def validate(self):
        if self.package_types:
            self.package_types.validate()

    def to_map(self):
        result = dict()
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.name is not None:
            result['Name'] = self.name
        if self.package_types is not None:
            result['PackageTypes'] = self.package_types.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PackageTypes') is not None:
            temp_model = DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypes()
            self.package_types = temp_model.from_map(m['PackageTypes'])
        return self


class DescribeResourcePackageProductResponseBodyDataResourcePackages(TeaModel):
    def __init__(
        self,
        resource_package: List[DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackage] = None,
    ):
        self.resource_package = resource_package

    def validate(self):
        if self.resource_package:
            for k in self.resource_package:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ResourcePackage'] = []
        if self.resource_package is not None:
            for k in self.resource_package:
                result['ResourcePackage'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource_package = []
        if m.get('ResourcePackage') is not None:
            for k in m.get('ResourcePackage'):
                temp_model = DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackage()
                self.resource_package.append(temp_model.from_map(k))
        return self


class DescribeResourcePackageProductResponseBodyData(TeaModel):
    def __init__(
        self,
        resource_packages: DescribeResourcePackageProductResponseBodyDataResourcePackages = None,
    ):
        self.resource_packages = resource_packages

    def validate(self):
        if self.resource_packages:
            self.resource_packages.validate()

    def to_map(self):
        result = dict()
        if self.resource_packages is not None:
            result['ResourcePackages'] = self.resource_packages.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourcePackages') is not None:
            temp_model = DescribeResourcePackageProductResponseBodyDataResourcePackages()
            self.resource_packages = temp_model.from_map(m['ResourcePackages'])
        return self


class DescribeResourcePackageProductResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        order_id: int = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        data: DescribeResourcePackageProductResponseBodyData = None,
    ):
        self.request_id = request_id
        self.order_id = order_id
        self.success = success
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = DescribeResourcePackageProductResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DescribeResourcePackageProductResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeResourcePackageProductResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeResourcePackageProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSplitItemBillRequestTagFilter(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_values: List[str] = None,
    ):
        self.tag_key = tag_key
        self.tag_values = tag_values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_values is not None:
            result['TagValues'] = self.tag_values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValues') is not None:
            self.tag_values = m.get('TagValues')
        return self


class DescribeSplitItemBillRequest(TeaModel):
    def __init__(
        self,
        billing_cycle: str = None,
        product_code: str = None,
        product_type: str = None,
        subscription_type: str = None,
        owner_id: int = None,
        next_token: str = None,
        max_results: int = None,
        bill_owner_id: int = None,
        tag_filter: List[DescribeSplitItemBillRequestTagFilter] = None,
        instance_id: str = None,
        split_item_id: str = None,
    ):
        self.billing_cycle = billing_cycle
        self.product_code = product_code
        self.product_type = product_type
        self.subscription_type = subscription_type
        self.owner_id = owner_id
        self.next_token = next_token
        self.max_results = max_results
        self.bill_owner_id = bill_owner_id
        self.tag_filter = tag_filter
        self.instance_id = instance_id
        self.split_item_id = split_item_id

    def validate(self):
        if self.tag_filter:
            for k in self.tag_filter:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.bill_owner_id is not None:
            result['BillOwnerId'] = self.bill_owner_id
        result['TagFilter'] = []
        if self.tag_filter is not None:
            for k in self.tag_filter:
                result['TagFilter'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id
        if self.split_item_id is not None:
            result['SplitItemID'] = self.split_item_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('BillOwnerId') is not None:
            self.bill_owner_id = m.get('BillOwnerId')
        self.tag_filter = []
        if m.get('TagFilter') is not None:
            for k in m.get('TagFilter'):
                temp_model = DescribeSplitItemBillRequestTagFilter()
                self.tag_filter.append(temp_model.from_map(k))
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')
        if m.get('SplitItemID') is not None:
            self.split_item_id = m.get('SplitItemID')
        return self


class DescribeSplitItemBillResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        billing_type: str = None,
        cost_unit: str = None,
        product_code: str = None,
        product_type: str = None,
        subscription_type: str = None,
        product_name: str = None,
        product_detail: str = None,
        owner_id: str = None,
        billing_item: str = None,
        list_price: str = None,
        list_price_unit: str = None,
        usage: str = None,
        usage_unit: str = None,
        deducted_by_resource_package: str = None,
        pretax_gross_amount: float = None,
        invoice_discount: float = None,
        deducted_by_coupons: float = None,
        pretax_amount: float = None,
        deducted_by_cash_coupons: float = None,
        deducted_by_prepaid_card: float = None,
        payment_amount: float = None,
        outstanding_amount: float = None,
        currency: str = None,
        nick_name: str = None,
        resource_group: str = None,
        tag: str = None,
        instance_config: str = None,
        instance_spec: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        region: str = None,
        zone: str = None,
        item: str = None,
        service_period: str = None,
        billing_date: str = None,
        split_item_id: str = None,
        split_item_name: str = None,
        pip_code: str = None,
        commodity_code: str = None,
        service_period_unit: str = None,
        split_commodity_code: str = None,
        split_product_detail: str = None,
        split_account_id: str = None,
        split_account_name: str = None,
        split_billing_cycle: str = None,
    ):
        self.instance_id = instance_id
        self.billing_type = billing_type
        self.cost_unit = cost_unit
        self.product_code = product_code
        self.product_type = product_type
        self.subscription_type = subscription_type
        self.product_name = product_name
        self.product_detail = product_detail
        self.owner_id = owner_id
        self.billing_item = billing_item
        self.list_price = list_price
        self.list_price_unit = list_price_unit
        self.usage = usage
        self.usage_unit = usage_unit
        self.deducted_by_resource_package = deducted_by_resource_package
        self.pretax_gross_amount = pretax_gross_amount
        self.invoice_discount = invoice_discount
        self.deducted_by_coupons = deducted_by_coupons
        self.pretax_amount = pretax_amount
        self.deducted_by_cash_coupons = deducted_by_cash_coupons
        self.deducted_by_prepaid_card = deducted_by_prepaid_card
        self.payment_amount = payment_amount
        self.outstanding_amount = outstanding_amount
        self.currency = currency
        self.nick_name = nick_name
        self.resource_group = resource_group
        self.tag = tag
        self.instance_config = instance_config
        self.instance_spec = instance_spec
        self.internet_ip = internet_ip
        self.intranet_ip = intranet_ip
        self.region = region
        self.zone = zone
        self.item = item
        self.service_period = service_period
        self.billing_date = billing_date
        self.split_item_id = split_item_id
        self.split_item_name = split_item_name
        self.pip_code = pip_code
        self.commodity_code = commodity_code
        self.service_period_unit = service_period_unit
        self.split_commodity_code = split_commodity_code
        self.split_product_detail = split_product_detail
        self.split_account_id = split_account_id
        self.split_account_name = split_account_name
        self.split_billing_cycle = split_billing_cycle

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id
        if self.billing_type is not None:
            result['BillingType'] = self.billing_type
        if self.cost_unit is not None:
            result['CostUnit'] = self.cost_unit
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.product_detail is not None:
            result['ProductDetail'] = self.product_detail
        if self.owner_id is not None:
            result['OwnerID'] = self.owner_id
        if self.billing_item is not None:
            result['BillingItem'] = self.billing_item
        if self.list_price is not None:
            result['ListPrice'] = self.list_price
        if self.list_price_unit is not None:
            result['ListPriceUnit'] = self.list_price_unit
        if self.usage is not None:
            result['Usage'] = self.usage
        if self.usage_unit is not None:
            result['UsageUnit'] = self.usage_unit
        if self.deducted_by_resource_package is not None:
            result['DeductedByResourcePackage'] = self.deducted_by_resource_package
        if self.pretax_gross_amount is not None:
            result['PretaxGrossAmount'] = self.pretax_gross_amount
        if self.invoice_discount is not None:
            result['InvoiceDiscount'] = self.invoice_discount
        if self.deducted_by_coupons is not None:
            result['DeductedByCoupons'] = self.deducted_by_coupons
        if self.pretax_amount is not None:
            result['PretaxAmount'] = self.pretax_amount
        if self.deducted_by_cash_coupons is not None:
            result['DeductedByCashCoupons'] = self.deducted_by_cash_coupons
        if self.deducted_by_prepaid_card is not None:
            result['DeductedByPrepaidCard'] = self.deducted_by_prepaid_card
        if self.payment_amount is not None:
            result['PaymentAmount'] = self.payment_amount
        if self.outstanding_amount is not None:
            result['OutstandingAmount'] = self.outstanding_amount
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.instance_config is not None:
            result['InstanceConfig'] = self.instance_config
        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec
        if self.internet_ip is not None:
            result['InternetIP'] = self.internet_ip
        if self.intranet_ip is not None:
            result['IntranetIP'] = self.intranet_ip
        if self.region is not None:
            result['Region'] = self.region
        if self.zone is not None:
            result['Zone'] = self.zone
        if self.item is not None:
            result['Item'] = self.item
        if self.service_period is not None:
            result['ServicePeriod'] = self.service_period
        if self.billing_date is not None:
            result['BillingDate'] = self.billing_date
        if self.split_item_id is not None:
            result['SplitItemID'] = self.split_item_id
        if self.split_item_name is not None:
            result['SplitItemName'] = self.split_item_name
        if self.pip_code is not None:
            result['PipCode'] = self.pip_code
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.service_period_unit is not None:
            result['ServicePeriodUnit'] = self.service_period_unit
        if self.split_commodity_code is not None:
            result['SplitCommodityCode'] = self.split_commodity_code
        if self.split_product_detail is not None:
            result['SplitProductDetail'] = self.split_product_detail
        if self.split_account_id is not None:
            result['SplitAccountID'] = self.split_account_id
        if self.split_account_name is not None:
            result['SplitAccountName'] = self.split_account_name
        if self.split_billing_cycle is not None:
            result['SplitBillingCycle'] = self.split_billing_cycle
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')
        if m.get('BillingType') is not None:
            self.billing_type = m.get('BillingType')
        if m.get('CostUnit') is not None:
            self.cost_unit = m.get('CostUnit')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProductDetail') is not None:
            self.product_detail = m.get('ProductDetail')
        if m.get('OwnerID') is not None:
            self.owner_id = m.get('OwnerID')
        if m.get('BillingItem') is not None:
            self.billing_item = m.get('BillingItem')
        if m.get('ListPrice') is not None:
            self.list_price = m.get('ListPrice')
        if m.get('ListPriceUnit') is not None:
            self.list_price_unit = m.get('ListPriceUnit')
        if m.get('Usage') is not None:
            self.usage = m.get('Usage')
        if m.get('UsageUnit') is not None:
            self.usage_unit = m.get('UsageUnit')
        if m.get('DeductedByResourcePackage') is not None:
            self.deducted_by_resource_package = m.get('DeductedByResourcePackage')
        if m.get('PretaxGrossAmount') is not None:
            self.pretax_gross_amount = m.get('PretaxGrossAmount')
        if m.get('InvoiceDiscount') is not None:
            self.invoice_discount = m.get('InvoiceDiscount')
        if m.get('DeductedByCoupons') is not None:
            self.deducted_by_coupons = m.get('DeductedByCoupons')
        if m.get('PretaxAmount') is not None:
            self.pretax_amount = m.get('PretaxAmount')
        if m.get('DeductedByCashCoupons') is not None:
            self.deducted_by_cash_coupons = m.get('DeductedByCashCoupons')
        if m.get('DeductedByPrepaidCard') is not None:
            self.deducted_by_prepaid_card = m.get('DeductedByPrepaidCard')
        if m.get('PaymentAmount') is not None:
            self.payment_amount = m.get('PaymentAmount')
        if m.get('OutstandingAmount') is not None:
            self.outstanding_amount = m.get('OutstandingAmount')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        if m.get('ResourceGroup') is not None:
            self.resource_group = m.get('ResourceGroup')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('InstanceConfig') is not None:
            self.instance_config = m.get('InstanceConfig')
        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')
        if m.get('InternetIP') is not None:
            self.internet_ip = m.get('InternetIP')
        if m.get('IntranetIP') is not None:
            self.intranet_ip = m.get('IntranetIP')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Zone') is not None:
            self.zone = m.get('Zone')
        if m.get('Item') is not None:
            self.item = m.get('Item')
        if m.get('ServicePeriod') is not None:
            self.service_period = m.get('ServicePeriod')
        if m.get('BillingDate') is not None:
            self.billing_date = m.get('BillingDate')
        if m.get('SplitItemID') is not None:
            self.split_item_id = m.get('SplitItemID')
        if m.get('SplitItemName') is not None:
            self.split_item_name = m.get('SplitItemName')
        if m.get('PipCode') is not None:
            self.pip_code = m.get('PipCode')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('ServicePeriodUnit') is not None:
            self.service_period_unit = m.get('ServicePeriodUnit')
        if m.get('SplitCommodityCode') is not None:
            self.split_commodity_code = m.get('SplitCommodityCode')
        if m.get('SplitProductDetail') is not None:
            self.split_product_detail = m.get('SplitProductDetail')
        if m.get('SplitAccountID') is not None:
            self.split_account_id = m.get('SplitAccountID')
        if m.get('SplitAccountName') is not None:
            self.split_account_name = m.get('SplitAccountName')
        if m.get('SplitBillingCycle') is not None:
            self.split_billing_cycle = m.get('SplitBillingCycle')
        return self


class DescribeSplitItemBillResponseBodyData(TeaModel):
    def __init__(
        self,
        billing_cycle: str = None,
        account_id: str = None,
        account_name: str = None,
        total_count: int = None,
        next_token: str = None,
        max_results: int = None,
        items: List[DescribeSplitItemBillResponseBodyDataItems] = None,
    ):
        self.billing_cycle = billing_cycle
        self.account_id = account_id
        self.account_name = account_name
        self.total_count = total_count
        self.next_token = next_token
        self.max_results = max_results
        self.items = items

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle
        if self.account_id is not None:
            result['AccountID'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')
        if m.get('AccountID') is not None:
            self.account_id = m.get('AccountID')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeSplitItemBillResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        return self


class DescribeSplitItemBillResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        data: DescribeSplitItemBillResponseBodyData = None,
    ):
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = DescribeSplitItemBillResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DescribeSplitItemBillResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSplitItemBillResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeSplitItemBillResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableBillGenerationRequest(TeaModel):
    def __init__(
        self,
        product_code: str = None,
        owner_id: int = None,
    ):
        self.product_code = product_code
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class EnableBillGenerationResponseBodyData(TeaModel):
    def __init__(
        self,
        boolean: bool = None,
    ):
        self.boolean = boolean

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.boolean is not None:
            result['Boolean'] = self.boolean
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Boolean') is not None:
            self.boolean = m.get('Boolean')
        return self


class EnableBillGenerationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        data: EnableBillGenerationResponseBodyData = None,
    ):
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = EnableBillGenerationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class EnableBillGenerationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EnableBillGenerationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = EnableBillGenerationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCustomerAccountInfoRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
    ):
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class GetCustomerAccountInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        login_email: str = None,
        account_type: str = None,
        mpk: int = None,
        hosting_status: str = None,
        credit_limit_status: str = None,
        is_certified: bool = None,
    ):
        self.login_email = login_email
        self.account_type = account_type
        self.mpk = mpk
        self.hosting_status = hosting_status
        self.credit_limit_status = credit_limit_status
        self.is_certified = is_certified

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.login_email is not None:
            result['LoginEmail'] = self.login_email
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.mpk is not None:
            result['Mpk'] = self.mpk
        if self.hosting_status is not None:
            result['HostingStatus'] = self.hosting_status
        if self.credit_limit_status is not None:
            result['CreditLimitStatus'] = self.credit_limit_status
        if self.is_certified is not None:
            result['IsCertified'] = self.is_certified
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoginEmail') is not None:
            self.login_email = m.get('LoginEmail')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('Mpk') is not None:
            self.mpk = m.get('Mpk')
        if m.get('HostingStatus') is not None:
            self.hosting_status = m.get('HostingStatus')
        if m.get('CreditLimitStatus') is not None:
            self.credit_limit_status = m.get('CreditLimitStatus')
        if m.get('IsCertified') is not None:
            self.is_certified = m.get('IsCertified')
        return self


class GetCustomerAccountInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        data: GetCustomerAccountInfoResponseBodyData = None,
    ):
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = GetCustomerAccountInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetCustomerAccountInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetCustomerAccountInfoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetCustomerAccountInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCustomerListResponseBodyData(TeaModel):
    def __init__(
        self,
        uid_list: List[str] = None,
    ):
        self.uid_list = uid_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.uid_list is not None:
            result['UidList'] = self.uid_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UidList') is not None:
            self.uid_list = m.get('UidList')
        return self


class GetCustomerListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        data: GetCustomerListResponseBodyData = None,
    ):
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = GetCustomerListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetCustomerListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetCustomerListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetCustomerListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOrderDetailRequest(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        owner_id: int = None,
    ):
        self.order_id = order_id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class GetOrderDetailResponseBodyDataOrderListOrder(TeaModel):
    def __init__(
        self,
        operator: str = None,
        after_tax_amount: str = None,
        sub_order_id: str = None,
        config: str = None,
        tax: str = None,
        payment_time: str = None,
        payment_currency: str = None,
        usage_end_time: str = None,
        subscription_type: str = None,
        pretax_gross_amount: str = None,
        order_type: str = None,
        currency: str = None,
        usage_start_time: str = None,
        original_config: str = None,
        payment_status: str = None,
        product_code: str = None,
        create_time: str = None,
        product_type: str = None,
        related_order_id: str = None,
        quantity: str = None,
        order_id: str = None,
        pretax_amount: str = None,
        order_sub_type: str = None,
        region: str = None,
        instance_ids: str = None,
        pretax_amount_local: str = None,
        commodity_code: str = None,
    ):
        self.operator = operator
        self.after_tax_amount = after_tax_amount
        self.sub_order_id = sub_order_id
        self.config = config
        self.tax = tax
        self.payment_time = payment_time
        self.payment_currency = payment_currency
        self.usage_end_time = usage_end_time
        self.subscription_type = subscription_type
        self.pretax_gross_amount = pretax_gross_amount
        self.order_type = order_type
        self.currency = currency
        self.usage_start_time = usage_start_time
        self.original_config = original_config
        self.payment_status = payment_status
        self.product_code = product_code
        self.create_time = create_time
        self.product_type = product_type
        self.related_order_id = related_order_id
        self.quantity = quantity
        self.order_id = order_id
        self.pretax_amount = pretax_amount
        self.order_sub_type = order_sub_type
        self.region = region
        self.instance_ids = instance_ids
        self.pretax_amount_local = pretax_amount_local
        self.commodity_code = commodity_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.after_tax_amount is not None:
            result['AfterTaxAmount'] = self.after_tax_amount
        if self.sub_order_id is not None:
            result['SubOrderId'] = self.sub_order_id
        if self.config is not None:
            result['Config'] = self.config
        if self.tax is not None:
            result['Tax'] = self.tax
        if self.payment_time is not None:
            result['PaymentTime'] = self.payment_time
        if self.payment_currency is not None:
            result['PaymentCurrency'] = self.payment_currency
        if self.usage_end_time is not None:
            result['UsageEndTime'] = self.usage_end_time
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.pretax_gross_amount is not None:
            result['PretaxGrossAmount'] = self.pretax_gross_amount
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.usage_start_time is not None:
            result['UsageStartTime'] = self.usage_start_time
        if self.original_config is not None:
            result['OriginalConfig'] = self.original_config
        if self.payment_status is not None:
            result['PaymentStatus'] = self.payment_status
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.related_order_id is not None:
            result['RelatedOrderId'] = self.related_order_id
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.pretax_amount is not None:
            result['PretaxAmount'] = self.pretax_amount
        if self.order_sub_type is not None:
            result['OrderSubType'] = self.order_sub_type
        if self.region is not None:
            result['Region'] = self.region
        if self.instance_ids is not None:
            result['InstanceIDs'] = self.instance_ids
        if self.pretax_amount_local is not None:
            result['PretaxAmountLocal'] = self.pretax_amount_local
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('AfterTaxAmount') is not None:
            self.after_tax_amount = m.get('AfterTaxAmount')
        if m.get('SubOrderId') is not None:
            self.sub_order_id = m.get('SubOrderId')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('Tax') is not None:
            self.tax = m.get('Tax')
        if m.get('PaymentTime') is not None:
            self.payment_time = m.get('PaymentTime')
        if m.get('PaymentCurrency') is not None:
            self.payment_currency = m.get('PaymentCurrency')
        if m.get('UsageEndTime') is not None:
            self.usage_end_time = m.get('UsageEndTime')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('PretaxGrossAmount') is not None:
            self.pretax_gross_amount = m.get('PretaxGrossAmount')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('UsageStartTime') is not None:
            self.usage_start_time = m.get('UsageStartTime')
        if m.get('OriginalConfig') is not None:
            self.original_config = m.get('OriginalConfig')
        if m.get('PaymentStatus') is not None:
            self.payment_status = m.get('PaymentStatus')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('RelatedOrderId') is not None:
            self.related_order_id = m.get('RelatedOrderId')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PretaxAmount') is not None:
            self.pretax_amount = m.get('PretaxAmount')
        if m.get('OrderSubType') is not None:
            self.order_sub_type = m.get('OrderSubType')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('InstanceIDs') is not None:
            self.instance_ids = m.get('InstanceIDs')
        if m.get('PretaxAmountLocal') is not None:
            self.pretax_amount_local = m.get('PretaxAmountLocal')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        return self


class GetOrderDetailResponseBodyDataOrderList(TeaModel):
    def __init__(
        self,
        order: List[GetOrderDetailResponseBodyDataOrderListOrder] = None,
    ):
        self.order = order

    def validate(self):
        if self.order:
            for k in self.order:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Order'] = []
        if self.order is not None:
            for k in self.order:
                result['Order'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.order = []
        if m.get('Order') is not None:
            for k in m.get('Order'):
                temp_model = GetOrderDetailResponseBodyDataOrderListOrder()
                self.order.append(temp_model.from_map(k))
        return self


class GetOrderDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        page_num: int = None,
        host_name: str = None,
        order_list: GetOrderDetailResponseBodyDataOrderList = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.page_num = page_num
        self.host_name = host_name
        self.order_list = order_list

    def validate(self):
        if self.order_list:
            self.order_list.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.order_list is not None:
            result['OrderList'] = self.order_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('OrderList') is not None:
            temp_model = GetOrderDetailResponseBodyDataOrderList()
            self.order_list = temp_model.from_map(m['OrderList'])
        return self


class GetOrderDetailResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        code: str = None,
        success: bool = None,
        data: GetOrderDetailResponseBodyData = None,
    ):
        self.request_id = request_id
        self.message = message
        self.code = code
        self.success = success
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Data') is not None:
            temp_model = GetOrderDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetOrderDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetOrderDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetOrderDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPayAsYouGoPriceRequestModuleList(TeaModel):
    def __init__(
        self,
        module_code: str = None,
        config: str = None,
        price_type: str = None,
    ):
        self.module_code = module_code
        self.config = config
        self.price_type = price_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.module_code is not None:
            result['ModuleCode'] = self.module_code
        if self.config is not None:
            result['Config'] = self.config
        if self.price_type is not None:
            result['PriceType'] = self.price_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModuleCode') is not None:
            self.module_code = m.get('ModuleCode')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('PriceType') is not None:
            self.price_type = m.get('PriceType')
        return self


class GetPayAsYouGoPriceRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        product_code: str = None,
        product_type: str = None,
        subscription_type: str = None,
        region: str = None,
        module_list: List[GetPayAsYouGoPriceRequestModuleList] = None,
    ):
        self.owner_id = owner_id
        self.product_code = product_code
        self.product_type = product_type
        self.subscription_type = subscription_type
        self.region = region
        self.module_list = module_list

    def validate(self):
        if self.module_list:
            for k in self.module_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.region is not None:
            result['Region'] = self.region
        result['ModuleList'] = []
        if self.module_list is not None:
            for k in self.module_list:
                result['ModuleList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        self.module_list = []
        if m.get('ModuleList') is not None:
            for k in m.get('ModuleList'):
                temp_model = GetPayAsYouGoPriceRequestModuleList()
                self.module_list.append(temp_model.from_map(k))
        return self


class GetPayAsYouGoPriceResponseBodyDataModuleDetailsModuleDetail(TeaModel):
    def __init__(
        self,
        module_code: str = None,
        original_cost: float = None,
        invoice_discount: float = None,
        cost_after_discount: float = None,
        unit_price: float = None,
    ):
        self.module_code = module_code
        self.original_cost = original_cost
        self.invoice_discount = invoice_discount
        self.cost_after_discount = cost_after_discount
        self.unit_price = unit_price

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.module_code is not None:
            result['ModuleCode'] = self.module_code
        if self.original_cost is not None:
            result['OriginalCost'] = self.original_cost
        if self.invoice_discount is not None:
            result['InvoiceDiscount'] = self.invoice_discount
        if self.cost_after_discount is not None:
            result['CostAfterDiscount'] = self.cost_after_discount
        if self.unit_price is not None:
            result['UnitPrice'] = self.unit_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModuleCode') is not None:
            self.module_code = m.get('ModuleCode')
        if m.get('OriginalCost') is not None:
            self.original_cost = m.get('OriginalCost')
        if m.get('InvoiceDiscount') is not None:
            self.invoice_discount = m.get('InvoiceDiscount')
        if m.get('CostAfterDiscount') is not None:
            self.cost_after_discount = m.get('CostAfterDiscount')
        if m.get('UnitPrice') is not None:
            self.unit_price = m.get('UnitPrice')
        return self


class GetPayAsYouGoPriceResponseBodyDataModuleDetails(TeaModel):
    def __init__(
        self,
        module_detail: List[GetPayAsYouGoPriceResponseBodyDataModuleDetailsModuleDetail] = None,
    ):
        self.module_detail = module_detail

    def validate(self):
        if self.module_detail:
            for k in self.module_detail:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ModuleDetail'] = []
        if self.module_detail is not None:
            for k in self.module_detail:
                result['ModuleDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.module_detail = []
        if m.get('ModuleDetail') is not None:
            for k in m.get('ModuleDetail'):
                temp_model = GetPayAsYouGoPriceResponseBodyDataModuleDetailsModuleDetail()
                self.module_detail.append(temp_model.from_map(k))
        return self


class GetPayAsYouGoPriceResponseBodyDataPromotionDetailsPromotionDetail(TeaModel):
    def __init__(
        self,
        promotion_name: str = None,
        promotion_desc: str = None,
        promotion_id: int = None,
    ):
        self.promotion_name = promotion_name
        self.promotion_desc = promotion_desc
        self.promotion_id = promotion_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.promotion_name is not None:
            result['PromotionName'] = self.promotion_name
        if self.promotion_desc is not None:
            result['PromotionDesc'] = self.promotion_desc
        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PromotionName') is not None:
            self.promotion_name = m.get('PromotionName')
        if m.get('PromotionDesc') is not None:
            self.promotion_desc = m.get('PromotionDesc')
        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')
        return self


class GetPayAsYouGoPriceResponseBodyDataPromotionDetails(TeaModel):
    def __init__(
        self,
        promotion_detail: List[GetPayAsYouGoPriceResponseBodyDataPromotionDetailsPromotionDetail] = None,
    ):
        self.promotion_detail = promotion_detail

    def validate(self):
        if self.promotion_detail:
            for k in self.promotion_detail:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['PromotionDetail'] = []
        if self.promotion_detail is not None:
            for k in self.promotion_detail:
                result['PromotionDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.promotion_detail = []
        if m.get('PromotionDetail') is not None:
            for k in m.get('PromotionDetail'):
                temp_model = GetPayAsYouGoPriceResponseBodyDataPromotionDetailsPromotionDetail()
                self.promotion_detail.append(temp_model.from_map(k))
        return self


class GetPayAsYouGoPriceResponseBodyData(TeaModel):
    def __init__(
        self,
        currency: str = None,
        module_details: GetPayAsYouGoPriceResponseBodyDataModuleDetails = None,
        promotion_details: GetPayAsYouGoPriceResponseBodyDataPromotionDetails = None,
    ):
        self.currency = currency
        self.module_details = module_details
        self.promotion_details = promotion_details

    def validate(self):
        if self.module_details:
            self.module_details.validate()
        if self.promotion_details:
            self.promotion_details.validate()

    def to_map(self):
        result = dict()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.module_details is not None:
            result['ModuleDetails'] = self.module_details.to_map()
        if self.promotion_details is not None:
            result['PromotionDetails'] = self.promotion_details.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('ModuleDetails') is not None:
            temp_model = GetPayAsYouGoPriceResponseBodyDataModuleDetails()
            self.module_details = temp_model.from_map(m['ModuleDetails'])
        if m.get('PromotionDetails') is not None:
            temp_model = GetPayAsYouGoPriceResponseBodyDataPromotionDetails()
            self.promotion_details = temp_model.from_map(m['PromotionDetails'])
        return self


class GetPayAsYouGoPriceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        data: GetPayAsYouGoPriceResponseBodyData = None,
    ):
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = GetPayAsYouGoPriceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetPayAsYouGoPriceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPayAsYouGoPriceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetPayAsYouGoPriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourcePackagePriceRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        product_code: str = None,
        package_type: str = None,
        effective_date: str = None,
        specification: str = None,
        duration: int = None,
        pricing_cycle: str = None,
        order_type: str = None,
        instance_id: str = None,
    ):
        self.owner_id = owner_id
        self.product_code = product_code
        self.package_type = package_type
        self.effective_date = effective_date
        self.specification = specification
        self.duration = duration
        self.pricing_cycle = pricing_cycle
        self.order_type = order_type
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.effective_date is not None:
            result['EffectiveDate'] = self.effective_date
        if self.specification is not None:
            result['Specification'] = self.specification
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('EffectiveDate') is not None:
            self.effective_date = m.get('EffectiveDate')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetResourcePackagePriceResponseBodyDataPromotionsPromotion(TeaModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
    ):
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetResourcePackagePriceResponseBodyDataPromotions(TeaModel):
    def __init__(
        self,
        promotion: List[GetResourcePackagePriceResponseBodyDataPromotionsPromotion] = None,
    ):
        self.promotion = promotion

    def validate(self):
        if self.promotion:
            for k in self.promotion:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Promotion'] = []
        if self.promotion is not None:
            for k in self.promotion:
                result['Promotion'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.promotion = []
        if m.get('Promotion') is not None:
            for k in m.get('Promotion'):
                temp_model = GetResourcePackagePriceResponseBodyDataPromotionsPromotion()
                self.promotion.append(temp_model.from_map(k))
        return self


class GetResourcePackagePriceResponseBodyData(TeaModel):
    def __init__(
        self,
        currency: str = None,
        original_price: float = None,
        trade_price: float = None,
        discount_price: float = None,
        promotions: GetResourcePackagePriceResponseBodyDataPromotions = None,
    ):
        self.currency = currency
        self.original_price = original_price
        self.trade_price = trade_price
        self.discount_price = discount_price
        self.promotions = promotions

    def validate(self):
        if self.promotions:
            self.promotions.validate()

    def to_map(self):
        result = dict()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.promotions is not None:
            result['Promotions'] = self.promotions.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('Promotions') is not None:
            temp_model = GetResourcePackagePriceResponseBodyDataPromotions()
            self.promotions = temp_model.from_map(m['Promotions'])
        return self


class GetResourcePackagePriceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        data: GetResourcePackagePriceResponseBodyData = None,
    ):
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = GetResourcePackagePriceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetResourcePackagePriceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetResourcePackagePriceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetResourcePackagePriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSubscriptionPriceRequestModuleList(TeaModel):
    def __init__(
        self,
        module_code: str = None,
        config: str = None,
        module_status: int = None,
        tag: str = None,
    ):
        self.module_code = module_code
        self.config = config
        self.module_status = module_status
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.module_code is not None:
            result['ModuleCode'] = self.module_code
        if self.config is not None:
            result['Config'] = self.config
        if self.module_status is not None:
            result['ModuleStatus'] = self.module_status
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModuleCode') is not None:
            self.module_code = m.get('ModuleCode')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('ModuleStatus') is not None:
            self.module_status = m.get('ModuleStatus')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class GetSubscriptionPriceRequest(TeaModel):
    def __init__(
        self,
        service_period_unit: str = None,
        subscription_type: str = None,
        owner_id: int = None,
        product_code: str = None,
        order_type: str = None,
        service_period_quantity: int = None,
        product_type: str = None,
        region: str = None,
        instance_id: str = None,
        module_list: List[GetSubscriptionPriceRequestModuleList] = None,
        quantity: int = None,
    ):
        self.service_period_unit = service_period_unit
        self.subscription_type = subscription_type
        self.owner_id = owner_id
        self.product_code = product_code
        self.order_type = order_type
        self.service_period_quantity = service_period_quantity
        self.product_type = product_type
        self.region = region
        self.instance_id = instance_id
        self.module_list = module_list
        self.quantity = quantity

    def validate(self):
        if self.module_list:
            for k in self.module_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.service_period_unit is not None:
            result['ServicePeriodUnit'] = self.service_period_unit
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.service_period_quantity is not None:
            result['ServicePeriodQuantity'] = self.service_period_quantity
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.region is not None:
            result['Region'] = self.region
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        result['ModuleList'] = []
        if self.module_list is not None:
            for k in self.module_list:
                result['ModuleList'].append(k.to_map() if k else None)
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServicePeriodUnit') is not None:
            self.service_period_unit = m.get('ServicePeriodUnit')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('ServicePeriodQuantity') is not None:
            self.service_period_quantity = m.get('ServicePeriodQuantity')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        self.module_list = []
        if m.get('ModuleList') is not None:
            for k in m.get('ModuleList'):
                temp_model = GetSubscriptionPriceRequestModuleList()
                self.module_list.append(temp_model.from_map(k))
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        return self


class GetSubscriptionPriceResponseBodyDataModuleDetailsModuleDetail(TeaModel):
    def __init__(
        self,
        module_code: str = None,
        original_cost: float = None,
        invoice_discount: float = None,
        cost_after_discount: float = None,
        unit_price: float = None,
    ):
        self.module_code = module_code
        self.original_cost = original_cost
        self.invoice_discount = invoice_discount
        self.cost_after_discount = cost_after_discount
        self.unit_price = unit_price

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.module_code is not None:
            result['ModuleCode'] = self.module_code
        if self.original_cost is not None:
            result['OriginalCost'] = self.original_cost
        if self.invoice_discount is not None:
            result['InvoiceDiscount'] = self.invoice_discount
        if self.cost_after_discount is not None:
            result['CostAfterDiscount'] = self.cost_after_discount
        if self.unit_price is not None:
            result['UnitPrice'] = self.unit_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModuleCode') is not None:
            self.module_code = m.get('ModuleCode')
        if m.get('OriginalCost') is not None:
            self.original_cost = m.get('OriginalCost')
        if m.get('InvoiceDiscount') is not None:
            self.invoice_discount = m.get('InvoiceDiscount')
        if m.get('CostAfterDiscount') is not None:
            self.cost_after_discount = m.get('CostAfterDiscount')
        if m.get('UnitPrice') is not None:
            self.unit_price = m.get('UnitPrice')
        return self


class GetSubscriptionPriceResponseBodyDataModuleDetails(TeaModel):
    def __init__(
        self,
        module_detail: List[GetSubscriptionPriceResponseBodyDataModuleDetailsModuleDetail] = None,
    ):
        self.module_detail = module_detail

    def validate(self):
        if self.module_detail:
            for k in self.module_detail:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ModuleDetail'] = []
        if self.module_detail is not None:
            for k in self.module_detail:
                result['ModuleDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.module_detail = []
        if m.get('ModuleDetail') is not None:
            for k in m.get('ModuleDetail'):
                temp_model = GetSubscriptionPriceResponseBodyDataModuleDetailsModuleDetail()
                self.module_detail.append(temp_model.from_map(k))
        return self


class GetSubscriptionPriceResponseBodyDataPromotionDetailsPromotionDetail(TeaModel):
    def __init__(
        self,
        promotion_name: str = None,
        promotion_desc: str = None,
        promotion_id: int = None,
    ):
        self.promotion_name = promotion_name
        self.promotion_desc = promotion_desc
        self.promotion_id = promotion_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.promotion_name is not None:
            result['PromotionName'] = self.promotion_name
        if self.promotion_desc is not None:
            result['PromotionDesc'] = self.promotion_desc
        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PromotionName') is not None:
            self.promotion_name = m.get('PromotionName')
        if m.get('PromotionDesc') is not None:
            self.promotion_desc = m.get('PromotionDesc')
        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')
        return self


class GetSubscriptionPriceResponseBodyDataPromotionDetails(TeaModel):
    def __init__(
        self,
        promotion_detail: List[GetSubscriptionPriceResponseBodyDataPromotionDetailsPromotionDetail] = None,
    ):
        self.promotion_detail = promotion_detail

    def validate(self):
        if self.promotion_detail:
            for k in self.promotion_detail:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['PromotionDetail'] = []
        if self.promotion_detail is not None:
            for k in self.promotion_detail:
                result['PromotionDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.promotion_detail = []
        if m.get('PromotionDetail') is not None:
            for k in m.get('PromotionDetail'):
                temp_model = GetSubscriptionPriceResponseBodyDataPromotionDetailsPromotionDetail()
                self.promotion_detail.append(temp_model.from_map(k))
        return self


class GetSubscriptionPriceResponseBodyData(TeaModel):
    def __init__(
        self,
        original_price: float = None,
        discount_price: float = None,
        trade_price: float = None,
        currency: str = None,
        quantity: int = None,
        module_details: GetSubscriptionPriceResponseBodyDataModuleDetails = None,
        promotion_details: GetSubscriptionPriceResponseBodyDataPromotionDetails = None,
    ):
        self.original_price = original_price
        self.discount_price = discount_price
        self.trade_price = trade_price
        self.currency = currency
        self.quantity = quantity
        self.module_details = module_details
        self.promotion_details = promotion_details

    def validate(self):
        if self.module_details:
            self.module_details.validate()
        if self.promotion_details:
            self.promotion_details.validate()

    def to_map(self):
        result = dict()
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.module_details is not None:
            result['ModuleDetails'] = self.module_details.to_map()
        if self.promotion_details is not None:
            result['PromotionDetails'] = self.promotion_details.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('ModuleDetails') is not None:
            temp_model = GetSubscriptionPriceResponseBodyDataModuleDetails()
            self.module_details = temp_model.from_map(m['ModuleDetails'])
        if m.get('PromotionDetails') is not None:
            temp_model = GetSubscriptionPriceResponseBodyDataPromotionDetails()
            self.promotion_details = temp_model.from_map(m['PromotionDetails'])
        return self


class GetSubscriptionPriceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        data: GetSubscriptionPriceResponseBodyData = None,
    ):
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = GetSubscriptionPriceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetSubscriptionPriceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSubscriptionPriceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetSubscriptionPriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyCostUnitRequestUnitEntityList(TeaModel):
    def __init__(
        self,
        new_unit_name: str = None,
        owner_uid: int = None,
        unit_id: int = None,
    ):
        self.new_unit_name = new_unit_name
        self.owner_uid = owner_uid
        self.unit_id = unit_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.new_unit_name is not None:
            result['NewUnitName'] = self.new_unit_name
        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid
        if self.unit_id is not None:
            result['UnitId'] = self.unit_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewUnitName') is not None:
            self.new_unit_name = m.get('NewUnitName')
        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')
        if m.get('UnitId') is not None:
            self.unit_id = m.get('UnitId')
        return self


class ModifyCostUnitRequest(TeaModel):
    def __init__(
        self,
        unit_entity_list: List[ModifyCostUnitRequestUnitEntityList] = None,
    ):
        self.unit_entity_list = unit_entity_list

    def validate(self):
        if self.unit_entity_list:
            for k in self.unit_entity_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['UnitEntityList'] = []
        if self.unit_entity_list is not None:
            for k in self.unit_entity_list:
                result['UnitEntityList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.unit_entity_list = []
        if m.get('UnitEntityList') is not None:
            for k in m.get('UnitEntityList'):
                temp_model = ModifyCostUnitRequestUnitEntityList()
                self.unit_entity_list.append(temp_model.from_map(k))
        return self


class ModifyCostUnitResponseBodyData(TeaModel):
    def __init__(
        self,
        is_success: bool = None,
        unit_id: int = None,
        owner_uid: int = None,
    ):
        self.is_success = is_success
        self.unit_id = unit_id
        self.owner_uid = owner_uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.unit_id is not None:
            result['UnitId'] = self.unit_id
        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('UnitId') is not None:
            self.unit_id = m.get('UnitId')
        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')
        return self


class ModifyCostUnitResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        code: str = None,
        success: bool = None,
        data: List[ModifyCostUnitResponseBodyData] = None,
    ):
        self.request_id = request_id
        self.message = message
        self.code = code
        self.success = success
        self.data = data

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ModifyCostUnitResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class ModifyCostUnitResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyCostUnitResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ModifyCostUnitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceRequestParameter(TeaModel):
    def __init__(
        self,
        code: str = None,
        value: str = None,
    ):
        self.code = code
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ModifyInstanceRequest(TeaModel):
    def __init__(
        self,
        product_code: str = None,
        owner_id: int = None,
        product_type: str = None,
        subscription_type: str = None,
        modify_type: str = None,
        instance_id: str = None,
        parameter: List[ModifyInstanceRequestParameter] = None,
        client_token: str = None,
    ):
        self.product_code = product_code
        self.owner_id = owner_id
        self.product_type = product_type
        self.subscription_type = subscription_type
        self.modify_type = modify_type
        self.instance_id = instance_id
        self.parameter = parameter
        self.client_token = client_token

    def validate(self):
        if self.parameter:
            for k in self.parameter:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.modify_type is not None:
            result['ModifyType'] = self.modify_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        result['Parameter'] = []
        if self.parameter is not None:
            for k in self.parameter:
                result['Parameter'].append(k.to_map() if k else None)
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('ModifyType') is not None:
            self.modify_type = m.get('ModifyType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        self.parameter = []
        if m.get('Parameter') is not None:
            for k in m.get('Parameter'):
                temp_model = ModifyInstanceRequestParameter()
                self.parameter.append(temp_model.from_map(k))
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class ModifyInstanceResponseBodyData(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        order_id: str = None,
    ):
        self.host_id = host_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class ModifyInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        data: ModifyInstanceResponseBodyData = None,
    ):
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = ModifyInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class ModifyInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ModifyInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAccountBalanceResponseBodyData(TeaModel):
    def __init__(
        self,
        available_amount: str = None,
        available_cash_amount: str = None,
        credit_amount: str = None,
        mybank_credit_amount: str = None,
        currency: str = None,
    ):
        self.available_amount = available_amount
        self.available_cash_amount = available_cash_amount
        self.credit_amount = credit_amount
        self.mybank_credit_amount = mybank_credit_amount
        self.currency = currency

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.available_amount is not None:
            result['AvailableAmount'] = self.available_amount
        if self.available_cash_amount is not None:
            result['AvailableCashAmount'] = self.available_cash_amount
        if self.credit_amount is not None:
            result['CreditAmount'] = self.credit_amount
        if self.mybank_credit_amount is not None:
            result['MybankCreditAmount'] = self.mybank_credit_amount
        if self.currency is not None:
            result['Currency'] = self.currency
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableAmount') is not None:
            self.available_amount = m.get('AvailableAmount')
        if m.get('AvailableCashAmount') is not None:
            self.available_cash_amount = m.get('AvailableCashAmount')
        if m.get('CreditAmount') is not None:
            self.credit_amount = m.get('CreditAmount')
        if m.get('MybankCreditAmount') is not None:
            self.mybank_credit_amount = m.get('MybankCreditAmount')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        return self


class QueryAccountBalanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        data: QueryAccountBalanceResponseBodyData = None,
    ):
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = QueryAccountBalanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryAccountBalanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryAccountBalanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = QueryAccountBalanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAccountBillRequest(TeaModel):
    def __init__(
        self,
        billing_cycle: str = None,
        page_num: int = None,
        page_size: int = None,
        owner_id: int = None,
        is_group_by_product: bool = None,
        product_code: str = None,
        bill_owner_id: int = None,
        granularity: str = None,
        billing_date: str = None,
    ):
        self.billing_cycle = billing_cycle
        self.page_num = page_num
        self.page_size = page_size
        self.owner_id = owner_id
        self.is_group_by_product = is_group_by_product
        self.product_code = product_code
        self.bill_owner_id = bill_owner_id
        self.granularity = granularity
        self.billing_date = billing_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.owner_id is not None:
            result['OwnerID'] = self.owner_id
        if self.is_group_by_product is not None:
            result['IsGroupByProduct'] = self.is_group_by_product
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.bill_owner_id is not None:
            result['BillOwnerId'] = self.bill_owner_id
        if self.granularity is not None:
            result['Granularity'] = self.granularity
        if self.billing_date is not None:
            result['BillingDate'] = self.billing_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('OwnerID') is not None:
            self.owner_id = m.get('OwnerID')
        if m.get('IsGroupByProduct') is not None:
            self.is_group_by_product = m.get('IsGroupByProduct')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('BillOwnerId') is not None:
            self.bill_owner_id = m.get('BillOwnerId')
        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')
        if m.get('BillingDate') is not None:
            self.billing_date = m.get('BillingDate')
        return self


class QueryAccountBillResponseBodyDataItemsItem(TeaModel):
    def __init__(
        self,
        cost_unit: str = None,
        owner_id: str = None,
        pretax_gross_amount: float = None,
        invoice_discount: float = None,
        deducted_by_coupons: float = None,
        pretax_amount: float = None,
        deducted_by_cash_coupons: float = None,
        deducted_by_prepaid_card: float = None,
        payment_amount: float = None,
        outstanding_amount: float = None,
        currency: str = None,
        owner_name: str = None,
        product_code: str = None,
        product_name: str = None,
        subscription_type: str = None,
        pip_code: str = None,
        billing_date: str = None,
    ):
        self.cost_unit = cost_unit
        self.owner_id = owner_id
        self.pretax_gross_amount = pretax_gross_amount
        self.invoice_discount = invoice_discount
        self.deducted_by_coupons = deducted_by_coupons
        self.pretax_amount = pretax_amount
        self.deducted_by_cash_coupons = deducted_by_cash_coupons
        self.deducted_by_prepaid_card = deducted_by_prepaid_card
        self.payment_amount = payment_amount
        self.outstanding_amount = outstanding_amount
        self.currency = currency
        self.owner_name = owner_name
        self.product_code = product_code
        self.product_name = product_name
        self.subscription_type = subscription_type
        self.pip_code = pip_code
        self.billing_date = billing_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cost_unit is not None:
            result['CostUnit'] = self.cost_unit
        if self.owner_id is not None:
            result['OwnerID'] = self.owner_id
        if self.pretax_gross_amount is not None:
            result['PretaxGrossAmount'] = self.pretax_gross_amount
        if self.invoice_discount is not None:
            result['InvoiceDiscount'] = self.invoice_discount
        if self.deducted_by_coupons is not None:
            result['DeductedByCoupons'] = self.deducted_by_coupons
        if self.pretax_amount is not None:
            result['PretaxAmount'] = self.pretax_amount
        if self.deducted_by_cash_coupons is not None:
            result['DeductedByCashCoupons'] = self.deducted_by_cash_coupons
        if self.deducted_by_prepaid_card is not None:
            result['DeductedByPrepaidCard'] = self.deducted_by_prepaid_card
        if self.payment_amount is not None:
            result['PaymentAmount'] = self.payment_amount
        if self.outstanding_amount is not None:
            result['OutstandingAmount'] = self.outstanding_amount
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.pip_code is not None:
            result['PipCode'] = self.pip_code
        if self.billing_date is not None:
            result['BillingDate'] = self.billing_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostUnit') is not None:
            self.cost_unit = m.get('CostUnit')
        if m.get('OwnerID') is not None:
            self.owner_id = m.get('OwnerID')
        if m.get('PretaxGrossAmount') is not None:
            self.pretax_gross_amount = m.get('PretaxGrossAmount')
        if m.get('InvoiceDiscount') is not None:
            self.invoice_discount = m.get('InvoiceDiscount')
        if m.get('DeductedByCoupons') is not None:
            self.deducted_by_coupons = m.get('DeductedByCoupons')
        if m.get('PretaxAmount') is not None:
            self.pretax_amount = m.get('PretaxAmount')
        if m.get('DeductedByCashCoupons') is not None:
            self.deducted_by_cash_coupons = m.get('DeductedByCashCoupons')
        if m.get('DeductedByPrepaidCard') is not None:
            self.deducted_by_prepaid_card = m.get('DeductedByPrepaidCard')
        if m.get('PaymentAmount') is not None:
            self.payment_amount = m.get('PaymentAmount')
        if m.get('OutstandingAmount') is not None:
            self.outstanding_amount = m.get('OutstandingAmount')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('PipCode') is not None:
            self.pip_code = m.get('PipCode')
        if m.get('BillingDate') is not None:
            self.billing_date = m.get('BillingDate')
        return self


class QueryAccountBillResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        item: List[QueryAccountBillResponseBodyDataItemsItem] = None,
    ):
        self.item = item

    def validate(self):
        if self.item:
            for k in self.item:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Item'] = []
        if self.item is not None:
            for k in self.item:
                result['Item'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.item = []
        if m.get('Item') is not None:
            for k in m.get('Item'):
                temp_model = QueryAccountBillResponseBodyDataItemsItem()
                self.item.append(temp_model.from_map(k))
        return self


class QueryAccountBillResponseBodyData(TeaModel):
    def __init__(
        self,
        billing_cycle: str = None,
        account_id: str = None,
        account_name: str = None,
        total_count: int = None,
        page_num: int = None,
        page_size: int = None,
        items: QueryAccountBillResponseBodyDataItems = None,
    ):
        self.billing_cycle = billing_cycle
        self.account_id = account_id
        self.account_name = account_name
        self.total_count = total_count
        self.page_num = page_num
        self.page_size = page_size
        self.items = items

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle
        if self.account_id is not None:
            result['AccountID'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.items is not None:
            result['Items'] = self.items.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')
        if m.get('AccountID') is not None:
            self.account_id = m.get('AccountID')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Items') is not None:
            temp_model = QueryAccountBillResponseBodyDataItems()
            self.items = temp_model.from_map(m['Items'])
        return self


class QueryAccountBillResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        data: QueryAccountBillResponseBodyData = None,
    ):
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = QueryAccountBillResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryAccountBillResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryAccountBillResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = QueryAccountBillResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAccountTransactionDetailsRequest(TeaModel):
    def __init__(
        self,
        transaction_number: str = None,
        record_id: str = None,
        transaction_channel_sn: str = None,
        create_time_start: str = None,
        create_time_end: str = None,
        transaction_type: str = None,
        transaction_channel: str = None,
        next_token: str = None,
        max_results: int = None,
    ):
        self.transaction_number = transaction_number
        self.record_id = record_id
        self.transaction_channel_sn = transaction_channel_sn
        self.create_time_start = create_time_start
        self.create_time_end = create_time_end
        self.transaction_type = transaction_type
        self.transaction_channel = transaction_channel
        self.next_token = next_token
        self.max_results = max_results

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.transaction_number is not None:
            result['TransactionNumber'] = self.transaction_number
        if self.record_id is not None:
            result['RecordID'] = self.record_id
        if self.transaction_channel_sn is not None:
            result['TransactionChannelSN'] = self.transaction_channel_sn
        if self.create_time_start is not None:
            result['CreateTimeStart'] = self.create_time_start
        if self.create_time_end is not None:
            result['CreateTimeEnd'] = self.create_time_end
        if self.transaction_type is not None:
            result['TransactionType'] = self.transaction_type
        if self.transaction_channel is not None:
            result['TransactionChannel'] = self.transaction_channel
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TransactionNumber') is not None:
            self.transaction_number = m.get('TransactionNumber')
        if m.get('RecordID') is not None:
            self.record_id = m.get('RecordID')
        if m.get('TransactionChannelSN') is not None:
            self.transaction_channel_sn = m.get('TransactionChannelSN')
        if m.get('CreateTimeStart') is not None:
            self.create_time_start = m.get('CreateTimeStart')
        if m.get('CreateTimeEnd') is not None:
            self.create_time_end = m.get('CreateTimeEnd')
        if m.get('TransactionType') is not None:
            self.transaction_type = m.get('TransactionType')
        if m.get('TransactionChannel') is not None:
            self.transaction_channel = m.get('TransactionChannel')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class QueryAccountTransactionDetailsResponseBodyDataAccountTransactionsListAccountTransactionsList(TeaModel):
    def __init__(
        self,
        transaction_number: str = None,
        transaction_time: str = None,
        transaction_flow: str = None,
        transaction_type: str = None,
        transaction_channel: str = None,
        transaction_channel_sn: str = None,
        fund_type: str = None,
        record_id: str = None,
        remarks: str = None,
        billing_cycle: str = None,
        amount: str = None,
        balance: str = None,
        transaction_account: str = None,
    ):
        self.transaction_number = transaction_number
        self.transaction_time = transaction_time
        self.transaction_flow = transaction_flow
        self.transaction_type = transaction_type
        self.transaction_channel = transaction_channel
        self.transaction_channel_sn = transaction_channel_sn
        self.fund_type = fund_type
        self.record_id = record_id
        self.remarks = remarks
        self.billing_cycle = billing_cycle
        self.amount = amount
        self.balance = balance
        self.transaction_account = transaction_account

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.transaction_number is not None:
            result['TransactionNumber'] = self.transaction_number
        if self.transaction_time is not None:
            result['TransactionTime'] = self.transaction_time
        if self.transaction_flow is not None:
            result['TransactionFlow'] = self.transaction_flow
        if self.transaction_type is not None:
            result['TransactionType'] = self.transaction_type
        if self.transaction_channel is not None:
            result['TransactionChannel'] = self.transaction_channel
        if self.transaction_channel_sn is not None:
            result['TransactionChannelSN'] = self.transaction_channel_sn
        if self.fund_type is not None:
            result['FundType'] = self.fund_type
        if self.record_id is not None:
            result['RecordID'] = self.record_id
        if self.remarks is not None:
            result['Remarks'] = self.remarks
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.balance is not None:
            result['Balance'] = self.balance
        if self.transaction_account is not None:
            result['TransactionAccount'] = self.transaction_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TransactionNumber') is not None:
            self.transaction_number = m.get('TransactionNumber')
        if m.get('TransactionTime') is not None:
            self.transaction_time = m.get('TransactionTime')
        if m.get('TransactionFlow') is not None:
            self.transaction_flow = m.get('TransactionFlow')
        if m.get('TransactionType') is not None:
            self.transaction_type = m.get('TransactionType')
        if m.get('TransactionChannel') is not None:
            self.transaction_channel = m.get('TransactionChannel')
        if m.get('TransactionChannelSN') is not None:
            self.transaction_channel_sn = m.get('TransactionChannelSN')
        if m.get('FundType') is not None:
            self.fund_type = m.get('FundType')
        if m.get('RecordID') is not None:
            self.record_id = m.get('RecordID')
        if m.get('Remarks') is not None:
            self.remarks = m.get('Remarks')
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('Balance') is not None:
            self.balance = m.get('Balance')
        if m.get('TransactionAccount') is not None:
            self.transaction_account = m.get('TransactionAccount')
        return self


class QueryAccountTransactionDetailsResponseBodyDataAccountTransactionsList(TeaModel):
    def __init__(
        self,
        account_transactions_list: List[QueryAccountTransactionDetailsResponseBodyDataAccountTransactionsListAccountTransactionsList] = None,
    ):
        self.account_transactions_list = account_transactions_list

    def validate(self):
        if self.account_transactions_list:
            for k in self.account_transactions_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['AccountTransactionsList'] = []
        if self.account_transactions_list is not None:
            for k in self.account_transactions_list:
                result['AccountTransactionsList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.account_transactions_list = []
        if m.get('AccountTransactionsList') is not None:
            for k in m.get('AccountTransactionsList'):
                temp_model = QueryAccountTransactionDetailsResponseBodyDataAccountTransactionsListAccountTransactionsList()
                self.account_transactions_list.append(temp_model.from_map(k))
        return self


class QueryAccountTransactionDetailsResponseBodyData(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        total_count: int = None,
        next_token: str = None,
        max_results: int = None,
        account_transactions_list: QueryAccountTransactionDetailsResponseBodyDataAccountTransactionsList = None,
    ):
        self.account_name = account_name
        self.total_count = total_count
        self.next_token = next_token
        self.max_results = max_results
        self.account_transactions_list = account_transactions_list

    def validate(self):
        if self.account_transactions_list:
            self.account_transactions_list.validate()

    def to_map(self):
        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.account_transactions_list is not None:
            result['AccountTransactionsList'] = self.account_transactions_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('AccountTransactionsList') is not None:
            temp_model = QueryAccountTransactionDetailsResponseBodyDataAccountTransactionsList()
            self.account_transactions_list = temp_model.from_map(m['AccountTransactionsList'])
        return self


class QueryAccountTransactionDetailsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        data: QueryAccountTransactionDetailsResponseBodyData = None,
    ):
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = QueryAccountTransactionDetailsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryAccountTransactionDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryAccountTransactionDetailsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = QueryAccountTransactionDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAccountTransactionsRequest(TeaModel):
    def __init__(
        self,
        transaction_number: str = None,
        record_id: str = None,
        transaction_channel_sn: str = None,
        create_time_start: str = None,
        create_time_end: str = None,
        page_num: int = None,
        page_size: int = None,
    ):
        self.transaction_number = transaction_number
        self.record_id = record_id
        self.transaction_channel_sn = transaction_channel_sn
        self.create_time_start = create_time_start
        self.create_time_end = create_time_end
        self.page_num = page_num
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.transaction_number is not None:
            result['TransactionNumber'] = self.transaction_number
        if self.record_id is not None:
            result['RecordID'] = self.record_id
        if self.transaction_channel_sn is not None:
            result['TransactionChannelSN'] = self.transaction_channel_sn
        if self.create_time_start is not None:
            result['CreateTimeStart'] = self.create_time_start
        if self.create_time_end is not None:
            result['CreateTimeEnd'] = self.create_time_end
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TransactionNumber') is not None:
            self.transaction_number = m.get('TransactionNumber')
        if m.get('RecordID') is not None:
            self.record_id = m.get('RecordID')
        if m.get('TransactionChannelSN') is not None:
            self.transaction_channel_sn = m.get('TransactionChannelSN')
        if m.get('CreateTimeStart') is not None:
            self.create_time_start = m.get('CreateTimeStart')
        if m.get('CreateTimeEnd') is not None:
            self.create_time_end = m.get('CreateTimeEnd')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryAccountTransactionsResponseBodyDataAccountTransactionsListAccountTransactionsList(TeaModel):
    def __init__(
        self,
        transaction_number: str = None,
        transaction_time: str = None,
        transaction_flow: str = None,
        transaction_type: str = None,
        transaction_channel: str = None,
        transaction_channel_sn: str = None,
        fund_type: str = None,
        record_id: str = None,
        remarks: str = None,
        billing_cycle: str = None,
        amount: str = None,
        balance: str = None,
        transaction_account: str = None,
    ):
        self.transaction_number = transaction_number
        self.transaction_time = transaction_time
        self.transaction_flow = transaction_flow
        self.transaction_type = transaction_type
        self.transaction_channel = transaction_channel
        self.transaction_channel_sn = transaction_channel_sn
        self.fund_type = fund_type
        self.record_id = record_id
        self.remarks = remarks
        self.billing_cycle = billing_cycle
        self.amount = amount
        self.balance = balance
        self.transaction_account = transaction_account

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.transaction_number is not None:
            result['TransactionNumber'] = self.transaction_number
        if self.transaction_time is not None:
            result['TransactionTime'] = self.transaction_time
        if self.transaction_flow is not None:
            result['TransactionFlow'] = self.transaction_flow
        if self.transaction_type is not None:
            result['TransactionType'] = self.transaction_type
        if self.transaction_channel is not None:
            result['TransactionChannel'] = self.transaction_channel
        if self.transaction_channel_sn is not None:
            result['TransactionChannelSN'] = self.transaction_channel_sn
        if self.fund_type is not None:
            result['FundType'] = self.fund_type
        if self.record_id is not None:
            result['RecordID'] = self.record_id
        if self.remarks is not None:
            result['Remarks'] = self.remarks
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.balance is not None:
            result['Balance'] = self.balance
        if self.transaction_account is not None:
            result['TransactionAccount'] = self.transaction_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TransactionNumber') is not None:
            self.transaction_number = m.get('TransactionNumber')
        if m.get('TransactionTime') is not None:
            self.transaction_time = m.get('TransactionTime')
        if m.get('TransactionFlow') is not None:
            self.transaction_flow = m.get('TransactionFlow')
        if m.get('TransactionType') is not None:
            self.transaction_type = m.get('TransactionType')
        if m.get('TransactionChannel') is not None:
            self.transaction_channel = m.get('TransactionChannel')
        if m.get('TransactionChannelSN') is not None:
            self.transaction_channel_sn = m.get('TransactionChannelSN')
        if m.get('FundType') is not None:
            self.fund_type = m.get('FundType')
        if m.get('RecordID') is not None:
            self.record_id = m.get('RecordID')
        if m.get('Remarks') is not None:
            self.remarks = m.get('Remarks')
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('Balance') is not None:
            self.balance = m.get('Balance')
        if m.get('TransactionAccount') is not None:
            self.transaction_account = m.get('TransactionAccount')
        return self


class QueryAccountTransactionsResponseBodyDataAccountTransactionsList(TeaModel):
    def __init__(
        self,
        account_transactions_list: List[QueryAccountTransactionsResponseBodyDataAccountTransactionsListAccountTransactionsList] = None,
    ):
        self.account_transactions_list = account_transactions_list

    def validate(self):
        if self.account_transactions_list:
            for k in self.account_transactions_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['AccountTransactionsList'] = []
        if self.account_transactions_list is not None:
            for k in self.account_transactions_list:
                result['AccountTransactionsList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.account_transactions_list = []
        if m.get('AccountTransactionsList') is not None:
            for k in m.get('AccountTransactionsList'):
                temp_model = QueryAccountTransactionsResponseBodyDataAccountTransactionsListAccountTransactionsList()
                self.account_transactions_list.append(temp_model.from_map(k))
        return self


class QueryAccountTransactionsResponseBodyData(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        total_count: int = None,
        page_num: int = None,
        page_size: int = None,
        account_transactions_list: QueryAccountTransactionsResponseBodyDataAccountTransactionsList = None,
    ):
        self.account_name = account_name
        self.total_count = total_count
        self.page_num = page_num
        self.page_size = page_size
        self.account_transactions_list = account_transactions_list

    def validate(self):
        if self.account_transactions_list:
            self.account_transactions_list.validate()

    def to_map(self):
        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.account_transactions_list is not None:
            result['AccountTransactionsList'] = self.account_transactions_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('AccountTransactionsList') is not None:
            temp_model = QueryAccountTransactionsResponseBodyDataAccountTransactionsList()
            self.account_transactions_list = temp_model.from_map(m['AccountTransactionsList'])
        return self


class QueryAccountTransactionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        data: QueryAccountTransactionsResponseBodyData = None,
    ):
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = QueryAccountTransactionsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryAccountTransactionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryAccountTransactionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = QueryAccountTransactionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAvailableInstancesRequest(TeaModel):
    def __init__(
        self,
        region: str = None,
        owner_id: int = None,
        page_num: int = None,
        page_size: int = None,
        product_code: str = None,
        product_type: str = None,
        subscription_type: str = None,
        instance_ids: str = None,
        end_time_start: str = None,
        end_time_end: str = None,
        create_time_start: str = None,
        create_time_end: str = None,
        renew_status: str = None,
    ):
        self.region = region
        self.owner_id = owner_id
        self.page_num = page_num
        self.page_size = page_size
        self.product_code = product_code
        self.product_type = product_type
        self.subscription_type = subscription_type
        self.instance_ids = instance_ids
        self.end_time_start = end_time_start
        self.end_time_end = end_time_end
        self.create_time_start = create_time_start
        self.create_time_end = create_time_end
        self.renew_status = renew_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.instance_ids is not None:
            result['InstanceIDs'] = self.instance_ids
        if self.end_time_start is not None:
            result['EndTimeStart'] = self.end_time_start
        if self.end_time_end is not None:
            result['EndTimeEnd'] = self.end_time_end
        if self.create_time_start is not None:
            result['CreateTimeStart'] = self.create_time_start
        if self.create_time_end is not None:
            result['CreateTimeEnd'] = self.create_time_end
        if self.renew_status is not None:
            result['RenewStatus'] = self.renew_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('InstanceIDs') is not None:
            self.instance_ids = m.get('InstanceIDs')
        if m.get('EndTimeStart') is not None:
            self.end_time_start = m.get('EndTimeStart')
        if m.get('EndTimeEnd') is not None:
            self.end_time_end = m.get('EndTimeEnd')
        if m.get('CreateTimeStart') is not None:
            self.create_time_start = m.get('CreateTimeStart')
        if m.get('CreateTimeEnd') is not None:
            self.create_time_end = m.get('CreateTimeEnd')
        if m.get('RenewStatus') is not None:
            self.renew_status = m.get('RenewStatus')
        return self


class QueryAvailableInstancesResponseBodyDataInstanceList(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        seller_id: int = None,
        product_code: str = None,
        product_type: str = None,
        subscription_type: str = None,
        instance_id: str = None,
        region: str = None,
        create_time: str = None,
        end_time: str = None,
        stop_time: str = None,
        release_time: str = None,
        expected_release_time: str = None,
        status: str = None,
        sub_status: str = None,
        renew_status: str = None,
        renewal_duration: int = None,
        renewal_duration_unit: str = None,
        seller: str = None,
    ):
        self.owner_id = owner_id
        self.seller_id = seller_id
        self.product_code = product_code
        self.product_type = product_type
        self.subscription_type = subscription_type
        self.instance_id = instance_id
        self.region = region
        self.create_time = create_time
        self.end_time = end_time
        self.stop_time = stop_time
        self.release_time = release_time
        self.expected_release_time = expected_release_time
        self.status = status
        self.sub_status = sub_status
        self.renew_status = renew_status
        self.renewal_duration = renewal_duration
        self.renewal_duration_unit = renewal_duration_unit
        self.seller = seller

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.seller_id is not None:
            result['SellerId'] = self.seller_id
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id
        if self.region is not None:
            result['Region'] = self.region
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.stop_time is not None:
            result['StopTime'] = self.stop_time
        if self.release_time is not None:
            result['ReleaseTime'] = self.release_time
        if self.expected_release_time is not None:
            result['ExpectedReleaseTime'] = self.expected_release_time
        if self.status is not None:
            result['Status'] = self.status
        if self.sub_status is not None:
            result['SubStatus'] = self.sub_status
        if self.renew_status is not None:
            result['RenewStatus'] = self.renew_status
        if self.renewal_duration is not None:
            result['RenewalDuration'] = self.renewal_duration
        if self.renewal_duration_unit is not None:
            result['RenewalDurationUnit'] = self.renewal_duration_unit
        if self.seller is not None:
            result['Seller'] = self.seller
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SellerId') is not None:
            self.seller_id = m.get('SellerId')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StopTime') is not None:
            self.stop_time = m.get('StopTime')
        if m.get('ReleaseTime') is not None:
            self.release_time = m.get('ReleaseTime')
        if m.get('ExpectedReleaseTime') is not None:
            self.expected_release_time = m.get('ExpectedReleaseTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubStatus') is not None:
            self.sub_status = m.get('SubStatus')
        if m.get('RenewStatus') is not None:
            self.renew_status = m.get('RenewStatus')
        if m.get('RenewalDuration') is not None:
            self.renewal_duration = m.get('RenewalDuration')
        if m.get('RenewalDurationUnit') is not None:
            self.renewal_duration_unit = m.get('RenewalDurationUnit')
        if m.get('Seller') is not None:
            self.seller = m.get('Seller')
        return self


class QueryAvailableInstancesResponseBodyData(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        total_count: int = None,
        instance_list: List[QueryAvailableInstancesResponseBodyDataInstanceList] = None,
    ):
        self.page_num = page_num
        self.page_size = page_size
        self.total_count = total_count
        self.instance_list = instance_list

    def validate(self):
        if self.instance_list:
            for k in self.instance_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['InstanceList'] = []
        if self.instance_list is not None:
            for k in self.instance_list:
                result['InstanceList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.instance_list = []
        if m.get('InstanceList') is not None:
            for k in m.get('InstanceList'):
                temp_model = QueryAvailableInstancesResponseBodyDataInstanceList()
                self.instance_list.append(temp_model.from_map(k))
        return self


class QueryAvailableInstancesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        data: QueryAvailableInstancesResponseBodyData = None,
    ):
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = QueryAvailableInstancesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryAvailableInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryAvailableInstancesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = QueryAvailableInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryBillRequest(TeaModel):
    def __init__(
        self,
        billing_cycle: str = None,
        type: str = None,
        product_code: str = None,
        product_type: str = None,
        subscription_type: str = None,
        is_hide_zero_charge: bool = None,
        is_display_local_currency: bool = None,
        owner_id: int = None,
        page_num: int = None,
        page_size: int = None,
        bill_owner_id: int = None,
    ):
        self.billing_cycle = billing_cycle
        self.type = type
        self.product_code = product_code
        self.product_type = product_type
        self.subscription_type = subscription_type
        self.is_hide_zero_charge = is_hide_zero_charge
        self.is_display_local_currency = is_display_local_currency
        self.owner_id = owner_id
        self.page_num = page_num
        self.page_size = page_size
        self.bill_owner_id = bill_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle
        if self.type is not None:
            result['Type'] = self.type
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.is_hide_zero_charge is not None:
            result['IsHideZeroCharge'] = self.is_hide_zero_charge
        if self.is_display_local_currency is not None:
            result['IsDisplayLocalCurrency'] = self.is_display_local_currency
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.bill_owner_id is not None:
            result['BillOwnerId'] = self.bill_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('IsHideZeroCharge') is not None:
            self.is_hide_zero_charge = m.get('IsHideZeroCharge')
        if m.get('IsDisplayLocalCurrency') is not None:
            self.is_display_local_currency = m.get('IsDisplayLocalCurrency')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('BillOwnerId') is not None:
            self.bill_owner_id = m.get('BillOwnerId')
        return self


class QueryBillResponseBodyDataItemsItem(TeaModel):
    def __init__(
        self,
        record_id: str = None,
        item: str = None,
        owner_id: str = None,
        usage_start_time: str = None,
        usage_end_time: str = None,
        payment_time: str = None,
        product_code: str = None,
        product_type: str = None,
        subscription_type: str = None,
        product_name: str = None,
        product_detail: str = None,
        pretax_gross_amount: float = None,
        deducted_by_coupons: float = None,
        invoice_discount: float = None,
        pretax_amount: float = None,
        currency: str = None,
        pretax_amount_local: float = None,
        tax: float = None,
        payment_amount: float = None,
        deducted_by_cash_coupons: float = None,
        deducted_by_prepaid_card: float = None,
        outstanding_amount: float = None,
        after_tax_amount: float = None,
        status: str = None,
        payment_currency: str = None,
        payment_transaction_id: str = None,
        round_down_discount: str = None,
        sub_order_id: str = None,
        pip_code: str = None,
        commodity_code: str = None,
    ):
        self.record_id = record_id
        self.item = item
        self.owner_id = owner_id
        self.usage_start_time = usage_start_time
        self.usage_end_time = usage_end_time
        self.payment_time = payment_time
        self.product_code = product_code
        self.product_type = product_type
        self.subscription_type = subscription_type
        self.product_name = product_name
        self.product_detail = product_detail
        self.pretax_gross_amount = pretax_gross_amount
        self.deducted_by_coupons = deducted_by_coupons
        self.invoice_discount = invoice_discount
        self.pretax_amount = pretax_amount
        self.currency = currency
        self.pretax_amount_local = pretax_amount_local
        self.tax = tax
        self.payment_amount = payment_amount
        self.deducted_by_cash_coupons = deducted_by_cash_coupons
        self.deducted_by_prepaid_card = deducted_by_prepaid_card
        self.outstanding_amount = outstanding_amount
        self.after_tax_amount = after_tax_amount
        self.status = status
        self.payment_currency = payment_currency
        self.payment_transaction_id = payment_transaction_id
        self.round_down_discount = round_down_discount
        self.sub_order_id = sub_order_id
        self.pip_code = pip_code
        self.commodity_code = commodity_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.record_id is not None:
            result['RecordID'] = self.record_id
        if self.item is not None:
            result['Item'] = self.item
        if self.owner_id is not None:
            result['OwnerID'] = self.owner_id
        if self.usage_start_time is not None:
            result['UsageStartTime'] = self.usage_start_time
        if self.usage_end_time is not None:
            result['UsageEndTime'] = self.usage_end_time
        if self.payment_time is not None:
            result['PaymentTime'] = self.payment_time
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.product_detail is not None:
            result['ProductDetail'] = self.product_detail
        if self.pretax_gross_amount is not None:
            result['PretaxGrossAmount'] = self.pretax_gross_amount
        if self.deducted_by_coupons is not None:
            result['DeductedByCoupons'] = self.deducted_by_coupons
        if self.invoice_discount is not None:
            result['InvoiceDiscount'] = self.invoice_discount
        if self.pretax_amount is not None:
            result['PretaxAmount'] = self.pretax_amount
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.pretax_amount_local is not None:
            result['PretaxAmountLocal'] = self.pretax_amount_local
        if self.tax is not None:
            result['Tax'] = self.tax
        if self.payment_amount is not None:
            result['PaymentAmount'] = self.payment_amount
        if self.deducted_by_cash_coupons is not None:
            result['DeductedByCashCoupons'] = self.deducted_by_cash_coupons
        if self.deducted_by_prepaid_card is not None:
            result['DeductedByPrepaidCard'] = self.deducted_by_prepaid_card
        if self.outstanding_amount is not None:
            result['OutstandingAmount'] = self.outstanding_amount
        if self.after_tax_amount is not None:
            result['AfterTaxAmount'] = self.after_tax_amount
        if self.status is not None:
            result['Status'] = self.status
        if self.payment_currency is not None:
            result['PaymentCurrency'] = self.payment_currency
        if self.payment_transaction_id is not None:
            result['PaymentTransactionID'] = self.payment_transaction_id
        if self.round_down_discount is not None:
            result['RoundDownDiscount'] = self.round_down_discount
        if self.sub_order_id is not None:
            result['SubOrderId'] = self.sub_order_id
        if self.pip_code is not None:
            result['PipCode'] = self.pip_code
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordID') is not None:
            self.record_id = m.get('RecordID')
        if m.get('Item') is not None:
            self.item = m.get('Item')
        if m.get('OwnerID') is not None:
            self.owner_id = m.get('OwnerID')
        if m.get('UsageStartTime') is not None:
            self.usage_start_time = m.get('UsageStartTime')
        if m.get('UsageEndTime') is not None:
            self.usage_end_time = m.get('UsageEndTime')
        if m.get('PaymentTime') is not None:
            self.payment_time = m.get('PaymentTime')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProductDetail') is not None:
            self.product_detail = m.get('ProductDetail')
        if m.get('PretaxGrossAmount') is not None:
            self.pretax_gross_amount = m.get('PretaxGrossAmount')
        if m.get('DeductedByCoupons') is not None:
            self.deducted_by_coupons = m.get('DeductedByCoupons')
        if m.get('InvoiceDiscount') is not None:
            self.invoice_discount = m.get('InvoiceDiscount')
        if m.get('PretaxAmount') is not None:
            self.pretax_amount = m.get('PretaxAmount')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('PretaxAmountLocal') is not None:
            self.pretax_amount_local = m.get('PretaxAmountLocal')
        if m.get('Tax') is not None:
            self.tax = m.get('Tax')
        if m.get('PaymentAmount') is not None:
            self.payment_amount = m.get('PaymentAmount')
        if m.get('DeductedByCashCoupons') is not None:
            self.deducted_by_cash_coupons = m.get('DeductedByCashCoupons')
        if m.get('DeductedByPrepaidCard') is not None:
            self.deducted_by_prepaid_card = m.get('DeductedByPrepaidCard')
        if m.get('OutstandingAmount') is not None:
            self.outstanding_amount = m.get('OutstandingAmount')
        if m.get('AfterTaxAmount') is not None:
            self.after_tax_amount = m.get('AfterTaxAmount')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PaymentCurrency') is not None:
            self.payment_currency = m.get('PaymentCurrency')
        if m.get('PaymentTransactionID') is not None:
            self.payment_transaction_id = m.get('PaymentTransactionID')
        if m.get('RoundDownDiscount') is not None:
            self.round_down_discount = m.get('RoundDownDiscount')
        if m.get('SubOrderId') is not None:
            self.sub_order_id = m.get('SubOrderId')
        if m.get('PipCode') is not None:
            self.pip_code = m.get('PipCode')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        return self


class QueryBillResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        item: List[QueryBillResponseBodyDataItemsItem] = None,
    ):
        self.item = item

    def validate(self):
        if self.item:
            for k in self.item:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Item'] = []
        if self.item is not None:
            for k in self.item:
                result['Item'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.item = []
        if m.get('Item') is not None:
            for k in m.get('Item'):
                temp_model = QueryBillResponseBodyDataItemsItem()
                self.item.append(temp_model.from_map(k))
        return self


class QueryBillResponseBodyData(TeaModel):
    def __init__(
        self,
        billing_cycle: str = None,
        account_id: str = None,
        account_name: str = None,
        page_num: int = None,
        page_size: int = None,
        total_count: int = None,
        items: QueryBillResponseBodyDataItems = None,
    ):
        self.billing_cycle = billing_cycle
        self.account_id = account_id
        self.account_name = account_name
        self.page_num = page_num
        self.page_size = page_size
        self.total_count = total_count
        self.items = items

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle
        if self.account_id is not None:
            result['AccountID'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.items is not None:
            result['Items'] = self.items.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')
        if m.get('AccountID') is not None:
            self.account_id = m.get('AccountID')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Items') is not None:
            temp_model = QueryBillResponseBodyDataItems()
            self.items = temp_model.from_map(m['Items'])
        return self


class QueryBillResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        data: QueryBillResponseBodyData = None,
    ):
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = QueryBillResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryBillResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryBillResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = QueryBillResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryBillOverviewRequest(TeaModel):
    def __init__(
        self,
        billing_cycle: str = None,
        product_code: str = None,
        product_type: str = None,
        subscription_type: str = None,
        bill_owner_id: int = None,
    ):
        self.billing_cycle = billing_cycle
        self.product_code = product_code
        self.product_type = product_type
        self.subscription_type = subscription_type
        self.bill_owner_id = bill_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.bill_owner_id is not None:
            result['BillOwnerId'] = self.bill_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('BillOwnerId') is not None:
            self.bill_owner_id = m.get('BillOwnerId')
        return self


class QueryBillOverviewResponseBodyDataItemsItem(TeaModel):
    def __init__(
        self,
        item: str = None,
        product_code: str = None,
        product_type: str = None,
        subscription_type: str = None,
        product_name: str = None,
        product_detail: str = None,
        pretax_gross_amount: float = None,
        invoice_discount: float = None,
        deducted_by_coupons: float = None,
        pretax_amount: float = None,
        currency: str = None,
        payment_amount: float = None,
        outstanding_amount: float = None,
        deducted_by_cash_coupons: float = None,
        deducted_by_prepaid_card: float = None,
        pretax_amount_local: float = None,
        tax: float = None,
        after_tax_amount: float = None,
        payment_currency: str = None,
        round_down_discount: str = None,
        pip_code: str = None,
        commodity_code: str = None,
    ):
        self.item = item
        self.product_code = product_code
        self.product_type = product_type
        self.subscription_type = subscription_type
        self.product_name = product_name
        self.product_detail = product_detail
        self.pretax_gross_amount = pretax_gross_amount
        self.invoice_discount = invoice_discount
        self.deducted_by_coupons = deducted_by_coupons
        self.pretax_amount = pretax_amount
        self.currency = currency
        self.payment_amount = payment_amount
        self.outstanding_amount = outstanding_amount
        self.deducted_by_cash_coupons = deducted_by_cash_coupons
        self.deducted_by_prepaid_card = deducted_by_prepaid_card
        self.pretax_amount_local = pretax_amount_local
        self.tax = tax
        self.after_tax_amount = after_tax_amount
        self.payment_currency = payment_currency
        self.round_down_discount = round_down_discount
        self.pip_code = pip_code
        self.commodity_code = commodity_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.item is not None:
            result['Item'] = self.item
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.product_detail is not None:
            result['ProductDetail'] = self.product_detail
        if self.pretax_gross_amount is not None:
            result['PretaxGrossAmount'] = self.pretax_gross_amount
        if self.invoice_discount is not None:
            result['InvoiceDiscount'] = self.invoice_discount
        if self.deducted_by_coupons is not None:
            result['DeductedByCoupons'] = self.deducted_by_coupons
        if self.pretax_amount is not None:
            result['PretaxAmount'] = self.pretax_amount
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.payment_amount is not None:
            result['PaymentAmount'] = self.payment_amount
        if self.outstanding_amount is not None:
            result['OutstandingAmount'] = self.outstanding_amount
        if self.deducted_by_cash_coupons is not None:
            result['DeductedByCashCoupons'] = self.deducted_by_cash_coupons
        if self.deducted_by_prepaid_card is not None:
            result['DeductedByPrepaidCard'] = self.deducted_by_prepaid_card
        if self.pretax_amount_local is not None:
            result['PretaxAmountLocal'] = self.pretax_amount_local
        if self.tax is not None:
            result['Tax'] = self.tax
        if self.after_tax_amount is not None:
            result['AfterTaxAmount'] = self.after_tax_amount
        if self.payment_currency is not None:
            result['PaymentCurrency'] = self.payment_currency
        if self.round_down_discount is not None:
            result['RoundDownDiscount'] = self.round_down_discount
        if self.pip_code is not None:
            result['PipCode'] = self.pip_code
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Item') is not None:
            self.item = m.get('Item')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProductDetail') is not None:
            self.product_detail = m.get('ProductDetail')
        if m.get('PretaxGrossAmount') is not None:
            self.pretax_gross_amount = m.get('PretaxGrossAmount')
        if m.get('InvoiceDiscount') is not None:
            self.invoice_discount = m.get('InvoiceDiscount')
        if m.get('DeductedByCoupons') is not None:
            self.deducted_by_coupons = m.get('DeductedByCoupons')
        if m.get('PretaxAmount') is not None:
            self.pretax_amount = m.get('PretaxAmount')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('PaymentAmount') is not None:
            self.payment_amount = m.get('PaymentAmount')
        if m.get('OutstandingAmount') is not None:
            self.outstanding_amount = m.get('OutstandingAmount')
        if m.get('DeductedByCashCoupons') is not None:
            self.deducted_by_cash_coupons = m.get('DeductedByCashCoupons')
        if m.get('DeductedByPrepaidCard') is not None:
            self.deducted_by_prepaid_card = m.get('DeductedByPrepaidCard')
        if m.get('PretaxAmountLocal') is not None:
            self.pretax_amount_local = m.get('PretaxAmountLocal')
        if m.get('Tax') is not None:
            self.tax = m.get('Tax')
        if m.get('AfterTaxAmount') is not None:
            self.after_tax_amount = m.get('AfterTaxAmount')
        if m.get('PaymentCurrency') is not None:
            self.payment_currency = m.get('PaymentCurrency')
        if m.get('RoundDownDiscount') is not None:
            self.round_down_discount = m.get('RoundDownDiscount')
        if m.get('PipCode') is not None:
            self.pip_code = m.get('PipCode')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        return self


class QueryBillOverviewResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        item: List[QueryBillOverviewResponseBodyDataItemsItem] = None,
    ):
        self.item = item

    def validate(self):
        if self.item:
            for k in self.item:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Item'] = []
        if self.item is not None:
            for k in self.item:
                result['Item'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.item = []
        if m.get('Item') is not None:
            for k in m.get('Item'):
                temp_model = QueryBillOverviewResponseBodyDataItemsItem()
                self.item.append(temp_model.from_map(k))
        return self


class QueryBillOverviewResponseBodyData(TeaModel):
    def __init__(
        self,
        billing_cycle: str = None,
        account_id: str = None,
        account_name: str = None,
        items: QueryBillOverviewResponseBodyDataItems = None,
    ):
        self.billing_cycle = billing_cycle
        self.account_id = account_id
        self.account_name = account_name
        self.items = items

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle
        if self.account_id is not None:
            result['AccountID'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.items is not None:
            result['Items'] = self.items.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')
        if m.get('AccountID') is not None:
            self.account_id = m.get('AccountID')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('Items') is not None:
            temp_model = QueryBillOverviewResponseBodyDataItems()
            self.items = temp_model.from_map(m['Items'])
        return self


class QueryBillOverviewResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        data: QueryBillOverviewResponseBodyData = None,
    ):
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = QueryBillOverviewResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryBillOverviewResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryBillOverviewResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = QueryBillOverviewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryBillToOSSSubscriptionResponseBodyDataItemsItem(TeaModel):
    def __init__(
        self,
        subscribe_type: str = None,
        subscribe_bucket: str = None,
        bucket_owner_id: int = None,
        subscribe_time: str = None,
        subscribe_language: str = None,
    ):
        self.subscribe_type = subscribe_type
        self.subscribe_bucket = subscribe_bucket
        self.bucket_owner_id = bucket_owner_id
        self.subscribe_time = subscribe_time
        self.subscribe_language = subscribe_language

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.subscribe_type is not None:
            result['SubscribeType'] = self.subscribe_type
        if self.subscribe_bucket is not None:
            result['SubscribeBucket'] = self.subscribe_bucket
        if self.bucket_owner_id is not None:
            result['BucketOwnerId'] = self.bucket_owner_id
        if self.subscribe_time is not None:
            result['SubscribeTime'] = self.subscribe_time
        if self.subscribe_language is not None:
            result['SubscribeLanguage'] = self.subscribe_language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubscribeType') is not None:
            self.subscribe_type = m.get('SubscribeType')
        if m.get('SubscribeBucket') is not None:
            self.subscribe_bucket = m.get('SubscribeBucket')
        if m.get('BucketOwnerId') is not None:
            self.bucket_owner_id = m.get('BucketOwnerId')
        if m.get('SubscribeTime') is not None:
            self.subscribe_time = m.get('SubscribeTime')
        if m.get('SubscribeLanguage') is not None:
            self.subscribe_language = m.get('SubscribeLanguage')
        return self


class QueryBillToOSSSubscriptionResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        item: List[QueryBillToOSSSubscriptionResponseBodyDataItemsItem] = None,
    ):
        self.item = item

    def validate(self):
        if self.item:
            for k in self.item:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Item'] = []
        if self.item is not None:
            for k in self.item:
                result['Item'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.item = []
        if m.get('Item') is not None:
            for k in m.get('Item'):
                temp_model = QueryBillToOSSSubscriptionResponseBodyDataItemsItem()
                self.item.append(temp_model.from_map(k))
        return self


class QueryBillToOSSSubscriptionResponseBodyData(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        account_name: str = None,
        items: QueryBillToOSSSubscriptionResponseBodyDataItems = None,
    ):
        self.account_id = account_id
        self.account_name = account_name
        self.items = items

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        if self.account_id is not None:
            result['AccountID'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.items is not None:
            result['Items'] = self.items.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountID') is not None:
            self.account_id = m.get('AccountID')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('Items') is not None:
            temp_model = QueryBillToOSSSubscriptionResponseBodyDataItems()
            self.items = temp_model.from_map(m['Items'])
        return self


class QueryBillToOSSSubscriptionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        data: QueryBillToOSSSubscriptionResponseBodyData = None,
    ):
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = QueryBillToOSSSubscriptionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryBillToOSSSubscriptionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryBillToOSSSubscriptionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = QueryBillToOSSSubscriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCashCouponsRequest(TeaModel):
    def __init__(
        self,
        expiry_time_end: str = None,
        expiry_time_start: str = None,
        effective_or_not: bool = None,
    ):
        self.expiry_time_end = expiry_time_end
        self.expiry_time_start = expiry_time_start
        self.effective_or_not = effective_or_not

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.expiry_time_end is not None:
            result['ExpiryTimeEnd'] = self.expiry_time_end
        if self.expiry_time_start is not None:
            result['ExpiryTimeStart'] = self.expiry_time_start
        if self.effective_or_not is not None:
            result['EffectiveOrNot'] = self.effective_or_not
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpiryTimeEnd') is not None:
            self.expiry_time_end = m.get('ExpiryTimeEnd')
        if m.get('ExpiryTimeStart') is not None:
            self.expiry_time_start = m.get('ExpiryTimeStart')
        if m.get('EffectiveOrNot') is not None:
            self.effective_or_not = m.get('EffectiveOrNot')
        return self


class QueryCashCouponsResponseBodyDataCashCoupon(TeaModel):
    def __init__(
        self,
        cash_coupon_id: int = None,
        cash_coupon_no: str = None,
        granted_time: str = None,
        effective_time: str = None,
        expiry_time: str = None,
        applicable_products: str = None,
        applicable_scenarios: str = None,
        nominal_value: str = None,
        balance: str = None,
        status: str = None,
    ):
        self.cash_coupon_id = cash_coupon_id
        self.cash_coupon_no = cash_coupon_no
        self.granted_time = granted_time
        self.effective_time = effective_time
        self.expiry_time = expiry_time
        self.applicable_products = applicable_products
        self.applicable_scenarios = applicable_scenarios
        self.nominal_value = nominal_value
        self.balance = balance
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cash_coupon_id is not None:
            result['CashCouponId'] = self.cash_coupon_id
        if self.cash_coupon_no is not None:
            result['CashCouponNo'] = self.cash_coupon_no
        if self.granted_time is not None:
            result['GrantedTime'] = self.granted_time
        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time
        if self.expiry_time is not None:
            result['ExpiryTime'] = self.expiry_time
        if self.applicable_products is not None:
            result['ApplicableProducts'] = self.applicable_products
        if self.applicable_scenarios is not None:
            result['ApplicableScenarios'] = self.applicable_scenarios
        if self.nominal_value is not None:
            result['NominalValue'] = self.nominal_value
        if self.balance is not None:
            result['Balance'] = self.balance
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CashCouponId') is not None:
            self.cash_coupon_id = m.get('CashCouponId')
        if m.get('CashCouponNo') is not None:
            self.cash_coupon_no = m.get('CashCouponNo')
        if m.get('GrantedTime') is not None:
            self.granted_time = m.get('GrantedTime')
        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')
        if m.get('ExpiryTime') is not None:
            self.expiry_time = m.get('ExpiryTime')
        if m.get('ApplicableProducts') is not None:
            self.applicable_products = m.get('ApplicableProducts')
        if m.get('ApplicableScenarios') is not None:
            self.applicable_scenarios = m.get('ApplicableScenarios')
        if m.get('NominalValue') is not None:
            self.nominal_value = m.get('NominalValue')
        if m.get('Balance') is not None:
            self.balance = m.get('Balance')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryCashCouponsResponseBodyData(TeaModel):
    def __init__(
        self,
        cash_coupon: List[QueryCashCouponsResponseBodyDataCashCoupon] = None,
    ):
        self.cash_coupon = cash_coupon

    def validate(self):
        if self.cash_coupon:
            for k in self.cash_coupon:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['CashCoupon'] = []
        if self.cash_coupon is not None:
            for k in self.cash_coupon:
                result['CashCoupon'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cash_coupon = []
        if m.get('CashCoupon') is not None:
            for k in m.get('CashCoupon'):
                temp_model = QueryCashCouponsResponseBodyDataCashCoupon()
                self.cash_coupon.append(temp_model.from_map(k))
        return self


class QueryCashCouponsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        data: QueryCashCouponsResponseBodyData = None,
    ):
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = QueryCashCouponsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryCashCouponsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryCashCouponsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = QueryCashCouponsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCostUnitRequest(TeaModel):
    def __init__(
        self,
        owner_uid: int = None,
        parent_unit_id: int = None,
        page_num: int = None,
        page_size: int = None,
    ):
        self.owner_uid = owner_uid
        self.parent_unit_id = parent_unit_id
        self.page_num = page_num
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid
        if self.parent_unit_id is not None:
            result['ParentUnitId'] = self.parent_unit_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')
        if m.get('ParentUnitId') is not None:
            self.parent_unit_id = m.get('ParentUnitId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryCostUnitResponseBodyDataCostUnitDtoList(TeaModel):
    def __init__(
        self,
        unit_id: int = None,
        parent_unit_id: int = None,
        owner_uid: int = None,
        unit_name: str = None,
    ):
        self.unit_id = unit_id
        self.parent_unit_id = parent_unit_id
        self.owner_uid = owner_uid
        self.unit_name = unit_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.unit_id is not None:
            result['UnitId'] = self.unit_id
        if self.parent_unit_id is not None:
            result['ParentUnitId'] = self.parent_unit_id
        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid
        if self.unit_name is not None:
            result['UnitName'] = self.unit_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UnitId') is not None:
            self.unit_id = m.get('UnitId')
        if m.get('ParentUnitId') is not None:
            self.parent_unit_id = m.get('ParentUnitId')
        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')
        if m.get('UnitName') is not None:
            self.unit_name = m.get('UnitName')
        return self


class QueryCostUnitResponseBodyData(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        page_num: int = None,
        cost_unit_dto_list: List[QueryCostUnitResponseBodyDataCostUnitDtoList] = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.page_num = page_num
        self.cost_unit_dto_list = cost_unit_dto_list

    def validate(self):
        if self.cost_unit_dto_list:
            for k in self.cost_unit_dto_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        result['CostUnitDtoList'] = []
        if self.cost_unit_dto_list is not None:
            for k in self.cost_unit_dto_list:
                result['CostUnitDtoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        self.cost_unit_dto_list = []
        if m.get('CostUnitDtoList') is not None:
            for k in m.get('CostUnitDtoList'):
                temp_model = QueryCostUnitResponseBodyDataCostUnitDtoList()
                self.cost_unit_dto_list.append(temp_model.from_map(k))
        return self


class QueryCostUnitResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        code: str = None,
        success: bool = None,
        data: QueryCostUnitResponseBodyData = None,
    ):
        self.request_id = request_id
        self.message = message
        self.code = code
        self.success = success
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Data') is not None:
            temp_model = QueryCostUnitResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryCostUnitResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryCostUnitResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = QueryCostUnitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCostUnitResourceRequest(TeaModel):
    def __init__(
        self,
        owner_uid: int = None,
        unit_id: int = None,
        page_num: int = None,
        page_size: int = None,
    ):
        self.owner_uid = owner_uid
        self.unit_id = unit_id
        self.page_num = page_num
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid
        if self.unit_id is not None:
            result['UnitId'] = self.unit_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')
        if m.get('UnitId') is not None:
            self.unit_id = m.get('UnitId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryCostUnitResourceResponseBodyDataResourceInstanceDtoList(TeaModel):
    def __init__(
        self,
        resource_user_id: int = None,
        resource_tag: str = None,
        related_resources: str = None,
        apportion_name: str = None,
        resource_id: str = None,
        commodity_code: str = None,
        resource_status: str = None,
        resource_type: str = None,
        resource_user_name: str = None,
        resource_nick: str = None,
        resource_group: str = None,
        commodity_name: str = None,
        apportion_code: str = None,
    ):
        self.resource_user_id = resource_user_id
        self.resource_tag = resource_tag
        self.related_resources = related_resources
        self.apportion_name = apportion_name
        self.resource_id = resource_id
        self.commodity_code = commodity_code
        self.resource_status = resource_status
        self.resource_type = resource_type
        self.resource_user_name = resource_user_name
        self.resource_nick = resource_nick
        self.resource_group = resource_group
        self.commodity_name = commodity_name
        self.apportion_code = apportion_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_user_id is not None:
            result['ResourceUserId'] = self.resource_user_id
        if self.resource_tag is not None:
            result['ResourceTag'] = self.resource_tag
        if self.related_resources is not None:
            result['RelatedResources'] = self.related_resources
        if self.apportion_name is not None:
            result['ApportionName'] = self.apportion_name
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.resource_status is not None:
            result['ResourceStatus'] = self.resource_status
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_user_name is not None:
            result['ResourceUserName'] = self.resource_user_name
        if self.resource_nick is not None:
            result['ResourceNick'] = self.resource_nick
        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group
        if self.commodity_name is not None:
            result['CommodityName'] = self.commodity_name
        if self.apportion_code is not None:
            result['ApportionCode'] = self.apportion_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceUserId') is not None:
            self.resource_user_id = m.get('ResourceUserId')
        if m.get('ResourceTag') is not None:
            self.resource_tag = m.get('ResourceTag')
        if m.get('RelatedResources') is not None:
            self.related_resources = m.get('RelatedResources')
        if m.get('ApportionName') is not None:
            self.apportion_name = m.get('ApportionName')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('ResourceStatus') is not None:
            self.resource_status = m.get('ResourceStatus')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceUserName') is not None:
            self.resource_user_name = m.get('ResourceUserName')
        if m.get('ResourceNick') is not None:
            self.resource_nick = m.get('ResourceNick')
        if m.get('ResourceGroup') is not None:
            self.resource_group = m.get('ResourceGroup')
        if m.get('CommodityName') is not None:
            self.commodity_name = m.get('CommodityName')
        if m.get('ApportionCode') is not None:
            self.apportion_code = m.get('ApportionCode')
        return self


class QueryCostUnitResourceResponseBodyDataCostUnit(TeaModel):
    def __init__(
        self,
        unit_id: int = None,
        parent_unit_id: int = None,
        owner_uid: int = None,
        unit_name: str = None,
    ):
        self.unit_id = unit_id
        self.parent_unit_id = parent_unit_id
        self.owner_uid = owner_uid
        self.unit_name = unit_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.unit_id is not None:
            result['UnitId'] = self.unit_id
        if self.parent_unit_id is not None:
            result['ParentUnitId'] = self.parent_unit_id
        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid
        if self.unit_name is not None:
            result['UnitName'] = self.unit_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UnitId') is not None:
            self.unit_id = m.get('UnitId')
        if m.get('ParentUnitId') is not None:
            self.parent_unit_id = m.get('ParentUnitId')
        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')
        if m.get('UnitName') is not None:
            self.unit_name = m.get('UnitName')
        return self


class QueryCostUnitResourceResponseBodyDataCostUnitStatisInfo(TeaModel):
    def __init__(
        self,
        sub_unit_count: int = None,
        total_resource_group_count: int = None,
        total_resource_count: int = None,
        user_count: int = None,
        resource_count: int = None,
        total_user_count: int = None,
        resource_group_count: int = None,
    ):
        self.sub_unit_count = sub_unit_count
        self.total_resource_group_count = total_resource_group_count
        self.total_resource_count = total_resource_count
        self.user_count = user_count
        self.resource_count = resource_count
        self.total_user_count = total_user_count
        self.resource_group_count = resource_group_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.sub_unit_count is not None:
            result['SubUnitCount'] = self.sub_unit_count
        if self.total_resource_group_count is not None:
            result['TotalResourceGroupCount'] = self.total_resource_group_count
        if self.total_resource_count is not None:
            result['TotalResourceCount'] = self.total_resource_count
        if self.user_count is not None:
            result['UserCount'] = self.user_count
        if self.resource_count is not None:
            result['ResourceCount'] = self.resource_count
        if self.total_user_count is not None:
            result['TotalUserCount'] = self.total_user_count
        if self.resource_group_count is not None:
            result['ResourceGroupCount'] = self.resource_group_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubUnitCount') is not None:
            self.sub_unit_count = m.get('SubUnitCount')
        if m.get('TotalResourceGroupCount') is not None:
            self.total_resource_group_count = m.get('TotalResourceGroupCount')
        if m.get('TotalResourceCount') is not None:
            self.total_resource_count = m.get('TotalResourceCount')
        if m.get('UserCount') is not None:
            self.user_count = m.get('UserCount')
        if m.get('ResourceCount') is not None:
            self.resource_count = m.get('ResourceCount')
        if m.get('TotalUserCount') is not None:
            self.total_user_count = m.get('TotalUserCount')
        if m.get('ResourceGroupCount') is not None:
            self.resource_group_count = m.get('ResourceGroupCount')
        return self


class QueryCostUnitResourceResponseBodyData(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        page_num: int = None,
        resource_instance_dto_list: List[QueryCostUnitResourceResponseBodyDataResourceInstanceDtoList] = None,
        cost_unit: QueryCostUnitResourceResponseBodyDataCostUnit = None,
        cost_unit_statis_info: QueryCostUnitResourceResponseBodyDataCostUnitStatisInfo = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.page_num = page_num
        self.resource_instance_dto_list = resource_instance_dto_list
        self.cost_unit = cost_unit
        self.cost_unit_statis_info = cost_unit_statis_info

    def validate(self):
        if self.resource_instance_dto_list:
            for k in self.resource_instance_dto_list:
                if k:
                    k.validate()
        if self.cost_unit:
            self.cost_unit.validate()
        if self.cost_unit_statis_info:
            self.cost_unit_statis_info.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        result['ResourceInstanceDtoList'] = []
        if self.resource_instance_dto_list is not None:
            for k in self.resource_instance_dto_list:
                result['ResourceInstanceDtoList'].append(k.to_map() if k else None)
        if self.cost_unit is not None:
            result['CostUnit'] = self.cost_unit.to_map()
        if self.cost_unit_statis_info is not None:
            result['CostUnitStatisInfo'] = self.cost_unit_statis_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        self.resource_instance_dto_list = []
        if m.get('ResourceInstanceDtoList') is not None:
            for k in m.get('ResourceInstanceDtoList'):
                temp_model = QueryCostUnitResourceResponseBodyDataResourceInstanceDtoList()
                self.resource_instance_dto_list.append(temp_model.from_map(k))
        if m.get('CostUnit') is not None:
            temp_model = QueryCostUnitResourceResponseBodyDataCostUnit()
            self.cost_unit = temp_model.from_map(m['CostUnit'])
        if m.get('CostUnitStatisInfo') is not None:
            temp_model = QueryCostUnitResourceResponseBodyDataCostUnitStatisInfo()
            self.cost_unit_statis_info = temp_model.from_map(m['CostUnitStatisInfo'])
        return self


class QueryCostUnitResourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        code: str = None,
        success: bool = None,
        data: QueryCostUnitResourceResponseBodyData = None,
    ):
        self.request_id = request_id
        self.message = message
        self.code = code
        self.success = success
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Data') is not None:
            temp_model = QueryCostUnitResourceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryCostUnitResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryCostUnitResourceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = QueryCostUnitResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCustomerAddressListRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
    ):
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class QueryCustomerAddressListResponseBodyDataCustomerInvoiceAddressListCustomerInvoiceAddress(TeaModel):
    def __init__(
        self,
        id: int = None,
        user_id: int = None,
        user_nick: str = None,
        addressee: str = None,
        province: str = None,
        city: str = None,
        county: str = None,
        street: str = None,
        postal_code: str = None,
        phone: str = None,
        biz_type: str = None,
        delivery_address: str = None,
    ):
        self.id = id
        self.user_id = user_id
        self.user_nick = user_nick
        self.addressee = addressee
        self.province = province
        self.city = city
        self.county = county
        self.street = street
        self.postal_code = postal_code
        self.phone = phone
        self.biz_type = biz_type
        self.delivery_address = delivery_address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_nick is not None:
            result['UserNick'] = self.user_nick
        if self.addressee is not None:
            result['Addressee'] = self.addressee
        if self.province is not None:
            result['Province'] = self.province
        if self.city is not None:
            result['City'] = self.city
        if self.county is not None:
            result['County'] = self.county
        if self.street is not None:
            result['Street'] = self.street
        if self.postal_code is not None:
            result['PostalCode'] = self.postal_code
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.delivery_address is not None:
            result['DeliveryAddress'] = self.delivery_address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserNick') is not None:
            self.user_nick = m.get('UserNick')
        if m.get('Addressee') is not None:
            self.addressee = m.get('Addressee')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('County') is not None:
            self.county = m.get('County')
        if m.get('Street') is not None:
            self.street = m.get('Street')
        if m.get('PostalCode') is not None:
            self.postal_code = m.get('PostalCode')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('DeliveryAddress') is not None:
            self.delivery_address = m.get('DeliveryAddress')
        return self


class QueryCustomerAddressListResponseBodyDataCustomerInvoiceAddressList(TeaModel):
    def __init__(
        self,
        customer_invoice_address: List[QueryCustomerAddressListResponseBodyDataCustomerInvoiceAddressListCustomerInvoiceAddress] = None,
    ):
        self.customer_invoice_address = customer_invoice_address

    def validate(self):
        if self.customer_invoice_address:
            for k in self.customer_invoice_address:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['CustomerInvoiceAddress'] = []
        if self.customer_invoice_address is not None:
            for k in self.customer_invoice_address:
                result['CustomerInvoiceAddress'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.customer_invoice_address = []
        if m.get('CustomerInvoiceAddress') is not None:
            for k in m.get('CustomerInvoiceAddress'):
                temp_model = QueryCustomerAddressListResponseBodyDataCustomerInvoiceAddressListCustomerInvoiceAddress()
                self.customer_invoice_address.append(temp_model.from_map(k))
        return self


class QueryCustomerAddressListResponseBodyData(TeaModel):
    def __init__(
        self,
        customer_invoice_address_list: QueryCustomerAddressListResponseBodyDataCustomerInvoiceAddressList = None,
    ):
        self.customer_invoice_address_list = customer_invoice_address_list

    def validate(self):
        if self.customer_invoice_address_list:
            self.customer_invoice_address_list.validate()

    def to_map(self):
        result = dict()
        if self.customer_invoice_address_list is not None:
            result['CustomerInvoiceAddressList'] = self.customer_invoice_address_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomerInvoiceAddressList') is not None:
            temp_model = QueryCustomerAddressListResponseBodyDataCustomerInvoiceAddressList()
            self.customer_invoice_address_list = temp_model.from_map(m['CustomerInvoiceAddressList'])
        return self


class QueryCustomerAddressListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        data: QueryCustomerAddressListResponseBodyData = None,
    ):
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = QueryCustomerAddressListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryCustomerAddressListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryCustomerAddressListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = QueryCustomerAddressListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryEvaluateListRequest(TeaModel):
    def __init__(
        self,
        type: int = None,
        out_biz_id: str = None,
        owner_id: int = None,
        page_num: int = None,
        page_size: int = None,
        start_amount: int = None,
        end_amount: int = None,
        start_biz_time: str = None,
        end_biz_time: str = None,
        sort_type: int = None,
        start_search_time: str = None,
        end_search_time: str = None,
        bill_cycle: str = None,
        biz_type_list: List[str] = None,
    ):
        self.type = type
        self.out_biz_id = out_biz_id
        self.owner_id = owner_id
        self.page_num = page_num
        self.page_size = page_size
        self.start_amount = start_amount
        self.end_amount = end_amount
        self.start_biz_time = start_biz_time
        self.end_biz_time = end_biz_time
        self.sort_type = sort_type
        self.start_search_time = start_search_time
        self.end_search_time = end_search_time
        self.bill_cycle = bill_cycle
        self.biz_type_list = biz_type_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.out_biz_id is not None:
            result['OutBizId'] = self.out_biz_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_amount is not None:
            result['StartAmount'] = self.start_amount
        if self.end_amount is not None:
            result['EndAmount'] = self.end_amount
        if self.start_biz_time is not None:
            result['StartBizTime'] = self.start_biz_time
        if self.end_biz_time is not None:
            result['EndBizTime'] = self.end_biz_time
        if self.sort_type is not None:
            result['SortType'] = self.sort_type
        if self.start_search_time is not None:
            result['StartSearchTime'] = self.start_search_time
        if self.end_search_time is not None:
            result['EndSearchTime'] = self.end_search_time
        if self.bill_cycle is not None:
            result['BillCycle'] = self.bill_cycle
        if self.biz_type_list is not None:
            result['BizTypeList'] = self.biz_type_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('OutBizId') is not None:
            self.out_biz_id = m.get('OutBizId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartAmount') is not None:
            self.start_amount = m.get('StartAmount')
        if m.get('EndAmount') is not None:
            self.end_amount = m.get('EndAmount')
        if m.get('StartBizTime') is not None:
            self.start_biz_time = m.get('StartBizTime')
        if m.get('EndBizTime') is not None:
            self.end_biz_time = m.get('EndBizTime')
        if m.get('SortType') is not None:
            self.sort_type = m.get('SortType')
        if m.get('StartSearchTime') is not None:
            self.start_search_time = m.get('StartSearchTime')
        if m.get('EndSearchTime') is not None:
            self.end_search_time = m.get('EndSearchTime')
        if m.get('BillCycle') is not None:
            self.bill_cycle = m.get('BillCycle')
        if m.get('BizTypeList') is not None:
            self.biz_type_list = m.get('BizTypeList')
        return self


class QueryEvaluateListResponseBodyDataEvaluateListEvaluate(TeaModel):
    def __init__(
        self,
        id: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        user_id: int = None,
        user_nick: str = None,
        out_biz_id: str = None,
        bill_id: int = None,
        item_id: int = None,
        bill_cycle: str = None,
        biz_type: str = None,
        original_amount: int = None,
        present_amount: int = None,
        can_invoice_amount: int = None,
        invoiced_amount: int = None,
        offset_cost_amount: int = None,
        offset_accept_amount: int = None,
        status: int = None,
        op_id: str = None,
        name: str = None,
        biz_time: str = None,
        type: int = None,
    ):
        self.id = id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.user_id = user_id
        self.user_nick = user_nick
        self.out_biz_id = out_biz_id
        self.bill_id = bill_id
        self.item_id = item_id
        self.bill_cycle = bill_cycle
        self.biz_type = biz_type
        self.original_amount = original_amount
        self.present_amount = present_amount
        self.can_invoice_amount = can_invoice_amount
        self.invoiced_amount = invoiced_amount
        self.offset_cost_amount = offset_cost_amount
        self.offset_accept_amount = offset_accept_amount
        self.status = status
        self.op_id = op_id
        self.name = name
        self.biz_time = biz_time
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_nick is not None:
            result['UserNick'] = self.user_nick
        if self.out_biz_id is not None:
            result['OutBizId'] = self.out_biz_id
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.bill_cycle is not None:
            result['BillCycle'] = self.bill_cycle
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.original_amount is not None:
            result['OriginalAmount'] = self.original_amount
        if self.present_amount is not None:
            result['PresentAmount'] = self.present_amount
        if self.can_invoice_amount is not None:
            result['CanInvoiceAmount'] = self.can_invoice_amount
        if self.invoiced_amount is not None:
            result['InvoicedAmount'] = self.invoiced_amount
        if self.offset_cost_amount is not None:
            result['OffsetCostAmount'] = self.offset_cost_amount
        if self.offset_accept_amount is not None:
            result['OffsetAcceptAmount'] = self.offset_accept_amount
        if self.status is not None:
            result['Status'] = self.status
        if self.op_id is not None:
            result['OpId'] = self.op_id
        if self.name is not None:
            result['Name'] = self.name
        if self.biz_time is not None:
            result['BizTime'] = self.biz_time
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserNick') is not None:
            self.user_nick = m.get('UserNick')
        if m.get('OutBizId') is not None:
            self.out_biz_id = m.get('OutBizId')
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('BillCycle') is not None:
            self.bill_cycle = m.get('BillCycle')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('OriginalAmount') is not None:
            self.original_amount = m.get('OriginalAmount')
        if m.get('PresentAmount') is not None:
            self.present_amount = m.get('PresentAmount')
        if m.get('CanInvoiceAmount') is not None:
            self.can_invoice_amount = m.get('CanInvoiceAmount')
        if m.get('InvoicedAmount') is not None:
            self.invoiced_amount = m.get('InvoicedAmount')
        if m.get('OffsetCostAmount') is not None:
            self.offset_cost_amount = m.get('OffsetCostAmount')
        if m.get('OffsetAcceptAmount') is not None:
            self.offset_accept_amount = m.get('OffsetAcceptAmount')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('OpId') is not None:
            self.op_id = m.get('OpId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('BizTime') is not None:
            self.biz_time = m.get('BizTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryEvaluateListResponseBodyDataEvaluateList(TeaModel):
    def __init__(
        self,
        evaluate: List[QueryEvaluateListResponseBodyDataEvaluateListEvaluate] = None,
    ):
        self.evaluate = evaluate

    def validate(self):
        if self.evaluate:
            for k in self.evaluate:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Evaluate'] = []
        if self.evaluate is not None:
            for k in self.evaluate:
                result['Evaluate'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.evaluate = []
        if m.get('Evaluate') is not None:
            for k in m.get('Evaluate'):
                temp_model = QueryEvaluateListResponseBodyDataEvaluateListEvaluate()
                self.evaluate.append(temp_model.from_map(k))
        return self


class QueryEvaluateListResponseBodyData(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        page_num: int = None,
        page_size: int = None,
        total_count: int = None,
        total_invoice_amount: int = None,
        total_un_applied_invoice_amount: int = None,
        evaluate_list: QueryEvaluateListResponseBodyDataEvaluateList = None,
    ):
        self.host_id = host_id
        self.page_num = page_num
        self.page_size = page_size
        self.total_count = total_count
        self.total_invoice_amount = total_invoice_amount
        self.total_un_applied_invoice_amount = total_un_applied_invoice_amount
        self.evaluate_list = evaluate_list

    def validate(self):
        if self.evaluate_list:
            self.evaluate_list.validate()

    def to_map(self):
        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_invoice_amount is not None:
            result['TotalInvoiceAmount'] = self.total_invoice_amount
        if self.total_un_applied_invoice_amount is not None:
            result['TotalUnAppliedInvoiceAmount'] = self.total_un_applied_invoice_amount
        if self.evaluate_list is not None:
            result['EvaluateList'] = self.evaluate_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalInvoiceAmount') is not None:
            self.total_invoice_amount = m.get('TotalInvoiceAmount')
        if m.get('TotalUnAppliedInvoiceAmount') is not None:
            self.total_un_applied_invoice_amount = m.get('TotalUnAppliedInvoiceAmount')
        if m.get('EvaluateList') is not None:
            temp_model = QueryEvaluateListResponseBodyDataEvaluateList()
            self.evaluate_list = temp_model.from_map(m['EvaluateList'])
        return self


class QueryEvaluateListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        data: QueryEvaluateListResponseBodyData = None,
    ):
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = QueryEvaluateListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryEvaluateListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryEvaluateListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = QueryEvaluateListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryFinancialAccountInfoRequest(TeaModel):
    def __init__(
        self,
        user_id: int = None,
    ):
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryFinancialAccountInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        user_name: str = None,
        is_financial_account: bool = None,
        account_type: str = None,
        member_nick_name: str = None,
        member_group_id: int = None,
        member_group_name: str = None,
    ):
        self.user_name = user_name
        self.is_financial_account = is_financial_account
        self.account_type = account_type
        self.member_nick_name = member_nick_name
        self.member_group_id = member_group_id
        self.member_group_name = member_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.is_financial_account is not None:
            result['IsFinancialAccount'] = self.is_financial_account
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.member_nick_name is not None:
            result['MemberNickName'] = self.member_nick_name
        if self.member_group_id is not None:
            result['MemberGroupId'] = self.member_group_id
        if self.member_group_name is not None:
            result['MemberGroupName'] = self.member_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('IsFinancialAccount') is not None:
            self.is_financial_account = m.get('IsFinancialAccount')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('MemberNickName') is not None:
            self.member_nick_name = m.get('MemberNickName')
        if m.get('MemberGroupId') is not None:
            self.member_group_id = m.get('MemberGroupId')
        if m.get('MemberGroupName') is not None:
            self.member_group_name = m.get('MemberGroupName')
        return self


class QueryFinancialAccountInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        request_id: str = None,
        success: bool = None,
        message: str = None,
        data: QueryFinancialAccountInfoResponseBodyData = None,
    ):
        self.code = code
        self.request_id = request_id
        self.success = success
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = QueryFinancialAccountInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryFinancialAccountInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryFinancialAccountInfoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = QueryFinancialAccountInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryInstanceBillRequest(TeaModel):
    def __init__(
        self,
        billing_cycle: str = None,
        product_code: str = None,
        product_type: str = None,
        subscription_type: str = None,
        owner_id: int = None,
        is_billing_item: bool = None,
        page_num: int = None,
        page_size: int = None,
        is_hide_zero_charge: bool = None,
        billing_date: str = None,
        granularity: str = None,
        bill_owner_id: int = None,
    ):
        self.billing_cycle = billing_cycle
        self.product_code = product_code
        self.product_type = product_type
        self.subscription_type = subscription_type
        self.owner_id = owner_id
        self.is_billing_item = is_billing_item
        self.page_num = page_num
        self.page_size = page_size
        self.is_hide_zero_charge = is_hide_zero_charge
        self.billing_date = billing_date
        self.granularity = granularity
        self.bill_owner_id = bill_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.is_billing_item is not None:
            result['IsBillingItem'] = self.is_billing_item
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.is_hide_zero_charge is not None:
            result['IsHideZeroCharge'] = self.is_hide_zero_charge
        if self.billing_date is not None:
            result['BillingDate'] = self.billing_date
        if self.granularity is not None:
            result['Granularity'] = self.granularity
        if self.bill_owner_id is not None:
            result['BillOwnerId'] = self.bill_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('IsBillingItem') is not None:
            self.is_billing_item = m.get('IsBillingItem')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('IsHideZeroCharge') is not None:
            self.is_hide_zero_charge = m.get('IsHideZeroCharge')
        if m.get('BillingDate') is not None:
            self.billing_date = m.get('BillingDate')
        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')
        if m.get('BillOwnerId') is not None:
            self.bill_owner_id = m.get('BillOwnerId')
        return self


class QueryInstanceBillResponseBodyDataItemsItem(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        billing_type: str = None,
        cost_unit: str = None,
        product_code: str = None,
        product_type: str = None,
        subscription_type: str = None,
        product_name: str = None,
        product_detail: str = None,
        owner_id: str = None,
        billing_item: str = None,
        list_price: str = None,
        list_price_unit: str = None,
        usage: str = None,
        usage_unit: str = None,
        deducted_by_resource_package: str = None,
        pretax_gross_amount: float = None,
        invoice_discount: float = None,
        deducted_by_coupons: float = None,
        pretax_amount: float = None,
        deducted_by_cash_coupons: float = None,
        deducted_by_prepaid_card: float = None,
        payment_amount: float = None,
        outstanding_amount: float = None,
        currency: str = None,
        nick_name: str = None,
        resource_group: str = None,
        tag: str = None,
        instance_config: str = None,
        instance_spec: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        region: str = None,
        zone: str = None,
        item: str = None,
        service_period: str = None,
        billing_date: str = None,
        service_period_unit: str = None,
        pip_code: str = None,
        commodity_code: str = None,
    ):
        self.instance_id = instance_id
        self.billing_type = billing_type
        self.cost_unit = cost_unit
        self.product_code = product_code
        self.product_type = product_type
        self.subscription_type = subscription_type
        self.product_name = product_name
        self.product_detail = product_detail
        self.owner_id = owner_id
        self.billing_item = billing_item
        self.list_price = list_price
        self.list_price_unit = list_price_unit
        self.usage = usage
        self.usage_unit = usage_unit
        self.deducted_by_resource_package = deducted_by_resource_package
        self.pretax_gross_amount = pretax_gross_amount
        self.invoice_discount = invoice_discount
        self.deducted_by_coupons = deducted_by_coupons
        self.pretax_amount = pretax_amount
        self.deducted_by_cash_coupons = deducted_by_cash_coupons
        self.deducted_by_prepaid_card = deducted_by_prepaid_card
        self.payment_amount = payment_amount
        self.outstanding_amount = outstanding_amount
        self.currency = currency
        self.nick_name = nick_name
        self.resource_group = resource_group
        self.tag = tag
        self.instance_config = instance_config
        self.instance_spec = instance_spec
        self.internet_ip = internet_ip
        self.intranet_ip = intranet_ip
        self.region = region
        self.zone = zone
        self.item = item
        self.service_period = service_period
        self.billing_date = billing_date
        self.service_period_unit = service_period_unit
        self.pip_code = pip_code
        self.commodity_code = commodity_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id
        if self.billing_type is not None:
            result['BillingType'] = self.billing_type
        if self.cost_unit is not None:
            result['CostUnit'] = self.cost_unit
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.product_detail is not None:
            result['ProductDetail'] = self.product_detail
        if self.owner_id is not None:
            result['OwnerID'] = self.owner_id
        if self.billing_item is not None:
            result['BillingItem'] = self.billing_item
        if self.list_price is not None:
            result['ListPrice'] = self.list_price
        if self.list_price_unit is not None:
            result['ListPriceUnit'] = self.list_price_unit
        if self.usage is not None:
            result['Usage'] = self.usage
        if self.usage_unit is not None:
            result['UsageUnit'] = self.usage_unit
        if self.deducted_by_resource_package is not None:
            result['DeductedByResourcePackage'] = self.deducted_by_resource_package
        if self.pretax_gross_amount is not None:
            result['PretaxGrossAmount'] = self.pretax_gross_amount
        if self.invoice_discount is not None:
            result['InvoiceDiscount'] = self.invoice_discount
        if self.deducted_by_coupons is not None:
            result['DeductedByCoupons'] = self.deducted_by_coupons
        if self.pretax_amount is not None:
            result['PretaxAmount'] = self.pretax_amount
        if self.deducted_by_cash_coupons is not None:
            result['DeductedByCashCoupons'] = self.deducted_by_cash_coupons
        if self.deducted_by_prepaid_card is not None:
            result['DeductedByPrepaidCard'] = self.deducted_by_prepaid_card
        if self.payment_amount is not None:
            result['PaymentAmount'] = self.payment_amount
        if self.outstanding_amount is not None:
            result['OutstandingAmount'] = self.outstanding_amount
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.instance_config is not None:
            result['InstanceConfig'] = self.instance_config
        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec
        if self.internet_ip is not None:
            result['InternetIP'] = self.internet_ip
        if self.intranet_ip is not None:
            result['IntranetIP'] = self.intranet_ip
        if self.region is not None:
            result['Region'] = self.region
        if self.zone is not None:
            result['Zone'] = self.zone
        if self.item is not None:
            result['Item'] = self.item
        if self.service_period is not None:
            result['ServicePeriod'] = self.service_period
        if self.billing_date is not None:
            result['BillingDate'] = self.billing_date
        if self.service_period_unit is not None:
            result['ServicePeriodUnit'] = self.service_period_unit
        if self.pip_code is not None:
            result['PipCode'] = self.pip_code
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')
        if m.get('BillingType') is not None:
            self.billing_type = m.get('BillingType')
        if m.get('CostUnit') is not None:
            self.cost_unit = m.get('CostUnit')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProductDetail') is not None:
            self.product_detail = m.get('ProductDetail')
        if m.get('OwnerID') is not None:
            self.owner_id = m.get('OwnerID')
        if m.get('BillingItem') is not None:
            self.billing_item = m.get('BillingItem')
        if m.get('ListPrice') is not None:
            self.list_price = m.get('ListPrice')
        if m.get('ListPriceUnit') is not None:
            self.list_price_unit = m.get('ListPriceUnit')
        if m.get('Usage') is not None:
            self.usage = m.get('Usage')
        if m.get('UsageUnit') is not None:
            self.usage_unit = m.get('UsageUnit')
        if m.get('DeductedByResourcePackage') is not None:
            self.deducted_by_resource_package = m.get('DeductedByResourcePackage')
        if m.get('PretaxGrossAmount') is not None:
            self.pretax_gross_amount = m.get('PretaxGrossAmount')
        if m.get('InvoiceDiscount') is not None:
            self.invoice_discount = m.get('InvoiceDiscount')
        if m.get('DeductedByCoupons') is not None:
            self.deducted_by_coupons = m.get('DeductedByCoupons')
        if m.get('PretaxAmount') is not None:
            self.pretax_amount = m.get('PretaxAmount')
        if m.get('DeductedByCashCoupons') is not None:
            self.deducted_by_cash_coupons = m.get('DeductedByCashCoupons')
        if m.get('DeductedByPrepaidCard') is not None:
            self.deducted_by_prepaid_card = m.get('DeductedByPrepaidCard')
        if m.get('PaymentAmount') is not None:
            self.payment_amount = m.get('PaymentAmount')
        if m.get('OutstandingAmount') is not None:
            self.outstanding_amount = m.get('OutstandingAmount')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        if m.get('ResourceGroup') is not None:
            self.resource_group = m.get('ResourceGroup')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('InstanceConfig') is not None:
            self.instance_config = m.get('InstanceConfig')
        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')
        if m.get('InternetIP') is not None:
            self.internet_ip = m.get('InternetIP')
        if m.get('IntranetIP') is not None:
            self.intranet_ip = m.get('IntranetIP')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Zone') is not None:
            self.zone = m.get('Zone')
        if m.get('Item') is not None:
            self.item = m.get('Item')
        if m.get('ServicePeriod') is not None:
            self.service_period = m.get('ServicePeriod')
        if m.get('BillingDate') is not None:
            self.billing_date = m.get('BillingDate')
        if m.get('ServicePeriodUnit') is not None:
            self.service_period_unit = m.get('ServicePeriodUnit')
        if m.get('PipCode') is not None:
            self.pip_code = m.get('PipCode')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        return self


class QueryInstanceBillResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        item: List[QueryInstanceBillResponseBodyDataItemsItem] = None,
    ):
        self.item = item

    def validate(self):
        if self.item:
            for k in self.item:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Item'] = []
        if self.item is not None:
            for k in self.item:
                result['Item'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.item = []
        if m.get('Item') is not None:
            for k in m.get('Item'):
                temp_model = QueryInstanceBillResponseBodyDataItemsItem()
                self.item.append(temp_model.from_map(k))
        return self


class QueryInstanceBillResponseBodyData(TeaModel):
    def __init__(
        self,
        billing_cycle: str = None,
        account_id: str = None,
        account_name: str = None,
        total_count: int = None,
        page_num: int = None,
        page_size: int = None,
        items: QueryInstanceBillResponseBodyDataItems = None,
    ):
        self.billing_cycle = billing_cycle
        self.account_id = account_id
        self.account_name = account_name
        self.total_count = total_count
        self.page_num = page_num
        self.page_size = page_size
        self.items = items

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle
        if self.account_id is not None:
            result['AccountID'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.items is not None:
            result['Items'] = self.items.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')
        if m.get('AccountID') is not None:
            self.account_id = m.get('AccountID')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Items') is not None:
            temp_model = QueryInstanceBillResponseBodyDataItems()
            self.items = temp_model.from_map(m['Items'])
        return self


class QueryInstanceBillResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        data: QueryInstanceBillResponseBodyData = None,
    ):
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = QueryInstanceBillResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryInstanceBillResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryInstanceBillResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = QueryInstanceBillResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryInstanceByTagRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class QueryInstanceByTagRequest(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
        resource_id: List[str] = None,
        tag: List[QueryInstanceByTagRequestTag] = None,
    ):
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = QueryInstanceByTagRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class QueryInstanceByTagResponseBodyTagResourceTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class QueryInstanceByTagResponseBodyTagResource(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        tag: List[QueryInstanceByTagResponseBodyTagResourceTag] = None,
    ):
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = QueryInstanceByTagResponseBodyTagResourceTag()
                self.tag.append(temp_model.from_map(k))
        return self


class QueryInstanceByTagResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        request_id: str = None,
        success: bool = None,
        message: str = None,
        next_token: str = None,
        tag_resource: List[QueryInstanceByTagResponseBodyTagResource] = None,
    ):
        self.code = code
        self.request_id = request_id
        self.success = success
        self.message = message
        self.next_token = next_token
        self.tag_resource = tag_resource

    def validate(self):
        if self.tag_resource:
            for k in self.tag_resource:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['TagResource'] = []
        if self.tag_resource is not None:
            for k in self.tag_resource:
                result['TagResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.tag_resource = []
        if m.get('TagResource') is not None:
            for k in m.get('TagResource'):
                temp_model = QueryInstanceByTagResponseBodyTagResource()
                self.tag_resource.append(temp_model.from_map(k))
        return self


class QueryInstanceByTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryInstanceByTagResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = QueryInstanceByTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryInstanceGaapCostRequest(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        billing_cycle: str = None,
        product_code: str = None,
        product_type: str = None,
        subscription_type: str = None,
    ):
        self.page_num = page_num
        self.page_size = page_size
        self.billing_cycle = billing_cycle
        self.product_code = product_code
        self.product_type = product_type
        self.subscription_type = subscription_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        return self


class QueryInstanceGaapCostResponseBodyDataModulesModule(TeaModel):
    def __init__(
        self,
        billing_cycle: str = None,
        instance_id: str = None,
        product_code: str = None,
        product_type: str = None,
        subscription_type: str = None,
        tag: str = None,
        resource_group: str = None,
        accounting_unit: str = None,
        payer_account: str = None,
        owner_id: str = None,
        region: str = None,
        currency: str = None,
        payment_currency: str = None,
        order_type: str = None,
        pay_time: str = None,
        pretax_gross_amount: str = None,
        pricing_discount: str = None,
        deducted_by_coupons: str = None,
        pretax_amount: str = None,
        pretax_amount_local: str = None,
        deducted_by_cash_coupons: str = None,
        deducted_by_prepaid_card: str = None,
        payment_amount: str = None,
        gaap_pretax_gross_amount: str = None,
        gaap_pricing_discount: str = None,
        gaap_deducted_by_coupons: str = None,
        gaap_pretax_amount: str = None,
        gaap_pretax_amount_local: str = None,
        gaap_deducted_by_cash_coupons: str = None,
        gaap_deducted_by_prepaid_card: str = None,
        gaap_payment_amount: str = None,
        month_gaap_pretax_gross_amount: str = None,
        month_gaap_pricing_discount: str = None,
        month_gaap_deducted_by_coupons: str = None,
        month_gaap_pretax_amount: str = None,
        month_gaap_pretax_amount_local: str = None,
        month_gaap_deducted_by_cash_coupons: str = None,
        month_gaap_deducted_by_prepaid_card: str = None,
        month_gaap_payment_amount: str = None,
        unallocated_payment_amount: str = None,
        usage_start_date: str = None,
        usage_end_date: str = None,
        bill_type: str = None,
        order_id: str = None,
        sub_order_id: str = None,
        unallocated_pretax_gross_amount: str = None,
        unallocated_pricing_discount: str = None,
        unallocated_deducted_by_coupons: str = None,
        unallocated_pretax_amount: str = None,
        unallocated_pretax_amount_local: str = None,
        unallocated_deducted_by_cash_coupons: str = None,
        unallocated_deducted_by_prepaid_card: str = None,
    ):
        self.billing_cycle = billing_cycle
        self.instance_id = instance_id
        self.product_code = product_code
        self.product_type = product_type
        self.subscription_type = subscription_type
        self.tag = tag
        self.resource_group = resource_group
        self.accounting_unit = accounting_unit
        self.payer_account = payer_account
        self.owner_id = owner_id
        self.region = region
        self.currency = currency
        self.payment_currency = payment_currency
        self.order_type = order_type
        self.pay_time = pay_time
        self.pretax_gross_amount = pretax_gross_amount
        self.pricing_discount = pricing_discount
        self.deducted_by_coupons = deducted_by_coupons
        self.pretax_amount = pretax_amount
        self.pretax_amount_local = pretax_amount_local
        self.deducted_by_cash_coupons = deducted_by_cash_coupons
        self.deducted_by_prepaid_card = deducted_by_prepaid_card
        self.payment_amount = payment_amount
        self.gaap_pretax_gross_amount = gaap_pretax_gross_amount
        self.gaap_pricing_discount = gaap_pricing_discount
        self.gaap_deducted_by_coupons = gaap_deducted_by_coupons
        self.gaap_pretax_amount = gaap_pretax_amount
        self.gaap_pretax_amount_local = gaap_pretax_amount_local
        self.gaap_deducted_by_cash_coupons = gaap_deducted_by_cash_coupons
        self.gaap_deducted_by_prepaid_card = gaap_deducted_by_prepaid_card
        self.gaap_payment_amount = gaap_payment_amount
        self.month_gaap_pretax_gross_amount = month_gaap_pretax_gross_amount
        self.month_gaap_pricing_discount = month_gaap_pricing_discount
        self.month_gaap_deducted_by_coupons = month_gaap_deducted_by_coupons
        self.month_gaap_pretax_amount = month_gaap_pretax_amount
        self.month_gaap_pretax_amount_local = month_gaap_pretax_amount_local
        self.month_gaap_deducted_by_cash_coupons = month_gaap_deducted_by_cash_coupons
        self.month_gaap_deducted_by_prepaid_card = month_gaap_deducted_by_prepaid_card
        self.month_gaap_payment_amount = month_gaap_payment_amount
        self.unallocated_payment_amount = unallocated_payment_amount
        self.usage_start_date = usage_start_date
        self.usage_end_date = usage_end_date
        self.bill_type = bill_type
        self.order_id = order_id
        self.sub_order_id = sub_order_id
        self.unallocated_pretax_gross_amount = unallocated_pretax_gross_amount
        self.unallocated_pricing_discount = unallocated_pricing_discount
        self.unallocated_deducted_by_coupons = unallocated_deducted_by_coupons
        self.unallocated_pretax_amount = unallocated_pretax_amount
        self.unallocated_pretax_amount_local = unallocated_pretax_amount_local
        self.unallocated_deducted_by_cash_coupons = unallocated_deducted_by_cash_coupons
        self.unallocated_deducted_by_prepaid_card = unallocated_deducted_by_prepaid_card

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group
        if self.accounting_unit is not None:
            result['AccountingUnit'] = self.accounting_unit
        if self.payer_account is not None:
            result['PayerAccount'] = self.payer_account
        if self.owner_id is not None:
            result['OwnerID'] = self.owner_id
        if self.region is not None:
            result['Region'] = self.region
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.payment_currency is not None:
            result['PaymentCurrency'] = self.payment_currency
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.pay_time is not None:
            result['PayTime'] = self.pay_time
        if self.pretax_gross_amount is not None:
            result['PretaxGrossAmount'] = self.pretax_gross_amount
        if self.pricing_discount is not None:
            result['PricingDiscount'] = self.pricing_discount
        if self.deducted_by_coupons is not None:
            result['DeductedByCoupons'] = self.deducted_by_coupons
        if self.pretax_amount is not None:
            result['PretaxAmount'] = self.pretax_amount
        if self.pretax_amount_local is not None:
            result['PretaxAmountLocal'] = self.pretax_amount_local
        if self.deducted_by_cash_coupons is not None:
            result['DeductedByCashCoupons'] = self.deducted_by_cash_coupons
        if self.deducted_by_prepaid_card is not None:
            result['DeductedByPrepaidCard'] = self.deducted_by_prepaid_card
        if self.payment_amount is not None:
            result['PaymentAmount'] = self.payment_amount
        if self.gaap_pretax_gross_amount is not None:
            result['GaapPretaxGrossAmount'] = self.gaap_pretax_gross_amount
        if self.gaap_pricing_discount is not None:
            result['GaapPricingDiscount'] = self.gaap_pricing_discount
        if self.gaap_deducted_by_coupons is not None:
            result['GaapDeductedByCoupons'] = self.gaap_deducted_by_coupons
        if self.gaap_pretax_amount is not None:
            result['GaapPretaxAmount'] = self.gaap_pretax_amount
        if self.gaap_pretax_amount_local is not None:
            result['GaapPretaxAmountLocal'] = self.gaap_pretax_amount_local
        if self.gaap_deducted_by_cash_coupons is not None:
            result['GaapDeductedByCashCoupons'] = self.gaap_deducted_by_cash_coupons
        if self.gaap_deducted_by_prepaid_card is not None:
            result['GaapDeductedByPrepaidCard'] = self.gaap_deducted_by_prepaid_card
        if self.gaap_payment_amount is not None:
            result['GaapPaymentAmount'] = self.gaap_payment_amount
        if self.month_gaap_pretax_gross_amount is not None:
            result['MonthGaapPretaxGrossAmount'] = self.month_gaap_pretax_gross_amount
        if self.month_gaap_pricing_discount is not None:
            result['MonthGaapPricingDiscount'] = self.month_gaap_pricing_discount
        if self.month_gaap_deducted_by_coupons is not None:
            result['MonthGaapDeductedByCoupons'] = self.month_gaap_deducted_by_coupons
        if self.month_gaap_pretax_amount is not None:
            result['MonthGaapPretaxAmount'] = self.month_gaap_pretax_amount
        if self.month_gaap_pretax_amount_local is not None:
            result['MonthGaapPretaxAmountLocal'] = self.month_gaap_pretax_amount_local
        if self.month_gaap_deducted_by_cash_coupons is not None:
            result['MonthGaapDeductedByCashCoupons'] = self.month_gaap_deducted_by_cash_coupons
        if self.month_gaap_deducted_by_prepaid_card is not None:
            result['MonthGaapDeductedByPrepaidCard'] = self.month_gaap_deducted_by_prepaid_card
        if self.month_gaap_payment_amount is not None:
            result['MonthGaapPaymentAmount'] = self.month_gaap_payment_amount
        if self.unallocated_payment_amount is not None:
            result['UnallocatedPaymentAmount'] = self.unallocated_payment_amount
        if self.usage_start_date is not None:
            result['UsageStartDate'] = self.usage_start_date
        if self.usage_end_date is not None:
            result['UsageEndDate'] = self.usage_end_date
        if self.bill_type is not None:
            result['BillType'] = self.bill_type
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.sub_order_id is not None:
            result['SubOrderId'] = self.sub_order_id
        if self.unallocated_pretax_gross_amount is not None:
            result['UnallocatedPretaxGrossAmount'] = self.unallocated_pretax_gross_amount
        if self.unallocated_pricing_discount is not None:
            result['UnallocatedPricingDiscount'] = self.unallocated_pricing_discount
        if self.unallocated_deducted_by_coupons is not None:
            result['UnallocatedDeductedByCoupons'] = self.unallocated_deducted_by_coupons
        if self.unallocated_pretax_amount is not None:
            result['UnallocatedPretaxAmount'] = self.unallocated_pretax_amount
        if self.unallocated_pretax_amount_local is not None:
            result['UnallocatedPretaxAmountLocal'] = self.unallocated_pretax_amount_local
        if self.unallocated_deducted_by_cash_coupons is not None:
            result['UnallocatedDeductedByCashCoupons'] = self.unallocated_deducted_by_cash_coupons
        if self.unallocated_deducted_by_prepaid_card is not None:
            result['UnallocatedDeductedByPrepaidCard'] = self.unallocated_deducted_by_prepaid_card
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('ResourceGroup') is not None:
            self.resource_group = m.get('ResourceGroup')
        if m.get('AccountingUnit') is not None:
            self.accounting_unit = m.get('AccountingUnit')
        if m.get('PayerAccount') is not None:
            self.payer_account = m.get('PayerAccount')
        if m.get('OwnerID') is not None:
            self.owner_id = m.get('OwnerID')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('PaymentCurrency') is not None:
            self.payment_currency = m.get('PaymentCurrency')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('PayTime') is not None:
            self.pay_time = m.get('PayTime')
        if m.get('PretaxGrossAmount') is not None:
            self.pretax_gross_amount = m.get('PretaxGrossAmount')
        if m.get('PricingDiscount') is not None:
            self.pricing_discount = m.get('PricingDiscount')
        if m.get('DeductedByCoupons') is not None:
            self.deducted_by_coupons = m.get('DeductedByCoupons')
        if m.get('PretaxAmount') is not None:
            self.pretax_amount = m.get('PretaxAmount')
        if m.get('PretaxAmountLocal') is not None:
            self.pretax_amount_local = m.get('PretaxAmountLocal')
        if m.get('DeductedByCashCoupons') is not None:
            self.deducted_by_cash_coupons = m.get('DeductedByCashCoupons')
        if m.get('DeductedByPrepaidCard') is not None:
            self.deducted_by_prepaid_card = m.get('DeductedByPrepaidCard')
        if m.get('PaymentAmount') is not None:
            self.payment_amount = m.get('PaymentAmount')
        if m.get('GaapPretaxGrossAmount') is not None:
            self.gaap_pretax_gross_amount = m.get('GaapPretaxGrossAmount')
        if m.get('GaapPricingDiscount') is not None:
            self.gaap_pricing_discount = m.get('GaapPricingDiscount')
        if m.get('GaapDeductedByCoupons') is not None:
            self.gaap_deducted_by_coupons = m.get('GaapDeductedByCoupons')
        if m.get('GaapPretaxAmount') is not None:
            self.gaap_pretax_amount = m.get('GaapPretaxAmount')
        if m.get('GaapPretaxAmountLocal') is not None:
            self.gaap_pretax_amount_local = m.get('GaapPretaxAmountLocal')
        if m.get('GaapDeductedByCashCoupons') is not None:
            self.gaap_deducted_by_cash_coupons = m.get('GaapDeductedByCashCoupons')
        if m.get('GaapDeductedByPrepaidCard') is not None:
            self.gaap_deducted_by_prepaid_card = m.get('GaapDeductedByPrepaidCard')
        if m.get('GaapPaymentAmount') is not None:
            self.gaap_payment_amount = m.get('GaapPaymentAmount')
        if m.get('MonthGaapPretaxGrossAmount') is not None:
            self.month_gaap_pretax_gross_amount = m.get('MonthGaapPretaxGrossAmount')
        if m.get('MonthGaapPricingDiscount') is not None:
            self.month_gaap_pricing_discount = m.get('MonthGaapPricingDiscount')
        if m.get('MonthGaapDeductedByCoupons') is not None:
            self.month_gaap_deducted_by_coupons = m.get('MonthGaapDeductedByCoupons')
        if m.get('MonthGaapPretaxAmount') is not None:
            self.month_gaap_pretax_amount = m.get('MonthGaapPretaxAmount')
        if m.get('MonthGaapPretaxAmountLocal') is not None:
            self.month_gaap_pretax_amount_local = m.get('MonthGaapPretaxAmountLocal')
        if m.get('MonthGaapDeductedByCashCoupons') is not None:
            self.month_gaap_deducted_by_cash_coupons = m.get('MonthGaapDeductedByCashCoupons')
        if m.get('MonthGaapDeductedByPrepaidCard') is not None:
            self.month_gaap_deducted_by_prepaid_card = m.get('MonthGaapDeductedByPrepaidCard')
        if m.get('MonthGaapPaymentAmount') is not None:
            self.month_gaap_payment_amount = m.get('MonthGaapPaymentAmount')
        if m.get('UnallocatedPaymentAmount') is not None:
            self.unallocated_payment_amount = m.get('UnallocatedPaymentAmount')
        if m.get('UsageStartDate') is not None:
            self.usage_start_date = m.get('UsageStartDate')
        if m.get('UsageEndDate') is not None:
            self.usage_end_date = m.get('UsageEndDate')
        if m.get('BillType') is not None:
            self.bill_type = m.get('BillType')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('SubOrderId') is not None:
            self.sub_order_id = m.get('SubOrderId')
        if m.get('UnallocatedPretaxGrossAmount') is not None:
            self.unallocated_pretax_gross_amount = m.get('UnallocatedPretaxGrossAmount')
        if m.get('UnallocatedPricingDiscount') is not None:
            self.unallocated_pricing_discount = m.get('UnallocatedPricingDiscount')
        if m.get('UnallocatedDeductedByCoupons') is not None:
            self.unallocated_deducted_by_coupons = m.get('UnallocatedDeductedByCoupons')
        if m.get('UnallocatedPretaxAmount') is not None:
            self.unallocated_pretax_amount = m.get('UnallocatedPretaxAmount')
        if m.get('UnallocatedPretaxAmountLocal') is not None:
            self.unallocated_pretax_amount_local = m.get('UnallocatedPretaxAmountLocal')
        if m.get('UnallocatedDeductedByCashCoupons') is not None:
            self.unallocated_deducted_by_cash_coupons = m.get('UnallocatedDeductedByCashCoupons')
        if m.get('UnallocatedDeductedByPrepaidCard') is not None:
            self.unallocated_deducted_by_prepaid_card = m.get('UnallocatedDeductedByPrepaidCard')
        return self


class QueryInstanceGaapCostResponseBodyDataModules(TeaModel):
    def __init__(
        self,
        module: List[QueryInstanceGaapCostResponseBodyDataModulesModule] = None,
    ):
        self.module = module

    def validate(self):
        if self.module:
            for k in self.module:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Module'] = []
        if self.module is not None:
            for k in self.module:
                result['Module'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.module = []
        if m.get('Module') is not None:
            for k in m.get('Module'):
                temp_model = QueryInstanceGaapCostResponseBodyDataModulesModule()
                self.module.append(temp_model.from_map(k))
        return self


class QueryInstanceGaapCostResponseBodyData(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        page_num: int = None,
        page_size: int = None,
        total_count: int = None,
        modules: QueryInstanceGaapCostResponseBodyDataModules = None,
    ):
        self.host_id = host_id
        self.page_num = page_num
        self.page_size = page_size
        self.total_count = total_count
        self.modules = modules

    def validate(self):
        if self.modules:
            self.modules.validate()

    def to_map(self):
        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.modules is not None:
            result['Modules'] = self.modules.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Modules') is not None:
            temp_model = QueryInstanceGaapCostResponseBodyDataModules()
            self.modules = temp_model.from_map(m['Modules'])
        return self


class QueryInstanceGaapCostResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        data: QueryInstanceGaapCostResponseBodyData = None,
    ):
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = QueryInstanceGaapCostResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryInstanceGaapCostResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryInstanceGaapCostResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = QueryInstanceGaapCostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryInvoicingCustomerListRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
    ):
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class QueryInvoicingCustomerListResponseBodyDataCustomerInvoiceListCustomerInvoice(TeaModel):
    def __init__(
        self,
        id: int = None,
        user_id: int = None,
        user_nick: str = None,
        invoice_title: str = None,
        customer_type: int = None,
        taxpayer_type: int = None,
        bank: str = None,
        bank_no: str = None,
        operating_license_address: str = None,
        operating_license_phone: str = None,
        register_no: str = None,
        start_cycle: int = None,
        status: int = None,
        gmt_create: str = None,
        taxation_license: str = None,
        adjust_type: int = None,
        end_cycle: int = None,
        title_change_instructions: str = None,
        issue_type: int = None,
        type: int = None,
        default_remark: str = None,
    ):
        self.id = id
        self.user_id = user_id
        self.user_nick = user_nick
        self.invoice_title = invoice_title
        self.customer_type = customer_type
        self.taxpayer_type = taxpayer_type
        self.bank = bank
        self.bank_no = bank_no
        self.operating_license_address = operating_license_address
        self.operating_license_phone = operating_license_phone
        self.register_no = register_no
        self.start_cycle = start_cycle
        self.status = status
        self.gmt_create = gmt_create
        self.taxation_license = taxation_license
        self.adjust_type = adjust_type
        self.end_cycle = end_cycle
        self.title_change_instructions = title_change_instructions
        self.issue_type = issue_type
        self.type = type
        self.default_remark = default_remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_nick is not None:
            result['UserNick'] = self.user_nick
        if self.invoice_title is not None:
            result['InvoiceTitle'] = self.invoice_title
        if self.customer_type is not None:
            result['CustomerType'] = self.customer_type
        if self.taxpayer_type is not None:
            result['TaxpayerType'] = self.taxpayer_type
        if self.bank is not None:
            result['Bank'] = self.bank
        if self.bank_no is not None:
            result['BankNo'] = self.bank_no
        if self.operating_license_address is not None:
            result['OperatingLicenseAddress'] = self.operating_license_address
        if self.operating_license_phone is not None:
            result['OperatingLicensePhone'] = self.operating_license_phone
        if self.register_no is not None:
            result['RegisterNo'] = self.register_no
        if self.start_cycle is not None:
            result['StartCycle'] = self.start_cycle
        if self.status is not None:
            result['Status'] = self.status
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.taxation_license is not None:
            result['TaxationLicense'] = self.taxation_license
        if self.adjust_type is not None:
            result['AdjustType'] = self.adjust_type
        if self.end_cycle is not None:
            result['EndCycle'] = self.end_cycle
        if self.title_change_instructions is not None:
            result['TitleChangeInstructions'] = self.title_change_instructions
        if self.issue_type is not None:
            result['IssueType'] = self.issue_type
        if self.type is not None:
            result['Type'] = self.type
        if self.default_remark is not None:
            result['DefaultRemark'] = self.default_remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserNick') is not None:
            self.user_nick = m.get('UserNick')
        if m.get('InvoiceTitle') is not None:
            self.invoice_title = m.get('InvoiceTitle')
        if m.get('CustomerType') is not None:
            self.customer_type = m.get('CustomerType')
        if m.get('TaxpayerType') is not None:
            self.taxpayer_type = m.get('TaxpayerType')
        if m.get('Bank') is not None:
            self.bank = m.get('Bank')
        if m.get('BankNo') is not None:
            self.bank_no = m.get('BankNo')
        if m.get('OperatingLicenseAddress') is not None:
            self.operating_license_address = m.get('OperatingLicenseAddress')
        if m.get('OperatingLicensePhone') is not None:
            self.operating_license_phone = m.get('OperatingLicensePhone')
        if m.get('RegisterNo') is not None:
            self.register_no = m.get('RegisterNo')
        if m.get('StartCycle') is not None:
            self.start_cycle = m.get('StartCycle')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('TaxationLicense') is not None:
            self.taxation_license = m.get('TaxationLicense')
        if m.get('AdjustType') is not None:
            self.adjust_type = m.get('AdjustType')
        if m.get('EndCycle') is not None:
            self.end_cycle = m.get('EndCycle')
        if m.get('TitleChangeInstructions') is not None:
            self.title_change_instructions = m.get('TitleChangeInstructions')
        if m.get('IssueType') is not None:
            self.issue_type = m.get('IssueType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('DefaultRemark') is not None:
            self.default_remark = m.get('DefaultRemark')
        return self


class QueryInvoicingCustomerListResponseBodyDataCustomerInvoiceList(TeaModel):
    def __init__(
        self,
        customer_invoice: List[QueryInvoicingCustomerListResponseBodyDataCustomerInvoiceListCustomerInvoice] = None,
    ):
        self.customer_invoice = customer_invoice

    def validate(self):
        if self.customer_invoice:
            for k in self.customer_invoice:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['CustomerInvoice'] = []
        if self.customer_invoice is not None:
            for k in self.customer_invoice:
                result['CustomerInvoice'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.customer_invoice = []
        if m.get('CustomerInvoice') is not None:
            for k in m.get('CustomerInvoice'):
                temp_model = QueryInvoicingCustomerListResponseBodyDataCustomerInvoiceListCustomerInvoice()
                self.customer_invoice.append(temp_model.from_map(k))
        return self


class QueryInvoicingCustomerListResponseBodyData(TeaModel):
    def __init__(
        self,
        customer_invoice_list: QueryInvoicingCustomerListResponseBodyDataCustomerInvoiceList = None,
    ):
        self.customer_invoice_list = customer_invoice_list

    def validate(self):
        if self.customer_invoice_list:
            self.customer_invoice_list.validate()

    def to_map(self):
        result = dict()
        if self.customer_invoice_list is not None:
            result['CustomerInvoiceList'] = self.customer_invoice_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomerInvoiceList') is not None:
            temp_model = QueryInvoicingCustomerListResponseBodyDataCustomerInvoiceList()
            self.customer_invoice_list = temp_model.from_map(m['CustomerInvoiceList'])
        return self


class QueryInvoicingCustomerListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        data: QueryInvoicingCustomerListResponseBodyData = None,
    ):
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = QueryInvoicingCustomerListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryInvoicingCustomerListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryInvoicingCustomerListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = QueryInvoicingCustomerListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMonthlyBillRequest(TeaModel):
    def __init__(
        self,
        billing_cycle: str = None,
    ):
        self.billing_cycle = billing_cycle

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')
        return self


class QueryMonthlyBillResponseBodyDataItemsItem(TeaModel):
    def __init__(
        self,
        item: str = None,
        product_code: str = None,
        product_type: str = None,
        subscription_type: str = None,
        solution_code: str = None,
        solution_name: str = None,
        pretax_gross_amount: float = None,
        invoice_discount: float = None,
        deducted_by_coupons: float = None,
        pretax_amount: float = None,
        currency: str = None,
        pretax_amount_local: float = None,
        tax: float = None,
        after_tax_amount: float = None,
        outstanding_amount: float = None,
        deducted_by_cash_coupons: float = None,
        deducted_by_prepaid_card: float = None,
        payment_amount: float = None,
        payment_currency: str = None,
    ):
        self.item = item
        self.product_code = product_code
        self.product_type = product_type
        self.subscription_type = subscription_type
        self.solution_code = solution_code
        self.solution_name = solution_name
        self.pretax_gross_amount = pretax_gross_amount
        self.invoice_discount = invoice_discount
        self.deducted_by_coupons = deducted_by_coupons
        self.pretax_amount = pretax_amount
        self.currency = currency
        self.pretax_amount_local = pretax_amount_local
        self.tax = tax
        self.after_tax_amount = after_tax_amount
        self.outstanding_amount = outstanding_amount
        self.deducted_by_cash_coupons = deducted_by_cash_coupons
        self.deducted_by_prepaid_card = deducted_by_prepaid_card
        self.payment_amount = payment_amount
        self.payment_currency = payment_currency

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.item is not None:
            result['Item'] = self.item
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.solution_code is not None:
            result['SolutionCode'] = self.solution_code
        if self.solution_name is not None:
            result['SolutionName'] = self.solution_name
        if self.pretax_gross_amount is not None:
            result['PretaxGrossAmount'] = self.pretax_gross_amount
        if self.invoice_discount is not None:
            result['InvoiceDiscount'] = self.invoice_discount
        if self.deducted_by_coupons is not None:
            result['DeductedByCoupons'] = self.deducted_by_coupons
        if self.pretax_amount is not None:
            result['PretaxAmount'] = self.pretax_amount
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.pretax_amount_local is not None:
            result['PretaxAmountLocal'] = self.pretax_amount_local
        if self.tax is not None:
            result['Tax'] = self.tax
        if self.after_tax_amount is not None:
            result['AfterTaxAmount'] = self.after_tax_amount
        if self.outstanding_amount is not None:
            result['OutstandingAmount'] = self.outstanding_amount
        if self.deducted_by_cash_coupons is not None:
            result['DeductedByCashCoupons'] = self.deducted_by_cash_coupons
        if self.deducted_by_prepaid_card is not None:
            result['DeductedByPrepaidCard'] = self.deducted_by_prepaid_card
        if self.payment_amount is not None:
            result['PaymentAmount'] = self.payment_amount
        if self.payment_currency is not None:
            result['PaymentCurrency'] = self.payment_currency
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Item') is not None:
            self.item = m.get('Item')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('SolutionCode') is not None:
            self.solution_code = m.get('SolutionCode')
        if m.get('SolutionName') is not None:
            self.solution_name = m.get('SolutionName')
        if m.get('PretaxGrossAmount') is not None:
            self.pretax_gross_amount = m.get('PretaxGrossAmount')
        if m.get('InvoiceDiscount') is not None:
            self.invoice_discount = m.get('InvoiceDiscount')
        if m.get('DeductedByCoupons') is not None:
            self.deducted_by_coupons = m.get('DeductedByCoupons')
        if m.get('PretaxAmount') is not None:
            self.pretax_amount = m.get('PretaxAmount')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('PretaxAmountLocal') is not None:
            self.pretax_amount_local = m.get('PretaxAmountLocal')
        if m.get('Tax') is not None:
            self.tax = m.get('Tax')
        if m.get('AfterTaxAmount') is not None:
            self.after_tax_amount = m.get('AfterTaxAmount')
        if m.get('OutstandingAmount') is not None:
            self.outstanding_amount = m.get('OutstandingAmount')
        if m.get('DeductedByCashCoupons') is not None:
            self.deducted_by_cash_coupons = m.get('DeductedByCashCoupons')
        if m.get('DeductedByPrepaidCard') is not None:
            self.deducted_by_prepaid_card = m.get('DeductedByPrepaidCard')
        if m.get('PaymentAmount') is not None:
            self.payment_amount = m.get('PaymentAmount')
        if m.get('PaymentCurrency') is not None:
            self.payment_currency = m.get('PaymentCurrency')
        return self


class QueryMonthlyBillResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        item: List[QueryMonthlyBillResponseBodyDataItemsItem] = None,
    ):
        self.item = item

    def validate(self):
        if self.item:
            for k in self.item:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Item'] = []
        if self.item is not None:
            for k in self.item:
                result['Item'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.item = []
        if m.get('Item') is not None:
            for k in m.get('Item'):
                temp_model = QueryMonthlyBillResponseBodyDataItemsItem()
                self.item.append(temp_model.from_map(k))
        return self


class QueryMonthlyBillResponseBodyData(TeaModel):
    def __init__(
        self,
        outstanding_amount: float = None,
        total_outstanding_amount: float = None,
        new_invoice_amount: float = None,
        billing_cycle: str = None,
        items: QueryMonthlyBillResponseBodyDataItems = None,
    ):
        self.outstanding_amount = outstanding_amount
        self.total_outstanding_amount = total_outstanding_amount
        self.new_invoice_amount = new_invoice_amount
        self.billing_cycle = billing_cycle
        self.items = items

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        if self.outstanding_amount is not None:
            result['OutstandingAmount'] = self.outstanding_amount
        if self.total_outstanding_amount is not None:
            result['TotalOutstandingAmount'] = self.total_outstanding_amount
        if self.new_invoice_amount is not None:
            result['NewInvoiceAmount'] = self.new_invoice_amount
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle
        if self.items is not None:
            result['Items'] = self.items.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutstandingAmount') is not None:
            self.outstanding_amount = m.get('OutstandingAmount')
        if m.get('TotalOutstandingAmount') is not None:
            self.total_outstanding_amount = m.get('TotalOutstandingAmount')
        if m.get('NewInvoiceAmount') is not None:
            self.new_invoice_amount = m.get('NewInvoiceAmount')
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')
        if m.get('Items') is not None:
            temp_model = QueryMonthlyBillResponseBodyDataItems()
            self.items = temp_model.from_map(m['Items'])
        return self


class QueryMonthlyBillResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        data: QueryMonthlyBillResponseBodyData = None,
    ):
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = QueryMonthlyBillResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryMonthlyBillResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryMonthlyBillResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = QueryMonthlyBillResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMonthlyInstanceConsumptionRequest(TeaModel):
    def __init__(
        self,
        product_code: str = None,
        owner_id: int = None,
        page_num: int = None,
        page_size: int = None,
        billing_cycle: str = None,
        product_type: str = None,
        subscription_type: str = None,
    ):
        self.product_code = product_code
        self.owner_id = owner_id
        self.page_num = page_num
        self.page_size = page_size
        self.billing_cycle = billing_cycle
        self.product_type = product_type
        self.subscription_type = subscription_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        return self


class QueryMonthlyInstanceConsumptionResponseBodyDataItemsItem(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        product_code: str = None,
        product_type: str = None,
        subscription_type: str = None,
        tag: str = None,
        resource_group: str = None,
        payer_account: str = None,
        owner_id: str = None,
        region: str = None,
        pretax_gross_amount: float = None,
        discount_amount: float = None,
        pretax_amount: float = None,
        currency: str = None,
        pretax_amount_local: float = None,
        tax: float = None,
        after_tax_amount: float = None,
        payment_currency: str = None,
    ):
        self.instance_id = instance_id
        self.product_code = product_code
        self.product_type = product_type
        self.subscription_type = subscription_type
        self.tag = tag
        self.resource_group = resource_group
        self.payer_account = payer_account
        self.owner_id = owner_id
        self.region = region
        self.pretax_gross_amount = pretax_gross_amount
        self.discount_amount = discount_amount
        self.pretax_amount = pretax_amount
        self.currency = currency
        self.pretax_amount_local = pretax_amount_local
        self.tax = tax
        self.after_tax_amount = after_tax_amount
        self.payment_currency = payment_currency

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group
        if self.payer_account is not None:
            result['PayerAccount'] = self.payer_account
        if self.owner_id is not None:
            result['OwnerID'] = self.owner_id
        if self.region is not None:
            result['Region'] = self.region
        if self.pretax_gross_amount is not None:
            result['PretaxGrossAmount'] = self.pretax_gross_amount
        if self.discount_amount is not None:
            result['DiscountAmount'] = self.discount_amount
        if self.pretax_amount is not None:
            result['PretaxAmount'] = self.pretax_amount
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.pretax_amount_local is not None:
            result['PretaxAmountLocal'] = self.pretax_amount_local
        if self.tax is not None:
            result['Tax'] = self.tax
        if self.after_tax_amount is not None:
            result['AfterTaxAmount'] = self.after_tax_amount
        if self.payment_currency is not None:
            result['PaymentCurrency'] = self.payment_currency
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('ResourceGroup') is not None:
            self.resource_group = m.get('ResourceGroup')
        if m.get('PayerAccount') is not None:
            self.payer_account = m.get('PayerAccount')
        if m.get('OwnerID') is not None:
            self.owner_id = m.get('OwnerID')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('PretaxGrossAmount') is not None:
            self.pretax_gross_amount = m.get('PretaxGrossAmount')
        if m.get('DiscountAmount') is not None:
            self.discount_amount = m.get('DiscountAmount')
        if m.get('PretaxAmount') is not None:
            self.pretax_amount = m.get('PretaxAmount')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('PretaxAmountLocal') is not None:
            self.pretax_amount_local = m.get('PretaxAmountLocal')
        if m.get('Tax') is not None:
            self.tax = m.get('Tax')
        if m.get('AfterTaxAmount') is not None:
            self.after_tax_amount = m.get('AfterTaxAmount')
        if m.get('PaymentCurrency') is not None:
            self.payment_currency = m.get('PaymentCurrency')
        return self


class QueryMonthlyInstanceConsumptionResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        item: List[QueryMonthlyInstanceConsumptionResponseBodyDataItemsItem] = None,
    ):
        self.item = item

    def validate(self):
        if self.item:
            for k in self.item:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Item'] = []
        if self.item is not None:
            for k in self.item:
                result['Item'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.item = []
        if m.get('Item') is not None:
            for k in m.get('Item'):
                temp_model = QueryMonthlyInstanceConsumptionResponseBodyDataItemsItem()
                self.item.append(temp_model.from_map(k))
        return self


class QueryMonthlyInstanceConsumptionResponseBodyData(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        total_count: int = None,
        billing_cycle: str = None,
        items: QueryMonthlyInstanceConsumptionResponseBodyDataItems = None,
    ):
        self.page_num = page_num
        self.page_size = page_size
        self.total_count = total_count
        self.billing_cycle = billing_cycle
        self.items = items

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle
        if self.items is not None:
            result['Items'] = self.items.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')
        if m.get('Items') is not None:
            temp_model = QueryMonthlyInstanceConsumptionResponseBodyDataItems()
            self.items = temp_model.from_map(m['Items'])
        return self


class QueryMonthlyInstanceConsumptionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        data: QueryMonthlyInstanceConsumptionResponseBodyData = None,
    ):
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = QueryMonthlyInstanceConsumptionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryMonthlyInstanceConsumptionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryMonthlyInstanceConsumptionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = QueryMonthlyInstanceConsumptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryOrdersRequest(TeaModel):
    def __init__(
        self,
        create_time_end: str = None,
        page_num: int = None,
        page_size: int = None,
        product_code: str = None,
        product_type: str = None,
        subscription_type: str = None,
        order_type: str = None,
        payment_status: str = None,
        create_time_start: str = None,
        owner_id: int = None,
    ):
        self.create_time_end = create_time_end
        self.page_num = page_num
        self.page_size = page_size
        self.product_code = product_code
        self.product_type = product_type
        self.subscription_type = subscription_type
        self.order_type = order_type
        self.payment_status = payment_status
        self.create_time_start = create_time_start
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.create_time_end is not None:
            result['CreateTimeEnd'] = self.create_time_end
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.payment_status is not None:
            result['PaymentStatus'] = self.payment_status
        if self.create_time_start is not None:
            result['CreateTimeStart'] = self.create_time_start
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTimeEnd') is not None:
            self.create_time_end = m.get('CreateTimeEnd')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('PaymentStatus') is not None:
            self.payment_status = m.get('PaymentStatus')
        if m.get('CreateTimeStart') is not None:
            self.create_time_start = m.get('CreateTimeStart')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class QueryOrdersResponseBodyDataOrderListOrder(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        product_code: str = None,
        product_type: str = None,
        subscription_type: str = None,
        order_type: str = None,
        create_time: str = None,
        payment_time: str = None,
        payment_status: str = None,
        pretax_gross_amount: str = None,
        pretax_amount: str = None,
        currency: str = None,
        pretax_amount_local: str = None,
        tax: str = None,
        after_tax_amount: str = None,
        payment_currency: str = None,
        related_order_id: str = None,
        commodity_code: str = None,
    ):
        self.order_id = order_id
        self.product_code = product_code
        self.product_type = product_type
        self.subscription_type = subscription_type
        self.order_type = order_type
        self.create_time = create_time
        self.payment_time = payment_time
        self.payment_status = payment_status
        self.pretax_gross_amount = pretax_gross_amount
        self.pretax_amount = pretax_amount
        self.currency = currency
        self.pretax_amount_local = pretax_amount_local
        self.tax = tax
        self.after_tax_amount = after_tax_amount
        self.payment_currency = payment_currency
        self.related_order_id = related_order_id
        self.commodity_code = commodity_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.payment_time is not None:
            result['PaymentTime'] = self.payment_time
        if self.payment_status is not None:
            result['PaymentStatus'] = self.payment_status
        if self.pretax_gross_amount is not None:
            result['PretaxGrossAmount'] = self.pretax_gross_amount
        if self.pretax_amount is not None:
            result['PretaxAmount'] = self.pretax_amount
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.pretax_amount_local is not None:
            result['PretaxAmountLocal'] = self.pretax_amount_local
        if self.tax is not None:
            result['Tax'] = self.tax
        if self.after_tax_amount is not None:
            result['AfterTaxAmount'] = self.after_tax_amount
        if self.payment_currency is not None:
            result['PaymentCurrency'] = self.payment_currency
        if self.related_order_id is not None:
            result['RelatedOrderId'] = self.related_order_id
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('PaymentTime') is not None:
            self.payment_time = m.get('PaymentTime')
        if m.get('PaymentStatus') is not None:
            self.payment_status = m.get('PaymentStatus')
        if m.get('PretaxGrossAmount') is not None:
            self.pretax_gross_amount = m.get('PretaxGrossAmount')
        if m.get('PretaxAmount') is not None:
            self.pretax_amount = m.get('PretaxAmount')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('PretaxAmountLocal') is not None:
            self.pretax_amount_local = m.get('PretaxAmountLocal')
        if m.get('Tax') is not None:
            self.tax = m.get('Tax')
        if m.get('AfterTaxAmount') is not None:
            self.after_tax_amount = m.get('AfterTaxAmount')
        if m.get('PaymentCurrency') is not None:
            self.payment_currency = m.get('PaymentCurrency')
        if m.get('RelatedOrderId') is not None:
            self.related_order_id = m.get('RelatedOrderId')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        return self


class QueryOrdersResponseBodyDataOrderList(TeaModel):
    def __init__(
        self,
        order: List[QueryOrdersResponseBodyDataOrderListOrder] = None,
    ):
        self.order = order

    def validate(self):
        if self.order:
            for k in self.order:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Order'] = []
        if self.order is not None:
            for k in self.order:
                result['Order'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.order = []
        if m.get('Order') is not None:
            for k in m.get('Order'):
                temp_model = QueryOrdersResponseBodyDataOrderListOrder()
                self.order.append(temp_model.from_map(k))
        return self


class QueryOrdersResponseBodyData(TeaModel):
    def __init__(
        self,
        host_name: str = None,
        page_num: int = None,
        page_size: int = None,
        total_count: int = None,
        order_list: QueryOrdersResponseBodyDataOrderList = None,
    ):
        self.host_name = host_name
        self.page_num = page_num
        self.page_size = page_size
        self.total_count = total_count
        self.order_list = order_list

    def validate(self):
        if self.order_list:
            self.order_list.validate()

    def to_map(self):
        result = dict()
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.order_list is not None:
            result['OrderList'] = self.order_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('OrderList') is not None:
            temp_model = QueryOrdersResponseBodyDataOrderList()
            self.order_list = temp_model.from_map(m['OrderList'])
        return self


class QueryOrdersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        data: QueryOrdersResponseBodyData = None,
    ):
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = QueryOrdersResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryOrdersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryOrdersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = QueryOrdersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPermissionListRequest(TeaModel):
    def __init__(
        self,
        relation_id: int = None,
    ):
        self.relation_id = relation_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.relation_id is not None:
            result['RelationId'] = self.relation_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RelationId') is not None:
            self.relation_id = m.get('RelationId')
        return self


class QueryPermissionListResponseBodyDataPermissionList(TeaModel):
    def __init__(
        self,
        permission_code: str = None,
        permission_name: str = None,
        start_time: str = None,
        end_time: str = None,
    ):
        self.permission_code = permission_code
        self.permission_name = permission_name
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.permission_code is not None:
            result['PermissionCode'] = self.permission_code
        if self.permission_name is not None:
            result['PermissionName'] = self.permission_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PermissionCode') is not None:
            self.permission_code = m.get('PermissionCode')
        if m.get('PermissionName') is not None:
            self.permission_name = m.get('PermissionName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class QueryPermissionListResponseBodyData(TeaModel):
    def __init__(
        self,
        master_id: int = None,
        member_id: int = None,
        relation_type: str = None,
        state: str = None,
        setup_time: str = None,
        start_time: str = None,
        end_time: str = None,
        permission_list: List[QueryPermissionListResponseBodyDataPermissionList] = None,
    ):
        self.master_id = master_id
        self.member_id = member_id
        self.relation_type = relation_type
        self.state = state
        self.setup_time = setup_time
        self.start_time = start_time
        self.end_time = end_time
        self.permission_list = permission_list

    def validate(self):
        if self.permission_list:
            for k in self.permission_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.master_id is not None:
            result['MasterId'] = self.master_id
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.relation_type is not None:
            result['RelationType'] = self.relation_type
        if self.state is not None:
            result['State'] = self.state
        if self.setup_time is not None:
            result['SetupTime'] = self.setup_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        result['PermissionList'] = []
        if self.permission_list is not None:
            for k in self.permission_list:
                result['PermissionList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MasterId') is not None:
            self.master_id = m.get('MasterId')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('RelationType') is not None:
            self.relation_type = m.get('RelationType')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('SetupTime') is not None:
            self.setup_time = m.get('SetupTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        self.permission_list = []
        if m.get('PermissionList') is not None:
            for k in m.get('PermissionList'):
                temp_model = QueryPermissionListResponseBodyDataPermissionList()
                self.permission_list.append(temp_model.from_map(k))
        return self


class QueryPermissionListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        request_id: str = None,
        success: bool = None,
        message: str = None,
        data: QueryPermissionListResponseBodyData = None,
    ):
        self.code = code
        self.request_id = request_id
        self.success = success
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = QueryPermissionListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryPermissionListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryPermissionListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = QueryPermissionListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPrepaidCardsRequest(TeaModel):
    def __init__(
        self,
        expiry_time_end: str = None,
        expiry_time_start: str = None,
        effective_or_not: bool = None,
    ):
        self.expiry_time_end = expiry_time_end
        self.expiry_time_start = expiry_time_start
        self.effective_or_not = effective_or_not

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.expiry_time_end is not None:
            result['ExpiryTimeEnd'] = self.expiry_time_end
        if self.expiry_time_start is not None:
            result['ExpiryTimeStart'] = self.expiry_time_start
        if self.effective_or_not is not None:
            result['EffectiveOrNot'] = self.effective_or_not
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpiryTimeEnd') is not None:
            self.expiry_time_end = m.get('ExpiryTimeEnd')
        if m.get('ExpiryTimeStart') is not None:
            self.expiry_time_start = m.get('ExpiryTimeStart')
        if m.get('EffectiveOrNot') is not None:
            self.effective_or_not = m.get('EffectiveOrNot')
        return self


class QueryPrepaidCardsResponseBodyDataPrepaidCard(TeaModel):
    def __init__(
        self,
        prepaid_card_id: int = None,
        prepaid_card_no: str = None,
        granted_time: str = None,
        effective_time: str = None,
        expiry_time: str = None,
        applicable_products: str = None,
        applicable_scenarios: str = None,
        nominal_value: str = None,
        balance: str = None,
        status: str = None,
    ):
        self.prepaid_card_id = prepaid_card_id
        self.prepaid_card_no = prepaid_card_no
        self.granted_time = granted_time
        self.effective_time = effective_time
        self.expiry_time = expiry_time
        self.applicable_products = applicable_products
        self.applicable_scenarios = applicable_scenarios
        self.nominal_value = nominal_value
        self.balance = balance
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.prepaid_card_id is not None:
            result['PrepaidCardId'] = self.prepaid_card_id
        if self.prepaid_card_no is not None:
            result['PrepaidCardNo'] = self.prepaid_card_no
        if self.granted_time is not None:
            result['GrantedTime'] = self.granted_time
        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time
        if self.expiry_time is not None:
            result['ExpiryTime'] = self.expiry_time
        if self.applicable_products is not None:
            result['ApplicableProducts'] = self.applicable_products
        if self.applicable_scenarios is not None:
            result['ApplicableScenarios'] = self.applicable_scenarios
        if self.nominal_value is not None:
            result['NominalValue'] = self.nominal_value
        if self.balance is not None:
            result['Balance'] = self.balance
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrepaidCardId') is not None:
            self.prepaid_card_id = m.get('PrepaidCardId')
        if m.get('PrepaidCardNo') is not None:
            self.prepaid_card_no = m.get('PrepaidCardNo')
        if m.get('GrantedTime') is not None:
            self.granted_time = m.get('GrantedTime')
        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')
        if m.get('ExpiryTime') is not None:
            self.expiry_time = m.get('ExpiryTime')
        if m.get('ApplicableProducts') is not None:
            self.applicable_products = m.get('ApplicableProducts')
        if m.get('ApplicableScenarios') is not None:
            self.applicable_scenarios = m.get('ApplicableScenarios')
        if m.get('NominalValue') is not None:
            self.nominal_value = m.get('NominalValue')
        if m.get('Balance') is not None:
            self.balance = m.get('Balance')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryPrepaidCardsResponseBodyData(TeaModel):
    def __init__(
        self,
        prepaid_card: List[QueryPrepaidCardsResponseBodyDataPrepaidCard] = None,
    ):
        self.prepaid_card = prepaid_card

    def validate(self):
        if self.prepaid_card:
            for k in self.prepaid_card:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['PrepaidCard'] = []
        if self.prepaid_card is not None:
            for k in self.prepaid_card:
                result['PrepaidCard'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.prepaid_card = []
        if m.get('PrepaidCard') is not None:
            for k in m.get('PrepaidCard'):
                temp_model = QueryPrepaidCardsResponseBodyDataPrepaidCard()
                self.prepaid_card.append(temp_model.from_map(k))
        return self


class QueryPrepaidCardsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        data: QueryPrepaidCardsResponseBodyData = None,
    ):
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = QueryPrepaidCardsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryPrepaidCardsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryPrepaidCardsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = QueryPrepaidCardsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryProductListRequest(TeaModel):
    def __init__(
        self,
        query_total_count: bool = None,
        page_num: int = None,
        page_size: int = None,
    ):
        self.query_total_count = query_total_count
        self.page_num = page_num
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.query_total_count is not None:
            result['QueryTotalCount'] = self.query_total_count
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QueryTotalCount') is not None:
            self.query_total_count = m.get('QueryTotalCount')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryProductListResponseBodyDataProductListProduct(TeaModel):
    def __init__(
        self,
        product_code: str = None,
        product_name: str = None,
        product_type: str = None,
        subscription_type: str = None,
    ):
        self.product_code = product_code
        self.product_name = product_name
        self.product_type = product_type
        self.subscription_type = subscription_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        return self


class QueryProductListResponseBodyDataProductList(TeaModel):
    def __init__(
        self,
        product: List[QueryProductListResponseBodyDataProductListProduct] = None,
    ):
        self.product = product

    def validate(self):
        if self.product:
            for k in self.product:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Product'] = []
        if self.product is not None:
            for k in self.product:
                result['Product'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.product = []
        if m.get('Product') is not None:
            for k in m.get('Product'):
                temp_model = QueryProductListResponseBodyDataProductListProduct()
                self.product.append(temp_model.from_map(k))
        return self


class QueryProductListResponseBodyData(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_num: int = None,
        page_size: int = None,
        product_list: QueryProductListResponseBodyDataProductList = None,
    ):
        self.total_count = total_count
        self.page_num = page_num
        self.page_size = page_size
        self.product_list = product_list

    def validate(self):
        if self.product_list:
            self.product_list.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_list is not None:
            result['ProductList'] = self.product_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductList') is not None:
            temp_model = QueryProductListResponseBodyDataProductList()
            self.product_list = temp_model.from_map(m['ProductList'])
        return self


class QueryProductListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        data: QueryProductListResponseBodyData = None,
    ):
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = QueryProductListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryProductListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryProductListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = QueryProductListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRedeemRequest(TeaModel):
    def __init__(
        self,
        expiry_time_start: str = None,
        expiry_time_end: str = None,
        effective_or_not: bool = None,
        page_num: int = None,
        page_size: int = None,
    ):
        self.expiry_time_start = expiry_time_start
        self.expiry_time_end = expiry_time_end
        self.effective_or_not = effective_or_not
        self.page_num = page_num
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.expiry_time_start is not None:
            result['ExpiryTimeStart'] = self.expiry_time_start
        if self.expiry_time_end is not None:
            result['ExpiryTimeEnd'] = self.expiry_time_end
        if self.effective_or_not is not None:
            result['EffectiveOrNot'] = self.effective_or_not
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpiryTimeStart') is not None:
            self.expiry_time_start = m.get('ExpiryTimeStart')
        if m.get('ExpiryTimeEnd') is not None:
            self.expiry_time_end = m.get('ExpiryTimeEnd')
        if m.get('EffectiveOrNot') is not None:
            self.effective_or_not = m.get('EffectiveOrNot')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryRedeemResponseBodyDataRedeemRedeem(TeaModel):
    def __init__(
        self,
        redeem_id: str = None,
        redeem_no: str = None,
        status: str = None,
        granted_time: str = None,
        effective_time: str = None,
        expiry_time: str = None,
        nominal_value: str = None,
        balance: str = None,
        applicable_products: str = None,
        specification: str = None,
    ):
        self.redeem_id = redeem_id
        self.redeem_no = redeem_no
        self.status = status
        self.granted_time = granted_time
        self.effective_time = effective_time
        self.expiry_time = expiry_time
        self.nominal_value = nominal_value
        self.balance = balance
        self.applicable_products = applicable_products
        self.specification = specification

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.redeem_id is not None:
            result['RedeemId'] = self.redeem_id
        if self.redeem_no is not None:
            result['RedeemNo'] = self.redeem_no
        if self.status is not None:
            result['Status'] = self.status
        if self.granted_time is not None:
            result['GrantedTime'] = self.granted_time
        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time
        if self.expiry_time is not None:
            result['ExpiryTime'] = self.expiry_time
        if self.nominal_value is not None:
            result['NominalValue'] = self.nominal_value
        if self.balance is not None:
            result['Balance'] = self.balance
        if self.applicable_products is not None:
            result['ApplicableProducts'] = self.applicable_products
        if self.specification is not None:
            result['Specification'] = self.specification
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RedeemId') is not None:
            self.redeem_id = m.get('RedeemId')
        if m.get('RedeemNo') is not None:
            self.redeem_no = m.get('RedeemNo')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('GrantedTime') is not None:
            self.granted_time = m.get('GrantedTime')
        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')
        if m.get('ExpiryTime') is not None:
            self.expiry_time = m.get('ExpiryTime')
        if m.get('NominalValue') is not None:
            self.nominal_value = m.get('NominalValue')
        if m.get('Balance') is not None:
            self.balance = m.get('Balance')
        if m.get('ApplicableProducts') is not None:
            self.applicable_products = m.get('ApplicableProducts')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        return self


class QueryRedeemResponseBodyDataRedeem(TeaModel):
    def __init__(
        self,
        redeem: List[QueryRedeemResponseBodyDataRedeemRedeem] = None,
    ):
        self.redeem = redeem

    def validate(self):
        if self.redeem:
            for k in self.redeem:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Redeem'] = []
        if self.redeem is not None:
            for k in self.redeem:
                result['Redeem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.redeem = []
        if m.get('Redeem') is not None:
            for k in m.get('Redeem'):
                temp_model = QueryRedeemResponseBodyDataRedeemRedeem()
                self.redeem.append(temp_model.from_map(k))
        return self


class QueryRedeemResponseBodyData(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        total_count: int = None,
        redeem: QueryRedeemResponseBodyDataRedeem = None,
    ):
        self.page_num = page_num
        self.page_size = page_size
        self.total_count = total_count
        self.redeem = redeem

    def validate(self):
        if self.redeem:
            self.redeem.validate()

    def to_map(self):
        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.redeem is not None:
            result['Redeem'] = self.redeem.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Redeem') is not None:
            temp_model = QueryRedeemResponseBodyDataRedeem()
            self.redeem = temp_model.from_map(m['Redeem'])
        return self


class QueryRedeemResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        data: QueryRedeemResponseBodyData = None,
    ):
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = QueryRedeemResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryRedeemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryRedeemResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = QueryRedeemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRelationListRequest(TeaModel):
    def __init__(
        self,
        user_id: int = None,
        status_list: List[str] = None,
        page_num: int = None,
        page_size: int = None,
    ):
        self.user_id = user_id
        self.status_list = status_list
        self.page_num = page_num
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.status_list is not None:
            result['StatusList'] = self.status_list
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryRelationListResponseBodyDataFinancialRelationInfoList(TeaModel):
    def __init__(
        self,
        relation_id: int = None,
        account_type: str = None,
        account_id: int = None,
        account_name: str = None,
        account_nick_name: str = None,
        relation_type: str = None,
        state: str = None,
        setup_time: str = None,
        start_time: str = None,
        end_time: str = None,
    ):
        self.relation_id = relation_id
        self.account_type = account_type
        self.account_id = account_id
        self.account_name = account_name
        self.account_nick_name = account_nick_name
        self.relation_type = relation_type
        self.state = state
        self.setup_time = setup_time
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.relation_id is not None:
            result['RelationId'] = self.relation_id
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_nick_name is not None:
            result['AccountNickName'] = self.account_nick_name
        if self.relation_type is not None:
            result['RelationType'] = self.relation_type
        if self.state is not None:
            result['State'] = self.state
        if self.setup_time is not None:
            result['SetupTime'] = self.setup_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RelationId') is not None:
            self.relation_id = m.get('RelationId')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountNickName') is not None:
            self.account_nick_name = m.get('AccountNickName')
        if m.get('RelationType') is not None:
            self.relation_type = m.get('RelationType')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('SetupTime') is not None:
            self.setup_time = m.get('SetupTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class QueryRelationListResponseBodyData(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        total_count: int = None,
        financial_relation_info_list: List[QueryRelationListResponseBodyDataFinancialRelationInfoList] = None,
    ):
        self.page_num = page_num
        self.page_size = page_size
        self.total_count = total_count
        self.financial_relation_info_list = financial_relation_info_list

    def validate(self):
        if self.financial_relation_info_list:
            for k in self.financial_relation_info_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['FinancialRelationInfoList'] = []
        if self.financial_relation_info_list is not None:
            for k in self.financial_relation_info_list:
                result['FinancialRelationInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.financial_relation_info_list = []
        if m.get('FinancialRelationInfoList') is not None:
            for k in m.get('FinancialRelationInfoList'):
                temp_model = QueryRelationListResponseBodyDataFinancialRelationInfoList()
                self.financial_relation_info_list.append(temp_model.from_map(k))
        return self


class QueryRelationListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        request_id: str = None,
        success: bool = None,
        message: str = None,
        data: QueryRelationListResponseBodyData = None,
    ):
        self.code = code
        self.request_id = request_id
        self.success = success
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = QueryRelationListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryRelationListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryRelationListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = QueryRelationListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryResellerAvailableQuotaRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        item_codes: str = None,
    ):
        self.owner_id = owner_id
        self.item_codes = item_codes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.item_codes is not None:
            result['ItemCodes'] = self.item_codes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ItemCodes') is not None:
            self.item_codes = m.get('ItemCodes')
        return self


class QueryResellerAvailableQuotaResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
        success: bool = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.message = message
        self.success = success
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class QueryResellerAvailableQuotaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryResellerAvailableQuotaResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = QueryResellerAvailableQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryResourcePackageInstancesRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        product_code: str = None,
        expiry_time_start: str = None,
        expiry_time_end: str = None,
        page_num: int = None,
        page_size: int = None,
    ):
        self.owner_id = owner_id
        self.product_code = product_code
        self.expiry_time_start = expiry_time_start
        self.expiry_time_end = expiry_time_end
        self.page_num = page_num
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.expiry_time_start is not None:
            result['ExpiryTimeStart'] = self.expiry_time_start
        if self.expiry_time_end is not None:
            result['ExpiryTimeEnd'] = self.expiry_time_end
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ExpiryTimeStart') is not None:
            self.expiry_time_start = m.get('ExpiryTimeStart')
        if m.get('ExpiryTimeEnd') is not None:
            self.expiry_time_end = m.get('ExpiryTimeEnd')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryResourcePackageInstancesResponseBodyDataInstancesInstanceApplicableProducts(TeaModel):
    def __init__(
        self,
        product: List[str] = None,
    ):
        self.product = product

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.product is not None:
            result['Product'] = self.product
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Product') is not None:
            self.product = m.get('Product')
        return self


class QueryResourcePackageInstancesResponseBodyDataInstancesInstance(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region: str = None,
        total_amount: str = None,
        total_amount_unit: str = None,
        remaining_amount: str = None,
        remaining_amount_unit: str = None,
        effective_time: str = None,
        expiry_time: str = None,
        remark: str = None,
        package_type: str = None,
        status: str = None,
        deduct_type: str = None,
        applicable_products: QueryResourcePackageInstancesResponseBodyDataInstancesInstanceApplicableProducts = None,
    ):
        self.instance_id = instance_id
        self.region = region
        self.total_amount = total_amount
        self.total_amount_unit = total_amount_unit
        self.remaining_amount = remaining_amount
        self.remaining_amount_unit = remaining_amount_unit
        self.effective_time = effective_time
        self.expiry_time = expiry_time
        self.remark = remark
        self.package_type = package_type
        self.status = status
        self.deduct_type = deduct_type
        self.applicable_products = applicable_products

    def validate(self):
        if self.applicable_products:
            self.applicable_products.validate()

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region is not None:
            result['Region'] = self.region
        if self.total_amount is not None:
            result['TotalAmount'] = self.total_amount
        if self.total_amount_unit is not None:
            result['TotalAmountUnit'] = self.total_amount_unit
        if self.remaining_amount is not None:
            result['RemainingAmount'] = self.remaining_amount
        if self.remaining_amount_unit is not None:
            result['RemainingAmountUnit'] = self.remaining_amount_unit
        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time
        if self.expiry_time is not None:
            result['ExpiryTime'] = self.expiry_time
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.status is not None:
            result['Status'] = self.status
        if self.deduct_type is not None:
            result['DeductType'] = self.deduct_type
        if self.applicable_products is not None:
            result['ApplicableProducts'] = self.applicable_products.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('TotalAmount') is not None:
            self.total_amount = m.get('TotalAmount')
        if m.get('TotalAmountUnit') is not None:
            self.total_amount_unit = m.get('TotalAmountUnit')
        if m.get('RemainingAmount') is not None:
            self.remaining_amount = m.get('RemainingAmount')
        if m.get('RemainingAmountUnit') is not None:
            self.remaining_amount_unit = m.get('RemainingAmountUnit')
        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')
        if m.get('ExpiryTime') is not None:
            self.expiry_time = m.get('ExpiryTime')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('DeductType') is not None:
            self.deduct_type = m.get('DeductType')
        if m.get('ApplicableProducts') is not None:
            temp_model = QueryResourcePackageInstancesResponseBodyDataInstancesInstanceApplicableProducts()
            self.applicable_products = temp_model.from_map(m['ApplicableProducts'])
        return self


class QueryResourcePackageInstancesResponseBodyDataInstances(TeaModel):
    def __init__(
        self,
        instance: List[QueryResourcePackageInstancesResponseBodyDataInstancesInstance] = None,
    ):
        self.instance = instance

    def validate(self):
        if self.instance:
            for k in self.instance:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Instance'] = []
        if self.instance is not None:
            for k in self.instance:
                result['Instance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance = []
        if m.get('Instance') is not None:
            for k in m.get('Instance'):
                temp_model = QueryResourcePackageInstancesResponseBodyDataInstancesInstance()
                self.instance.append(temp_model.from_map(k))
        return self


class QueryResourcePackageInstancesResponseBodyData(TeaModel):
    def __init__(
        self,
        host_id: str = None,
        page_num: str = None,
        page_size: str = None,
        total_count: str = None,
        instances: QueryResourcePackageInstancesResponseBodyDataInstances = None,
    ):
        self.host_id = host_id
        self.page_num = page_num
        self.page_size = page_size
        self.total_count = total_count
        self.instances = instances

    def validate(self):
        if self.instances:
            self.instances.validate()

    def to_map(self):
        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.instances is not None:
            result['Instances'] = self.instances.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Instances') is not None:
            temp_model = QueryResourcePackageInstancesResponseBodyDataInstances()
            self.instances = temp_model.from_map(m['Instances'])
        return self


class QueryResourcePackageInstancesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        page: int = None,
        page_size: int = None,
        total: int = None,
        data: QueryResourcePackageInstancesResponseBodyData = None,
    ):
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message
        self.page = page
        self.page_size = page_size
        self.total = total
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('Data') is not None:
            temp_model = QueryResourcePackageInstancesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryResourcePackageInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryResourcePackageInstancesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = QueryResourcePackageInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRIUtilizationDetailRequest(TeaModel):
    def __init__(
        self,
        riinstance_id: str = None,
        instance_spec: str = None,
        ricommodity_code: str = None,
        deducted_instance_id: str = None,
        start_time: str = None,
        end_time: str = None,
        page_num: int = None,
        page_size: int = None,
    ):
        self.riinstance_id = riinstance_id
        self.instance_spec = instance_spec
        self.ricommodity_code = ricommodity_code
        self.deducted_instance_id = deducted_instance_id
        self.start_time = start_time
        self.end_time = end_time
        self.page_num = page_num
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.riinstance_id is not None:
            result['RIInstanceId'] = self.riinstance_id
        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec
        if self.ricommodity_code is not None:
            result['RICommodityCode'] = self.ricommodity_code
        if self.deducted_instance_id is not None:
            result['DeductedInstanceId'] = self.deducted_instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RIInstanceId') is not None:
            self.riinstance_id = m.get('RIInstanceId')
        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')
        if m.get('RICommodityCode') is not None:
            self.ricommodity_code = m.get('RICommodityCode')
        if m.get('DeductedInstanceId') is not None:
            self.deducted_instance_id = m.get('DeductedInstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryRIUtilizationDetailResponseBodyDataDetailListDetailList(TeaModel):
    def __init__(
        self,
        riinstance_id: str = None,
        instance_spec: str = None,
        deducted_instance_id: str = None,
        deducted_commodity_code: str = None,
        deduct_date: str = None,
        deduct_hours: str = None,
        deducted_product_detail: str = None,
        deduct_quantity: float = None,
        deduct_factor_total: float = None,
    ):
        self.riinstance_id = riinstance_id
        self.instance_spec = instance_spec
        self.deducted_instance_id = deducted_instance_id
        self.deducted_commodity_code = deducted_commodity_code
        self.deduct_date = deduct_date
        self.deduct_hours = deduct_hours
        self.deducted_product_detail = deducted_product_detail
        self.deduct_quantity = deduct_quantity
        self.deduct_factor_total = deduct_factor_total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.riinstance_id is not None:
            result['RIInstanceId'] = self.riinstance_id
        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec
        if self.deducted_instance_id is not None:
            result['DeductedInstanceId'] = self.deducted_instance_id
        if self.deducted_commodity_code is not None:
            result['DeductedCommodityCode'] = self.deducted_commodity_code
        if self.deduct_date is not None:
            result['DeductDate'] = self.deduct_date
        if self.deduct_hours is not None:
            result['DeductHours'] = self.deduct_hours
        if self.deducted_product_detail is not None:
            result['DeductedProductDetail'] = self.deducted_product_detail
        if self.deduct_quantity is not None:
            result['DeductQuantity'] = self.deduct_quantity
        if self.deduct_factor_total is not None:
            result['DeductFactorTotal'] = self.deduct_factor_total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RIInstanceId') is not None:
            self.riinstance_id = m.get('RIInstanceId')
        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')
        if m.get('DeductedInstanceId') is not None:
            self.deducted_instance_id = m.get('DeductedInstanceId')
        if m.get('DeductedCommodityCode') is not None:
            self.deducted_commodity_code = m.get('DeductedCommodityCode')
        if m.get('DeductDate') is not None:
            self.deduct_date = m.get('DeductDate')
        if m.get('DeductHours') is not None:
            self.deduct_hours = m.get('DeductHours')
        if m.get('DeductedProductDetail') is not None:
            self.deducted_product_detail = m.get('DeductedProductDetail')
        if m.get('DeductQuantity') is not None:
            self.deduct_quantity = m.get('DeductQuantity')
        if m.get('DeductFactorTotal') is not None:
            self.deduct_factor_total = m.get('DeductFactorTotal')
        return self


class QueryRIUtilizationDetailResponseBodyDataDetailList(TeaModel):
    def __init__(
        self,
        detail_list: List[QueryRIUtilizationDetailResponseBodyDataDetailListDetailList] = None,
    ):
        self.detail_list = detail_list

    def validate(self):
        if self.detail_list:
            for k in self.detail_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['DetailList'] = []
        if self.detail_list is not None:
            for k in self.detail_list:
                result['DetailList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detail_list = []
        if m.get('DetailList') is not None:
            for k in m.get('DetailList'):
                temp_model = QueryRIUtilizationDetailResponseBodyDataDetailListDetailList()
                self.detail_list.append(temp_model.from_map(k))
        return self


class QueryRIUtilizationDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        total_count: int = None,
        detail_list: QueryRIUtilizationDetailResponseBodyDataDetailList = None,
    ):
        self.page_num = page_num
        self.page_size = page_size
        self.total_count = total_count
        self.detail_list = detail_list

    def validate(self):
        if self.detail_list:
            self.detail_list.validate()

    def to_map(self):
        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.detail_list is not None:
            result['DetailList'] = self.detail_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('DetailList') is not None:
            temp_model = QueryRIUtilizationDetailResponseBodyDataDetailList()
            self.detail_list = temp_model.from_map(m['DetailList'])
        return self


class QueryRIUtilizationDetailResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        data: QueryRIUtilizationDetailResponseBodyData = None,
    ):
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = QueryRIUtilizationDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryRIUtilizationDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryRIUtilizationDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = QueryRIUtilizationDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySavingsPlansDeductLogRequest(TeaModel):
    def __init__(
        self,
        instance_type: str = None,
        page_size: int = None,
        locale: str = None,
        page_num: int = None,
        instance_id: str = None,
        start_time: str = None,
        end_time: str = None,
    ):
        self.instance_type = instance_type
        self.page_size = page_size
        self.locale = locale
        self.page_num = page_num
        self.instance_id = instance_id
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.locale is not None:
            result['Locale'] = self.locale
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Locale') is not None:
            self.locale = m.get('Locale')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class QuerySavingsPlansDeductLogResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        start_time: str = None,
        end_time: str = None,
        savings_type: str = None,
        bill_module: str = None,
        deduct_fee: str = None,
        deduct_rate: str = None,
        user_id: int = None,
        deduct_commodity: str = None,
        deduct_instance_id: str = None,
        discount_rate: str = None,
    ):
        self.instance_id = instance_id
        self.start_time = start_time
        self.end_time = end_time
        self.savings_type = savings_type
        self.bill_module = bill_module
        self.deduct_fee = deduct_fee
        self.deduct_rate = deduct_rate
        self.user_id = user_id
        self.deduct_commodity = deduct_commodity
        self.deduct_instance_id = deduct_instance_id
        self.discount_rate = discount_rate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.savings_type is not None:
            result['SavingsType'] = self.savings_type
        if self.bill_module is not None:
            result['BillModule'] = self.bill_module
        if self.deduct_fee is not None:
            result['DeductFee'] = self.deduct_fee
        if self.deduct_rate is not None:
            result['DeductRate'] = self.deduct_rate
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.deduct_commodity is not None:
            result['DeductCommodity'] = self.deduct_commodity
        if self.deduct_instance_id is not None:
            result['DeductInstanceId'] = self.deduct_instance_id
        if self.discount_rate is not None:
            result['DiscountRate'] = self.discount_rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('SavingsType') is not None:
            self.savings_type = m.get('SavingsType')
        if m.get('BillModule') is not None:
            self.bill_module = m.get('BillModule')
        if m.get('DeductFee') is not None:
            self.deduct_fee = m.get('DeductFee')
        if m.get('DeductRate') is not None:
            self.deduct_rate = m.get('DeductRate')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('DeductCommodity') is not None:
            self.deduct_commodity = m.get('DeductCommodity')
        if m.get('DeductInstanceId') is not None:
            self.deduct_instance_id = m.get('DeductInstanceId')
        if m.get('DiscountRate') is not None:
            self.discount_rate = m.get('DiscountRate')
        return self


class QuerySavingsPlansDeductLogResponseBodyData(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        total_count: int = None,
        items: List[QuerySavingsPlansDeductLogResponseBodyDataItems] = None,
    ):
        self.page_num = page_num
        self.page_size = page_size
        self.total_count = total_count
        self.items = items

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = QuerySavingsPlansDeductLogResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        return self


class QuerySavingsPlansDeductLogResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        request_id: str = None,
        success: bool = None,
        message: str = None,
        data: QuerySavingsPlansDeductLogResponseBodyData = None,
    ):
        self.code = code
        self.request_id = request_id
        self.success = success
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = QuerySavingsPlansDeductLogResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QuerySavingsPlansDeductLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QuerySavingsPlansDeductLogResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = QuerySavingsPlansDeductLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySavingsPlansInstanceRequest(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        locale: str = None,
        page_num: int = None,
        instance_id: str = None,
        start_time: str = None,
        end_time: str = None,
    ):
        self.page_size = page_size
        self.locale = locale
        self.page_num = page_num
        self.instance_id = instance_id
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.locale is not None:
            result['Locale'] = self.locale
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Locale') is not None:
            self.locale = m.get('Locale')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class QuerySavingsPlansInstanceResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        savings_type: str = None,
        instance_family: str = None,
        region: str = None,
        pool_value: str = None,
        currency: str = None,
        status: str = None,
        start_time: str = None,
        end_time: str = None,
        pay_mode: str = None,
        prepay_fee: str = None,
        total_save: str = None,
        utilization: str = None,
        share: bool = None,
    ):
        self.instance_id = instance_id
        self.savings_type = savings_type
        self.instance_family = instance_family
        self.region = region
        self.pool_value = pool_value
        self.currency = currency
        self.status = status
        self.start_time = start_time
        self.end_time = end_time
        self.pay_mode = pay_mode
        self.prepay_fee = prepay_fee
        self.total_save = total_save
        self.utilization = utilization
        self.share = share

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.savings_type is not None:
            result['SavingsType'] = self.savings_type
        if self.instance_family is not None:
            result['InstanceFamily'] = self.instance_family
        if self.region is not None:
            result['Region'] = self.region
        if self.pool_value is not None:
            result['PoolValue'] = self.pool_value
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.status is not None:
            result['Status'] = self.status
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.pay_mode is not None:
            result['PayMode'] = self.pay_mode
        if self.prepay_fee is not None:
            result['PrepayFee'] = self.prepay_fee
        if self.total_save is not None:
            result['TotalSave'] = self.total_save
        if self.utilization is not None:
            result['Utilization'] = self.utilization
        if self.share is not None:
            result['Share'] = self.share
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SavingsType') is not None:
            self.savings_type = m.get('SavingsType')
        if m.get('InstanceFamily') is not None:
            self.instance_family = m.get('InstanceFamily')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('PoolValue') is not None:
            self.pool_value = m.get('PoolValue')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PayMode') is not None:
            self.pay_mode = m.get('PayMode')
        if m.get('PrepayFee') is not None:
            self.prepay_fee = m.get('PrepayFee')
        if m.get('TotalSave') is not None:
            self.total_save = m.get('TotalSave')
        if m.get('Utilization') is not None:
            self.utilization = m.get('Utilization')
        if m.get('Share') is not None:
            self.share = m.get('Share')
        return self


class QuerySavingsPlansInstanceResponseBodyData(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        total_count: int = None,
        items: List[QuerySavingsPlansInstanceResponseBodyDataItems] = None,
    ):
        self.page_num = page_num
        self.page_size = page_size
        self.total_count = total_count
        self.items = items

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = QuerySavingsPlansInstanceResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        return self


class QuerySavingsPlansInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        request_id: str = None,
        success: bool = None,
        message: str = None,
        data: QuerySavingsPlansInstanceResponseBodyData = None,
    ):
        self.code = code
        self.request_id = request_id
        self.success = success
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = QuerySavingsPlansInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QuerySavingsPlansInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QuerySavingsPlansInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = QuerySavingsPlansInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySettleBillRequest(TeaModel):
    def __init__(
        self,
        billing_cycle: str = None,
        type: str = None,
        product_code: str = None,
        product_type: str = None,
        subscription_type: str = None,
        is_hide_zero_charge: bool = None,
        is_display_local_currency: bool = None,
        owner_id: int = None,
        next_token: str = None,
        max_results: int = None,
        bill_owner_id: int = None,
    ):
        self.billing_cycle = billing_cycle
        self.type = type
        self.product_code = product_code
        self.product_type = product_type
        self.subscription_type = subscription_type
        self.is_hide_zero_charge = is_hide_zero_charge
        self.is_display_local_currency = is_display_local_currency
        self.owner_id = owner_id
        self.next_token = next_token
        self.max_results = max_results
        self.bill_owner_id = bill_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle
        if self.type is not None:
            result['Type'] = self.type
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.is_hide_zero_charge is not None:
            result['IsHideZeroCharge'] = self.is_hide_zero_charge
        if self.is_display_local_currency is not None:
            result['IsDisplayLocalCurrency'] = self.is_display_local_currency
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.bill_owner_id is not None:
            result['BillOwnerId'] = self.bill_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('IsHideZeroCharge') is not None:
            self.is_hide_zero_charge = m.get('IsHideZeroCharge')
        if m.get('IsDisplayLocalCurrency') is not None:
            self.is_display_local_currency = m.get('IsDisplayLocalCurrency')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('BillOwnerId') is not None:
            self.bill_owner_id = m.get('BillOwnerId')
        return self


class QuerySettleBillResponseBodyDataItemsItem(TeaModel):
    def __init__(
        self,
        record_id: str = None,
        item: str = None,
        owner_id: str = None,
        usage_start_time: str = None,
        usage_end_time: str = None,
        payment_time: str = None,
        product_code: str = None,
        product_type: str = None,
        subscription_type: str = None,
        product_name: str = None,
        product_detail: str = None,
        pretax_gross_amount: float = None,
        deducted_by_coupons: float = None,
        invoice_discount: float = None,
        pretax_amount: float = None,
        currency: str = None,
        pretax_amount_local: float = None,
        tax: float = None,
        payment_amount: float = None,
        deducted_by_cash_coupons: float = None,
        deducted_by_prepaid_card: float = None,
        outstanding_amount: float = None,
        after_tax_amount: float = None,
        status: str = None,
        payment_currency: str = None,
        payment_transaction_id: str = None,
        round_down_discount: str = None,
        sub_order_id: str = None,
        pip_code: str = None,
        commodity_code: str = None,
    ):
        self.record_id = record_id
        self.item = item
        self.owner_id = owner_id
        self.usage_start_time = usage_start_time
        self.usage_end_time = usage_end_time
        self.payment_time = payment_time
        self.product_code = product_code
        self.product_type = product_type
        self.subscription_type = subscription_type
        self.product_name = product_name
        self.product_detail = product_detail
        self.pretax_gross_amount = pretax_gross_amount
        self.deducted_by_coupons = deducted_by_coupons
        self.invoice_discount = invoice_discount
        self.pretax_amount = pretax_amount
        self.currency = currency
        self.pretax_amount_local = pretax_amount_local
        self.tax = tax
        self.payment_amount = payment_amount
        self.deducted_by_cash_coupons = deducted_by_cash_coupons
        self.deducted_by_prepaid_card = deducted_by_prepaid_card
        self.outstanding_amount = outstanding_amount
        self.after_tax_amount = after_tax_amount
        self.status = status
        self.payment_currency = payment_currency
        self.payment_transaction_id = payment_transaction_id
        self.round_down_discount = round_down_discount
        self.sub_order_id = sub_order_id
        self.pip_code = pip_code
        self.commodity_code = commodity_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.record_id is not None:
            result['RecordID'] = self.record_id
        if self.item is not None:
            result['Item'] = self.item
        if self.owner_id is not None:
            result['OwnerID'] = self.owner_id
        if self.usage_start_time is not None:
            result['UsageStartTime'] = self.usage_start_time
        if self.usage_end_time is not None:
            result['UsageEndTime'] = self.usage_end_time
        if self.payment_time is not None:
            result['PaymentTime'] = self.payment_time
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.product_detail is not None:
            result['ProductDetail'] = self.product_detail
        if self.pretax_gross_amount is not None:
            result['PretaxGrossAmount'] = self.pretax_gross_amount
        if self.deducted_by_coupons is not None:
            result['DeductedByCoupons'] = self.deducted_by_coupons
        if self.invoice_discount is not None:
            result['InvoiceDiscount'] = self.invoice_discount
        if self.pretax_amount is not None:
            result['PretaxAmount'] = self.pretax_amount
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.pretax_amount_local is not None:
            result['PretaxAmountLocal'] = self.pretax_amount_local
        if self.tax is not None:
            result['Tax'] = self.tax
        if self.payment_amount is not None:
            result['PaymentAmount'] = self.payment_amount
        if self.deducted_by_cash_coupons is not None:
            result['DeductedByCashCoupons'] = self.deducted_by_cash_coupons
        if self.deducted_by_prepaid_card is not None:
            result['DeductedByPrepaidCard'] = self.deducted_by_prepaid_card
        if self.outstanding_amount is not None:
            result['OutstandingAmount'] = self.outstanding_amount
        if self.after_tax_amount is not None:
            result['AfterTaxAmount'] = self.after_tax_amount
        if self.status is not None:
            result['Status'] = self.status
        if self.payment_currency is not None:
            result['PaymentCurrency'] = self.payment_currency
        if self.payment_transaction_id is not None:
            result['PaymentTransactionID'] = self.payment_transaction_id
        if self.round_down_discount is not None:
            result['RoundDownDiscount'] = self.round_down_discount
        if self.sub_order_id is not None:
            result['SubOrderId'] = self.sub_order_id
        if self.pip_code is not None:
            result['PipCode'] = self.pip_code
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordID') is not None:
            self.record_id = m.get('RecordID')
        if m.get('Item') is not None:
            self.item = m.get('Item')
        if m.get('OwnerID') is not None:
            self.owner_id = m.get('OwnerID')
        if m.get('UsageStartTime') is not None:
            self.usage_start_time = m.get('UsageStartTime')
        if m.get('UsageEndTime') is not None:
            self.usage_end_time = m.get('UsageEndTime')
        if m.get('PaymentTime') is not None:
            self.payment_time = m.get('PaymentTime')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProductDetail') is not None:
            self.product_detail = m.get('ProductDetail')
        if m.get('PretaxGrossAmount') is not None:
            self.pretax_gross_amount = m.get('PretaxGrossAmount')
        if m.get('DeductedByCoupons') is not None:
            self.deducted_by_coupons = m.get('DeductedByCoupons')
        if m.get('InvoiceDiscount') is not None:
            self.invoice_discount = m.get('InvoiceDiscount')
        if m.get('PretaxAmount') is not None:
            self.pretax_amount = m.get('PretaxAmount')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('PretaxAmountLocal') is not None:
            self.pretax_amount_local = m.get('PretaxAmountLocal')
        if m.get('Tax') is not None:
            self.tax = m.get('Tax')
        if m.get('PaymentAmount') is not None:
            self.payment_amount = m.get('PaymentAmount')
        if m.get('DeductedByCashCoupons') is not None:
            self.deducted_by_cash_coupons = m.get('DeductedByCashCoupons')
        if m.get('DeductedByPrepaidCard') is not None:
            self.deducted_by_prepaid_card = m.get('DeductedByPrepaidCard')
        if m.get('OutstandingAmount') is not None:
            self.outstanding_amount = m.get('OutstandingAmount')
        if m.get('AfterTaxAmount') is not None:
            self.after_tax_amount = m.get('AfterTaxAmount')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PaymentCurrency') is not None:
            self.payment_currency = m.get('PaymentCurrency')
        if m.get('PaymentTransactionID') is not None:
            self.payment_transaction_id = m.get('PaymentTransactionID')
        if m.get('RoundDownDiscount') is not None:
            self.round_down_discount = m.get('RoundDownDiscount')
        if m.get('SubOrderId') is not None:
            self.sub_order_id = m.get('SubOrderId')
        if m.get('PipCode') is not None:
            self.pip_code = m.get('PipCode')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        return self


class QuerySettleBillResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        item: List[QuerySettleBillResponseBodyDataItemsItem] = None,
    ):
        self.item = item

    def validate(self):
        if self.item:
            for k in self.item:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Item'] = []
        if self.item is not None:
            for k in self.item:
                result['Item'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.item = []
        if m.get('Item') is not None:
            for k in m.get('Item'):
                temp_model = QuerySettleBillResponseBodyDataItemsItem()
                self.item.append(temp_model.from_map(k))
        return self


class QuerySettleBillResponseBodyData(TeaModel):
    def __init__(
        self,
        billing_cycle: str = None,
        account_id: str = None,
        account_name: str = None,
        next_token: str = None,
        max_results: int = None,
        total_count: int = None,
        items: QuerySettleBillResponseBodyDataItems = None,
    ):
        self.billing_cycle = billing_cycle
        self.account_id = account_id
        self.account_name = account_name
        self.next_token = next_token
        self.max_results = max_results
        self.total_count = total_count
        self.items = items

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle
        if self.account_id is not None:
            result['AccountID'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.items is not None:
            result['Items'] = self.items.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')
        if m.get('AccountID') is not None:
            self.account_id = m.get('AccountID')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Items') is not None:
            temp_model = QuerySettleBillResponseBodyDataItems()
            self.items = temp_model.from_map(m['Items'])
        return self


class QuerySettleBillResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        data: QuerySettleBillResponseBodyData = None,
    ):
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = QuerySettleBillResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QuerySettleBillResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QuerySettleBillResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = QuerySettleBillResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySettlementBillRequest(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        owner_id: int = None,
        page_num: int = None,
        billing_cycle: str = None,
        start_time: str = None,
        end_time: str = None,
        type: str = None,
        product_code: str = None,
        product_type: str = None,
        subscription_type: str = None,
        is_hide_zero_charge: bool = None,
    ):
        self.page_size = page_size
        self.owner_id = owner_id
        self.page_num = page_num
        self.billing_cycle = billing_cycle
        self.start_time = start_time
        self.end_time = end_time
        self.type = type
        self.product_code = product_code
        self.product_type = product_type
        self.subscription_type = subscription_type
        self.is_hide_zero_charge = is_hide_zero_charge

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.type is not None:
            result['Type'] = self.type
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.is_hide_zero_charge is not None:
            result['IsHideZeroCharge'] = self.is_hide_zero_charge
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('IsHideZeroCharge') is not None:
            self.is_hide_zero_charge = m.get('IsHideZeroCharge')
        return self


class QuerySettlementBillResponseBodyDataItemsItem(TeaModel):
    def __init__(
        self,
        record_id: str = None,
        item: str = None,
        payer_account: str = None,
        owner_id: str = None,
        create_time: str = None,
        usage_start_time: str = None,
        usage_end_time: str = None,
        suborder_id: str = None,
        order_id: str = None,
        order_type: str = None,
        linked_customer_order_id: str = None,
        original_order_id: str = None,
        payment_time: str = None,
        solution_id: str = None,
        solution_name: str = None,
        bill_id: str = None,
        product_code: str = None,
        product_type: str = None,
        subscription_type: str = None,
        region: str = None,
        config: str = None,
        quantity: str = None,
        pretax_gross_amount: float = None,
        charge_discount: float = None,
        deducted_by_coupons: float = None,
        account_discount: float = None,
        promotion: str = None,
        pretax_amount: float = None,
        currency: str = None,
        pretax_amount_local: float = None,
        previous_billing_cycle_balance: float = None,
        tax: float = None,
        after_tax_amount: float = None,
        status: str = None,
        cleared_time: str = None,
        outstanding_amount: float = None,
        deducted_by_cash_coupons: float = None,
        deducted_by_prepaid_card: float = None,
        mybank_payment_amount: float = None,
        payment_amount: float = None,
        payment_currency: str = None,
        seller: str = None,
        invoice_no: str = None,
    ):
        self.record_id = record_id
        self.item = item
        self.payer_account = payer_account
        self.owner_id = owner_id
        self.create_time = create_time
        self.usage_start_time = usage_start_time
        self.usage_end_time = usage_end_time
        self.suborder_id = suborder_id
        self.order_id = order_id
        self.order_type = order_type
        self.linked_customer_order_id = linked_customer_order_id
        self.original_order_id = original_order_id
        self.payment_time = payment_time
        self.solution_id = solution_id
        self.solution_name = solution_name
        self.bill_id = bill_id
        self.product_code = product_code
        self.product_type = product_type
        self.subscription_type = subscription_type
        self.region = region
        self.config = config
        self.quantity = quantity
        self.pretax_gross_amount = pretax_gross_amount
        self.charge_discount = charge_discount
        self.deducted_by_coupons = deducted_by_coupons
        self.account_discount = account_discount
        self.promotion = promotion
        self.pretax_amount = pretax_amount
        self.currency = currency
        self.pretax_amount_local = pretax_amount_local
        self.previous_billing_cycle_balance = previous_billing_cycle_balance
        self.tax = tax
        self.after_tax_amount = after_tax_amount
        self.status = status
        self.cleared_time = cleared_time
        self.outstanding_amount = outstanding_amount
        self.deducted_by_cash_coupons = deducted_by_cash_coupons
        self.deducted_by_prepaid_card = deducted_by_prepaid_card
        self.mybank_payment_amount = mybank_payment_amount
        self.payment_amount = payment_amount
        self.payment_currency = payment_currency
        self.seller = seller
        self.invoice_no = invoice_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.record_id is not None:
            result['RecordID'] = self.record_id
        if self.item is not None:
            result['Item'] = self.item
        if self.payer_account is not None:
            result['PayerAccount'] = self.payer_account
        if self.owner_id is not None:
            result['OwnerID'] = self.owner_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.usage_start_time is not None:
            result['UsageStartTime'] = self.usage_start_time
        if self.usage_end_time is not None:
            result['UsageEndTime'] = self.usage_end_time
        if self.suborder_id is not None:
            result['SuborderID'] = self.suborder_id
        if self.order_id is not None:
            result['OrderID'] = self.order_id
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.linked_customer_order_id is not None:
            result['LinkedCustomerOrderID'] = self.linked_customer_order_id
        if self.original_order_id is not None:
            result['OriginalOrderID'] = self.original_order_id
        if self.payment_time is not None:
            result['PaymentTime'] = self.payment_time
        if self.solution_id is not None:
            result['SolutionID'] = self.solution_id
        if self.solution_name is not None:
            result['SolutionName'] = self.solution_name
        if self.bill_id is not None:
            result['BillID'] = self.bill_id
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.region is not None:
            result['Region'] = self.region
        if self.config is not None:
            result['Config'] = self.config
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.pretax_gross_amount is not None:
            result['PretaxGrossAmount'] = self.pretax_gross_amount
        if self.charge_discount is not None:
            result['ChargeDiscount'] = self.charge_discount
        if self.deducted_by_coupons is not None:
            result['DeductedByCoupons'] = self.deducted_by_coupons
        if self.account_discount is not None:
            result['AccountDiscount'] = self.account_discount
        if self.promotion is not None:
            result['Promotion'] = self.promotion
        if self.pretax_amount is not None:
            result['PretaxAmount'] = self.pretax_amount
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.pretax_amount_local is not None:
            result['PretaxAmountLocal'] = self.pretax_amount_local
        if self.previous_billing_cycle_balance is not None:
            result['PreviousBillingCycleBalance'] = self.previous_billing_cycle_balance
        if self.tax is not None:
            result['Tax'] = self.tax
        if self.after_tax_amount is not None:
            result['AfterTaxAmount'] = self.after_tax_amount
        if self.status is not None:
            result['Status'] = self.status
        if self.cleared_time is not None:
            result['ClearedTime'] = self.cleared_time
        if self.outstanding_amount is not None:
            result['OutstandingAmount'] = self.outstanding_amount
        if self.deducted_by_cash_coupons is not None:
            result['DeductedByCashCoupons'] = self.deducted_by_cash_coupons
        if self.deducted_by_prepaid_card is not None:
            result['DeductedByPrepaidCard'] = self.deducted_by_prepaid_card
        if self.mybank_payment_amount is not None:
            result['MybankPaymentAmount'] = self.mybank_payment_amount
        if self.payment_amount is not None:
            result['PaymentAmount'] = self.payment_amount
        if self.payment_currency is not None:
            result['PaymentCurrency'] = self.payment_currency
        if self.seller is not None:
            result['Seller'] = self.seller
        if self.invoice_no is not None:
            result['InvoiceNo'] = self.invoice_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordID') is not None:
            self.record_id = m.get('RecordID')
        if m.get('Item') is not None:
            self.item = m.get('Item')
        if m.get('PayerAccount') is not None:
            self.payer_account = m.get('PayerAccount')
        if m.get('OwnerID') is not None:
            self.owner_id = m.get('OwnerID')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UsageStartTime') is not None:
            self.usage_start_time = m.get('UsageStartTime')
        if m.get('UsageEndTime') is not None:
            self.usage_end_time = m.get('UsageEndTime')
        if m.get('SuborderID') is not None:
            self.suborder_id = m.get('SuborderID')
        if m.get('OrderID') is not None:
            self.order_id = m.get('OrderID')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('LinkedCustomerOrderID') is not None:
            self.linked_customer_order_id = m.get('LinkedCustomerOrderID')
        if m.get('OriginalOrderID') is not None:
            self.original_order_id = m.get('OriginalOrderID')
        if m.get('PaymentTime') is not None:
            self.payment_time = m.get('PaymentTime')
        if m.get('SolutionID') is not None:
            self.solution_id = m.get('SolutionID')
        if m.get('SolutionName') is not None:
            self.solution_name = m.get('SolutionName')
        if m.get('BillID') is not None:
            self.bill_id = m.get('BillID')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('PretaxGrossAmount') is not None:
            self.pretax_gross_amount = m.get('PretaxGrossAmount')
        if m.get('ChargeDiscount') is not None:
            self.charge_discount = m.get('ChargeDiscount')
        if m.get('DeductedByCoupons') is not None:
            self.deducted_by_coupons = m.get('DeductedByCoupons')
        if m.get('AccountDiscount') is not None:
            self.account_discount = m.get('AccountDiscount')
        if m.get('Promotion') is not None:
            self.promotion = m.get('Promotion')
        if m.get('PretaxAmount') is not None:
            self.pretax_amount = m.get('PretaxAmount')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('PretaxAmountLocal') is not None:
            self.pretax_amount_local = m.get('PretaxAmountLocal')
        if m.get('PreviousBillingCycleBalance') is not None:
            self.previous_billing_cycle_balance = m.get('PreviousBillingCycleBalance')
        if m.get('Tax') is not None:
            self.tax = m.get('Tax')
        if m.get('AfterTaxAmount') is not None:
            self.after_tax_amount = m.get('AfterTaxAmount')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ClearedTime') is not None:
            self.cleared_time = m.get('ClearedTime')
        if m.get('OutstandingAmount') is not None:
            self.outstanding_amount = m.get('OutstandingAmount')
        if m.get('DeductedByCashCoupons') is not None:
            self.deducted_by_cash_coupons = m.get('DeductedByCashCoupons')
        if m.get('DeductedByPrepaidCard') is not None:
            self.deducted_by_prepaid_card = m.get('DeductedByPrepaidCard')
        if m.get('MybankPaymentAmount') is not None:
            self.mybank_payment_amount = m.get('MybankPaymentAmount')
        if m.get('PaymentAmount') is not None:
            self.payment_amount = m.get('PaymentAmount')
        if m.get('PaymentCurrency') is not None:
            self.payment_currency = m.get('PaymentCurrency')
        if m.get('Seller') is not None:
            self.seller = m.get('Seller')
        if m.get('InvoiceNo') is not None:
            self.invoice_no = m.get('InvoiceNo')
        return self


class QuerySettlementBillResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        item: List[QuerySettlementBillResponseBodyDataItemsItem] = None,
    ):
        self.item = item

    def validate(self):
        if self.item:
            for k in self.item:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Item'] = []
        if self.item is not None:
            for k in self.item:
                result['Item'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.item = []
        if m.get('Item') is not None:
            for k in m.get('Item'):
                temp_model = QuerySettlementBillResponseBodyDataItemsItem()
                self.item.append(temp_model.from_map(k))
        return self


class QuerySettlementBillResponseBodyData(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        total_count: int = None,
        billing_cycle: str = None,
        items: QuerySettlementBillResponseBodyDataItems = None,
    ):
        self.page_num = page_num
        self.page_size = page_size
        self.total_count = total_count
        self.billing_cycle = billing_cycle
        self.items = items

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle
        if self.items is not None:
            result['Items'] = self.items.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')
        if m.get('Items') is not None:
            temp_model = QuerySettlementBillResponseBodyDataItems()
            self.items = temp_model.from_map(m['Items'])
        return self


class QuerySettlementBillResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        data: QuerySettlementBillResponseBodyData = None,
    ):
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = QuerySettlementBillResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QuerySettlementBillResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QuerySettlementBillResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = QuerySettlementBillResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySplitItemBillRequest(TeaModel):
    def __init__(
        self,
        billing_cycle: str = None,
        product_code: str = None,
        product_type: str = None,
        subscription_type: str = None,
        owner_id: int = None,
        page_num: int = None,
        page_size: int = None,
        bill_owner_id: int = None,
    ):
        self.billing_cycle = billing_cycle
        self.product_code = product_code
        self.product_type = product_type
        self.subscription_type = subscription_type
        self.owner_id = owner_id
        self.page_num = page_num
        self.page_size = page_size
        self.bill_owner_id = bill_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.bill_owner_id is not None:
            result['BillOwnerId'] = self.bill_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('BillOwnerId') is not None:
            self.bill_owner_id = m.get('BillOwnerId')
        return self


class QuerySplitItemBillResponseBodyDataItemsItem(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        billing_type: str = None,
        cost_unit: str = None,
        product_code: str = None,
        product_type: str = None,
        subscription_type: str = None,
        product_name: str = None,
        product_detail: str = None,
        owner_id: str = None,
        billing_item: str = None,
        list_price: str = None,
        list_price_unit: str = None,
        usage: str = None,
        usage_unit: str = None,
        deducted_by_resource_package: str = None,
        pretax_gross_amount: float = None,
        invoice_discount: float = None,
        deducted_by_coupons: float = None,
        pretax_amount: float = None,
        deducted_by_cash_coupons: float = None,
        deducted_by_prepaid_card: float = None,
        payment_amount: float = None,
        outstanding_amount: float = None,
        currency: str = None,
        nick_name: str = None,
        resource_group: str = None,
        tag: str = None,
        instance_config: str = None,
        instance_spec: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        region: str = None,
        zone: str = None,
        item: str = None,
        service_period: str = None,
        billing_date: str = None,
        split_item_id: str = None,
        split_item_name: str = None,
        pip_code: str = None,
        commodity_code: str = None,
        service_period_unit: str = None,
        split_commodity_code: str = None,
        split_product_detail: str = None,
        split_account_id: str = None,
        split_account_name: str = None,
        split_billing_cycle: str = None,
    ):
        self.instance_id = instance_id
        self.billing_type = billing_type
        self.cost_unit = cost_unit
        self.product_code = product_code
        self.product_type = product_type
        self.subscription_type = subscription_type
        self.product_name = product_name
        self.product_detail = product_detail
        self.owner_id = owner_id
        self.billing_item = billing_item
        self.list_price = list_price
        self.list_price_unit = list_price_unit
        self.usage = usage
        self.usage_unit = usage_unit
        self.deducted_by_resource_package = deducted_by_resource_package
        self.pretax_gross_amount = pretax_gross_amount
        self.invoice_discount = invoice_discount
        self.deducted_by_coupons = deducted_by_coupons
        self.pretax_amount = pretax_amount
        self.deducted_by_cash_coupons = deducted_by_cash_coupons
        self.deducted_by_prepaid_card = deducted_by_prepaid_card
        self.payment_amount = payment_amount
        self.outstanding_amount = outstanding_amount
        self.currency = currency
        self.nick_name = nick_name
        self.resource_group = resource_group
        self.tag = tag
        self.instance_config = instance_config
        self.instance_spec = instance_spec
        self.internet_ip = internet_ip
        self.intranet_ip = intranet_ip
        self.region = region
        self.zone = zone
        self.item = item
        self.service_period = service_period
        self.billing_date = billing_date
        self.split_item_id = split_item_id
        self.split_item_name = split_item_name
        self.pip_code = pip_code
        self.commodity_code = commodity_code
        self.service_period_unit = service_period_unit
        self.split_commodity_code = split_commodity_code
        self.split_product_detail = split_product_detail
        self.split_account_id = split_account_id
        self.split_account_name = split_account_name
        self.split_billing_cycle = split_billing_cycle

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id
        if self.billing_type is not None:
            result['BillingType'] = self.billing_type
        if self.cost_unit is not None:
            result['CostUnit'] = self.cost_unit
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.product_detail is not None:
            result['ProductDetail'] = self.product_detail
        if self.owner_id is not None:
            result['OwnerID'] = self.owner_id
        if self.billing_item is not None:
            result['BillingItem'] = self.billing_item
        if self.list_price is not None:
            result['ListPrice'] = self.list_price
        if self.list_price_unit is not None:
            result['ListPriceUnit'] = self.list_price_unit
        if self.usage is not None:
            result['Usage'] = self.usage
        if self.usage_unit is not None:
            result['UsageUnit'] = self.usage_unit
        if self.deducted_by_resource_package is not None:
            result['DeductedByResourcePackage'] = self.deducted_by_resource_package
        if self.pretax_gross_amount is not None:
            result['PretaxGrossAmount'] = self.pretax_gross_amount
        if self.invoice_discount is not None:
            result['InvoiceDiscount'] = self.invoice_discount
        if self.deducted_by_coupons is not None:
            result['DeductedByCoupons'] = self.deducted_by_coupons
        if self.pretax_amount is not None:
            result['PretaxAmount'] = self.pretax_amount
        if self.deducted_by_cash_coupons is not None:
            result['DeductedByCashCoupons'] = self.deducted_by_cash_coupons
        if self.deducted_by_prepaid_card is not None:
            result['DeductedByPrepaidCard'] = self.deducted_by_prepaid_card
        if self.payment_amount is not None:
            result['PaymentAmount'] = self.payment_amount
        if self.outstanding_amount is not None:
            result['OutstandingAmount'] = self.outstanding_amount
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.instance_config is not None:
            result['InstanceConfig'] = self.instance_config
        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec
        if self.internet_ip is not None:
            result['InternetIP'] = self.internet_ip
        if self.intranet_ip is not None:
            result['IntranetIP'] = self.intranet_ip
        if self.region is not None:
            result['Region'] = self.region
        if self.zone is not None:
            result['Zone'] = self.zone
        if self.item is not None:
            result['Item'] = self.item
        if self.service_period is not None:
            result['ServicePeriod'] = self.service_period
        if self.billing_date is not None:
            result['BillingDate'] = self.billing_date
        if self.split_item_id is not None:
            result['SplitItemID'] = self.split_item_id
        if self.split_item_name is not None:
            result['SplitItemName'] = self.split_item_name
        if self.pip_code is not None:
            result['PipCode'] = self.pip_code
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.service_period_unit is not None:
            result['ServicePeriodUnit'] = self.service_period_unit
        if self.split_commodity_code is not None:
            result['SplitCommodityCode'] = self.split_commodity_code
        if self.split_product_detail is not None:
            result['SplitProductDetail'] = self.split_product_detail
        if self.split_account_id is not None:
            result['SplitAccountID'] = self.split_account_id
        if self.split_account_name is not None:
            result['SplitAccountName'] = self.split_account_name
        if self.split_billing_cycle is not None:
            result['SplitBillingCycle'] = self.split_billing_cycle
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')
        if m.get('BillingType') is not None:
            self.billing_type = m.get('BillingType')
        if m.get('CostUnit') is not None:
            self.cost_unit = m.get('CostUnit')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProductDetail') is not None:
            self.product_detail = m.get('ProductDetail')
        if m.get('OwnerID') is not None:
            self.owner_id = m.get('OwnerID')
        if m.get('BillingItem') is not None:
            self.billing_item = m.get('BillingItem')
        if m.get('ListPrice') is not None:
            self.list_price = m.get('ListPrice')
        if m.get('ListPriceUnit') is not None:
            self.list_price_unit = m.get('ListPriceUnit')
        if m.get('Usage') is not None:
            self.usage = m.get('Usage')
        if m.get('UsageUnit') is not None:
            self.usage_unit = m.get('UsageUnit')
        if m.get('DeductedByResourcePackage') is not None:
            self.deducted_by_resource_package = m.get('DeductedByResourcePackage')
        if m.get('PretaxGrossAmount') is not None:
            self.pretax_gross_amount = m.get('PretaxGrossAmount')
        if m.get('InvoiceDiscount') is not None:
            self.invoice_discount = m.get('InvoiceDiscount')
        if m.get('DeductedByCoupons') is not None:
            self.deducted_by_coupons = m.get('DeductedByCoupons')
        if m.get('PretaxAmount') is not None:
            self.pretax_amount = m.get('PretaxAmount')
        if m.get('DeductedByCashCoupons') is not None:
            self.deducted_by_cash_coupons = m.get('DeductedByCashCoupons')
        if m.get('DeductedByPrepaidCard') is not None:
            self.deducted_by_prepaid_card = m.get('DeductedByPrepaidCard')
        if m.get('PaymentAmount') is not None:
            self.payment_amount = m.get('PaymentAmount')
        if m.get('OutstandingAmount') is not None:
            self.outstanding_amount = m.get('OutstandingAmount')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        if m.get('ResourceGroup') is not None:
            self.resource_group = m.get('ResourceGroup')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('InstanceConfig') is not None:
            self.instance_config = m.get('InstanceConfig')
        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')
        if m.get('InternetIP') is not None:
            self.internet_ip = m.get('InternetIP')
        if m.get('IntranetIP') is not None:
            self.intranet_ip = m.get('IntranetIP')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Zone') is not None:
            self.zone = m.get('Zone')
        if m.get('Item') is not None:
            self.item = m.get('Item')
        if m.get('ServicePeriod') is not None:
            self.service_period = m.get('ServicePeriod')
        if m.get('BillingDate') is not None:
            self.billing_date = m.get('BillingDate')
        if m.get('SplitItemID') is not None:
            self.split_item_id = m.get('SplitItemID')
        if m.get('SplitItemName') is not None:
            self.split_item_name = m.get('SplitItemName')
        if m.get('PipCode') is not None:
            self.pip_code = m.get('PipCode')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('ServicePeriodUnit') is not None:
            self.service_period_unit = m.get('ServicePeriodUnit')
        if m.get('SplitCommodityCode') is not None:
            self.split_commodity_code = m.get('SplitCommodityCode')
        if m.get('SplitProductDetail') is not None:
            self.split_product_detail = m.get('SplitProductDetail')
        if m.get('SplitAccountID') is not None:
            self.split_account_id = m.get('SplitAccountID')
        if m.get('SplitAccountName') is not None:
            self.split_account_name = m.get('SplitAccountName')
        if m.get('SplitBillingCycle') is not None:
            self.split_billing_cycle = m.get('SplitBillingCycle')
        return self


class QuerySplitItemBillResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        item: List[QuerySplitItemBillResponseBodyDataItemsItem] = None,
    ):
        self.item = item

    def validate(self):
        if self.item:
            for k in self.item:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Item'] = []
        if self.item is not None:
            for k in self.item:
                result['Item'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.item = []
        if m.get('Item') is not None:
            for k in m.get('Item'):
                temp_model = QuerySplitItemBillResponseBodyDataItemsItem()
                self.item.append(temp_model.from_map(k))
        return self


class QuerySplitItemBillResponseBodyData(TeaModel):
    def __init__(
        self,
        billing_cycle: str = None,
        account_id: str = None,
        account_name: str = None,
        total_count: int = None,
        page_num: int = None,
        page_size: int = None,
        items: QuerySplitItemBillResponseBodyDataItems = None,
    ):
        self.billing_cycle = billing_cycle
        self.account_id = account_id
        self.account_name = account_name
        self.total_count = total_count
        self.page_num = page_num
        self.page_size = page_size
        self.items = items

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle
        if self.account_id is not None:
            result['AccountID'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.items is not None:
            result['Items'] = self.items.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')
        if m.get('AccountID') is not None:
            self.account_id = m.get('AccountID')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Items') is not None:
            temp_model = QuerySplitItemBillResponseBodyDataItems()
            self.items = temp_model.from_map(m['Items'])
        return self


class QuerySplitItemBillResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        data: QuerySplitItemBillResponseBodyData = None,
    ):
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = QuerySplitItemBillResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QuerySplitItemBillResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QuerySplitItemBillResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = QuerySplitItemBillResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryUserOmsDataRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        table: str = None,
        data_type: str = None,
        start_time: str = None,
        end_time: str = None,
        marker: str = None,
        page_size: int = None,
    ):
        self.owner_id = owner_id
        self.table = table
        self.data_type = data_type
        self.start_time = start_time
        self.end_time = end_time
        self.marker = marker
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.table is not None:
            result['Table'] = self.table
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Table') is not None:
            self.table = m.get('Table')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryUserOmsDataResponseBodyData(TeaModel):
    def __init__(
        self,
        marker: str = None,
        host_id: str = None,
        oms_data: List[Dict[str, str]] = None,
    ):
        self.marker = marker
        self.host_id = host_id
        self.oms_data = oms_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.oms_data is not None:
            result['OmsData'] = self.oms_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('OmsData') is not None:
            self.oms_data = m.get('OmsData')
        return self


class QueryUserOmsDataResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        data: QueryUserOmsDataResponseBodyData = None,
    ):
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = QueryUserOmsDataResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryUserOmsDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryUserOmsDataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = QueryUserOmsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewInstanceRequest(TeaModel):
    def __init__(
        self,
        product_code: str = None,
        instance_id: str = None,
        renew_period: int = None,
        client_token: str = None,
        product_type: str = None,
        owner_id: int = None,
    ):
        self.product_code = product_code
        self.instance_id = instance_id
        self.renew_period = renew_period
        self.client_token = client_token
        self.product_type = product_type
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.renew_period is not None:
            result['RenewPeriod'] = self.renew_period
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RenewPeriod') is not None:
            self.renew_period = m.get('RenewPeriod')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class RenewInstanceResponseBodyData(TeaModel):
    def __init__(
        self,
        order_id: str = None,
    ):
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class RenewInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        data: RenewInstanceResponseBodyData = None,
    ):
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = RenewInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class RenewInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RenewInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = RenewInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewResourcePackageRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        instance_id: str = None,
        effective_date: str = None,
        duration: int = None,
        pricing_cycle: str = None,
    ):
        self.owner_id = owner_id
        self.instance_id = instance_id
        self.effective_date = effective_date
        self.duration = duration
        self.pricing_cycle = pricing_cycle

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.effective_date is not None:
            result['EffectiveDate'] = self.effective_date
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('EffectiveDate') is not None:
            self.effective_date = m.get('EffectiveDate')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        return self


class RenewResourcePackageResponseBodyData(TeaModel):
    def __init__(
        self,
        order_id: int = None,
        instance_id: str = None,
    ):
        self.order_id = order_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class RenewResourcePackageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        order_id: int = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        data: RenewResourcePackageResponseBodyData = None,
    ):
        self.request_id = request_id
        self.order_id = order_id
        self.success = success
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = RenewResourcePackageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class RenewResourcePackageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RenewResourcePackageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = RenewResourcePackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveUserCreditRequest(TeaModel):
    def __init__(
        self,
        avoid_expiration: bool = None,
        avoid_prepaid_notification: bool = None,
        description: str = None,
        avoid_notification: bool = None,
        credit_value: str = None,
        avoid_prepaid_expiration: bool = None,
        operator: str = None,
        credit_type: str = None,
    ):
        self.avoid_expiration = avoid_expiration
        self.avoid_prepaid_notification = avoid_prepaid_notification
        self.description = description
        self.avoid_notification = avoid_notification
        self.credit_value = credit_value
        self.avoid_prepaid_expiration = avoid_prepaid_expiration
        self.operator = operator
        self.credit_type = credit_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.avoid_expiration is not None:
            result['AvoidExpiration'] = self.avoid_expiration
        if self.avoid_prepaid_notification is not None:
            result['AvoidPrepaidNotification'] = self.avoid_prepaid_notification
        if self.description is not None:
            result['Description'] = self.description
        if self.avoid_notification is not None:
            result['AvoidNotification'] = self.avoid_notification
        if self.credit_value is not None:
            result['CreditValue'] = self.credit_value
        if self.avoid_prepaid_expiration is not None:
            result['AvoidPrepaidExpiration'] = self.avoid_prepaid_expiration
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.credit_type is not None:
            result['CreditType'] = self.credit_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvoidExpiration') is not None:
            self.avoid_expiration = m.get('AvoidExpiration')
        if m.get('AvoidPrepaidNotification') is not None:
            self.avoid_prepaid_notification = m.get('AvoidPrepaidNotification')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('AvoidNotification') is not None:
            self.avoid_notification = m.get('AvoidNotification')
        if m.get('CreditValue') is not None:
            self.credit_value = m.get('CreditValue')
        if m.get('AvoidPrepaidExpiration') is not None:
            self.avoid_prepaid_expiration = m.get('AvoidPrepaidExpiration')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('CreditType') is not None:
            self.credit_type = m.get('CreditType')
        return self


class SaveUserCreditResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        success: bool = None,
        request_id: str = None,
        message: str = None,
    ):
        self.code = code
        self.success = success
        self.request_id = request_id
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class SaveUserCreditResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SaveUserCreditResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = SaveUserCreditResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetCreditLabelActionRequest(TeaModel):
    def __init__(
        self,
        action_type: str = None,
        uid: str = None,
        clear_cycle: str = None,
        credit_amount: str = None,
        currency_code: str = None,
        daily_cycle: str = None,
        description: str = None,
        is_need_add_settle_label: str = None,
        is_need_adjust_credit_account: str = None,
        is_need_save_notify_rule: str = None,
        is_need_set_credit_amount: str = None,
        need_notice: bool = None,
        new_create_mode: bool = None,
        operator: str = None,
        request_id: str = None,
        site_code: str = None,
        source: str = None,
    ):
        self.action_type = action_type
        self.uid = uid
        self.clear_cycle = clear_cycle
        self.credit_amount = credit_amount
        self.currency_code = currency_code
        self.daily_cycle = daily_cycle
        self.description = description
        self.is_need_add_settle_label = is_need_add_settle_label
        self.is_need_adjust_credit_account = is_need_adjust_credit_account
        self.is_need_save_notify_rule = is_need_save_notify_rule
        self.is_need_set_credit_amount = is_need_set_credit_amount
        self.need_notice = need_notice
        self.new_create_mode = new_create_mode
        self.operator = operator
        self.request_id = request_id
        self.site_code = site_code
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.clear_cycle is not None:
            result['ClearCycle'] = self.clear_cycle
        if self.credit_amount is not None:
            result['CreditAmount'] = self.credit_amount
        if self.currency_code is not None:
            result['CurrencyCode'] = self.currency_code
        if self.daily_cycle is not None:
            result['DailyCycle'] = self.daily_cycle
        if self.description is not None:
            result['Description'] = self.description
        if self.is_need_add_settle_label is not None:
            result['IsNeedAddSettleLabel'] = self.is_need_add_settle_label
        if self.is_need_adjust_credit_account is not None:
            result['IsNeedAdjustCreditAccount'] = self.is_need_adjust_credit_account
        if self.is_need_save_notify_rule is not None:
            result['IsNeedSaveNotifyRule'] = self.is_need_save_notify_rule
        if self.is_need_set_credit_amount is not None:
            result['IsNeedSetCreditAmount'] = self.is_need_set_credit_amount
        if self.need_notice is not None:
            result['NeedNotice'] = self.need_notice
        if self.new_create_mode is not None:
            result['NewCreateMode'] = self.new_create_mode
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.site_code is not None:
            result['SiteCode'] = self.site_code
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('ClearCycle') is not None:
            self.clear_cycle = m.get('ClearCycle')
        if m.get('CreditAmount') is not None:
            self.credit_amount = m.get('CreditAmount')
        if m.get('CurrencyCode') is not None:
            self.currency_code = m.get('CurrencyCode')
        if m.get('DailyCycle') is not None:
            self.daily_cycle = m.get('DailyCycle')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IsNeedAddSettleLabel') is not None:
            self.is_need_add_settle_label = m.get('IsNeedAddSettleLabel')
        if m.get('IsNeedAdjustCreditAccount') is not None:
            self.is_need_adjust_credit_account = m.get('IsNeedAdjustCreditAccount')
        if m.get('IsNeedSaveNotifyRule') is not None:
            self.is_need_save_notify_rule = m.get('IsNeedSaveNotifyRule')
        if m.get('IsNeedSetCreditAmount') is not None:
            self.is_need_set_credit_amount = m.get('IsNeedSetCreditAmount')
        if m.get('NeedNotice') is not None:
            self.need_notice = m.get('NeedNotice')
        if m.get('NewCreateMode') is not None:
            self.new_create_mode = m.get('NewCreateMode')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SiteCode') is not None:
            self.site_code = m.get('SiteCode')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class SetCreditLabelActionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        message: str = None,
        success: bool = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.success = success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
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
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetCreditLabelActionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetCreditLabelActionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = SetCreditLabelActionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetRenewalRequest(TeaModel):
    def __init__(
        self,
        renewal_period: int = None,
        instance_ids: str = None,
        owner_id: int = None,
        product_code: str = None,
        product_type: str = None,
        subscription_type: str = None,
        renewal_period_unit: str = None,
        renewal_status: str = None,
    ):
        self.renewal_period = renewal_period
        self.instance_ids = instance_ids
        self.owner_id = owner_id
        self.product_code = product_code
        self.product_type = product_type
        self.subscription_type = subscription_type
        self.renewal_period_unit = renewal_period_unit
        self.renewal_status = renewal_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.renewal_period is not None:
            result['RenewalPeriod'] = self.renewal_period
        if self.instance_ids is not None:
            result['InstanceIDs'] = self.instance_ids
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.renewal_period_unit is not None:
            result['RenewalPeriodUnit'] = self.renewal_period_unit
        if self.renewal_status is not None:
            result['RenewalStatus'] = self.renewal_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RenewalPeriod') is not None:
            self.renewal_period = m.get('RenewalPeriod')
        if m.get('InstanceIDs') is not None:
            self.instance_ids = m.get('InstanceIDs')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('RenewalPeriodUnit') is not None:
            self.renewal_period_unit = m.get('RenewalPeriodUnit')
        if m.get('RenewalStatus') is not None:
            self.renewal_status = m.get('RenewalStatus')
        return self


class SetRenewalResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
    ):
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class SetRenewalResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetRenewalResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = SetRenewalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetResellerUserAlarmThresholdRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        alarm_type: str = None,
        alarm_thresholds: str = None,
    ):
        self.owner_id = owner_id
        self.alarm_type = alarm_type
        self.alarm_thresholds = alarm_thresholds

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.alarm_type is not None:
            result['AlarmType'] = self.alarm_type
        if self.alarm_thresholds is not None:
            result['AlarmThresholds'] = self.alarm_thresholds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('AlarmType') is not None:
            self.alarm_type = m.get('AlarmType')
        if m.get('AlarmThresholds') is not None:
            self.alarm_thresholds = m.get('AlarmThresholds')
        return self


class SetResellerUserAlarmThresholdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
        success: bool = None,
        data: bool = None,
    ):
        self.request_id = request_id
        self.code = code
        self.message = message
        self.success = success
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class SetResellerUserAlarmThresholdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetResellerUserAlarmThresholdResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = SetResellerUserAlarmThresholdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetResellerUserQuotaRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        amount: str = None,
        currency: str = None,
        out_biz_id: str = None,
    ):
        self.owner_id = owner_id
        self.amount = amount
        self.currency = currency
        self.out_biz_id = out_biz_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.out_biz_id is not None:
            result['OutBizId'] = self.out_biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('OutBizId') is not None:
            self.out_biz_id = m.get('OutBizId')
        return self


class SetResellerUserQuotaResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
        success: bool = None,
        data: bool = None,
    ):
        self.request_id = request_id
        self.code = code
        self.message = message
        self.success = success
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class SetResellerUserQuotaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetResellerUserQuotaResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = SetResellerUserQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetResellerUserStatusRequest(TeaModel):
    def __init__(
        self,
        owner_id: str = None,
        status: str = None,
        business_type: str = None,
    ):
        self.owner_id = owner_id
        self.status = status
        self.business_type = business_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.status is not None:
            result['Status'] = self.status
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        return self


class SetResellerUserStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
        success: bool = None,
        data: bool = None,
    ):
        self.request_id = request_id
        self.code = code
        self.message = message
        self.success = success
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class SetResellerUserStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetResellerUserStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = SetResellerUserStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubscribeBillToOSSRequest(TeaModel):
    def __init__(
        self,
        subscribe_bucket: str = None,
        subscribe_type: str = None,
        mult_account_rel_subscribe: str = None,
        bucket_owner_id: int = None,
    ):
        self.subscribe_bucket = subscribe_bucket
        self.subscribe_type = subscribe_type
        self.mult_account_rel_subscribe = mult_account_rel_subscribe
        self.bucket_owner_id = bucket_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.subscribe_bucket is not None:
            result['SubscribeBucket'] = self.subscribe_bucket
        if self.subscribe_type is not None:
            result['SubscribeType'] = self.subscribe_type
        if self.mult_account_rel_subscribe is not None:
            result['MultAccountRelSubscribe'] = self.mult_account_rel_subscribe
        if self.bucket_owner_id is not None:
            result['BucketOwnerId'] = self.bucket_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubscribeBucket') is not None:
            self.subscribe_bucket = m.get('SubscribeBucket')
        if m.get('SubscribeType') is not None:
            self.subscribe_type = m.get('SubscribeType')
        if m.get('MultAccountRelSubscribe') is not None:
            self.mult_account_rel_subscribe = m.get('MultAccountRelSubscribe')
        if m.get('BucketOwnerId') is not None:
            self.bucket_owner_id = m.get('BucketOwnerId')
        return self


class SubscribeBillToOSSResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
    ):
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class SubscribeBillToOSSResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SubscribeBillToOSSResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = SubscribeBillToOSSResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
        resource_id: List[str] = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        request_id: str = None,
        success: bool = None,
        message: str = None,
        data: bool = None,
    ):
        self.code = code
        self.request_id = request_id
        self.success = success
        self.message = message
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnsubscribeBillToOSSRequest(TeaModel):
    def __init__(
        self,
        subscribe_type: str = None,
        mult_account_rel_subscribe: str = None,
    ):
        self.subscribe_type = subscribe_type
        self.mult_account_rel_subscribe = mult_account_rel_subscribe

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.subscribe_type is not None:
            result['SubscribeType'] = self.subscribe_type
        if self.mult_account_rel_subscribe is not None:
            result['MultAccountRelSubscribe'] = self.mult_account_rel_subscribe
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubscribeType') is not None:
            self.subscribe_type = m.get('SubscribeType')
        if m.get('MultAccountRelSubscribe') is not None:
            self.mult_account_rel_subscribe = m.get('MultAccountRelSubscribe')
        return self


class UnsubscribeBillToOSSResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
    ):
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class UnsubscribeBillToOSSResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UnsubscribeBillToOSSResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = UnsubscribeBillToOSSResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
        resource_id: List[str] = None,
        tag_key: List[str] = None,
        all: bool = None,
    ):
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.tag_key = tag_key
        self.all = all

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.all is not None:
            result['All'] = self.all
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('All') is not None:
            self.all = m.get('All')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        request_id: str = None,
        success: bool = None,
        message: str = None,
        data: bool = None,
    ):
        self.code = code
        self.request_id = request_id
        self.success = success
        self.message = message
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UntagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeResourcePackageRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        instance_id: str = None,
        effective_date: str = None,
        specification: str = None,
    ):
        self.owner_id = owner_id
        self.instance_id = instance_id
        self.effective_date = effective_date
        self.specification = specification

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.effective_date is not None:
            result['EffectiveDate'] = self.effective_date
        if self.specification is not None:
            result['Specification'] = self.specification
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('EffectiveDate') is not None:
            self.effective_date = m.get('EffectiveDate')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        return self


class UpgradeResourcePackageResponseBodyData(TeaModel):
    def __init__(
        self,
        order_id: int = None,
        instance_id: str = None,
    ):
        self.order_id = order_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class UpgradeResourcePackageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        order_id: int = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        data: UpgradeResourcePackageResponseBodyData = None,
    ):
        self.request_id = request_id
        self.order_id = order_id
        self.success = success
        self.code = code
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = UpgradeResourcePackageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class UpgradeResourcePackageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpgradeResourcePackageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = UpgradeResourcePackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


