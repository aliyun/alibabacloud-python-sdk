# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDBInstancesRequest(DaraModel):
    def __init__(
        self,
        category: str = None,
        client_token: str = None,
        connection_mode: str = None,
        connection_string: str = None,
        dbinstance_class: str = None,
        dbinstance_id: str = None,
        dbinstance_status: str = None,
        dbinstance_type: str = None,
        dedicated_host_group_id: str = None,
        dedicated_host_id: str = None,
        engine: str = None,
        engine_version: str = None,
        expired: str = None,
        filter: str = None,
        instance_level: int = None,
        instance_network_type: str = None,
        max_results: int = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        pay_type: str = None,
        query_auto_renewal: bool = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        search_key: str = None,
        tags: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
        proxy_id: str = None,
    ):
        # The RDS edition of the instance. Valid values:
        # 
        # *   **Basic**: RDS Basic Edition
        # *   **HighAvailability**: RDS High-availability Edition
        # *   **cluster**: RDS Cluster Edition
        # *   **serverless_basic**: RDS Serverless Basic Edition
        self.category = category
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The connection mode of the instance. Valid values:
        # 
        # *   **Standard**: standard mode
        # *   **Safe**: database proxy mode
        # 
        # By default, this operation queries the instances that use any of the supported connection modes.
        self.connection_mode = connection_mode
        # The endpoint of the instance. You must specify this parameter only when you want to query a single instance.
        self.connection_string = connection_string
        # The instance type of the instance. For information, see [Primary ApsaraDB RDS instance types](https://help.aliyun.com/document_detail/26312.html).
        self.dbinstance_class = dbinstance_class
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # The status of the instance. For more information, see [Instance states](https://help.aliyun.com/document_detail/26315.html).
        self.dbinstance_status = dbinstance_status
        # The role of the instance. Valid values:
        # 
        # *   **Primary**: primary instance
        # *   **Readonly**: read-only instance
        # *   **Guard**: disaster recovery instance
        # *   **Temp**: temporary instance
        # 
        # By default, this operation returns the instances that assume any of the supported roles.
        self.dbinstance_type = dbinstance_type
        # The dedicated cluster ID.
        self.dedicated_host_group_id = dedicated_host_group_id
        # The host ID of the instance in the dedicated cluster.
        self.dedicated_host_id = dedicated_host_id
        # The database engine of the instance. Valid values:
        # 
        # *   **MySQL**
        # *   **SQLServer**
        # *   **PostgreSQL**
        # *   **MariaDB**
        # 
        # By default, this operation returns the instances that run any of the supported database engines.
        self.engine = engine
        # The database engine version.
        self.engine_version = engine_version
        # Specifies whether the instances have expired. Valid values:
        # 
        # *   **True**
        # *   **False**
        self.expired = expired
        # The JSON string that consists of filter condition parameters and their values.
        self.filter = filter
        # Specifies whether to return the RDS edition of the instance by using the Category parameter. Valid values:
        # 
        # *   **0**: returns the RDS edition of the instance.
        # *   **1**: does not return the RDS edition of the instance.
        self.instance_level = instance_level
        # The network type of the instance. Valid values:
        # 
        # *   **VPC**
        # *   **Classic**
        # 
        # By default, this operation returns the instances that reside in any of the supported network types.
        self.instance_network_type = instance_network_type
        # The number of entries to return per page. Valid values: **1 to 100**.
        # 
        # Default value: **30**.
        # 
        # > If you specify this parameter, **PageSize** and **PageNumber** are unavailable.
        self.max_results = max_results
        # The token that is used to display the next page. You must set this parameter to the value that is returned from the most recent call of the **DescribeDBInstances** operation for **NextToken**. If the returned entries are displayed on multiple pages, the next page can be displayed when you call this operation again with this parameter specified.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number. Pages start from 1.
        # 
        # Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values: **1** to **100**.
        # 
        # Default value: **30**.
        self.page_size = page_size
        # The billing method of the instance. Valid values:
        # 
        # *   **Postpaid**: pay-as-you-go
        # *   **Prepaid**: subscription
        self.pay_type = pay_type
        self.query_auto_renewal = query_auto_renewal
        # The region ID. You can call the DescribeRegions operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The keyword that is used for fuzzy search. The keyword can be part of an instance ID or an instance description.
        self.search_key = search_key
        # The tag that is added to the instance. Each tag is a key-value pair that consists of two fields: TagKey and TagValue. You can specify a maximum of five tags in the following format for each request: {"key1":"value1","key2":"value2"...}.
        self.tags = tags
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The VPC ID.
        self.vpc_id = vpc_id
        # The zone ID of the instance.
        self.zone_id = zone_id
        # A deprecated parameter. You do not need to configure this parameter.
        self.proxy_id = proxy_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.connection_mode is not None:
            result['ConnectionMode'] = self.connection_mode

        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dbinstance_status is not None:
            result['DBInstanceStatus'] = self.dbinstance_status

        if self.dbinstance_type is not None:
            result['DBInstanceType'] = self.dbinstance_type

        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id

        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.expired is not None:
            result['Expired'] = self.expired

        if self.filter is not None:
            result['Filter'] = self.filter

        if self.instance_level is not None:
            result['InstanceLevel'] = self.instance_level

        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.query_auto_renewal is not None:
            result['QueryAutoRenewal'] = self.query_auto_renewal

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.search_key is not None:
            result['SearchKey'] = self.search_key

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        if self.proxy_id is not None:
            result['proxyId'] = self.proxy_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ConnectionMode') is not None:
            self.connection_mode = m.get('ConnectionMode')

        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBInstanceStatus') is not None:
            self.dbinstance_status = m.get('DBInstanceStatus')

        if m.get('DBInstanceType') is not None:
            self.dbinstance_type = m.get('DBInstanceType')

        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')

        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('Expired') is not None:
            self.expired = m.get('Expired')

        if m.get('Filter') is not None:
            self.filter = m.get('Filter')

        if m.get('InstanceLevel') is not None:
            self.instance_level = m.get('InstanceLevel')

        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('QueryAutoRenewal') is not None:
            self.query_auto_renewal = m.get('QueryAutoRenewal')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        if m.get('proxyId') is not None:
            self.proxy_id = m.get('proxyId')

        return self

