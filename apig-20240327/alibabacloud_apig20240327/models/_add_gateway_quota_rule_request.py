# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AddGatewayQuotaRuleRequest(DaraModel):
    def __init__(
        self,
        conflict_hash: str = None,
        consumer_group_ids: List[str] = None,
        consumer_ids: List[str] = None,
        dry_run: bool = None,
        overwrite: bool = None,
        period_type: str = None,
        quota_dimension: str = None,
        quota_limit: int = None,
        rule_name: str = None,
        timezone: str = None,
        window_alignment: str = None,
    ):
        self.conflict_hash = conflict_hash
        self.consumer_group_ids = consumer_group_ids
        self.consumer_ids = consumer_ids
        self.dry_run = dry_run
        self.overwrite = overwrite
        # This parameter is required.
        self.period_type = period_type
        # This parameter is required.
        self.quota_dimension = quota_dimension
        # This parameter is required.
        self.quota_limit = quota_limit
        # This parameter is required.
        self.rule_name = rule_name
        self.timezone = timezone
        self.window_alignment = window_alignment

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conflict_hash is not None:
            result['conflictHash'] = self.conflict_hash

        if self.consumer_group_ids is not None:
            result['consumerGroupIds'] = self.consumer_group_ids

        if self.consumer_ids is not None:
            result['consumerIds'] = self.consumer_ids

        if self.dry_run is not None:
            result['dryRun'] = self.dry_run

        if self.overwrite is not None:
            result['overwrite'] = self.overwrite

        if self.period_type is not None:
            result['periodType'] = self.period_type

        if self.quota_dimension is not None:
            result['quotaDimension'] = self.quota_dimension

        if self.quota_limit is not None:
            result['quotaLimit'] = self.quota_limit

        if self.rule_name is not None:
            result['ruleName'] = self.rule_name

        if self.timezone is not None:
            result['timezone'] = self.timezone

        if self.window_alignment is not None:
            result['windowAlignment'] = self.window_alignment

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('conflictHash') is not None:
            self.conflict_hash = m.get('conflictHash')

        if m.get('consumerGroupIds') is not None:
            self.consumer_group_ids = m.get('consumerGroupIds')

        if m.get('consumerIds') is not None:
            self.consumer_ids = m.get('consumerIds')

        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')

        if m.get('overwrite') is not None:
            self.overwrite = m.get('overwrite')

        if m.get('periodType') is not None:
            self.period_type = m.get('periodType')

        if m.get('quotaDimension') is not None:
            self.quota_dimension = m.get('quotaDimension')

        if m.get('quotaLimit') is not None:
            self.quota_limit = m.get('quotaLimit')

        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')

        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')

        if m.get('windowAlignment') is not None:
            self.window_alignment = m.get('windowAlignment')

        return self

