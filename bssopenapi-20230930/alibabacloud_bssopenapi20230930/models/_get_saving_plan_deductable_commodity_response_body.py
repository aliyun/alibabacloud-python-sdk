# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_bssopenapi20230930 import models as main_models
from darabonba.model import DaraModel

class GetSavingPlanDeductableCommodityResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.GetSavingPlanDeductableCommodityResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetSavingPlanDeductableCommodityResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetSavingPlanDeductableCommodityResponseBodyData(DaraModel):
    def __init__(
        self,
        activity_id: int = None,
        commodity_code: str = None,
        commodity_id: int = None,
        commodity_name: str = None,
        cycle_list: List[main_models.GetSavingPlanDeductableCommodityResponseBodyDataCycleList] = None,
        filter_modules: List[main_models.GetSavingPlanDeductableCommodityResponseBodyDataFilterModules] = None,
        item_code: str = None,
        item_id: int = None,
        item_name: str = None,
        module_map_list: List[main_models.GetSavingPlanDeductableCommodityResponseBodyDataModuleMapList] = None,
        pay_mode_list: List[main_models.GetSavingPlanDeductableCommodityResponseBodyDataPayModeList] = None,
        pricing_modules: List[main_models.GetSavingPlanDeductableCommodityResponseBodyDataPricingModules] = None,
        spn_commodity_code: str = None,
        spn_commodity_name: str = None,
        spn_discount_config_type: str = None,
        step_price_map: Dict[str, List[main_models.DataStepPriceMapValue]] = None,
    ):
        self.activity_id = activity_id
        self.commodity_code = commodity_code
        self.commodity_id = commodity_id
        self.commodity_name = commodity_name
        self.cycle_list = cycle_list
        self.filter_modules = filter_modules
        self.item_code = item_code
        self.item_id = item_id
        self.item_name = item_name
        self.module_map_list = module_map_list
        self.pay_mode_list = pay_mode_list
        self.pricing_modules = pricing_modules
        self.spn_commodity_code = spn_commodity_code
        self.spn_commodity_name = spn_commodity_name
        self.spn_discount_config_type = spn_discount_config_type
        self.step_price_map = step_price_map

    def validate(self):
        if self.cycle_list:
            for v1 in self.cycle_list:
                 if v1:
                    v1.validate()
        if self.filter_modules:
            for v1 in self.filter_modules:
                 if v1:
                    v1.validate()
        if self.module_map_list:
            for v1 in self.module_map_list:
                 if v1:
                    v1.validate()
        if self.pay_mode_list:
            for v1 in self.pay_mode_list:
                 if v1:
                    v1.validate()
        if self.pricing_modules:
            for v1 in self.pricing_modules:
                 if v1:
                    v1.validate()
        if self.step_price_map:
            for v1 in self.step_price_map.values():
                for v2 in v1:
                     if v2:
                        v2.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activity_id is not None:
            result['ActivityId'] = self.activity_id

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.commodity_id is not None:
            result['CommodityId'] = self.commodity_id

        if self.commodity_name is not None:
            result['CommodityName'] = self.commodity_name

        result['CycleList'] = []
        if self.cycle_list is not None:
            for k1 in self.cycle_list:
                result['CycleList'].append(k1.to_map() if k1 else None)

        result['FilterModules'] = []
        if self.filter_modules is not None:
            for k1 in self.filter_modules:
                result['FilterModules'].append(k1.to_map() if k1 else None)

        if self.item_code is not None:
            result['ItemCode'] = self.item_code

        if self.item_id is not None:
            result['ItemId'] = self.item_id

        if self.item_name is not None:
            result['ItemName'] = self.item_name

        result['ModuleMapList'] = []
        if self.module_map_list is not None:
            for k1 in self.module_map_list:
                result['ModuleMapList'].append(k1.to_map() if k1 else None)

        result['PayModeList'] = []
        if self.pay_mode_list is not None:
            for k1 in self.pay_mode_list:
                result['PayModeList'].append(k1.to_map() if k1 else None)

        result['PricingModules'] = []
        if self.pricing_modules is not None:
            for k1 in self.pricing_modules:
                result['PricingModules'].append(k1.to_map() if k1 else None)

        if self.spn_commodity_code is not None:
            result['SpnCommodityCode'] = self.spn_commodity_code

        if self.spn_commodity_name is not None:
            result['SpnCommodityName'] = self.spn_commodity_name

        if self.spn_discount_config_type is not None:
            result['SpnDiscountConfigType'] = self.spn_discount_config_type

        result['StepPriceMap'] = {}
        if self.step_price_map is not None:
            for k1, v1 in self.step_price_map.items():
                l1 = []
                for k2 in v1:
                    l1.append(k2.to_map() if k2 else None)
                result['StepPriceMap'][k1] = l1

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityId') is not None:
            self.activity_id = m.get('ActivityId')

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('CommodityId') is not None:
            self.commodity_id = m.get('CommodityId')

        if m.get('CommodityName') is not None:
            self.commodity_name = m.get('CommodityName')

        self.cycle_list = []
        if m.get('CycleList') is not None:
            for k1 in m.get('CycleList'):
                temp_model = main_models.GetSavingPlanDeductableCommodityResponseBodyDataCycleList()
                self.cycle_list.append(temp_model.from_map(k1))

        self.filter_modules = []
        if m.get('FilterModules') is not None:
            for k1 in m.get('FilterModules'):
                temp_model = main_models.GetSavingPlanDeductableCommodityResponseBodyDataFilterModules()
                self.filter_modules.append(temp_model.from_map(k1))

        if m.get('ItemCode') is not None:
            self.item_code = m.get('ItemCode')

        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')

        if m.get('ItemName') is not None:
            self.item_name = m.get('ItemName')

        self.module_map_list = []
        if m.get('ModuleMapList') is not None:
            for k1 in m.get('ModuleMapList'):
                temp_model = main_models.GetSavingPlanDeductableCommodityResponseBodyDataModuleMapList()
                self.module_map_list.append(temp_model.from_map(k1))

        self.pay_mode_list = []
        if m.get('PayModeList') is not None:
            for k1 in m.get('PayModeList'):
                temp_model = main_models.GetSavingPlanDeductableCommodityResponseBodyDataPayModeList()
                self.pay_mode_list.append(temp_model.from_map(k1))

        self.pricing_modules = []
        if m.get('PricingModules') is not None:
            for k1 in m.get('PricingModules'):
                temp_model = main_models.GetSavingPlanDeductableCommodityResponseBodyDataPricingModules()
                self.pricing_modules.append(temp_model.from_map(k1))

        if m.get('SpnCommodityCode') is not None:
            self.spn_commodity_code = m.get('SpnCommodityCode')

        if m.get('SpnCommodityName') is not None:
            self.spn_commodity_name = m.get('SpnCommodityName')

        if m.get('SpnDiscountConfigType') is not None:
            self.spn_discount_config_type = m.get('SpnDiscountConfigType')

        self.step_price_map = {}
        if m.get('StepPriceMap') is not None:
            for k1, v1 in m.get('StepPriceMap').items():
                l1 = []
                for k2 in v1:
                    temp_model = main_models.DataStepPriceMapValue()
                    l1.append(temp_model.from_map(k2))
                self.step_price_map[k1] = l1

        return self

