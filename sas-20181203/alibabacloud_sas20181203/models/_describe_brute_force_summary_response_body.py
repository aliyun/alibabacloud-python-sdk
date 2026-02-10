# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeBruteForceSummaryResponseBody(DaraModel):
    def __init__(
        self,
        brute_force_summary: main_models.DescribeBruteForceSummaryResponseBodyBruteForceSummary = None,
        request_id: str = None,
    ):
        # The statistics of IP address blocking policies.
        self.brute_force_summary = brute_force_summary
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.brute_force_summary:
            self.brute_force_summary.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.brute_force_summary is not None:
            result['BruteForceSummary'] = self.brute_force_summary.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BruteForceSummary') is not None:
            temp_model = main_models.DescribeBruteForceSummaryResponseBodyBruteForceSummary()
            self.brute_force_summary = temp_model.from_map(m.get('BruteForceSummary'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeBruteForceSummaryResponseBodyBruteForceSummary(DaraModel):
    def __init__(
        self,
        all_strategy_count: int = None,
        anti_brute_force_rule_count: str = None,
        custom_effective_count: str = None,
        custom_record_count: str = None,
        effective_count: int = None,
        system_effective_count: str = None,
        system_record_count: str = None,
    ):
        # The number of anti-brute force IP blocking policies.
        self.all_strategy_count = all_strategy_count
        # The number of defense policies.
        self.anti_brute_force_rule_count = anti_brute_force_rule_count
        # The number of custom blocking rules that are in effect.
        self.custom_effective_count = custom_effective_count
        # The number of custom blocking rules.
        self.custom_record_count = custom_record_count
        # The number of anti-brute force IP blocking policies enabled.
        self.effective_count = effective_count
        # The number of system blocking rules that are in effect.
        self.system_effective_count = system_effective_count
        # The number of system blocking rules.
        self.system_record_count = system_record_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.all_strategy_count is not None:
            result['AllStrategyCount'] = self.all_strategy_count

        if self.anti_brute_force_rule_count is not None:
            result['AntiBruteForceRuleCount'] = self.anti_brute_force_rule_count

        if self.custom_effective_count is not None:
            result['CustomEffectiveCount'] = self.custom_effective_count

        if self.custom_record_count is not None:
            result['CustomRecordCount'] = self.custom_record_count

        if self.effective_count is not None:
            result['EffectiveCount'] = self.effective_count

        if self.system_effective_count is not None:
            result['SystemEffectiveCount'] = self.system_effective_count

        if self.system_record_count is not None:
            result['SystemRecordCount'] = self.system_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllStrategyCount') is not None:
            self.all_strategy_count = m.get('AllStrategyCount')

        if m.get('AntiBruteForceRuleCount') is not None:
            self.anti_brute_force_rule_count = m.get('AntiBruteForceRuleCount')

        if m.get('CustomEffectiveCount') is not None:
            self.custom_effective_count = m.get('CustomEffectiveCount')

        if m.get('CustomRecordCount') is not None:
            self.custom_record_count = m.get('CustomRecordCount')

        if m.get('EffectiveCount') is not None:
            self.effective_count = m.get('EffectiveCount')

        if m.get('SystemEffectiveCount') is not None:
            self.system_effective_count = m.get('SystemEffectiveCount')

        if m.get('SystemRecordCount') is not None:
            self.system_record_count = m.get('SystemRecordCount')

        return self

