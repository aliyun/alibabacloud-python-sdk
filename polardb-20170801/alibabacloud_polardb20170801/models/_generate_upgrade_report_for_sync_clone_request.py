# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateUpgradeReportForSyncCloneRequest(DaraModel):
    def __init__(
        self,
        creation_category: str = None,
        creation_option: str = None,
        dbname: str = None,
        dbtype: str = None,
        dbversion: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        reserve: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        source_dbcluster_id: str = None,
    ):
        # The product series. Valid values:
        # 
        # - **Normal**: Cluster Edition (default)
        # 
        # - **SENormal**: Standard Edition
        # 
        # See [Product series](https://help.aliyun.com/document_detail/183258.html).
        self.creation_category = creation_category
        # The creation method. Valid values:
        # 
        # - **MigrationFromRDS**: Migrate data from an existing RDS instance to a new PolarDB cluster. The created PolarDB cluster is in read-only mode and has binary logging enabled by default. For operations in the console, see [Upgrade an ApsaraDB RDS for MySQL instance to PolarDB for MySQL](https://help.aliyun.com/document_detail/121582.html).
        # 
        # - **UpgradeFromPolarDB**: Upgrade and migrate data from a PolarDB cluster. See [Upgrade the major version](https://help.aliyun.com/document_detail/459712.html).
        self.creation_option = creation_option
        # The name of the database. You can specify only one database name.
        # 
        # > This parameter is supported only for PolarDB for PostgreSQL (Oracle Compatible) clusters.
        self.dbname = dbname
        # The type of the database engine. Valid values:
        # 
        # - **MySQL**
        # 
        # - **Oracle**
        self.dbtype = dbtype
        # The version of the destination database engine.
        # 
        # - Valid values for MySQL:
        # 
        #   - **5.6**
        # 
        #   - **5.7**
        # 
        #   - **8.0**
        # 
        # - Valid value for Oracle: **14**.
        self.dbversion = dbversion
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id
        # A reserved parameter in the JSON string format.
        self.reserve = reserve
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the source instance.
        self.source_dbcluster_id = source_dbcluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_category is not None:
            result['CreationCategory'] = self.creation_category

        if self.creation_option is not None:
            result['CreationOption'] = self.creation_option

        if self.dbname is not None:
            result['DBName'] = self.dbname

        if self.dbtype is not None:
            result['DBType'] = self.dbtype

        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.reserve is not None:
            result['Reserve'] = self.reserve

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.source_dbcluster_id is not None:
            result['SourceDBClusterId'] = self.source_dbcluster_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationCategory') is not None:
            self.creation_category = m.get('CreationCategory')

        if m.get('CreationOption') is not None:
            self.creation_option = m.get('CreationOption')

        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')

        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Reserve') is not None:
            self.reserve = m.get('Reserve')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SourceDBClusterId') is not None:
            self.source_dbcluster_id = m.get('SourceDBClusterId')

        return self