class GetSavingPlanDeductableCommodityResponseBodyDataPricingModules(DaraModel):
    def __init__(
        self,
        module_code: str = None,
        module_id: int = None,
        module_name: str = None,
    ):
        self.module_code = module_code
        self.module_id = module_id
        self.module_name = module_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.module_code is not None:
            result['ModuleCode'] = self.module_code

        if self.module_id is not None:
            result['ModuleId'] = self.module_id

        if self.module_name is not None:
            result['ModuleName'] = self.module_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModuleCode') is not None:
            self.module_code = m.get('ModuleCode')

        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')

        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')

        return self

class GetSavingPlanDeductableCommodityResponseBodyDataPayModeList(DaraModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
    ):
        self.code = code
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

class GetSavingPlanDeductableCommodityResponseBodyDataModuleMapList(DaraModel):
    def __init__(
        self,
        filter_modules: List[main_models.GetSavingPlanDeductableCommodityResponseBodyDataModuleMapListFilterModules] = None,
        module_code: str = None,
        module_id: int = None,
        module_name: str = None,
        show_modules: List[main_models.GetSavingPlanDeductableCommodityResponseBodyDataModuleMapListShowModules] = None,
        spn_type_list: List[str] = None,
        spn_type_map_list: List[Dict[str, main_models.DataModuleMapListSpnTypeMapListValue]] = None,
        spn_type_name_list: List[main_models.GetSavingPlanDeductableCommodityResponseBodyDataModuleMapListSpnTypeNameList] = None,
    ):
        self.filter_modules = filter_modules
        self.module_code = module_code
        self.module_id = module_id
        self.module_name = module_name
        self.show_modules = show_modules
        self.spn_type_list = spn_type_list
        self.spn_type_map_list = spn_type_map_list
        self.spn_type_name_list = spn_type_name_list

    def validate(self):
        if self.filter_modules:
            for v1 in self.filter_modules:
                 if v1:
                    v1.validate()
        if self.show_modules:
            for v1 in self.show_modules:
                 if v1:
                    v1.validate()
        if self.spn_type_map_list:
            for v1 in self.spn_type_map_list:
                for v2 in self.spn_type_map_list.values():
                     if v2:
                        v2.validate()
        if self.spn_type_name_list:
            for v1 in self.spn_type_name_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FilterModules'] = []
        if self.filter_modules is not None:
            for k1 in self.filter_modules:
                result['FilterModules'].append(k1.to_map() if k1 else None)

        if self.module_code is not None:
            result['ModuleCode'] = self.module_code

        if self.module_id is not None:
            result['ModuleId'] = self.module_id

        if self.module_name is not None:
            result['ModuleName'] = self.module_name

        result['ShowModules'] = []
        if self.show_modules is not None:
            for k1 in self.show_modules:
                result['ShowModules'].append(k1.to_map() if k1 else None)

        if self.spn_type_list is not None:
            result['SpnTypeList'] = self.spn_type_list

        result['SpnTypeMapList'] = []
        if self.spn_type_map_list is not None:
            for k1 in self.spn_type_map_list:
                d1 = {}
                for k2, v2 in self.spn_type_map_list.items():
                    d1[k2] = v2.to_map() if v2 else None
                result['SpnTypeMapList'].append(d1)

        result['SpnTypeNameList'] = []
        if self.spn_type_name_list is not None:
            for k1 in self.spn_type_name_list:
                result['SpnTypeNameList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filter_modules = []
        if m.get('FilterModules') is not None:
            for k1 in m.get('FilterModules'):
                temp_model = main_models.GetSavingPlanDeductableCommodityResponseBodyDataModuleMapListFilterModules()
                self.filter_modules.append(temp_model.from_map(k1))

        if m.get('ModuleCode') is not None:
            self.module_code = m.get('ModuleCode')

        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')

        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')

        self.show_modules = []
        if m.get('ShowModules') is not None:
            for k1 in m.get('ShowModules'):
                temp_model = main_models.GetSavingPlanDeductableCommodityResponseBodyDataModuleMapListShowModules()
                self.show_modules.append(temp_model.from_map(k1))

        if m.get('SpnTypeList') is not None:
            self.spn_type_list = m.get('SpnTypeList')

        self.spn_type_map_list = []
        if m.get('SpnTypeMapList') is not None:
            for k1 in m.get('SpnTypeMapList'):
                d1 = {}
                for k2, v2 in k1.items():
                    temp_model = main_models.DataModuleMapListSpnTypeMapListValue()
                    d1[k2] = temp_model.from_map(v2)
                self.spn_type_map_list.append(d1)

        self.spn_type_name_list = []
        if m.get('SpnTypeNameList') is not None:
            for k1 in m.get('SpnTypeNameList'):
                temp_model = main_models.GetSavingPlanDeductableCommodityResponseBodyDataModuleMapListSpnTypeNameList()
                self.spn_type_name_list.append(temp_model.from_map(k1))

        return self

class GetSavingPlanDeductableCommodityResponseBodyDataModuleMapListSpnTypeNameList(DaraModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
    ):
        self.code = code
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

class GetSavingPlanDeductableCommodityResponseBodyDataModuleMapListShowModules(DaraModel):
    def __init__(
        self,
        module_code: str = None,
        module_id: int = None,
        module_name: str = None,
    ):
        self.module_code = module_code
        self.module_id = module_id
        self.module_name = module_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.module_code is not None:
            result['ModuleCode'] = self.module_code

        if self.module_id is not None:
            result['ModuleId'] = self.module_id

        if self.module_name is not None:
            result['ModuleName'] = self.module_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModuleCode') is not None:
            self.module_code = m.get('ModuleCode')

        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')

        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')

        return self

class GetSavingPlanDeductableCommodityResponseBodyDataModuleMapListFilterModules(DaraModel):
    def __init__(
        self,
        module_code: str = None,
        module_id: int = None,
        module_name: str = None,
    ):
        self.module_code = module_code
        self.module_id = module_id
        self.module_name = module_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.module_code is not None:
            result['ModuleCode'] = self.module_code

        if self.module_id is not None:
            result['ModuleId'] = self.module_id

        if self.module_name is not None:
            result['ModuleName'] = self.module_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModuleCode') is not None:
            self.module_code = m.get('ModuleCode')

        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')

        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')

        return self

class GetSavingPlanDeductableCommodityResponseBodyDataFilterModules(DaraModel):
    def __init__(
        self,
        module_code: str = None,
        module_id: int = None,
        module_name: str = None,
    ):
        self.module_code = module_code
        self.module_id = module_id
        self.module_name = module_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.module_code is not None:
            result['ModuleCode'] = self.module_code

        if self.module_id is not None:
            result['ModuleId'] = self.module_id

        if self.module_name is not None:
            result['ModuleName'] = self.module_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModuleCode') is not None:
            self.module_code = m.get('ModuleCode')

        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')

        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')

        return self

class GetSavingPlanDeductableCommodityResponseBodyDataCycleList(DaraModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
    ):
        self.code = code
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

