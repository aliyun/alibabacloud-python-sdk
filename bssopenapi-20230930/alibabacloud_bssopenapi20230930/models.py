# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class DataModuleMapListSpnTypeMapListValueFilterModules(TeaModel):
    def __init__(
        self,
        module_id: int = None,
        module_code: str = None,
        module_name: str = None,
    ):
        self.module_id = module_id
        self.module_code = module_code
        self.module_name = module_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.module_code is not None:
            result['ModuleCode'] = self.module_code
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ModuleCode') is not None:
            self.module_code = m.get('ModuleCode')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        return self


class DataModuleMapListSpnTypeMapListValueShowModules(TeaModel):
    def __init__(
        self,
        module_id: int = None,
        module_code: str = None,
        module_name: str = None,
    ):
        self.module_id = module_id
        self.module_code = module_code
        self.module_name = module_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.module_code is not None:
            result['ModuleCode'] = self.module_code
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ModuleCode') is not None:
            self.module_code = m.get('ModuleCode')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        return self


class DataModuleMapListSpnTypeMapListValue(TeaModel):
    def __init__(
        self,
        filter_modules: List[DataModuleMapListSpnTypeMapListValueFilterModules] = None,
        show_modules: List[DataModuleMapListSpnTypeMapListValueShowModules] = None,
    ):
        self.filter_modules = filter_modules
        self.show_modules = show_modules

    def validate(self):
        if self.filter_modules:
            for k in self.filter_modules:
                if k:
                    k.validate()
        if self.show_modules:
            for k in self.show_modules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FilterModules'] = []
        if self.filter_modules is not None:
            for k in self.filter_modules:
                result['FilterModules'].append(k.to_map() if k else None)
        result['ShowModules'] = []
        if self.show_modules is not None:
            for k in self.show_modules:
                result['ShowModules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filter_modules = []
        if m.get('FilterModules') is not None:
            for k in m.get('FilterModules'):
                temp_model = DataModuleMapListSpnTypeMapListValueFilterModules()
                self.filter_modules.append(temp_model.from_map(k))
        self.show_modules = []
        if m.get('ShowModules') is not None:
            for k in m.get('ShowModules'):
                temp_model = DataModuleMapListSpnTypeMapListValueShowModules()
                self.show_modules.append(temp_model.from_map(k))
        return self


class DataStepPriceMapValue(TeaModel):
    def __init__(
        self,
        right_close: bool = None,
        min: str = None,
        max: str = None,
        currency: str = None,
        left_close: bool = None,
        step_price_value: str = None,
        price_value_type: str = None,
        price_value: str = None,
        deduct_cycle_type: str = None,
    ):
        self.right_close = right_close
        self.min = min
        self.max = max
        self.currency = currency
        self.left_close = left_close
        self.step_price_value = step_price_value
        self.price_value_type = price_value_type
        self.price_value = price_value
        self.deduct_cycle_type = deduct_cycle_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.right_close is not None:
            result['RightClose'] = self.right_close
        if self.min is not None:
            result['Min'] = self.min
        if self.max is not None:
            result['Max'] = self.max
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.left_close is not None:
            result['LeftClose'] = self.left_close
        if self.step_price_value is not None:
            result['StepPriceValue'] = self.step_price_value
        if self.price_value_type is not None:
            result['PriceValueType'] = self.price_value_type
        if self.price_value is not None:
            result['PriceValue'] = self.price_value
        if self.deduct_cycle_type is not None:
            result['DeductCycleType'] = self.deduct_cycle_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RightClose') is not None:
            self.right_close = m.get('RightClose')
        if m.get('Min') is not None:
            self.min = m.get('Min')
        if m.get('Max') is not None:
            self.max = m.get('Max')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('LeftClose') is not None:
            self.left_close = m.get('LeftClose')
        if m.get('StepPriceValue') is not None:
            self.step_price_value = m.get('StepPriceValue')
        if m.get('PriceValueType') is not None:
            self.price_value_type = m.get('PriceValueType')
        if m.get('PriceValue') is not None:
            self.price_value = m.get('PriceValue')
        if m.get('DeductCycleType') is not None:
            self.deduct_cycle_type = m.get('DeductCycleType')
        return self


class AddCouponDeductTagRequestEcIdAccountIds(TeaModel):
    def __init__(
        self,
        account_ids: List[int] = None,
        ec_id: str = None,
    ):
        self.account_ids = account_ids
        # This parameter is required.
        self.ec_id = ec_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids
        if self.ec_id is not None:
            result['EcId'] = self.ec_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')
        if m.get('EcId') is not None:
            self.ec_id = m.get('EcId')
        return self


class AddCouponDeductTagRequestTags(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class AddCouponDeductTagRequest(TeaModel):
    def __init__(
        self,
        coupon_id: str = None,
        ec_id_account_ids: List[AddCouponDeductTagRequestEcIdAccountIds] = None,
        nbid: str = None,
        tags: List[AddCouponDeductTagRequestTags] = None,
    ):
        self.coupon_id = coupon_id
        self.ec_id_account_ids = ec_id_account_ids
        self.nbid = nbid
        self.tags = tags

    def validate(self):
        if self.ec_id_account_ids:
            for k in self.ec_id_account_ids:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coupon_id is not None:
            result['CouponId'] = self.coupon_id
        result['EcIdAccountIds'] = []
        if self.ec_id_account_ids is not None:
            for k in self.ec_id_account_ids:
                result['EcIdAccountIds'].append(k.to_map() if k else None)
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CouponId') is not None:
            self.coupon_id = m.get('CouponId')
        self.ec_id_account_ids = []
        if m.get('EcIdAccountIds') is not None:
            for k in m.get('EcIdAccountIds'):
                temp_model = AddCouponDeductTagRequestEcIdAccountIds()
                self.ec_id_account_ids.append(temp_model.from_map(k))
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = AddCouponDeductTagRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class AddCouponDeductTagShrinkRequest(TeaModel):
    def __init__(
        self,
        coupon_id: str = None,
        ec_id_account_ids_shrink: str = None,
        nbid: str = None,
        tags_shrink: str = None,
    ):
        self.coupon_id = coupon_id
        self.ec_id_account_ids_shrink = ec_id_account_ids_shrink
        self.nbid = nbid
        self.tags_shrink = tags_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coupon_id is not None:
            result['CouponId'] = self.coupon_id
        if self.ec_id_account_ids_shrink is not None:
            result['EcIdAccountIds'] = self.ec_id_account_ids_shrink
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CouponId') is not None:
            self.coupon_id = m.get('CouponId')
        if m.get('EcIdAccountIds') is not None:
            self.ec_id_account_ids_shrink = m.get('EcIdAccountIds')
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        return self


class AddCouponDeductTagResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddCouponDeductTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddCouponDeductTagResponseBody = None,
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
            temp_model = AddCouponDeductTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AllocateCostCenterResourceRequestResourceInstanceList(TeaModel):
    def __init__(
        self,
        apportion_code: str = None,
        apportion_name: str = None,
        commodity_code: str = None,
        commodity_name: str = None,
        instance_id: str = None,
        pip_code: str = None,
        related_resources: str = None,
        resource_group: str = None,
        resource_id: str = None,
        resource_nick: str = None,
        resource_source: str = None,
        resource_status: str = None,
        resource_tag: str = None,
        resource_type: str = None,
        resource_user_id: int = None,
        resource_user_name: str = None,
    ):
        self.apportion_code = apportion_code
        self.apportion_name = apportion_name
        self.commodity_code = commodity_code
        self.commodity_name = commodity_name
        self.instance_id = instance_id
        self.pip_code = pip_code
        self.related_resources = related_resources
        self.resource_group = resource_group
        self.resource_id = resource_id
        self.resource_nick = resource_nick
        self.resource_source = resource_source
        self.resource_status = resource_status
        self.resource_tag = resource_tag
        self.resource_type = resource_type
        self.resource_user_id = resource_user_id
        self.resource_user_name = resource_user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apportion_code is not None:
            result['ApportionCode'] = self.apportion_code
        if self.apportion_name is not None:
            result['ApportionName'] = self.apportion_name
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.commodity_name is not None:
            result['CommodityName'] = self.commodity_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.pip_code is not None:
            result['PipCode'] = self.pip_code
        if self.related_resources is not None:
            result['RelatedResources'] = self.related_resources
        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_nick is not None:
            result['ResourceNick'] = self.resource_nick
        if self.resource_source is not None:
            result['ResourceSource'] = self.resource_source
        if self.resource_status is not None:
            result['ResourceStatus'] = self.resource_status
        if self.resource_tag is not None:
            result['ResourceTag'] = self.resource_tag
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_user_id is not None:
            result['ResourceUserId'] = self.resource_user_id
        if self.resource_user_name is not None:
            result['ResourceUserName'] = self.resource_user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApportionCode') is not None:
            self.apportion_code = m.get('ApportionCode')
        if m.get('ApportionName') is not None:
            self.apportion_name = m.get('ApportionName')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('CommodityName') is not None:
            self.commodity_name = m.get('CommodityName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PipCode') is not None:
            self.pip_code = m.get('PipCode')
        if m.get('RelatedResources') is not None:
            self.related_resources = m.get('RelatedResources')
        if m.get('ResourceGroup') is not None:
            self.resource_group = m.get('ResourceGroup')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceNick') is not None:
            self.resource_nick = m.get('ResourceNick')
        if m.get('ResourceSource') is not None:
            self.resource_source = m.get('ResourceSource')
        if m.get('ResourceStatus') is not None:
            self.resource_status = m.get('ResourceStatus')
        if m.get('ResourceTag') is not None:
            self.resource_tag = m.get('ResourceTag')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceUserId') is not None:
            self.resource_user_id = m.get('ResourceUserId')
        if m.get('ResourceUserName') is not None:
            self.resource_user_name = m.get('ResourceUserName')
        return self


class AllocateCostCenterResourceRequest(TeaModel):
    def __init__(
        self,
        from_cost_center_id: int = None,
        from_owner_account_id: int = None,
        nbid: str = None,
        resource_instance_list: List[AllocateCostCenterResourceRequestResourceInstanceList] = None,
        to_cost_center_id: int = None,
    ):
        self.from_cost_center_id = from_cost_center_id
        self.from_owner_account_id = from_owner_account_id
        self.nbid = nbid
        # This parameter is required.
        self.resource_instance_list = resource_instance_list
        self.to_cost_center_id = to_cost_center_id

    def validate(self):
        if self.resource_instance_list:
            for k in self.resource_instance_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_cost_center_id is not None:
            result['FromCostCenterId'] = self.from_cost_center_id
        if self.from_owner_account_id is not None:
            result['FromOwnerAccountId'] = self.from_owner_account_id
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        result['ResourceInstanceList'] = []
        if self.resource_instance_list is not None:
            for k in self.resource_instance_list:
                result['ResourceInstanceList'].append(k.to_map() if k else None)
        if self.to_cost_center_id is not None:
            result['ToCostCenterId'] = self.to_cost_center_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromCostCenterId') is not None:
            self.from_cost_center_id = m.get('FromCostCenterId')
        if m.get('FromOwnerAccountId') is not None:
            self.from_owner_account_id = m.get('FromOwnerAccountId')
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        self.resource_instance_list = []
        if m.get('ResourceInstanceList') is not None:
            for k in m.get('ResourceInstanceList'):
                temp_model = AllocateCostCenterResourceRequestResourceInstanceList()
                self.resource_instance_list.append(temp_model.from_map(k))
        if m.get('ToCostCenterId') is not None:
            self.to_cost_center_id = m.get('ToCostCenterId')
        return self


class AllocateCostCenterResourceShrinkRequest(TeaModel):
    def __init__(
        self,
        from_cost_center_id: int = None,
        from_owner_account_id: int = None,
        nbid: str = None,
        resource_instance_list_shrink: str = None,
        to_cost_center_id: int = None,
    ):
        self.from_cost_center_id = from_cost_center_id
        self.from_owner_account_id = from_owner_account_id
        self.nbid = nbid
        # This parameter is required.
        self.resource_instance_list_shrink = resource_instance_list_shrink
        self.to_cost_center_id = to_cost_center_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_cost_center_id is not None:
            result['FromCostCenterId'] = self.from_cost_center_id
        if self.from_owner_account_id is not None:
            result['FromOwnerAccountId'] = self.from_owner_account_id
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        if self.resource_instance_list_shrink is not None:
            result['ResourceInstanceList'] = self.resource_instance_list_shrink
        if self.to_cost_center_id is not None:
            result['ToCostCenterId'] = self.to_cost_center_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromCostCenterId') is not None:
            self.from_cost_center_id = m.get('FromCostCenterId')
        if m.get('FromOwnerAccountId') is not None:
            self.from_owner_account_id = m.get('FromOwnerAccountId')
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        if m.get('ResourceInstanceList') is not None:
            self.resource_instance_list_shrink = m.get('ResourceInstanceList')
        if m.get('ToCostCenterId') is not None:
            self.to_cost_center_id = m.get('ToCostCenterId')
        return self


class AllocateCostCenterResourceResponseBody(TeaModel):
    def __init__(
        self,
        cost_center_id: int = None,
        is_success: bool = None,
        metadata: Any = None,
        owner_account_id: int = None,
        request_id: str = None,
    ):
        self.cost_center_id = cost_center_id
        self.is_success = is_success
        self.metadata = metadata
        self.owner_account_id = owner_account_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_center_id is not None:
            result['CostCenterId'] = self.cost_center_id
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.owner_account_id is not None:
            result['OwnerAccountId'] = self.owner_account_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostCenterId') is not None:
            self.cost_center_id = m.get('CostCenterId')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('OwnerAccountId') is not None:
            self.owner_account_id = m.get('OwnerAccountId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AllocateCostCenterResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AllocateCostCenterResourceResponseBody = None,
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
            temp_model = AllocateCostCenterResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelFundAccountLowAvailableAmountAlarmRequest(TeaModel):
    def __init__(
        self,
        fund_account_id: int = None,
    ):
        self.fund_account_id = fund_account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fund_account_id is not None:
            result['FundAccountId'] = self.fund_account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FundAccountId') is not None:
            self.fund_account_id = m.get('FundAccountId')
        return self


class CancelFundAccountLowAvailableAmountAlarmResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        metadata: Any = None,
        request_id: str = None,
    ):
        self.data = data
        self.metadata = metadata
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CancelFundAccountLowAvailableAmountAlarmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelFundAccountLowAvailableAmountAlarmResponseBody = None,
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
            temp_model = CancelFundAccountLowAvailableAmountAlarmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCostCenterRequestCostCenterEntityList(TeaModel):
    def __init__(
        self,
        cost_center_name: str = None,
        owner_account_id: int = None,
        parent_cost_center_id: int = None,
    ):
        # This parameter is required.
        self.cost_center_name = cost_center_name
        # This parameter is required.
        self.owner_account_id = owner_account_id
        # This parameter is required.
        self.parent_cost_center_id = parent_cost_center_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_center_name is not None:
            result['CostCenterName'] = self.cost_center_name
        if self.owner_account_id is not None:
            result['OwnerAccountId'] = self.owner_account_id
        if self.parent_cost_center_id is not None:
            result['ParentCostCenterId'] = self.parent_cost_center_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostCenterName') is not None:
            self.cost_center_name = m.get('CostCenterName')
        if m.get('OwnerAccountId') is not None:
            self.owner_account_id = m.get('OwnerAccountId')
        if m.get('ParentCostCenterId') is not None:
            self.parent_cost_center_id = m.get('ParentCostCenterId')
        return self


class CreateCostCenterRequest(TeaModel):
    def __init__(
        self,
        cost_center_entity_list: List[CreateCostCenterRequestCostCenterEntityList] = None,
        nbid: str = None,
    ):
        # This parameter is required.
        self.cost_center_entity_list = cost_center_entity_list
        self.nbid = nbid

    def validate(self):
        if self.cost_center_entity_list:
            for k in self.cost_center_entity_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CostCenterEntityList'] = []
        if self.cost_center_entity_list is not None:
            for k in self.cost_center_entity_list:
                result['CostCenterEntityList'].append(k.to_map() if k else None)
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cost_center_entity_list = []
        if m.get('CostCenterEntityList') is not None:
            for k in m.get('CostCenterEntityList'):
                temp_model = CreateCostCenterRequestCostCenterEntityList()
                self.cost_center_entity_list.append(temp_model.from_map(k))
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        return self


class CreateCostCenterShrinkRequest(TeaModel):
    def __init__(
        self,
        cost_center_entity_list_shrink: str = None,
        nbid: str = None,
    ):
        # This parameter is required.
        self.cost_center_entity_list_shrink = cost_center_entity_list_shrink
        self.nbid = nbid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_center_entity_list_shrink is not None:
            result['CostCenterEntityList'] = self.cost_center_entity_list_shrink
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostCenterEntityList') is not None:
            self.cost_center_entity_list_shrink = m.get('CostCenterEntityList')
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        return self


class CreateCostCenterResponseBodyCostCenterDtoList(TeaModel):
    def __init__(
        self,
        cost_center_id: int = None,
        cost_center_name: str = None,
        owner_account_id: int = None,
        parent_cost_center_id: int = None,
    ):
        self.cost_center_id = cost_center_id
        self.cost_center_name = cost_center_name
        self.owner_account_id = owner_account_id
        self.parent_cost_center_id = parent_cost_center_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_center_id is not None:
            result['CostCenterId'] = self.cost_center_id
        if self.cost_center_name is not None:
            result['CostCenterName'] = self.cost_center_name
        if self.owner_account_id is not None:
            result['OwnerAccountId'] = self.owner_account_id
        if self.parent_cost_center_id is not None:
            result['ParentCostCenterId'] = self.parent_cost_center_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostCenterId') is not None:
            self.cost_center_id = m.get('CostCenterId')
        if m.get('CostCenterName') is not None:
            self.cost_center_name = m.get('CostCenterName')
        if m.get('OwnerAccountId') is not None:
            self.owner_account_id = m.get('OwnerAccountId')
        if m.get('ParentCostCenterId') is not None:
            self.parent_cost_center_id = m.get('ParentCostCenterId')
        return self


class CreateCostCenterResponseBody(TeaModel):
    def __init__(
        self,
        cost_center_dto_list: List[CreateCostCenterResponseBodyCostCenterDtoList] = None,
        metadata: Any = None,
        request_id: str = None,
    ):
        self.cost_center_dto_list = cost_center_dto_list
        self.metadata = metadata
        self.request_id = request_id

    def validate(self):
        if self.cost_center_dto_list:
            for k in self.cost_center_dto_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CostCenterDtoList'] = []
        if self.cost_center_dto_list is not None:
            for k in self.cost_center_dto_list:
                result['CostCenterDtoList'].append(k.to_map() if k else None)
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cost_center_dto_list = []
        if m.get('CostCenterDtoList') is not None:
            for k in m.get('CostCenterDtoList'):
                temp_model = CreateCostCenterResponseBodyCostCenterDtoList()
                self.cost_center_dto_list.append(temp_model.from_map(k))
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCostCenterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCostCenterResponseBody = None,
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
            temp_model = CreateCostCenterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCostCenterRuleRequestFilterExpressionFilterValues(TeaModel):
    def __init__(
        self,
        code: str = None,
        code_name: str = None,
        select_type: str = None,
        values: List[str] = None,
    ):
        self.code = code
        self.code_name = code_name
        self.select_type = select_type
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.code_name is not None:
            result['CodeName'] = self.code_name
        if self.select_type is not None:
            result['SelectType'] = self.select_type
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CodeName') is not None:
            self.code_name = m.get('CodeName')
        if m.get('SelectType') is not None:
            self.select_type = m.get('SelectType')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class CreateCostCenterRuleRequestFilterExpression(TeaModel):
    def __init__(
        self,
        expression_type: str = None,
        filter_values: CreateCostCenterRuleRequestFilterExpressionFilterValues = None,
        operand: Any = None,
        operands: List[Any] = None,
        operator_type: str = None,
    ):
        self.expression_type = expression_type
        self.filter_values = filter_values
        self.operand = operand
        self.operands = operands
        self.operator_type = operator_type

    def validate(self):
        if self.filter_values:
            self.filter_values.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expression_type is not None:
            result['ExpressionType'] = self.expression_type
        if self.filter_values is not None:
            result['FilterValues'] = self.filter_values.to_map()
        if self.operand is not None:
            result['Operand'] = self.operand
        if self.operands is not None:
            result['Operands'] = self.operands
        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpressionType') is not None:
            self.expression_type = m.get('ExpressionType')
        if m.get('FilterValues') is not None:
            temp_model = CreateCostCenterRuleRequestFilterExpressionFilterValues()
            self.filter_values = temp_model.from_map(m['FilterValues'])
        if m.get('Operand') is not None:
            self.operand = m.get('Operand')
        if m.get('Operands') is not None:
            self.operands = m.get('Operands')
        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')
        return self


class CreateCostCenterRuleRequest(TeaModel):
    def __init__(
        self,
        cost_center_id: int = None,
        filter_expression: CreateCostCenterRuleRequestFilterExpression = None,
        nbid: str = None,
    ):
        self.cost_center_id = cost_center_id
        self.filter_expression = filter_expression
        self.nbid = nbid

    def validate(self):
        if self.filter_expression:
            self.filter_expression.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_center_id is not None:
            result['CostCenterId'] = self.cost_center_id
        if self.filter_expression is not None:
            result['FilterExpression'] = self.filter_expression.to_map()
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostCenterId') is not None:
            self.cost_center_id = m.get('CostCenterId')
        if m.get('FilterExpression') is not None:
            temp_model = CreateCostCenterRuleRequestFilterExpression()
            self.filter_expression = temp_model.from_map(m['FilterExpression'])
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        return self


class CreateCostCenterRuleShrinkRequest(TeaModel):
    def __init__(
        self,
        cost_center_id: int = None,
        filter_expression_shrink: str = None,
        nbid: str = None,
    ):
        self.cost_center_id = cost_center_id
        self.filter_expression_shrink = filter_expression_shrink
        self.nbid = nbid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_center_id is not None:
            result['CostCenterId'] = self.cost_center_id
        if self.filter_expression_shrink is not None:
            result['FilterExpression'] = self.filter_expression_shrink
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostCenterId') is not None:
            self.cost_center_id = m.get('CostCenterId')
        if m.get('FilterExpression') is not None:
            self.filter_expression_shrink = m.get('FilterExpression')
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        return self


class CreateCostCenterRuleResponseBody(TeaModel):
    def __init__(
        self,
        data: int = None,
        metadata: Any = None,
        request_id: str = None,
    ):
        self.data = data
        self.metadata = metadata
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCostCenterRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCostCenterRuleResponseBody = None,
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
            temp_model = CreateCostCenterRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFundAccountPayRelationRequestEcIdAccountIds(TeaModel):
    def __init__(
        self,
        account_ids: List[int] = None,
        ec_id: str = None,
    ):
        # This parameter is required.
        self.account_ids = account_ids
        self.ec_id = ec_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids
        if self.ec_id is not None:
            result['EcId'] = self.ec_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')
        if m.get('EcId') is not None:
            self.ec_id = m.get('EcId')
        return self


class CreateFundAccountPayRelationRequest(TeaModel):
    def __init__(
        self,
        ec_id_account_ids: List[CreateFundAccountPayRelationRequestEcIdAccountIds] = None,
        fund_account_id: str = None,
        nbid: str = None,
    ):
        # This parameter is required.
        self.ec_id_account_ids = ec_id_account_ids
        # This parameter is required.
        self.fund_account_id = fund_account_id
        self.nbid = nbid

    def validate(self):
        if self.ec_id_account_ids:
            for k in self.ec_id_account_ids:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EcIdAccountIds'] = []
        if self.ec_id_account_ids is not None:
            for k in self.ec_id_account_ids:
                result['EcIdAccountIds'].append(k.to_map() if k else None)
        if self.fund_account_id is not None:
            result['FundAccountId'] = self.fund_account_id
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ec_id_account_ids = []
        if m.get('EcIdAccountIds') is not None:
            for k in m.get('EcIdAccountIds'):
                temp_model = CreateFundAccountPayRelationRequestEcIdAccountIds()
                self.ec_id_account_ids.append(temp_model.from_map(k))
        if m.get('FundAccountId') is not None:
            self.fund_account_id = m.get('FundAccountId')
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        return self


class CreateFundAccountPayRelationShrinkRequest(TeaModel):
    def __init__(
        self,
        ec_id_account_ids_shrink: str = None,
        fund_account_id: str = None,
        nbid: str = None,
    ):
        # This parameter is required.
        self.ec_id_account_ids_shrink = ec_id_account_ids_shrink
        # This parameter is required.
        self.fund_account_id = fund_account_id
        self.nbid = nbid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ec_id_account_ids_shrink is not None:
            result['EcIdAccountIds'] = self.ec_id_account_ids_shrink
        if self.fund_account_id is not None:
            result['FundAccountId'] = self.fund_account_id
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EcIdAccountIds') is not None:
            self.ec_id_account_ids_shrink = m.get('EcIdAccountIds')
        if m.get('FundAccountId') is not None:
            self.fund_account_id = m.get('FundAccountId')
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        return self


class CreateFundAccountPayRelationResponseBodyData(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        account_name: str = None,
        fund_account_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.account_id = account_id
        self.account_name = account_name
        self.fund_account_id = fund_account_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.fund_account_id is not None:
            result['FundAccountId'] = self.fund_account_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('FundAccountId') is not None:
            self.fund_account_id = m.get('FundAccountId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class CreateFundAccountPayRelationResponseBody(TeaModel):
    def __init__(
        self,
        data: List[CreateFundAccountPayRelationResponseBodyData] = None,
        metadata: Any = None,
        request_id: str = None,
    ):
        self.data = data
        self.metadata = metadata
        self.request_id = request_id

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
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = CreateFundAccountPayRelationResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateFundAccountPayRelationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFundAccountPayRelationResponseBody = None,
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
            temp_model = CreateFundAccountPayRelationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFundAccountTransferRequest(TeaModel):
    def __init__(
        self,
        amount: str = None,
        currency: str = None,
        finance_type: str = None,
        from_fund_account_id: int = None,
        remark: str = None,
        to_fund_account_id: int = None,
        transfer_type: str = None,
    ):
        # This parameter is required.
        self.amount = amount
        # This parameter is required.
        self.currency = currency
        # This parameter is required.
        self.finance_type = finance_type
        # This parameter is required.
        self.from_fund_account_id = from_fund_account_id
        # This parameter is required.
        self.remark = remark
        # This parameter is required.
        self.to_fund_account_id = to_fund_account_id
        # This parameter is required.
        self.transfer_type = transfer_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.finance_type is not None:
            result['FinanceType'] = self.finance_type
        if self.from_fund_account_id is not None:
            result['FromFundAccountId'] = self.from_fund_account_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.to_fund_account_id is not None:
            result['ToFundAccountId'] = self.to_fund_account_id
        if self.transfer_type is not None:
            result['TransferType'] = self.transfer_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('FinanceType') is not None:
            self.finance_type = m.get('FinanceType')
        if m.get('FromFundAccountId') is not None:
            self.from_fund_account_id = m.get('FromFundAccountId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ToFundAccountId') is not None:
            self.to_fund_account_id = m.get('ToFundAccountId')
        if m.get('TransferType') is not None:
            self.transfer_type = m.get('TransferType')
        return self


class CreateFundAccountTransferResponseBody(TeaModel):
    def __init__(
        self,
        metadata: Any = None,
        request_id: str = None,
    ):
        self.metadata = metadata
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateFundAccountTransferResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFundAccountTransferResponseBody = None,
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
            temp_model = CreateFundAccountTransferResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInvoiceRequestEcIdAccountIds(TeaModel):
    def __init__(
        self,
        account_ids: List[int] = None,
        ec_id: str = None,
    ):
        self.account_ids = account_ids
        self.ec_id = ec_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids
        if self.ec_id is not None:
            result['EcId'] = self.ec_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')
        if m.get('EcId') is not None:
            self.ec_id = m.get('EcId')
        return self


class CreateInvoiceRequest(TeaModel):
    def __init__(
        self,
        amount: str = None,
        ec_id_account_ids: List[CreateInvoiceRequestEcIdAccountIds] = None,
        invoice_candidate_ids: List[str] = None,
        invoice_mode: int = None,
        invoice_remark: str = None,
        invoice_title_id: str = None,
        invoice_type: int = None,
        nbid: str = None,
        recipient_emails: List[str] = None,
    ):
        self.amount = amount
        self.ec_id_account_ids = ec_id_account_ids
        # This parameter is required.
        self.invoice_candidate_ids = invoice_candidate_ids
        # This parameter is required.
        self.invoice_mode = invoice_mode
        self.invoice_remark = invoice_remark
        # This parameter is required.
        self.invoice_title_id = invoice_title_id
        # This parameter is required.
        self.invoice_type = invoice_type
        self.nbid = nbid
        # This parameter is required.
        self.recipient_emails = recipient_emails

    def validate(self):
        if self.ec_id_account_ids:
            for k in self.ec_id_account_ids:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        result['EcIdAccountIds'] = []
        if self.ec_id_account_ids is not None:
            for k in self.ec_id_account_ids:
                result['EcIdAccountIds'].append(k.to_map() if k else None)
        if self.invoice_candidate_ids is not None:
            result['InvoiceCandidateIds'] = self.invoice_candidate_ids
        if self.invoice_mode is not None:
            result['InvoiceMode'] = self.invoice_mode
        if self.invoice_remark is not None:
            result['InvoiceRemark'] = self.invoice_remark
        if self.invoice_title_id is not None:
            result['InvoiceTitleId'] = self.invoice_title_id
        if self.invoice_type is not None:
            result['InvoiceType'] = self.invoice_type
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        if self.recipient_emails is not None:
            result['RecipientEmails'] = self.recipient_emails
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        self.ec_id_account_ids = []
        if m.get('EcIdAccountIds') is not None:
            for k in m.get('EcIdAccountIds'):
                temp_model = CreateInvoiceRequestEcIdAccountIds()
                self.ec_id_account_ids.append(temp_model.from_map(k))
        if m.get('InvoiceCandidateIds') is not None:
            self.invoice_candidate_ids = m.get('InvoiceCandidateIds')
        if m.get('InvoiceMode') is not None:
            self.invoice_mode = m.get('InvoiceMode')
        if m.get('InvoiceRemark') is not None:
            self.invoice_remark = m.get('InvoiceRemark')
        if m.get('InvoiceTitleId') is not None:
            self.invoice_title_id = m.get('InvoiceTitleId')
        if m.get('InvoiceType') is not None:
            self.invoice_type = m.get('InvoiceType')
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        if m.get('RecipientEmails') is not None:
            self.recipient_emails = m.get('RecipientEmails')
        return self


class CreateInvoiceShrinkRequest(TeaModel):
    def __init__(
        self,
        amount: str = None,
        ec_id_account_ids_shrink: str = None,
        invoice_candidate_ids_shrink: str = None,
        invoice_mode: int = None,
        invoice_remark: str = None,
        invoice_title_id: str = None,
        invoice_type: int = None,
        nbid: str = None,
        recipient_emails_shrink: str = None,
    ):
        self.amount = amount
        self.ec_id_account_ids_shrink = ec_id_account_ids_shrink
        # This parameter is required.
        self.invoice_candidate_ids_shrink = invoice_candidate_ids_shrink
        # This parameter is required.
        self.invoice_mode = invoice_mode
        self.invoice_remark = invoice_remark
        # This parameter is required.
        self.invoice_title_id = invoice_title_id
        # This parameter is required.
        self.invoice_type = invoice_type
        self.nbid = nbid
        # This parameter is required.
        self.recipient_emails_shrink = recipient_emails_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.ec_id_account_ids_shrink is not None:
            result['EcIdAccountIds'] = self.ec_id_account_ids_shrink
        if self.invoice_candidate_ids_shrink is not None:
            result['InvoiceCandidateIds'] = self.invoice_candidate_ids_shrink
        if self.invoice_mode is not None:
            result['InvoiceMode'] = self.invoice_mode
        if self.invoice_remark is not None:
            result['InvoiceRemark'] = self.invoice_remark
        if self.invoice_title_id is not None:
            result['InvoiceTitleId'] = self.invoice_title_id
        if self.invoice_type is not None:
            result['InvoiceType'] = self.invoice_type
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        if self.recipient_emails_shrink is not None:
            result['RecipientEmails'] = self.recipient_emails_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('EcIdAccountIds') is not None:
            self.ec_id_account_ids_shrink = m.get('EcIdAccountIds')
        if m.get('InvoiceCandidateIds') is not None:
            self.invoice_candidate_ids_shrink = m.get('InvoiceCandidateIds')
        if m.get('InvoiceMode') is not None:
            self.invoice_mode = m.get('InvoiceMode')
        if m.get('InvoiceRemark') is not None:
            self.invoice_remark = m.get('InvoiceRemark')
        if m.get('InvoiceTitleId') is not None:
            self.invoice_title_id = m.get('InvoiceTitleId')
        if m.get('InvoiceType') is not None:
            self.invoice_type = m.get('InvoiceType')
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        if m.get('RecipientEmails') is not None:
            self.recipient_emails_shrink = m.get('RecipientEmails')
        return self


class CreateInvoiceResponseBodyData(TeaModel):
    def __init__(
        self,
        account_id: int = None,
        amount: str = None,
        error_code: str = None,
        invoice_issuer: str = None,
        message: str = None,
    ):
        self.account_id = account_id
        self.amount = amount
        self.error_code = error_code
        self.invoice_issuer = invoice_issuer
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.invoice_issuer is not None:
            result['InvoiceIssuer'] = self.invoice_issuer
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('InvoiceIssuer') is not None:
            self.invoice_issuer = m.get('InvoiceIssuer')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class CreateInvoiceResponseBody(TeaModel):
    def __init__(
        self,
        data: List[CreateInvoiceResponseBodyData] = None,
        metadata: Any = None,
        request_id: str = None,
    ):
        self.data = data
        self.metadata = metadata
        self.request_id = request_id

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
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = CreateInvoiceResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateInvoiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateInvoiceResponseBody = None,
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
            temp_model = CreateInvoiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateReportDefinitionRequest(TeaModel):
    def __init__(
        self,
        begin_billing_cycle: str = None,
        mc_project: str = None,
        mc_table_name: str = None,
        nbid: str = None,
        oss_bucket_name: str = None,
        oss_bucket_owner_account_id: int = None,
        oss_bucket_path: str = None,
        report_source_type: str = None,
        report_type: str = None,
    ):
        self.begin_billing_cycle = begin_billing_cycle
        self.mc_project = mc_project
        self.mc_table_name = mc_table_name
        self.nbid = nbid
        self.oss_bucket_name = oss_bucket_name
        self.oss_bucket_owner_account_id = oss_bucket_owner_account_id
        self.oss_bucket_path = oss_bucket_path
        self.report_source_type = report_source_type
        # This parameter is required.
        self.report_type = report_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_billing_cycle is not None:
            result['BeginBillingCycle'] = self.begin_billing_cycle
        if self.mc_project is not None:
            result['McProject'] = self.mc_project
        if self.mc_table_name is not None:
            result['McTableName'] = self.mc_table_name
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.oss_bucket_owner_account_id is not None:
            result['OssBucketOwnerAccountId'] = self.oss_bucket_owner_account_id
        if self.oss_bucket_path is not None:
            result['OssBucketPath'] = self.oss_bucket_path
        if self.report_source_type is not None:
            result['ReportSourceType'] = self.report_source_type
        if self.report_type is not None:
            result['ReportType'] = self.report_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginBillingCycle') is not None:
            self.begin_billing_cycle = m.get('BeginBillingCycle')
        if m.get('McProject') is not None:
            self.mc_project = m.get('McProject')
        if m.get('McTableName') is not None:
            self.mc_table_name = m.get('McTableName')
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('OssBucketOwnerAccountId') is not None:
            self.oss_bucket_owner_account_id = m.get('OssBucketOwnerAccountId')
        if m.get('OssBucketPath') is not None:
            self.oss_bucket_path = m.get('OssBucketPath')
        if m.get('ReportSourceType') is not None:
            self.report_source_type = m.get('ReportSourceType')
        if m.get('ReportType') is not None:
            self.report_type = m.get('ReportType')
        return self


class CreateReportDefinitionResponseBody(TeaModel):
    def __init__(
        self,
        begin_billing_cycle: str = None,
        metadata: Any = None,
        oss_bucket_name: str = None,
        oss_bucket_owner_account_id: int = None,
        oss_bucket_path: str = None,
        report_source_name: str = None,
        report_source_type: str = None,
        report_task_id: int = None,
        report_type: str = None,
        request_id: str = None,
        subscribe_create_time: str = None,
    ):
        self.begin_billing_cycle = begin_billing_cycle
        self.metadata = metadata
        self.oss_bucket_name = oss_bucket_name
        self.oss_bucket_owner_account_id = oss_bucket_owner_account_id
        self.oss_bucket_path = oss_bucket_path
        self.report_source_name = report_source_name
        self.report_source_type = report_source_type
        self.report_task_id = report_task_id
        self.report_type = report_type
        self.request_id = request_id
        self.subscribe_create_time = subscribe_create_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_billing_cycle is not None:
            result['BeginBillingCycle'] = self.begin_billing_cycle
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.oss_bucket_owner_account_id is not None:
            result['OssBucketOwnerAccountId'] = self.oss_bucket_owner_account_id
        if self.oss_bucket_path is not None:
            result['OssBucketPath'] = self.oss_bucket_path
        if self.report_source_name is not None:
            result['ReportSourceName'] = self.report_source_name
        if self.report_source_type is not None:
            result['ReportSourceType'] = self.report_source_type
        if self.report_task_id is not None:
            result['ReportTaskId'] = self.report_task_id
        if self.report_type is not None:
            result['ReportType'] = self.report_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.subscribe_create_time is not None:
            result['SubscribeCreateTime'] = self.subscribe_create_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginBillingCycle') is not None:
            self.begin_billing_cycle = m.get('BeginBillingCycle')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('OssBucketOwnerAccountId') is not None:
            self.oss_bucket_owner_account_id = m.get('OssBucketOwnerAccountId')
        if m.get('OssBucketPath') is not None:
            self.oss_bucket_path = m.get('OssBucketPath')
        if m.get('ReportSourceName') is not None:
            self.report_source_name = m.get('ReportSourceName')
        if m.get('ReportSourceType') is not None:
            self.report_source_type = m.get('ReportSourceType')
        if m.get('ReportTaskId') is not None:
            self.report_task_id = m.get('ReportTaskId')
        if m.get('ReportType') is not None:
            self.report_type = m.get('ReportType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubscribeCreateTime') is not None:
            self.subscribe_create_time = m.get('SubscribeCreateTime')
        return self


class CreateReportDefinitionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateReportDefinitionResponseBody = None,
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
            temp_model = CreateReportDefinitionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCostCenterRequest(TeaModel):
    def __init__(
        self,
        cost_center_id: int = None,
        nbid: str = None,
        owner_account_id: int = None,
    ):
        # This parameter is required.
        self.cost_center_id = cost_center_id
        self.nbid = nbid
        # This parameter is required.
        self.owner_account_id = owner_account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_center_id is not None:
            result['CostCenterId'] = self.cost_center_id
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        if self.owner_account_id is not None:
            result['OwnerAccountId'] = self.owner_account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostCenterId') is not None:
            self.cost_center_id = m.get('CostCenterId')
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        if m.get('OwnerAccountId') is not None:
            self.owner_account_id = m.get('OwnerAccountId')
        return self


class DeleteCostCenterResponseBody(TeaModel):
    def __init__(
        self,
        cost_center_id: int = None,
        is_success: bool = None,
        metadata: Any = None,
        owner_account_id: int = None,
        request_id: str = None,
    ):
        self.cost_center_id = cost_center_id
        self.is_success = is_success
        self.metadata = metadata
        self.owner_account_id = owner_account_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_center_id is not None:
            result['CostCenterId'] = self.cost_center_id
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.owner_account_id is not None:
            result['OwnerAccountId'] = self.owner_account_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostCenterId') is not None:
            self.cost_center_id = m.get('CostCenterId')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('OwnerAccountId') is not None:
            self.owner_account_id = m.get('OwnerAccountId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteCostCenterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCostCenterResponseBody = None,
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
            temp_model = DeleteCostCenterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCostCenterRuleRequestFilterExpressionFilterValues(TeaModel):
    def __init__(
        self,
        code: str = None,
        code_name: str = None,
        select_type: str = None,
        values: List[str] = None,
    ):
        self.code = code
        self.code_name = code_name
        self.select_type = select_type
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.code_name is not None:
            result['CodeName'] = self.code_name
        if self.select_type is not None:
            result['SelectType'] = self.select_type
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CodeName') is not None:
            self.code_name = m.get('CodeName')
        if m.get('SelectType') is not None:
            self.select_type = m.get('SelectType')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class DeleteCostCenterRuleRequestFilterExpression(TeaModel):
    def __init__(
        self,
        expression_type: str = None,
        filter_values: DeleteCostCenterRuleRequestFilterExpressionFilterValues = None,
        operand: Any = None,
        operands: List[Any] = None,
        operator_type: str = None,
    ):
        self.expression_type = expression_type
        self.filter_values = filter_values
        self.operand = operand
        self.operands = operands
        self.operator_type = operator_type

    def validate(self):
        if self.filter_values:
            self.filter_values.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expression_type is not None:
            result['ExpressionType'] = self.expression_type
        if self.filter_values is not None:
            result['FilterValues'] = self.filter_values.to_map()
        if self.operand is not None:
            result['Operand'] = self.operand
        if self.operands is not None:
            result['Operands'] = self.operands
        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpressionType') is not None:
            self.expression_type = m.get('ExpressionType')
        if m.get('FilterValues') is not None:
            temp_model = DeleteCostCenterRuleRequestFilterExpressionFilterValues()
            self.filter_values = temp_model.from_map(m['FilterValues'])
        if m.get('Operand') is not None:
            self.operand = m.get('Operand')
        if m.get('Operands') is not None:
            self.operands = m.get('Operands')
        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')
        return self


class DeleteCostCenterRuleRequest(TeaModel):
    def __init__(
        self,
        cost_center_id: int = None,
        filter_expression: DeleteCostCenterRuleRequestFilterExpression = None,
        nbid: str = None,
    ):
        self.cost_center_id = cost_center_id
        self.filter_expression = filter_expression
        self.nbid = nbid

    def validate(self):
        if self.filter_expression:
            self.filter_expression.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_center_id is not None:
            result['CostCenterId'] = self.cost_center_id
        if self.filter_expression is not None:
            result['FilterExpression'] = self.filter_expression.to_map()
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostCenterId') is not None:
            self.cost_center_id = m.get('CostCenterId')
        if m.get('FilterExpression') is not None:
            temp_model = DeleteCostCenterRuleRequestFilterExpression()
            self.filter_expression = temp_model.from_map(m['FilterExpression'])
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        return self


class DeleteCostCenterRuleShrinkRequest(TeaModel):
    def __init__(
        self,
        cost_center_id: int = None,
        filter_expression_shrink: str = None,
        nbid: str = None,
    ):
        self.cost_center_id = cost_center_id
        self.filter_expression_shrink = filter_expression_shrink
        self.nbid = nbid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_center_id is not None:
            result['CostCenterId'] = self.cost_center_id
        if self.filter_expression_shrink is not None:
            result['FilterExpression'] = self.filter_expression_shrink
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostCenterId') is not None:
            self.cost_center_id = m.get('CostCenterId')
        if m.get('FilterExpression') is not None:
            self.filter_expression_shrink = m.get('FilterExpression')
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        return self


class DeleteCostCenterRuleResponseBody(TeaModel):
    def __init__(
        self,
        data: int = None,
        metadata: Any = None,
        request_id: str = None,
    ):
        self.data = data
        self.metadata = metadata
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteCostCenterRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCostCenterRuleResponseBody = None,
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
            temp_model = DeleteCostCenterRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCouponDeductTagRequestEcIdAccountIds(TeaModel):
    def __init__(
        self,
        account_ids: List[int] = None,
        ec_id: str = None,
    ):
        self.account_ids = account_ids
        # This parameter is required.
        self.ec_id = ec_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids
        if self.ec_id is not None:
            result['EcId'] = self.ec_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')
        if m.get('EcId') is not None:
            self.ec_id = m.get('EcId')
        return self


class DeleteCouponDeductTagRequest(TeaModel):
    def __init__(
        self,
        coupon_id: str = None,
        ec_id_account_ids: List[DeleteCouponDeductTagRequestEcIdAccountIds] = None,
        nbid: str = None,
        tag_keys: List[str] = None,
    ):
        self.coupon_id = coupon_id
        self.ec_id_account_ids = ec_id_account_ids
        self.nbid = nbid
        self.tag_keys = tag_keys

    def validate(self):
        if self.ec_id_account_ids:
            for k in self.ec_id_account_ids:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coupon_id is not None:
            result['CouponId'] = self.coupon_id
        result['EcIdAccountIds'] = []
        if self.ec_id_account_ids is not None:
            for k in self.ec_id_account_ids:
                result['EcIdAccountIds'].append(k.to_map() if k else None)
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        if self.tag_keys is not None:
            result['TagKeys'] = self.tag_keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CouponId') is not None:
            self.coupon_id = m.get('CouponId')
        self.ec_id_account_ids = []
        if m.get('EcIdAccountIds') is not None:
            for k in m.get('EcIdAccountIds'):
                temp_model = DeleteCouponDeductTagRequestEcIdAccountIds()
                self.ec_id_account_ids.append(temp_model.from_map(k))
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        if m.get('TagKeys') is not None:
            self.tag_keys = m.get('TagKeys')
        return self


class DeleteCouponDeductTagShrinkRequest(TeaModel):
    def __init__(
        self,
        coupon_id: str = None,
        ec_id_account_ids_shrink: str = None,
        nbid: str = None,
        tag_keys_shrink: str = None,
    ):
        self.coupon_id = coupon_id
        self.ec_id_account_ids_shrink = ec_id_account_ids_shrink
        self.nbid = nbid
        self.tag_keys_shrink = tag_keys_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coupon_id is not None:
            result['CouponId'] = self.coupon_id
        if self.ec_id_account_ids_shrink is not None:
            result['EcIdAccountIds'] = self.ec_id_account_ids_shrink
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        if self.tag_keys_shrink is not None:
            result['TagKeys'] = self.tag_keys_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CouponId') is not None:
            self.coupon_id = m.get('CouponId')
        if m.get('EcIdAccountIds') is not None:
            self.ec_id_account_ids_shrink = m.get('EcIdAccountIds')
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        if m.get('TagKeys') is not None:
            self.tag_keys_shrink = m.get('TagKeys')
        return self


class DeleteCouponDeductTagResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteCouponDeductTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCouponDeductTagResponseBody = None,
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
            temp_model = DeleteCouponDeductTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteReportDefinitionRequest(TeaModel):
    def __init__(
        self,
        nbid: str = None,
        report_task_id: int = None,
    ):
        self.nbid = nbid
        # This parameter is required.
        self.report_task_id = report_task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        if self.report_task_id is not None:
            result['ReportTaskId'] = self.report_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        if m.get('ReportTaskId') is not None:
            self.report_task_id = m.get('ReportTaskId')
        return self


class DeleteReportDefinitionResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        metadata: Any = None,
        request_id: str = None,
    ):
        self.data = data
        self.metadata = metadata
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteReportDefinitionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteReportDefinitionResponseBody = None,
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
            temp_model = DeleteReportDefinitionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCouponRequestEcIdAccountIds(TeaModel):
    def __init__(
        self,
        account_ids: List[int] = None,
        ec_id: str = None,
    ):
        self.account_ids = account_ids
        # This parameter is required.
        self.ec_id = ec_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids
        if self.ec_id is not None:
            result['EcId'] = self.ec_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')
        if m.get('EcId') is not None:
            self.ec_id = m.get('EcId')
        return self


class DescribeCouponRequest(TeaModel):
    def __init__(
        self,
        coupon_id: int = None,
        coupon_no: str = None,
        coupon_type: str = None,
        current_page: int = None,
        ec_id_account_ids: List[DescribeCouponRequestEcIdAccountIds] = None,
        effective_end_time: int = None,
        effective_start_time: int = None,
        expire_end_date: int = None,
        expire_start_date: int = None,
        nbid: str = None,
        page_size: int = None,
        status: str = None,
    ):
        self.coupon_id = coupon_id
        self.coupon_no = coupon_no
        self.coupon_type = coupon_type
        # This parameter is required.
        self.current_page = current_page
        self.ec_id_account_ids = ec_id_account_ids
        self.effective_end_time = effective_end_time
        self.effective_start_time = effective_start_time
        self.expire_end_date = expire_end_date
        self.expire_start_date = expire_start_date
        self.nbid = nbid
        # This parameter is required.
        self.page_size = page_size
        self.status = status

    def validate(self):
        if self.ec_id_account_ids:
            for k in self.ec_id_account_ids:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coupon_id is not None:
            result['CouponId'] = self.coupon_id
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no
        if self.coupon_type is not None:
            result['CouponType'] = self.coupon_type
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['EcIdAccountIds'] = []
        if self.ec_id_account_ids is not None:
            for k in self.ec_id_account_ids:
                result['EcIdAccountIds'].append(k.to_map() if k else None)
        if self.effective_end_time is not None:
            result['EffectiveEndTime'] = self.effective_end_time
        if self.effective_start_time is not None:
            result['EffectiveStartTime'] = self.effective_start_time
        if self.expire_end_date is not None:
            result['ExpireEndDate'] = self.expire_end_date
        if self.expire_start_date is not None:
            result['ExpireStartDate'] = self.expire_start_date
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CouponId') is not None:
            self.coupon_id = m.get('CouponId')
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')
        if m.get('CouponType') is not None:
            self.coupon_type = m.get('CouponType')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.ec_id_account_ids = []
        if m.get('EcIdAccountIds') is not None:
            for k in m.get('EcIdAccountIds'):
                temp_model = DescribeCouponRequestEcIdAccountIds()
                self.ec_id_account_ids.append(temp_model.from_map(k))
        if m.get('EffectiveEndTime') is not None:
            self.effective_end_time = m.get('EffectiveEndTime')
        if m.get('EffectiveStartTime') is not None:
            self.effective_start_time = m.get('EffectiveStartTime')
        if m.get('ExpireEndDate') is not None:
            self.expire_end_date = m.get('ExpireEndDate')
        if m.get('ExpireStartDate') is not None:
            self.expire_start_date = m.get('ExpireStartDate')
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeCouponShrinkRequest(TeaModel):
    def __init__(
        self,
        coupon_id: int = None,
        coupon_no: str = None,
        coupon_type: str = None,
        current_page: int = None,
        ec_id_account_ids_shrink: str = None,
        effective_end_time: int = None,
        effective_start_time: int = None,
        expire_end_date: int = None,
        expire_start_date: int = None,
        nbid: str = None,
        page_size: int = None,
        status: str = None,
    ):
        self.coupon_id = coupon_id
        self.coupon_no = coupon_no
        self.coupon_type = coupon_type
        # This parameter is required.
        self.current_page = current_page
        self.ec_id_account_ids_shrink = ec_id_account_ids_shrink
        self.effective_end_time = effective_end_time
        self.effective_start_time = effective_start_time
        self.expire_end_date = expire_end_date
        self.expire_start_date = expire_start_date
        self.nbid = nbid
        # This parameter is required.
        self.page_size = page_size
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coupon_id is not None:
            result['CouponId'] = self.coupon_id
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no
        if self.coupon_type is not None:
            result['CouponType'] = self.coupon_type
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.ec_id_account_ids_shrink is not None:
            result['EcIdAccountIds'] = self.ec_id_account_ids_shrink
        if self.effective_end_time is not None:
            result['EffectiveEndTime'] = self.effective_end_time
        if self.effective_start_time is not None:
            result['EffectiveStartTime'] = self.effective_start_time
        if self.expire_end_date is not None:
            result['ExpireEndDate'] = self.expire_end_date
        if self.expire_start_date is not None:
            result['ExpireStartDate'] = self.expire_start_date
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CouponId') is not None:
            self.coupon_id = m.get('CouponId')
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')
        if m.get('CouponType') is not None:
            self.coupon_type = m.get('CouponType')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EcIdAccountIds') is not None:
            self.ec_id_account_ids_shrink = m.get('EcIdAccountIds')
        if m.get('EffectiveEndTime') is not None:
            self.effective_end_time = m.get('EffectiveEndTime')
        if m.get('EffectiveStartTime') is not None:
            self.effective_start_time = m.get('EffectiveStartTime')
        if m.get('ExpireEndDate') is not None:
            self.expire_end_date = m.get('ExpireEndDate')
        if m.get('ExpireStartDate') is not None:
            self.expire_start_date = m.get('ExpireStartDate')
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeCouponResponseBodyDataShareUidList(TeaModel):
    def __init__(
        self,
        uid: str = None,
        user_nick: str = None,
    ):
        self.uid = uid
        self.user_nick = user_nick

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.user_nick is not None:
            result['UserNick'] = self.user_nick
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('UserNick') is not None:
            self.user_nick = m.get('UserNick')
        return self


class DescribeCouponResponseBodyData(TeaModel):
    def __init__(
        self,
        amount: str = None,
        certain_amount: str = None,
        coupon_id: int = None,
        coupon_no: str = None,
        coupon_type: str = None,
        coupon_type_name: str = None,
        currency: str = None,
        end_time: str = None,
        gmt_create: str = None,
        item_names: List[str] = None,
        money_limit: str = None,
        order_time_rule: str = None,
        remain_amount: str = None,
        remark: str = None,
        share_uid_list: List[DescribeCouponResponseBodyDataShareUidList] = None,
        show_set_deduct_tag_button: bool = None,
        site: str = None,
        site_name: str = None,
        start_time: str = None,
        status: str = None,
        suit_account: str = None,
        suit_item_type: str = None,
        universal_type: str = None,
        yh_order_types: List[str] = None,
    ):
        self.amount = amount
        self.certain_amount = certain_amount
        self.coupon_id = coupon_id
        self.coupon_no = coupon_no
        self.coupon_type = coupon_type
        self.coupon_type_name = coupon_type_name
        self.currency = currency
        self.end_time = end_time
        self.gmt_create = gmt_create
        self.item_names = item_names
        self.money_limit = money_limit
        self.order_time_rule = order_time_rule
        self.remain_amount = remain_amount
        self.remark = remark
        self.share_uid_list = share_uid_list
        self.show_set_deduct_tag_button = show_set_deduct_tag_button
        self.site = site
        self.site_name = site_name
        self.start_time = start_time
        self.status = status
        self.suit_account = suit_account
        self.suit_item_type = suit_item_type
        self.universal_type = universal_type
        self.yh_order_types = yh_order_types

    def validate(self):
        if self.share_uid_list:
            for k in self.share_uid_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.certain_amount is not None:
            result['CertainAmount'] = self.certain_amount
        if self.coupon_id is not None:
            result['CouponId'] = self.coupon_id
        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no
        if self.coupon_type is not None:
            result['CouponType'] = self.coupon_type
        if self.coupon_type_name is not None:
            result['CouponTypeName'] = self.coupon_type_name
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.item_names is not None:
            result['ItemNames'] = self.item_names
        if self.money_limit is not None:
            result['MoneyLimit'] = self.money_limit
        if self.order_time_rule is not None:
            result['OrderTimeRule'] = self.order_time_rule
        if self.remain_amount is not None:
            result['RemainAmount'] = self.remain_amount
        if self.remark is not None:
            result['Remark'] = self.remark
        result['ShareUidList'] = []
        if self.share_uid_list is not None:
            for k in self.share_uid_list:
                result['ShareUidList'].append(k.to_map() if k else None)
        if self.show_set_deduct_tag_button is not None:
            result['ShowSetDeductTagButton'] = self.show_set_deduct_tag_button
        if self.site is not None:
            result['Site'] = self.site
        if self.site_name is not None:
            result['SiteName'] = self.site_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.suit_account is not None:
            result['SuitAccount'] = self.suit_account
        if self.suit_item_type is not None:
            result['SuitItemType'] = self.suit_item_type
        if self.universal_type is not None:
            result['UniversalType'] = self.universal_type
        if self.yh_order_types is not None:
            result['YhOrderTypes'] = self.yh_order_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('CertainAmount') is not None:
            self.certain_amount = m.get('CertainAmount')
        if m.get('CouponId') is not None:
            self.coupon_id = m.get('CouponId')
        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')
        if m.get('CouponType') is not None:
            self.coupon_type = m.get('CouponType')
        if m.get('CouponTypeName') is not None:
            self.coupon_type_name = m.get('CouponTypeName')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('ItemNames') is not None:
            self.item_names = m.get('ItemNames')
        if m.get('MoneyLimit') is not None:
            self.money_limit = m.get('MoneyLimit')
        if m.get('OrderTimeRule') is not None:
            self.order_time_rule = m.get('OrderTimeRule')
        if m.get('RemainAmount') is not None:
            self.remain_amount = m.get('RemainAmount')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        self.share_uid_list = []
        if m.get('ShareUidList') is not None:
            for k in m.get('ShareUidList'):
                temp_model = DescribeCouponResponseBodyDataShareUidList()
                self.share_uid_list.append(temp_model.from_map(k))
        if m.get('ShowSetDeductTagButton') is not None:
            self.show_set_deduct_tag_button = m.get('ShowSetDeductTagButton')
        if m.get('Site') is not None:
            self.site = m.get('Site')
        if m.get('SiteName') is not None:
            self.site_name = m.get('SiteName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SuitAccount') is not None:
            self.suit_account = m.get('SuitAccount')
        if m.get('SuitItemType') is not None:
            self.suit_item_type = m.get('SuitItemType')
        if m.get('UniversalType') is not None:
            self.universal_type = m.get('UniversalType')
        if m.get('YhOrderTypes') is not None:
            self.yh_order_types = m.get('YhOrderTypes')
        return self


class DescribeCouponResponseBody(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        data: List[DescribeCouponResponseBodyData] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.data = data
        self.page_size = page_size
        self.request_id = request_id
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
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
            for k in m.get('Data'):
                temp_model = DescribeCouponResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeCouponResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCouponResponseBody = None,
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
            temp_model = DescribeCouponResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCouponItemListRequestEcIdAccountIds(TeaModel):
    def __init__(
        self,
        account_ids: List[int] = None,
        ec_id: str = None,
    ):
        self.account_ids = account_ids
        # This parameter is required.
        self.ec_id = ec_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids
        if self.ec_id is not None:
            result['EcId'] = self.ec_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')
        if m.get('EcId') is not None:
            self.ec_id = m.get('EcId')
        return self


class DescribeCouponItemListRequest(TeaModel):
    def __init__(
        self,
        coupon_id: int = None,
        current_page: int = None,
        ec_id_account_ids: List[DescribeCouponItemListRequestEcIdAccountIds] = None,
        name: str = None,
        nbid: str = None,
        page_size: int = None,
    ):
        self.coupon_id = coupon_id
        self.current_page = current_page
        self.ec_id_account_ids = ec_id_account_ids
        self.name = name
        self.nbid = nbid
        self.page_size = page_size

    def validate(self):
        if self.ec_id_account_ids:
            for k in self.ec_id_account_ids:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coupon_id is not None:
            result['CouponId'] = self.coupon_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['EcIdAccountIds'] = []
        if self.ec_id_account_ids is not None:
            for k in self.ec_id_account_ids:
                result['EcIdAccountIds'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CouponId') is not None:
            self.coupon_id = m.get('CouponId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.ec_id_account_ids = []
        if m.get('EcIdAccountIds') is not None:
            for k in m.get('EcIdAccountIds'):
                temp_model = DescribeCouponItemListRequestEcIdAccountIds()
                self.ec_id_account_ids.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeCouponItemListShrinkRequest(TeaModel):
    def __init__(
        self,
        coupon_id: int = None,
        current_page: int = None,
        ec_id_account_ids_shrink: str = None,
        name: str = None,
        nbid: str = None,
        page_size: int = None,
    ):
        self.coupon_id = coupon_id
        self.current_page = current_page
        self.ec_id_account_ids_shrink = ec_id_account_ids_shrink
        self.name = name
        self.nbid = nbid
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coupon_id is not None:
            result['CouponId'] = self.coupon_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.ec_id_account_ids_shrink is not None:
            result['EcIdAccountIds'] = self.ec_id_account_ids_shrink
        if self.name is not None:
            result['Name'] = self.name
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CouponId') is not None:
            self.coupon_id = m.get('CouponId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EcIdAccountIds') is not None:
            self.ec_id_account_ids_shrink = m.get('EcIdAccountIds')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeCouponItemListResponseBodyData(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeCouponItemListResponseBody(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        data: List[DescribeCouponItemListResponseBodyData] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.data = data
        self.page_size = page_size
        self.request_id = request_id
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
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
            for k in m.get('Data'):
                temp_model = DescribeCouponItemListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeCouponItemListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCouponItemListResponseBody = None,
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
            temp_model = DescribeCouponItemListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserSpnSummaryInfoRequestEcIdAccountIds(TeaModel):
    def __init__(
        self,
        account_ids: List[int] = None,
        ec_id: str = None,
    ):
        self.account_ids = account_ids
        # This parameter is required.
        self.ec_id = ec_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids
        if self.ec_id is not None:
            result['EcId'] = self.ec_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')
        if m.get('EcId') is not None:
            self.ec_id = m.get('EcId')
        return self


class DescribeUserSpnSummaryInfoRequest(TeaModel):
    def __init__(
        self,
        ec_id_account_ids: List[DescribeUserSpnSummaryInfoRequestEcIdAccountIds] = None,
        nbid: str = None,
    ):
        self.ec_id_account_ids = ec_id_account_ids
        self.nbid = nbid

    def validate(self):
        if self.ec_id_account_ids:
            for k in self.ec_id_account_ids:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EcIdAccountIds'] = []
        if self.ec_id_account_ids is not None:
            for k in self.ec_id_account_ids:
                result['EcIdAccountIds'].append(k.to_map() if k else None)
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ec_id_account_ids = []
        if m.get('EcIdAccountIds') is not None:
            for k in m.get('EcIdAccountIds'):
                temp_model = DescribeUserSpnSummaryInfoRequestEcIdAccountIds()
                self.ec_id_account_ids.append(temp_model.from_map(k))
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        return self


class DescribeUserSpnSummaryInfoShrinkRequest(TeaModel):
    def __init__(
        self,
        ec_id_account_ids_shrink: str = None,
        nbid: str = None,
    ):
        self.ec_id_account_ids_shrink = ec_id_account_ids_shrink
        self.nbid = nbid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ec_id_account_ids_shrink is not None:
            result['EcIdAccountIds'] = self.ec_id_account_ids_shrink
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EcIdAccountIds') is not None:
            self.ec_id_account_ids_shrink = m.get('EcIdAccountIds')
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        return self


class DescribeUserSpnSummaryInfoResponseBodyRegionList(TeaModel):
    def __init__(
        self,
        region_code: str = None,
        region_name: str = None,
    ):
        self.region_code = region_code
        self.region_name = region_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_code is not None:
            result['RegionCode'] = self.region_code
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        return self


class DescribeUserSpnSummaryInfoResponseBodySpnCodeAndTypeList(TeaModel):
    def __init__(
        self,
        product_code: str = None,
        spn_commodity_code: str = None,
        spn_type: str = None,
        spn_type_name: str = None,
    ):
        self.product_code = product_code
        self.spn_commodity_code = spn_commodity_code
        self.spn_type = spn_type
        self.spn_type_name = spn_type_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.spn_commodity_code is not None:
            result['SpnCommodityCode'] = self.spn_commodity_code
        if self.spn_type is not None:
            result['SpnType'] = self.spn_type
        if self.spn_type_name is not None:
            result['SpnTypeName'] = self.spn_type_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('SpnCommodityCode') is not None:
            self.spn_commodity_code = m.get('SpnCommodityCode')
        if m.get('SpnType') is not None:
            self.spn_type = m.get('SpnType')
        if m.get('SpnTypeName') is not None:
            self.spn_type_name = m.get('SpnTypeName')
        return self


class DescribeUserSpnSummaryInfoResponseBody(TeaModel):
    def __init__(
        self,
        instance_family_list: List[str] = None,
        region_list: List[DescribeUserSpnSummaryInfoResponseBodyRegionList] = None,
        request_id: str = None,
        spn_code_and_type_list: List[DescribeUserSpnSummaryInfoResponseBodySpnCodeAndTypeList] = None,
    ):
        self.instance_family_list = instance_family_list
        self.region_list = region_list
        self.request_id = request_id
        self.spn_code_and_type_list = spn_code_and_type_list

    def validate(self):
        if self.region_list:
            for k in self.region_list:
                if k:
                    k.validate()
        if self.spn_code_and_type_list:
            for k in self.spn_code_and_type_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_family_list is not None:
            result['InstanceFamilyList'] = self.instance_family_list
        result['RegionList'] = []
        if self.region_list is not None:
            for k in self.region_list:
                result['RegionList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SpnCodeAndTypeList'] = []
        if self.spn_code_and_type_list is not None:
            for k in self.spn_code_and_type_list:
                result['SpnCodeAndTypeList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceFamilyList') is not None:
            self.instance_family_list = m.get('InstanceFamilyList')
        self.region_list = []
        if m.get('RegionList') is not None:
            for k in m.get('RegionList'):
                temp_model = DescribeUserSpnSummaryInfoResponseBodyRegionList()
                self.region_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.spn_code_and_type_list = []
        if m.get('SpnCodeAndTypeList') is not None:
            for k in m.get('SpnCodeAndTypeList'):
                temp_model = DescribeUserSpnSummaryInfoResponseBodySpnCodeAndTypeList()
                self.spn_code_and_type_list.append(temp_model.from_map(k))
        return self


class DescribeUserSpnSummaryInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeUserSpnSummaryInfoResponseBody = None,
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
            temp_model = DescribeUserSpnSummaryInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFundAccountAvailableAmountRequest(TeaModel):
    def __init__(
        self,
        fund_account_id: str = None,
    ):
        self.fund_account_id = fund_account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fund_account_id is not None:
            result['FundAccountId'] = self.fund_account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FundAccountId') is not None:
            self.fund_account_id = m.get('FundAccountId')
        return self


class GetFundAccountAvailableAmountResponseBodyExtendLedgerList(TeaModel):
    def __init__(
        self,
        currency: str = None,
        ledger_name: str = None,
        original_amount: str = None,
    ):
        self.currency = currency
        self.ledger_name = ledger_name
        self.original_amount = original_amount

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.ledger_name is not None:
            result['LedgerName'] = self.ledger_name
        if self.original_amount is not None:
            result['OriginalAmount'] = self.original_amount
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('LedgerName') is not None:
            self.ledger_name = m.get('LedgerName')
        if m.get('OriginalAmount') is not None:
            self.original_amount = m.get('OriginalAmount')
        return self


class GetFundAccountAvailableAmountResponseBodyOriginalCashAmountList(TeaModel):
    def __init__(
        self,
        amount: str = None,
        currency: str = None,
    ):
        self.amount = amount
        self.currency = currency

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.currency is not None:
            result['Currency'] = self.currency
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        return self


class GetFundAccountAvailableAmountResponseBody(TeaModel):
    def __init__(
        self,
        available_amount: str = None,
        available_credit_amount: str = None,
        bank_acceptance_amount: str = None,
        cash_amount: str = None,
        credit_amount: str = None,
        credit_refund_amount: str = None,
        credit_user: bool = None,
        currency: str = None,
        current_month_uncleared_amount: str = None,
        extend_ledger_list: List[GetFundAccountAvailableAmountResponseBodyExtendLedgerList] = None,
        fund_account_id: str = None,
        fund_account_owner_account_id: str = None,
        fund_account_status: str = None,
        fund_account_type: str = None,
        history_month_uncleared_amount: str = None,
        metadata: Any = None,
        negative_bill_amount: str = None,
        original_cash_amount_list: List[GetFundAccountAvailableAmountResponseBodyOriginalCashAmountList] = None,
        quota_amount: str = None,
        quota_consumed_amount: str = None,
        request_id: str = None,
        uncleared_amount: str = None,
    ):
        self.available_amount = available_amount
        self.available_credit_amount = available_credit_amount
        self.bank_acceptance_amount = bank_acceptance_amount
        self.cash_amount = cash_amount
        self.credit_amount = credit_amount
        self.credit_refund_amount = credit_refund_amount
        self.credit_user = credit_user
        self.currency = currency
        self.current_month_uncleared_amount = current_month_uncleared_amount
        self.extend_ledger_list = extend_ledger_list
        self.fund_account_id = fund_account_id
        self.fund_account_owner_account_id = fund_account_owner_account_id
        self.fund_account_status = fund_account_status
        self.fund_account_type = fund_account_type
        self.history_month_uncleared_amount = history_month_uncleared_amount
        self.metadata = metadata
        self.negative_bill_amount = negative_bill_amount
        self.original_cash_amount_list = original_cash_amount_list
        self.quota_amount = quota_amount
        self.quota_consumed_amount = quota_consumed_amount
        self.request_id = request_id
        self.uncleared_amount = uncleared_amount

    def validate(self):
        if self.extend_ledger_list:
            for k in self.extend_ledger_list:
                if k:
                    k.validate()
        if self.original_cash_amount_list:
            for k in self.original_cash_amount_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_amount is not None:
            result['AvailableAmount'] = self.available_amount
        if self.available_credit_amount is not None:
            result['AvailableCreditAmount'] = self.available_credit_amount
        if self.bank_acceptance_amount is not None:
            result['BankAcceptanceAmount'] = self.bank_acceptance_amount
        if self.cash_amount is not None:
            result['CashAmount'] = self.cash_amount
        if self.credit_amount is not None:
            result['CreditAmount'] = self.credit_amount
        if self.credit_refund_amount is not None:
            result['CreditRefundAmount'] = self.credit_refund_amount
        if self.credit_user is not None:
            result['CreditUser'] = self.credit_user
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.current_month_uncleared_amount is not None:
            result['CurrentMonthUnclearedAmount'] = self.current_month_uncleared_amount
        result['ExtendLedgerList'] = []
        if self.extend_ledger_list is not None:
            for k in self.extend_ledger_list:
                result['ExtendLedgerList'].append(k.to_map() if k else None)
        if self.fund_account_id is not None:
            result['FundAccountId'] = self.fund_account_id
        if self.fund_account_owner_account_id is not None:
            result['FundAccountOwnerAccountId'] = self.fund_account_owner_account_id
        if self.fund_account_status is not None:
            result['FundAccountStatus'] = self.fund_account_status
        if self.fund_account_type is not None:
            result['FundAccountType'] = self.fund_account_type
        if self.history_month_uncleared_amount is not None:
            result['HistoryMonthUnclearedAmount'] = self.history_month_uncleared_amount
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.negative_bill_amount is not None:
            result['NegativeBillAmount'] = self.negative_bill_amount
        result['OriginalCashAmountList'] = []
        if self.original_cash_amount_list is not None:
            for k in self.original_cash_amount_list:
                result['OriginalCashAmountList'].append(k.to_map() if k else None)
        if self.quota_amount is not None:
            result['QuotaAmount'] = self.quota_amount
        if self.quota_consumed_amount is not None:
            result['QuotaConsumedAmount'] = self.quota_consumed_amount
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.uncleared_amount is not None:
            result['UnclearedAmount'] = self.uncleared_amount
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableAmount') is not None:
            self.available_amount = m.get('AvailableAmount')
        if m.get('AvailableCreditAmount') is not None:
            self.available_credit_amount = m.get('AvailableCreditAmount')
        if m.get('BankAcceptanceAmount') is not None:
            self.bank_acceptance_amount = m.get('BankAcceptanceAmount')
        if m.get('CashAmount') is not None:
            self.cash_amount = m.get('CashAmount')
        if m.get('CreditAmount') is not None:
            self.credit_amount = m.get('CreditAmount')
        if m.get('CreditRefundAmount') is not None:
            self.credit_refund_amount = m.get('CreditRefundAmount')
        if m.get('CreditUser') is not None:
            self.credit_user = m.get('CreditUser')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('CurrentMonthUnclearedAmount') is not None:
            self.current_month_uncleared_amount = m.get('CurrentMonthUnclearedAmount')
        self.extend_ledger_list = []
        if m.get('ExtendLedgerList') is not None:
            for k in m.get('ExtendLedgerList'):
                temp_model = GetFundAccountAvailableAmountResponseBodyExtendLedgerList()
                self.extend_ledger_list.append(temp_model.from_map(k))
        if m.get('FundAccountId') is not None:
            self.fund_account_id = m.get('FundAccountId')
        if m.get('FundAccountOwnerAccountId') is not None:
            self.fund_account_owner_account_id = m.get('FundAccountOwnerAccountId')
        if m.get('FundAccountStatus') is not None:
            self.fund_account_status = m.get('FundAccountStatus')
        if m.get('FundAccountType') is not None:
            self.fund_account_type = m.get('FundAccountType')
        if m.get('HistoryMonthUnclearedAmount') is not None:
            self.history_month_uncleared_amount = m.get('HistoryMonthUnclearedAmount')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('NegativeBillAmount') is not None:
            self.negative_bill_amount = m.get('NegativeBillAmount')
        self.original_cash_amount_list = []
        if m.get('OriginalCashAmountList') is not None:
            for k in m.get('OriginalCashAmountList'):
                temp_model = GetFundAccountAvailableAmountResponseBodyOriginalCashAmountList()
                self.original_cash_amount_list.append(temp_model.from_map(k))
        if m.get('QuotaAmount') is not None:
            self.quota_amount = m.get('QuotaAmount')
        if m.get('QuotaConsumedAmount') is not None:
            self.quota_consumed_amount = m.get('QuotaConsumedAmount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UnclearedAmount') is not None:
            self.uncleared_amount = m.get('UnclearedAmount')
        return self


class GetFundAccountAvailableAmountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFundAccountAvailableAmountResponseBody = None,
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
            temp_model = GetFundAccountAvailableAmountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFundAccountCanAllocateCreditAmountRequest(TeaModel):
    def __init__(
        self,
        fund_account_id: int = None,
    ):
        self.fund_account_id = fund_account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fund_account_id is not None:
            result['FundAccountId'] = self.fund_account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FundAccountId') is not None:
            self.fund_account_id = m.get('FundAccountId')
        return self


class GetFundAccountCanAllocateCreditAmountResponseBody(TeaModel):
    def __init__(
        self,
        ecid: str = None,
        ecid_allocated_credit_amount: str = None,
        ecid_credit_amount: str = None,
        fund_account_ecid: str = None,
        fund_account_id: int = None,
        fund_account_name: str = None,
        fund_account_owner_account_id: int = None,
        max_can_allocate_credit_amount: str = None,
        metadata: Any = None,
        min_can_allocate_credit_amount: str = None,
        nbid: str = None,
        request_id: str = None,
        site: str = None,
    ):
        self.ecid = ecid
        self.ecid_allocated_credit_amount = ecid_allocated_credit_amount
        self.ecid_credit_amount = ecid_credit_amount
        self.fund_account_ecid = fund_account_ecid
        self.fund_account_id = fund_account_id
        self.fund_account_name = fund_account_name
        self.fund_account_owner_account_id = fund_account_owner_account_id
        self.max_can_allocate_credit_amount = max_can_allocate_credit_amount
        self.metadata = metadata
        self.min_can_allocate_credit_amount = min_can_allocate_credit_amount
        self.nbid = nbid
        self.request_id = request_id
        self.site = site

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ecid is not None:
            result['Ecid'] = self.ecid
        if self.ecid_allocated_credit_amount is not None:
            result['EcidAllocatedCreditAmount'] = self.ecid_allocated_credit_amount
        if self.ecid_credit_amount is not None:
            result['EcidCreditAmount'] = self.ecid_credit_amount
        if self.fund_account_ecid is not None:
            result['FundAccountEcid'] = self.fund_account_ecid
        if self.fund_account_id is not None:
            result['FundAccountId'] = self.fund_account_id
        if self.fund_account_name is not None:
            result['FundAccountName'] = self.fund_account_name
        if self.fund_account_owner_account_id is not None:
            result['FundAccountOwnerAccountId'] = self.fund_account_owner_account_id
        if self.max_can_allocate_credit_amount is not None:
            result['MaxCanAllocateCreditAmount'] = self.max_can_allocate_credit_amount
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.min_can_allocate_credit_amount is not None:
            result['MinCanAllocateCreditAmount'] = self.min_can_allocate_credit_amount
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.site is not None:
            result['Site'] = self.site
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ecid') is not None:
            self.ecid = m.get('Ecid')
        if m.get('EcidAllocatedCreditAmount') is not None:
            self.ecid_allocated_credit_amount = m.get('EcidAllocatedCreditAmount')
        if m.get('EcidCreditAmount') is not None:
            self.ecid_credit_amount = m.get('EcidCreditAmount')
        if m.get('FundAccountEcid') is not None:
            self.fund_account_ecid = m.get('FundAccountEcid')
        if m.get('FundAccountId') is not None:
            self.fund_account_id = m.get('FundAccountId')
        if m.get('FundAccountName') is not None:
            self.fund_account_name = m.get('FundAccountName')
        if m.get('FundAccountOwnerAccountId') is not None:
            self.fund_account_owner_account_id = m.get('FundAccountOwnerAccountId')
        if m.get('MaxCanAllocateCreditAmount') is not None:
            self.max_can_allocate_credit_amount = m.get('MaxCanAllocateCreditAmount')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('MinCanAllocateCreditAmount') is not None:
            self.min_can_allocate_credit_amount = m.get('MinCanAllocateCreditAmount')
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Site') is not None:
            self.site = m.get('Site')
        return self


class GetFundAccountCanAllocateCreditAmountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFundAccountCanAllocateCreditAmountResponseBody = None,
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
            temp_model = GetFundAccountCanAllocateCreditAmountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFundAccountCanRecycleAmountRequest(TeaModel):
    def __init__(
        self,
        currency: str = None,
        recycle_from_fund_account_id: str = None,
    ):
        # This parameter is required.
        self.currency = currency
        self.recycle_from_fund_account_id = recycle_from_fund_account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.recycle_from_fund_account_id is not None:
            result['RecycleFromFundAccountId'] = self.recycle_from_fund_account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('RecycleFromFundAccountId') is not None:
            self.recycle_from_fund_account_id = m.get('RecycleFromFundAccountId')
        return self


class GetFundAccountCanRecycleAmountResponseBodyRecycleToFundAccountList(TeaModel):
    def __init__(
        self,
        fund_account_id: str = None,
        fund_account_name: str = None,
        fund_account_owner_account_id: str = None,
        max_recyclable_amount: str = None,
        original_transfer_remain_amount: str = None,
    ):
        self.fund_account_id = fund_account_id
        self.fund_account_name = fund_account_name
        self.fund_account_owner_account_id = fund_account_owner_account_id
        self.max_recyclable_amount = max_recyclable_amount
        self.original_transfer_remain_amount = original_transfer_remain_amount

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fund_account_id is not None:
            result['FundAccountId'] = self.fund_account_id
        if self.fund_account_name is not None:
            result['FundAccountName'] = self.fund_account_name
        if self.fund_account_owner_account_id is not None:
            result['FundAccountOwnerAccountId'] = self.fund_account_owner_account_id
        if self.max_recyclable_amount is not None:
            result['MaxRecyclableAmount'] = self.max_recyclable_amount
        if self.original_transfer_remain_amount is not None:
            result['OriginalTransferRemainAmount'] = self.original_transfer_remain_amount
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FundAccountId') is not None:
            self.fund_account_id = m.get('FundAccountId')
        if m.get('FundAccountName') is not None:
            self.fund_account_name = m.get('FundAccountName')
        if m.get('FundAccountOwnerAccountId') is not None:
            self.fund_account_owner_account_id = m.get('FundAccountOwnerAccountId')
        if m.get('MaxRecyclableAmount') is not None:
            self.max_recyclable_amount = m.get('MaxRecyclableAmount')
        if m.get('OriginalTransferRemainAmount') is not None:
            self.original_transfer_remain_amount = m.get('OriginalTransferRemainAmount')
        return self


class GetFundAccountCanRecycleAmountResponseBody(TeaModel):
    def __init__(
        self,
        available_amount: str = None,
        currency: str = None,
        metadata: Any = None,
        recycle_from_fund_account_id: str = None,
        recycle_to_fund_account_list: List[GetFundAccountCanRecycleAmountResponseBodyRecycleToFundAccountList] = None,
        request_id: str = None,
        transfer_amount: str = None,
    ):
        self.available_amount = available_amount
        self.currency = currency
        self.metadata = metadata
        self.recycle_from_fund_account_id = recycle_from_fund_account_id
        self.recycle_to_fund_account_list = recycle_to_fund_account_list
        self.request_id = request_id
        self.transfer_amount = transfer_amount

    def validate(self):
        if self.recycle_to_fund_account_list:
            for k in self.recycle_to_fund_account_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_amount is not None:
            result['AvailableAmount'] = self.available_amount
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.recycle_from_fund_account_id is not None:
            result['RecycleFromFundAccountId'] = self.recycle_from_fund_account_id
        result['RecycleToFundAccountList'] = []
        if self.recycle_to_fund_account_list is not None:
            for k in self.recycle_to_fund_account_list:
                result['RecycleToFundAccountList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.transfer_amount is not None:
            result['TransferAmount'] = self.transfer_amount
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableAmount') is not None:
            self.available_amount = m.get('AvailableAmount')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('RecycleFromFundAccountId') is not None:
            self.recycle_from_fund_account_id = m.get('RecycleFromFundAccountId')
        self.recycle_to_fund_account_list = []
        if m.get('RecycleToFundAccountList') is not None:
            for k in m.get('RecycleToFundAccountList'):
                temp_model = GetFundAccountCanRecycleAmountResponseBodyRecycleToFundAccountList()
                self.recycle_to_fund_account_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TransferAmount') is not None:
            self.transfer_amount = m.get('TransferAmount')
        return self


class GetFundAccountCanRecycleAmountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFundAccountCanRecycleAmountResponseBody = None,
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
            temp_model = GetFundAccountCanRecycleAmountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFundAccountCanTransferAmountRequest(TeaModel):
    def __init__(
        self,
        currency: str = None,
        fund_account_id: str = None,
    ):
        # This parameter is required.
        self.currency = currency
        self.fund_account_id = fund_account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.fund_account_id is not None:
            result['FundAccountId'] = self.fund_account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('FundAccountId') is not None:
            self.fund_account_id = m.get('FundAccountId')
        return self


class GetFundAccountCanTransferAmountResponseBody(TeaModel):
    def __init__(
        self,
        available_amount: str = None,
        cash_amount: str = None,
        currency: str = None,
        fund_account_ecid: str = None,
        fund_account_id: int = None,
        fund_account_name: str = None,
        fund_account_owner_account_id: int = None,
        max_transferable_amount: str = None,
        metadata: Any = None,
        nbid: str = None,
        request_id: str = None,
        site: str = None,
        transfer_amount: str = None,
    ):
        self.available_amount = available_amount
        self.cash_amount = cash_amount
        self.currency = currency
        self.fund_account_ecid = fund_account_ecid
        self.fund_account_id = fund_account_id
        self.fund_account_name = fund_account_name
        self.fund_account_owner_account_id = fund_account_owner_account_id
        self.max_transferable_amount = max_transferable_amount
        self.metadata = metadata
        self.nbid = nbid
        self.request_id = request_id
        self.site = site
        self.transfer_amount = transfer_amount

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_amount is not None:
            result['AvailableAmount'] = self.available_amount
        if self.cash_amount is not None:
            result['CashAmount'] = self.cash_amount
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.fund_account_ecid is not None:
            result['FundAccountEcid'] = self.fund_account_ecid
        if self.fund_account_id is not None:
            result['FundAccountId'] = self.fund_account_id
        if self.fund_account_name is not None:
            result['FundAccountName'] = self.fund_account_name
        if self.fund_account_owner_account_id is not None:
            result['FundAccountOwnerAccountId'] = self.fund_account_owner_account_id
        if self.max_transferable_amount is not None:
            result['MaxTransferableAmount'] = self.max_transferable_amount
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.site is not None:
            result['Site'] = self.site
        if self.transfer_amount is not None:
            result['TransferAmount'] = self.transfer_amount
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableAmount') is not None:
            self.available_amount = m.get('AvailableAmount')
        if m.get('CashAmount') is not None:
            self.cash_amount = m.get('CashAmount')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('FundAccountEcid') is not None:
            self.fund_account_ecid = m.get('FundAccountEcid')
        if m.get('FundAccountId') is not None:
            self.fund_account_id = m.get('FundAccountId')
        if m.get('FundAccountName') is not None:
            self.fund_account_name = m.get('FundAccountName')
        if m.get('FundAccountOwnerAccountId') is not None:
            self.fund_account_owner_account_id = m.get('FundAccountOwnerAccountId')
        if m.get('MaxTransferableAmount') is not None:
            self.max_transferable_amount = m.get('MaxTransferableAmount')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Site') is not None:
            self.site = m.get('Site')
        if m.get('TransferAmount') is not None:
            self.transfer_amount = m.get('TransferAmount')
        return self


class GetFundAccountCanTransferAmountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFundAccountCanTransferAmountResponseBody = None,
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
            temp_model = GetFundAccountCanTransferAmountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFundAccountCanWithdrawAmountRequest(TeaModel):
    def __init__(
        self,
        fund_account_id: int = None,
    ):
        self.fund_account_id = fund_account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fund_account_id is not None:
            result['FundAccountId'] = self.fund_account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FundAccountId') is not None:
            self.fund_account_id = m.get('FundAccountId')
        return self


class GetFundAccountCanWithdrawAmountResponseBody(TeaModel):
    def __init__(
        self,
        can_original_withdraw_amount: str = None,
        can_withdraw_amount: str = None,
        cannot_original_withdraw_amount: str = None,
        cash_amount: str = None,
        credit_memo_amount: str = None,
        current_month_uncleared_amount: str = None,
        history_month_uncleared_amount: str = None,
        metadata: Any = None,
        pay_as_you_go_reversed_amount: str = None,
        request_id: str = None,
        transfer_amount: str = None,
    ):
        self.can_original_withdraw_amount = can_original_withdraw_amount
        self.can_withdraw_amount = can_withdraw_amount
        self.cannot_original_withdraw_amount = cannot_original_withdraw_amount
        self.cash_amount = cash_amount
        self.credit_memo_amount = credit_memo_amount
        self.current_month_uncleared_amount = current_month_uncleared_amount
        self.history_month_uncleared_amount = history_month_uncleared_amount
        self.metadata = metadata
        self.pay_as_you_go_reversed_amount = pay_as_you_go_reversed_amount
        self.request_id = request_id
        self.transfer_amount = transfer_amount

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_original_withdraw_amount is not None:
            result['CanOriginalWithdrawAmount'] = self.can_original_withdraw_amount
        if self.can_withdraw_amount is not None:
            result['CanWithdrawAmount'] = self.can_withdraw_amount
        if self.cannot_original_withdraw_amount is not None:
            result['CannotOriginalWithdrawAmount'] = self.cannot_original_withdraw_amount
        if self.cash_amount is not None:
            result['CashAmount'] = self.cash_amount
        if self.credit_memo_amount is not None:
            result['CreditMemoAmount'] = self.credit_memo_amount
        if self.current_month_uncleared_amount is not None:
            result['CurrentMonthUnclearedAmount'] = self.current_month_uncleared_amount
        if self.history_month_uncleared_amount is not None:
            result['HistoryMonthUnclearedAmount'] = self.history_month_uncleared_amount
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.pay_as_you_go_reversed_amount is not None:
            result['PayAsYouGoReversedAmount'] = self.pay_as_you_go_reversed_amount
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.transfer_amount is not None:
            result['TransferAmount'] = self.transfer_amount
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanOriginalWithdrawAmount') is not None:
            self.can_original_withdraw_amount = m.get('CanOriginalWithdrawAmount')
        if m.get('CanWithdrawAmount') is not None:
            self.can_withdraw_amount = m.get('CanWithdrawAmount')
        if m.get('CannotOriginalWithdrawAmount') is not None:
            self.cannot_original_withdraw_amount = m.get('CannotOriginalWithdrawAmount')
        if m.get('CashAmount') is not None:
            self.cash_amount = m.get('CashAmount')
        if m.get('CreditMemoAmount') is not None:
            self.credit_memo_amount = m.get('CreditMemoAmount')
        if m.get('CurrentMonthUnclearedAmount') is not None:
            self.current_month_uncleared_amount = m.get('CurrentMonthUnclearedAmount')
        if m.get('HistoryMonthUnclearedAmount') is not None:
            self.history_month_uncleared_amount = m.get('HistoryMonthUnclearedAmount')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('PayAsYouGoReversedAmount') is not None:
            self.pay_as_you_go_reversed_amount = m.get('PayAsYouGoReversedAmount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TransferAmount') is not None:
            self.transfer_amount = m.get('TransferAmount')
        return self


class GetFundAccountCanWithdrawAmountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFundAccountCanWithdrawAmountResponseBody = None,
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
            temp_model = GetFundAccountCanWithdrawAmountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFundAccountLowAvailableAmountAlarmRequest(TeaModel):
    def __init__(
        self,
        fund_account_id: int = None,
    ):
        self.fund_account_id = fund_account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fund_account_id is not None:
            result['FundAccountId'] = self.fund_account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FundAccountId') is not None:
            self.fund_account_id = m.get('FundAccountId')
        return self


class GetFundAccountLowAvailableAmountAlarmResponseBody(TeaModel):
    def __init__(
        self,
        alarm_enabled: bool = None,
        metadata: Any = None,
        request_id: str = None,
        threshold_amount: str = None,
    ):
        self.alarm_enabled = alarm_enabled
        self.metadata = metadata
        self.request_id = request_id
        self.threshold_amount = threshold_amount

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_enabled is not None:
            result['AlarmEnabled'] = self.alarm_enabled
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.threshold_amount is not None:
            result['ThresholdAmount'] = self.threshold_amount
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmEnabled') is not None:
            self.alarm_enabled = m.get('AlarmEnabled')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ThresholdAmount') is not None:
            self.threshold_amount = m.get('ThresholdAmount')
        return self


class GetFundAccountLowAvailableAmountAlarmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFundAccountLowAvailableAmountAlarmResponseBody = None,
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
            temp_model = GetFundAccountLowAvailableAmountAlarmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFundAccountTransactionDetailsRequest(TeaModel):
    def __init__(
        self,
        bill_number: str = None,
        channel_transaction_number: str = None,
        current_page: int = None,
        end_time: int = None,
        fund_account_id: int = None,
        page_size: int = None,
        start_time: int = None,
        transaction_channel_list: List[str] = None,
        transaction_direction: str = None,
        transaction_number: int = None,
        transaction_type: str = None,
        transaction_type_list: List[str] = None,
    ):
        self.bill_number = bill_number
        self.channel_transaction_number = channel_transaction_number
        self.current_page = current_page
        self.end_time = end_time
        self.fund_account_id = fund_account_id
        self.page_size = page_size
        self.start_time = start_time
        self.transaction_channel_list = transaction_channel_list
        self.transaction_direction = transaction_direction
        self.transaction_number = transaction_number
        self.transaction_type = transaction_type
        self.transaction_type_list = transaction_type_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_number is not None:
            result['BillNumber'] = self.bill_number
        if self.channel_transaction_number is not None:
            result['ChannelTransactionNumber'] = self.channel_transaction_number
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.fund_account_id is not None:
            result['FundAccountId'] = self.fund_account_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.transaction_channel_list is not None:
            result['TransactionChannelList'] = self.transaction_channel_list
        if self.transaction_direction is not None:
            result['TransactionDirection'] = self.transaction_direction
        if self.transaction_number is not None:
            result['TransactionNumber'] = self.transaction_number
        if self.transaction_type is not None:
            result['TransactionType'] = self.transaction_type
        if self.transaction_type_list is not None:
            result['TransactionTypeList'] = self.transaction_type_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillNumber') is not None:
            self.bill_number = m.get('BillNumber')
        if m.get('ChannelTransactionNumber') is not None:
            self.channel_transaction_number = m.get('ChannelTransactionNumber')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FundAccountId') is not None:
            self.fund_account_id = m.get('FundAccountId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TransactionChannelList') is not None:
            self.transaction_channel_list = m.get('TransactionChannelList')
        if m.get('TransactionDirection') is not None:
            self.transaction_direction = m.get('TransactionDirection')
        if m.get('TransactionNumber') is not None:
            self.transaction_number = m.get('TransactionNumber')
        if m.get('TransactionType') is not None:
            self.transaction_type = m.get('TransactionType')
        if m.get('TransactionTypeList') is not None:
            self.transaction_type_list = m.get('TransactionTypeList')
        return self


class GetFundAccountTransactionDetailsShrinkRequest(TeaModel):
    def __init__(
        self,
        bill_number: str = None,
        channel_transaction_number: str = None,
        current_page: int = None,
        end_time: int = None,
        fund_account_id: int = None,
        page_size: int = None,
        start_time: int = None,
        transaction_channel_list_shrink: str = None,
        transaction_direction: str = None,
        transaction_number: int = None,
        transaction_type: str = None,
        transaction_type_list_shrink: str = None,
    ):
        self.bill_number = bill_number
        self.channel_transaction_number = channel_transaction_number
        self.current_page = current_page
        self.end_time = end_time
        self.fund_account_id = fund_account_id
        self.page_size = page_size
        self.start_time = start_time
        self.transaction_channel_list_shrink = transaction_channel_list_shrink
        self.transaction_direction = transaction_direction
        self.transaction_number = transaction_number
        self.transaction_type = transaction_type
        self.transaction_type_list_shrink = transaction_type_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_number is not None:
            result['BillNumber'] = self.bill_number
        if self.channel_transaction_number is not None:
            result['ChannelTransactionNumber'] = self.channel_transaction_number
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.fund_account_id is not None:
            result['FundAccountId'] = self.fund_account_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.transaction_channel_list_shrink is not None:
            result['TransactionChannelList'] = self.transaction_channel_list_shrink
        if self.transaction_direction is not None:
            result['TransactionDirection'] = self.transaction_direction
        if self.transaction_number is not None:
            result['TransactionNumber'] = self.transaction_number
        if self.transaction_type is not None:
            result['TransactionType'] = self.transaction_type
        if self.transaction_type_list_shrink is not None:
            result['TransactionTypeList'] = self.transaction_type_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillNumber') is not None:
            self.bill_number = m.get('BillNumber')
        if m.get('ChannelTransactionNumber') is not None:
            self.channel_transaction_number = m.get('ChannelTransactionNumber')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FundAccountId') is not None:
            self.fund_account_id = m.get('FundAccountId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TransactionChannelList') is not None:
            self.transaction_channel_list_shrink = m.get('TransactionChannelList')
        if m.get('TransactionDirection') is not None:
            self.transaction_direction = m.get('TransactionDirection')
        if m.get('TransactionNumber') is not None:
            self.transaction_number = m.get('TransactionNumber')
        if m.get('TransactionType') is not None:
            self.transaction_type = m.get('TransactionType')
        if m.get('TransactionTypeList') is not None:
            self.transaction_type_list_shrink = m.get('TransactionTypeList')
        return self


class GetFundAccountTransactionDetailsResponseBodyData(TeaModel):
    def __init__(
        self,
        balance: str = None,
        bill_number: str = None,
        channel_transaction_number: str = None,
        currency: str = None,
        fund_account_ecid: str = None,
        fund_account_id: int = None,
        fund_account_name: str = None,
        fund_account_owner_account_id: int = None,
        fund_type: str = None,
        nbid: str = None,
        remark: str = None,
        site: str = None,
        transaction_account: str = None,
        transaction_amount: str = None,
        transaction_channel: str = None,
        transaction_direction: str = None,
        transaction_number: int = None,
        transaction_time: str = None,
        transaction_type: str = None,
    ):
        self.balance = balance
        self.bill_number = bill_number
        self.channel_transaction_number = channel_transaction_number
        self.currency = currency
        self.fund_account_ecid = fund_account_ecid
        self.fund_account_id = fund_account_id
        self.fund_account_name = fund_account_name
        self.fund_account_owner_account_id = fund_account_owner_account_id
        self.fund_type = fund_type
        self.nbid = nbid
        self.remark = remark
        self.site = site
        self.transaction_account = transaction_account
        self.transaction_amount = transaction_amount
        self.transaction_channel = transaction_channel
        self.transaction_direction = transaction_direction
        self.transaction_number = transaction_number
        self.transaction_time = transaction_time
        self.transaction_type = transaction_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.balance is not None:
            result['Balance'] = self.balance
        if self.bill_number is not None:
            result['BillNumber'] = self.bill_number
        if self.channel_transaction_number is not None:
            result['ChannelTransactionNumber'] = self.channel_transaction_number
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.fund_account_ecid is not None:
            result['FundAccountEcid'] = self.fund_account_ecid
        if self.fund_account_id is not None:
            result['FundAccountId'] = self.fund_account_id
        if self.fund_account_name is not None:
            result['FundAccountName'] = self.fund_account_name
        if self.fund_account_owner_account_id is not None:
            result['FundAccountOwnerAccountId'] = self.fund_account_owner_account_id
        if self.fund_type is not None:
            result['FundType'] = self.fund_type
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.site is not None:
            result['Site'] = self.site
        if self.transaction_account is not None:
            result['TransactionAccount'] = self.transaction_account
        if self.transaction_amount is not None:
            result['TransactionAmount'] = self.transaction_amount
        if self.transaction_channel is not None:
            result['TransactionChannel'] = self.transaction_channel
        if self.transaction_direction is not None:
            result['TransactionDirection'] = self.transaction_direction
        if self.transaction_number is not None:
            result['TransactionNumber'] = self.transaction_number
        if self.transaction_time is not None:
            result['TransactionTime'] = self.transaction_time
        if self.transaction_type is not None:
            result['TransactionType'] = self.transaction_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Balance') is not None:
            self.balance = m.get('Balance')
        if m.get('BillNumber') is not None:
            self.bill_number = m.get('BillNumber')
        if m.get('ChannelTransactionNumber') is not None:
            self.channel_transaction_number = m.get('ChannelTransactionNumber')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('FundAccountEcid') is not None:
            self.fund_account_ecid = m.get('FundAccountEcid')
        if m.get('FundAccountId') is not None:
            self.fund_account_id = m.get('FundAccountId')
        if m.get('FundAccountName') is not None:
            self.fund_account_name = m.get('FundAccountName')
        if m.get('FundAccountOwnerAccountId') is not None:
            self.fund_account_owner_account_id = m.get('FundAccountOwnerAccountId')
        if m.get('FundType') is not None:
            self.fund_type = m.get('FundType')
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Site') is not None:
            self.site = m.get('Site')
        if m.get('TransactionAccount') is not None:
            self.transaction_account = m.get('TransactionAccount')
        if m.get('TransactionAmount') is not None:
            self.transaction_amount = m.get('TransactionAmount')
        if m.get('TransactionChannel') is not None:
            self.transaction_channel = m.get('TransactionChannel')
        if m.get('TransactionDirection') is not None:
            self.transaction_direction = m.get('TransactionDirection')
        if m.get('TransactionNumber') is not None:
            self.transaction_number = m.get('TransactionNumber')
        if m.get('TransactionTime') is not None:
            self.transaction_time = m.get('TransactionTime')
        if m.get('TransactionType') is not None:
            self.transaction_type = m.get('TransactionType')
        return self


class GetFundAccountTransactionDetailsResponseBody(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        data: List[GetFundAccountTransactionDetailsResponseBodyData] = None,
        metadata: Any = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.data = data
        self.metadata = metadata
        self.page_size = page_size
        self.request_id = request_id
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
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.metadata is not None:
            result['Metadata'] = self.metadata
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
            for k in m.get('Data'):
                temp_model = GetFundAccountTransactionDetailsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetFundAccountTransactionDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFundAccountTransactionDetailsResponseBody = None,
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
            temp_model = GetFundAccountTransactionDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOrderDetailRequest(TeaModel):
    def __init__(
        self,
        member_uid: int = None,
        order_id: str = None,
        owner_id: int = None,
    ):
        self.member_uid = member_uid
        # This parameter is required.
        self.order_id = order_id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class GetOrderDetailResponseBodyDataOrderListOrderBillModuleConfigBillModuleConfigBillModulePropertiesBillModuleProperties(TeaModel):
    def __init__(
        self,
        attr_api_code: str = None,
        module_api_code: str = None,
        value: str = None,
    ):
        self.attr_api_code = attr_api_code
        self.module_api_code = module_api_code
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetOrderDetailResponseBodyDataOrderListOrderBillModuleConfigBillModuleConfigBillModuleProperties(TeaModel):
    def __init__(
        self,
        bill_module_properties: List[GetOrderDetailResponseBodyDataOrderListOrderBillModuleConfigBillModuleConfigBillModulePropertiesBillModuleProperties] = None,
    ):
        self.bill_module_properties = bill_module_properties

    def validate(self):
        if self.bill_module_properties:
            for k in self.bill_module_properties:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['billModuleProperties'] = []
        if self.bill_module_properties is not None:
            for k in self.bill_module_properties:
                result['billModuleProperties'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bill_module_properties = []
        if m.get('billModuleProperties') is not None:
            for k in m.get('billModuleProperties'):
                temp_model = GetOrderDetailResponseBodyDataOrderListOrderBillModuleConfigBillModuleConfigBillModulePropertiesBillModuleProperties()
                self.bill_module_properties.append(temp_model.from_map(k))
        return self


class GetOrderDetailResponseBodyDataOrderListOrderBillModuleConfigBillModuleConfig(TeaModel):
    def __init__(
        self,
        api_code: str = None,
        bill_module_properties: GetOrderDetailResponseBodyDataOrderListOrderBillModuleConfigBillModuleConfigBillModuleProperties = None,
        code: str = None,
        name: str = None,
    ):
        # apiCode
        self.api_code = api_code
        self.bill_module_properties = bill_module_properties
        self.code = code
        self.name = name

    def validate(self):
        if self.bill_module_properties:
            self.bill_module_properties.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetOrderDetailResponseBodyDataOrderListOrderBillModuleConfigBillModuleConfigBillModuleProperties()
            self.bill_module_properties = temp_model.from_map(m['BillModuleProperties'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetOrderDetailResponseBodyDataOrderListOrderBillModuleConfig(TeaModel):
    def __init__(
        self,
        bill_module_config: List[GetOrderDetailResponseBodyDataOrderListOrderBillModuleConfigBillModuleConfig] = None,
    ):
        self.bill_module_config = bill_module_config

    def validate(self):
        if self.bill_module_config:
            for k in self.bill_module_config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['billModuleConfig'] = []
        if self.bill_module_config is not None:
            for k in self.bill_module_config:
                result['billModuleConfig'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bill_module_config = []
        if m.get('billModuleConfig') is not None:
            for k in m.get('billModuleConfig'):
                temp_model = GetOrderDetailResponseBodyDataOrderListOrderBillModuleConfigBillModuleConfig()
                self.bill_module_config.append(temp_model.from_map(k))
        return self


class GetOrderDetailResponseBodyDataOrderListOrderOriginalModuleConfigOriginalModuleConfigModulePropertiesModuleProperties(TeaModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
        value: str = None,
    ):
        self.code = code
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetOrderDetailResponseBodyDataOrderListOrderOriginalModuleConfigOriginalModuleConfigModuleProperties(TeaModel):
    def __init__(
        self,
        module_properties: List[GetOrderDetailResponseBodyDataOrderListOrderOriginalModuleConfigOriginalModuleConfigModulePropertiesModuleProperties] = None,
    ):
        self.module_properties = module_properties

    def validate(self):
        if self.module_properties:
            for k in self.module_properties:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['moduleProperties'] = []
        if self.module_properties is not None:
            for k in self.module_properties:
                result['moduleProperties'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.module_properties = []
        if m.get('moduleProperties') is not None:
            for k in m.get('moduleProperties'):
                temp_model = GetOrderDetailResponseBodyDataOrderListOrderOriginalModuleConfigOriginalModuleConfigModulePropertiesModuleProperties()
                self.module_properties.append(temp_model.from_map(k))
        return self


class GetOrderDetailResponseBodyDataOrderListOrderOriginalModuleConfigOriginalModuleConfig(TeaModel):
    def __init__(
        self,
        code: str = None,
        module_properties: GetOrderDetailResponseBodyDataOrderListOrderOriginalModuleConfigOriginalModuleConfigModuleProperties = None,
        name: str = None,
    ):
        self.code = code
        self.module_properties = module_properties
        self.name = name

    def validate(self):
        if self.module_properties:
            self.module_properties.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetOrderDetailResponseBodyDataOrderListOrderOriginalModuleConfigOriginalModuleConfigModuleProperties()
            self.module_properties = temp_model.from_map(m['ModuleProperties'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetOrderDetailResponseBodyDataOrderListOrderOriginalModuleConfig(TeaModel):
    def __init__(
        self,
        original_module_config: List[GetOrderDetailResponseBodyDataOrderListOrderOriginalModuleConfigOriginalModuleConfig] = None,
    ):
        self.original_module_config = original_module_config

    def validate(self):
        if self.original_module_config:
            for k in self.original_module_config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['originalModuleConfig'] = []
        if self.original_module_config is not None:
            for k in self.original_module_config:
                result['originalModuleConfig'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.original_module_config = []
        if m.get('originalModuleConfig') is not None:
            for k in m.get('originalModuleConfig'):
                temp_model = GetOrderDetailResponseBodyDataOrderListOrderOriginalModuleConfigOriginalModuleConfig()
                self.original_module_config.append(temp_model.from_map(k))
        return self


class GetOrderDetailResponseBodyDataOrderListOrder(TeaModel):
    def __init__(
        self,
        after_tax_amount: str = None,
        bill_module_config: GetOrderDetailResponseBodyDataOrderListOrderBillModuleConfig = None,
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
        original_module_config: GetOrderDetailResponseBodyDataOrderListOrderOriginalModuleConfig = None,
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
        self.after_tax_amount = after_tax_amount
        self.bill_module_config = bill_module_config
        self.commodity_code = commodity_code
        self.config = config
        self.create_time = create_time
        self.currency = currency
        self.extend_infos = extend_infos
        self.instance_ids = instance_ids
        self.operator = operator
        self.order_id = order_id
        self.order_sub_type = order_sub_type
        self.order_type = order_type
        self.original_config = original_config
        self.original_module_config = original_module_config
        self.payment_currency = payment_currency
        self.payment_status = payment_status
        self.payment_time = payment_time
        self.pretax_amount = pretax_amount
        self.pretax_amount_local = pretax_amount_local
        self.pretax_gross_amount = pretax_gross_amount
        self.product_code = product_code
        self.product_type = product_type
        self.quantity = quantity
        self.region = region
        self.related_order_id = related_order_id
        self.sub_order_id = sub_order_id
        self.subscription_type = subscription_type
        self.tax = tax
        self.usage_end_time = usage_end_time
        self.usage_start_time = usage_start_time

    def validate(self):
        if self.bill_module_config:
            self.bill_module_config.validate()
        if self.original_module_config:
            self.original_module_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            result['InstanceIds'] = self.instance_ids
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
            temp_model = GetOrderDetailResponseBodyDataOrderListOrderBillModuleConfig()
            self.bill_module_config = temp_model.from_map(m['BillModuleConfig'])
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
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
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
            temp_model = GetOrderDetailResponseBodyDataOrderListOrderOriginalModuleConfig()
            self.original_module_config = temp_model.from_map(m['OriginalModuleConfig'])
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        host_name: str = None,
        order_list: GetOrderDetailResponseBodyDataOrderList = None,
        page_num: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.host_name = host_name
        self.order_list = order_list
        self.page_num = page_num
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.order_list:
            self.order_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetOrderDetailResponseBodyDataOrderList()
            self.order_list = temp_model.from_map(m['OrderList'])
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetOrderDetailResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetOrderDetailResponseBodyData = None,
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
            temp_model = GetOrderDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetOrderDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOrderDetailResponseBody = None,
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
            temp_model = GetOrderDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOrdersRequest(TeaModel):
    def __init__(
        self,
        create_time_end: str = None,
        create_time_start: str = None,
        member_uid: int = None,
        order_type: str = None,
        owner_id: int = None,
        page_num: int = None,
        page_size: int = None,
        payment_status: str = None,
        product_code: str = None,
        product_type: str = None,
        subscription_type: str = None,
    ):
        self.create_time_end = create_time_end
        self.create_time_start = create_time_start
        self.member_uid = member_uid
        self.order_type = order_type
        self.owner_id = owner_id
        self.page_num = page_num
        self.page_size = page_size
        self.payment_status = payment_status
        self.product_code = product_code
        self.product_type = product_type
        self.subscription_type = subscription_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time_end is not None:
            result['CreateTimeEnd'] = self.create_time_end
        if self.create_time_start is not None:
            result['CreateTimeStart'] = self.create_time_start
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.payment_status is not None:
            result['PaymentStatus'] = self.payment_status
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTimeEnd') is not None:
            self.create_time_end = m.get('CreateTimeEnd')
        if m.get('CreateTimeStart') is not None:
            self.create_time_start = m.get('CreateTimeStart')
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PaymentStatus') is not None:
            self.payment_status = m.get('PaymentStatus')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        return self


class GetOrdersResponseBodyDataOrderListOrder(TeaModel):
    def __init__(
        self,
        after_tax_amount: str = None,
        commodity_code: str = None,
        create_time: str = None,
        currency: str = None,
        order_id: str = None,
        order_type: str = None,
        payment_currency: str = None,
        payment_status: str = None,
        payment_time: str = None,
        pretax_amount: str = None,
        pretax_amount_local: str = None,
        pretax_gross_amount: str = None,
        product_code: str = None,
        product_type: str = None,
        related_order_id: str = None,
        subscription_type: str = None,
        tax: str = None,
    ):
        self.after_tax_amount = after_tax_amount
        self.commodity_code = commodity_code
        self.create_time = create_time
        self.currency = currency
        self.order_id = order_id
        self.order_type = order_type
        self.payment_currency = payment_currency
        self.payment_status = payment_status
        self.payment_time = payment_time
        self.pretax_amount = pretax_amount
        self.pretax_amount_local = pretax_amount_local
        self.pretax_gross_amount = pretax_gross_amount
        self.product_code = product_code
        self.product_type = product_type
        self.related_order_id = related_order_id
        self.subscription_type = subscription_type
        self.tax = tax

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.after_tax_amount is not None:
            result['AfterTaxAmount'] = self.after_tax_amount
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.order_type is not None:
            result['OrderType'] = self.order_type
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
        if self.related_order_id is not None:
            result['RelatedOrderId'] = self.related_order_id
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.tax is not None:
            result['Tax'] = self.tax
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AfterTaxAmount') is not None:
            self.after_tax_amount = m.get('AfterTaxAmount')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
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
        if m.get('RelatedOrderId') is not None:
            self.related_order_id = m.get('RelatedOrderId')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('Tax') is not None:
            self.tax = m.get('Tax')
        return self


class GetOrdersResponseBodyDataOrderList(TeaModel):
    def __init__(
        self,
        order: List[GetOrdersResponseBodyDataOrderListOrder] = None,
    ):
        self.order = order

    def validate(self):
        if self.order:
            for k in self.order:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
                temp_model = GetOrdersResponseBodyDataOrderListOrder()
                self.order.append(temp_model.from_map(k))
        return self


class GetOrdersResponseBodyData(TeaModel):
    def __init__(
        self,
        host_name: str = None,
        order_list: GetOrdersResponseBodyDataOrderList = None,
        page_num: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.host_name = host_name
        self.order_list = order_list
        self.page_num = page_num
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.order_list:
            self.order_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetOrdersResponseBodyDataOrderList()
            self.order_list = temp_model.from_map(m['OrderList'])
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetOrdersResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetOrdersResponseBodyData = None,
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
            temp_model = GetOrdersResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetOrdersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOrdersResponseBody = None,
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
            temp_model = GetOrdersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSavingPlanDeductableCommodityRequestEcIdAccountIds(TeaModel):
    def __init__(
        self,
        account_ids: List[int] = None,
        ec_id: str = None,
    ):
        self.account_ids = account_ids
        # This parameter is required.
        self.ec_id = ec_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids
        if self.ec_id is not None:
            result['EcId'] = self.ec_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')
        if m.get('EcId') is not None:
            self.ec_id = m.get('EcId')
        return self


class GetSavingPlanDeductableCommodityRequest(TeaModel):
    def __init__(
        self,
        ec_id_account_ids: List[GetSavingPlanDeductableCommodityRequestEcIdAccountIds] = None,
        nbid: str = None,
    ):
        self.ec_id_account_ids = ec_id_account_ids
        self.nbid = nbid

    def validate(self):
        if self.ec_id_account_ids:
            for k in self.ec_id_account_ids:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EcIdAccountIds'] = []
        if self.ec_id_account_ids is not None:
            for k in self.ec_id_account_ids:
                result['EcIdAccountIds'].append(k.to_map() if k else None)
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ec_id_account_ids = []
        if m.get('EcIdAccountIds') is not None:
            for k in m.get('EcIdAccountIds'):
                temp_model = GetSavingPlanDeductableCommodityRequestEcIdAccountIds()
                self.ec_id_account_ids.append(temp_model.from_map(k))
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        return self


class GetSavingPlanDeductableCommodityShrinkRequest(TeaModel):
    def __init__(
        self,
        ec_id_account_ids_shrink: str = None,
        nbid: str = None,
    ):
        self.ec_id_account_ids_shrink = ec_id_account_ids_shrink
        self.nbid = nbid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ec_id_account_ids_shrink is not None:
            result['EcIdAccountIds'] = self.ec_id_account_ids_shrink
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EcIdAccountIds') is not None:
            self.ec_id_account_ids_shrink = m.get('EcIdAccountIds')
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        return self


class GetSavingPlanDeductableCommodityResponseBodyDataCycleList(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetSavingPlanDeductableCommodityResponseBodyDataFilterModules(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetSavingPlanDeductableCommodityResponseBodyDataModuleMapListFilterModules(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetSavingPlanDeductableCommodityResponseBodyDataModuleMapListShowModules(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetSavingPlanDeductableCommodityResponseBodyDataModuleMapListSpnTypeNameList(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetSavingPlanDeductableCommodityResponseBodyDataModuleMapList(TeaModel):
    def __init__(
        self,
        filter_modules: List[GetSavingPlanDeductableCommodityResponseBodyDataModuleMapListFilterModules] = None,
        module_code: str = None,
        module_id: int = None,
        module_name: str = None,
        show_modules: List[GetSavingPlanDeductableCommodityResponseBodyDataModuleMapListShowModules] = None,
        spn_type_list: List[str] = None,
        spn_type_map_list: List[Dict[str, DataModuleMapListSpnTypeMapListValue]] = None,
        spn_type_name_list: List[GetSavingPlanDeductableCommodityResponseBodyDataModuleMapListSpnTypeNameList] = None,
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
            for k in self.filter_modules:
                if k:
                    k.validate()
        if self.show_modules:
            for k in self.show_modules:
                if k:
                    k.validate()
        if self.spn_type_name_list:
            for k in self.spn_type_name_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FilterModules'] = []
        if self.filter_modules is not None:
            for k in self.filter_modules:
                result['FilterModules'].append(k.to_map() if k else None)
        if self.module_code is not None:
            result['ModuleCode'] = self.module_code
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        result['ShowModules'] = []
        if self.show_modules is not None:
            for k in self.show_modules:
                result['ShowModules'].append(k.to_map() if k else None)
        if self.spn_type_list is not None:
            result['SpnTypeList'] = self.spn_type_list
        result['SpnTypeMapList'] = []
        if self.spn_type_map_list is not None:
            for k in self.spn_type_map_list:
                d1 = {}
                for k1 ,v1 in k.items():
                    d1[k1] = v1.to_map()
                result['SpnTypeMapList'].append(d1)
        result['SpnTypeNameList'] = []
        if self.spn_type_name_list is not None:
            for k in self.spn_type_name_list:
                result['SpnTypeNameList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filter_modules = []
        if m.get('FilterModules') is not None:
            for k in m.get('FilterModules'):
                temp_model = GetSavingPlanDeductableCommodityResponseBodyDataModuleMapListFilterModules()
                self.filter_modules.append(temp_model.from_map(k))
        if m.get('ModuleCode') is not None:
            self.module_code = m.get('ModuleCode')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        self.show_modules = []
        if m.get('ShowModules') is not None:
            for k in m.get('ShowModules'):
                temp_model = GetSavingPlanDeductableCommodityResponseBodyDataModuleMapListShowModules()
                self.show_modules.append(temp_model.from_map(k))
        if m.get('SpnTypeList') is not None:
            self.spn_type_list = m.get('SpnTypeList')
        self.spn_type_map_list = []
        if m.get('SpnTypeMapList') is not None:
            for k in m.get('SpnTypeMapList'):
                d1 = {}
                for k1, v1 in k.items():
                    temp_model = DataModuleMapListSpnTypeMapListValue()
                    d1[k1] = temp_model.from_map(v1)
                self.spn_type_map_list.append(d1)
        self.spn_type_name_list = []
        if m.get('SpnTypeNameList') is not None:
            for k in m.get('SpnTypeNameList'):
                temp_model = GetSavingPlanDeductableCommodityResponseBodyDataModuleMapListSpnTypeNameList()
                self.spn_type_name_list.append(temp_model.from_map(k))
        return self


class GetSavingPlanDeductableCommodityResponseBodyDataPayModeList(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetSavingPlanDeductableCommodityResponseBodyDataPricingModules(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetSavingPlanDeductableCommodityResponseBodyData(TeaModel):
    def __init__(
        self,
        activity_id: int = None,
        commodity_code: str = None,
        commodity_id: int = None,
        commodity_name: str = None,
        cycle_list: List[GetSavingPlanDeductableCommodityResponseBodyDataCycleList] = None,
        filter_modules: List[GetSavingPlanDeductableCommodityResponseBodyDataFilterModules] = None,
        item_code: str = None,
        item_id: int = None,
        item_name: str = None,
        module_map_list: List[GetSavingPlanDeductableCommodityResponseBodyDataModuleMapList] = None,
        pay_mode_list: List[GetSavingPlanDeductableCommodityResponseBodyDataPayModeList] = None,
        pricing_modules: List[GetSavingPlanDeductableCommodityResponseBodyDataPricingModules] = None,
        spn_commodity_code: str = None,
        spn_commodity_name: str = None,
        spn_discount_config_type: str = None,
        step_price_map: Dict[str, List[DataStepPriceMapValue]] = None,
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
            for k in self.cycle_list:
                if k:
                    k.validate()
        if self.filter_modules:
            for k in self.filter_modules:
                if k:
                    k.validate()
        if self.module_map_list:
            for k in self.module_map_list:
                if k:
                    k.validate()
        if self.pay_mode_list:
            for k in self.pay_mode_list:
                if k:
                    k.validate()
        if self.pricing_modules:
            for k in self.pricing_modules:
                if k:
                    k.validate()
        if self.step_price_map:
            for v in self.step_price_map.values():
                for k1 in v:
                    if k1:
                        k1.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            for k in self.cycle_list:
                result['CycleList'].append(k.to_map() if k else None)
        result['FilterModules'] = []
        if self.filter_modules is not None:
            for k in self.filter_modules:
                result['FilterModules'].append(k.to_map() if k else None)
        if self.item_code is not None:
            result['ItemCode'] = self.item_code
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.item_name is not None:
            result['ItemName'] = self.item_name
        result['ModuleMapList'] = []
        if self.module_map_list is not None:
            for k in self.module_map_list:
                result['ModuleMapList'].append(k.to_map() if k else None)
        result['PayModeList'] = []
        if self.pay_mode_list is not None:
            for k in self.pay_mode_list:
                result['PayModeList'].append(k.to_map() if k else None)
        result['PricingModules'] = []
        if self.pricing_modules is not None:
            for k in self.pricing_modules:
                result['PricingModules'].append(k.to_map() if k else None)
        if self.spn_commodity_code is not None:
            result['SpnCommodityCode'] = self.spn_commodity_code
        if self.spn_commodity_name is not None:
            result['SpnCommodityName'] = self.spn_commodity_name
        if self.spn_discount_config_type is not None:
            result['SpnDiscountConfigType'] = self.spn_discount_config_type
        result['StepPriceMap'] = {}
        if self.step_price_map is not None:
            for k, v in self.step_price_map.items():
                l1 = []
                for k1 in v:
                    l1.append(k1.to_map() if k1 else None)
                result['StepPriceMap'][k] = l1
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
            for k in m.get('CycleList'):
                temp_model = GetSavingPlanDeductableCommodityResponseBodyDataCycleList()
                self.cycle_list.append(temp_model.from_map(k))
        self.filter_modules = []
        if m.get('FilterModules') is not None:
            for k in m.get('FilterModules'):
                temp_model = GetSavingPlanDeductableCommodityResponseBodyDataFilterModules()
                self.filter_modules.append(temp_model.from_map(k))
        if m.get('ItemCode') is not None:
            self.item_code = m.get('ItemCode')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ItemName') is not None:
            self.item_name = m.get('ItemName')
        self.module_map_list = []
        if m.get('ModuleMapList') is not None:
            for k in m.get('ModuleMapList'):
                temp_model = GetSavingPlanDeductableCommodityResponseBodyDataModuleMapList()
                self.module_map_list.append(temp_model.from_map(k))
        self.pay_mode_list = []
        if m.get('PayModeList') is not None:
            for k in m.get('PayModeList'):
                temp_model = GetSavingPlanDeductableCommodityResponseBodyDataPayModeList()
                self.pay_mode_list.append(temp_model.from_map(k))
        self.pricing_modules = []
        if m.get('PricingModules') is not None:
            for k in m.get('PricingModules'):
                temp_model = GetSavingPlanDeductableCommodityResponseBodyDataPricingModules()
                self.pricing_modules.append(temp_model.from_map(k))
        if m.get('SpnCommodityCode') is not None:
            self.spn_commodity_code = m.get('SpnCommodityCode')
        if m.get('SpnCommodityName') is not None:
            self.spn_commodity_name = m.get('SpnCommodityName')
        if m.get('SpnDiscountConfigType') is not None:
            self.spn_discount_config_type = m.get('SpnDiscountConfigType')
        self.step_price_map = {}
        if m.get('StepPriceMap') is not None:
            for k, v in m.get('StepPriceMap').items():
                l1 = []
                for k1 in v:
                    temp_model = DataStepPriceMapValue()
                    l1.append(temp_model.from_map(k1))
                self.step_price_map['k'] = l1
        return self


class GetSavingPlanDeductableCommodityResponseBody(TeaModel):
    def __init__(
        self,
        data: List[GetSavingPlanDeductableCommodityResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetSavingPlanDeductableCommodityResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSavingPlanDeductableCommodityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSavingPlanDeductableCommodityResponseBody = None,
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
            temp_model = GetSavingPlanDeductableCommodityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSavingPlanShareAccountsRequestEcIdAccountIds(TeaModel):
    def __init__(
        self,
        account_ids: List[int] = None,
        ec_id: str = None,
    ):
        self.account_ids = account_ids
        # This parameter is required.
        self.ec_id = ec_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids
        if self.ec_id is not None:
            result['EcId'] = self.ec_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')
        if m.get('EcId') is not None:
            self.ec_id = m.get('EcId')
        return self


class GetSavingPlanShareAccountsRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        ec_id_account_ids: List[GetSavingPlanShareAccountsRequestEcIdAccountIds] = None,
        nbid: str = None,
        page_size: int = None,
        spn_instance_code: str = None,
    ):
        self.current_page = current_page
        self.ec_id_account_ids = ec_id_account_ids
        self.nbid = nbid
        self.page_size = page_size
        self.spn_instance_code = spn_instance_code

    def validate(self):
        if self.ec_id_account_ids:
            for k in self.ec_id_account_ids:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['EcIdAccountIds'] = []
        if self.ec_id_account_ids is not None:
            for k in self.ec_id_account_ids:
                result['EcIdAccountIds'].append(k.to_map() if k else None)
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.spn_instance_code is not None:
            result['SpnInstanceCode'] = self.spn_instance_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.ec_id_account_ids = []
        if m.get('EcIdAccountIds') is not None:
            for k in m.get('EcIdAccountIds'):
                temp_model = GetSavingPlanShareAccountsRequestEcIdAccountIds()
                self.ec_id_account_ids.append(temp_model.from_map(k))
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SpnInstanceCode') is not None:
            self.spn_instance_code = m.get('SpnInstanceCode')
        return self


class GetSavingPlanShareAccountsShrinkRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        ec_id_account_ids_shrink: str = None,
        nbid: str = None,
        page_size: int = None,
        spn_instance_code: str = None,
    ):
        self.current_page = current_page
        self.ec_id_account_ids_shrink = ec_id_account_ids_shrink
        self.nbid = nbid
        self.page_size = page_size
        self.spn_instance_code = spn_instance_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.ec_id_account_ids_shrink is not None:
            result['EcIdAccountIds'] = self.ec_id_account_ids_shrink
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.spn_instance_code is not None:
            result['SpnInstanceCode'] = self.spn_instance_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EcIdAccountIds') is not None:
            self.ec_id_account_ids_shrink = m.get('EcIdAccountIds')
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SpnInstanceCode') is not None:
            self.spn_instance_code = m.get('SpnInstanceCode')
        return self


class GetSavingPlanShareAccountsResponseBodyDataShareTimeList(TeaModel):
    def __init__(
        self,
        share_end_time: str = None,
        share_start_time: str = None,
    ):
        self.share_end_time = share_end_time
        self.share_start_time = share_start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.share_end_time is not None:
            result['ShareEndTime'] = self.share_end_time
        if self.share_start_time is not None:
            result['ShareStartTime'] = self.share_start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ShareEndTime') is not None:
            self.share_end_time = m.get('ShareEndTime')
        if m.get('ShareStartTime') is not None:
            self.share_start_time = m.get('ShareStartTime')
        return self


class GetSavingPlanShareAccountsResponseBodyData(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        ali_uid: int = None,
        share_time_list: List[GetSavingPlanShareAccountsResponseBodyDataShareTimeList] = None,
    ):
        self.account_id = account_id
        self.ali_uid = ali_uid
        self.share_time_list = share_time_list

    def validate(self):
        if self.share_time_list:
            for k in self.share_time_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        result['ShareTimeList'] = []
        if self.share_time_list is not None:
            for k in self.share_time_list:
                result['ShareTimeList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        self.share_time_list = []
        if m.get('ShareTimeList') is not None:
            for k in m.get('ShareTimeList'):
                temp_model = GetSavingPlanShareAccountsResponseBodyDataShareTimeList()
                self.share_time_list.append(temp_model.from_map(k))
        return self


class GetSavingPlanShareAccountsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[GetSavingPlanShareAccountsResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetSavingPlanShareAccountsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSavingPlanShareAccountsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSavingPlanShareAccountsResponseBody = None,
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
            temp_model = GetSavingPlanShareAccountsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSavingPlanUserDeductRuleRequestEcIdAccountIds(TeaModel):
    def __init__(
        self,
        account_ids: List[int] = None,
        ec_id: str = None,
    ):
        self.account_ids = account_ids
        # This parameter is required.
        self.ec_id = ec_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids
        if self.ec_id is not None:
            result['EcId'] = self.ec_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')
        if m.get('EcId') is not None:
            self.ec_id = m.get('EcId')
        return self


class GetSavingPlanUserDeductRuleRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        ec_id_account_ids: List[GetSavingPlanUserDeductRuleRequestEcIdAccountIds] = None,
        nbid: str = None,
        page_size: int = None,
        spn_instance_code: str = None,
    ):
        self.current_page = current_page
        self.ec_id_account_ids = ec_id_account_ids
        self.nbid = nbid
        self.page_size = page_size
        self.spn_instance_code = spn_instance_code

    def validate(self):
        if self.ec_id_account_ids:
            for k in self.ec_id_account_ids:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['EcIdAccountIds'] = []
        if self.ec_id_account_ids is not None:
            for k in self.ec_id_account_ids:
                result['EcIdAccountIds'].append(k.to_map() if k else None)
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.spn_instance_code is not None:
            result['SpnInstanceCode'] = self.spn_instance_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.ec_id_account_ids = []
        if m.get('EcIdAccountIds') is not None:
            for k in m.get('EcIdAccountIds'):
                temp_model = GetSavingPlanUserDeductRuleRequestEcIdAccountIds()
                self.ec_id_account_ids.append(temp_model.from_map(k))
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SpnInstanceCode') is not None:
            self.spn_instance_code = m.get('SpnInstanceCode')
        return self


class GetSavingPlanUserDeductRuleShrinkRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        ec_id_account_ids_shrink: str = None,
        nbid: str = None,
        page_size: int = None,
        spn_instance_code: str = None,
    ):
        self.current_page = current_page
        self.ec_id_account_ids_shrink = ec_id_account_ids_shrink
        self.nbid = nbid
        self.page_size = page_size
        self.spn_instance_code = spn_instance_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.ec_id_account_ids_shrink is not None:
            result['EcIdAccountIds'] = self.ec_id_account_ids_shrink
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.spn_instance_code is not None:
            result['SpnInstanceCode'] = self.spn_instance_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EcIdAccountIds') is not None:
            self.ec_id_account_ids_shrink = m.get('EcIdAccountIds')
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SpnInstanceCode') is not None:
            self.spn_instance_code = m.get('SpnInstanceCode')
        return self


class GetSavingPlanUserDeductRuleResponseBodyData(TeaModel):
    def __init__(
        self,
        commodity_code: str = None,
        commodity_name: str = None,
        module_code: str = None,
        module_name: str = None,
        skip_deduct: bool = None,
    ):
        self.commodity_code = commodity_code
        self.commodity_name = commodity_name
        self.module_code = module_code
        self.module_name = module_name
        self.skip_deduct = skip_deduct

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
        if self.module_code is not None:
            result['ModuleCode'] = self.module_code
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        if self.skip_deduct is not None:
            result['SkipDeduct'] = self.skip_deduct
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('CommodityName') is not None:
            self.commodity_name = m.get('CommodityName')
        if m.get('ModuleCode') is not None:
            self.module_code = m.get('ModuleCode')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        if m.get('SkipDeduct') is not None:
            self.skip_deduct = m.get('SkipDeduct')
        return self


class GetSavingPlanUserDeductRuleResponseBody(TeaModel):
    def __init__(
        self,
        data: List[GetSavingPlanUserDeductRuleResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetSavingPlanUserDeductRuleResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSavingPlanUserDeductRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSavingPlanUserDeductRuleResponseBody = None,
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
            temp_model = GetSavingPlanUserDeductRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCouponDeductTagRequestEcIdAccountIds(TeaModel):
    def __init__(
        self,
        account_ids: List[int] = None,
        ec_id: str = None,
    ):
        self.account_ids = account_ids
        # This parameter is required.
        self.ec_id = ec_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids
        if self.ec_id is not None:
            result['EcId'] = self.ec_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')
        if m.get('EcId') is not None:
            self.ec_id = m.get('EcId')
        return self


class ListCouponDeductTagRequest(TeaModel):
    def __init__(
        self,
        coupon_id: str = None,
        ec_id_account_ids: List[ListCouponDeductTagRequestEcIdAccountIds] = None,
        nbid: str = None,
    ):
        self.coupon_id = coupon_id
        self.ec_id_account_ids = ec_id_account_ids
        self.nbid = nbid

    def validate(self):
        if self.ec_id_account_ids:
            for k in self.ec_id_account_ids:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coupon_id is not None:
            result['CouponId'] = self.coupon_id
        result['EcIdAccountIds'] = []
        if self.ec_id_account_ids is not None:
            for k in self.ec_id_account_ids:
                result['EcIdAccountIds'].append(k.to_map() if k else None)
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CouponId') is not None:
            self.coupon_id = m.get('CouponId')
        self.ec_id_account_ids = []
        if m.get('EcIdAccountIds') is not None:
            for k in m.get('EcIdAccountIds'):
                temp_model = ListCouponDeductTagRequestEcIdAccountIds()
                self.ec_id_account_ids.append(temp_model.from_map(k))
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        return self


class ListCouponDeductTagShrinkRequest(TeaModel):
    def __init__(
        self,
        coupon_id: str = None,
        ec_id_account_ids_shrink: str = None,
        nbid: str = None,
    ):
        self.coupon_id = coupon_id
        self.ec_id_account_ids_shrink = ec_id_account_ids_shrink
        self.nbid = nbid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coupon_id is not None:
            result['CouponId'] = self.coupon_id
        if self.ec_id_account_ids_shrink is not None:
            result['EcIdAccountIds'] = self.ec_id_account_ids_shrink
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CouponId') is not None:
            self.coupon_id = m.get('CouponId')
        if m.get('EcIdAccountIds') is not None:
            self.ec_id_account_ids_shrink = m.get('EcIdAccountIds')
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        return self


class ListCouponDeductTagResponseBodyData(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class ListCouponDeductTagResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListCouponDeductTagResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListCouponDeductTagResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListCouponDeductTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCouponDeductTagResponseBody = None,
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
            temp_model = ListCouponDeductTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFundAccountRequest(TeaModel):
    def __init__(
        self,
        nbid: str = None,
        query_only_in_use: bool = None,
        query_only_manage: bool = None,
    ):
        self.nbid = nbid
        self.query_only_in_use = query_only_in_use
        self.query_only_manage = query_only_manage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        if self.query_only_in_use is not None:
            result['QueryOnlyInUse'] = self.query_only_in_use
        if self.query_only_manage is not None:
            result['QueryOnlyManage'] = self.query_only_manage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        if m.get('QueryOnlyInUse') is not None:
            self.query_only_in_use = m.get('QueryOnlyInUse')
        if m.get('QueryOnlyManage') is not None:
            self.query_only_manage = m.get('QueryOnlyManage')
        return self


class ListFundAccountResponseBodyData(TeaModel):
    def __init__(
        self,
        create_date: str = None,
        fund_account_admin_account_id: str = None,
        fund_account_admin_account_name: str = None,
        fund_account_id: str = None,
        fund_account_name: str = None,
        fund_account_owner_account_id: str = None,
        fund_account_status: str = None,
        fund_account_type: str = None,
        nbid: str = None,
        permissions: List[str] = None,
        site: str = None,
    ):
        self.create_date = create_date
        self.fund_account_admin_account_id = fund_account_admin_account_id
        self.fund_account_admin_account_name = fund_account_admin_account_name
        self.fund_account_id = fund_account_id
        self.fund_account_name = fund_account_name
        self.fund_account_owner_account_id = fund_account_owner_account_id
        self.fund_account_status = fund_account_status
        self.fund_account_type = fund_account_type
        self.nbid = nbid
        self.permissions = permissions
        self.site = site

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.fund_account_admin_account_id is not None:
            result['FundAccountAdminAccountId'] = self.fund_account_admin_account_id
        if self.fund_account_admin_account_name is not None:
            result['FundAccountAdminAccountName'] = self.fund_account_admin_account_name
        if self.fund_account_id is not None:
            result['FundAccountId'] = self.fund_account_id
        if self.fund_account_name is not None:
            result['FundAccountName'] = self.fund_account_name
        if self.fund_account_owner_account_id is not None:
            result['FundAccountOwnerAccountId'] = self.fund_account_owner_account_id
        if self.fund_account_status is not None:
            result['FundAccountStatus'] = self.fund_account_status
        if self.fund_account_type is not None:
            result['FundAccountType'] = self.fund_account_type
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        if self.permissions is not None:
            result['Permissions'] = self.permissions
        if self.site is not None:
            result['Site'] = self.site
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('FundAccountAdminAccountId') is not None:
            self.fund_account_admin_account_id = m.get('FundAccountAdminAccountId')
        if m.get('FundAccountAdminAccountName') is not None:
            self.fund_account_admin_account_name = m.get('FundAccountAdminAccountName')
        if m.get('FundAccountId') is not None:
            self.fund_account_id = m.get('FundAccountId')
        if m.get('FundAccountName') is not None:
            self.fund_account_name = m.get('FundAccountName')
        if m.get('FundAccountOwnerAccountId') is not None:
            self.fund_account_owner_account_id = m.get('FundAccountOwnerAccountId')
        if m.get('FundAccountStatus') is not None:
            self.fund_account_status = m.get('FundAccountStatus')
        if m.get('FundAccountType') is not None:
            self.fund_account_type = m.get('FundAccountType')
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        if m.get('Permissions') is not None:
            self.permissions = m.get('Permissions')
        if m.get('Site') is not None:
            self.site = m.get('Site')
        return self


class ListFundAccountResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListFundAccountResponseBodyData] = None,
        metadata: Any = None,
        request_id: str = None,
    ):
        self.data = data
        self.metadata = metadata
        self.request_id = request_id

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
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListFundAccountResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListFundAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFundAccountResponseBody = None,
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
            temp_model = ListFundAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFundAccountPayRelationRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        fund_account_id: str = None,
        nbid: str = None,
        page_size: int = None,
        status: str = None,
    ):
        self.current_page = current_page
        # This parameter is required.
        self.fund_account_id = fund_account_id
        self.nbid = nbid
        self.page_size = page_size
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.fund_account_id is not None:
            result['FundAccountId'] = self.fund_account_id
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('FundAccountId') is not None:
            self.fund_account_id = m.get('FundAccountId')
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListFundAccountPayRelationResponseBodyData(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        account_name: str = None,
        ecid: str = None,
        effective_time: str = None,
        fund_account_id: str = None,
        fund_account_owner_account_id: str = None,
        ineffective_time: str = None,
        nbid: str = None,
        operator_name: str = None,
        operator_no: str = None,
        operator_type: str = None,
        relation_type: str = None,
        site: str = None,
        status: str = None,
    ):
        self.account_id = account_id
        self.account_name = account_name
        self.ecid = ecid
        self.effective_time = effective_time
        self.fund_account_id = fund_account_id
        self.fund_account_owner_account_id = fund_account_owner_account_id
        self.ineffective_time = ineffective_time
        self.nbid = nbid
        self.operator_name = operator_name
        self.operator_no = operator_no
        self.operator_type = operator_type
        self.relation_type = relation_type
        self.site = site
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.ecid is not None:
            result['Ecid'] = self.ecid
        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time
        if self.fund_account_id is not None:
            result['FundAccountId'] = self.fund_account_id
        if self.fund_account_owner_account_id is not None:
            result['FundAccountOwnerAccountId'] = self.fund_account_owner_account_id
        if self.ineffective_time is not None:
            result['IneffectiveTime'] = self.ineffective_time
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        if self.operator_name is not None:
            result['OperatorName'] = self.operator_name
        if self.operator_no is not None:
            result['OperatorNo'] = self.operator_no
        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type
        if self.relation_type is not None:
            result['RelationType'] = self.relation_type
        if self.site is not None:
            result['Site'] = self.site
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('Ecid') is not None:
            self.ecid = m.get('Ecid')
        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')
        if m.get('FundAccountId') is not None:
            self.fund_account_id = m.get('FundAccountId')
        if m.get('FundAccountOwnerAccountId') is not None:
            self.fund_account_owner_account_id = m.get('FundAccountOwnerAccountId')
        if m.get('IneffectiveTime') is not None:
            self.ineffective_time = m.get('IneffectiveTime')
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        if m.get('OperatorName') is not None:
            self.operator_name = m.get('OperatorName')
        if m.get('OperatorNo') is not None:
            self.operator_no = m.get('OperatorNo')
        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')
        if m.get('RelationType') is not None:
            self.relation_type = m.get('RelationType')
        if m.get('Site') is not None:
            self.site = m.get('Site')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListFundAccountPayRelationResponseBody(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        data: List[ListFundAccountPayRelationResponseBodyData] = None,
        metadata: Any = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.data = data
        self.metadata = metadata
        self.page_size = page_size
        self.request_id = request_id
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
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.metadata is not None:
            result['Metadata'] = self.metadata
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
            for k in m.get('Data'):
                temp_model = ListFundAccountPayRelationResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListFundAccountPayRelationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFundAccountPayRelationResponseBody = None,
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
            temp_model = ListFundAccountPayRelationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInvoiceCandidateRequestEcIdAccountIds(TeaModel):
    def __init__(
        self,
        account_ids: List[int] = None,
        ec_id: str = None,
    ):
        self.account_ids = account_ids
        self.ec_id = ec_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids
        if self.ec_id is not None:
            result['EcId'] = self.ec_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')
        if m.get('EcId') is not None:
            self.ec_id = m.get('EcId')
        return self


class ListInvoiceCandidateRequest(TeaModel):
    def __init__(
        self,
        billing_cycles: List[int] = None,
        business_ids: List[str] = None,
        current_page: int = None,
        ec_id_account_ids: List[ListInvoiceCandidateRequestEcIdAccountIds] = None,
        end_time: str = None,
        invoice_issuers: List[str] = None,
        nbid: str = None,
        page_size: int = None,
        start_time: str = None,
        status: List[int] = None,
        types: List[int] = None,
    ):
        self.billing_cycles = billing_cycles
        self.business_ids = business_ids
        self.current_page = current_page
        self.ec_id_account_ids = ec_id_account_ids
        self.end_time = end_time
        self.invoice_issuers = invoice_issuers
        self.nbid = nbid
        self.page_size = page_size
        self.start_time = start_time
        self.status = status
        self.types = types

    def validate(self):
        if self.ec_id_account_ids:
            for k in self.ec_id_account_ids:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_cycles is not None:
            result['BillingCycles'] = self.billing_cycles
        if self.business_ids is not None:
            result['BusinessIds'] = self.business_ids
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['EcIdAccountIds'] = []
        if self.ec_id_account_ids is not None:
            for k in self.ec_id_account_ids:
                result['EcIdAccountIds'].append(k.to_map() if k else None)
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.invoice_issuers is not None:
            result['InvoiceIssuers'] = self.invoice_issuers
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.types is not None:
            result['Types'] = self.types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillingCycles') is not None:
            self.billing_cycles = m.get('BillingCycles')
        if m.get('BusinessIds') is not None:
            self.business_ids = m.get('BusinessIds')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.ec_id_account_ids = []
        if m.get('EcIdAccountIds') is not None:
            for k in m.get('EcIdAccountIds'):
                temp_model = ListInvoiceCandidateRequestEcIdAccountIds()
                self.ec_id_account_ids.append(temp_model.from_map(k))
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InvoiceIssuers') is not None:
            self.invoice_issuers = m.get('InvoiceIssuers')
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Types') is not None:
            self.types = m.get('Types')
        return self


class ListInvoiceCandidateShrinkRequest(TeaModel):
    def __init__(
        self,
        billing_cycles_shrink: str = None,
        business_ids_shrink: str = None,
        current_page: int = None,
        ec_id_account_ids_shrink: str = None,
        end_time: str = None,
        invoice_issuers_shrink: str = None,
        nbid: str = None,
        page_size: int = None,
        start_time: str = None,
        status_shrink: str = None,
        types_shrink: str = None,
    ):
        self.billing_cycles_shrink = billing_cycles_shrink
        self.business_ids_shrink = business_ids_shrink
        self.current_page = current_page
        self.ec_id_account_ids_shrink = ec_id_account_ids_shrink
        self.end_time = end_time
        self.invoice_issuers_shrink = invoice_issuers_shrink
        self.nbid = nbid
        self.page_size = page_size
        self.start_time = start_time
        self.status_shrink = status_shrink
        self.types_shrink = types_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_cycles_shrink is not None:
            result['BillingCycles'] = self.billing_cycles_shrink
        if self.business_ids_shrink is not None:
            result['BusinessIds'] = self.business_ids_shrink
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.ec_id_account_ids_shrink is not None:
            result['EcIdAccountIds'] = self.ec_id_account_ids_shrink
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.invoice_issuers_shrink is not None:
            result['InvoiceIssuers'] = self.invoice_issuers_shrink
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status_shrink is not None:
            result['Status'] = self.status_shrink
        if self.types_shrink is not None:
            result['Types'] = self.types_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillingCycles') is not None:
            self.billing_cycles_shrink = m.get('BillingCycles')
        if m.get('BusinessIds') is not None:
            self.business_ids_shrink = m.get('BusinessIds')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EcIdAccountIds') is not None:
            self.ec_id_account_ids_shrink = m.get('EcIdAccountIds')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InvoiceIssuers') is not None:
            self.invoice_issuers_shrink = m.get('InvoiceIssuers')
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status_shrink = m.get('Status')
        if m.get('Types') is not None:
            self.types_shrink = m.get('Types')
        return self


class ListInvoiceCandidateResponseBodyData(TeaModel):
    def __init__(
        self,
        accepted_offset_amount: str = None,
        account_id: int = None,
        account_name: str = None,
        billing_cycle: int = None,
        business_id: str = None,
        business_time: str = None,
        commodity_code: str = None,
        commodity_name: str = None,
        create_time: str = None,
        id: str = None,
        invoice_issuer: str = None,
        invoiceable_amount: str = None,
        invoiced_amount: str = None,
        offset_amount: str = None,
        product_code: str = None,
        product_name: str = None,
        resource_owner_account_id: int = None,
        resource_owner_account_name: str = None,
        status: int = None,
        total_amount: str = None,
        type: int = None,
    ):
        self.accepted_offset_amount = accepted_offset_amount
        self.account_id = account_id
        self.account_name = account_name
        self.billing_cycle = billing_cycle
        self.business_id = business_id
        self.business_time = business_time
        self.commodity_code = commodity_code
        self.commodity_name = commodity_name
        self.create_time = create_time
        self.id = id
        self.invoice_issuer = invoice_issuer
        self.invoiceable_amount = invoiceable_amount
        self.invoiced_amount = invoiced_amount
        self.offset_amount = offset_amount
        self.product_code = product_code
        self.product_name = product_name
        self.resource_owner_account_id = resource_owner_account_id
        self.resource_owner_account_name = resource_owner_account_name
        self.status = status
        self.total_amount = total_amount
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accepted_offset_amount is not None:
            result['AcceptedOffsetAmount'] = self.accepted_offset_amount
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle
        if self.business_id is not None:
            result['BusinessId'] = self.business_id
        if self.business_time is not None:
            result['BusinessTime'] = self.business_time
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.commodity_name is not None:
            result['CommodityName'] = self.commodity_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.id is not None:
            result['Id'] = self.id
        if self.invoice_issuer is not None:
            result['InvoiceIssuer'] = self.invoice_issuer
        if self.invoiceable_amount is not None:
            result['InvoiceableAmount'] = self.invoiceable_amount
        if self.invoiced_amount is not None:
            result['InvoicedAmount'] = self.invoiced_amount
        if self.offset_amount is not None:
            result['OffsetAmount'] = self.offset_amount
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.resource_owner_account_id is not None:
            result['ResourceOwnerAccountId'] = self.resource_owner_account_id
        if self.resource_owner_account_name is not None:
            result['ResourceOwnerAccountName'] = self.resource_owner_account_name
        if self.status is not None:
            result['Status'] = self.status
        if self.total_amount is not None:
            result['TotalAmount'] = self.total_amount
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptedOffsetAmount') is not None:
            self.accepted_offset_amount = m.get('AcceptedOffsetAmount')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')
        if m.get('BusinessId') is not None:
            self.business_id = m.get('BusinessId')
        if m.get('BusinessTime') is not None:
            self.business_time = m.get('BusinessTime')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('CommodityName') is not None:
            self.commodity_name = m.get('CommodityName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InvoiceIssuer') is not None:
            self.invoice_issuer = m.get('InvoiceIssuer')
        if m.get('InvoiceableAmount') is not None:
            self.invoiceable_amount = m.get('InvoiceableAmount')
        if m.get('InvoicedAmount') is not None:
            self.invoiced_amount = m.get('InvoicedAmount')
        if m.get('OffsetAmount') is not None:
            self.offset_amount = m.get('OffsetAmount')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ResourceOwnerAccountId') is not None:
            self.resource_owner_account_id = m.get('ResourceOwnerAccountId')
        if m.get('ResourceOwnerAccountName') is not None:
            self.resource_owner_account_name = m.get('ResourceOwnerAccountName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalAmount') is not None:
            self.total_amount = m.get('TotalAmount')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListInvoiceCandidateResponseBody(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        data: List[ListInvoiceCandidateResponseBodyData] = None,
        metadata: Any = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.data = data
        self.metadata = metadata
        self.page_size = page_size
        self.request_id = request_id
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
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.metadata is not None:
            result['Metadata'] = self.metadata
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
            for k in m.get('Data'):
                temp_model = ListInvoiceCandidateResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListInvoiceCandidateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInvoiceCandidateResponseBody = None,
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
            temp_model = ListInvoiceCandidateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInvoiceTitleResponseBodyData(TeaModel):
    def __init__(
        self,
        account_bank_name: str = None,
        account_id: int = None,
        bank_account_number: str = None,
        create_time: str = None,
        id: str = None,
        invoice_title: str = None,
        registered_address: str = None,
        registered_landline: str = None,
        unified_social_credit_code: str = None,
    ):
        self.account_bank_name = account_bank_name
        self.account_id = account_id
        self.bank_account_number = bank_account_number
        self.create_time = create_time
        self.id = id
        self.invoice_title = invoice_title
        self.registered_address = registered_address
        self.registered_landline = registered_landline
        self.unified_social_credit_code = unified_social_credit_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_bank_name is not None:
            result['AccountBankName'] = self.account_bank_name
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.bank_account_number is not None:
            result['BankAccountNumber'] = self.bank_account_number
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.id is not None:
            result['Id'] = self.id
        if self.invoice_title is not None:
            result['InvoiceTitle'] = self.invoice_title
        if self.registered_address is not None:
            result['RegisteredAddress'] = self.registered_address
        if self.registered_landline is not None:
            result['RegisteredLandline'] = self.registered_landline
        if self.unified_social_credit_code is not None:
            result['UnifiedSocialCreditCode'] = self.unified_social_credit_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountBankName') is not None:
            self.account_bank_name = m.get('AccountBankName')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('BankAccountNumber') is not None:
            self.bank_account_number = m.get('BankAccountNumber')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InvoiceTitle') is not None:
            self.invoice_title = m.get('InvoiceTitle')
        if m.get('RegisteredAddress') is not None:
            self.registered_address = m.get('RegisteredAddress')
        if m.get('RegisteredLandline') is not None:
            self.registered_landline = m.get('RegisteredLandline')
        if m.get('UnifiedSocialCreditCode') is not None:
            self.unified_social_credit_code = m.get('UnifiedSocialCreditCode')
        return self


class ListInvoiceTitleResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListInvoiceTitleResponseBodyData] = None,
        metadata: Any = None,
        request_id: str = None,
    ):
        self.data = data
        self.metadata = metadata
        self.request_id = request_id

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
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListInvoiceTitleResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListInvoiceTitleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInvoiceTitleResponseBody = None,
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
            temp_model = ListInvoiceTitleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListReportDefinitionsRequest(TeaModel):
    def __init__(
        self,
        nbid: str = None,
    ):
        self.nbid = nbid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        return self


class ListReportDefinitionsResponseBodyReportDefinitions(TeaModel):
    def __init__(
        self,
        begin_billing_cycle: str = None,
        oss_bucket_name: str = None,
        oss_bucket_owner_account_id: int = None,
        oss_bucket_path: str = None,
        report_source_name: str = None,
        report_source_type: str = None,
        report_task_id: int = None,
        report_type: str = None,
        subscribe_create_time: str = None,
    ):
        self.begin_billing_cycle = begin_billing_cycle
        self.oss_bucket_name = oss_bucket_name
        self.oss_bucket_owner_account_id = oss_bucket_owner_account_id
        self.oss_bucket_path = oss_bucket_path
        self.report_source_name = report_source_name
        self.report_source_type = report_source_type
        self.report_task_id = report_task_id
        self.report_type = report_type
        self.subscribe_create_time = subscribe_create_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_billing_cycle is not None:
            result['BeginBillingCycle'] = self.begin_billing_cycle
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.oss_bucket_owner_account_id is not None:
            result['OssBucketOwnerAccountId'] = self.oss_bucket_owner_account_id
        if self.oss_bucket_path is not None:
            result['OssBucketPath'] = self.oss_bucket_path
        if self.report_source_name is not None:
            result['ReportSourceName'] = self.report_source_name
        if self.report_source_type is not None:
            result['ReportSourceType'] = self.report_source_type
        if self.report_task_id is not None:
            result['ReportTaskId'] = self.report_task_id
        if self.report_type is not None:
            result['ReportType'] = self.report_type
        if self.subscribe_create_time is not None:
            result['SubscribeCreateTime'] = self.subscribe_create_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginBillingCycle') is not None:
            self.begin_billing_cycle = m.get('BeginBillingCycle')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('OssBucketOwnerAccountId') is not None:
            self.oss_bucket_owner_account_id = m.get('OssBucketOwnerAccountId')
        if m.get('OssBucketPath') is not None:
            self.oss_bucket_path = m.get('OssBucketPath')
        if m.get('ReportSourceName') is not None:
            self.report_source_name = m.get('ReportSourceName')
        if m.get('ReportSourceType') is not None:
            self.report_source_type = m.get('ReportSourceType')
        if m.get('ReportTaskId') is not None:
            self.report_task_id = m.get('ReportTaskId')
        if m.get('ReportType') is not None:
            self.report_type = m.get('ReportType')
        if m.get('SubscribeCreateTime') is not None:
            self.subscribe_create_time = m.get('SubscribeCreateTime')
        return self


class ListReportDefinitionsResponseBody(TeaModel):
    def __init__(
        self,
        metadata: Any = None,
        report_definitions: List[ListReportDefinitionsResponseBodyReportDefinitions] = None,
        request_id: str = None,
    ):
        self.metadata = metadata
        self.report_definitions = report_definitions
        self.request_id = request_id

    def validate(self):
        if self.report_definitions:
            for k in self.report_definitions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        result['ReportDefinitions'] = []
        if self.report_definitions is not None:
            for k in self.report_definitions:
                result['ReportDefinitions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        self.report_definitions = []
        if m.get('ReportDefinitions') is not None:
            for k in m.get('ReportDefinitions'):
                temp_model = ListReportDefinitionsResponseBodyReportDefinitions()
                self.report_definitions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListReportDefinitionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListReportDefinitionsResponseBody = None,
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
            temp_model = ListReportDefinitionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyCostCenterRequestCostCenterEntityList(TeaModel):
    def __init__(
        self,
        cost_center_id: int = None,
        cost_center_name: str = None,
        owner_account_id: int = None,
    ):
        # This parameter is required.
        self.cost_center_id = cost_center_id
        # This parameter is required.
        self.cost_center_name = cost_center_name
        # This parameter is required.
        self.owner_account_id = owner_account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_center_id is not None:
            result['CostCenterId'] = self.cost_center_id
        if self.cost_center_name is not None:
            result['CostCenterName'] = self.cost_center_name
        if self.owner_account_id is not None:
            result['OwnerAccountId'] = self.owner_account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostCenterId') is not None:
            self.cost_center_id = m.get('CostCenterId')
        if m.get('CostCenterName') is not None:
            self.cost_center_name = m.get('CostCenterName')
        if m.get('OwnerAccountId') is not None:
            self.owner_account_id = m.get('OwnerAccountId')
        return self


class ModifyCostCenterRequest(TeaModel):
    def __init__(
        self,
        cost_center_entity_list: List[ModifyCostCenterRequestCostCenterEntityList] = None,
        nbid: str = None,
    ):
        # This parameter is required.
        self.cost_center_entity_list = cost_center_entity_list
        self.nbid = nbid

    def validate(self):
        if self.cost_center_entity_list:
            for k in self.cost_center_entity_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CostCenterEntityList'] = []
        if self.cost_center_entity_list is not None:
            for k in self.cost_center_entity_list:
                result['CostCenterEntityList'].append(k.to_map() if k else None)
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cost_center_entity_list = []
        if m.get('CostCenterEntityList') is not None:
            for k in m.get('CostCenterEntityList'):
                temp_model = ModifyCostCenterRequestCostCenterEntityList()
                self.cost_center_entity_list.append(temp_model.from_map(k))
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        return self


class ModifyCostCenterShrinkRequest(TeaModel):
    def __init__(
        self,
        cost_center_entity_list_shrink: str = None,
        nbid: str = None,
    ):
        # This parameter is required.
        self.cost_center_entity_list_shrink = cost_center_entity_list_shrink
        self.nbid = nbid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_center_entity_list_shrink is not None:
            result['CostCenterEntityList'] = self.cost_center_entity_list_shrink
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostCenterEntityList') is not None:
            self.cost_center_entity_list_shrink = m.get('CostCenterEntityList')
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        return self


class ModifyCostCenterResponseBodyCostCenterOperateDto(TeaModel):
    def __init__(
        self,
        cost_center_id: int = None,
        is_success: bool = None,
        owner_account_id: int = None,
    ):
        self.cost_center_id = cost_center_id
        self.is_success = is_success
        self.owner_account_id = owner_account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_center_id is not None:
            result['CostCenterId'] = self.cost_center_id
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.owner_account_id is not None:
            result['OwnerAccountId'] = self.owner_account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostCenterId') is not None:
            self.cost_center_id = m.get('CostCenterId')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('OwnerAccountId') is not None:
            self.owner_account_id = m.get('OwnerAccountId')
        return self


class ModifyCostCenterResponseBody(TeaModel):
    def __init__(
        self,
        cost_center_operate_dto: List[ModifyCostCenterResponseBodyCostCenterOperateDto] = None,
        metadata: Any = None,
        request_id: str = None,
    ):
        self.cost_center_operate_dto = cost_center_operate_dto
        self.metadata = metadata
        self.request_id = request_id

    def validate(self):
        if self.cost_center_operate_dto:
            for k in self.cost_center_operate_dto:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CostCenterOperateDto'] = []
        if self.cost_center_operate_dto is not None:
            for k in self.cost_center_operate_dto:
                result['CostCenterOperateDto'].append(k.to_map() if k else None)
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cost_center_operate_dto = []
        if m.get('CostCenterOperateDto') is not None:
            for k in m.get('CostCenterOperateDto'):
                temp_model = ModifyCostCenterResponseBodyCostCenterOperateDto()
                self.cost_center_operate_dto.append(temp_model.from_map(k))
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyCostCenterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyCostCenterResponseBody = None,
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
            temp_model = ModifyCostCenterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyCostCenterRuleRequestFilterExpressionFilterValues(TeaModel):
    def __init__(
        self,
        code: str = None,
        code_name: str = None,
        select_type: str = None,
        values: List[str] = None,
    ):
        self.code = code
        self.code_name = code_name
        self.select_type = select_type
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.code_name is not None:
            result['CodeName'] = self.code_name
        if self.select_type is not None:
            result['SelectType'] = self.select_type
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CodeName') is not None:
            self.code_name = m.get('CodeName')
        if m.get('SelectType') is not None:
            self.select_type = m.get('SelectType')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class ModifyCostCenterRuleRequestFilterExpression(TeaModel):
    def __init__(
        self,
        expression_type: str = None,
        filter_values: ModifyCostCenterRuleRequestFilterExpressionFilterValues = None,
        operand: Any = None,
        operands: List[Any] = None,
        operator_type: str = None,
    ):
        self.expression_type = expression_type
        self.filter_values = filter_values
        self.operand = operand
        self.operands = operands
        self.operator_type = operator_type

    def validate(self):
        if self.filter_values:
            self.filter_values.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expression_type is not None:
            result['ExpressionType'] = self.expression_type
        if self.filter_values is not None:
            result['FilterValues'] = self.filter_values.to_map()
        if self.operand is not None:
            result['Operand'] = self.operand
        if self.operands is not None:
            result['Operands'] = self.operands
        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpressionType') is not None:
            self.expression_type = m.get('ExpressionType')
        if m.get('FilterValues') is not None:
            temp_model = ModifyCostCenterRuleRequestFilterExpressionFilterValues()
            self.filter_values = temp_model.from_map(m['FilterValues'])
        if m.get('Operand') is not None:
            self.operand = m.get('Operand')
        if m.get('Operands') is not None:
            self.operands = m.get('Operands')
        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')
        return self


class ModifyCostCenterRuleRequest(TeaModel):
    def __init__(
        self,
        cost_center_id: int = None,
        filter_expression: ModifyCostCenterRuleRequestFilterExpression = None,
        nbid: str = None,
        owner_account_id: int = None,
    ):
        self.cost_center_id = cost_center_id
        self.filter_expression = filter_expression
        self.nbid = nbid
        self.owner_account_id = owner_account_id

    def validate(self):
        if self.filter_expression:
            self.filter_expression.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_center_id is not None:
            result['CostCenterId'] = self.cost_center_id
        if self.filter_expression is not None:
            result['FilterExpression'] = self.filter_expression.to_map()
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        if self.owner_account_id is not None:
            result['OwnerAccountId'] = self.owner_account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostCenterId') is not None:
            self.cost_center_id = m.get('CostCenterId')
        if m.get('FilterExpression') is not None:
            temp_model = ModifyCostCenterRuleRequestFilterExpression()
            self.filter_expression = temp_model.from_map(m['FilterExpression'])
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        if m.get('OwnerAccountId') is not None:
            self.owner_account_id = m.get('OwnerAccountId')
        return self


class ModifyCostCenterRuleShrinkRequest(TeaModel):
    def __init__(
        self,
        cost_center_id: int = None,
        filter_expression_shrink: str = None,
        nbid: str = None,
        owner_account_id: int = None,
    ):
        self.cost_center_id = cost_center_id
        self.filter_expression_shrink = filter_expression_shrink
        self.nbid = nbid
        self.owner_account_id = owner_account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_center_id is not None:
            result['CostCenterId'] = self.cost_center_id
        if self.filter_expression_shrink is not None:
            result['FilterExpression'] = self.filter_expression_shrink
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        if self.owner_account_id is not None:
            result['OwnerAccountId'] = self.owner_account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostCenterId') is not None:
            self.cost_center_id = m.get('CostCenterId')
        if m.get('FilterExpression') is not None:
            self.filter_expression_shrink = m.get('FilterExpression')
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        if m.get('OwnerAccountId') is not None:
            self.owner_account_id = m.get('OwnerAccountId')
        return self


class ModifyCostCenterRuleResponseBody(TeaModel):
    def __init__(
        self,
        data: int = None,
        metadata: Any = None,
        request_id: str = None,
    ):
        self.data = data
        self.metadata = metadata
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyCostCenterRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyCostCenterRuleResponseBody = None,
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
            temp_model = ModifyCostCenterRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCostCenterRequestEcIdAccountIds(TeaModel):
    def __init__(
        self,
        account_ids: List[int] = None,
        ec_id: str = None,
    ):
        self.account_ids = account_ids
        # This parameter is required.
        self.ec_id = ec_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids
        if self.ec_id is not None:
            result['EcId'] = self.ec_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')
        if m.get('EcId') is not None:
            self.ec_id = m.get('EcId')
        return self


class QueryCostCenterRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        ec_id_account_ids: List[QueryCostCenterRequestEcIdAccountIds] = None,
        nbid: str = None,
        owner_account_id: int = None,
        page_size: int = None,
        parent_cost_center_id: int = None,
    ):
        # This parameter is required.
        self.current_page = current_page
        self.ec_id_account_ids = ec_id_account_ids
        self.nbid = nbid
        # This parameter is required.
        self.owner_account_id = owner_account_id
        # This parameter is required.
        self.page_size = page_size
        # This parameter is required.
        self.parent_cost_center_id = parent_cost_center_id

    def validate(self):
        if self.ec_id_account_ids:
            for k in self.ec_id_account_ids:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['EcIdAccountIds'] = []
        if self.ec_id_account_ids is not None:
            for k in self.ec_id_account_ids:
                result['EcIdAccountIds'].append(k.to_map() if k else None)
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        if self.owner_account_id is not None:
            result['OwnerAccountId'] = self.owner_account_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.parent_cost_center_id is not None:
            result['ParentCostCenterId'] = self.parent_cost_center_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.ec_id_account_ids = []
        if m.get('EcIdAccountIds') is not None:
            for k in m.get('EcIdAccountIds'):
                temp_model = QueryCostCenterRequestEcIdAccountIds()
                self.ec_id_account_ids.append(temp_model.from_map(k))
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        if m.get('OwnerAccountId') is not None:
            self.owner_account_id = m.get('OwnerAccountId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ParentCostCenterId') is not None:
            self.parent_cost_center_id = m.get('ParentCostCenterId')
        return self


class QueryCostCenterShrinkRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        ec_id_account_ids_shrink: str = None,
        nbid: str = None,
        owner_account_id: int = None,
        page_size: int = None,
        parent_cost_center_id: int = None,
    ):
        # This parameter is required.
        self.current_page = current_page
        self.ec_id_account_ids_shrink = ec_id_account_ids_shrink
        self.nbid = nbid
        # This parameter is required.
        self.owner_account_id = owner_account_id
        # This parameter is required.
        self.page_size = page_size
        # This parameter is required.
        self.parent_cost_center_id = parent_cost_center_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.ec_id_account_ids_shrink is not None:
            result['EcIdAccountIds'] = self.ec_id_account_ids_shrink
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        if self.owner_account_id is not None:
            result['OwnerAccountId'] = self.owner_account_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.parent_cost_center_id is not None:
            result['ParentCostCenterId'] = self.parent_cost_center_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EcIdAccountIds') is not None:
            self.ec_id_account_ids_shrink = m.get('EcIdAccountIds')
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        if m.get('OwnerAccountId') is not None:
            self.owner_account_id = m.get('OwnerAccountId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ParentCostCenterId') is not None:
            self.parent_cost_center_id = m.get('ParentCostCenterId')
        return self


class QueryCostCenterResponseBodyCostCenterDtoList(TeaModel):
    def __init__(
        self,
        cost_center_code: str = None,
        cost_center_id: int = None,
        cost_center_name: str = None,
        level: int = None,
        owner_account_id: int = None,
        parent_cost_center_id: int = None,
        prev_cost_center_id: int = None,
    ):
        self.cost_center_code = cost_center_code
        self.cost_center_id = cost_center_id
        self.cost_center_name = cost_center_name
        self.level = level
        self.owner_account_id = owner_account_id
        self.parent_cost_center_id = parent_cost_center_id
        self.prev_cost_center_id = prev_cost_center_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_center_code is not None:
            result['CostCenterCode'] = self.cost_center_code
        if self.cost_center_id is not None:
            result['CostCenterId'] = self.cost_center_id
        if self.cost_center_name is not None:
            result['CostCenterName'] = self.cost_center_name
        if self.level is not None:
            result['Level'] = self.level
        if self.owner_account_id is not None:
            result['OwnerAccountId'] = self.owner_account_id
        if self.parent_cost_center_id is not None:
            result['ParentCostCenterId'] = self.parent_cost_center_id
        if self.prev_cost_center_id is not None:
            result['PrevCostCenterId'] = self.prev_cost_center_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostCenterCode') is not None:
            self.cost_center_code = m.get('CostCenterCode')
        if m.get('CostCenterId') is not None:
            self.cost_center_id = m.get('CostCenterId')
        if m.get('CostCenterName') is not None:
            self.cost_center_name = m.get('CostCenterName')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('OwnerAccountId') is not None:
            self.owner_account_id = m.get('OwnerAccountId')
        if m.get('ParentCostCenterId') is not None:
            self.parent_cost_center_id = m.get('ParentCostCenterId')
        if m.get('PrevCostCenterId') is not None:
            self.prev_cost_center_id = m.get('PrevCostCenterId')
        return self


class QueryCostCenterResponseBody(TeaModel):
    def __init__(
        self,
        cost_center_dto_list: List[QueryCostCenterResponseBodyCostCenterDtoList] = None,
        current_page: int = None,
        metadata: Any = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.cost_center_dto_list = cost_center_dto_list
        self.current_page = current_page
        self.metadata = metadata
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.cost_center_dto_list:
            for k in self.cost_center_dto_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CostCenterDtoList'] = []
        if self.cost_center_dto_list is not None:
            for k in self.cost_center_dto_list:
                result['CostCenterDtoList'].append(k.to_map() if k else None)
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cost_center_dto_list = []
        if m.get('CostCenterDtoList') is not None:
            for k in m.get('CostCenterDtoList'):
                temp_model = QueryCostCenterResponseBodyCostCenterDtoList()
                self.cost_center_dto_list.append(temp_model.from_map(k))
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryCostCenterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryCostCenterResponseBody = None,
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
            temp_model = QueryCostCenterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCostCenterResourceRequestEcIdAccountIds(TeaModel):
    def __init__(
        self,
        account_ids: List[int] = None,
        ec_id: str = None,
    ):
        self.account_ids = account_ids
        # This parameter is required.
        self.ec_id = ec_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids
        if self.ec_id is not None:
            result['EcId'] = self.ec_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')
        if m.get('EcId') is not None:
            self.ec_id = m.get('EcId')
        return self


class QueryCostCenterResourceRequest(TeaModel):
    def __init__(
        self,
        cost_center_id: int = None,
        ec_id_account_ids: List[QueryCostCenterResourceRequestEcIdAccountIds] = None,
        max_results: int = None,
        nbid: str = None,
        next_token: str = None,
        owner_account_id: int = None,
    ):
        self.cost_center_id = cost_center_id
        self.ec_id_account_ids = ec_id_account_ids
        self.max_results = max_results
        self.nbid = nbid
        self.next_token = next_token
        self.owner_account_id = owner_account_id

    def validate(self):
        if self.ec_id_account_ids:
            for k in self.ec_id_account_ids:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_center_id is not None:
            result['CostCenterId'] = self.cost_center_id
        result['EcIdAccountIds'] = []
        if self.ec_id_account_ids is not None:
            for k in self.ec_id_account_ids:
                result['EcIdAccountIds'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account_id is not None:
            result['OwnerAccountId'] = self.owner_account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostCenterId') is not None:
            self.cost_center_id = m.get('CostCenterId')
        self.ec_id_account_ids = []
        if m.get('EcIdAccountIds') is not None:
            for k in m.get('EcIdAccountIds'):
                temp_model = QueryCostCenterResourceRequestEcIdAccountIds()
                self.ec_id_account_ids.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccountId') is not None:
            self.owner_account_id = m.get('OwnerAccountId')
        return self


class QueryCostCenterResourceResponseBodyCostCenterResourceDtoList(TeaModel):
    def __init__(
        self,
        apportion_item_code: str = None,
        apportion_item_name: str = None,
        commodity_code: str = None,
        commodity_name: str = None,
        cost_center_code: str = None,
        cost_center_create_time: str = None,
        cost_center_id: int = None,
        cost_center_name: str = None,
        cost_center_update_time: str = None,
        instance_id: str = None,
        owner_account_id: int = None,
        owner_account_name: str = None,
        parent_cost_center_id: int = None,
        pip_code: str = None,
        pip_name: str = None,
        resource_group: str = None,
        resource_id: str = None,
        resource_nick: str = None,
        resource_source: str = None,
        resource_tag: str = None,
        resource_type: str = None,
        resource_update_time: str = None,
        resource_user_id: int = None,
        resource_user_name: str = None,
        root_cost_center_id: int = None,
    ):
        self.apportion_item_code = apportion_item_code
        self.apportion_item_name = apportion_item_name
        self.commodity_code = commodity_code
        self.commodity_name = commodity_name
        self.cost_center_code = cost_center_code
        self.cost_center_create_time = cost_center_create_time
        self.cost_center_id = cost_center_id
        self.cost_center_name = cost_center_name
        self.cost_center_update_time = cost_center_update_time
        self.instance_id = instance_id
        self.owner_account_id = owner_account_id
        self.owner_account_name = owner_account_name
        self.parent_cost_center_id = parent_cost_center_id
        self.pip_code = pip_code
        self.pip_name = pip_name
        self.resource_group = resource_group
        self.resource_id = resource_id
        self.resource_nick = resource_nick
        self.resource_source = resource_source
        self.resource_tag = resource_tag
        self.resource_type = resource_type
        self.resource_update_time = resource_update_time
        self.resource_user_id = resource_user_id
        self.resource_user_name = resource_user_name
        self.root_cost_center_id = root_cost_center_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apportion_item_code is not None:
            result['ApportionItemCode'] = self.apportion_item_code
        if self.apportion_item_name is not None:
            result['ApportionItemName'] = self.apportion_item_name
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.commodity_name is not None:
            result['CommodityName'] = self.commodity_name
        if self.cost_center_code is not None:
            result['CostCenterCode'] = self.cost_center_code
        if self.cost_center_create_time is not None:
            result['CostCenterCreateTime'] = self.cost_center_create_time
        if self.cost_center_id is not None:
            result['CostCenterId'] = self.cost_center_id
        if self.cost_center_name is not None:
            result['CostCenterName'] = self.cost_center_name
        if self.cost_center_update_time is not None:
            result['CostCenterUpdateTime'] = self.cost_center_update_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account_id is not None:
            result['OwnerAccountId'] = self.owner_account_id
        if self.owner_account_name is not None:
            result['OwnerAccountName'] = self.owner_account_name
        if self.parent_cost_center_id is not None:
            result['ParentCostCenterId'] = self.parent_cost_center_id
        if self.pip_code is not None:
            result['PipCode'] = self.pip_code
        if self.pip_name is not None:
            result['PipName'] = self.pip_name
        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_nick is not None:
            result['ResourceNick'] = self.resource_nick
        if self.resource_source is not None:
            result['ResourceSource'] = self.resource_source
        if self.resource_tag is not None:
            result['ResourceTag'] = self.resource_tag
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_update_time is not None:
            result['ResourceUpdateTime'] = self.resource_update_time
        if self.resource_user_id is not None:
            result['ResourceUserId'] = self.resource_user_id
        if self.resource_user_name is not None:
            result['ResourceUserName'] = self.resource_user_name
        if self.root_cost_center_id is not None:
            result['RootCostCenterId'] = self.root_cost_center_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApportionItemCode') is not None:
            self.apportion_item_code = m.get('ApportionItemCode')
        if m.get('ApportionItemName') is not None:
            self.apportion_item_name = m.get('ApportionItemName')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('CommodityName') is not None:
            self.commodity_name = m.get('CommodityName')
        if m.get('CostCenterCode') is not None:
            self.cost_center_code = m.get('CostCenterCode')
        if m.get('CostCenterCreateTime') is not None:
            self.cost_center_create_time = m.get('CostCenterCreateTime')
        if m.get('CostCenterId') is not None:
            self.cost_center_id = m.get('CostCenterId')
        if m.get('CostCenterName') is not None:
            self.cost_center_name = m.get('CostCenterName')
        if m.get('CostCenterUpdateTime') is not None:
            self.cost_center_update_time = m.get('CostCenterUpdateTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccountId') is not None:
            self.owner_account_id = m.get('OwnerAccountId')
        if m.get('OwnerAccountName') is not None:
            self.owner_account_name = m.get('OwnerAccountName')
        if m.get('ParentCostCenterId') is not None:
            self.parent_cost_center_id = m.get('ParentCostCenterId')
        if m.get('PipCode') is not None:
            self.pip_code = m.get('PipCode')
        if m.get('PipName') is not None:
            self.pip_name = m.get('PipName')
        if m.get('ResourceGroup') is not None:
            self.resource_group = m.get('ResourceGroup')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceNick') is not None:
            self.resource_nick = m.get('ResourceNick')
        if m.get('ResourceSource') is not None:
            self.resource_source = m.get('ResourceSource')
        if m.get('ResourceTag') is not None:
            self.resource_tag = m.get('ResourceTag')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceUpdateTime') is not None:
            self.resource_update_time = m.get('ResourceUpdateTime')
        if m.get('ResourceUserId') is not None:
            self.resource_user_id = m.get('ResourceUserId')
        if m.get('ResourceUserName') is not None:
            self.resource_user_name = m.get('ResourceUserName')
        if m.get('RootCostCenterId') is not None:
            self.root_cost_center_id = m.get('RootCostCenterId')
        return self


class QueryCostCenterResourceResponseBody(TeaModel):
    def __init__(
        self,
        cost_center_resource_dto_list: List[QueryCostCenterResourceResponseBodyCostCenterResourceDtoList] = None,
        max_results: int = None,
        metadata: Any = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.cost_center_resource_dto_list = cost_center_resource_dto_list
        self.max_results = max_results
        self.metadata = metadata
        # This parameter is required.
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.cost_center_resource_dto_list:
            for k in self.cost_center_resource_dto_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CostCenterResourceDtoList'] = []
        if self.cost_center_resource_dto_list is not None:
            for k in self.cost_center_resource_dto_list:
                result['CostCenterResourceDtoList'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cost_center_resource_dto_list = []
        if m.get('CostCenterResourceDtoList') is not None:
            for k in m.get('CostCenterResourceDtoList'):
                temp_model = QueryCostCenterResourceResponseBodyCostCenterResourceDtoList()
                self.cost_center_resource_dto_list.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryCostCenterResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryCostCenterResourceResponseBody = None,
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
            temp_model = QueryCostCenterResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCostCenterRuleRequestEcIdAccountIds(TeaModel):
    def __init__(
        self,
        account_ids: List[int] = None,
        ec_id: str = None,
    ):
        self.account_ids = account_ids
        # This parameter is required.
        self.ec_id = ec_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids
        if self.ec_id is not None:
            result['EcId'] = self.ec_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')
        if m.get('EcId') is not None:
            self.ec_id = m.get('EcId')
        return self


class QueryCostCenterRuleRequest(TeaModel):
    def __init__(
        self,
        cost_center_id: int = None,
        ec_id_account_ids: List[QueryCostCenterRuleRequestEcIdAccountIds] = None,
        nbid: str = None,
    ):
        self.cost_center_id = cost_center_id
        self.ec_id_account_ids = ec_id_account_ids
        self.nbid = nbid

    def validate(self):
        if self.ec_id_account_ids:
            for k in self.ec_id_account_ids:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_center_id is not None:
            result['CostCenterId'] = self.cost_center_id
        result['EcIdAccountIds'] = []
        if self.ec_id_account_ids is not None:
            for k in self.ec_id_account_ids:
                result['EcIdAccountIds'].append(k.to_map() if k else None)
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostCenterId') is not None:
            self.cost_center_id = m.get('CostCenterId')
        self.ec_id_account_ids = []
        if m.get('EcIdAccountIds') is not None:
            for k in m.get('EcIdAccountIds'):
                temp_model = QueryCostCenterRuleRequestEcIdAccountIds()
                self.ec_id_account_ids.append(temp_model.from_map(k))
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        return self


class QueryCostCenterRuleResponseBodyFilterExpressionFilterValues(TeaModel):
    def __init__(
        self,
        code: str = None,
        code_name: str = None,
        select_type: str = None,
        values: List[str] = None,
    ):
        self.code = code
        self.code_name = code_name
        self.select_type = select_type
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.code_name is not None:
            result['CodeName'] = self.code_name
        if self.select_type is not None:
            result['SelectType'] = self.select_type
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CodeName') is not None:
            self.code_name = m.get('CodeName')
        if m.get('SelectType') is not None:
            self.select_type = m.get('SelectType')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class QueryCostCenterRuleResponseBodyFilterExpression(TeaModel):
    def __init__(
        self,
        expression_type: str = None,
        filter_values: QueryCostCenterRuleResponseBodyFilterExpressionFilterValues = None,
        operand: Any = None,
        operands: List[Any] = None,
        operator_type: str = None,
    ):
        self.expression_type = expression_type
        self.filter_values = filter_values
        self.operand = operand
        self.operands = operands
        self.operator_type = operator_type

    def validate(self):
        if self.filter_values:
            self.filter_values.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expression_type is not None:
            result['ExpressionType'] = self.expression_type
        if self.filter_values is not None:
            result['FilterValues'] = self.filter_values.to_map()
        if self.operand is not None:
            result['Operand'] = self.operand
        if self.operands is not None:
            result['Operands'] = self.operands
        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpressionType') is not None:
            self.expression_type = m.get('ExpressionType')
        if m.get('FilterValues') is not None:
            temp_model = QueryCostCenterRuleResponseBodyFilterExpressionFilterValues()
            self.filter_values = temp_model.from_map(m['FilterValues'])
        if m.get('Operand') is not None:
            self.operand = m.get('Operand')
        if m.get('Operands') is not None:
            self.operands = m.get('Operands')
        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')
        return self


class QueryCostCenterRuleResponseBody(TeaModel):
    def __init__(
        self,
        cost_center_id: int = None,
        filter_expression: QueryCostCenterRuleResponseBodyFilterExpression = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        is_deleted: int = None,
        metadata: Any = None,
        owner_account_id: int = None,
        request_id: str = None,
        root_cost_center_id: int = None,
        status: str = None,
    ):
        self.cost_center_id = cost_center_id
        self.filter_expression = filter_expression
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.is_deleted = is_deleted
        self.metadata = metadata
        self.owner_account_id = owner_account_id
        # Id of the request
        self.request_id = request_id
        self.root_cost_center_id = root_cost_center_id
        self.status = status

    def validate(self):
        if self.filter_expression:
            self.filter_expression.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_center_id is not None:
            result['CostCenterId'] = self.cost_center_id
        if self.filter_expression is not None:
            result['FilterExpression'] = self.filter_expression.to_map()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.is_deleted is not None:
            result['IsDeleted'] = self.is_deleted
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.owner_account_id is not None:
            result['OwnerAccountId'] = self.owner_account_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.root_cost_center_id is not None:
            result['RootCostCenterId'] = self.root_cost_center_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostCenterId') is not None:
            self.cost_center_id = m.get('CostCenterId')
        if m.get('FilterExpression') is not None:
            temp_model = QueryCostCenterRuleResponseBodyFilterExpression()
            self.filter_expression = temp_model.from_map(m['FilterExpression'])
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsDeleted') is not None:
            self.is_deleted = m.get('IsDeleted')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('OwnerAccountId') is not None:
            self.owner_account_id = m.get('OwnerAccountId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RootCostCenterId') is not None:
            self.root_cost_center_id = m.get('RootCostCenterId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryCostCenterRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryCostCenterRuleResponseBody = None,
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
            temp_model = QueryCostCenterRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetFundAccountCreditAmountRequest(TeaModel):
    def __init__(
        self,
        credit_amount: str = None,
        currency: str = None,
        fund_account_id: int = None,
    ):
        # This parameter is required.
        self.credit_amount = credit_amount
        # This parameter is required.
        self.currency = currency
        self.fund_account_id = fund_account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credit_amount is not None:
            result['CreditAmount'] = self.credit_amount
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.fund_account_id is not None:
            result['FundAccountId'] = self.fund_account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreditAmount') is not None:
            self.credit_amount = m.get('CreditAmount')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('FundAccountId') is not None:
            self.fund_account_id = m.get('FundAccountId')
        return self


class SetFundAccountCreditAmountResponseBody(TeaModel):
    def __init__(
        self,
        metadata: Any = None,
        request_id: str = None,
    ):
        self.metadata = metadata
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetFundAccountCreditAmountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetFundAccountCreditAmountResponseBody = None,
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
            temp_model = SetFundAccountCreditAmountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetFundAccountLowAvailableAmountAlarmRequest(TeaModel):
    def __init__(
        self,
        fund_account_id: int = None,
        threshold_amount: str = None,
    ):
        self.fund_account_id = fund_account_id
        self.threshold_amount = threshold_amount

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fund_account_id is not None:
            result['FundAccountId'] = self.fund_account_id
        if self.threshold_amount is not None:
            result['ThresholdAmount'] = self.threshold_amount
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FundAccountId') is not None:
            self.fund_account_id = m.get('FundAccountId')
        if m.get('ThresholdAmount') is not None:
            self.threshold_amount = m.get('ThresholdAmount')
        return self


class SetFundAccountLowAvailableAmountAlarmResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        metadata: Any = None,
        request_id: str = None,
    ):
        self.data = data
        self.metadata = metadata
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetFundAccountLowAvailableAmountAlarmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetFundAccountLowAvailableAmountAlarmResponseBody = None,
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
            temp_model = SetFundAccountLowAvailableAmountAlarmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetSavingPlanUserDeductRuleRequestEcIdAccountIds(TeaModel):
    def __init__(
        self,
        account_ids: List[int] = None,
        ec_id: str = None,
    ):
        self.account_ids = account_ids
        self.ec_id = ec_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids
        if self.ec_id is not None:
            result['EcId'] = self.ec_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')
        if m.get('EcId') is not None:
            self.ec_id = m.get('EcId')
        return self


class SetSavingPlanUserDeductRuleRequestUserDeductRules(TeaModel):
    def __init__(
        self,
        commodity_code: str = None,
        module_code: str = None,
        skip_deduct: bool = None,
    ):
        self.commodity_code = commodity_code
        self.module_code = module_code
        self.skip_deduct = skip_deduct

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.module_code is not None:
            result['ModuleCode'] = self.module_code
        if self.skip_deduct is not None:
            result['SkipDeduct'] = self.skip_deduct
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('ModuleCode') is not None:
            self.module_code = m.get('ModuleCode')
        if m.get('SkipDeduct') is not None:
            self.skip_deduct = m.get('SkipDeduct')
        return self


class SetSavingPlanUserDeductRuleRequest(TeaModel):
    def __init__(
        self,
        ec_id_account_ids: List[SetSavingPlanUserDeductRuleRequestEcIdAccountIds] = None,
        nbid: str = None,
        spn_instance_code: str = None,
        user_deduct_rules: List[SetSavingPlanUserDeductRuleRequestUserDeductRules] = None,
    ):
        self.ec_id_account_ids = ec_id_account_ids
        self.nbid = nbid
        self.spn_instance_code = spn_instance_code
        self.user_deduct_rules = user_deduct_rules

    def validate(self):
        if self.ec_id_account_ids:
            for k in self.ec_id_account_ids:
                if k:
                    k.validate()
        if self.user_deduct_rules:
            for k in self.user_deduct_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EcIdAccountIds'] = []
        if self.ec_id_account_ids is not None:
            for k in self.ec_id_account_ids:
                result['EcIdAccountIds'].append(k.to_map() if k else None)
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        if self.spn_instance_code is not None:
            result['SpnInstanceCode'] = self.spn_instance_code
        result['UserDeductRules'] = []
        if self.user_deduct_rules is not None:
            for k in self.user_deduct_rules:
                result['UserDeductRules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ec_id_account_ids = []
        if m.get('EcIdAccountIds') is not None:
            for k in m.get('EcIdAccountIds'):
                temp_model = SetSavingPlanUserDeductRuleRequestEcIdAccountIds()
                self.ec_id_account_ids.append(temp_model.from_map(k))
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        if m.get('SpnInstanceCode') is not None:
            self.spn_instance_code = m.get('SpnInstanceCode')
        self.user_deduct_rules = []
        if m.get('UserDeductRules') is not None:
            for k in m.get('UserDeductRules'):
                temp_model = SetSavingPlanUserDeductRuleRequestUserDeductRules()
                self.user_deduct_rules.append(temp_model.from_map(k))
        return self


class SetSavingPlanUserDeductRuleShrinkRequest(TeaModel):
    def __init__(
        self,
        ec_id_account_ids_shrink: str = None,
        nbid: str = None,
        spn_instance_code: str = None,
        user_deduct_rules_shrink: str = None,
    ):
        self.ec_id_account_ids_shrink = ec_id_account_ids_shrink
        self.nbid = nbid
        self.spn_instance_code = spn_instance_code
        self.user_deduct_rules_shrink = user_deduct_rules_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ec_id_account_ids_shrink is not None:
            result['EcIdAccountIds'] = self.ec_id_account_ids_shrink
        if self.nbid is not None:
            result['Nbid'] = self.nbid
        if self.spn_instance_code is not None:
            result['SpnInstanceCode'] = self.spn_instance_code
        if self.user_deduct_rules_shrink is not None:
            result['UserDeductRules'] = self.user_deduct_rules_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EcIdAccountIds') is not None:
            self.ec_id_account_ids_shrink = m.get('EcIdAccountIds')
        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')
        if m.get('SpnInstanceCode') is not None:
            self.spn_instance_code = m.get('SpnInstanceCode')
        if m.get('UserDeductRules') is not None:
            self.user_deduct_rules_shrink = m.get('UserDeductRules')
        return self


class SetSavingPlanUserDeductRuleResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetSavingPlanUserDeductRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetSavingPlanUserDeductRuleResponseBody = None,
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
            temp_model = SetSavingPlanUserDeductRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


