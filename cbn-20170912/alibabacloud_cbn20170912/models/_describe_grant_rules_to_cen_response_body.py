# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class DescribeGrantRulesToCenResponseBody(DaraModel):
    def __init__(
        self,
        grant_rules: main_models.DescribeGrantRulesToCenResponseBodyGrantRules = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.grant_rules = grant_rules
        # *   If no value is specified for **MaxResults**, query results are returned in one batch. The value of **MaxResults** indicates the total number of entries.
        # *   If a value is specified for **MaxResults**, it indicates that you need to query results in batches. The value of **MaxResults** in the response indicates the number of entries in the current batch.
        self.max_results = max_results
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, no next page exists.
        # *   If a value of **NextToken** was returned in the previous query, specify the value to obtain the next set of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.grant_rules:
            self.grant_rules.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.grant_rules is not None:
            result['GrantRules'] = self.grant_rules.to_map()

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GrantRules') is not None:
            temp_model = main_models.DescribeGrantRulesToCenResponseBodyGrantRules()
            self.grant_rules = temp_model.from_map(m.get('GrantRules'))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeGrantRulesToCenResponseBodyGrantRules(DaraModel):
    def __init__(
        self,
        grant_rule: List[main_models.DescribeGrantRulesToCenResponseBodyGrantRulesGrantRule] = None,
    ):
        self.grant_rule = grant_rule

    def validate(self):
        if self.grant_rule:
            for v1 in self.grant_rule:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['GrantRule'] = []
        if self.grant_rule is not None:
            for k1 in self.grant_rule:
                result['GrantRule'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.grant_rule = []
        if m.get('GrantRule') is not None:
            for k1 in m.get('GrantRule'):
                temp_model = main_models.DescribeGrantRulesToCenResponseBodyGrantRulesGrantRule()
                self.grant_rule.append(temp_model.from_map(k1))

        return self

class DescribeGrantRulesToCenResponseBodyGrantRulesGrantRule(DaraModel):
    def __init__(
        self,
        cen_id: str = None,
        cen_owner_id: int = None,
        child_instance_id: str = None,
        child_instance_owner_id: int = None,
        child_instance_region_id: str = None,
        child_instance_type: str = None,
        create_time: int = None,
        effective_order_type: str = None,
        order_type: str = None,
    ):
        self.cen_id = cen_id
        self.cen_owner_id = cen_owner_id
        self.child_instance_id = child_instance_id
        self.child_instance_owner_id = child_instance_owner_id
        self.child_instance_region_id = child_instance_region_id
        self.child_instance_type = child_instance_type
        self.create_time = create_time
        self.effective_order_type = effective_order_type
        self.order_type = order_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.cen_owner_id is not None:
            result['CenOwnerId'] = self.cen_owner_id

        if self.child_instance_id is not None:
            result['ChildInstanceId'] = self.child_instance_id

        if self.child_instance_owner_id is not None:
            result['ChildInstanceOwnerId'] = self.child_instance_owner_id

        if self.child_instance_region_id is not None:
            result['ChildInstanceRegionId'] = self.child_instance_region_id

        if self.child_instance_type is not None:
            result['ChildInstanceType'] = self.child_instance_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.effective_order_type is not None:
            result['EffectiveOrderType'] = self.effective_order_type

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('CenOwnerId') is not None:
            self.cen_owner_id = m.get('CenOwnerId')

        if m.get('ChildInstanceId') is not None:
            self.child_instance_id = m.get('ChildInstanceId')

        if m.get('ChildInstanceOwnerId') is not None:
            self.child_instance_owner_id = m.get('ChildInstanceOwnerId')

        if m.get('ChildInstanceRegionId') is not None:
            self.child_instance_region_id = m.get('ChildInstanceRegionId')

        if m.get('ChildInstanceType') is not None:
            self.child_instance_type = m.get('ChildInstanceType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EffectiveOrderType') is not None:
            self.effective_order_type = m.get('EffectiveOrderType')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        return self

