# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyADInfoRequest(DaraModel):
    def __init__(
        self,
        adaccount_name: str = None,
        addns: str = None,
        adpassword: str = None,
        adserver_ip_address: str = None,
        client_token: str = None,
        dbinstance_id: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The account of the AD domain.
        self.adaccount_name = adaccount_name
        # The DNS information about the AD domain.
        self.addns = addns
        # The password for the account of the AD domain.
        self.adpassword = adpassword
        # The IP address of the AD domain.
        self.adserver_ip_address = adserver_ip_address
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The instance ID. You can call the DescribeDBInstances operation to query the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        self.owner_id = owner_id
        # The region ID. You can call the DescribeRegions operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adaccount_name is not None:
            result['ADAccountName'] = self.adaccount_name

        if self.addns is not None:
            result['ADDNS'] = self.addns

        if self.adpassword is not None:
            result['ADPassword'] = self.adpassword

        if self.adserver_ip_address is not None:
            result['ADServerIpAddress'] = self.adserver_ip_address

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ADAccountName') is not None:
            self.adaccount_name = m.get('ADAccountName')

        if m.get('ADDNS') is not None:
            self.addns = m.get('ADDNS')

        if m.get('ADPassword') is not None:
            self.adpassword = m.get('ADPassword')

        if m.get('ADServerIpAddress') is not None:
            self.adserver_ip_address = m.get('ADServerIpAddress')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

