# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_market20151101 import models as main_models
from darabonba.model import DaraModel

class DescribeProductResponseBody(DaraModel):
    def __init__(
        self,
        audit_fail_msg: str = None,
        audit_status: str = None,
        audit_time: int = None,
        code: str = None,
        description: str = None,
        front_category_id: int = None,
        gmt_created: int = None,
        gmt_modified: int = None,
        name: str = None,
        pic_url: str = None,
        product_extras: main_models.DescribeProductResponseBodyProductExtras = None,
        product_skus: main_models.DescribeProductResponseBodyProductSkus = None,
        request_id: str = None,
        score: float = None,
        shop_info: main_models.DescribeProductResponseBodyShopInfo = None,
        short_description: str = None,
        status: str = None,
        supplier_pk: int = None,
        type: str = None,
        use_count: int = None,
    ):
        self.audit_fail_msg = audit_fail_msg
        self.audit_status = audit_status
        self.audit_time = audit_time
        self.code = code
        self.description = description
        self.front_category_id = front_category_id
        self.gmt_created = gmt_created
        self.gmt_modified = gmt_modified
        self.name = name
        self.pic_url = pic_url
        self.product_extras = product_extras
        self.product_skus = product_skus
        self.request_id = request_id
        self.score = score
        self.shop_info = shop_info
        self.short_description = short_description
        self.status = status
        self.supplier_pk = supplier_pk
        self.type = type
        self.use_count = use_count

    def validate(self):
        if self.product_extras:
            self.product_extras.validate()
        if self.product_skus:
            self.product_skus.validate()
        if self.shop_info:
            self.shop_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit_fail_msg is not None:
            result['AuditFailMsg'] = self.audit_fail_msg

        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status

        if self.audit_time is not None:
            result['AuditTime'] = self.audit_time

        if self.code is not None:
            result['Code'] = self.code

        if self.description is not None:
            result['Description'] = self.description

        if self.front_category_id is not None:
            result['FrontCategoryId'] = self.front_category_id

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.name is not None:
            result['Name'] = self.name

        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url

        if self.product_extras is not None:
            result['ProductExtras'] = self.product_extras.to_map()

        if self.product_skus is not None:
            result['ProductSkus'] = self.product_skus.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.score is not None:
            result['Score'] = self.score

        if self.shop_info is not None:
            result['ShopInfo'] = self.shop_info.to_map()

        if self.short_description is not None:
            result['ShortDescription'] = self.short_description

        if self.status is not None:
            result['Status'] = self.status

        if self.supplier_pk is not None:
            result['SupplierPk'] = self.supplier_pk

        if self.type is not None:
            result['Type'] = self.type

        if self.use_count is not None:
            result['UseCount'] = self.use_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditFailMsg') is not None:
            self.audit_fail_msg = m.get('AuditFailMsg')

        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')

        if m.get('AuditTime') is not None:
            self.audit_time = m.get('AuditTime')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FrontCategoryId') is not None:
            self.front_category_id = m.get('FrontCategoryId')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')

        if m.get('ProductExtras') is not None:
            temp_model = main_models.DescribeProductResponseBodyProductExtras()
            self.product_extras = temp_model.from_map(m.get('ProductExtras'))

        if m.get('ProductSkus') is not None:
            temp_model = main_models.DescribeProductResponseBodyProductSkus()
            self.product_skus = temp_model.from_map(m.get('ProductSkus'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('ShopInfo') is not None:
            temp_model = main_models.DescribeProductResponseBodyShopInfo()
            self.shop_info = temp_model.from_map(m.get('ShopInfo'))

        if m.get('ShortDescription') is not None:
            self.short_description = m.get('ShortDescription')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SupplierPk') is not None:
            self.supplier_pk = m.get('SupplierPk')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UseCount') is not None:
            self.use_count = m.get('UseCount')

        return self

class DescribeProductResponseBodyShopInfo(DaraModel):
    def __init__(
        self,
        emails: str = None,
        id: int = None,
        name: str = None,
        telephones: main_models.DescribeProductResponseBodyShopInfoTelephones = None,
        wang_wangs: main_models.DescribeProductResponseBodyShopInfoWangWangs = None,
    ):
        self.emails = emails
        self.id = id
        self.name = name
        self.telephones = telephones
        self.wang_wangs = wang_wangs

    def validate(self):
        if self.telephones:
            self.telephones.validate()
        if self.wang_wangs:
            self.wang_wangs.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.emails is not None:
            result['Emails'] = self.emails

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.telephones is not None:
            result['Telephones'] = self.telephones.to_map()

        if self.wang_wangs is not None:
            result['WangWangs'] = self.wang_wangs.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Emails') is not None:
            self.emails = m.get('Emails')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Telephones') is not None:
            temp_model = main_models.DescribeProductResponseBodyShopInfoTelephones()
            self.telephones = temp_model.from_map(m.get('Telephones'))

        if m.get('WangWangs') is not None:
            temp_model = main_models.DescribeProductResponseBodyShopInfoWangWangs()
            self.wang_wangs = temp_model.from_map(m.get('WangWangs'))

        return self

class DescribeProductResponseBodyShopInfoWangWangs(DaraModel):
    def __init__(
        self,
        wang_wang: List[main_models.DescribeProductResponseBodyShopInfoWangWangsWangWang] = None,
    ):
        self.wang_wang = wang_wang

    def validate(self):
        if self.wang_wang:
            for v1 in self.wang_wang:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['WangWang'] = []
        if self.wang_wang is not None:
            for k1 in self.wang_wang:
                result['WangWang'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.wang_wang = []
        if m.get('WangWang') is not None:
            for k1 in m.get('WangWang'):
                temp_model = main_models.DescribeProductResponseBodyShopInfoWangWangsWangWang()
                self.wang_wang.append(temp_model.from_map(k1))

        return self

class DescribeProductResponseBodyShopInfoWangWangsWangWang(DaraModel):
    def __init__(
        self,
        remark: str = None,
        user_name: str = None,
    ):
        self.remark = remark
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.remark is not None:
            result['Remark'] = self.remark

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

class DescribeProductResponseBodyShopInfoTelephones(DaraModel):
    def __init__(
        self,
        telephone: List[str] = None,
    ):
        self.telephone = telephone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.telephone is not None:
            result['Telephone'] = self.telephone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Telephone') is not None:
            self.telephone = m.get('Telephone')

        return self

class DescribeProductResponseBodyProductSkus(DaraModel):
    def __init__(
        self,
        product_sku: List[main_models.DescribeProductResponseBodyProductSkusProductSku] = None,
    ):
        self.product_sku = product_sku

    def validate(self):
        if self.product_sku:
            for v1 in self.product_sku:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ProductSku'] = []
        if self.product_sku is not None:
            for k1 in self.product_sku:
                result['ProductSku'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.product_sku = []
        if m.get('ProductSku') is not None:
            for k1 in m.get('ProductSku'):
                temp_model = main_models.DescribeProductResponseBodyProductSkusProductSku()
                self.product_sku.append(temp_model.from_map(k1))

        return self

class DescribeProductResponseBodyProductSkusProductSku(DaraModel):
    def __init__(
        self,
        charge_type: str = None,
        code: str = None,
        constraints: str = None,
        hidden: bool = None,
        modules: main_models.DescribeProductResponseBodyProductSkusProductSkuModules = None,
        name: str = None,
        order_periods: main_models.DescribeProductResponseBodyProductSkusProductSkuOrderPeriods = None,
    ):
        self.charge_type = charge_type
        self.code = code
        self.constraints = constraints
        self.hidden = hidden
        self.modules = modules
        self.name = name
        self.order_periods = order_periods

    def validate(self):
        if self.modules:
            self.modules.validate()
        if self.order_periods:
            self.order_periods.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.code is not None:
            result['Code'] = self.code

        if self.constraints is not None:
            result['Constraints'] = self.constraints

        if self.hidden is not None:
            result['Hidden'] = self.hidden

        if self.modules is not None:
            result['Modules'] = self.modules.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.order_periods is not None:
            result['OrderPeriods'] = self.order_periods.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Constraints') is not None:
            self.constraints = m.get('Constraints')

        if m.get('Hidden') is not None:
            self.hidden = m.get('Hidden')

        if m.get('Modules') is not None:
            temp_model = main_models.DescribeProductResponseBodyProductSkusProductSkuModules()
            self.modules = temp_model.from_map(m.get('Modules'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OrderPeriods') is not None:
            temp_model = main_models.DescribeProductResponseBodyProductSkusProductSkuOrderPeriods()
            self.order_periods = temp_model.from_map(m.get('OrderPeriods'))

        return self

class DescribeProductResponseBodyProductSkusProductSkuOrderPeriods(DaraModel):
    def __init__(
        self,
        order_period: List[main_models.DescribeProductResponseBodyProductSkusProductSkuOrderPeriodsOrderPeriod] = None,
    ):
        self.order_period = order_period

    def validate(self):
        if self.order_period:
            for v1 in self.order_period:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['OrderPeriod'] = []
        if self.order_period is not None:
            for k1 in self.order_period:
                result['OrderPeriod'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.order_period = []
        if m.get('OrderPeriod') is not None:
            for k1 in m.get('OrderPeriod'):
                temp_model = main_models.DescribeProductResponseBodyProductSkusProductSkuOrderPeriodsOrderPeriod()
                self.order_period.append(temp_model.from_map(k1))

        return self

class DescribeProductResponseBodyProductSkusProductSkuOrderPeriodsOrderPeriod(DaraModel):
    def __init__(
        self,
        name: str = None,
        period_type: str = None,
    ):
        self.name = name
        self.period_type = period_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.period_type is not None:
            result['PeriodType'] = self.period_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PeriodType') is not None:
            self.period_type = m.get('PeriodType')

        return self

class DescribeProductResponseBodyProductSkusProductSkuModules(DaraModel):
    def __init__(
        self,
        module: List[main_models.DescribeProductResponseBodyProductSkusProductSkuModulesModule] = None,
    ):
        self.module = module

    def validate(self):
        if self.module:
            for v1 in self.module:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Module'] = []
        if self.module is not None:
            for k1 in self.module:
                result['Module'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.module = []
        if m.get('Module') is not None:
            for k1 in m.get('Module'):
                temp_model = main_models.DescribeProductResponseBodyProductSkusProductSkuModulesModule()
                self.module.append(temp_model.from_map(k1))

        return self

class DescribeProductResponseBodyProductSkusProductSkuModulesModule(DaraModel):
    def __init__(
        self,
        code: str = None,
        id: str = None,
        name: str = None,
        properties: main_models.DescribeProductResponseBodyProductSkusProductSkuModulesModuleProperties = None,
    ):
        self.code = code
        self.id = id
        self.name = name
        self.properties = properties

    def validate(self):
        if self.properties:
            self.properties.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.properties is not None:
            result['Properties'] = self.properties.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Properties') is not None:
            temp_model = main_models.DescribeProductResponseBodyProductSkusProductSkuModulesModuleProperties()
            self.properties = temp_model.from_map(m.get('Properties'))

        return self

class DescribeProductResponseBodyProductSkusProductSkuModulesModuleProperties(DaraModel):
    def __init__(
        self,
        property: List[main_models.DescribeProductResponseBodyProductSkusProductSkuModulesModulePropertiesProperty] = None,
    ):
        self.property = property

    def validate(self):
        if self.property:
            for v1 in self.property:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Property'] = []
        if self.property is not None:
            for k1 in self.property:
                result['Property'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.property = []
        if m.get('Property') is not None:
            for k1 in m.get('Property'):
                temp_model = main_models.DescribeProductResponseBodyProductSkusProductSkuModulesModulePropertiesProperty()
                self.property.append(temp_model.from_map(k1))

        return self

class DescribeProductResponseBodyProductSkusProductSkuModulesModulePropertiesProperty(DaraModel):
    def __init__(
        self,
        display_unit: str = None,
        key: str = None,
        name: str = None,
        property_values: main_models.DescribeProductResponseBodyProductSkusProductSkuModulesModulePropertiesPropertyPropertyValues = None,
        show_type: str = None,
    ):
        self.display_unit = display_unit
        self.key = key
        self.name = name
        self.property_values = property_values
        self.show_type = show_type

    def validate(self):
        if self.property_values:
            self.property_values.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_unit is not None:
            result['DisplayUnit'] = self.display_unit

        if self.key is not None:
            result['Key'] = self.key

        if self.name is not None:
            result['Name'] = self.name

        if self.property_values is not None:
            result['PropertyValues'] = self.property_values.to_map()

        if self.show_type is not None:
            result['ShowType'] = self.show_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayUnit') is not None:
            self.display_unit = m.get('DisplayUnit')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PropertyValues') is not None:
            temp_model = main_models.DescribeProductResponseBodyProductSkusProductSkuModulesModulePropertiesPropertyPropertyValues()
            self.property_values = temp_model.from_map(m.get('PropertyValues'))

        if m.get('ShowType') is not None:
            self.show_type = m.get('ShowType')

        return self

class DescribeProductResponseBodyProductSkusProductSkuModulesModulePropertiesPropertyPropertyValues(DaraModel):
    def __init__(
        self,
        property_value: List[main_models.DescribeProductResponseBodyProductSkusProductSkuModulesModulePropertiesPropertyPropertyValuesPropertyValue] = None,
    ):
        self.property_value = property_value

    def validate(self):
        if self.property_value:
            for v1 in self.property_value:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PropertyValue'] = []
        if self.property_value is not None:
            for k1 in self.property_value:
                result['PropertyValue'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.property_value = []
        if m.get('PropertyValue') is not None:
            for k1 in m.get('PropertyValue'):
                temp_model = main_models.DescribeProductResponseBodyProductSkusProductSkuModulesModulePropertiesPropertyPropertyValuesPropertyValue()
                self.property_value.append(temp_model.from_map(k1))

        return self

class DescribeProductResponseBodyProductSkusProductSkuModulesModulePropertiesPropertyPropertyValuesPropertyValue(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        max: str = None,
        min: str = None,
        remark: str = None,
        step: str = None,
        type: str = None,
        value: str = None,
    ):
        self.display_name = display_name
        self.max = max
        self.min = min
        self.remark = remark
        self.step = step
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.max is not None:
            result['Max'] = self.max

        if self.min is not None:
            result['Min'] = self.min

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.step is not None:
            result['Step'] = self.step

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Max') is not None:
            self.max = m.get('Max')

        if m.get('Min') is not None:
            self.min = m.get('Min')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('Step') is not None:
            self.step = m.get('Step')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeProductResponseBodyProductExtras(DaraModel):
    def __init__(
        self,
        product_extra: List[main_models.DescribeProductResponseBodyProductExtrasProductExtra] = None,
    ):
        self.product_extra = product_extra

    def validate(self):
        if self.product_extra:
            for v1 in self.product_extra:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ProductExtra'] = []
        if self.product_extra is not None:
            for k1 in self.product_extra:
                result['ProductExtra'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.product_extra = []
        if m.get('ProductExtra') is not None:
            for k1 in m.get('ProductExtra'):
                temp_model = main_models.DescribeProductResponseBodyProductExtrasProductExtra()
                self.product_extra.append(temp_model.from_map(k1))

        return self

class DescribeProductResponseBodyProductExtrasProductExtra(DaraModel):
    def __init__(
        self,
        key: str = None,
        label: str = None,
        order: int = None,
        type: str = None,
        values: str = None,
    ):
        self.key = key
        self.label = label
        self.order = order
        self.type = type
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.label is not None:
            result['Label'] = self.label

        if self.order is not None:
            result['Order'] = self.order

        if self.type is not None:
            result['Type'] = self.type

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

