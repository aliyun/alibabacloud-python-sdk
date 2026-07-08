# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_tag20180828 import models as main_models
from darabonba.model import DaraModel

class CreateAssociatedResourceRulesRequest(DaraModel):
    def __init__(
        self,
        create_rules_list: List[main_models.CreateAssociatedResourceRulesRequestCreateRulesList] = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
    ):
        # A list of associated resource tag rules.
        self.create_rules_list = create_rules_list
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account

    def validate(self):
        if self.create_rules_list:
            for v1 in self.create_rules_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CreateRulesList'] = []
        if self.create_rules_list is not None:
            for k1 in self.create_rules_list:
                result['CreateRulesList'].append(k1.to_map() if k1 else None)

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.create_rules_list = []
        if m.get('CreateRulesList') is not None:
            for k1 in m.get('CreateRulesList'):
                temp_model = main_models.CreateAssociatedResourceRulesRequestCreateRulesList()
                self.create_rules_list.append(temp_model.from_map(k1))

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        return self



class CreateAssociatedResourceRulesRequestCreateRulesList(DaraModel):
    def __init__(
        self,
        existing_status: str = None,
        setting_name: str = None,
        status: str = None,
        tag_keys: List[str] = None,
    ):
        self.existing_status = existing_status
        # The setting name of the associated resource tag rule.
        # 
        # For valid values, see the **Setting name** column in [Resources that support associated resource tagging](https://help.aliyun.com/document_detail/2586330.html).
        # 
        # This parameter is required.
        self.setting_name = setting_name
        # Specifies whether to enable the associated resource tag rule. Valid values:
        # 
        # - Enable (default): The rule is enabled.
        # 
        # - Disable: The rule is disabled.
        # 
        # This parameter is required.
        self.status = status
        # The tag keys to which the rule applies.
        self.tag_keys = tag_keys

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.existing_status is not None:
            result['ExistingStatus'] = self.existing_status

        if self.setting_name is not None:
            result['SettingName'] = self.setting_name

        if self.status is not None:
            result['Status'] = self.status

        if self.tag_keys is not None:
            result['TagKeys'] = self.tag_keys

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExistingStatus') is not None:
            self.existing_status = m.get('ExistingStatus')

        if m.get('SettingName') is not None:
            self.setting_name = m.get('SettingName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TagKeys') is not None:
            self.tag_keys = m.get('TagKeys')

        return self

