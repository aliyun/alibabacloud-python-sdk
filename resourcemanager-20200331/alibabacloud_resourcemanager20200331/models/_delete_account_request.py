# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteAccountRequest(DaraModel):
    def __init__(
        self,
        abandonable_check_id: List[str] = None,
        account_id: str = None,
    ):
        # The ID of a check item that you can choose to ignore for the member deletion.
        # 
        # You can obtain the ID from the response of the [GetAccountDeletionCheckResult](https://help.aliyun.com/document_detail/448775.html) operation.
        self.abandonable_check_id = abandonable_check_id
        # The Alibaba Cloud account ID of the member that you want to delete.
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
        if self.abandonable_check_id is not None:
            result['AbandonableCheckId'] = self.abandonable_check_id

        if self.account_id is not None:
            result['AccountId'] = self.account_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbandonableCheckId') is not None:
            self.abandonable_check_id = m.get('AbandonableCheckId')

        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        return self

