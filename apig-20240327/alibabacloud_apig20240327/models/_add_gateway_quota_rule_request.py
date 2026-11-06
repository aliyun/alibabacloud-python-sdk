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
        period_multiplier: int = None,
        period_type: str = None,
        quota_dimension: str = None,
        quota_limit: int = None,
        rule_name: str = None,
        subject_type: str = None,
        timezone: str = None,
        window_alignment: str = None,
    ):
        # The conflict snapshot hash used to prevent concurrent dirty overwrites when you confirm an overwrite. You can obtain this value by first performing a dry run with dryRun=true and extracting it from the response.
        # 
        # You do not need to specify this parameter in the following scenarios: no conflict exists; you are only performing a dry run with dryRun=true; or overwrite=false, which means you do not confirm the overwrite.
        # 
        # If dryRun=false and overwrite=true but this parameter is not specified or has expired and does not match, the backend returns accepted=false along with a new conflict preview. In this case, you must perform a dry run again to confirm the new conflict.
        self.conflict_hash = conflict_hash
        # The list of consumer group IDs to which the rule is bound.
        self.consumer_group_ids = consumer_group_ids
        # The list of consumer IDs to which the rule is bound. You can specify up to 1,000 consumers in a single request.
        self.consumer_ids = consumer_ids
        # Specifies whether to perform only a dry run without saving data to the database or delivering actual configurations. This parameter is used to check whether conflicting rules exist on the bound consumption subjects. A single consumption subject cannot be configured with two natural period quotas of the same period. For example, a consumption subject that already has a natural day quota cannot be added with another natural day quota rule.
        self.dry_run = dry_run
        # Specifies whether to allow overwriting when a conflict occurs. If you allow overwriting, the conflicting subjects (consumers or consumer groups) are unbound from the old rule and bound to the new rule.
        self.overwrite = overwrite
        # The period multiplier. This parameter applies to custom period rules.
        self.period_multiplier = period_multiplier
        # The period type. Natural periods support daily, weekly, and monthly statistics. Valid values: day, week, and month. Custom periods support only daily statistics, and the value is fixed to day.
        # 
        # This parameter is required.
        self.period_type = period_type
        # The quota dimension or limit type. Valid values: token and credit.
        # 
        # This parameter is required.
        self.quota_dimension = quota_dimension
        # The total available quota (limit) for the period.
        # 
        # This parameter is required.
        self.quota_limit = quota_limit
        # The name of the rule.
        # 
        # This parameter is required.
        self.rule_name = rule_name
        # The subject type of the rule. consumer indicates a consumer, and consumer_group indicates a consumer group. If you do not specify this parameter, the default value is consumer.
        self.subject_type = subject_type
        # The time zone corresponding to the natural period in the UTC+x format.
        self.timezone = timezone
        # The reset period type. Natural periods (windowAlignment=calendar) and custom periods (windowAlignment=epoch) are supported.
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

        if self.period_multiplier is not None:
            result['periodMultiplier'] = self.period_multiplier

        if self.period_type is not None:
            result['periodType'] = self.period_type

        if self.quota_dimension is not None:
            result['quotaDimension'] = self.quota_dimension

        if self.quota_limit is not None:
            result['quotaLimit'] = self.quota_limit

        if self.rule_name is not None:
            result['ruleName'] = self.rule_name

        if self.subject_type is not None:
            result['subjectType'] = self.subject_type

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

        if m.get('periodMultiplier') is not None:
            self.period_multiplier = m.get('periodMultiplier')

        if m.get('periodType') is not None:
            self.period_type = m.get('periodType')

        if m.get('quotaDimension') is not None:
            self.quota_dimension = m.get('quotaDimension')

        if m.get('quotaLimit') is not None:
            self.quota_limit = m.get('quotaLimit')

        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')

        if m.get('subjectType') is not None:
            self.subject_type = m.get('subjectType')

        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')

        if m.get('windowAlignment') is not None:
            self.window_alignment = m.get('windowAlignment')

        return self

