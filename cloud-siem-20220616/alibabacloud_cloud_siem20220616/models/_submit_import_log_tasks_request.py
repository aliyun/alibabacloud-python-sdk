# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitImportLogTasksRequest(DaraModel):
    def __init__(
        self,
        accounts: str = None,
        auto_imported: int = None,
        cloud_code: str = None,
        log_codes: str = None,
        prod_code: str = None,
        region_id: str = None,
        role_for: int = None,
        role_type: int = None,
    ):
        # The list of accounts to be onboarded, in JSON array format. Valid values:
        # - AccountId: the ID of the account to be onboarded.
        # - Imported: specifies whether to onboard or disconnect the account. Valid values:
        #   - 0: Disconnect the account.
        #   - 1: Onboard the account.
        self.accounts = accounts
        # Specifies whether to automatically onboard accounts that are configured with the log. Valid values:
        # - 1: Automatically onboard. 
        # - 0: Do not automatically onboard.
        self.auto_imported = auto_imported
        # The multi-cloud code.
        # 
        # This parameter is required.
        self.cloud_code = cloud_code
        # The list of logs to be onboarded, in JSON array format.
        self.log_codes = log_codes
        # The product code.
        # 
        # This parameter is required.
        self.prod_code = prod_code
        # The region of the data management center for Threat Analysis. You must select the region of the management center based on the region where your assets are located. Valid values:
        # - cn-hangzhou: Assets are located in the Chinese mainland and Hong Kong (China).
        # - ap-southeast-1: Assets are located outside the Chinese mainland.
        self.region_id = region_id
        # The ID of the user whose perspective the administrator switches to.
        self.role_for = role_for
        # The view type. Valid values:
        # 
        # - 0: Current Alibaba Cloud account view.
        # - 1: View of all accounts in the enterprise.
        self.role_type = role_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accounts is not None:
            result['Accounts'] = self.accounts

        if self.auto_imported is not None:
            result['AutoImported'] = self.auto_imported

        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code

        if self.log_codes is not None:
            result['LogCodes'] = self.log_codes

        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        if self.role_type is not None:
            result['RoleType'] = self.role_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accounts') is not None:
            self.accounts = m.get('Accounts')

        if m.get('AutoImported') is not None:
            self.auto_imported = m.get('AutoImported')

        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')

        if m.get('LogCodes') is not None:
            self.log_codes = m.get('LogCodes')

        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        return self

