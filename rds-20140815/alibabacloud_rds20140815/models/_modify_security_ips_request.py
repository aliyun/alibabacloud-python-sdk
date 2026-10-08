# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifySecurityIpsRequest(DaraModel):
    def __init__(
        self,
        dbinstance_iparray_attribute: str = None,
        dbinstance_iparray_name: str = None,
        dbinstance_id: str = None,
        fresh_white_list_readins: str = None,
        modify_mode: str = None,
        resource_owner_id: int = None,
        security_iptype: str = None,
        security_ips: str = None,
        whitelist_network_type: str = None,
    ):
        # The attribute of the whitelist group.
        # 
        # - (Default) If you do not specify this parameter, the group is a common group.
        # - If you set this parameter to `hidden`, the group is a system default group used by services such as DMS, DTS, and DAS. These groups are not displayed in the console. Deleting or modifying these groups may prevent DMS, DTS, and DAS from accessing ApsaraDB RDS. Proceed with caution.
        self.dbinstance_iparray_attribute = dbinstance_iparray_attribute
        # The name of the whitelist group to modify. Default value: Default. If the specified group does not exist, a new group is automatically created.
        # 
        # >Each instance supports up to 200 whitelist groups.
        self.dbinstance_iparray_name = dbinstance_iparray_name
        # The target instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The list of read-only instances to which the whitelist is synchronized.
        # 
        # - This parameter is applicable only to ApsaraDB RDS for PostgreSQL instances that have read-only instances.
        # - Separate multiple read-only instances with commas (,).
        self.fresh_white_list_readins = fresh_white_list_readins
        # The modification mode. Valid values:
        # * **Cover** (default): overwrites the original IP whitelist with the value of the **SecurityIps** parameter.
        # * **Append**: appends the IP addresses specified in the **SecurityIps** parameter to the original IP whitelist.
        # * **Delete**: removes the IP addresses specified in the **SecurityIps** parameter from the original IP whitelist. At least one IP address must be retained.
        self.modify_mode = modify_mode
        self.resource_owner_id = resource_owner_id
        # The type of IP address. The value is fixed as IPv4. IPv6 is not supported.
        self.security_iptype = security_iptype
        # The IP whitelist. Before you modify the IP whitelist, call the [DescribeDBInstanceIPArrayList](https://help.aliyun.com/document_detail/610518.html) operation to query the existing IP whitelist information of the instance.
        # 
        # <details>
        # <summary>Configuration rules</summary>
        # 
        # - IP addresses (such as 10.23.XX.XX) and CIDR blocks (such as 10.23.XX.XX/24) are supported.
        # 
        # - Separate multiple IP addresses or CIDR blocks with commas (,). No spaces are allowed before or after the commas.
        # 
        # - Each instance can contain up to 1,000 IP addresses or CIDR blocks. If you have a large number of IP addresses, merge them into CIDR blocks, such as 10.23.XX.XX/24.
        # </details>
        # 
        # This parameter is required.
        self.security_ips = security_ips
        # The network type of the whitelist. Valid values:
        # 
        # * **MIX** (default): general mode.
        # * **Classic**: the classic network in enhanced whitelist mode.
        # * **VPC**: the virtual private cloud (VPC) in enhanced whitelist mode.
        # 
        # > * ApsaraDB RDS for PostgreSQL instances with cloud disks use only the general mode (MIX). If you set this parameter to another mode, the value is automatically converted to MIX.
        # > * Only ApsaraDB RDS for MySQL 5.1, 5.5, 5.6, and 5.7 instances with Premium Local SSDs and ApsaraDB RDS for PostgreSQL 9.4 and 10 instances with Premium Local SSDs support the enhanced whitelist mode.
        self.whitelist_network_type = whitelist_network_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_iparray_attribute is not None:
            result['DBInstanceIPArrayAttribute'] = self.dbinstance_iparray_attribute

        if self.dbinstance_iparray_name is not None:
            result['DBInstanceIPArrayName'] = self.dbinstance_iparray_name

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.fresh_white_list_readins is not None:
            result['FreshWhiteListReadins'] = self.fresh_white_list_readins

        if self.modify_mode is not None:
            result['ModifyMode'] = self.modify_mode

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.security_iptype is not None:
            result['SecurityIPType'] = self.security_iptype

        if self.security_ips is not None:
            result['SecurityIps'] = self.security_ips

        if self.whitelist_network_type is not None:
            result['WhitelistNetworkType'] = self.whitelist_network_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceIPArrayAttribute') is not None:
            self.dbinstance_iparray_attribute = m.get('DBInstanceIPArrayAttribute')

        if m.get('DBInstanceIPArrayName') is not None:
            self.dbinstance_iparray_name = m.get('DBInstanceIPArrayName')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('FreshWhiteListReadins') is not None:
            self.fresh_white_list_readins = m.get('FreshWhiteListReadins')

        if m.get('ModifyMode') is not None:
            self.modify_mode = m.get('ModifyMode')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityIPType') is not None:
            self.security_iptype = m.get('SecurityIPType')

        if m.get('SecurityIps') is not None:
            self.security_ips = m.get('SecurityIps')

        if m.get('WhitelistNetworkType') is not None:
            self.whitelist_network_type = m.get('WhitelistNetworkType')

        return self

