# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20230930 import models as main_models
from darabonba.model import DaraModel

class DescribeFrInstancesResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        data: List[main_models.DescribeFrInstancesResponseBodyData] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The current page number.
        self.current_page = current_page
        # The data list.
        self.data = data
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of records.
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
                temp_model = main_models.DescribeFrInstancesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeFrInstancesResponseBodyData(DaraModel):
    def __init__(
        self,
        account_id: int = None,
        account_name: str = None,
        auto_purchase: main_models.DescribeFrInstancesResponseBodyDataAutoPurchase = None,
        capacitiy_type_name: str = None,
        capacity_type: main_models.DescribeFrInstancesResponseBodyDataCapacityType = None,
        capacity_type_code: str = None,
        commodity: main_models.DescribeFrInstancesResponseBodyDataCommodity = None,
        commodity_code: str = None,
        commodity_name: str = None,
        curr_capacity_base_unit: str = None,
        curr_capacity_base_value: str = None,
        curr_capacity_view_unit: str = None,
        curr_capacity_view_value: str = None,
        cycle_type: main_models.DescribeFrInstancesResponseBodyDataCycleType = None,
        cycle_type_code: str = None,
        cycle_type_name: str = None,
        deduct_regions: List[main_models.DescribeFrInstancesResponseBodyDataDeductRegions] = None,
        enable_deduct_rule: bool = None,
        enable_exchange: bool = None,
        enable_renew: bool = None,
        enable_upgrade: bool = None,
        end_time: int = None,
        exchange_commodity_code: str = None,
        init_capacity_base_unit: str = None,
        init_capacity_base_value: str = None,
        init_capacity_view_unit: str = None,
        init_capacity_view_value: str = None,
        instance_id: str = None,
        period_capacity_view_unit: str = None,
        period_capacity_view_value: str = None,
        period_time: str = None,
        product: main_models.DescribeFrInstancesResponseBodyDataProduct = None,
        product_code: str = None,
        product_name: str = None,
        purchase_time: int = None,
        region: str = None,
        region_name: str = None,
        spec: str = None,
        start_time: int = None,
        status: main_models.DescribeFrInstancesResponseBodyDataStatus = None,
        status_code: str = None,
        status_name: str = None,
        template: main_models.DescribeFrInstancesResponseBodyDataTemplate = None,
        template_code: str = None,
        template_name: str = None,
        period_capacity_base_unit: str = None,
        period_capacity_base_value: str = None,
    ):
        # The account ID.
        self.account_id = account_id
        # The account name.
        self.account_name = account_name
        self.auto_purchase = auto_purchase
        # The capacity type name.
        self.capacitiy_type_name = capacitiy_type_name
        # The capacity type.
        self.capacity_type = capacity_type
        # The capacity type code.
        self.capacity_type_code = capacity_type_code
        # The commodity.
        self.commodity = commodity
        # The commodity code.
        self.commodity_code = commodity_code
        # The commodity name.
        self.commodity_name = commodity_name
        # The current capacity base unit.
        self.curr_capacity_base_unit = curr_capacity_base_unit
        # The current capacity base value.
        self.curr_capacity_base_value = curr_capacity_base_value
        # The current capacity display unit.
        self.curr_capacity_view_unit = curr_capacity_view_unit
        # The current capacity display value.
        self.curr_capacity_view_value = curr_capacity_view_value
        # The commitment cycle.
        self.cycle_type = cycle_type
        # The commitment cycle code.
        self.cycle_type_code = cycle_type_code
        # The commitment cycle name.
        self.cycle_type_name = cycle_type_name
        # The list of deductible regions.
        self.deduct_regions = deduct_regions
        self.enable_deduct_rule = enable_deduct_rule
        # Indicates whether exchange is supported.
        self.enable_exchange = enable_exchange
        # Indicates whether renewal is supported.
        self.enable_renew = enable_renew
        # Indicates whether upgrade is supported.
        self.enable_upgrade = enable_upgrade
        # The expiration time.
        self.end_time = end_time
        # The exchange commodity code.
        self.exchange_commodity_code = exchange_commodity_code
        # The initial capacity base unit.
        self.init_capacity_base_unit = init_capacity_base_unit
        # The initial capacity base value.
        self.init_capacity_base_value = init_capacity_base_value
        # The initial capacity display unit.
        self.init_capacity_view_unit = init_capacity_view_unit
        # The initial capacity display value.
        self.init_capacity_view_value = init_capacity_view_value
        # The instance name.
        self.instance_id = instance_id
        # The period capacity display unit.
        self.period_capacity_view_unit = period_capacity_view_unit
        # The period capacity display value.
        self.period_capacity_view_value = period_capacity_view_value
        # The period time.
        self.period_time = period_time
        # The product.
        self.product = product
        # The product code.
        self.product_code = product_code
        # The product name.
        self.product_name = product_name
        # The purchase time.
        self.purchase_time = purchase_time
        # The region.
        self.region = region
        # The region name.
        self.region_name = region_name
        # The specification.
        self.spec = spec
        # The effective period.
        self.start_time = start_time
        # The resource status.
        self.status = status
        # The resource status code.
        self.status_code = status_code
        # The resource status name.
        self.status_name = status_name
        # The template.
        self.template = template
        # The template code.
        self.template_code = template_code
        # The template name.
        self.template_name = template_name
        # The periodic capacity base unit.
        self.period_capacity_base_unit = period_capacity_base_unit
        # The periodic capacity base value.
        self.period_capacity_base_value = period_capacity_base_value

    def validate(self):
        if self.auto_purchase:
            self.auto_purchase.validate()
        if self.capacity_type:
            self.capacity_type.validate()
        if self.commodity:
            self.commodity.validate()
        if self.cycle_type:
            self.cycle_type.validate()
        if self.deduct_regions:
            for v1 in self.deduct_regions:
                 if v1:
                    v1.validate()
        if self.product:
            self.product.validate()
        if self.status:
            self.status.validate()
        if self.template:
            self.template.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.auto_purchase is not None:
            result['AutoPurchase'] = self.auto_purchase.to_map()

        if self.capacitiy_type_name is not None:
            result['CapacitiyTypeName'] = self.capacitiy_type_name

        if self.capacity_type is not None:
            result['CapacityType'] = self.capacity_type.to_map()

        if self.capacity_type_code is not None:
            result['CapacityTypeCode'] = self.capacity_type_code

        if self.commodity is not None:
            result['Commodity'] = self.commodity.to_map()

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.commodity_name is not None:
            result['CommodityName'] = self.commodity_name

        if self.curr_capacity_base_unit is not None:
            result['CurrCapacityBaseUnit'] = self.curr_capacity_base_unit

        if self.curr_capacity_base_value is not None:
            result['CurrCapacityBaseValue'] = self.curr_capacity_base_value

        if self.curr_capacity_view_unit is not None:
            result['CurrCapacityViewUnit'] = self.curr_capacity_view_unit

        if self.curr_capacity_view_value is not None:
            result['CurrCapacityViewValue'] = self.curr_capacity_view_value

        if self.cycle_type is not None:
            result['CycleType'] = self.cycle_type.to_map()

        if self.cycle_type_code is not None:
            result['CycleTypeCode'] = self.cycle_type_code

        if self.cycle_type_name is not None:
            result['CycleTypeName'] = self.cycle_type_name

        result['DeductRegions'] = []
        if self.deduct_regions is not None:
            for k1 in self.deduct_regions:
                result['DeductRegions'].append(k1.to_map() if k1 else None)

        if self.enable_deduct_rule is not None:
            result['EnableDeductRule'] = self.enable_deduct_rule

        if self.enable_exchange is not None:
            result['EnableExchange'] = self.enable_exchange

        if self.enable_renew is not None:
            result['EnableRenew'] = self.enable_renew

        if self.enable_upgrade is not None:
            result['EnableUpgrade'] = self.enable_upgrade

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.exchange_commodity_code is not None:
            result['ExchangeCommodityCode'] = self.exchange_commodity_code

        if self.init_capacity_base_unit is not None:
            result['InitCapacityBaseUnit'] = self.init_capacity_base_unit

        if self.init_capacity_base_value is not None:
            result['InitCapacityBaseValue'] = self.init_capacity_base_value

        if self.init_capacity_view_unit is not None:
            result['InitCapacityViewUnit'] = self.init_capacity_view_unit

        if self.init_capacity_view_value is not None:
            result['InitCapacityViewValue'] = self.init_capacity_view_value

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.period_capacity_view_unit is not None:
            result['PeriodCapacityViewUnit'] = self.period_capacity_view_unit

        if self.period_capacity_view_value is not None:
            result['PeriodCapacityViewValue'] = self.period_capacity_view_value

        if self.period_time is not None:
            result['PeriodTime'] = self.period_time

        if self.product is not None:
            result['Product'] = self.product.to_map()

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_name is not None:
            result['ProductName'] = self.product_name

        if self.purchase_time is not None:
            result['PurchaseTime'] = self.purchase_time

        if self.region is not None:
            result['Region'] = self.region

        if self.region_name is not None:
            result['RegionName'] = self.region_name

        if self.spec is not None:
            result['Spec'] = self.spec

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status.to_map()

        if self.status_code is not None:
            result['StatusCode'] = self.status_code

        if self.status_name is not None:
            result['StatusName'] = self.status_name

        if self.template is not None:
            result['Template'] = self.template.to_map()

        if self.template_code is not None:
            result['TemplateCode'] = self.template_code

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.period_capacity_base_unit is not None:
            result['periodCapacityBaseUnit'] = self.period_capacity_base_unit

        if self.period_capacity_base_value is not None:
            result['periodCapacityBaseValue'] = self.period_capacity_base_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('AutoPurchase') is not None:
            temp_model = main_models.DescribeFrInstancesResponseBodyDataAutoPurchase()
            self.auto_purchase = temp_model.from_map(m.get('AutoPurchase'))

        if m.get('CapacitiyTypeName') is not None:
            self.capacitiy_type_name = m.get('CapacitiyTypeName')

        if m.get('CapacityType') is not None:
            temp_model = main_models.DescribeFrInstancesResponseBodyDataCapacityType()
            self.capacity_type = temp_model.from_map(m.get('CapacityType'))

        if m.get('CapacityTypeCode') is not None:
            self.capacity_type_code = m.get('CapacityTypeCode')

        if m.get('Commodity') is not None:
            temp_model = main_models.DescribeFrInstancesResponseBodyDataCommodity()
            self.commodity = temp_model.from_map(m.get('Commodity'))

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('CommodityName') is not None:
            self.commodity_name = m.get('CommodityName')

        if m.get('CurrCapacityBaseUnit') is not None:
            self.curr_capacity_base_unit = m.get('CurrCapacityBaseUnit')

        if m.get('CurrCapacityBaseValue') is not None:
            self.curr_capacity_base_value = m.get('CurrCapacityBaseValue')

        if m.get('CurrCapacityViewUnit') is not None:
            self.curr_capacity_view_unit = m.get('CurrCapacityViewUnit')

        if m.get('CurrCapacityViewValue') is not None:
            self.curr_capacity_view_value = m.get('CurrCapacityViewValue')

        if m.get('CycleType') is not None:
            temp_model = main_models.DescribeFrInstancesResponseBodyDataCycleType()
            self.cycle_type = temp_model.from_map(m.get('CycleType'))

        if m.get('CycleTypeCode') is not None:
            self.cycle_type_code = m.get('CycleTypeCode')

        if m.get('CycleTypeName') is not None:
            self.cycle_type_name = m.get('CycleTypeName')

        self.deduct_regions = []
        if m.get('DeductRegions') is not None:
            for k1 in m.get('DeductRegions'):
                temp_model = main_models.DescribeFrInstancesResponseBodyDataDeductRegions()
                self.deduct_regions.append(temp_model.from_map(k1))

        if m.get('EnableDeductRule') is not None:
            self.enable_deduct_rule = m.get('EnableDeductRule')

        if m.get('EnableExchange') is not None:
            self.enable_exchange = m.get('EnableExchange')

        if m.get('EnableRenew') is not None:
            self.enable_renew = m.get('EnableRenew')

        if m.get('EnableUpgrade') is not None:
            self.enable_upgrade = m.get('EnableUpgrade')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ExchangeCommodityCode') is not None:
            self.exchange_commodity_code = m.get('ExchangeCommodityCode')

        if m.get('InitCapacityBaseUnit') is not None:
            self.init_capacity_base_unit = m.get('InitCapacityBaseUnit')

        if m.get('InitCapacityBaseValue') is not None:
            self.init_capacity_base_value = m.get('InitCapacityBaseValue')

        if m.get('InitCapacityViewUnit') is not None:
            self.init_capacity_view_unit = m.get('InitCapacityViewUnit')

        if m.get('InitCapacityViewValue') is not None:
            self.init_capacity_view_value = m.get('InitCapacityViewValue')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PeriodCapacityViewUnit') is not None:
            self.period_capacity_view_unit = m.get('PeriodCapacityViewUnit')

        if m.get('PeriodCapacityViewValue') is not None:
            self.period_capacity_view_value = m.get('PeriodCapacityViewValue')

        if m.get('PeriodTime') is not None:
            self.period_time = m.get('PeriodTime')

        if m.get('Product') is not None:
            temp_model = main_models.DescribeFrInstancesResponseBodyDataProduct()
            self.product = temp_model.from_map(m.get('Product'))

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')

        if m.get('PurchaseTime') is not None:
            self.purchase_time = m.get('PurchaseTime')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            temp_model = main_models.DescribeFrInstancesResponseBodyDataStatus()
            self.status = temp_model.from_map(m.get('Status'))

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        if m.get('StatusName') is not None:
            self.status_name = m.get('StatusName')

        if m.get('Template') is not None:
            temp_model = main_models.DescribeFrInstancesResponseBodyDataTemplate()
            self.template = temp_model.from_map(m.get('Template'))

        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('periodCapacityBaseUnit') is not None:
            self.period_capacity_base_unit = m.get('periodCapacityBaseUnit')

        if m.get('periodCapacityBaseValue') is not None:
            self.period_capacity_base_value = m.get('periodCapacityBaseValue')

        return self

