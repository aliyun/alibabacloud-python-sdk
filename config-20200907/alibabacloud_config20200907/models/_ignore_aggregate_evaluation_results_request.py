# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class IgnoreAggregateEvaluationResultsRequest(DaraModel):
    def __init__(
        self,
        aggregator_id: str = None,
        config_rule_id: str = None,
        ignore_date: str = None,
        reason: str = None,
        resources: List[main_models.IgnoreAggregateEvaluationResultsRequestResources] = None,
    ):
        # The ID of the account group.
        # 
        # For more information about how to obtain the ID of an account group, see [ListAggregators](https://help.aliyun.com/document_detail/255797.html).
        # 
        # This parameter is required.
        self.aggregator_id = aggregator_id
        # The ID of the rule.
        # 
        # For more information about how to obtain the ID of a rule, see [ListAggregateConfigRules](https://help.aliyun.com/document_detail/264148.html).
        # 
        # This parameter is required.
        self.config_rule_id = config_rule_id
        # The date from which the system automatically re-evaluates the ignored incompliant resources.
        # 
        # >  If you leave this parameter empty, the system does not automatically re-evaluate the ignored incompliant resources. You must manually re-evaluate the ignored incompliant resources.
        self.ignore_date = ignore_date
        # The reason why you ignore the resource.
        self.reason = reason
        # The resources to be ignored.
        # 
        # This parameter is required.
        self.resources = resources

    def validate(self):
        if self.resources:
            for v1 in self.resources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id

        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id

        if self.ignore_date is not None:
            result['IgnoreDate'] = self.ignore_date

        if self.reason is not None:
            result['Reason'] = self.reason

        result['Resources'] = []
        if self.resources is not None:
            for k1 in self.resources:
                result['Resources'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')

        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')

        if m.get('IgnoreDate') is not None:
            self.ignore_date = m.get('IgnoreDate')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        self.resources = []
        if m.get('Resources') is not None:
            for k1 in m.get('Resources'):
                temp_model = main_models.IgnoreAggregateEvaluationResultsRequestResources()
                self.resources.append(temp_model.from_map(k1))

        return self

class IgnoreAggregateEvaluationResultsRequestResources(DaraModel):
    def __init__(
        self,
        region: str = None,
        resource_account_id: int = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # The ID of the region in which the resource resides.
        # 
        # For more information about how to obtain the ID of a region, see [ListAggregateDiscoveredResources](https://help.aliyun.com/document_detail/265983.html).
        # 
        # This parameter is required.
        self.region = region
        # The ID of the Alibaba Cloud account to which the resources belong.
        # 
        # >  You must specify the ID of the current management account or a member account in the account group of the management account.
        # 
        # This parameter is required.
        self.resource_account_id = resource_account_id
        # The ID of the resource.
        # 
        # For more information about how to query the ID of a resource, see [ListAggregateDiscoveredResources](https://help.aliyun.com/document_detail/265983.html).
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The type of the resource.
        # 
        # For more information about how to query the type of a resource, see [ListAggregateDiscoveredResources](https://help.aliyun.com/document_detail/265983.html).
        # 
        # This parameter is required.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region is not None:
            result['Region'] = self.region

        if self.resource_account_id is not None:
            result['ResourceAccountId'] = self.resource_account_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('ResourceAccountId') is not None:
            self.resource_account_id = m.get('ResourceAccountId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

