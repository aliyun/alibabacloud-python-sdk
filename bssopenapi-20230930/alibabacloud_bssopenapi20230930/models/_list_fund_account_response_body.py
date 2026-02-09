# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_bssopenapi20230930 import models as main_models
from darabonba.model import DaraModel

class ListFundAccountResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListFundAccountResponseBodyData] = None,
        metadata: Any = None,
        request_id: str = None,
    ):
        self.data = data
        self.metadata = metadata
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListFundAccountResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListFundAccountResponseBodyData(DaraModel):
    def __init__(
        self,
        create_date: str = None,
        fund_account_admin_account_id: str = None,
        fund_account_admin_account_name: str = None,
        fund_account_id: str = None,
        fund_account_name: str = None,
        fund_account_owner_account_id: str = None,
        fund_account_status: str = None,
        fund_account_type: str = None,
        nbid: str = None,
        permissions: List[str] = None,
        site: str = None,
    ):
        self.create_date = create_date
        self.fund_account_admin_account_id = fund_account_admin_account_id
        self.fund_account_admin_account_name = fund_account_admin_account_name
        self.fund_account_id = fund_account_id
        self.fund_account_name = fund_account_name
        self.fund_account_owner_account_id = fund_account_owner_account_id
        self.fund_account_status = fund_account_status
        self.fund_account_type = fund_account_type
        self.nbid = nbid
        self.permissions = permissions
        self.site = site

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_date is not None:
            result['CreateDate'] = self.create_date

        if self.fund_account_admin_account_id is not None:
            result['FundAccountAdminAccountId'] = self.fund_account_admin_account_id

        if self.fund_account_admin_account_name is not None:
            result['FundAccountAdminAccountName'] = self.fund_account_admin_account_name

        if self.fund_account_id is not None:
            result['FundAccountId'] = self.fund_account_id

        if self.fund_account_name is not None:
            result['FundAccountName'] = self.fund_account_name

        if self.fund_account_owner_account_id is not None:
            result['FundAccountOwnerAccountId'] = self.fund_account_owner_account_id

        if self.fund_account_status is not None:
            result['FundAccountStatus'] = self.fund_account_status

        if self.fund_account_type is not None:
            result['FundAccountType'] = self.fund_account_type

        if self.nbid is not None:
            result['Nbid'] = self.nbid

        if self.permissions is not None:
            result['Permissions'] = self.permissions

        if self.site is not None:
            result['Site'] = self.site

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

        if m.get('FundAccountAdminAccountId') is not None:
            self.fund_account_admin_account_id = m.get('FundAccountAdminAccountId')

        if m.get('FundAccountAdminAccountName') is not None:
            self.fund_account_admin_account_name = m.get('FundAccountAdminAccountName')

        if m.get('FundAccountId') is not None:
            self.fund_account_id = m.get('FundAccountId')

        if m.get('FundAccountName') is not None:
            self.fund_account_name = m.get('FundAccountName')

        if m.get('FundAccountOwnerAccountId') is not None:
            self.fund_account_owner_account_id = m.get('FundAccountOwnerAccountId')

        if m.get('FundAccountStatus') is not None:
            self.fund_account_status = m.get('FundAccountStatus')

        if m.get('FundAccountType') is not None:
            self.fund_account_type = m.get('FundAccountType')

        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')

        if m.get('Permissions') is not None:
            self.permissions = m.get('Permissions')

        if m.get('Site') is not None:
            self.site = m.get('Site')

        return self

