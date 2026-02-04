# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20241212 import models as main_models
from darabonba.model import DaraModel

class ListNormalizationRuleVersionsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        normalization_rule_versions: List[main_models.ListNormalizationRuleVersionsResponseBodyNormalizationRuleVersions] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.normalization_rule_versions = normalization_rule_versions
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.normalization_rule_versions:
            for v1 in self.normalization_rule_versions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['NormalizationRuleVersions'] = []
        if self.normalization_rule_versions is not None:
            for k1 in self.normalization_rule_versions:
                result['NormalizationRuleVersions'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.normalization_rule_versions = []
        if m.get('NormalizationRuleVersions') is not None:
            for k1 in m.get('NormalizationRuleVersions'):
                temp_model = main_models.ListNormalizationRuleVersionsResponseBodyNormalizationRuleVersions()
                self.normalization_rule_versions.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListNormalizationRuleVersionsResponseBodyNormalizationRuleVersions(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        normalization_rule_expression: str = None,
        normalization_rule_id: str = None,
        normalization_rule_version: int = None,
        update_time: int = None,
    ):
        self.create_time = create_time
        self.normalization_rule_expression = normalization_rule_expression
        self.normalization_rule_id = normalization_rule_id
        self.normalization_rule_version = normalization_rule_version
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.normalization_rule_expression is not None:
            result['NormalizationRuleExpression'] = self.normalization_rule_expression

        if self.normalization_rule_id is not None:
            result['NormalizationRuleId'] = self.normalization_rule_id

        if self.normalization_rule_version is not None:
            result['NormalizationRuleVersion'] = self.normalization_rule_version

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('NormalizationRuleExpression') is not None:
            self.normalization_rule_expression = m.get('NormalizationRuleExpression')

        if m.get('NormalizationRuleId') is not None:
            self.normalization_rule_id = m.get('NormalizationRuleId')

        if m.get('NormalizationRuleVersion') is not None:
            self.normalization_rule_version = m.get('NormalizationRuleVersion')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