class DescribeFrInstancesResponseBodyDataTemplate(DaraModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
    ):
        # The property code.
        self.code = code
        # The property name.
        self.name = name

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class DescribeFrInstancesResponseBodyDataStatus(DaraModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
    ):
        # The property code.
        self.code = code
        # The property name.
        self.name = name

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class DescribeFrInstancesResponseBodyDataProduct(DaraModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
    ):
        # The property code.
        self.code = code
        # The property name.
        self.name = name

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class DescribeFrInstancesResponseBodyDataDeductRegions(DaraModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
    ):
        # The deductible region code.
        self.code = code
        # The deductible region.
        self.name = name

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class DescribeFrInstancesResponseBodyDataCycleType(DaraModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
    ):
        # The commitment cycle code.
        self.code = code
        # The commitment cycle name.
        self.name = name

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class DescribeFrInstancesResponseBodyDataCommodity(DaraModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
    ):
        # The property code.
        self.code = code
        # The property name.
        self.name = name

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class DescribeFrInstancesResponseBodyDataCapacityType(DaraModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
    ):
        # The property code.
        self.code = code
        # The property name.
        self.name = name

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class DescribeFrInstancesResponseBodyDataAutoPurchase(DaraModel):
    def __init__(
        self,
        already_auto_purchase: bool = None,
        setting_auto_purchase: bool = None,
        support_auto_purchase: bool = None,
    ):
        self.already_auto_purchase = already_auto_purchase
        self.setting_auto_purchase = setting_auto_purchase
        self.support_auto_purchase = support_auto_purchase

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.already_auto_purchase is not None:
            result['AlreadyAutoPurchase'] = self.already_auto_purchase

        if self.setting_auto_purchase is not None:
            result['SettingAutoPurchase'] = self.setting_auto_purchase

        if self.support_auto_purchase is not None:
            result['SupportAutoPurchase'] = self.support_auto_purchase

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlreadyAutoPurchase') is not None:
            self.already_auto_purchase = m.get('AlreadyAutoPurchase')

        if m.get('SettingAutoPurchase') is not None:
            self.setting_auto_purchase = m.get('SettingAutoPurchase')

        if m.get('SupportAutoPurchase') is not None:
            self.support_auto_purchase = m.get('SupportAutoPurchase')

        return self

