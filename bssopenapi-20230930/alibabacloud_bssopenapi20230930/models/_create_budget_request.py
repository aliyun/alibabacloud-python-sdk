# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20230930 import models as main_models
from darabonba.model import DaraModel

class CreateBudgetRequest(DaraModel):
    def __init__(
        self,
        budget_name: str = None,
        budget_type: str = None,
        comment: str = None,
        cycle_end_period: str = None,
        cycle_quota: List[main_models.CreateBudgetRequestCycleQuota] = None,
        cycle_start_period: str = None,
        cycle_type: str = None,
        ec_id_account_ids: List[main_models.CreateBudgetRequestEcIdAccountIds] = None,
        metric: str = None,
        nbid: str = None,
        query_filter: List[main_models.CreateBudgetRequestQueryFilter] = None,
        quota: str = None,
        quota_type: str = None,
        warn_confs: List[main_models.CreateBudgetRequestWarnConfs] = None,
    ):
        # The budget name.
        # 
        # This parameter is required.
        self.budget_name = budget_name
        # The budget type.
        # 
        # This parameter is required.
        self.budget_type = budget_type
        # The remarks.
        self.comment = comment
        # The end cycle.
        # 
        # This parameter is required.
        self.cycle_end_period = cycle_end_period
        # The per-cycle specified quota. This parameter is required when QuotaType is set to `SPECIFY`.
        self.cycle_quota = cycle_quota
        # The start cycle.
        # 
        # This parameter is required.
        self.cycle_start_period = cycle_start_period
        # The cycle type.
        # 
        # This parameter is required.
        self.cycle_type = cycle_type
        # The list of enterprises and accounts. An empty value indicates the current account.
        self.ec_id_account_ids = ec_id_account_ids
        # The budget metric.
        # 
        # This parameter is required.
        self.metric = metric
        # The level-1 marketplace ID. If empty, the marketplace ID of the current user is used by default.
        self.nbid = nbid
        # The filter conditions.
        self.query_filter = query_filter
        # The fixed quota value. If the type is quota, the unit is percentage.
        self.quota = quota
        # The quota type.
        # 
        # This parameter is required.
        self.quota_type = quota_type
        # The alert configurations.
        self.warn_confs = warn_confs

    def validate(self):
        if self.cycle_quota:
            for v1 in self.cycle_quota:
                 if v1:
                    v1.validate()
        if self.ec_id_account_ids:
            for v1 in self.ec_id_account_ids:
                 if v1:
                    v1.validate()
        if self.query_filter:
            for v1 in self.query_filter:
                 if v1:
                    v1.validate()
        if self.warn_confs:
            for v1 in self.warn_confs:
                 if v1:
                    v1.validate()

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

        result['CycleQuota'] = []
        if self.cycle_quota is not None:
            for k1 in self.cycle_quota:
                result['CycleQuota'].append(k1.to_map() if k1 else None)

        if self.cycle_start_period is not None:
            result['CycleStartPeriod'] = self.cycle_start_period

        if self.cycle_type is not None:
            result['CycleType'] = self.cycle_type

        result['EcIdAccountIds'] = []
        if self.ec_id_account_ids is not None:
            for k1 in self.ec_id_account_ids:
                result['EcIdAccountIds'].append(k1.to_map() if k1 else None)

        if self.metric is not None:
            result['Metric'] = self.metric

        if self.nbid is not None:
            result['Nbid'] = self.nbid

        result['QueryFilter'] = []
        if self.query_filter is not None:
            for k1 in self.query_filter:
                result['QueryFilter'].append(k1.to_map() if k1 else None)

        if self.quota is not None:
            result['Quota'] = self.quota

        if self.quota_type is not None:
            result['QuotaType'] = self.quota_type

        result['WarnConfs'] = []
        if self.warn_confs is not None:
            for k1 in self.warn_confs:
                result['WarnConfs'].append(k1.to_map() if k1 else None)

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

        self.cycle_quota = []
        if m.get('CycleQuota') is not None:
            for k1 in m.get('CycleQuota'):
                temp_model = main_models.CreateBudgetRequestCycleQuota()
                self.cycle_quota.append(temp_model.from_map(k1))

        if m.get('CycleStartPeriod') is not None:
            self.cycle_start_period = m.get('CycleStartPeriod')

        if m.get('CycleType') is not None:
            self.cycle_type = m.get('CycleType')

        self.ec_id_account_ids = []
        if m.get('EcIdAccountIds') is not None:
            for k1 in m.get('EcIdAccountIds'):
                temp_model = main_models.CreateBudgetRequestEcIdAccountIds()
                self.ec_id_account_ids.append(temp_model.from_map(k1))

        if m.get('Metric') is not None:
            self.metric = m.get('Metric')

        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')

        self.query_filter = []
        if m.get('QueryFilter') is not None:
            for k1 in m.get('QueryFilter'):
                temp_model = main_models.CreateBudgetRequestQueryFilter()
                self.query_filter.append(temp_model.from_map(k1))

        if m.get('Quota') is not None:
            self.quota = m.get('Quota')

        if m.get('QuotaType') is not None:
            self.quota_type = m.get('QuotaType')

        self.warn_confs = []
        if m.get('WarnConfs') is not None:
            for k1 in m.get('WarnConfs'):
                temp_model = main_models.CreateBudgetRequestWarnConfs()
                self.warn_confs.append(temp_model.from_map(k1))

        return self

