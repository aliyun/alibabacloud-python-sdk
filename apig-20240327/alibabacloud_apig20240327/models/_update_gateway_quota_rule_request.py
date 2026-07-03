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
        # The list of principal (consumer) IDs to bind.
        self.add_ids = add_ids
        # The conflict snapshot hash, used to prevent concurrent dirty overwrites when confirming an overwrite. Obtain this value from the response of a prior dryRun=true call.
        # 
        # This parameter is not required in the following cases: no conflicts exist, the call is a dry run (dryRun=true), or overwrite is set to false.
        # 
        # When dryRun is set to false and overwrite is set to true, if this parameter is missing or the value has expired and no longer matches, the backend returns accepted=false with a new conflict preview. Perform the dry run again to confirm the new conflicts.
        self.conflict_hash = conflict_hash
        # The list of consumer group IDs. This parameter is not supported.
        self.consumer_group_ids = consumer_group_ids
        # Specifies whether to perform a dry run only without persisting or applying the configuration. A dry run checks whether conflicting rules exist on the bound consumers. For example, a consumer that already has a calendar-day quota cannot have another calendar-day quota rule added.
        self.dry_run = dry_run
        # Specifies whether to allow overwriting when a conflict exists. If overwriting is allowed, the conflicting principals (consumers) are unbound from the old rule and bound to the new rule.
        self.overwrite = overwrite
        # The updated total available quota.
        self.quota_limit = quota_limit
        # The list of principal (consumer) IDs to unbind.
        self.remove_ids = remove_ids
        # The updated rule name.
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

