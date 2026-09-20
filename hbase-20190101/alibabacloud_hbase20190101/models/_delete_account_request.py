# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAccountRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        cluster_id: str = None,
    ):
        # The name of the existing account to be deleted.
        # 
        # This parameter is required.
        self.account_name = account_name
        # Instance ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        return self

