# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_bssopenapi20230930 import models as main_models
from darabonba.model import DaraModel

class QueryCostCenterResourceResponseBody(DaraModel):
    def __init__(
        self,
        cost_center_resource_dto_list: List[main_models.QueryCostCenterResourceResponseBodyCostCenterResourceDtoList] = None,
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
            for v1 in self.cost_center_resource_dto_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CostCenterResourceDtoList'] = []
        if self.cost_center_resource_dto_list is not None:
            for k1 in self.cost_center_resource_dto_list:
                result['CostCenterResourceDtoList'].append(k1.to_map() if k1 else None)

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
            for k1 in m.get('CostCenterResourceDtoList'):
                temp_model = main_models.QueryCostCenterResourceResponseBodyCostCenterResourceDtoList()
                self.cost_center_resource_dto_list.append(temp_model.from_map(k1))

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

class QueryCostCenterResourceResponseBodyCostCenterResourceDtoList(DaraModel):
    def __init__(
        self,
        add_strategy: str = None,
        add_strategy_name: str = None,
        applicable_period_num: int = None,
        apportion_item_code: str = None,
        apportion_item_name: str = None,
        commodity_code: str = None,
        commodity_name: str = None,
        cost_center_code: str = None,
        cost_center_create_time: str = None,
        cost_center_id: int = None,
        cost_center_name: str = None,
        cost_center_update_time: str = None,
        finance_unit_rule_version: int = None,
        instance_id: str = None,
        master_commodity_code: str = None,
        master_instance_id: str = None,
        owner_account_id: int = None,
        owner_account_name: str = None,
        parent_cost_center_id: int = None,
        pip_code: str = None,
        pip_name: str = None,
        recent_billing_month: int = None,
        region_name: str = None,
        region_no: str = None,
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
        start_billing_month: int = None,
    ):
        self.add_strategy = add_strategy
        self.add_strategy_name = add_strategy_name
        self.applicable_period_num = applicable_period_num
        self.apportion_item_code = apportion_item_code
        self.apportion_item_name = apportion_item_name
        self.commodity_code = commodity_code
        self.commodity_name = commodity_name
        self.cost_center_code = cost_center_code
        self.cost_center_create_time = cost_center_create_time
        self.cost_center_id = cost_center_id
        self.cost_center_name = cost_center_name
        self.cost_center_update_time = cost_center_update_time
        self.finance_unit_rule_version = finance_unit_rule_version
        self.instance_id = instance_id
        self.master_commodity_code = master_commodity_code
        self.master_instance_id = master_instance_id
        self.owner_account_id = owner_account_id
        self.owner_account_name = owner_account_name
        self.parent_cost_center_id = parent_cost_center_id
        self.pip_code = pip_code
        self.pip_name = pip_name
        self.recent_billing_month = recent_billing_month
        self.region_name = region_name
        self.region_no = region_no
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
        self.start_billing_month = start_billing_month

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_strategy is not None:
            result['AddStrategy'] = self.add_strategy

        if self.add_strategy_name is not None:
            result['AddStrategyName'] = self.add_strategy_name

        if self.applicable_period_num is not None:
            result['ApplicablePeriodNum'] = self.applicable_period_num

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

        if self.finance_unit_rule_version is not None:
            result['FinanceUnitRuleVersion'] = self.finance_unit_rule_version

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.master_commodity_code is not None:
            result['MasterCommodityCode'] = self.master_commodity_code

        if self.master_instance_id is not None:
            result['MasterInstanceId'] = self.master_instance_id

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

        if self.recent_billing_month is not None:
            result['RecentBillingMonth'] = self.recent_billing_month

        if self.region_name is not None:
            result['RegionName'] = self.region_name

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

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

        if self.start_billing_month is not None:
            result['StartBillingMonth'] = self.start_billing_month

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddStrategy') is not None:
            self.add_strategy = m.get('AddStrategy')

        if m.get('AddStrategyName') is not None:
            self.add_strategy_name = m.get('AddStrategyName')

        if m.get('ApplicablePeriodNum') is not None:
            self.applicable_period_num = m.get('ApplicablePeriodNum')

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

        if m.get('FinanceUnitRuleVersion') is not None:
            self.finance_unit_rule_version = m.get('FinanceUnitRuleVersion')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MasterCommodityCode') is not None:
            self.master_commodity_code = m.get('MasterCommodityCode')

        if m.get('MasterInstanceId') is not None:
            self.master_instance_id = m.get('MasterInstanceId')

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

        if m.get('RecentBillingMonth') is not None:
            self.recent_billing_month = m.get('RecentBillingMonth')

        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

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

        if m.get('StartBillingMonth') is not None:
            self.start_billing_month = m.get('StartBillingMonth')

        return self

