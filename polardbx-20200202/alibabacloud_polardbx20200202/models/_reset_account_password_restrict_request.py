# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResetAccountPasswordRestrictRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        account_password: str = None,
        dbinstance_name: str = None,
        region_id: str = None,
        security_account_name: str = None,
        security_account_password: str = None,
    ):
        # The name of the account whose password you want to reset. > Only passwords of standard accounts can be reset.
        # 
        # This parameter is required.
        self.account_name = account_name
        # The account information for which you want to reset the password. Separate multiple account entries with commas (,).
        # 
        # This parameter is required.
        self.account_password = account_password
        # The instance ID. > You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/196830.html) operation to query the details of all instances in the specified region, including instance IDs.
        # 
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        # The region ID. > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/98041.html) operation to query available regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The name of the account whose password you want to reset. > *Only passwords of standard accounts can be reset.* You can invoke the [DescribeAccountList](https://help.aliyun.com/document_detail/196844.html) operation to query the account information of the target instance, including account names.
        self.security_account_name = security_account_name
        # The password of the security administrator account. > If three-role mode is enabled, this parameter is required. For more information about three-role mode, see [Three-role mode](https://help.aliyun.com/document_detail/213824.html).
        self.security_account_password = security_account_password

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.account_password is not None:
            result['AccountPassword'] = self.account_password

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.security_account_name is not None:
            result['SecurityAccountName'] = self.security_account_name

        if self.security_account_password is not None:
            result['SecurityAccountPassword'] = self.security_account_password

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecurityAccountName') is not None:
            self.security_account_name = m.get('SecurityAccountName')

        if m.get('SecurityAccountPassword') is not None:
            self.security_account_password = m.get('SecurityAccountPassword')

        return self

