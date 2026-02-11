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
        # The accounts that you want to add. The value is a JSON array. Valid values:
        # 
        # *   AccountId: the IDs of the accounts.
        # 
        # *   Imported: specifies whether to add the accounts. Valid values:
        # 
        #     *   0: no
        #     *   1: yes
        self.accounts = accounts
        # Specifies whether to automatically add the account for which the logging feature is configured. Valid values:
        # 
        # *   1: yes
        # *   0: no
        self.auto_imported = auto_imported
        # The code that is used for multi-cloud environments. Valid values:
        # 
        # *   qcloud: Tencent Cloud
        # *   aliyun: Alibaba Cloud
        # *   hcloud: Huawei Cloud
        # 
        # This parameter is required.
        self.cloud_code = cloud_code
        # The logs that you want to collect. The value is a JSON array.
        self.log_codes = log_codes
        # The code of the service.
        # 
        # This parameter is required.
        self.prod_code = prod_code
        # The data management center of the threat analysis feature. Specify this parameter based on the region where your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions inside China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id
        # The ID of the account that you switch from the management account.
        self.role_for = role_for
        # The type of the view. Valid values:
        # - 0: the current Alibaba Cloud account
        # - 1: the global account
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

