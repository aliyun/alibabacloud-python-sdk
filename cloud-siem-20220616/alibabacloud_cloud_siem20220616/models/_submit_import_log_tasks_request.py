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
        # The list of accounts for log ingestion. The value must be a JSON array. Valid values:
        # 
        # - AccountId: The ID of the account.
        # 
        # - Imported: Specifies whether to enable or disable log ingestion for the account. Valid values:
        # 
        #   - 0: Disable ingestion.
        # 
        #   - 1: Enable ingestion.
        self.accounts = accounts
        # Specifies whether to automatically enable log ingestion for accounts that are configured with the specified log. Valid values:
        # 
        # - 1: Yes.
        # 
        # - 0: No.
        self.auto_imported = auto_imported
        # The code of the cloud service provider.
        # 
        # This parameter is required.
        self.cloud_code = cloud_code
        # The list of logs to be ingested. The value must be a JSON array.
        self.log_codes = log_codes
        # The code of the product.
        # 
        # This parameter is required.
        self.prod_code = prod_code
        # The region where the data management center for Threat Analysis is located. Select a region based on the location of your assets. Valid values:
        # 
        # - cn-hangzhou: Your assets are in the Chinese mainland or Hong Kong (China).
        # 
        # - ap-southeast-1: Your assets are outside China.
        self.region_id = region_id
        # The user ID of the member that the administrator wants to access.
        self.role_for = role_for
        # The type of view. Valid values:
        # 
        # - 0: The view of the current Alibaba Cloud account.
        # 
        # - 1: The view of all accounts within the enterprise.
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

