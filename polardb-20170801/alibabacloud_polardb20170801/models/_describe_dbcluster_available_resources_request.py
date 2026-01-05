# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDBClusterAvailableResourcesRequest(DaraModel):
    def __init__(
        self,
        dbnode_class: str = None,
        dbtype: str = None,
        dbversion: str = None,
        owner_account: str = None,
        owner_id: int = None,
        pay_type: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        zone_id: str = None,
    ):
        # The specifications of the node. For more information, see [Specifications of compute nodes](https://help.aliyun.com/document_detail/102542.html).
        self.dbnode_class = dbnode_class
        # The type of the database engine. Valid values:
        # 
        # *   **MySQL**
        # *   **PostgreSQL**
        # *   **Oracle**
        self.dbtype = dbtype
        # The version of the database engine. Valid values for the MySQL database engine:
        # 
        # *   **5.6**
        # *   **5.7**
        # *   **8.0**
        # 
        # Valid values for the PostgreSQL database engine:
        # 
        # *   **11**
        # *   **14**
        # 
        # Valid value for the Oracle database engine: **11**
        # 
        # > This parameter is required when you specify the **DBType** parameter.
        self.dbversion = dbversion
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The billing method of the cluster. Valid values:
        # 
        # *   **Postpaid**: pay-as-you-go
        # *   **Prepaid**: subscription
        # 
        # This parameter is required.
        self.pay_type = pay_type
        # The region ID of the cluster. Default value: **cn-hangzhou**.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/98041.html) operation to query the available regions.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The zone ID of the cluster.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/98041.html) operation to query the available zones.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbnode_class is not None:
            result['DBNodeClass'] = self.dbnode_class

        if self.dbtype is not None:
            result['DBType'] = self.dbtype

        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBNodeClass') is not None:
            self.dbnode_class = m.get('DBNodeClass')

        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')

        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

