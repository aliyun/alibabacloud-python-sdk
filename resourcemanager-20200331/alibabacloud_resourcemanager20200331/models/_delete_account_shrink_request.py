# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAccountShrinkRequest(DaraModel):
    def __init__(
        self,
        abandonable_check_id_shrink: str = None,
        account_id: str = None,
    ):
        # The ID of the check item that you can choose to abandon and continue with the member deletion.
        # 
        # You can obtain this ID from the AbandonableChecks response parameter of [GetAccountDeletionCheckResult](https://help.aliyun.com/document_detail/448775.html).
        self.abandonable_check_id_shrink = abandonable_check_id_shrink
        # The ID of the member to delete.
        # 
        # This parameter is required.
        self.account_id = account_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.abandonable_check_id_shrink is not None:
            result['AbandonableCheckId'] = self.abandonable_check_id_shrink

        if self.account_id is not None:
            result['AccountId'] = self.account_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbandonableCheckId') is not None:
            self.abandonable_check_id_shrink = m.get('AbandonableCheckId')

        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        return self

