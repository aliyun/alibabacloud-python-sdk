# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateBudgetShrinkRequest(DaraModel):
    def __init__(
        self,
        budget_name: str = None,
        budget_type: str = None,
        comment: str = None,
        cycle_end_period: str = None,
        cycle_quota_shrink: str = None,
        cycle_start_period: str = None,
        cycle_type: str = None,
        ec_id_account_ids_shrink: str = None,
        metric: str = None,
        nbid: str = None,
        query_filter_shrink: str = None,
        quota: str = None,
        quota_type: str = None,
        warn_confs_shrink: str = None,
    ):
        # This parameter is required.
        self.budget_name = budget_name
        # This parameter is required.
        self.budget_type = budget_type
        self.comment = comment
        # This parameter is required.
        self.cycle_end_period = cycle_end_period
        self.cycle_quota_shrink = cycle_quota_shrink
        # This parameter is required.
        self.cycle_start_period = cycle_start_period
        # This parameter is required.
        self.cycle_type = cycle_type
        self.ec_id_account_ids_shrink = ec_id_account_ids_shrink
        # This parameter is required.
        self.metric = metric
        self.nbid = nbid
        self.query_filter_shrink = query_filter_shrink
        self.quota = quota
        # This parameter is required.
        self.quota_type = quota_type
        self.warn_confs_shrink = warn_confs_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.budget_name is not None:
            result['BudgetName'] = self.budget_name

        if self.budget_type is not None:
            result['BudgetType'] = self.budget_type

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.cycle_end_period is not None:
            result['CycleEndPeriod'] = self.cycle_end_period

        if self.cycle_quota_shrink is not None:
            result['CycleQuota'] = self.cycle_quota_shrink

        if self.cycle_start_period is not None:
            result['CycleStartPeriod'] = self.cycle_start_period

        if self.cycle_type is not None:
            result['CycleType'] = self.cycle_type

        if self.ec_id_account_ids_shrink is not None:
            result['EcIdAccountIds'] = self.ec_id_account_ids_shrink

        if self.metric is not None:
            result['Metric'] = self.metric

        if self.nbid is not None:
            result['Nbid'] = self.nbid

        if self.query_filter_shrink is not None:
            result['QueryFilter'] = self.query_filter_shrink

        if self.quota is not None:
            result['Quota'] = self.quota

        if self.quota_type is not None:
            result['QuotaType'] = self.quota_type

        if self.warn_confs_shrink is not None:
            result['WarnConfs'] = self.warn_confs_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BudgetName') is not None:
            self.budget_name = m.get('BudgetName')

        if m.get('BudgetType') is not None:
            self.budget_type = m.get('BudgetType')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('CycleEndPeriod') is not None:
            self.cycle_end_period = m.get('CycleEndPeriod')

        if m.get('CycleQuota') is not None:
            self.cycle_quota_shrink = m.get('CycleQuota')

        if m.get('CycleStartPeriod') is not None:
            self.cycle_start_period = m.get('CycleStartPeriod')

        if m.get('CycleType') is not None:
            self.cycle_type = m.get('CycleType')

        if m.get('EcIdAccountIds') is not None:
            self.ec_id_account_ids_shrink = m.get('EcIdAccountIds')

        if m.get('Metric') is not None:
            self.metric = m.get('Metric')

        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')

        if m.get('QueryFilter') is not None:
            self.query_filter_shrink = m.get('QueryFilter')

        if m.get('Quota') is not None:
            self.quota = m.get('Quota')

        if m.get('QuotaType') is not None:
            self.quota_type = m.get('QuotaType')

        if m.get('WarnConfs') is not None:
            self.warn_confs_shrink = m.get('WarnConfs')

        return self

