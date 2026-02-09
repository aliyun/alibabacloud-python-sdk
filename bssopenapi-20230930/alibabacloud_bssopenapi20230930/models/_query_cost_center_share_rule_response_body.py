# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_bssopenapi20230930 import models as main_models
from darabonba.model import DaraModel

class QueryCostCenterShareRuleResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.QueryCostCenterShareRuleResponseBodyData] = None,
        max_results: int = None,
        metadata: Any = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.data = data
        self.max_results = max_results
        self.metadata = metadata
        self.next_token = next_token
        self.request_id = request_id
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
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

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
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.QueryCostCenterShareRuleResponseBodyData()
                self.data.append(temp_model.from_map(k1))

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

class QueryCostCenterShareRuleResponseBodyData(DaraModel):
    def __init__(
        self,
        from_cost_center_share_rule_details: List[main_models.QueryCostCenterShareRuleResponseBodyDataFromCostCenterShareRuleDetails] = None,
        gmt_modified: str = None,
        owner_account_id: int = None,
        share_rule_id: int = None,
        share_rule_name: str = None,
        share_rule_type: str = None,
        to_cost_center_share_rule_details: List[main_models.QueryCostCenterShareRuleResponseBodyDataToCostCenterShareRuleDetails] = None,
    ):
        self.from_cost_center_share_rule_details = from_cost_center_share_rule_details
        self.gmt_modified = gmt_modified
        self.owner_account_id = owner_account_id
        self.share_rule_id = share_rule_id
        self.share_rule_name = share_rule_name
        self.share_rule_type = share_rule_type
        self.to_cost_center_share_rule_details = to_cost_center_share_rule_details

    def validate(self):
        if self.from_cost_center_share_rule_details:
            for v1 in self.from_cost_center_share_rule_details:
                 if v1:
                    v1.validate()
        if self.to_cost_center_share_rule_details:
            for v1 in self.to_cost_center_share_rule_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FromCostCenterShareRuleDetails'] = []
        if self.from_cost_center_share_rule_details is not None:
            for k1 in self.from_cost_center_share_rule_details:
                result['FromCostCenterShareRuleDetails'].append(k1.to_map() if k1 else None)

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.owner_account_id is not None:
            result['OwnerAccountId'] = self.owner_account_id

        if self.share_rule_id is not None:
            result['ShareRuleId'] = self.share_rule_id

        if self.share_rule_name is not None:
            result['ShareRuleName'] = self.share_rule_name

        if self.share_rule_type is not None:
            result['ShareRuleType'] = self.share_rule_type

        result['ToCostCenterShareRuleDetails'] = []
        if self.to_cost_center_share_rule_details is not None:
            for k1 in self.to_cost_center_share_rule_details:
                result['ToCostCenterShareRuleDetails'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.from_cost_center_share_rule_details = []
        if m.get('FromCostCenterShareRuleDetails') is not None:
            for k1 in m.get('FromCostCenterShareRuleDetails'):
                temp_model = main_models.QueryCostCenterShareRuleResponseBodyDataFromCostCenterShareRuleDetails()
                self.from_cost_center_share_rule_details.append(temp_model.from_map(k1))

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('OwnerAccountId') is not None:
            self.owner_account_id = m.get('OwnerAccountId')

        if m.get('ShareRuleId') is not None:
            self.share_rule_id = m.get('ShareRuleId')

        if m.get('ShareRuleName') is not None:
            self.share_rule_name = m.get('ShareRuleName')

        if m.get('ShareRuleType') is not None:
            self.share_rule_type = m.get('ShareRuleType')

        self.to_cost_center_share_rule_details = []
        if m.get('ToCostCenterShareRuleDetails') is not None:
            for k1 in m.get('ToCostCenterShareRuleDetails'):
                temp_model = main_models.QueryCostCenterShareRuleResponseBodyDataToCostCenterShareRuleDetails()
                self.to_cost_center_share_rule_details.append(temp_model.from_map(k1))

        return self

class QueryCostCenterShareRuleResponseBodyDataToCostCenterShareRuleDetails(DaraModel):
    def __init__(
        self,
        cost_center_code: str = None,
        cost_center_id: int = None,
        cost_center_name: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        owner_account_id: int = None,
        parent_cost_center_id: int = None,
        prev_cost_center_id: int = None,
        root_cost_center_id: int = None,
        share_ratio: float = None,
    ):
        self.cost_center_code = cost_center_code
        self.cost_center_id = cost_center_id
        self.cost_center_name = cost_center_name
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.owner_account_id = owner_account_id
        self.parent_cost_center_id = parent_cost_center_id
        self.prev_cost_center_id = prev_cost_center_id
        self.root_cost_center_id = root_cost_center_id
        self.share_ratio = share_ratio

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cost_center_code is not None:
            result['CostCenterCode'] = self.cost_center_code

        if self.cost_center_id is not None:
            result['CostCenterId'] = self.cost_center_id

        if self.cost_center_name is not None:
            result['CostCenterName'] = self.cost_center_name

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.owner_account_id is not None:
            result['OwnerAccountId'] = self.owner_account_id

        if self.parent_cost_center_id is not None:
            result['ParentCostCenterId'] = self.parent_cost_center_id

        if self.prev_cost_center_id is not None:
            result['PrevCostCenterId'] = self.prev_cost_center_id

        if self.root_cost_center_id is not None:
            result['RootCostCenterId'] = self.root_cost_center_id

        if self.share_ratio is not None:
            result['ShareRatio'] = self.share_ratio

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostCenterCode') is not None:
            self.cost_center_code = m.get('CostCenterCode')

        if m.get('CostCenterId') is not None:
            self.cost_center_id = m.get('CostCenterId')

        if m.get('CostCenterName') is not None:
            self.cost_center_name = m.get('CostCenterName')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('OwnerAccountId') is not None:
            self.owner_account_id = m.get('OwnerAccountId')

        if m.get('ParentCostCenterId') is not None:
            self.parent_cost_center_id = m.get('ParentCostCenterId')

        if m.get('PrevCostCenterId') is not None:
            self.prev_cost_center_id = m.get('PrevCostCenterId')

        if m.get('RootCostCenterId') is not None:
            self.root_cost_center_id = m.get('RootCostCenterId')

        if m.get('ShareRatio') is not None:
            self.share_ratio = m.get('ShareRatio')

        return self

class QueryCostCenterShareRuleResponseBodyDataFromCostCenterShareRuleDetails(DaraModel):
    def __init__(
        self,
        cost_center_code: str = None,
        cost_center_id: int = None,
        cost_center_name: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        owner_account_id: int = None,
        parent_cost_center_id: int = None,
        prev_cost_center_id: int = None,
        root_cost_center_id: int = None,
    ):
        self.cost_center_code = cost_center_code
        self.cost_center_id = cost_center_id
        self.cost_center_name = cost_center_name
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.owner_account_id = owner_account_id
        self.parent_cost_center_id = parent_cost_center_id
        self.prev_cost_center_id = prev_cost_center_id
        self.root_cost_center_id = root_cost_center_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cost_center_code is not None:
            result['CostCenterCode'] = self.cost_center_code

        if self.cost_center_id is not None:
            result['CostCenterId'] = self.cost_center_id

        if self.cost_center_name is not None:
            result['CostCenterName'] = self.cost_center_name

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.owner_account_id is not None:
            result['OwnerAccountId'] = self.owner_account_id

        if self.parent_cost_center_id is not None:
            result['ParentCostCenterId'] = self.parent_cost_center_id

        if self.prev_cost_center_id is not None:
            result['PrevCostCenterId'] = self.prev_cost_center_id

        if self.root_cost_center_id is not None:
            result['RootCostCenterId'] = self.root_cost_center_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostCenterCode') is not None:
            self.cost_center_code = m.get('CostCenterCode')

        if m.get('CostCenterId') is not None:
            self.cost_center_id = m.get('CostCenterId')

        if m.get('CostCenterName') is not None:
            self.cost_center_name = m.get('CostCenterName')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('OwnerAccountId') is not None:
            self.owner_account_id = m.get('OwnerAccountId')

        if m.get('ParentCostCenterId') is not None:
            self.parent_cost_center_id = m.get('ParentCostCenterId')

        if m.get('PrevCostCenterId') is not None:
            self.prev_cost_center_id = m.get('PrevCostCenterId')

        if m.get('RootCostCenterId') is not None:
            self.root_cost_center_id = m.get('RootCostCenterId')

        return self

