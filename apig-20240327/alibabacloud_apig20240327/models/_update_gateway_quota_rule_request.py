# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateGatewayQuotaRuleRequest(DaraModel):
    def __init__(
        self,
        add_ids: List[str] = None,
        conflict_hash: str = None,
        consumer_group_ids: List[str] = None,
        dry_run: bool = None,
        overwrite: bool = None,
        quota_limit: int = None,
        remove_ids: List[str] = None,
        rule_name: str = None,
    ):
        self.add_ids = add_ids
        self.conflict_hash = conflict_hash
        self.consumer_group_ids = consumer_group_ids
        self.dry_run = dry_run
        self.overwrite = overwrite
        self.quota_limit = quota_limit
        self.remove_ids = remove_ids
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_ids is not None:
            result['addIds'] = self.add_ids

        if self.conflict_hash is not None:
            result['conflictHash'] = self.conflict_hash

        if self.consumer_group_ids is not None:
            result['consumerGroupIds'] = self.consumer_group_ids

        if self.dry_run is not None:
            result['dryRun'] = self.dry_run

        if self.overwrite is not None:
            result['overwrite'] = self.overwrite

        if self.quota_limit is not None:
            result['quotaLimit'] = self.quota_limit

        if self.remove_ids is not None:
            result['removeIds'] = self.remove_ids

        if self.rule_name is not None:
            result['ruleName'] = self.rule_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('addIds') is not None:
            self.add_ids = m.get('addIds')

        if m.get('conflictHash') is not None:
            self.conflict_hash = m.get('conflictHash')

        if m.get('consumerGroupIds') is not None:
            self.consumer_group_ids = m.get('consumerGroupIds')

        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')

        if m.get('overwrite') is not None:
            self.overwrite = m.get('overwrite')

        if m.get('quotaLimit') is not None:
            self.quota_limit = m.get('quotaLimit')

        if m.get('removeIds') is not None:
            self.remove_ids = m.get('removeIds')

        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')

        return self

