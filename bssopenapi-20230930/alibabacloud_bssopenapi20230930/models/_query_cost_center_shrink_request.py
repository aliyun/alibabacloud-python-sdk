# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryCostCenterShrinkRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        ec_id_account_ids_shrink: str = None,
        nbid: str = None,
        owner_account_id: int = None,
        page_size: int = None,
        parent_cost_center_id: int = None,
    ):
        # This parameter is required.
        self.current_page = current_page
        self.ec_id_account_ids_shrink = ec_id_account_ids_shrink
        self.nbid = nbid
        # This parameter is required.
        self.owner_account_id = owner_account_id
        # This parameter is required.
        self.page_size = page_size
        # This parameter is required.
        self.parent_cost_center_id = parent_cost_center_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.ec_id_account_ids_shrink is not None:
            result['EcIdAccountIds'] = self.ec_id_account_ids_shrink

        if self.nbid is not None:
            result['Nbid'] = self.nbid

        if self.owner_account_id is not None:
            result['OwnerAccountId'] = self.owner_account_id

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.parent_cost_center_id is not None:
            result['ParentCostCenterId'] = self.parent_cost_center_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EcIdAccountIds') is not None:
            self.ec_id_account_ids_shrink = m.get('EcIdAccountIds')

        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')

        if m.get('OwnerAccountId') is not None:
            self.owner_account_id = m.get('OwnerAccountId')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ParentCostCenterId') is not None:
            self.parent_cost_center_id = m.get('ParentCostCenterId')

        return self

