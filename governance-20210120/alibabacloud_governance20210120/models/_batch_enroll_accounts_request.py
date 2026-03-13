# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_governance20210120 import models as main_models
from darabonba.model import DaraModel

class BatchEnrollAccountsRequest(DaraModel):
    def __init__(
        self,
        accounts: List[main_models.BatchEnrollAccountsRequestAccounts] = None,
        baseline_id: str = None,
        baseline_items: List[main_models.BatchEnrollAccountsRequestBaselineItems] = None,
        region_id: str = None,
    ):
        # The resource accounts.
        self.accounts = accounts
        # The baseline ID.
        # 
        # If this parameter is left empty, the default baseline is used.
        self.baseline_id = baseline_id
        # The baseline items.
        # 
        # If this parameter is specified, the configurations of the baseline items are merged with the baseline applied to the specified account. The configurations of the same baseline items are subject to the configurations of this parameter. We recommend that you leave this parameter empty and configure the `BaselineId` parameter to specify an account baseline and apply the configurations of the account baseline to the account.
        self.baseline_items = baseline_items
        # The region ID.
        self.region_id = region_id

    def validate(self):
        if self.accounts:
            for v1 in self.accounts:
                 if v1:
                    v1.validate()
        if self.baseline_items:
            for v1 in self.baseline_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Accounts'] = []
        if self.accounts is not None:
            for k1 in self.accounts:
                result['Accounts'].append(k1.to_map() if k1 else None)

        if self.baseline_id is not None:
            result['BaselineId'] = self.baseline_id

        result['BaselineItems'] = []
        if self.baseline_items is not None:
            for k1 in self.baseline_items:
                result['BaselineItems'].append(k1.to_map() if k1 else None)

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.accounts = []
        if m.get('Accounts') is not None:
            for k1 in m.get('Accounts'):
                temp_model = main_models.BatchEnrollAccountsRequestAccounts()
                self.accounts.append(temp_model.from_map(k1))

        if m.get('BaselineId') is not None:
            self.baseline_id = m.get('BaselineId')

        self.baseline_items = []
        if m.get('BaselineItems') is not None:
            for k1 in m.get('BaselineItems'):
                temp_model = main_models.BatchEnrollAccountsRequestBaselineItems()
                self.baseline_items.append(temp_model.from_map(k1))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class BatchEnrollAccountsRequestBaselineItems(DaraModel):
    def __init__(
        self,
        config: str = None,
        name: str = None,
        skip: bool = None,
        version: str = None,
    ):
        # The configurations of the baseline item.
        self.config = config
        # The name of the baseline item.
        self.name = name
        # Specifies whether to skip the baseline item. Valid values:
        # 
        # *   false
        # *   true
        self.skip = skip
        # The version of the baseline item.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.name is not None:
            result['Name'] = self.name

        if self.skip is not None:
            result['Skip'] = self.skip

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Skip') is not None:
            self.skip = m.get('Skip')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self



class BatchEnrollAccountsRequestAccounts(DaraModel):
    def __init__(
        self,
        account_uid: int = None,
    ):
        # The account ID. This parameter is required.
        self.account_uid = account_uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_uid is not None:
            result['AccountUid'] = self.account_uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountUid') is not None:
            self.account_uid = m.get('AccountUid')

        return self

