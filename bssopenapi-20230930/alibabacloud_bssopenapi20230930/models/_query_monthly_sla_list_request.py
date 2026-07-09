# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20230930 import models as main_models
from darabonba.model import DaraModel

class QueryMonthlySlaListRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        ec_id_account_ids: List[main_models.QueryMonthlySlaListRequestEcIdAccountIds] = None,
        instance_ids: List[str] = None,
        months: List[int] = None,
        nbid: str = None,
        page_size: int = None,
        pay_statuses: List[int] = None,
        product_codes: List[str] = None,
    ):
        # The current page number. Default value: 1, which indicates the first page.
        self.current_page = current_page
        # The list of enterprise entities and accounts. If this parameter is left empty, the current account is queried.
        self.ec_id_account_ids = ec_id_account_ids
        # Optional. Filter by instance ID.
        self.instance_ids = instance_ids
        # Optional. Month list in yyyyMM format.
        self.months = months
        # The level-1 marketplace ID. If this parameter is left empty, the marketplace ID of the current user is used by default.
        self.nbid = nbid
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # Optional. Filter by compensation status. Valid values: 0 and 1.
        self.pay_statuses = pay_statuses
        # Optional. Filter by product code.
        self.product_codes = product_codes

    def validate(self):
        if self.ec_id_account_ids:
            for v1 in self.ec_id_account_ids:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['EcIdAccountIds'] = []
        if self.ec_id_account_ids is not None:
            for k1 in self.ec_id_account_ids:
                result['EcIdAccountIds'].append(k1.to_map() if k1 else None)

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.months is not None:
            result['Months'] = self.months

        if self.nbid is not None:
            result['Nbid'] = self.nbid

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.pay_statuses is not None:
            result['PayStatuses'] = self.pay_statuses

        if self.product_codes is not None:
            result['ProductCodes'] = self.product_codes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.ec_id_account_ids = []
        if m.get('EcIdAccountIds') is not None:
            for k1 in m.get('EcIdAccountIds'):
                temp_model = main_models.QueryMonthlySlaListRequestEcIdAccountIds()
                self.ec_id_account_ids.append(temp_model.from_map(k1))

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('Months') is not None:
            self.months = m.get('Months')

        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PayStatuses') is not None:
            self.pay_statuses = m.get('PayStatuses')

        if m.get('ProductCodes') is not None:
            self.product_codes = m.get('ProductCodes')

        return self

class QueryMonthlySlaListRequestEcIdAccountIds(DaraModel):
    def __init__(
        self,
        account_ids: List[int] = None,
        ec_id: str = None,
    ):
        # The list of accounts to query. If this parameter is left empty, all accounts under the current entity ID are selected.
        self.account_ids = account_ids
        # The enterprise entity ID.
        self.ec_id = ec_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids

        if self.ec_id is not None:
            result['EcId'] = self.ec_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')

        if m.get('EcId') is not None:
            self.ec_id = m.get('EcId')

        return self

