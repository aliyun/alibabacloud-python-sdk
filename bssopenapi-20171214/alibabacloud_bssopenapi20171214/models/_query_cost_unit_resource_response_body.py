# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class QueryCostUnitResourceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryCostUnitResourceResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code.
        self.code = code
        # The data returned.
        self.data = data
        # The error message.
        self.message = message
        # The ID of the request.
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
            temp_model = main_models.QueryCostUnitResourceResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryCostUnitResourceResponseBodyData(DaraModel):
    def __init__(
        self,
        cost_unit: main_models.QueryCostUnitResourceResponseBodyDataCostUnit = None,
        cost_unit_statis_info: main_models.QueryCostUnitResourceResponseBodyDataCostUnitStatisInfo = None,
        page_num: int = None,
        page_size: int = None,
        resource_instance_dto_list: List[main_models.QueryCostUnitResourceResponseBodyDataResourceInstanceDtoList] = None,
        total_count: int = None,
    ):
        # The information about the cost center.
        self.cost_unit = cost_unit
        # The statistical information about the cost center.
        self.cost_unit_statis_info = cost_unit_statis_info
        # The page number of the returned page.
        self.page_num = page_num
        # The number of entries returned per page.
        self.page_size = page_size
        # The resource instances.
        self.resource_instance_dto_list = resource_instance_dto_list
        # The total number of returned entries.
        self.total_count = total_count

    def validate(self):
        if self.cost_unit:
            self.cost_unit.validate()
        if self.cost_unit_statis_info:
            self.cost_unit_statis_info.validate()
        if self.resource_instance_dto_list:
            for v1 in self.resource_instance_dto_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cost_unit is not None:
            result['CostUnit'] = self.cost_unit.to_map()

        if self.cost_unit_statis_info is not None:
            result['CostUnitStatisInfo'] = self.cost_unit_statis_info.to_map()

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['ResourceInstanceDtoList'] = []
        if self.resource_instance_dto_list is not None:
            for k1 in self.resource_instance_dto_list:
                result['ResourceInstanceDtoList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostUnit') is not None:
            temp_model = main_models.QueryCostUnitResourceResponseBodyDataCostUnit()
            self.cost_unit = temp_model.from_map(m.get('CostUnit'))

        if m.get('CostUnitStatisInfo') is not None:
            temp_model = main_models.QueryCostUnitResourceResponseBodyDataCostUnitStatisInfo()
            self.cost_unit_statis_info = temp_model.from_map(m.get('CostUnitStatisInfo'))

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.resource_instance_dto_list = []
        if m.get('ResourceInstanceDtoList') is not None:
            for k1 in m.get('ResourceInstanceDtoList'):
                temp_model = main_models.QueryCostUnitResourceResponseBodyDataResourceInstanceDtoList()
                self.resource_instance_dto_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class QueryCostUnitResourceResponseBodyDataResourceInstanceDtoList(DaraModel):
    def __init__(
        self,
        apportion_code: str = None,
        apportion_name: str = None,
        commodity_code: str = None,
        commodity_name: str = None,
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
        # The split code of the resource.
        self.apportion_code = apportion_code
        # The split name of the resource.
        self.apportion_name = apportion_name
        # The product code of the resource.
        self.commodity_code = commodity_code
        # The commodity name of the resource.
        self.commodity_name = commodity_name
        # The code of the service. The code is the same as that in Cost Center.
        self.pip_code = pip_code
        # The resources related to the resource instance.
        self.related_resources = related_resources
        # The resource group to which the resource belongs.
        self.resource_group = resource_group
        # The instance ID of the resource.
        self.resource_id = resource_id
        # The custom name of the resource.
        self.resource_nick = resource_nick
        # The source of the resource. Value:
        # - AUTO_ALLOCATE
        # - MANUAL_ALLOCATE
        self.resource_source = resource_source
        # The status of the resource.
        self.resource_status = resource_status
        # The tags of the resource.
        self.resource_tag = resource_tag
        # The type of the resource.
        self.resource_type = resource_type
        # The user ID of the resource owner.
        self.resource_user_id = resource_user_id
        # The username of the resource owner.
        self.resource_user_name = resource_user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apportion_code is not None:
            result['ApportionCode'] = self.apportion_code

        if self.apportion_name is not None:
            result['ApportionName'] = self.apportion_name

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.commodity_name is not None:
            result['CommodityName'] = self.commodity_name

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

class QueryCostUnitResourceResponseBodyDataCostUnitStatisInfo(DaraModel):
    def __init__(
        self,
        resource_count: int = None,
        resource_group_count: int = None,
        sub_unit_count: int = None,
        total_resource_count: int = None,
        total_resource_group_count: int = None,
        total_user_count: int = None,
        user_count: int = None,
    ):
        # The number of resource instances in the cost center.
        self.resource_count = resource_count
        # The number of resource groups in the cost center.
        self.resource_group_count = resource_group_count
        # The number of sub-cost centers in the cost center.
        self.sub_unit_count = sub_unit_count
        # The total number of resource instances, including resource instances of sub-cost centers, in the cost center.
        self.total_resource_count = total_resource_count
        # The total number of resource groups, including resource groups of sub-cost centers, in the cost center.
        self.total_resource_group_count = total_resource_group_count
        # The total number of the associated accounts, including associated accounts of sub-cost centers, in the cost center.
        self.total_user_count = total_user_count
        # The number of sub-cost centers in the cost center.
        self.user_count = user_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_count is not None:
            result['ResourceCount'] = self.resource_count

        if self.resource_group_count is not None:
            result['ResourceGroupCount'] = self.resource_group_count

        if self.sub_unit_count is not None:
            result['SubUnitCount'] = self.sub_unit_count

        if self.total_resource_count is not None:
            result['TotalResourceCount'] = self.total_resource_count

        if self.total_resource_group_count is not None:
            result['TotalResourceGroupCount'] = self.total_resource_group_count

        if self.total_user_count is not None:
            result['TotalUserCount'] = self.total_user_count

        if self.user_count is not None:
            result['UserCount'] = self.user_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceCount') is not None:
            self.resource_count = m.get('ResourceCount')

        if m.get('ResourceGroupCount') is not None:
            self.resource_group_count = m.get('ResourceGroupCount')

        if m.get('SubUnitCount') is not None:
            self.sub_unit_count = m.get('SubUnitCount')

        if m.get('TotalResourceCount') is not None:
            self.total_resource_count = m.get('TotalResourceCount')

        if m.get('TotalResourceGroupCount') is not None:
            self.total_resource_group_count = m.get('TotalResourceGroupCount')

        if m.get('TotalUserCount') is not None:
            self.total_user_count = m.get('TotalUserCount')

        if m.get('UserCount') is not None:
            self.user_count = m.get('UserCount')

        return self

class QueryCostUnitResourceResponseBodyDataCostUnit(DaraModel):
    def __init__(
        self,
        owner_uid: int = None,
        parent_unit_id: int = None,
        unit_id: int = None,
        unit_name: str = None,
    ):
        # The user ID of the cost center owner.
        self.owner_uid = owner_uid
        # The ID of the parent cost center. A value of -1 indicates the root cost center.
        self.parent_unit_id = parent_unit_id
        # The ID of the cost center.
        self.unit_id = unit_id
        # The name of the cost center.
        self.unit_name = unit_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid

        if self.parent_unit_id is not None:
            result['ParentUnitId'] = self.parent_unit_id

        if self.unit_id is not None:
            result['UnitId'] = self.unit_id

        if self.unit_name is not None:
            result['UnitName'] = self.unit_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')

        if m.get('ParentUnitId') is not None:
            self.parent_unit_id = m.get('ParentUnitId')

        if m.get('UnitId') is not None:
            self.unit_id = m.get('UnitId')

        if m.get('UnitName') is not None:
            self.unit_name = m.get('UnitName')

        return self

