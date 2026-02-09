# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SaveCostCenterShareRuleShrinkRequest(DaraModel):
    def __init__(
        self,
        create_share_rule_list_shrink: str = None,
        modify_share_rule_list_shrink: str = None,
        nbid: str = None,
        owner_account_id: int = None,
        remove_share_rule_list_shrink: str = None,
    ):
        self.create_share_rule_list_shrink = create_share_rule_list_shrink
        self.modify_share_rule_list_shrink = modify_share_rule_list_shrink
        self.nbid = nbid
        self.owner_account_id = owner_account_id
        self.remove_share_rule_list_shrink = remove_share_rule_list_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_share_rule_list_shrink is not None:
            result['CreateShareRuleList'] = self.create_share_rule_list_shrink

        if self.modify_share_rule_list_shrink is not None:
            result['ModifyShareRuleList'] = self.modify_share_rule_list_shrink

        if self.nbid is not None:
            result['Nbid'] = self.nbid

        if self.owner_account_id is not None:
            result['OwnerAccountId'] = self.owner_account_id

        if self.remove_share_rule_list_shrink is not None:
            result['RemoveShareRuleList'] = self.remove_share_rule_list_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateShareRuleList') is not None:
            self.create_share_rule_list_shrink = m.get('CreateShareRuleList')

        if m.get('ModifyShareRuleList') is not None:
            self.modify_share_rule_list_shrink = m.get('ModifyShareRuleList')

        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')

        if m.get('OwnerAccountId') is not None:
            self.owner_account_id = m.get('OwnerAccountId')

        if m.get('RemoveShareRuleList') is not None:
            self.remove_share_rule_list_shrink = m.get('RemoveShareRuleList')

        return self

