# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeBudgetsRequest(DaraModel):
    def __init__(
        self,
        budget_name: str = None,
        budget_type: str = None,
        expire_status: str = None,
        nbid: str = None,
        page_no: int = None,
        page_size: int = None,
    ):
        self.budget_name = budget_name
        self.budget_type = budget_type
        self.expire_status = expire_status
        self.nbid = nbid
        self.page_no = page_no
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.budget_name is not None:
            result['BudgetName'] = self.budget_name

        if self.budget_type is not None:
            result['BudgetType'] = self.budget_type

        if self.expire_status is not None:
            result['ExpireStatus'] = self.expire_status

        if self.nbid is not None:
            result['Nbid'] = self.nbid

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BudgetName') is not None:
            self.budget_name = m.get('BudgetName')

        if m.get('BudgetType') is not None:
            self.budget_type = m.get('BudgetType')

        if m.get('ExpireStatus') is not None:
            self.expire_status = m.get('ExpireStatus')

        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

