# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAIServiceRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        description: str = None,
        security_iplist: str = None,
        service_account: str = None,
        service_account_password: str = None,
        type: str = None,
    ):
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the details of all AnalyticDB for PostgreSQL instances in a region, including instance IDs.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The description.
        self.description = description
        # The list of IP addresses in IP address whitelist group. You can specify up to 1,000 IP addresses, separated by commas (,). The value 127.0.0.1 indicates that no external IP addresses are allowed to access the instance. The following formats are supported:
        # - 10.23.12.24 (IP address)
        # - 10.23.12.24/24 (CIDR block. The value /24 indicates the length of the prefix in the address, which ranges from 1 to 32.)
        # 
        # > After the service is created, you can call the ModifyAIServiceSecurityIps operation to modify IP address whitelist.
        self.security_iplist = security_iplist
        # The service account. The following limits apply:
        # - The account name can contain lowercase letters, digits, and underscores (_).
        # - The account name must start with a lowercase letter and end with a lowercase letter or digit.
        # - The account name cannot start with gp.
        # - The account name must be 2 to 16 characters in length.
        # 
        # This parameter is required.
        self.service_account = service_account
        # The password of the service account. The following limits apply:
        # - The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.
        # - Supported special characters: !@#$%^&*()_+-=
        # - The password must be 8 to 32 characters in length.
        # 
        # This parameter is required.
        self.service_account_password = service_account_password
        # The service type. Currently, only drama is supported.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.description is not None:
            result['Description'] = self.description

        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist

        if self.service_account is not None:
            result['ServiceAccount'] = self.service_account

        if self.service_account_password is not None:
            result['ServiceAccountPassword'] = self.service_account_password

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')

        if m.get('ServiceAccount') is not None:
            self.service_account = m.get('ServiceAccount')

        if m.get('ServiceAccountPassword') is not None:
            self.service_account_password = m.get('ServiceAccountPassword')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

