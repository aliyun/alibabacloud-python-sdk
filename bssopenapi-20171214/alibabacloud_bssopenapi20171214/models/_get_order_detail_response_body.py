# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class GetOrderDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetOrderDetailResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code.
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
            temp_model = main_models.GetOrderDetailResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetOrderDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        host_name: str = None,
        order_list: main_models.GetOrderDetailResponseBodyDataOrderList = None,
        page_num: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The hostname.
        self.host_name = host_name
        # The orders returned.
        self.order_list = order_list
        # The page number.
        self.page_num = page_num
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.order_list:
            self.order_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host_name is not None:
            result['HostName'] = self.host_name

        if self.order_list is not None:
            result['OrderList'] = self.order_list.to_map()

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')

        if m.get('OrderList') is not None:
            temp_model = main_models.GetOrderDetailResponseBodyDataOrderList()
            self.order_list = temp_model.from_map(m.get('OrderList'))

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class GetOrderDetailResponseBodyDataOrderList(DaraModel):
    def __init__(
        self,
        order: List[main_models.GetOrderDetailResponseBodyDataOrderListOrder] = None,
    ):
        self.order = order

    def validate(self):
        if self.order:
            for v1 in self.order:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Order'] = []
        if self.order is not None:
            for k1 in self.order:
                result['Order'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.order = []
        if m.get('Order') is not None:
            for k1 in m.get('Order'):
                temp_model = main_models.GetOrderDetailResponseBodyDataOrderListOrder()
                self.order.append(temp_model.from_map(k1))

        return self

class GetOrderDetailResponseBodyDataOrderListOrder(DaraModel):
    def __init__(
        self,
        after_tax_amount: str = None,
        bill_module_config: main_models.GetOrderDetailResponseBodyDataOrderListOrderBillModuleConfig = None,
        commodity_code: str = None,
        config: str = None,
        create_time: str = None,
        currency: str = None,
        extend_infos: Dict[str, str] = None,
        instance_ids: str = None,
        operator: str = None,
        order_id: str = None,
        order_sub_type: str = None,
        order_type: str = None,
        original_config: str = None,
        original_module_config: main_models.GetOrderDetailResponseBodyDataOrderListOrderOriginalModuleConfig = None,
        payment_currency: str = None,
        payment_status: str = None,
        payment_time: str = None,
        pretax_amount: str = None,
        pretax_amount_local: str = None,
        pretax_gross_amount: str = None,
        product_code: str = None,
        product_type: str = None,
        quantity: str = None,
        region: str = None,
        related_order_id: str = None,
        sub_order_id: str = None,
        subscription_type: str = None,
        tax: str = None,
        usage_end_time: str = None,
        usage_start_time: str = None,
    ):
        # The aftertaxt amount of the order.
        self.after_tax_amount = after_tax_amount
        # The billing information about the configurations.
        self.bill_module_config = bill_module_config
        # The commodity code.
        self.commodity_code = commodity_code
        # The configurations of the main service.
        self.config = config
        # The time when the order was created.
        self.create_time = create_time
        # The currency. Valid values: CNY, USD, and JPY.
        self.currency = currency
        # The additional information about the order.
        self.extend_infos = extend_infos
        # The instance IDs.
        self.instance_ids = instance_ids
        # The ID of the Resource Access Management (RAM) user that performs operations on the order. If no RAM user is involved, this parameter is empty.
        self.operator = operator
        # The order ID.
        self.order_id = order_id
        # The type of the suborder. A value of productsuborder indicates service suborder. A value of refundsuborder indicates refund suborder.
        self.order_sub_type = order_sub_type
        # The type of the order. Valid values: new, renew, upgrade, and refund.
        self.order_type = order_type
        # The configuration information that is not formatted.
        self.original_config = original_config
        # The information about the configurations.
        self.original_module_config = original_module_config
        # The currency used for payment. Valid values: CNY, USD, and JPY.
        self.payment_currency = payment_currency
        # The payment state. Valid values: unpaid, paid, and canceled.
        self.payment_status = payment_status
        # The time of payment.
        self.payment_time = payment_time
        # The pretax amount of the order.
        self.pretax_amount = pretax_amount
        # The pretax amount of the order in local currency.
        self.pretax_amount_local = pretax_amount_local
        # The pretax gross amount of the order.
        self.pretax_gross_amount = pretax_gross_amount
        # The code of the main service.
        self.product_code = product_code
        # The type of the main service.
        self.product_type = product_type
        # The number of main services.
        self.quantity = quantity
        # The region ID.
        self.region = region
        # The ID of the associated order.
        self.related_order_id = related_order_id
        # The ID of the suborder.
        self.sub_order_id = sub_order_id
        # The billing method. Valid values: Subscription and PayAsYouGo.
        self.subscription_type = subscription_type
        # The tax of the order.
        self.tax = tax
        # The time when the service ends.
        self.usage_end_time = usage_end_time
        # The time when the service starts.
        self.usage_start_time = usage_start_time

    def validate(self):
        if self.bill_module_config:
            self.bill_module_config.validate()
        if self.original_module_config:
            self.original_module_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.after_tax_amount is not None:
            result['AfterTaxAmount'] = self.after_tax_amount

        if self.bill_module_config is not None:
            result['BillModuleConfig'] = self.bill_module_config.to_map()

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.config is not None:
            result['Config'] = self.config

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.currency is not None:
            result['Currency'] = self.currency

        if self.extend_infos is not None:
            result['ExtendInfos'] = self.extend_infos

        if self.instance_ids is not None:
            result['InstanceIDs'] = self.instance_ids

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.order_sub_type is not None:
            result['OrderSubType'] = self.order_sub_type

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.original_config is not None:
            result['OriginalConfig'] = self.original_config

        if self.original_module_config is not None:
            result['OriginalModuleConfig'] = self.original_module_config.to_map()

        if self.payment_currency is not None:
            result['PaymentCurrency'] = self.payment_currency

        if self.payment_status is not None:
            result['PaymentStatus'] = self.payment_status

        if self.payment_time is not None:
            result['PaymentTime'] = self.payment_time

        if self.pretax_amount is not None:
            result['PretaxAmount'] = self.pretax_amount

        if self.pretax_amount_local is not None:
            result['PretaxAmountLocal'] = self.pretax_amount_local

        if self.pretax_gross_amount is not None:
            result['PretaxGrossAmount'] = self.pretax_gross_amount

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.quantity is not None:
            result['Quantity'] = self.quantity

        if self.region is not None:
            result['Region'] = self.region

        if self.related_order_id is not None:
            result['RelatedOrderId'] = self.related_order_id

        if self.sub_order_id is not None:
            result['SubOrderId'] = self.sub_order_id

        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type

        if self.tax is not None:
            result['Tax'] = self.tax

        if self.usage_end_time is not None:
            result['UsageEndTime'] = self.usage_end_time

        if self.usage_start_time is not None:
            result['UsageStartTime'] = self.usage_start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AfterTaxAmount') is not None:
            self.after_tax_amount = m.get('AfterTaxAmount')

        if m.get('BillModuleConfig') is not None:
            temp_model = main_models.GetOrderDetailResponseBodyDataOrderListOrderBillModuleConfig()
            self.bill_module_config = temp_model.from_map(m.get('BillModuleConfig'))

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('ExtendInfos') is not None:
            self.extend_infos = m.get('ExtendInfos')

        if m.get('InstanceIDs') is not None:
            self.instance_ids = m.get('InstanceIDs')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('OrderSubType') is not None:
            self.order_sub_type = m.get('OrderSubType')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('OriginalConfig') is not None:
            self.original_config = m.get('OriginalConfig')

        if m.get('OriginalModuleConfig') is not None:
            temp_model = main_models.GetOrderDetailResponseBodyDataOrderListOrderOriginalModuleConfig()
            self.original_module_config = temp_model.from_map(m.get('OriginalModuleConfig'))

        if m.get('PaymentCurrency') is not None:
            self.payment_currency = m.get('PaymentCurrency')

        if m.get('PaymentStatus') is not None:
            self.payment_status = m.get('PaymentStatus')

        if m.get('PaymentTime') is not None:
            self.payment_time = m.get('PaymentTime')

        if m.get('PretaxAmount') is not None:
            self.pretax_amount = m.get('PretaxAmount')

        if m.get('PretaxAmountLocal') is not None:
            self.pretax_amount_local = m.get('PretaxAmountLocal')

        if m.get('PretaxGrossAmount') is not None:
            self.pretax_gross_amount = m.get('PretaxGrossAmount')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('RelatedOrderId') is not None:
            self.related_order_id = m.get('RelatedOrderId')

        if m.get('SubOrderId') is not None:
            self.sub_order_id = m.get('SubOrderId')

        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')

        if m.get('Tax') is not None:
            self.tax = m.get('Tax')

        if m.get('UsageEndTime') is not None:
            self.usage_end_time = m.get('UsageEndTime')

        if m.get('UsageStartTime') is not None:
            self.usage_start_time = m.get('UsageStartTime')

        return self

class GetOrderDetailResponseBodyDataOrderListOrderOriginalModuleConfig(DaraModel):
    def __init__(
        self,
        original_module_config: List[main_models.GetOrderDetailResponseBodyDataOrderListOrderOriginalModuleConfigOriginalModuleConfig] = None,
    ):
        self.original_module_config = original_module_config

    def validate(self):
        if self.original_module_config:
            for v1 in self.original_module_config:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['originalModuleConfig'] = []
        if self.original_module_config is not None:
            for k1 in self.original_module_config:
                result['originalModuleConfig'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.original_module_config = []
        if m.get('originalModuleConfig') is not None:
            for k1 in m.get('originalModuleConfig'):
                temp_model = main_models.GetOrderDetailResponseBodyDataOrderListOrderOriginalModuleConfigOriginalModuleConfig()
                self.original_module_config.append(temp_model.from_map(k1))

        return self

class GetOrderDetailResponseBodyDataOrderListOrderOriginalModuleConfigOriginalModuleConfig(DaraModel):
    def __init__(
        self,
        code: str = None,
        module_properties: main_models.GetOrderDetailResponseBodyDataOrderListOrderOriginalModuleConfigOriginalModuleConfigModuleProperties = None,
        name: str = None,
    ):
        # The code of the configuration item.
        self.code = code
        # The attributes of the configured item.
        self.module_properties = module_properties
        # The name of the configuration item.
        self.name = name

    def validate(self):
        if self.module_properties:
            self.module_properties.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.module_properties is not None:
            result['ModuleProperties'] = self.module_properties.to_map()

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('ModuleProperties') is not None:
            temp_model = main_models.GetOrderDetailResponseBodyDataOrderListOrderOriginalModuleConfigOriginalModuleConfigModuleProperties()
            self.module_properties = temp_model.from_map(m.get('ModuleProperties'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class GetOrderDetailResponseBodyDataOrderListOrderOriginalModuleConfigOriginalModuleConfigModuleProperties(DaraModel):
    def __init__(
        self,
        module_properties: List[main_models.GetOrderDetailResponseBodyDataOrderListOrderOriginalModuleConfigOriginalModuleConfigModulePropertiesModuleProperties] = None,
    ):
        self.module_properties = module_properties

    def validate(self):
        if self.module_properties:
            for v1 in self.module_properties:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['moduleProperties'] = []
        if self.module_properties is not None:
            for k1 in self.module_properties:
                result['moduleProperties'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.module_properties = []
        if m.get('moduleProperties') is not None:
            for k1 in m.get('moduleProperties'):
                temp_model = main_models.GetOrderDetailResponseBodyDataOrderListOrderOriginalModuleConfigOriginalModuleConfigModulePropertiesModuleProperties()
                self.module_properties.append(temp_model.from_map(k1))

        return self

class GetOrderDetailResponseBodyDataOrderListOrderOriginalModuleConfigOriginalModuleConfigModulePropertiesModuleProperties(DaraModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
        value: str = None,
    ):
        # The attribute code of the configured item.
        self.code = code
        # The attribute name of the configured item.
        self.name = name
        # The attribute value of the configured item.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetOrderDetailResponseBodyDataOrderListOrderBillModuleConfig(DaraModel):
    def __init__(
        self,
        bill_module_config: List[main_models.GetOrderDetailResponseBodyDataOrderListOrderBillModuleConfigBillModuleConfig] = None,
    ):
        self.bill_module_config = bill_module_config

    def validate(self):
        if self.bill_module_config:
            for v1 in self.bill_module_config:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['billModuleConfig'] = []
        if self.bill_module_config is not None:
            for k1 in self.bill_module_config:
                result['billModuleConfig'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bill_module_config = []
        if m.get('billModuleConfig') is not None:
            for k1 in m.get('billModuleConfig'):
                temp_model = main_models.GetOrderDetailResponseBodyDataOrderListOrderBillModuleConfigBillModuleConfig()
                self.bill_module_config.append(temp_model.from_map(k1))

        return self

class GetOrderDetailResponseBodyDataOrderListOrderBillModuleConfigBillModuleConfig(DaraModel):
    def __init__(
        self,
        api_code: str = None,
        bill_module_properties: main_models.GetOrderDetailResponseBodyDataOrderListOrderBillModuleConfigBillModuleConfigBillModuleProperties = None,
        code: str = None,
        name: str = None,
    ):
        # The API code of the configuration item.
        self.api_code = api_code
        # The attributes of the configured item.
        self.bill_module_properties = bill_module_properties
        # The code of the configuration item.
        self.code = code
        # The name of the configuration item.
        self.name = name

    def validate(self):
        if self.bill_module_properties:
            self.bill_module_properties.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_code is not None:
            result['ApiCode'] = self.api_code

        if self.bill_module_properties is not None:
            result['BillModuleProperties'] = self.bill_module_properties.to_map()

        if self.code is not None:
            result['Code'] = self.code

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiCode') is not None:
            self.api_code = m.get('ApiCode')

        if m.get('BillModuleProperties') is not None:
            temp_model = main_models.GetOrderDetailResponseBodyDataOrderListOrderBillModuleConfigBillModuleConfigBillModuleProperties()
            self.bill_module_properties = temp_model.from_map(m.get('BillModuleProperties'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class GetOrderDetailResponseBodyDataOrderListOrderBillModuleConfigBillModuleConfigBillModuleProperties(DaraModel):
    def __init__(
        self,
        bill_module_properties: List[main_models.GetOrderDetailResponseBodyDataOrderListOrderBillModuleConfigBillModuleConfigBillModulePropertiesBillModuleProperties] = None,
    ):
        self.bill_module_properties = bill_module_properties

    def validate(self):
        if self.bill_module_properties:
            for v1 in self.bill_module_properties:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['billModuleProperties'] = []
        if self.bill_module_properties is not None:
            for k1 in self.bill_module_properties:
                result['billModuleProperties'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bill_module_properties = []
        if m.get('billModuleProperties') is not None:
            for k1 in m.get('billModuleProperties'):
                temp_model = main_models.GetOrderDetailResponseBodyDataOrderListOrderBillModuleConfigBillModuleConfigBillModulePropertiesBillModuleProperties()
                self.bill_module_properties.append(temp_model.from_map(k1))

        return self

class GetOrderDetailResponseBodyDataOrderListOrderBillModuleConfigBillModuleConfigBillModulePropertiesBillModuleProperties(DaraModel):
    def __init__(
        self,
        attr_api_code: str = None,
        module_api_code: str = None,
        value: str = None,
    ):
        # The attribute code of the configured item.
        self.attr_api_code = attr_api_code
        # The API code of the configured item.
        self.module_api_code = module_api_code
        # The attribute value of the configuration item.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attr_api_code is not None:
            result['AttrApiCode'] = self.attr_api_code

        if self.module_api_code is not None:
            result['ModuleApiCode'] = self.module_api_code

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttrApiCode') is not None:
            self.attr_api_code = m.get('AttrApiCode')

        if m.get('ModuleApiCode') is not None:
            self.module_api_code = m.get('ModuleApiCode')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

