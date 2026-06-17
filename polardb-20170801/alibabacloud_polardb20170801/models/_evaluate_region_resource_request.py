# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EvaluateRegionResourceRequest(DaraModel):
    def __init__(
        self,
        dbinstance_conn_type: str = None,
        dbnode_class: str = None,
        dbtype: str = None,
        dbversion: str = None,
        dispense_mode: str = None,
        need_max_scale_link: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sub_domain: str = None,
        zone_id: str = None,
    ):
        # The link type of the cluster. The backend randomly selects a default value. Valid values:
        # 
        # - **lvs**: Linux Virtual Server.
        # 
        # - **proxy**: proxy server.
        # 
        # - **dns**: Domain Name System.
        self.dbinstance_conn_type = dbinstance_conn_type
        # The node specifications. For more information, see the following documents:
        # 
        # - PolarDB for MySQL: [Compute node specifications](https://help.aliyun.com/document_detail/102542.html).
        # 
        # - PolarDB for PostgreSQL (Oracle Compatible): [Compute node specifications](https://help.aliyun.com/document_detail/207921.html).
        # 
        # - PolarDB for PostgreSQL: [Compute node specifications](https://help.aliyun.com/document_detail/209380.html).
        # 
        # This parameter is required.
        self.dbnode_class = dbnode_class
        # The database engine type. Valid values:
        # 
        # - **MySQL**
        # 
        # - **PostgreSQL**
        # 
        # - **Oracle**
        # 
        # This parameter is required.
        self.dbtype = dbtype
        # The version of the database engine.
        # 
        # - Valid values for MySQL:
        # 
        #   - **5.6**
        # 
        #   - **5.7**
        # 
        #   - **8.0**
        # 
        # - Valid values for PostgreSQL:
        # 
        #   - **11**
        # 
        #   - **14**
        # 
        # - Valid values for Oracle:
        # 
        #   - **11**
        # 
        #   - **14**
        # 
        # This parameter is required.
        self.dbversion = dbversion
        # Specifies whether to return the list of zones that support single-zone deployment. Valid values:
        # 
        # - **0** (default): The list is not returned.
        # 
        # - **1**: The list is returned.
        self.dispense_mode = dispense_mode
        # Specifies whether to create a MaxScale cluster. Valid values:
        # 
        # - **true** (default): A MaxScale cluster is created.
        # 
        # - **false**: A MaxScale cluster is not created.
        # 
        # This parameter is required.
        self.need_max_scale_link = need_max_scale_link
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID.
        # 
        # > Call the [DescribeRegions](https://help.aliyun.com/document_detail/98041.html) operation to query available regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The subdomain. A subdomain is a level below a top-level domain. For example, if the parent domain is \\`cn-beijing\\`, a valid subdomain is \\`cn-beijing-i-aliyun\\`.
        self.sub_domain = sub_domain
        # The zone ID.
        # 
        # > Call the [DescribeRegions](https://help.aliyun.com/document_detail/98041.html) operation to query the available zones.
        # 
        # This parameter is required.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_conn_type is not None:
            result['DBInstanceConnType'] = self.dbinstance_conn_type

        if self.dbnode_class is not None:
            result['DBNodeClass'] = self.dbnode_class

        if self.dbtype is not None:
            result['DBType'] = self.dbtype

        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion

        if self.dispense_mode is not None:
            result['DispenseMode'] = self.dispense_mode

        if self.need_max_scale_link is not None:
            result['NeedMaxScaleLink'] = self.need_max_scale_link

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.sub_domain is not None:
            result['SubDomain'] = self.sub_domain

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceConnType') is not None:
            self.dbinstance_conn_type = m.get('DBInstanceConnType')

        if m.get('DBNodeClass') is not None:
            self.dbnode_class = m.get('DBNodeClass')

        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')

        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')

        if m.get('DispenseMode') is not None:
            self.dispense_mode = m.get('DispenseMode')

        if m.get('NeedMaxScaleLink') is not None:
            self.need_max_scale_link = m.get('NeedMaxScaleLink')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SubDomain') is not None:
            self.sub_domain = m.get('SubDomain')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

