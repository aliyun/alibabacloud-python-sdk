# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20230930 import models as main_models
from darabonba.model import DaraModel

class DescribeDeductLogsResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        data: List[main_models.DescribeDeductLogsResponseBodyData] = None,
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
                temp_model = main_models.DescribeDeductLogsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDeductLogsResponseBodyData(DaraModel):
    def __init__(
        self,
        account_id: int = None,
        account_name: str = None,
        billing_commodity: main_models.DescribeDeductLogsResponseBodyDataBillingCommodity = None,
        billing_commodity_code: str = None,
        billing_commodity_name: str = None,
        billing_end_time: int = None,
        billing_instance_id: str = None,
        billing_price_field: main_models.DescribeDeductLogsResponseBodyDataBillingPriceField = None,
        billing_price_field_code: str = None,
        billing_price_field_name: str = None,
        billing_start_time: int = None,
        capacity_after_deduct_view_unit: str = None,
        capacity_after_deduct_view_value: str = None,
        capacity_before_deduct_view_unit: str = None,
        capacity_before_deduct_view_value: str = None,
        capacity_deducted_view_unit: str = None,
        capacity_deducted_view_value: str = None,
        capacity_type: main_models.DescribeDeductLogsResponseBodyDataCapacityType = None,
        capacity_type_code: str = None,
        capacity_type_name: str = None,
        commodity: main_models.DescribeDeductLogsResponseBodyDataCommodity = None,
        commodity_code: str = None,
        commodity_name: str = None,
        cycle_type: main_models.DescribeDeductLogsResponseBodyDataCycleType = None,
        cycle_type_code: str = None,
        cycle_type_name: str = None,
        deduct_time: int = None,
        factor: str = None,
        instance_belong_account_id: int = None,
        instance_belong_account_name: str = None,
        instance_id: str = None,
        measure_after_deduct_view_unit: str = None,
        measure_after_deduct_view_value: str = None,
        measure_before_deduct_view_unit: str = None,
        measure_before_deduct_view_value: str = None,
        measure_deducted_view_unit: str = None,
        measure_deducted_view_value: str = None,
        product: main_models.DescribeDeductLogsResponseBodyDataProduct = None,
        product_code: str = None,
        product_name: str = None,
        relation_account_id: int = None,
        relation_account_name: str = None,
        template: main_models.DescribeDeductLogsResponseBodyDataTemplate = None,
        template_code: str = None,
        template_name: str = None,
    ):
        # The account ID.
        self.account_id = account_id
        # The account name.
        self.account_name = account_name
        # The deducted commodity.
        self.billing_commodity = billing_commodity
        # The deducted commodity code.
        self.billing_commodity_code = billing_commodity_code
        # The deducted commodity name.
        self.billing_commodity_name = billing_commodity_name
        # The expiration time.
        self.billing_end_time = billing_end_time
        # The deduction instance.
        self.billing_instance_id = billing_instance_id
        # The deduction billable item.
        self.billing_price_field = billing_price_field
        # The deduction billable item code.
        self.billing_price_field_code = billing_price_field_code
        # The deduction billable item name.
        self.billing_price_field_name = billing_price_field_name
        # The effective period.
        self.billing_start_time = billing_start_time
        # The display unit of the capacity after deduction.
        self.capacity_after_deduct_view_unit = capacity_after_deduct_view_unit
        # The display value of the capacity after deduction.
        self.capacity_after_deduct_view_value = capacity_after_deduct_view_value
        # The display unit of the capacity before deduction.
        self.capacity_before_deduct_view_unit = capacity_before_deduct_view_unit
        # The display value of the capacity before deduction.
        self.capacity_before_deduct_view_value = capacity_before_deduct_view_value
        # The display unit of the deducted capacity.
        self.capacity_deducted_view_unit = capacity_deducted_view_unit
        # The display value of the deducted capacity.
        self.capacity_deducted_view_value = capacity_deducted_view_value
        # The capacity type.
        self.capacity_type = capacity_type
        # The capacity type code.
        self.capacity_type_code = capacity_type_code
        # The capacity type name.
        self.capacity_type_name = capacity_type_name
        # The commodity.
        self.commodity = commodity
        # The commodity code.
        self.commodity_code = commodity_code
        # The commodity name.
        self.commodity_name = commodity_name
        # The commitment cycle.
        self.cycle_type = cycle_type
        # The commitment cycle code.
        self.cycle_type_code = cycle_type_code
        # The commitment cycle name.
        self.cycle_type_name = cycle_type_name
        # The deduction time.
        self.deduct_time = deduct_time
        # The deduction factor.
        self.factor = factor
        # The ID of the account to which the instance belongs.
        self.instance_belong_account_id = instance_belong_account_id
        # The name of the account to which the instance belongs.
        self.instance_belong_account_name = instance_belong_account_name
        # The instance name.
        self.instance_id = instance_id
        # The display unit of the metering amount after deduction.
        self.measure_after_deduct_view_unit = measure_after_deduct_view_unit
        # The display value of the metering amount after deduction.
        self.measure_after_deduct_view_value = measure_after_deduct_view_value
        # The display unit of the metering amount before deduction.
        self.measure_before_deduct_view_unit = measure_before_deduct_view_unit
        # The display value of the metering amount before deduction.
        self.measure_before_deduct_view_value = measure_before_deduct_view_value
        # The display unit of the deducted metering amount.
        self.measure_deducted_view_unit = measure_deducted_view_unit
        # The display value of the deducted metering amount.
        self.measure_deducted_view_value = measure_deducted_view_value
        # The product.
        self.product = product
        # The product code.
        self.product_code = product_code
        # The product name.
        self.product_name = product_name
        # The deduction account ID.
        self.relation_account_id = relation_account_id
        # The deduction account name.
        self.relation_account_name = relation_account_name
        # The template.
        self.template = template
        # The template code.
        self.template_code = template_code
        # The template name.
        self.template_name = template_name

    def validate(self):
        if self.billing_commodity:
            self.billing_commodity.validate()
        if self.billing_price_field:
            self.billing_price_field.validate()
        if self.capacity_type:
            self.capacity_type.validate()
        if self.commodity:
            self.commodity.validate()
        if self.cycle_type:
            self.cycle_type.validate()
        if self.product:
            self.product.validate()
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

        if self.billing_commodity is not None:
            result['BillingCommodity'] = self.billing_commodity.to_map()

        if self.billing_commodity_code is not None:
            result['BillingCommodityCode'] = self.billing_commodity_code

        if self.billing_commodity_name is not None:
            result['BillingCommodityName'] = self.billing_commodity_name

        if self.billing_end_time is not None:
            result['BillingEndTime'] = self.billing_end_time

        if self.billing_instance_id is not None:
            result['BillingInstanceId'] = self.billing_instance_id

        if self.billing_price_field is not None:
            result['BillingPriceField'] = self.billing_price_field.to_map()

        if self.billing_price_field_code is not None:
            result['BillingPriceFieldCode'] = self.billing_price_field_code

        if self.billing_price_field_name is not None:
            result['BillingPriceFieldName'] = self.billing_price_field_name

        if self.billing_start_time is not None:
            result['BillingStartTime'] = self.billing_start_time

        if self.capacity_after_deduct_view_unit is not None:
            result['CapacityAfterDeductViewUnit'] = self.capacity_after_deduct_view_unit

        if self.capacity_after_deduct_view_value is not None:
            result['CapacityAfterDeductViewValue'] = self.capacity_after_deduct_view_value

        if self.capacity_before_deduct_view_unit is not None:
            result['CapacityBeforeDeductViewUnit'] = self.capacity_before_deduct_view_unit

        if self.capacity_before_deduct_view_value is not None:
            result['CapacityBeforeDeductViewValue'] = self.capacity_before_deduct_view_value

        if self.capacity_deducted_view_unit is not None:
            result['CapacityDeductedViewUnit'] = self.capacity_deducted_view_unit

        if self.capacity_deducted_view_value is not None:
            result['CapacityDeductedViewValue'] = self.capacity_deducted_view_value

        if self.capacity_type is not None:
            result['CapacityType'] = self.capacity_type.to_map()

        if self.capacity_type_code is not None:
            result['CapacityTypeCode'] = self.capacity_type_code

        if self.capacity_type_name is not None:
            result['CapacityTypeName'] = self.capacity_type_name

        if self.commodity is not None:
            result['Commodity'] = self.commodity.to_map()

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.commodity_name is not None:
            result['CommodityName'] = self.commodity_name

        if self.cycle_type is not None:
            result['CycleType'] = self.cycle_type.to_map()

        if self.cycle_type_code is not None:
            result['CycleTypeCode'] = self.cycle_type_code

        if self.cycle_type_name is not None:
            result['CycleTypeName'] = self.cycle_type_name

        if self.deduct_time is not None:
            result['DeductTime'] = self.deduct_time

        if self.factor is not None:
            result['Factor'] = self.factor

        if self.instance_belong_account_id is not None:
            result['InstanceBelongAccountId'] = self.instance_belong_account_id

        if self.instance_belong_account_name is not None:
            result['InstanceBelongAccountName'] = self.instance_belong_account_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.measure_after_deduct_view_unit is not None:
            result['MeasureAfterDeductViewUnit'] = self.measure_after_deduct_view_unit

        if self.measure_after_deduct_view_value is not None:
            result['MeasureAfterDeductViewValue'] = self.measure_after_deduct_view_value

        if self.measure_before_deduct_view_unit is not None:
            result['MeasureBeforeDeductViewUnit'] = self.measure_before_deduct_view_unit

        if self.measure_before_deduct_view_value is not None:
            result['MeasureBeforeDeductViewValue'] = self.measure_before_deduct_view_value

        if self.measure_deducted_view_unit is not None:
            result['MeasureDeductedViewUnit'] = self.measure_deducted_view_unit

        if self.measure_deducted_view_value is not None:
            result['MeasureDeductedViewValue'] = self.measure_deducted_view_value

        if self.product is not None:
            result['Product'] = self.product.to_map()

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_name is not None:
            result['ProductName'] = self.product_name

        if self.relation_account_id is not None:
            result['RelationAccountId'] = self.relation_account_id

        if self.relation_account_name is not None:
            result['RelationAccountName'] = self.relation_account_name

        if self.template is not None:
            result['Template'] = self.template.to_map()

        if self.template_code is not None:
            result['TemplateCode'] = self.template_code

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('BillingCommodity') is not None:
            temp_model = main_models.DescribeDeductLogsResponseBodyDataBillingCommodity()
            self.billing_commodity = temp_model.from_map(m.get('BillingCommodity'))

        if m.get('BillingCommodityCode') is not None:
            self.billing_commodity_code = m.get('BillingCommodityCode')

        if m.get('BillingCommodityName') is not None:
            self.billing_commodity_name = m.get('BillingCommodityName')

        if m.get('BillingEndTime') is not None:
            self.billing_end_time = m.get('BillingEndTime')

        if m.get('BillingInstanceId') is not None:
            self.billing_instance_id = m.get('BillingInstanceId')

        if m.get('BillingPriceField') is not None:
            temp_model = main_models.DescribeDeductLogsResponseBodyDataBillingPriceField()
            self.billing_price_field = temp_model.from_map(m.get('BillingPriceField'))

        if m.get('BillingPriceFieldCode') is not None:
            self.billing_price_field_code = m.get('BillingPriceFieldCode')

        if m.get('BillingPriceFieldName') is not None:
            self.billing_price_field_name = m.get('BillingPriceFieldName')

        if m.get('BillingStartTime') is not None:
            self.billing_start_time = m.get('BillingStartTime')

        if m.get('CapacityAfterDeductViewUnit') is not None:
            self.capacity_after_deduct_view_unit = m.get('CapacityAfterDeductViewUnit')

        if m.get('CapacityAfterDeductViewValue') is not None:
            self.capacity_after_deduct_view_value = m.get('CapacityAfterDeductViewValue')

        if m.get('CapacityBeforeDeductViewUnit') is not None:
            self.capacity_before_deduct_view_unit = m.get('CapacityBeforeDeductViewUnit')

        if m.get('CapacityBeforeDeductViewValue') is not None:
            self.capacity_before_deduct_view_value = m.get('CapacityBeforeDeductViewValue')

        if m.get('CapacityDeductedViewUnit') is not None:
            self.capacity_deducted_view_unit = m.get('CapacityDeductedViewUnit')

        if m.get('CapacityDeductedViewValue') is not None:
            self.capacity_deducted_view_value = m.get('CapacityDeductedViewValue')

        if m.get('CapacityType') is not None:
            temp_model = main_models.DescribeDeductLogsResponseBodyDataCapacityType()
            self.capacity_type = temp_model.from_map(m.get('CapacityType'))

        if m.get('CapacityTypeCode') is not None:
            self.capacity_type_code = m.get('CapacityTypeCode')

        if m.get('CapacityTypeName') is not None:
            self.capacity_type_name = m.get('CapacityTypeName')

        if m.get('Commodity') is not None:
            temp_model = main_models.DescribeDeductLogsResponseBodyDataCommodity()
            self.commodity = temp_model.from_map(m.get('Commodity'))

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('CommodityName') is not None:
            self.commodity_name = m.get('CommodityName')

        if m.get('CycleType') is not None:
            temp_model = main_models.DescribeDeductLogsResponseBodyDataCycleType()
            self.cycle_type = temp_model.from_map(m.get('CycleType'))

        if m.get('CycleTypeCode') is not None:
            self.cycle_type_code = m.get('CycleTypeCode')

        if m.get('CycleTypeName') is not None:
            self.cycle_type_name = m.get('CycleTypeName')

        if m.get('DeductTime') is not None:
            self.deduct_time = m.get('DeductTime')

        if m.get('Factor') is not None:
            self.factor = m.get('Factor')

        if m.get('InstanceBelongAccountId') is not None:
            self.instance_belong_account_id = m.get('InstanceBelongAccountId')

        if m.get('InstanceBelongAccountName') is not None:
            self.instance_belong_account_name = m.get('InstanceBelongAccountName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MeasureAfterDeductViewUnit') is not None:
            self.measure_after_deduct_view_unit = m.get('MeasureAfterDeductViewUnit')

        if m.get('MeasureAfterDeductViewValue') is not None:
            self.measure_after_deduct_view_value = m.get('MeasureAfterDeductViewValue')

        if m.get('MeasureBeforeDeductViewUnit') is not None:
            self.measure_before_deduct_view_unit = m.get('MeasureBeforeDeductViewUnit')

        if m.get('MeasureBeforeDeductViewValue') is not None:
            self.measure_before_deduct_view_value = m.get('MeasureBeforeDeductViewValue')

        if m.get('MeasureDeductedViewUnit') is not None:
            self.measure_deducted_view_unit = m.get('MeasureDeductedViewUnit')

        if m.get('MeasureDeductedViewValue') is not None:
            self.measure_deducted_view_value = m.get('MeasureDeductedViewValue')

        if m.get('Product') is not None:
            temp_model = main_models.DescribeDeductLogsResponseBodyDataProduct()
            self.product = temp_model.from_map(m.get('Product'))

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')

        if m.get('RelationAccountId') is not None:
            self.relation_account_id = m.get('RelationAccountId')

        if m.get('RelationAccountName') is not None:
            self.relation_account_name = m.get('RelationAccountName')

        if m.get('Template') is not None:
            temp_model = main_models.DescribeDeductLogsResponseBodyDataTemplate()
            self.template = temp_model.from_map(m.get('Template'))

        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        return self

class DescribeDeductLogsResponseBodyDataTemplate(DaraModel):
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

class DescribeDeductLogsResponseBodyDataProduct(DaraModel):
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

class DescribeDeductLogsResponseBodyDataCycleType(DaraModel):
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

class DescribeDeductLogsResponseBodyDataCommodity(DaraModel):
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

class DescribeDeductLogsResponseBodyDataCapacityType(DaraModel):
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

class DescribeDeductLogsResponseBodyDataBillingPriceField(DaraModel):
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

class DescribeDeductLogsResponseBodyDataBillingCommodity(DaraModel):
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

