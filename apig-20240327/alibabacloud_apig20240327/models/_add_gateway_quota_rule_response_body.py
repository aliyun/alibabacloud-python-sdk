# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class AddGatewayQuotaRuleResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.AddGatewayQuotaRuleResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code or error code.
        self.code = code
        # The response data.
        self.data = data
        # The message content.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.AddGatewayQuotaRuleResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class AddGatewayQuotaRuleResponseBodyData(DaraModel):
    def __init__(
        self,
        accepted: bool = None,
        conflict_preview: main_models.AddGatewayQuotaRuleResponseBodyDataConflictPreview = None,
        dry_run: bool = None,
        rule_id: str = None,
    ):
        # Indicates whether the write request is accepted by the system. A value of false typically indicates a retryable scenario, such as an unconfirmed conflict overwrite.
        self.accepted = accepted
        # The conflict preview.
        self.conflict_preview = conflict_preview
        # Indicates whether the request is a dry run.
        self.dry_run = dry_run
        # The rule ID.
        self.rule_id = rule_id

    def validate(self):
        if self.conflict_preview:
            self.conflict_preview.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accepted is not None:
            result['accepted'] = self.accepted

        if self.conflict_preview is not None:
            result['conflictPreview'] = self.conflict_preview.to_map()

        if self.dry_run is not None:
            result['dryRun'] = self.dry_run

        if self.rule_id is not None:
            result['ruleId'] = self.rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accepted') is not None:
            self.accepted = m.get('accepted')

        if m.get('conflictPreview') is not None:
            temp_model = main_models.AddGatewayQuotaRuleResponseBodyDataConflictPreview()
            self.conflict_preview = temp_model.from_map(m.get('conflictPreview'))

        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')

        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')

        return self

class AddGatewayQuotaRuleResponseBodyDataConflictPreview(DaraModel):
    def __init__(
        self,
        conflict_hash: str = None,
        items: List[main_models.AddGatewayQuotaRuleResponseBodyDataConflictPreviewItems] = None,
        total_conflict_count: int = None,
    ):
        # The hash of the conflict snapshot.
        self.conflict_hash = conflict_hash
        # The list of conflicting entities (consumers).
        self.items = items
        # The total number of conflicts.
        self.total_conflict_count = total_conflict_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conflict_hash is not None:
            result['conflictHash'] = self.conflict_hash

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.total_conflict_count is not None:
            result['totalConflictCount'] = self.total_conflict_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('conflictHash') is not None:
            self.conflict_hash = m.get('conflictHash')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.AddGatewayQuotaRuleResponseBodyDataConflictPreviewItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('totalConflictCount') is not None:
            self.total_conflict_count = m.get('totalConflictCount')

        return self

class AddGatewayQuotaRuleResponseBodyDataConflictPreviewItems(DaraModel):
    def __init__(
        self,
        conflict_period_type: str = None,
        conflict_type: str = None,
        consumer_id: str = None,
        consumer_name: str = None,
    ):
        # The period type of the existing conflicting rule on the consumer. A value of day, week, or month indicates that the conflicting rule uses a daily, weekly, or monthly period respectively.
        self.conflict_period_type = conflict_period_type
        # The type of the existing conflicting rule on the consumer. A value of calendar indicates that the conflicting rule uses a calendar period. A value of epoch indicates that the conflicting rule uses a custom period.
        self.conflict_type = conflict_type
        # The consumer ID.
        self.consumer_id = consumer_id
        # The consumer name.
        self.consumer_name = consumer_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conflict_period_type is not None:
            result['conflictPeriodType'] = self.conflict_period_type

        if self.conflict_type is not None:
            result['conflictType'] = self.conflict_type

        if self.consumer_id is not None:
            result['consumerId'] = self.consumer_id

        if self.consumer_name is not None:
            result['consumerName'] = self.consumer_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('conflictPeriodType') is not None:
            self.conflict_period_type = m.get('conflictPeriodType')

        if m.get('conflictType') is not None:
            self.conflict_type = m.get('conflictType')

        if m.get('consumerId') is not None:
            self.consumer_id = m.get('consumerId')

        if m.get('consumerName') is not None:
            self.consumer_name = m.get('consumerName')

        return self

