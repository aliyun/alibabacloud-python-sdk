# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeUserSpnSummaryInfoShrinkRequest(DaraModel):
    def __init__(
        self,
        ec_id_account_ids_shrink: str = None,
        nbid: str = None,
    ):
        self.ec_id_account_ids_shrink = ec_id_account_ids_shrink
        self.nbid = nbid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ec_id_account_ids_shrink is not None:
            result['EcIdAccountIds'] = self.ec_id_account_ids_shrink

        if self.nbid is not None:
            result['Nbid'] = self.nbid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EcIdAccountIds') is not None:
            self.ec_id_account_ids_shrink = m.get('EcIdAccountIds')

        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')

        return self

