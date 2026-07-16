# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSqlAuditInfoRequest(DaraModel):
    def __init__(
        self,
        audit_account_name: str = None,
        audit_account_password: str = None,
        dbinstance_id: str = None,
        region_id: str = None,
    ):
        # The name of the audit administrator account. > This parameter is required if the three-role mode is enabled. For more information, see [Three-role mode](https://help.aliyun.com/document_detail/213824.html).
        self.audit_account_name = audit_account_name
        # The password of the audit administrator account. > This parameter is required if the three-role mode is enabled. For more information about the three-role mode, see [Three-role mode](https://help.aliyun.com/document_detail/213824.html).
        self.audit_account_password = audit_account_password
        # The instance ID. > You can call [DescribeDBInstances](https://help.aliyun.com/document_detail/196830.html) to query the details of all instances in the specified region, including instance IDs.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The ID of the region where the instance resides. > You can call [DescribeRegions](https://help.aliyun.com/document_detail/196841.html) to query the regions supported by PolarDB-X, including region IDs.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit_account_name is not None:
            result['AuditAccountName'] = self.audit_account_name

        if self.audit_account_password is not None:
            result['AuditAccountPassword'] = self.audit_account_password

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditAccountName') is not None:
            self.audit_account_name = m.get('AuditAccountName')

        if m.get('AuditAccountPassword') is not None:
            self.audit_account_password = m.get('AuditAccountPassword')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