class CreateBudgetRequestWarnConfs(DaraModel):
    def __init__(
        self,
        comment: str = None,
        event_bridge: bool = None,
        msc_channels: List[str] = None,
        msc_contacts: List[str] = None,
        name: str = None,
        threshold_type: str = None,
        threshold_value: str = None,
        warn_target: str = None,
    ):
        # The remarks.
        self.comment = comment
        # Specifies whether to enable EventBridge.
        self.event_bridge = event_bridge
        # The list of Message Center notification channels.
        self.msc_channels = msc_channels
        # The list of Message Center contacts.
        self.msc_contacts = msc_contacts
        # The alert name. This is a user-defined optional field. If not specified, the backend automatically generates a name.
        self.name = name
        # The threshold type.
        self.threshold_type = threshold_type
        # The threshold value.
        self.threshold_value = threshold_value
        # The alert target.
        self.warn_target = warn_target

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.event_bridge is not None:
            result['EventBridge'] = self.event_bridge

        if self.msc_channels is not None:
            result['MscChannels'] = self.msc_channels

        if self.msc_contacts is not None:
            result['MscContacts'] = self.msc_contacts

        if self.name is not None:
            result['Name'] = self.name

        if self.threshold_type is not None:
            result['ThresholdType'] = self.threshold_type

        if self.threshold_value is not None:
            result['ThresholdValue'] = self.threshold_value

        if self.warn_target is not None:
            result['WarnTarget'] = self.warn_target

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('EventBridge') is not None:
            self.event_bridge = m.get('EventBridge')

        if m.get('MscChannels') is not None:
            self.msc_channels = m.get('MscChannels')

        if m.get('MscContacts') is not None:
            self.msc_contacts = m.get('MscContacts')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ThresholdType') is not None:
            self.threshold_type = m.get('ThresholdType')

        if m.get('ThresholdValue') is not None:
            self.threshold_value = m.get('ThresholdValue')

        if m.get('WarnTarget') is not None:
            self.warn_target = m.get('WarnTarget')

        return self

class CreateBudgetRequestQueryFilter(DaraModel):
    def __init__(
        self,
        code: str = None,
        select_type: str = None,
        values: List[str] = None,
    ):
        # The parameter code.
        self.code = code
        # The selection mode.
        self.select_type = select_type
        # The list of filter values.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.select_type is not None:
            result['SelectType'] = self.select_type

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('SelectType') is not None:
            self.select_type = m.get('SelectType')

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

class CreateBudgetRequestEcIdAccountIds(DaraModel):
    def __init__(
        self,
        account_ids: List[int] = None,
        ec_id: str = None,
    ):
        # The list of accounts to access. An empty value indicates all accounts under the current entity ID.
        self.account_ids = account_ids
        # The enterprise entity ID.
        self.ec_id = ec_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids

        if self.ec_id is not None:
            result['EcId'] = self.ec_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')

        if m.get('EcId') is not None:
            self.ec_id = m.get('EcId')

        return self

class CreateBudgetRequestCycleQuota(DaraModel):
    def __init__(
        self,
        cycle_period: str = None,
        quota: str = None,
    ):
        # The cycle.
        self.cycle_period = cycle_period
        # The quota.
        self.quota = quota

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cycle_period is not None:
            result['CyclePeriod'] = self.cycle_period

        if self.quota is not None:
            result['Quota'] = self.quota

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CyclePeriod') is not None:
            self.cycle_period = m.get('CyclePeriod')

        if m.get('Quota') is not None:
            self.quota = m.get('Quota')

        return self

