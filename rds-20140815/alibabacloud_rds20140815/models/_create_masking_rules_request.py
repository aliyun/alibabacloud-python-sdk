# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class CreateMaskingRulesRequest(DaraModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        dbname: str = None,
        default_algo: str = None,
        masking_algo: str = None,
        owner_id: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        rule_config: main_models.CreateMaskingRulesRequestRuleConfig = None,
        rule_name: str = None,
    ):
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        self.dbname = dbname
        self.default_algo = default_algo
        self.masking_algo = masking_algo
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.rule_config = rule_config
        # This parameter is required.
        self.rule_name = rule_name

    def validate(self):
        if self.rule_config:
            self.rule_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.dbname is not None:
            result['DBName'] = self.dbname

        if self.default_algo is not None:
            result['DefaultAlgo'] = self.default_algo

        if self.masking_algo is not None:
            result['MaskingAlgo'] = self.masking_algo

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.rule_config is not None:
            result['RuleConfig'] = self.rule_config.to_map()

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        if m.get('DefaultAlgo') is not None:
            self.default_algo = m.get('DefaultAlgo')

        if m.get('MaskingAlgo') is not None:
            self.masking_algo = m.get('MaskingAlgo')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RuleConfig') is not None:
            temp_model = main_models.CreateMaskingRulesRequestRuleConfig()
            self.rule_config = temp_model.from_map(m.get('RuleConfig'))

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        return self

class CreateMaskingRulesRequestRuleConfig(DaraModel):
    def __init__(
        self,
        columns: List[str] = None,
        databases: List[str] = None,
        tables: List[str] = None,
    ):
        self.columns = columns
        self.databases = databases
        self.tables = tables

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.columns is not None:
            result['Columns'] = self.columns

        if self.databases is not None:
            result['Databases'] = self.databases

        if self.tables is not None:
            result['Tables'] = self.tables

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Columns') is not None:
            self.columns = m.get('Columns')

        if m.get('Databases') is not None:
            self.databases = m.get('Databases')

        if m.get('Tables') is not None:
            self.tables = m.get('Tables')

        return self

