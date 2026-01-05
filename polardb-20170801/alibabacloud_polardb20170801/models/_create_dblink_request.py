# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDBLinkRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dbcluster_id: str = None,
        dblink_name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        source_dbname: str = None,
        target_dbaccount: str = None,
        target_dbinstance_name: str = None,
        target_dbname: str = None,
        target_dbpasswd: str = None,
        target_ip: str = None,
        target_port: str = None,
        vpc_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. The token is case-sensitive.
        self.client_token = client_token
        # The ID of the source cluster that the database link connects.
        # 
        # >  You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/173433.html) operation to query PolarDB clusters.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The name of the database link.
        # 
        # *   The name must contain lowercase letters and can also contain digits and underscores (_).
        # *   The name must start with a letter and end with a letter or digit.
        # *   The name must be 1 to 64 characters in length.
        # 
        # This parameter is required.
        self.dblink_name = dblink_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/98041.html) operation to query information about regions.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The name of the source database.
        # 
        # >  You can call the [DescribeDatabases](https://help.aliyun.com/document_detail/173558.html) operation to query information about databases in a PolarDB cluster.
        # 
        # This parameter is required.
        self.source_dbname = source_dbname
        # The account of the destination database.
        # 
        # >  You can call the [DescribeAccounts](https://help.aliyun.com/document_detail/173549.html) operation to query the account of a PolarDB cluster.
        # 
        # This parameter is required.
        self.target_dbaccount = target_dbaccount
        # The ID of the destination cluster that the database link connects.
        # 
        # > *   If the destination cluster is a user-created Oracle database on an ECS instance, set the value to `null`.
        # > *   You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/173433.html) operation to query PolarDB clusters.
        self.target_dbinstance_name = target_dbinstance_name
        # The name of the destination database.
        # 
        # >  You can call the [DescribeDatabases](https://help.aliyun.com/document_detail/173558.html) operation to query information about databases in a PolarDB cluster.
        # 
        # This parameter is required.
        self.target_dbname = target_dbname
        # The account password of the destination database.
        # 
        # This parameter is required.
        self.target_dbpasswd = target_dbpasswd
        # The IP address of the user-created Oracle database on an ECS instance.
        self.target_ip = target_ip
        # The port number of the user-created Oracle database on an ECS instance.
        self.target_port = target_port
        # The ID of the virtual private cloud (VPC).
        # 
        # >  You can call the [DescribeVpcs](https://help.aliyun.com/document_detail/35739.html) operation to query information about VPCs.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dblink_name is not None:
            result['DBLinkName'] = self.dblink_name

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

        if self.source_dbname is not None:
            result['SourceDBName'] = self.source_dbname

        if self.target_dbaccount is not None:
            result['TargetDBAccount'] = self.target_dbaccount

        if self.target_dbinstance_name is not None:
            result['TargetDBInstanceName'] = self.target_dbinstance_name

        if self.target_dbname is not None:
            result['TargetDBName'] = self.target_dbname

        if self.target_dbpasswd is not None:
            result['TargetDBPasswd'] = self.target_dbpasswd

        if self.target_ip is not None:
            result['TargetIp'] = self.target_ip

        if self.target_port is not None:
            result['TargetPort'] = self.target_port

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DBLinkName') is not None:
            self.dblink_name = m.get('DBLinkName')

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

        if m.get('SourceDBName') is not None:
            self.source_dbname = m.get('SourceDBName')

        if m.get('TargetDBAccount') is not None:
            self.target_dbaccount = m.get('TargetDBAccount')

        if m.get('TargetDBInstanceName') is not None:
            self.target_dbinstance_name = m.get('TargetDBInstanceName')

        if m.get('TargetDBName') is not None:
            self.target_dbname = m.get('TargetDBName')

        if m.get('TargetDBPasswd') is not None:
            self.target_dbpasswd = m.get('TargetDBPasswd')

        if m.get('TargetIp') is not None:
            self.target_ip = m.get('TargetIp')

        if m.get('TargetPort') is not None:
            self.target_port = m.get('TargetPort')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

