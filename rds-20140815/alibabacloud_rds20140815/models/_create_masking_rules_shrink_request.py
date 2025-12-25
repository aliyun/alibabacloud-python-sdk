# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateMaskingRulesShrinkRequest(DaraModel):
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
        rule_config_shrink: str = None,
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
        self.rule_config_shrink = rule_config_shrink
        # This parameter is required.
        self.rule_name = rule_name

    def validate(self):
        pass

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

        if self.rule_config_shrink is not None:
            result['RuleConfig'] = self.rule_config_shrink

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
            self.rule_config_shrink = m.get('RuleConfig')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        return self

