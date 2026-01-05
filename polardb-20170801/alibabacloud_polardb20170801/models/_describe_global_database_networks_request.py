# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeGlobalDatabaseNetworksRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        filter_region: str = None,
        gdndescription: str = None,
        gdnid: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        # The ID of the cluster.
        # 
        # > You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/98094.html) operation to query information about all clusters that are deployed in a specified region, such as the cluster ID.
        self.dbcluster_id = dbcluster_id
        # Specify the region in which you want to query GDNs. You can create secondary clusters for the GDNs.
        self.filter_region = filter_region
        # The description of the GDN. The description must meet the following requirements:
        # 
        # *   It cannot start with `http://` or `https://`.
        # *   It must start with a letter.
        # *   It can contain letters, digits, underscores (_), and hyphens (-).
        # *   It must be 2 to 126 characters in length.
        self.gdndescription = gdndescription
        # The ID of the GDN.
        self.gdnid = gdnid
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The number of the page to return. Default value: 1. The value must be an integer that is greater than 0.
        self.page_number = page_number
        # The number of entries per page. Default value: 30. Valid values:
        # 
        # *   30
        # *   50
        # *   100
        self.page_size = page_size
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.filter_region is not None:
            result['FilterRegion'] = self.filter_region

        if self.gdndescription is not None:
            result['GDNDescription'] = self.gdndescription

        if self.gdnid is not None:
            result['GDNId'] = self.gdnid

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('FilterRegion') is not None:
            self.filter_region = m.get('FilterRegion')

        if m.get('GDNDescription') is not None:
            self.gdndescription = m.get('GDNDescription')

        if m.get('GDNId') is not None:
            self.gdnid = m.get('GDNId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

