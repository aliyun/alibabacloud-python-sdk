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
        # > Call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to list all AnalyticDB for PostgreSQL instances in the destination region, including their instance IDs.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # A description of the service.
        self.description = description
        # A comma-separated list of IP addresses or CIDR blocks in the IP address whitelist. You can specify up to 1000 entries. To block all external IP access, use 127.0.0.1. Valid formats include the following:
        # 
        # - 10.23.12.24 (an IPv4 address)
        # 
        # - 10.23.12.24/24 (a CIDR block, where /24 indicates the prefix length, from 1 to 32)
        # 
        # > After you create the service, call the ModifyAIServiceSecurityIps operation to update the IP address whitelist.
        self.security_iplist = security_iplist
        # The service account. It must meet these requirements:
        # 
        # - Contain only lowercase letters, digits, and underscores.
        # 
        # - Start with a lowercase letter and end with a lowercase letter or digit.
        # 
        # - Not start with gp.
        # 
        # - Be 2 to 16 characters long.
        # 
        # This parameter is required.
        self.service_account = service_account
        # The password for the service account. It must meet these requirements:
        # 
        # - Contain at least three of the following: uppercase letters, lowercase letters, digits, and special characters.
        # 
        # - Support these special characters: !@#$%^&\\*()_+-=.
        # 
        # - Be 8 to 32 characters long.
        # 
        # This parameter is required.
        self.service_account_password = service_account_password
        # The service type. Only drama is supported.
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

