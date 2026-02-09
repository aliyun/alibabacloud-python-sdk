# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSavingPlanUserDeductRuleShrinkRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        ec_id_account_ids_shrink: str = None,
        nbid: str = None,
        page_size: int = None,
        spn_instance_code: str = None,
    ):
        self.current_page = current_page
        self.ec_id_account_ids_shrink = ec_id_account_ids_shrink
        self.nbid = nbid
        self.page_size = page_size
        self.spn_instance_code = spn_instance_code

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

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.spn_instance_code is not None:
            result['SpnInstanceCode'] = self.spn_instance_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EcIdAccountIds') is not None:
            self.ec_id_account_ids_shrink = m.get('EcIdAccountIds')

        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SpnInstanceCode') is not None:
            self.spn_instance_code = m.get('SpnInstanceCode')

        return self

